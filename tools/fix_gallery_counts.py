#!/usr/bin/env python3
"""Recalcule les comptes de photos affichés dans la galerie (span.photo-count)."""
import re

path = "pages/galerie.html"
txt = open(path, encoding="utf-8").read()

# Vérification des comptes déclarés
blocks = re.findall(
    r"<h2>(.*?) <span class=\"photo-count\">(\d+) photos</span></h2>(.*?)(?=<h2>|$)",
    txt, re.S,
)
for name, declared, body in blocks:
    real = body.count('class="gallery-item"')
    flag = "OK" if int(declared) == real else "A CORRIGER"
    print(f"{name}: declare={declared} reel={real} -> {flag}")

# Correction automatique
out, pos = [], 0
for m in re.finditer(r"<h2>(.*?) <span class=\"photo-count\">\d+ photos</span></h2>", txt):
    start = m.end()
    nxt = re.search(r"<h2>", txt[start:])
    end = start + nxt.start() if nxt else len(txt)
    real = txt[start:end].count('class="gallery-item"')
    out.append(txt[pos:m.start()])
    out.append(f'<h2>{m.group(1)} <span class="photo-count">{real} photos</span></h2>')
    pos = start
out.append(txt[pos:])
open(path, "w", encoding="utf-8").write("".join(out))

print("\nNouveaux comptes :")
txt = open(path, encoding="utf-8").read()
for m in re.finditer(r"<h2>(.*?) <span class=\"photo-count\">(\d+) photos</span></h2>", txt):
    print(f"  {m.group(1)}: {m.group(2)}")
