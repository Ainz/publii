# Changelog

One version number per Publii field, `1.xx`, raised on every change.

| Field | Current |
|---|---|
| Custom CSS | 1.65 |
| Custom HTML › Head | 1.04 |
| Custom HTML › Body | 1.04 |
| Custom HTML › Footer | 1.23 |
| Footer › Copyright text | 1.06 |

## 1.xx

**CSS 1.65** (8 Nov 2026)
- Cookie badge (Publii GDPR): silver with an ebony icon instead of Publii's `#1089FF`; sharp blue with a white icon on hover/focus. 44px, 14px from the corner; phones (≤ 40em) 36px, 8px from the corner, 70% until touched, so it no longer covers text (audit D5).

**CSS 1.64, Footer 1.23** (7 Nov 2026)
- CV index, scrolling: the open panel no longer swallows the mouse wheel (`overscroll-behavior: contain` removed). A long list scrolls itself first, then the page. Footer: the panel closes once the page has scrolled a quarter of the window; a single wheel notch keeps it open. Reopening lands on the current entry.
- CV index, phones (≤ 40em): bar text 13px so the section name fits, entries 15px, tighter rows, 44px button column.
- CV index: no automatic hyphenation in index entries at any width (body text unchanged).

**CSS 1.63, Footer 1.22** (7 Nov 2026)
- CV index as a navy bar the width of the text column, sticky at the top: label · count (Geist Mono 15px, as the top menu), the section being read, and an arrow. The old compact Ivory button disappeared against the page.
- Panel: full bar width, entries 1rem (was .82), hover = sharp-blue text without fill; current entry and its section get a 3px sharp-blue rule, the entry in bold (was 2px with a 7% tint).
- Fold-out buttons: no fill; a hovered arrow and the open section's arrow are sharp blue.
- Arrows are drawn 13.3 × 10px triangles instead of font glyphs, so they rotate around their own centre (the glyph shifted a few px when turned).
- Footer script: the bar tracks the section being read on every scroll (it used to update only while open).

**CSS 1.62, Footer 1.21** (7 Nov 2026)
- Menu states, one system for the top bar, the footer bar and the dropdowns (visitor feedback: the current-page marker was too faint and the two Home links disagreed).
- Current page: 3px light-blue `#5AA9FF` rule, at the foot of the row in the bars (5.1:1 on navy) and on the left edge in dropdowns (6.1:1 on ebony). Was 2px sharp blue, 2.6:1.
- Parent of the current page (e.g. Projects on a project page) now gets the same rule, in the top bar and the footer bar. Previously no marker.
- Hover: light-blue text in the bars, no rule; in dropdowns a sharp-blue row with white text (4.8:1). Hover no longer looks like "current".
- Keyboard focus: Ivory ring everywhere (was light blue).
- Footer script: the front-page Home link is marked current in the top bar too (Publii doesn't flag it); current links get `aria-current="page"` in both bars.
- Not changed: the phone sidebar's markers.

**Head 1.04** (6 Nov 2026)
- AdSense script removed (AdSense not in use).

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
