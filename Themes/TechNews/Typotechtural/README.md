# Typotechtural

The conram.it redesign: an adaptation of **Technews 3.2.0.0** by TidyCustoms for Publii. No fork and no template overrides; everything lives in Publii's own fields, so a theme update can't overwrite it.

Background: [Typotechtural, a new look for an old website](https://www.conram.it/typotechtural-a-new-look-for-an-old-website.html).

## Files and where they go

| File | Publii field | Version |
|---|---|---|
| `custom-css/custom-css.css` | Tools › Custom CSS | 1.64 |
| `custom-html/head.html` | Tools › Custom HTML › Head | 1.04 |
| `custom-html/body.html` | Tools › Custom HTML › Body | 1.04 |
| `custom-html/footer.html` | Tools › Custom HTML › Footer | 1.23 |
| `custom-html/copyright.html` | Theme Settings › Footer › Copyright text | 1.06 |
| `tools/fix_headings.py` | – (run against a site's `db.sqlite`, Publii closed) | – |

Each file is a complete field: replace the field's whole content. Head, Body and Copyright are written for conram.it (texts, links, menu labels, categories); treat them as a working example and adapt them to your own site.

## Requirements

- Publii 0.48 or later, Technews 3.2.0.0.
- The Footer scripts expect the conram.it category tags (Security, Compliance, Internet, ITSM, Career, Tech, Gaming); the list is in the core block (`window.TT`).

## Versioning

`1.xx`, one number per field, raised on every change. History in [CHANGELOG.md](CHANGELOG.md).

## Credits and licence

Rikard Malmborg, with Claude (Anthropic) and ChatGPT (OpenAI). Code: MIT (see the repository [LICENSE](../../../LICENSE)). Site content: all rights reserved. Technews and Publii belong to their authors.
