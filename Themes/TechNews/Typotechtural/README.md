# Typotechtural

The [conram.it](https://www.conram.it) redesign: an adaptation of the **Technews 3.2.0.0** theme for [Publii](https://getpublii.com). No fork and no template overrides. Everything lives in Publii's own Custom CSS and Custom HTML fields, so a theme update can't overwrite it, and removing the fields brings back stock Technews.

Background: [Typotechtural, a new look for an old website](https://www.conram.it/typotechtural-a-new-look-for-an-old-website.html).

## About Publii

[Publii](https://getpublii.com) is a free, open-source desktop CMS ([source on GitHub](https://github.com/GetPublii/Publii)) that builds static websites on your own computer and uploads the finished HTML to your server (FTP/SFTP, GitHub Pages, GitLab, S3 and more). There is no database or PHP on the server, which keeps hosting cheap and the attack surface small.

Useful documentation:

- [Tools](https://getpublii.com/docs/tools.html): Custom CSS, Custom HTML (Head, Body, Footer and theme-specific areas) and the File Manager, which is where these files go.
- [Theme Settings](https://getpublii.com/docs/theme-settings.html): includes the Footer › Copyright text field.
- [Installing, using and updating themes](https://getpublii.com/docs/installing-using-updating-themes.html)
- [Overriding a theme](https://getpublii.com/docs/overriding-publii-theme.html): the template route this adaptation deliberately avoids.
- [Website backups](https://getpublii.com/docs/website-backups.html): take one before pasting new fields.
- [Developer docs](https://getpublii.com/dev/) and the [community forum](https://forum.getpublii.com/).

## The theme

[Technews](https://marketplace.getpublii.com/themes/technews) is a free theme by the Publii team (TidyCustoms), from the [Publii Marketplace](https://marketplace.getpublii.com/themes/). It is not included here: install it from the Marketplace, then add these fields.

## Files and where they go

| File | Publii field | Version |
|---|---|---|
| `custom-css/custom-css.css` | Tools › Custom CSS | 1.66 |
| `custom-html/head.html` | Tools › Custom HTML › Head | 1.04 |
| `custom-html/body.html` | Tools › Custom HTML › Body | 1.04 |
| `custom-html/footer.html` | Tools › Custom HTML › Footer | 1.23 |
| `custom-html/copyright.html` | Theme Settings › Footer › Copyright text | 1.06 |

Each file is a complete field: replace the field's whole content, then regenerate the preview. Note that "Footer" appears twice in Publii: the scripts go in **Tools › Custom HTML › Footer**, the link columns in **Theme Settings › Footer › Copyright text**.

Head, Body and Copyright are written for conram.it (texts, links, menu labels); treat them as a working example and adapt them to your own site.

## Requirements

- Publii 0.48 or later, Technews 3.2.0.0.
- The Footer scripts expect one main tag per post as its category. The conram.it list (Security, Compliance, Internet, ITSM, Career, Tech, Gaming) is in the core block (`window.TT`); the matching colours are CSS tokens in the Custom CSS.

## Versioning

`1.xx`, one number per field, raised on every change. History in [CHANGELOG.md](CHANGELOG.md).

## Credits and licence

Rikard Malmborg, with Claude (Anthropic) and ChatGPT (OpenAI). Code: MIT (see the repository [LICENSE](../../../LICENSE)). Site content: all rights reserved. Technews and Publii belong to their authors and keep their own licences.
