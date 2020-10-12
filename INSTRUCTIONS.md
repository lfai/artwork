# How to add new project artwork

<project full name> is the display name for the project ( e.g. 'Elastic Deep Learning' )
<project name> is the name of the project in the filesystem ( e.g. 'elastic-deep-learning' )

1. Add a new directory under ```projects``` with the artwork. Artwork directory structure should map as follows...

```
<project name>
  - horizontal
    - color
      <project name>-horizontal-color.svg
      <project name>-horizontal-color.svg
    - white
      <project name>-horizontal-white.svg
      <project name>-horizontal-white.svg
    - black
      <project name>-horizontal-black.svg
      <project name>-horizontal-black.svg
  - stacked
    - color
      <project name>-stacked-color.svg
      <project name>-stacked-color.svg
    - white
      <project name>-stacked-white.svg
      <project name>-stacked-white.svg
    - black
      <project name>-stacked-black.svg
      <project name>-stacked-black.svg
  - icon
    - color
      <project name>-icon-color.svg
      <project name>-icon-color.svg
    - white
      <project name>-icon-white.svg
      <project name>-icon-white.svg
    - black
      <project name>-icon-black.svg
      <project name>-icon-black.svg
```

2. Create `README.md` under `<project name>` directory. Contents should match this typically...

```markdown
## <project full name>

*Note: GitHub Flavored Markdown used in the Readme doesn't support background colors. The white logos below are displayed on the light grey of tables.*

<table class="logos-table">
	<thead>
		<tr>
			<th></th>
			<th colspan="3">PNG</th>
			<th colspan="3">SVG</th>
		</tr>
		<tr>
			<th></th>
			<th>horizontal</th>
			<th>stacked</th>
			<th>icon</th>
			<th>horizontal</th>
			<th>stacked</th>
			<th>icon</th>
		</tr>
	</thead>	
    <tbody>
		<tr>
			<th>color</th>
			<td><a href="horizontal/color/<project name>-horizontal-color.png" download><img src="horizontal/color/amundsen-horizontal-color.png" width="200"></a></td>
			<td><a href="stacked/color/<project name>-stacked-color.png" download><img src="stacked/color/amundsen-stacked-color.png" width="95"></a></td>
			<td><a href="icon/color/<project name>-icon-color.png" download><img src="icon/color/amundsen-icon-color.png" width="75"></a></td>
			<td><a href="horizontal/color/<project name>-horizontal-color.svg" download><img src="horizontal/color/amundsen-horizontal-color.svg" width="200"></a></td>
			<td><a href="stacked/color/<project name>-stacked-color.svg" download><img src="stacked/color/amundsen-stacked-color.svg" width="95"></a></td>
			<td><a href="icon/color/<project name>-icon-color.png" download><img src="icon/color/amundsen-icon-color.png" width="75"></a></td>
		</tr>
		<tr>
			<th>white</th>
			<td><a href="horizontal/white/<project name>-horizontal-white.png" download><img src="horizontal/white/<project name>-horizontal-white.png" width="200"></a></td>
			<td><a href="stacked/white/<project name>-stacked-white.png" download><img src="stacked/white/<project name>-stacked-white.png" width="95"></a></td>
			<td><a href="icon/white/<project name>-icon-white.png" download><img src="icon/white/<project name>-icon-white.png" width="75"></a></td>
			<td><a href="horizontal/white/<project name>-horizontal-white.svg" download><img src="horizontal/white/<project name>-horizontal-white.svg" width="200"></a></td>
			<td><a href="stacked/white/<project name>-stacked-white.svg" download><img src="stacked/white/<project name>-stacked-white.svg" width="95"></a></td>
			<td><a href="icon/white/<project name>-icon-white.svg" download><img src="icon/white/<project name>-icon-white.svg" width="75"></a></td>
		</tr>
		<tr>
			<th>black</th>
			<td><a href="horizontal/black/<project name>-horizontal-black.png" download><img src="horizontal/black/<project name>-horizontal-black.png" width="200"></a></td>
			<td><a href="stacked/black/<project name>-stacked-black.png" download><img src="stacked/black/<project name>-stacked-black.png" width="95"></a></td>
			<td><a href="icon/black/<project name>-icon-black.png" download><img src="icon/black/<project name>-icon-black.png" width="75"></a></td>
			<td><a href="horizontal/black/<project name>-horizontal-black.svg" download><img src="horizontal/black/<project name>-horizontal-black.svg" width="200"></a></td>
			<td><a href="stacked/black/<project name>-stacked-black.svg" download><img src="stacked/black/<project name>-stacked-black.svg" width="95"></a></td>
			<td><a href="icon/black/<project name>-icon-black.svg" download><img src="icon/black/<project name>-icon-black.svg" width="75"></a></td>
		</tr>
	</tbody>	
</table>
```

3. Add project to `README.md` and `index.md` in root.

index.md
```markdown
# add under either 'Graduated Projects' or 'Incubating Projects' as appropriate in alphabetical order

<a href="projects/<project name>">
<div class="outer-wrapper">
<div class="imagesquare"><div class="imagecontainer"><img src="projects/<project name>/horizontal/color/<project name>-horizontal-color.svg"></div><div class="imagesquarecta">View Logos »</div></div>
</div>
</a>

```

README.md
```markdown
# add 'Projects' list in alphabetical order
- [<project full name>](projects/<project name>)
