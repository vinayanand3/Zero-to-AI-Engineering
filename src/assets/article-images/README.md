# Article Images

Put manually generated article images in this folder.

Use the article slug as the filename. Supported formats:

- `.png`
- `.jpg`
- `.jpeg`
- `.webp`
- `.avif`

Examples:

```text
01-from-zero-to-ai-engineering-why-im-starting-this-series.png
02-what-actually-is-artificial-intelligence-without-the-hype.png
03-how-do-machines-actually-learn-understanding-neural-networks-simply.webp
```

Recommended dimensions:

```text
1600 x 900
```

After adding images, run:

```bash
npm run build
git add src/assets/article-images
git commit -m "Add article images"
git push
```
