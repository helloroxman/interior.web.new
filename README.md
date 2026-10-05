# Oksana Ivanova — interior design studio website

Modern, fully static, bilingual (UA / EN) portfolio site. No build tools or frameworks are needed to host it — only HTML, CSS and vanilla JavaScript.

## Structure

```
New/
├── index.html              Ukrainian home page
├── en/index.html           English home page
├── projects/<slug>.html    Ukrainian project pages (37)
├── en/projects/<slug>.html English project pages (37)
├── 404.html                bilingual "not found" page
├── css/style.css           all styles
├── js/main.js              header, mobile menu, filters, reveal, counters, lightbox
├── img/                    logo, icons, favicons, optimized project images
├── files/sample_project.pdf
├── data/projects.json      project list: titles, areas, locations, types, descriptions, images
├── build.py                generator: data/projects.json → all HTML pages
└── .nojekyll               tells GitHub Pages to serve the folder as-is
```

## Editing content

All texts live in two places:

- `data/projects.json` — projects (title, area, type, location and description in both languages).
- `build.py` — the `T` dictionary holds every other string of the site (hero, services, process, contacts …).

After changing either file, regenerate the pages:

```bash
python3 build.py
```

Only Python 3 is required (no extra packages).

## Adding a project

1. Put the images in `img/projs/<slug>/` as `01.jpg`, `02.jpg`, … (max 2000 px) and `01-s.jpg`, `02-s.jpg`, … (max 900 px thumbnails), plus `cover.jpg` for the grid.
2. Add an entry to `data/projects.json` (copy an existing one; `w` and `h` are the pixel size of the full image, used to decide the gallery layout).
3. Run `python3 build.py`.

## Deploying to GitHub Pages

The site uses relative links, so it works from the repository root or from any sub-folder.

- **Whole repository = site:** copy the contents of `New/` to the repository root (or point Pages at the branch/folder that contains these files).
- **Custom domain:** add a `CNAME` file with the domain next to `index.html`.

Pages settings: *Settings → Pages → Deploy from a branch*, choose the branch and folder.

## Screenshots / static mode

Appending `?static` to any URL disables the scroll animations (handy for screenshots and automated tests).
