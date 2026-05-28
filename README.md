# Zero to AI Engineering Astro Site

This Astro site was generated from the local `AI series` Markdown folder.

## Local Development

```bash
npm install
npm run dev
```

The current local URL uses the configured GitHub Pages base path:

```text
http://127.0.0.1:4321/Zero-to-AI-Engineering/
```

If Astro chooses another port, use the URL printed by the terminal.

## Build

```bash
npm run build
```

The static site is written to `dist/`.

## GitHub Pages Setup

1. Create a new GitHub repository named `Zero-to-AI-Engineering`.
2. Keep `site` set to `https://vinayanand3.github.io`.
3. Keep `base` set to `/Zero-to-AI-Engineering`.
4. Push this folder to the repository.
5. In GitHub, go to Settings, Pages, Build and deployment.
6. Set Source to `GitHub Actions`.
7. Push to `main`. The included workflow will build and deploy the site.

Your published URL will usually be:

```text
https://vinayanand3.github.io/Zero-to-AI-Engineering/
```

## Re-run Conversion

If you update the original Markdown files, run:

```bash
python3 convert_posts.py
npm run build
```

The converter overwrites generated files in `src/content/posts/` and leaves the original `AI series` folder unchanged.
