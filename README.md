forking the add-on to suit my needs, specifically:
- only generate single texture per material (using node tree to find albedo image)
- convert image.pixels to image string (primarly to add support for .dds ripped textures, which crash the game if used)
- refactor using my own python p3dxml mini-library
