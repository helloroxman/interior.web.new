# Oksana Ivanova — interior design studio website

Modern, fully static, bilingual (UA / EN) portfolio site. No build tools or frameworks are needed to host it — only HTML, CSS and vanilla JavaScript.

## Structure

```
index.html, en/index.html             home pages (UA / EN)
projects/<slug>.html                  project pages (37 per language)
services/<slug>.html                  service pages: apartment, house, office & commercial, supervision
<slug>.html, en/<slug>.html           redirects from the old site's URLs to the new project pages
sample_project.pdf                    sample design album (kept at its old URL)
robots.txt, sitemap.xml               generated for search engines
404.html                              bilingual "not found" page
css/style.css, js/main.js             styles and scripts
fonts/                                self-hosted Inter (OFL licence)
img/projs/<slug>/                     NN.webp (≤2000 px), NN-s.webp (≤900 px), cover.webp, cover-s.webp, cover.jpg (link previews)
data/projects.json                    projects: title, area, type, location, description, photos with room labels
data/services.json                    service page texts and FAQ (UA / EN)
build.py                              generator: data → every HTML page, sitemap and robots
```

## SEO notes

- Every page has a canonical URL, `hreflang` links (uk, en, x-default) and Open Graph tags with absolute URLs on https://oksanaivanova.com.
- Structured data (JSON-LD): the studio as `ProfessionalService` on every page, `BreadcrumbList` and `CreativeWork` on projects, `Service` and `FAQPage` on service pages.
- Gallery `alt` texts come from the room labels in `data/projects.json` (`images[].label.uk/en`). Edit them there.
- Prices and timelines are deliberately not on the service pages. Add them in `data/services.json` when ready.

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

1. Put the images in `img/projs/<slug>/` as `01.webp`, `02.webp`, … (max 2000 px) and `01-s.webp`, … (max 900 px), plus `cover.webp` (1230 px), `cover-s.webp` (640 px) and `cover.jpg` for link previews.
2. Add an entry to `data/projects.json` (copy an existing one; `w` and `h` are the original pixel size, `label` describes the room in both languages).
3. Run `python3 build.py`.

## Deploying to GitHub Pages

The site uses relative links, so it works from the repository root or from any sub-folder.

- **Whole repository = site:** copy the contents of `New/` to the repository root (or point Pages at the branch/folder that contains these files).
- **Custom domain:** add a `CNAME` file with the domain next to `index.html`.

Pages settings: *Settings → Pages → Deploy from a branch*, choose the branch and folder.

## Screenshots / static mode

Appending `?static` to any URL disables the scroll animations (handy for screenshots and automated tests).
