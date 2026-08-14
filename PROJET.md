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

### Photos manquantes (introuvables sur l'ancien site)
| Fichier | Album |
|---|---|
| nkfu4691.jpg | Multi-Sports |
| mariette-alexandre-dominique.jpg | Multi-Sports |
| pyeb7201.jpg | Multi-Sports |
| qfws9546.jpg | Multi-Sports |
| photo-2023-06-26-23-16-58.jpg | Natation |

### État d'avancement

- ✅ Site développé (V1 draft)
- ✅ Photos sécurisées en local (46/51)
- ✅ **Retour association reçu (11/08/2026)** → validations : formulaire (nom/tél/email/ville+message), stats OK, SEO à travailler ensemble, 5 couleurs par activité (bleu/vert/jaune/gris/mauve, acidulées), traducteur pt/ar/en, section Documents, rubrique **ACTUALITÉS** (pas blog) — détails : `docs/RETOUR_ASSOCIATION_2026-08-11.md`
- ✅ **V1.1 intégrée (14/08/2026)** : formulaire fonctionnel (FormSubmit gratuit, champs nom/prénom/tél/email/ville/message), couleurs par activité appliquées (accueil, activités, inscriptions), page Actualités (données dans `js/actualites.js`), section Documents (fiche d'inscription + règlement en PDF dans `assets/docs/`), traducteur Google (pt/ar/en) sur toutes les pages
- ❌ URLs photos encore vers l'ancien site (e-monsite) → à migrer vers assets/photos/ (en cours — voir CAPSAAA-02)
- ❌ Pas déployé (voir CAPSAAA-02)
- 🔄 SEO à travailler avec l'association (voir CAPSAAA-02)

### Prochaine action
Voir issue CAPSAAA-02 (photos locales, SEO, déploiement). Pour la démo V1.1 : `python3 -m http.server` à la racine du projet, puis ouvrir http://localhost:8000.
