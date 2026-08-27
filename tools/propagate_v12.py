#!/usr/bin/env python3
"""Propagation V1.2 sur toutes les pages CAPSAAA (remarques François 26/08) :
- libellés nav + footer renommés : Activités → Nos Activités, Inscriptions → Nous
  rejoindre, Partenaires → Nos Partenaires, Contact → Nous contacter
- titres h1 de page alignés sur les nouveaux libellés
- « Nos partenaires financiers » → « Nos partenaires »
"""

import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ["index.html"] + [os.path.join("pages", f) for f in sorted(os.listdir(os.path.join(ROOT, "pages"))) if f.endswith(".html")]

# (ancien, nouveau) — ciblés sur les liens (nav/footer) et titres h1
RENAMES = [
    (">Activités</a>", ">Nos Activités</a>"),
    (">Inscriptions</a>", ">Nous rejoindre</a>"),
    (">Partenaires</a>", ">Nos Partenaires</a>"),
    (">Contact</a>", ">Nous contacter</a>"),
]

H1_RENAMES = [
    ("<h1>Inscriptions 2025/2026</h1>", "<h1>Nous rejoindre</h1>"),
    ("<h1>Inscriptions 2026/2027</h1>", "<h1>Nous rejoindre</h1>"),
    ("<h1>Partenaires &amp; Liens utiles</h1>", "<h1>Nos Partenaires &amp; Liens utiles</h1>"),
    ("<h1>Partenaires & Liens utiles</h1>", "<h1>Nos Partenaires & Liens utiles</h1>"),
    ("<h2>Nos partenaires financiers</h2>", "<h2>Nos partenaires</h2>"),
]

total_changes = 0
for fname in FILES:
    path = os.path.join(ROOT, fname)
    with open(path, encoding="utf-8") as f:
        html = f.read()
    orig = html
    for old, new in RENAMES + H1_RENAMES:
        html = html.replace(old, new)
    if html != orig:
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        n = sum(orig.count(old) for old, _ in RENAMES + H1_RENAMES)
        total_changes += n
        print(f"{fname}: {n} remplacement(s)")
    else:
        print(f"{fname}: inchangé")

print(f"TOTAL: {total_changes} remplacements")
