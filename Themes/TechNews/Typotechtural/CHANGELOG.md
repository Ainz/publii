# Changelog

One version number per Publii field, `1.xx`, raised on every change.

| Field | Current |
|---|---|
| Custom CSS | 1.71 |
| Custom HTML › Head | 1.04 |
| Custom HTML › Body | 1.04 |
| Custom HTML › Footer | 1.25 |
| Footer › Copyright text | 1.06 |

## 1.xx

**CSS 1.74** (25 Nov 2026)
- Images in text, floated (left or right, column at least 44rem): margins 1.775em above, 1.5em to the text side, 1em below (were 0 / 2.67rem / 2.67rem, stock). The image top now lines up with the first line of the text beside it instead of hanging one paragraph gap above it, and the text beside it gets more width. Checked on the compression post and the Vivaldi post.

**CSS 1.73** (25 Nov 2026)
- Images in text: left-aligned figures now float like right-aligned ones, mirrored (float left, 50% limit, stock margins swapped), when the reading column is at least 44rem. Below that, left-aligned figures stay blocks on the left, right-aligned on the right; phones are unchanged (full width, no float). Before, "Align left" in the editor always gave a centred block.

**Footer 1.27** (25 Nov 2026)
- Keyboard: a menu label with a dropdown (Publii "Text separator", `span.is-separator`, e.g. Info) gets `tabindex="0"` and `role="button"`, so Tab reaches it and the theme opens its dropdown as it does for links (WCAG 2.1.1). Before, Tab went from Archive straight to Contact and About, SiteLog and Imprint were only reachable in the footer bar.

**CSS 1.72, Footer 1.26** (25 Nov 2026)
- Menus: the Publii Footer menu sets the right-hand group and its order. A Footer-menu item named like a top-level Main-menu item moves that Main-menu item to the right with its dropdown (CV & Résumé, Info); other Footer-menu items are copied as links (Archive, Contact). Needed because the stock footer menu outputs no submenus. Without the script, CV & Résumé and Info stay at the end of the left group.
- Footer bar: flat; a label with a dropdown (Info) is replaced by its items, a link with a dropdown (CV & Résumé) stays one link. Right group gets the top bar's hairline and quieter weight; the hairline is dropped when the group wraps (below 64em).
- Top bar: dropdown parents in the right group, including a label without a link, follow the quieter weight and go full strength on hover, focus or when a child page is open. Section 7 comment corrected (block 6, not 7).

**CSS 1.71** (23 Nov 2026)
- New class `no-print`: hides any element in page content in print only. Used on the résumé pages for the role-fit paragraph, the Ways of working section and a repeated IAM education line.
- Résumé print: the track subtitle (`tt-track__sub`) is not printed (the H2 names the track).

**CSS 1.70** (23 Nov 2026)
- Résumé print (aim: one track on 3 A4 pages): the introduction (`tt-track-lead`) and the "Curriculum Vitae | Résumé" title line are not printed; bullets have no gap between them; the page title band prints at 16pt with no padding, and the portrait at 110px. Body line height, font size and screen layout unchanged.

**CSS 1.69** (18 Nov 2026)
- CV landing page: classes `cv-langs` (flag + Résumé | Curriculum rows) and `cv-updated` outside the CV layout, replacing long inline styles in the page. No visible change to the flag rows.

**CSS 1.68, Footer 1.25** (16 Nov 2026)
- Résumé tabs: on wide screens the whole navy section (tabs + INNEHÅLL) sticks to the top while scrolling, like the CV index bar. Stacked tabs (below 50em) do not stick.
- Direct links to a track or a heading land below the sticky bar (scroll margin); the focused track no longer draws a black box.

**CSS 1.67, Footer 1.24** (16 Nov 2026)
- Résumé pages: two or more `div.tt-track` (id + H2) become tabs (Footer block 10). Tab label from `data-tab`, else the H2. A hash naming a track or an element inside it opens that track; switching updates the hash. Without the script the tracks follow each other.
- Tab bar styled as the CV index bar (navy, Geist Mono 15px/600 caps, 37px, shadow); three equal tabs, centred text. Hover as the menu dropdowns (sharp-blue fill, white text), current = 3px light-blue rule, focus = Ivory ring. The theme's black `button:focus/:active` fill is overridden. Below 50em (phones, tablets upright): stacked tabs, rule on the left edge.
- INNEHÅLL (label from `data-toc`) hangs under the current tab and lists that track's H3s in a panel styled as the CV index panel; hover = the CV index bar's light-blue rule. Closes on choice, outside click or Esc.
- Print: the open track only, no tab bar.

**CSS 1.66** (9 Nov 2026)
- CV sub-headings (`.cv-doc h4`, e.g. "Teknisk miljö") lost to the content heading rule `.main.page .content__entry h4` (Exo, −0.025em tracking) and showed as squeezed, faded capitals. Specificity raised: Geist Mono labels in navy, full opacity, .8rem, more space above. Print 7.5pt → 8.5pt.
- Header "Code:" line points at this repository.

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
