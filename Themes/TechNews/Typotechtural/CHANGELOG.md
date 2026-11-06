# Changelog

One version number per Publii field, `1.xx`, raised on every change.

| Field | Current |
|---|---|
| Custom CSS | 1.61 |
| Custom HTML › Head | 1.03 |
| Custom HTML › Body | 1.04 |
| Custom HTML › Footer | 1.20 |
| Footer › Copyright text | 1.06 |

## 1.xx

**Head 1.03** (6 Nov 2026)
- AdSense publisher ID replaced with a placeholder; the version list removed from the header (each field carries its own number).

**Footer 1.20** (6 Nov 2026)
- Root links in Preview: the author panel's links and portrait are rewritten for Publii Preview's sub-folder, like the footer links. No effect on a live site at the root.

**CSS 1.61, Head 1.02, Body 1.04, Footer 1.19, Copyright 1.06** (6 Nov 2026)
- Credits and licence header (MIT for code, site content all rights reserved), contact as `dev [at] conram.it` so the e-mail obfuscation plugin leaves it alone.
- Change logs, dates and per-block credits moved out of the fields into this file. No functional change: CSS identical without comments, Footer scripts token-identical.

## Before 1.xx (26 Oct – 4 Nov 2026)

Development versions, condensed. CSS v29–v60, Footer rev. 15–18, Body v2–v3, Copyright v2–v5.1.

**Go-live** (4 Nov)
- Body v3: root-relative links in the author panel, so they work on tag and pagination pages.
- CSS v59–v60, Footer rev. 17–18: CV pages with a generated, collapsible two-level index; Master CV layout with the belt mark on section headings.

**Identity** (4 Nov)
- CSS v54: "going blue": sharp blue `#0070DC` for interaction, navy `#003466` menu and footer bands, gold kept for the wordmark dot and Career.
- CSS v55–v56: gutter art on wide screens (blueprint grid, circuit traces, belt construction lines).
- CSS v52–v53, Body v2: author panel footer row with a two-course brick strip.
- Copyright v3–v5.1: inline blue belt mark in the footer.

**Consolidation** (3–4 Nov)
- CSS v48–v51, v57: dead rules removed, Head CSS moved into Custom CSS, tag pages in one layer, category colours on one token pair.
- Footer rev. 15–16d: one shared script core (`window.TT`) for category list, site root, fetch cache, cards, tiles; category bar finds the Archive by address.

**Layout and print** (28 Oct – 3 Nov)
- CSS v29–v47: Previous/Next and pagination tiles, homepage author introduction, tag pages and tag index, featured image inside the text on Posts and Pages, right-aligned images wrap above 48rem, print hides cookie popup, banner and tiles.
