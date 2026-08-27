#!/usr/bin/env python3
"""Générateur des 5 pages activités détaillées CAPSAAA (V1.2, remarques François 26/08).
Chaque activité a sa page : héros coloré, déroulement, infos pratiques (lieu/horaires/
public/encadrement), bénéfices, photos, emplacements témoignages (à compléter par
l'association). Relancer après modification des données ci-dessous.
"""

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = os.path.join(ROOT, "pages")

ACTIVITES = [
    {
        "slug": "aquatique",
        "titre": "Activités aquatiques",
        "cls": "act-piscine",
        "emoji": "🏊",
        "sous_titre": "Détente et plaisir dans l'eau, à son rythme",
        "accroche": "Sous la surveillance de 2 maîtres nageurs, chacun vit sa propre expérience : se détendre, jouer et nager à son rythme, dans une eau accueillante. Ce n'est pas un cours de natation : c'est un moment de liberté et de bien-être.",
        "desc": [
            "Chaque séance se déroule dans une ambiance conviviale et sécurisée. Les pratiquants non autonomes sont accompagnés par un adulte valide (famille ou bénévole).",
            "Un fauteuil de mise à l'eau permet aux personnes à mobilité réduite d'accéder au bassin en toute sécurité. L'eau est un milieu idéal pour travailler la motricité en douceur, sans contrainte de poids.",
        ],
        "benefices": [
            "Se détendre et évacuer le stress dans un cadre ludique",
            "Travailler la motricité et l'équilibre en douceur",
            "Gagner confiance en soi et en ses capacités",
            "Partager un moment convivial entre adhérents",
        ],
        "lieu": "Piscine Monquaut — Trappes",
        "lieu_url": "https://www.google.com/maps/search/?api=1&query=Piscine+Monquaut+Trappes",
        "horaires": "Créneaux de la saison — nous contacter pour le planning",
        "public": "Dès 5 ans — tous types de handicap (visible ou non)",
        "encadrement": "2 maîtres nageurs + bénévoles",
        "photo_hero": "cbrh0506.jpg",
        "photos": ["qmfi8712.jpg", "photo-2023-06-26-23-16-59.jpg", "photo-2023-06-26-23-16-60.jpg"],
    },
    {
        "slug": "equitation",
        "titre": "Équitation adaptée",
        "cls": "act-equitation",
        "emoji": "🐴",
        "sous_titre": "Le lien avec l'animal, la confiance en soi",
        "accroche": "Selon leur taille, leur âge et leurs capacités, les cavaliers montent un cheval, un double poney ou un shetland. Une activité qui développe l'équilibre, la confiance et le lien avec l'animal.",
        "desc": [
            "Les séances sont encadrées par un instructeur d'équitation. Chaque participant apprend à soigner son animal — brosser, curer les pieds, seller et brider — puis à monter et diriger sa monture.",
            "Des accompagnants bénévoles assistent les cavaliers tout au long de la séance, du pansage à la monte. Un groupe limité à 7 cavaliers pour un accompagnement de qualité.",
        ],
        "benefices": [
            "Développer l'équilibre et la posture grâce au mouvement du cheval",
            "Créer un lien unique avec l'animal, source de confiance",
            "Apprendre l'autonomie : soins, harnachement, monte",
            "Partager une activité valorisante entre cavaliers",
        ],
        "lieu": "Club SQY Équitation — Île aux Loisirs (SQY)",
        "lieu_url": "https://www.google.com/maps/search/?api=1&query=Club+SQY+%C3%89quitation+%C3%8Ele+aux+Loisirs+Saint-Quentin-en-Yvelines",
        "horaires": "Créneaux de la saison — nous contacter pour le planning",
        "public": "À partir de 6 ans — tous types de handicap",
        "encadrement": "Instructeur d'équitation + bénévoles (7 cavaliers max)",
        "photo_hero": "pveh1252.jpg",
        "photos": ["equitation.jpg", "diego-sur-plume.jpg", "imzd6900.jpg"],
    },
    {
        "slug": "musculation",
        "titre": "Musculation",
        "cls": "act-musculation",
        "emoji": "💪",
        "sous_titre": "Force, endurance et dépassement de soi",
        "accroche": "Sous la surveillance d'un éducateur sportif, les séances commencent par des exercices individualisés puis se poursuivent en collectif : zumba, aérobic, cardio-boxing, fitness… Elles se terminent toujours par des étirements.",
        "desc": [
            "Chaque séance est adaptée au niveau et aux capacités de chacun : on progresse à son rythme, sans comparaison ni pression.",
            "Des Motomed sont mis à disposition pour la musculation des bras et des jambes des personnes en situation de handicap moteur. Le matériel est accessible et sécurisé.",
        ],
        "benefices": [
            "Gagner en force, en endurance et en tonicité",
            "Entretenir sa santé cardiovasculaire",
            "Renforcer sa musculature avec un accompagnement adapté",
            "Se dépasser dans une ambiance motivante et bienveillante",
        ],
        "lieu": "Gymnase Aviation — Guyancourt",
        "lieu_url": "https://www.google.com/maps/search/?api=1&query=Gymnase+Aviation+Guyancourt",
        "horaires": "Créneaux de la saison — nous contacter pour le planning",
        "public": "À partir de 16 ans — tous types de handicap",
        "encadrement": "Éducateur sportif diplômé",
        "photo_hero": "les-bras.jpg",
        "photos": ["abdoss1.jpg", "pere-et-fils1.jpg", "uxio7452.jpg"],
    },
    {
        "slug": "fitness",
        "titre": "Fitness",
        "cls": "act-fitness",
        "emoji": "🤸",
        "sous_titre": "Bouger en musique, pour le plaisir et la santé",
        "accroche": "Un programme varié, différent chaque semaine : zumba, drumfit, pilates, step fitness, stretching et relaxation, renforcement musculaire… Le fitness CAPSAAA, c'est du sport-santé avant tout.",
        "desc": [
            "Les séances sont rythmées par la musique et s'adaptent à tous les niveaux : chacun participe à son allure, assis ou debout selon ses possibilités.",
            "Dans une démarche de sport-santé, cette activité accueille notamment les personnes disposant d'une prescription médicale. Elle favorise la remise en forme, la prévention et le maintien de la santé par le mouvement.",
        ],
        "benefices": [
            "Se remettre en forme progressivement et durablement",
            "Améliorer sa condition physique et sa souplesse",
            "Prévenir les effets de la sédentarité (prescription médicale bienvenue)",
            "Se défouler en musique dans la bonne humeur",
        ],
        "lieu": "Salle Auguste-Renoir — Guyancourt",
        "lieu_url": "https://www.google.com/maps/search/?api=1&query=Salle+Auguste-Renoir+Guyancourt",
        "horaires": "Créneaux de la saison — nous contacter pour le planning",
        "public": "À partir de 16 ans — tous types de handicap, sport-santé",
        "encadrement": "Éducateur sportif diplômé",
        "photo_hero": "etirements.jpg",
        "photos": ["exmf9076.jpg", "qbia3436.jpg", "img-5562.jpg"],
    },
    {
        "slug": "multisport",
        "titre": "Multi-Sports",
        "cls": "act-multisport",
        "emoji": "🎯",
        "sous_titre": "Découvrir plein de disciplines, en s'amusant",
        "accroche": "En fonction des souhaits et des capacités de chacun, des jeux sont proposés : boccia, badminton, tennis de table, jeux de ballons, tir à l'arc… Une activité variée et ludique pour découvrir ou redécouvrir le sport.",
        "desc": [
            "Chaque séance est l'occasion d'essayer une discipline différente, seule ou en équipe, dans une ambiance conviviale.",
            "La boccia, sport de précision inscrit aux Jeux Paralympiques, est l'un des temps forts de l'année : elle développe la concentration et la stratégie tout en restant accessible à tous.",
        ],
        "benefices": [
            "Découvrir de nombreuses disciplines sportives",
            "Travailler la coordination, la précision et la concentration",
            "Jouer en équipe et renforcer les liens entre adhérents",
            "S'amuser ! Le sport est d'abord un plaisir",
        ],
        "lieu": "Gymnase Aviation — Guyancourt",
        "lieu_url": "https://www.google.com/maps/search/?api=1&query=Gymnase+Aviation+Guyancourt",
        "horaires": "Créneaux de la saison — nous contacter pour le planning",
        "public": "À partir de 15 ans — tous types de handicap",
        "encadrement": "Éducateur sportif diplômé",
        "photo_hero": "hexg8906-1.jpg",
        "photos": ["sebastien-et-son-papa-1.jpg", "mariette-alexandre-dominique-2.jpg", "on-se-prepare-a-jouer.jpg"],
    },
]

NAV_ACTIVE = '        <li><a href="activites.html" class="active">Nos Activités</a></li>'

def nav_items():
    return """        <li><a href="../index.html">Accueil</a></li>
        <li><a href="qui-sommes-nous.html">Qui sommes-nous ?</a></li>
""" + NAV_ACTIVE + """
        <li><a href="actualites.html">Actualités</a></li>
        <li><a href="sensibilisations.html">Sensibilisations</a></li>
        <li><a href="galerie.html">Galerie</a></li>
        <li><a href="inscriptions.html">Nous rejoindre</a></li>
        <li><a href="partenaires.html">Nos Partenaires</a></li>
        <li><a href="contact.html">Nous contacter</a></li>"""

def page(act):
    photos = "\n".join(
        f'            <img src="../assets/photos/{p}" alt="{act["titre"]} — photo CAPSAAA" loading="lazy" '
        f'onerror="this.parentElement.style.display=\'none\'" style="width:100%;height:220px;object-fit:cover;border-radius:var(--radius-sm)">'
        for p in act["photos"]
    )
    benefices = "\n".join(f"          <li>{b}</li>" for b in act["benefices"])
    desc = "\n".join(f"          <p>{d}</p>" for d in act["desc"])
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{act['titre']} — CAPSAAA SQY</title>
  <meta name="description" content="{act['titre']} adaptée aux personnes en situation de handicap à Saint-Quentin-en-Yvelines — {act['lieu']}. Encadrement par des éducateurs sportifs diplômés, tous handicaps accueillis.">
  <meta name="keywords" content="sport adapté handicap Saint-Quentin-en-Yvelines, association handisport Yvelines, sport adapté handicap SQY, CAPSAAA, {act['titre'].lower()}, sport personnes handicapées">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://cap-saaa-sqy.fr/pages/activite-{act['slug']}.html">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="CAPSAAA — Sport adapté à Saint-Quentin-en-Yvelines">
  <meta property="og:locale" content="fr_FR">
  <meta property="og:title" content="{act['titre']} — CAPSAAA SQY">
  <meta property="og:description" content="{act['accroche']}">
  <meta property="og:url" content="https://cap-saaa-sqy.fr/pages/activite-{act['slug']}.html">
  <meta property="og:image" content="https://cap-saaa-sqy.fr/assets/photos/{act['photo_hero']}">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../css/style.css">
  <link rel="icon" href="../assets/photos/logo-capsaaa-02.jpg">
  <script src="../js/stats.js" defer></script>
</head>
<body>

  <!-- ===== HEADER ===== -->
  <header class="site-header">
    <nav class="navbar container">
      <a href="../index.html" class="navbar-brand">
        <img src="../assets/photos/logo-capsaaa-copie.png" alt="CAPSAAA Logo" onerror="this.style.display='none'">
        <span>CAPSAAA <span class="brand-sub">Saint-Quentin-en-Yvelines</span></span>
      </a>
            <div class="translate-box">
              <select class="lang-select" aria-label="Choisir la langue" onchange="setPageLanguage(this.value)">
                <option value="">🌐 Langue</option>
                <option value="fr">Français</option>
                <option value="pt">Português</option>
                <option value="ar">العربية</option>
                <option value="en">English</option>
              </select>
            </div>
            <div id="google_translate_element" style="display:none"></div>
      <button class="nav-toggle" aria-label="Menu">
        <span></span><span></span><span></span>
      </button>
      <ul class="nav-menu">
{nav_items()}
      </ul>
    </nav>
  </header>

  <!-- ===== PAGE HEADER ===== -->
  <div class="page-header">
    <div class="container">
      <h1>{act['titre']}</h1>
      <p>{act['sous_titre']}</p>
    </div>
  </div>

  <!-- ===== CONTENT ===== -->
  <section class="content-page">
    <div class="container">

      <div class="activity-page-hero {act['cls']}">
        <div>
          <h2>{act['emoji']} {act['sous_titre']}</h2>
          <p>{act['accroche']}</p>
        </div>
      </div>

      <div class="activity-detail {act['cls']}">
        <div class="activity-detail-img">
          <img src="../assets/photos/{act['photo_hero']}" alt="{act['titre']} — photo CAPSAAA" loading="lazy" onerror="this.parentElement.innerHTML='<div style=\\'background:var(--color-primary-light);height:250px;display:flex;align-items:center;justify-content:center;font-size:3rem\\'>{act['emoji']}</div>'">
        </div>
        <div class="activity-detail-info">
          <h3>Le déroulement des séances</h3>
{desc}
          <h3>Les bénéfices de cette activité</h3>
          <ul class="benefits-list">
{benefices}
          </ul>
        </div>
      </div>

      <!-- Infos pratiques -->
      <div class="activity-practice">
        <div class="practice-item">
          <div class="practice-icon">📍</div>
          <h4>Lieu</h4>
          <p>{act['lieu']}<br><a href="{act['lieu_url']}" target="_blank" rel="noopener">Voir sur la carte →</a></p>
        </div>
        <div class="practice-item">
          <div class="practice-icon">🕐</div>
          <h4>Horaires</h4>
          <p>{act['horaires']}</p>
        </div>
        <div class="practice-item">
          <div class="practice-icon">👥</div>
          <h4>Public</h4>
          <p>{act['public']}</p>
        </div>
        <div class="practice-item">
          <div class="practice-icon">🎓</div>
          <h4>Encadrement</h4>
          <p>{act['encadrement']}</p>
        </div>
      </div>

      <!-- Photos -->
      <h2>En images</h2>
      <div class="activity-practice">
{photos}
      </div>

      <!-- Témoignages (emplacements réservés — à compléter par l'association) -->
      <h2>Témoignages</h2>
      <div class="testimonials-grid">
        <div class="testimonial-card">
          <div class="quote">"</div>
          <p>« Ici le témoignage d'un participant sera publié. »</p>
          <div class="author">Un participant</div>
          <div class="role">{act['titre']}</div>
        </div>
        <div class="testimonial-card">
          <div class="quote">"</div>
          <p>« Ici le témoignage d'un animateur sera publié. »</p>
          <div class="author">Un animateur</div>
          <div class="role">{act['titre']}</div>
        </div>
      </div>
      <!-- NOTE ASSOCIATION : emplacements réservés aux témoignages réels (participants,
           familles, animateurs). Transmettre les textes à l'équipe CAPSAAA qui les publiera
           ici — demandé par l'association dans l'analyse du 26/08/2026. -->

      <p style="margin-top:28px;text-align:center">
        <a href="activites.html" class="btn btn-outline">← Toutes nos activités</a>
        <a href="contact.html" class="btn btn-primary" style="margin-left:12px">Nous contacter</a>
      </p>

    </div>
  </section>

  <!-- ===== FOOTER ===== -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <h3>CAPSAAA SQY</h3>
          <p>Cap sur le Sport, l'Art, l'Aventure et l'Amitié. Association loi 1901 d'intérêt général.</p>
        </div>
        <div class="footer-col">
          <h4>Liens rapides</h4>
          <ul>
            <li><a href="../index.html">Accueil</a></li>
            <li><a href="activites.html">Nos Activités</a></li>
            <li><a href="actualites.html">Actualités</a></li>
            <li><a href="inscriptions.html">Nous rejoindre</a></li>
            <li><a href="galerie.html">Galerie photos</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>L'association</h4>
          <ul>
            <li><a href="qui-sommes-nous.html">Qui sommes-nous ?</a></li>
            <li><a href="sensibilisations.html">Sensibilisations</a></li>
            <li><a href="partenaires.html">Nos Partenaires</a></li>
            <li><a href="contact.html">Nous contacter</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Contact</h4>
          <ul>
            <li>14 rue Mansart<br>78190 Trappes</li>
            <li><a href="tel:+330****4530">06 03 41 45 30</a></li>
            <li><a href="mailto:capaaasqy@hotmail.fr">capaaasqy@hotmail.fr</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 CAPSAAA SQY — Tous droits réservés</p>
      </div>
    </div>
  </footer>

    <!-- Traducteur automatique (pt/ar prioritaire, en secondaire) -->
  <script type="text/javascript">
    function googleTranslateElementInit() {{
      new google.translate.TranslateElement({{
        pageLanguage: 'fr',
        includedLanguages: 'fr,pt,ar,en',
      }}, 'google_translate_element');
    }}
    function setPageLanguage(lang) {{
      if (!lang) lang = 'fr';
      document.cookie = 'googtrans=/fr/' + lang + '; path=/; expires=Thu, 31 Dec 2099 23:59:59 GMT';
      location.reload();
    }}
  </script>
  <script type="text/javascript" src="https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>

<script src="../js/script.js"></script>
</body>
</html>
"""

def main():
    for act in ACTIVITES:
        path = os.path.join(PAGES, f"activite-{act['slug']}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(page(act))
        print(f"OK {path} ({len(page(act))} octets)")

if __name__ == "__main__":
    main()
