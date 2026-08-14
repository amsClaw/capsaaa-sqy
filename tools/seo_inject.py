#!/usr/bin/env python3
"""CAPSAAA — Injection SEO dans le <head> des 9 pages.

Ajoute : keywords, robots, canonical, Open Graph, JSON-LD (NGO),
et la balise <script> du module de stats (js/stats.js).

Mots-clés validés avec l'association (retour 11/08/2026) :
« sport adapté handicap SQY », « association handisport Yvelines »,
« sport adapté handicap Saint-Quentin-en-Yvelines ».

Usage : python3 tools/seo_inject.py  (idempotent)
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE_URL = "https://cap-saaa-sqy.fr"

KEYWORDS = (
    "sport adapté handicap Saint-Quentin-en-Yvelines, "
    "association handisport Yvelines, sport adapté handicap SQY, "
    "sport handicap Trappes, sport adapté Yvelines, CAPSAAA, "
    "sport personnes handicapées, natation adaptée, équitation adaptée, "
    "multisports adaptés"
)

JSONLD = """  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "NGO",
    "name": "CAPSAAA — CAP Sport Art Aventure Amitié",
    "alternateName": "CAPSAAA",
    "description": "Association handisport à Saint-Quentin-en-Yvelines : activités sportives et loisirs adaptés aux personnes en situation de handicap depuis 1992.",
    "url": "https://cap-saaa-sqy.fr/",
    "telephone": "+33603414530",
    "email": "capaaasqy@hotmail.fr",
    "foundingDate": "1992",
    "areaServed": "Saint-Quentin-en-Yvelines",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "14 rue Mansart",
      "postalCode": "78190",
      "addressLocality": "Trappes",
      "addressRegion": "Île-de-France",
      "addressCountry": "FR"
    },
    "sameAs": ["https://www.cap-saaa-sqy.fr/"]
  }
  </script>"""

PAGES = ["index.html"] + [f"pages/{p.name}" for p in sorted((ROOT / "pages").glob("*.html"))]

for rel in PAGES:
    path = ROOT / rel
    html = path.read_text(encoding="utf-8")
    if "og:title" in html:
        print(f"skip (déjà injecté) : {rel}")
        continue

    title = re.search(r"<title>(.*?)</title>", html, re.S).group(1).strip()
    desc = re.search(r'name="description" content="(.*?)"', html).group(1)
    canonical = BASE_URL if rel == "index.html" else f"{BASE_URL}/{rel}"
    og_image = f"{BASE_URL}/assets/photos/atip2979.jpg"

    block = f"""  <meta name="keywords" content="{KEYWORDS}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{canonical}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="CAPSAAA — Sport adapté à Saint-Quentin-en-Yvelines">
  <meta property="og:locale" content="fr_FR">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{og_image}">
  <meta name="twitter:card" content="summary_large_image">"""

    # Insertion après la meta description existante
    html = re.sub(
        r'(<meta name="description" content=".*?">)',
        r"\1\n" + block,
        html,
        count=1,
    )
    # JSON-LD + script stats avant </head>
    stats_script = '<script src="js/stats.js" defer></script>' if rel == "index.html" else '<script src="../js/stats.js" defer></script>'
    html = html.replace("</head>", f"{JSONLD}\n  {stats_script}\n</head>", 1)
    path.write_text(html, encoding="utf-8")
    print(f"OK : {rel}")
