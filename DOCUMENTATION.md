# 🚀 CAPSAAA — Site Vitrine

**Documentation projet — Reprise & amélioration**

> Site vitrine pour **CAPSAAA** (CAP Sport Art Aventure Amitié)
> Association handisport — Saint-Quentin-en-Yvelines
> Projet créé le 9 juillet 2026

---

## 📋 Table des matières

1. [Présentation](#-présentation)
2. [Structure du projet](#-structure-du-projet)
3. [Pages détaillées](#-pages-détaillées)
4. [Arborescence du site](#-arborescence-du-site)
5. [Charte graphique](#-charte-graphique)
6. [Sources des contenus](#-sources-des-contenus)
7. [Images & photos utilisées](#-images--photos-utilisées)
8. [Fonctionnalités JS](#-fonctionnalités-js)
9. [Comment ouvrir le site](#-comment-ouvrir-le-site)
10. [Déploiement](#-déploiement)
11. [Améliorations possibles](#-améliorations-possibles)
12. [Contacts association](#-contacts-association)

---

## 📖 Présentation

CAPSAAA est une association à but non lucratif créée en 1992, basée à Trappes (78). Elle permet à des personnes en situation de handicap de pratiquer des activités sportives et de loisirs adaptées.

**Le site actuel (ancien)** : https://www.cap-saaa-sqy.fr/ — tourne sur e-monsite.com (CMS daté).
**Le nouveau site** : site statique HTML/CSS/JS moderne, responsive, prêt à être hébergé.

### Objectifs de la refonte
- Design moderne, aéré, mobile-first
- Navigation simplifiée et hiérarchisée
- Galerie photo enrichie avec lightbox
- Contenu enrichi depuis le projet associatif PDF
- Logos partenaires récupérés et intégrés

---

## 📁 Structure du projet

```
10_Projets/capsaaa/
│
├── README.md                          ← Brief projet (synthèse)
├── MAQUETTE.md                        ← Plan du site + charte graphique
│
├── index.html                         ← Page d'accueil
│
├── assets/                            ← Ressources statiques
│   ├── logo-conseil-general-78.jpg    ← Logo Conseil départemental 78
│   ├── logo-elancourt.jpg             ← Logo Ville d'Élancourt
│   ├── logo-guyancourt.png            ← Logo Ville de Guyancourt
│   ├── logo-ministere-sports.png      ← Logo Ministère des Sports
│   ├── logo-montigny.png              ← Logo Montigny-le-Bretonneux
│   ├── logo-sports-pour-tous.jpg      ← Logo FF Sports pour Tous
│   ├── logo-sqy.png                   ← Logo Saint-Quentin-en-Yvelines
│   ├── logo-trappes.png               ← Logo Ville de Trappes
│   └── projet-associatif-capsaaa.pdf  ← Fiche de présentation PDF
│
├── css/
│   └── style.css                      ← Styles complets (responsive + couleurs activités V1.1)
│
├── js/
│   ├── script.js                      ← Interactivité (menu, lightbox, formulaire, actualités)
│   └── actualites.js                  ← Données des actualités (facile à mettre à jour)
│
└── pages/
    ├── qui-sommes-nous.html           ← Histoire, valeurs, équipe
    ├── activites.html                 ← Détail des 5 activités
    ├── actualites.html                ← Rubrique ACTUALITÉS (V1.1)
    ├── sensibilisations.html          ← Ateliers de sensibilisation
    ├── galerie.html                   ← Galerie photos (48 photos, 7 onglets)
    ├── inscriptions.html              ← Infos pratiques + section Documents (V1.1)
    ├── partenaires.html               ← Partenaires + logos + liens utiles
    └── contact.html                   ← Formulaire fonctionnel (FormSubmit) + coordonnées
```

---

## 🧭 Arborescence du site

```
Accueil (index.html)
├── Hero section (photo + titre + accroche)
├── CAPSAAA en chiffres (4 stats)
├── Nos activités (6 cartes cliquables)
├── Nos valeurs (4 valeurs)
└── CTA Sensibilisation

Qui sommes-nous ?
├── Notre histoire (1992 → aujourd'hui)
├── Notre mission
├── Nos valeurs (4 cartes)
├── Notre équipe (bureau + administrateurs)
├── 📄 Télécharger le projet associatif (PDF)
└── Nos points forts

Activités (5 activités détaillées)
├── Activités aquatiques — Piscine Monquaut (Trappes)
├── Équitation adaptée — Club SQY Équitation (Île aux Loisirs)
├── Musculation — Gymnase Aviation (Guyancourt)
├── Fitness — Salle Auguste-Renoir (Guyancourt)
├── Multi-Sports — Gymnase Aviation (Guyancourt)
└── CTA contact + inscription

Sensibilisations
├── Notre approche (publics cibles, objectifs)
├── 6 ateliers proposés (basket fauteuil, parcours, boccia, torball, sensoriel, débat)
├── Présence sur le territoire (forums associations)
└── CTA contact

Galerie photos (7 onglets)
├── 🏊 Natation (6 photos)
├── 🐴 Équitation (8 photos)
├── 💪 Musculation (9 photos)
├── 🎯 Multi-Sports (8 photos)
├── 🎉 Sorties (3 photos)
├── ♿ Sensibilisations (14 photos)
└── 📸 Toutes (48 photos)

Inscriptions 2025/2026
├── Comment s'inscrire
├── Infos pratiques (adresse, téléphone)
├── Activités proposées (5 cartes)
├── Documents utiles
└── Tarifs

Partenaires & Liens utiles
├── 8 partenaires avec logos (SQY, villes, ministère, département, fédération)
└── Liens utiles (piscine, club équestre, fédération)

Contact
├── Coordonnées (adresse, téléphone, email, site)
├── Formulaire de contact (nom, email, sujet, message)
└── Mentions association
```

---

## 🎨 Charte graphique

| Élément | Valeur |
|---|---|
| **Couleur primaire** | `#E8843A` (orange) |
| **Couleur primaire foncée** | `#D06E2A` |
| **Couleur primaire claire** | `#FFF0E0` |
| **Couleur secondaire** | `#1E3A5F` (bleu profond) |
| **Couleur secondaire claire** | `#2E5A8F` |
| **Couleur de fond** | `#FFF8F0` (beige clair) |
| **Couleur de fond alternative** | `#F5EDE4` |
| **Texte principal** | `#2D2D2D` |
| **Texte secondaire** | `#6B6B6B` |
| **Police** | `Inter` (Google Font) |
| **Bordure** | `#E0D6CB` |
| **Succès** | `#4CAF50` |
| **Bordure radius** | `12px` (cart/boîtes) |
| **Ombre** | `0 2px 12px rgba(0,0,0,0.08)` |
| **Largeur max** | `1200px` |
| **Hauteur header** | `72px` |

### Police utilisée
- **Inter** (Google Font) en 400, 500, 600, 700, 800
- Importée via Google Fonts API dans le `<head>` de chaque page

### Style général
- Design aéré, espacé, beaucoup de `padding`
- Boutons arrondis (50px)
- Cartes avec ombre légère et effet de survol
- Navigation avec menu hamburger sur mobile
- Header fixe

---

## 📄 Sources des contenus

### Site actuel (cap-saaa-sqy.fr)
- Contenu des 13 pages
- Toutes les photos des albums
- Logos des partenaires

### PDF projet associatif
- Fichier source : `docs partagés/projet-associatif-capsaaa.pdf`
- Copié vers : `assets/projet-associatif-capsaaa.pdf`
- Contenu extrait : histoire, valeurs, équipe (bureau, CA), activités, sensibilisations, partenaires, organisation

### Informations clés extraites
- **Création** : 1992
- **Siège social** : 14 rue Mansart, 78190 Trappes
- **Téléphone** : 06 03 41 45 30
- **Email** : capaaasqy@hotmail.fr (3 x "a" dans capaaa — attention !)
- **Site** : www.capsaaa-sqy.fr (1 seul "a" dans le site)
- **Agrément** : Direction Départementale Jeunesse et Sports
- **Affiliation** : Fédération Française des Sports pour Tous
- **Adhérents** : 100-120 par saison (52% femmes, 42% hommes)
- **Âge** : À partir de 6 ans, sans limite d'âge
- **Bureau** : Nicole DIRAISON (Présidente), Dominique FONTAINE (VP), Catherine LAIGNEL (Secrétaire), Souriya BOUKRA HAMAM (Trésorière)
- **CA** : Fabienne BOURGEOIS, Joëlle DELMAS, Madeleine DUCRUET, François LECOMBE

---

## 🖼 Images & photos utilisées

### Logos partenaires (dans `assets/`)
Tous téléchargés depuis la page "Nos partenaires financiers" du site actuel.

### Photos (liées directement depuis le site actuel)
Les photos sont chargées depuis `https://www.cap-saaa-sqy.fr/medias/album/...` pour éviter de dupliquer le stockage.

**Liste des photos utilisées par album :**

| Album | Nb | Photos |
|---|---|---|
| 🏊 Natation | 6 | atip2979.jpg, cbrh0506.jpg, qmfi8712.jpg, photo-2023-06-26-23-16-58.jpg, photo-2023-06-26-23-16-59.jpg, photo-2023-06-26-23-16-60.jpg |
| 🐴 Équitation | 8 | pveh1252.jpg, imzd6900.jpg, diego-sur-plume.jpg, anis.jpg, anne-et-guillaume.jpg, anne-guillaume-joelle.jpg, dijbril.jpg, equitation.jpg |
| 💪 Musculation | 9 | les-bras.jpg, abdoss1.jpg, anne-et-fessal.jpg, etirements.jpg, nicole.jpg, pere-et-fils1.jpg, qbia3436.jpg, uxio7452.jpg, exmf9076.jpg |
| 🎯 Multi-Sports | 8 | nkfu4691.jpg, sebastien-et-son-papa-1.jpg, mariette-alexandre-dominique-2.jpg, corentin-et-son-papa.jpg, mariette-alexandre-dominique.jpg, on-se-prepare-a-jouer.jpg, pyeb7201.jpg, qfws9546.jpg |
| 🎉 Sorties | 3 | pique-nique-base-de-loisirs-saint-quentin.jpg, c5d7a270-8269-4469-977d-5ab9cf280514.jpeg, a215a3c3-622c-4a83-94ab-5df7e086e962.jpeg |
| ♿ Sensibilisations | 14 | hexg8906-1.jpg, apci4726-1.jpg, iwjy3417-1.jpg, kcet5662.jpg, nrht4766.jpg, swkx6891.jpg, tvfd9684.jpg, ulpz7456.jpg, uudl3422.jpg, bgns0799.jpg, fffp0382.jpg, img-5562.jpg, img-5563.jpg, img-5628.jpg |

**⚠️ Attention :** Les photos sont hébergées sur l'ancien site. Si l'ancien site disparaît ou change de plateforme, les photos ne seront plus accessibles. Solution : télécharger toutes les photos localement vers `assets/photos/`.

---

## ⚙️ Fonctionnalités JS

### `js/script.js` (chargé sur toutes les pages)

1. **Menu mobile** — Toggle hamburger, fermeture au clic sur un lien
2. **Navigation active** — Highlight automatique de la page courante
3. **Smooth scroll** — Pour les ancres internes
4. **Lightbox** — Clique sur une photo → agrandissement en plein écran
   - Clic sur fond ou bouton X pour fermer
   - Touche Échap pour fermer
5. **Compteurs animés** — Les chiffres (1992, 120+...) s'animent au scroll (Intersection Observer)
6. **Formulaire de contact** — Envoi réel via **FormSubmit** (service gratuit, sans backend)
   - Champs validés par l'association : nom, prénom, téléphone, email, ville, message
   - ⚠️ **Premier envoi** : FormSubmit envoie un email d'activation à capaaasqy@hotmail.fr — il faut cliquer le lien une fois pour activer la réception (fait une seule fois, au premier test réel)
7. **Actualités** — Rendu depuis `js/actualites.js` (page complète + aperçu accueil, 2 dernières)

### `js/actualites.js` (mise à jour des news)

- Chaque news = un objet : `date`, `titre`, `corps`, `photo` (optionnel, relatif à `assets/`), `lien` + `lienTexte` (optionnel, page interne OU adresse externe), `lienExterne: true` si site externe
- Enregistrer le fichier suffit : les pages se mettent à jour automatiquement

### Traducteur automatique (toutes les pages)

- Widget **Google Traduction** avec langues limitées à **fr, pt, ar, en** (pt/ar prioritaires, en secondaire)
- ⚠️ Nécessite une connexion internet + serveur HTTP (fonctionne en local via `python3 -m http.server`)

### Couleurs par activité (validées 11/08/2026)

| Activité | Couleur | Variables CSS |
|---|---|---|
| Piscine | Bleu | `--act-piscine` |
| Équitation | Vert | `--act-equitation` |
| Fitness | Jaune | `--act-fitness` |
| Musculation | Gris | `--act-musculation` |
| Multi-Sports | Mauve | `--act-multisport` |

Classes : `act-piscine`, `act-equitation`, `act-fitness`, `act-musculation`, `act-multisport` (bandeau carte, tag, bordure fiche détaillée).

### Script inline dans `pages/galerie.html`

7. **Onglets de galerie** — Filtrage par activité (changement de classe `active`)

---

## 💻 Comment ouvrir le site

### Simple (aucun serveur requis)
1. Ouvre `index.html` directement dans le navigateur
2. Navigue entre les pages via le menu

**⚠️ Limitation :** Les photos sont chargées depuis le site actuel en HTTP → besoin d'une connexion internet.

### Avec un serveur local (recommandé pour les tests)
```bash
# Avec Python (simple)
cd C:\Users\amsfo\Documents\Openclaw_folder\10_Projets\capsaaa
python3 -m http.server 8000

# Puis ouvre http://localhost:8000 dans le navigateur
```

```bash
# Avec Node.js (si disponible)
npx serve C:\Users\amsfo\Documents\Openclaw_folder\10_Projets\capsaaa
```

---

## 🚀 Déploiement (état 14/08/2026)

### En ligne maintenant
- **GitHub Pages (démo durable)** : https://amsclaw.github.io/capsaaa-sqy/ (repo `amsClaw/capsaaa-sqy`, branch `master`, dossier `/`)
- **Lien démo Cloudflare (temporaire)** : tunnel `cloudflared` vers un serveur local — voir issue CAPSAAA-02 pour l'URL courante

### Prochaines étapes
1. **Domaine cap-saaa-sqy.fr** : actuellement sur e-monsite (ancien site). Le pointage vers GitHub Pages ou Cloudflare Pages se fait une fois la décision AssoConnect prise (question en suspens — le site peut vivre seul dans un premier temps).
2. **Hébergement de production** : GitHub Pages convient ; Cloudflare Pages (gratuit, + stats Web Analytics intégrées) est l'alternative recommandée si l'association préfère Cloudflare.
3. **Stats** : renseigner l'identifiant GA4 (`G-…`) dans `CAPSAAA_STATS.gaMeasurementId` (fichier `js/stats.js`) quand François aura créé le compte — voir section « 📊 Statistiques de visite ».

### Important pour le déploiement
- Le site est 100% statique → pas de base de données, pas de backend
- Le formulaire de contact fonctionne via **FormSubmit** (gratuit, sans backend)
- **⚠️ Premier envoi** : FormSubmit envoie un email d'activation à capaaasqy@hotmail.fr — cliquer le lien une fois pour activer la réception
- Toutes les photos sont en local (`assets/photos/`) → le site ne dépend plus de l'ancien site
- Les chemins sont relatifs → le site fonctionne sous un sous-dossier (ex: GitHub Pages)

---

## 📊 Statistiques de visite (Google Analytics 4)

**Décision Ams (14/08/2026) : Google Analytics (pas Matomo).**

- `js/stats.js` est **GA4-ready** : balise `gtag.js`, placeholder centralisé `CAPSAAA_STATS.gaMeasurementId`.
- **Désactivé par défaut** : tant que `gaMeasurementId` est vide, aucun script n'est chargé, aucun cookie posé (RGPD).
- Le fichier est déjà inclus sur les 9 pages (`<script src="js/stats.js" defer>`).
- **Guide client prêt** : `docs/GUIDE_GOOGLE_ANALYTICS_SIMPLE.md` (non-informaticiens, ~15 min) — création du compte, propriété, flux de données, obtention de l'identifiant `G-XXXXXXXXXX`.
- **À faire (CAPSAAA-03)** : demander à François de créer le compte et transmettre l'ID `G-…` (le guide sera joint à la communication client), puis coller l'ID dans `js/stats.js` et republier. Données visibles sous 24-48 h.

---

## 🔧 Améliorations possibles

### Priorité haute
- [x] **Télécharger toutes les photos en local** dans `assets/photos/` pour ne plus dépendre de l'ancien site — fait le 14/08/2026 (0 URL externe restante)
- [x] **Rendre le formulaire de contact fonctionnel** — fait via FormSubmit (V1.1)
- [x] **Mettre en ligne** — fait : GitHub Pages + démo Cloudflare (14/08/2026) ; reste le domaine cap-saaa-sqy.fr

### Priorité moyenne
- [ ] **Page "Documents"** dédiée avec les documents d'inscription, les formulaires et le règlement (section Documents déjà ajoutée dans Inscriptions)
- [ ] **Filtres sur la galerie** par année ou par événement
- [ ] **Animation au scroll** (AOS.js ou Intersection Observer) pour les sections
- [x] **SEO** : balises meta description + keywords + canonical + OG + JSON-LD sur toutes les pages (14/08/2026)
- [ ] **Stats de visite** : `js/stats.js` prêt (GA4/gtag.js, désactivé sans ID) — reste à créer le compte et renseigner l'ID G-… (guide : `docs/GUIDE_GOOGLE_ANALYTICS_SIMPLE.md`)

### Priorité basse
- [ ] **Carte interactive** des lieux d'activités (Google Maps ou OpenStreetMap)
- [ ] **Blog/actualités** pour les événements de l'association
- [ ] **Page de sorties/événements** dédiée avec calendrier
- [ ] **Multilingue** (anglais) si besoin
- [ ] **Accessibilité** (WCAG) : contrastes, labels aria, navigation clavier
- [ ] **Mode sombre**

---

## 📞 Contacts association

| Rôle | Nom | 
|---|---|
| **Présidente** | Nicole DIRAISON |
| **Vice-Président** | Dominique FONTAINE |
| **Secrétaire** | Catherine LAIGNEL |
| **Trésorière** | Souriya BOUKRA HAMAM |

**Coordonnées :**
- **Adresse** : 14 rue Mansart, 78190 Trappes
- **Téléphone** : 06 03 41 45 30
- **Email** : capaaasqy@hotmail.fr
- **Site actuel** : https://www.cap-saaa-sqy.fr/

---

## 🧠 Notes pour le repreneur / agent

- **Toutes les pages sont liées entre elles** via les menus et les boutons CTA
- **Les chemins sont relatifs** : `index.html` → `pages/activites.html` → `css/style.css`
- **Les photos sont en local** dans `assets/photos/` (plus aucune URL vers l'ancien site depuis le 14/08/2026)
- **Les logos sont dans `assets/`** avec des noms explicites
- **Le projet associatif PDF** est dans `assets/projet-associatif-capsaaa.pdf`
- **Le CSS est responsive** avec des breakpoints à 992px, 768px et 480px
- **Pas de dépendances externes** à part Google Fonts (Inter) et les images du site actuel

---

*Document généré le 9 juillet 2026 par FoxAI — Dossier : 10_Projets/capsaaa/*
