import os
import re

def extract_existing_title(readme_path):
    """Extracts the title from an existing README.md if present."""
    if not os.path.exists(readme_path):
        return None
    try:
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
        # Matches title: "..." or title: ...
        match = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', content, re.MULTILINE)
        if match:
            return match.group(1).strip()
    except Exception as e:
        print(f"Error reading {readme_path}: {e}")
    return None

def find_svg_image(project_dir):
    """Finds the first SVG file in horizontal/color/."""
    color_dir = os.path.join(project_dir, "horizontal", "color")
    if not os.path.exists(color_dir):
        return None
    
    for file in os.listdir(color_dir):
        if file.lower().endswith(".svg"):
            # Normalize path slashes for cross-platform YAML compatibility
            return f"horizontal/color/{file}"
    return None

def update_readmes():
    current_dir = os.getcwd()
    print("Processing project directories...\n")

    for item in os.listdir(current_dir):
        project_dir = os.path.join(current_dir, item)

        # Process only directories (excluding hidden ones like .git)
        if not os.path.isdir(project_dir) or item.startswith("."):
            continue

        svg_path = find_svg_image(project_dir)
        if not svg_path:
            print(f"[{item}] Skipped (No .svg found in horizontal/color/)")
            continue

        readme_path = os.path.join(project_dir, "README.md")
        
        # Retain existing title or fallback to the folder name
        title = extract_existing_title(readme_path) or item
        safe_title = title.replace('"', '\\"')

        front_matter = f"""---
title: "{safe_title}"
featured_image: "{svg_path}"
---
"""
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(front_matter)

        print(f"[{item}] Updated README.md -> {svg_path}")

if __name__ == "__main__":
    update_readmes()
