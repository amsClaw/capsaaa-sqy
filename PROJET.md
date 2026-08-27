# CAPSAAA — Site Vitrine

## Identité

| Champ | Valeur |
|---|---|
| Nom complet | CAP Sport Art Aventure Amitié (CAPSAAA) |
| Type | Association loi 1901 |
| Création | 1992 |
| Objet | Activités sportives et loisirs adaptés aux personnes en situation de handicap |
| Territoire | Saint-Quentin-en-Yvelines (Trappes, Guyancourt, Élancourt…) |
| Adhésion | 100-120 adhérents par saison (52% femmes, 42% hommes) |
| Âge | À partir de 6 ans, sans limite |

## Bureau

| Rôle | Nom |
|---|---|
| Présidente | Nicole DIRAISON |
| Vice-Président | Dominique FONTAINE |
| Secrétaire | Catherine LAIGNEL |
| Trésorière | Souriya BOUKRA HAMAM |

**Conseil d'administration :** Fabienne BOURGEOIS, Joëlle DELMAS, Madeleine DUCRUET, François LECOMBE

## Coordonnées

- **Adresse** : 14 rue Mansart, 78190 Trappes
- **Téléphone** : 06 03 41 45 30
- **Email** : capaaasqy@hotmail.fr (attention : 3x "a" dans capaaa)
- **Site actuel** : https://www.cap-saaa-sqy.fr/
- **Agrément** : Direction Départementale Jeunesse et Sports
- **Affiliation** : Fédération Française des Sports pour Tous

## Activités proposées

1. **Activités aquatiques** — Piscine Monquaut (Trappes)
2. **Équitation adaptée** — Club SQY Équitation (Île aux Loisirs)
3. **Musculation** — Gymnase Aviation (Guyancourt)
4. **Fitness** — Salle Auguste-Renoir (Guyancourt)
5. **Multi-Sports** — Gymnase Aviation (Guyancourt)
6. **Sorties & événements**

## Sensibilisations

Ateliers de sensibilisation au handicap proposés aux écoles, centres de loisirs et entreprises :
- Basket fauteuil
- Parcours fauteuil
- Parcours aveugles
- Torball
- Boccia
- Parcours sensoriel

## Partenaires financiers

- Saint-Quentin-en-Yvelines (SQY)
- Villes de Trappes, Guyancourt, Élancourt, Montigny-le-Bretonneux
- Conseil départemental des Yvelines (78)
- Ministère des Sports
- Fédération Française des Sports pour Tous

---

## Projet technique

### Stack
- Site statique HTML5 / CSS3 / JS vanilla
- Police : Inter (Google Fonts)
- Aucune dépendance externe (hors Google Fonts)
- Responsive (breakpoints 992px, 768px, 480px)
- Design : orange (#E8843A) + bleu profond (#1E3A5F), beige clair (#FFF8F0)

### Structure du site

```
index.html                    → Accueil (aperçu actualités)
pages/qui-sommes-nous.html    → Histoire, mission, bureau
pages/activites.html          → 5 activités détaillées (couleurs par activité)
pages/actualites.html         → Rubrique ACTUALITÉS (données : js/actualites.js)
pages/sensibilisations.html   → Ateliers handicap
pages/galerie.html            → 7 albums (48 photos), lightbox
pages/inscriptions.html       → Tarifs & infos + section Documents (PDF)
pages/partenaires.html        → Logos & liens utiles
pages/contact.html            → Formulaire fonctionnel (FormSubmit) + coordonnées
```

### Assets

```
assets/
├── photos/                   ← 46 photos téléchargées depuis l'ancien site (local)
├── projet-associatif-capsaaa.pdf
├── logo-conseil-general-78.jpg
├── logo-elancourt.jpg
├── logo-guyancourt.png
├── logo-ministere-sports.png
├── logo-montigny.png
├── logo-sports-pour-tous.jpg
├── logo-sqy.png
└── logo-trappes.png
```

### Photos manquantes (introuvables sur l'ancien site — 404 vérifiés 14/08/2026)
| Fichier | Album | Sort |
|---|---|---|
| nkfu4691.jpg | Multi-Sports | retirée de la galerie ; carte Fitness remplacée par etirements.jpg |
| mariette-alexandre-dominique.jpg | Multi-Sports | retirée (la variante `-2` reste) |
| pyeb7201.jpg | Multi-Sports | retirée |
| qfws9546.jpg | Multi-Sports | retirée |
| photo-2023-06-26-23-16-58.jpg | Natation | retirée (les `-59`/`-60` restent) |

### État d'avancement

- ✅ Site développé (V1 draft)
- ✅ Photos 100 % locales (56 références vérifiées, 0 URL externe restante — 14/08/2026)
- ✅ **Retour association reçu (11/08/2026)** → validations : formulaire (nom/tél/email/ville+message), stats OK, SEO à travailler ensemble, 5 couleurs par activité (bleu/vert/jaune/gris/mauve, acidulées), traducteur pt/ar/en, section Documents, rubrique **ACTUALITÉS** (pas blog) — détails : `docs/RETOUR_ASSOCIATION_2026-08-11.md`
- ✅ **V1.1 intégrée (14/08/2026)** : formulaire fonctionnel (FormSubmit gratuit, champs nom/prénom/tél/email/ville/message), couleurs par activité appliquées (accueil, activités, inscriptions), page Actualités (données dans `js/actualites.js`), section Documents (fiche d'inscription + règlement en PDF dans `assets/docs/`), traducteur Google (pt/ar/en) sur toutes les pages
- ✅ **SEO (14/08/2026)** : keywords « sport adapté handicap SQY / association handisport Yvelines », canonical, Open Graph, JSON-LD NGO sur les 9 pages (`tools/seo_inject.py`)
- ✅ **Stats (14/08/2026)** : `js/stats.js` prêt **Google Analytics 4** (gtag.js, placeholder centralisé `gaMeasurementId`, désactivé si ID absent) intégré sur les 9 pages. Décision Ams : GA plutôt que Matomo. Guide simple pour l'association : `docs/GUIDE_GOOGLE_ANALYTICS_SIMPLE.md`. Reste : François crée le compte et transmet l'ID G-… (CAPSAAA-03)
- ✅ **Déployé (14/08/2026)** : GitHub Pages https://amsclaw.github.io/capsaaa-sqy/ + lien démo Cloudflare (tunnel temporaire) pour recette
- ✅ **V1.2 — Retour François 26/08 intégré (27/08/2026)** : nav renommée (Nos Activités, Nous rejoindre, Nos Partenaires, Nous contacter), sélecteur langue déplacé (plus de chevauchement), accueil resserré (chiffres 5 activités + conviviales, éducateurs sportifs diplômés, valeurs enrichies, bloc sensibilisation = titre + texte fournis par François), 5 pages détaillées par activité avec infos pratiques + bénéfices + photos + emplacements témoignages (à compléter par l'association), reCAPTCHA activé sur le formulaire. Détails : `docs/ANALYSE_SITE_V1_FRANCOIS_2026-08-26.docx` + issue Paperclip CAPSAAA-04
- 🔄 Reste : validation Ams + envoi du retour à François, activation du compte stats officiel, domaine cap-saaa-sqy.fr, décision AssoConnect (voir CAPSAAA-03)

### Liens (27/08/2026)
- Démo durable : https://amsclaw.github.io/capsaaa-sqy/
- Démo Cloudflare (temporaire, tunnel local) : voir issue CAPSAAA-02 (le tunnel doit être relancé si la machine redémarre : `python3 -m http.server 8000` + `cloudflared tunnel --url http://localhost:8000`)
- Prochaine action : validation Ams de la V1.2 → réponse à François (mail du 26/08) + issue CAPSAAA-03 (stats + domaine + AssoConnect).
