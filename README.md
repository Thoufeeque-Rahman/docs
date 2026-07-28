# Festie docs

This directory contains the Mintlify documentation site for Festie.

## Local preview

```bash
mint dev
```

## Validation

```bash
mint validate
mint broken-links
```

## Structure

- `docs.json` controls Mintlify navigation, branding, and site settings.
- `*.mdx` files contain documentation pages with YAML frontmatter.
- `base-content.txt` is the source transcript used for the first admin workflow documentation pass.

Use root-relative internal links without `.mdx` extensions.
