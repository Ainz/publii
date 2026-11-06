"""
fix_headings.py: tidy heading markup in a Publii site database (Typotechtural, 6 Nov 2026).

What it changes in the text of every post and page:
  1. <strong>/<b> inside a heading (h1-h6) is removed; the text stays.
  2. An <h1> in the content becomes <h2> (the title is the page's H1).
  3. A "heading" whose text is longer than 100 characters becomes a plain <p>
     (an opening paragraph formatted as a heading).

Usage (close Publii first):
  py fix_headings.py "C:\\Users\\<you>\\Documents\\Publii\\sites\\<site>\\input\\db.sqlite"           (dry run: shows changes)
  py fix_headings.py "...\\db.sqlite" --apply                                                        (backs up, then writes)

The backup is written next to the database as db.sqlite.bak-YYYYMMDD-HHMMSS.
"""
import re, sqlite3, shutil, sys, datetime, os

LONG = 100  # characters: longer "headings" are paragraphs

HEADING = re.compile(r'<(h[1-6])(\b[^>]*)>(.*?)</\1\s*>', re.I | re.S)
BOLD = re.compile(r'</?(?:strong|b)\b[^>]*>', re.I)
TAGS = re.compile(r'<[^>]+>')

def fix(html):
    notes = []
    def one(m):
        tag, attrs, inner = m.group(1).lower(), m.group(2), m.group(3)
        new_inner = BOLD.sub('', inner)
        text = re.sub(r'\s+', ' ', TAGS.sub('', new_inner)).strip()
        if new_inner != inner:
            notes.append(f'unbold {tag}: {text[:60]}')
        if len(text) > LONG:
            notes.append(f'{tag} -> p (long): {text[:60]}')
            attrs = re.sub(r'\s+id="mcetoc_[^"]*"', '', attrs)
            return f'<p{attrs}>{new_inner}</p>'
        if tag == 'h1':
            notes.append(f'h1 -> h2: {text[:60]}')
            tag = 'h2'
        return f'<{tag}{attrs}>{new_inner}</{tag}>'
    return HEADING.sub(one, html), notes

def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    db, apply = sys.argv[1], '--apply' in sys.argv
    if not os.path.isfile(db):
        sys.exit(f'Not found: {db}')
    con = sqlite3.connect(db)
    cols = [r[1] for r in con.execute('PRAGMA table_info(posts)')]
    if not {'id', 'title', 'text'} <= set(cols):
        sys.exit(f'Unexpected database layout (posts columns: {cols}); nothing changed.')
    rows = con.execute('SELECT id, title, text FROM posts').fetchall()
    changes = []
    for pid, title, text in rows:
        if not text:
            continue
        new, notes = fix(text)
        if new != text:
            changes.append((pid, title, new, notes))
    for pid, title, _, notes in changes:
        print(f'\n[{pid}] {title}')
        for n in notes:
            print('   ', n)
    print(f'\n{len(changes)} of {len(rows)} posts/pages would change.')
    if not apply:
        print('Dry run: nothing written. Add --apply to write (a backup is made first).')
        return
    con.close()
    stamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    backup = f'{db}.bak-{stamp}'
    shutil.copy2(db, backup)
    con = sqlite3.connect(db)
    with con:
        for pid, _, new, _ in changes:
            con.execute('UPDATE posts SET text = ? WHERE id = ?', (new, pid))
    con.close()
    print(f'Written. Backup: {backup}')
    print('Open Publii and regenerate the preview (or sync) to see the result.')

if __name__ == '__main__':
    main()
