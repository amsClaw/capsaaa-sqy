#!/usr/bin/env python3
"""Propagation V1.1 sur toutes les pages CAPSAAA :
- lien nav + footer "Actualités"
- widget traducteur (translate-box + script Google Translate)"""

import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ["index.html"] + [os.path.join("pages", f) for f in sorted(os.listdir(os.path.join(ROOT, "pages"))) if f.endswith(".html")]

TRANSLATE_SCRIPTS = """  <!-- Traducteur automatique (pt/ar prioritaire, en secondaire) -->
  <script type="text/javascript">
    function googleTranslateElementInit() {
      new google.translate.TranslateElement({
        pageLanguage: 'fr',
        includedLanguages: 'fr,pt,ar,en',
        layout: google.translate.TranslateElement.InlineLayout.SIMPLE
      }, 'google_translate_element');
    }
  </script>
  <script type="text/javascript" src="https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>

"""

def patch_nav(html, prefix):
    """Ajoute le lien Actualités dans la nav, après Activités."""
    if "actualites.html" in html:
        return html, False
    # nav: ligne Activités
    act_li = f'<li><a href="{prefix}activites.html">Activités</a></li>'
    news_li = f'<li><a href="{prefix}actualites.html">Actualités</a></li>'
    if act_li in html:
        html = html.replace(act_li, act_li + "\n        " + news_li, 1)
        return html, True
    return html, False

def patch_footer(html, prefix):
    """Ajoute le lien Actualités dans le footer (bloc 'Liens rapides'), après Activités."""
    news_f = f'<li><a href="{prefix}actualites.html">Actualités</a></li>'
    marker = '<h4>Liens rapides</h4>'
    if marker not in html:
        return html, False
    head, tail = html.split(marker, 1)
    if news_f in tail.split('</ul>', 1)[0]:
        return html, False  # déjà présent dans le footer
    act_f = f'<li><a href="{prefix}activites.html">Activités</a></li>'
    if act_f in tail:
        tail = tail.replace(act_f, act_f + "\n            " + news_f, 1)
        return head + marker + tail, True
    return html, False

def patch_translate(html):
    """Ajoute le div translate-box avant le nav-toggle et les scripts avant script.js."""
    if "google_translate_element" in html:
        return html, False
    changed = False
    # 1. div dans la navbar
    if '<div class="translate-box"' not in html:
        m = re.search(r'(<button class="nav-toggle" aria-label="Menu">)', html)
        if m:
            html = html.replace(m.group(1), '      <div class="translate-box" id="google_translate_element"></div>\n      ' + m.group(1), 1)
            changed = True
    # 2. scripts avant js/script.js
    for pat in [r'(<script src="\.\./js/script\.js"></script>)', r'(<script src="js/script\.js"></script>)']:
        m = re.search(pat, html)
        if m:
            html = html.replace(m.group(1), TRANSLATE_SCRIPTS + m.group(1), 1)
            changed = True
            break
    return html, changed

for f in FILES:
    path = os.path.join(ROOT, f)
    with open(path, "r", encoding="utf-8") as fh:
        html = fh.read()
    prefix = "" if f.startswith("pages/") else "pages/"
    orig = html
    html, c1 = patch_nav(html, prefix)
    html, c2 = patch_footer(html, prefix)
    html, c3 = patch_translate(html)
    if html != orig:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(html)
        print(f"  [MAJ] {f}  (nav={c1}, footer={c2}, translate={c3})")
    else:
        print(f"  [---] {f}  inchangé")
