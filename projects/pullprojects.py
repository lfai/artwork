import json
import os
import re
import urllib.error
import urllib.parse
import urllib.request

API_URL = (
    "https://api-gw.platform.linuxfoundation.org/project-service/v1/public/projects"
    "?$filter=parentSlug%20eq%20lf-ai-foundation&pageSize=2000&orderBy=name"
)

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

IMAGE_EXTENSIONS = {".svg", ".png", ".jpg", ".jpeg", ".webp", ".gif", ".ico", ".avif"}

def sanitize_folder_name(name):
    """Remove invalid filesystem characters from directory names."""
    return re.sub(r'[\\/*?:"<>|]', "", name)

def fetch_json(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))

def download_file(url, destination_path):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=15) as response:
        with open(destination_path, "wb") as f:
            f.write(response.read())

def extract_projects_list(data):
    """Dynamically locates the list of projects within the response JSON."""
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        for key in ["projects", "Projects", "data", "Data", "items", "rows", "results"]:
            if key in data and isinstance(data[key], list):
                return data[key]
        for value in data.values():
            if isinstance(value, list):
                return value
    return []

def find_existing_image(project_dir):
    """Checks if any image exists in the directory tree and returns its relative path."""
    if not os.path.exists(project_dir):
        return None
    for root, _, files in os.walk(project_dir):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in IMAGE_EXTENSIONS:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, project_dir)
                return rel_path.replace("\\", "/")  # Normalize for cross-platform YAML
    return None

def download_logos_and_create_readme():
    print(f"Fetching projects from API...\nURL: {API_URL}")
    try:
        data = fetch_json(API_URL)
    except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError) as e:
        print(f"Error fetching data from API: {e}")
        return

    projects = extract_projects_list(data)

    if not projects:
        print("\nNo projects found.")
        return

    print(f"Found {len(projects)} projects. Processing...\n")

    for project in projects:
        if not isinstance(project, dict):
            continue

        name = project.get("name") or project.get("Name") or "Untitled Project"
        slug = project.get("slug") or project.get("Slug") or project.get("projectSlug")
        
        if not slug:
            print(f"Skipping project (no slug found): {name}")
            continue

        project_dir = sanitize_folder_name(slug)
        os.makedirs(project_dir, exist_ok=True)

        # Check if an image already exists in the folder
        existing_image = find_existing_image(project_dir)

        if existing_image:
            print(f"[{project_dir}] Image already exists ({existing_image}). Skipping download.")
            featured_image_path = existing_image
        else:
            # Get logo URL from API payload
            logo_url = (
                project.get("logo") or 
                project.get("logoUrl") or 
                project.get("logoURL") or
                (project.get("logos", [{}])[0].get("url") if isinstance(project.get("logos"), list) and project.get("logos") else None)
            )

            featured_image_path = ""

            if logo_url:
                parsed_path = logo_url.split("?")[0]
                ext = os.path.splitext(parsed_path)[1].lower()
                if not ext or len(ext) > 5:
                    ext = ".svg"  # Default extension if undetermined

                # Construct target path: SLUG/horizontal/color/SLUG-horizontal-color.svg
                target_dir = os.path.join(project_dir, "horizontal", "color")
                os.makedirs(target_dir, exist_ok=True)

                filename = f"{slug}-horizontal-color{ext}"
                target_file_path = os.path.join(target_dir, filename)

                try:
                    download_file(logo_url, target_file_path)
                    featured_image_path = f"horizontal/color/{filename}"
                    print(f"[{project_dir}] Saved logo -> {featured_image_path}")
                except Exception as e:
                    print(f"[{project_dir}] Failed to download logo: {e}")
            else:
                print(f"[{project_dir}] No logo URL available.")

        # Create/Update README.md
        readme_path = os.path.join(project_dir, "README.md")
        safe_title = name.replace('"', '\\"')

        front_matter = f"""---
title: "{safe_title}"
featured_image: "{featured_image_path}"
---
"""
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(front_matter)

        print(f"[{project_dir}] Created/Updated README.md")

if __name__ == "__main__":
    download_logos_and_create_readme()
