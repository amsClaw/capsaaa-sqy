# Modifications appliquées — retour client du 17/09/2026

Source : mail de François LECOMBE (17/09/2026 11h28) + pièce jointe
« Texte du nouveau site CAPSAAA V2.docx » (annotations page par page).
Archivé dans `docs/client-feedback/2026-09-17/`.

## ✅ Appliqué (ne dépend pas des photos)

| # | Modification | Fichier(s) |
|---|---|---|
| 1 | Suppression de 2 actualités : « Une belle journée à la base de loisirs de Saint-Quentin » et « CAPSAAA au forum des associations » | `js/actualites.js` |
| 2 | Emoji 🎉 retiré de la ligne « …et des activités conviviales » | `index.html` |
| 3 | Âge d'accueil : 6 ans → **5 ans** | `pages/activites.html`, `pages/inscriptions.html`, `pages/qui-sommes-nous.html` |
| 4 | Fitness : « prescription médicale » → **« indication médicale »** (×2) | `pages/activite-fitness.html` |
| 5 | Fitness : virgule après « step » (step, fitness, stretching) | `pages/activite-fitness.html` |
| 6 | Multi-Sports : ajout de « **Basket fauteuil** » dans les disciplines | `pages/activite-multisport.html`, `pages/activites.html` |
| 7 | Multi-Sports : « seule » → « **solo** ou en équipe » | `pages/activite-multisport.html` |
| 8 | Aquatique : horaire **« Le samedi 10h45 – 12h »** | `pages/activite-aquatique.html` |
| 9 | Torball : « fil équipé **également** de grelots » | `pages/sensibilisations.html` |
| 10 | Emoji Boccia : 🎯 → **🥇** | `pages/sensibilisations.html` |
| 11 | Galerie : nouvelle catégorie **🤸 Fitness** (onglet + section, 1 photo) | `pages/galerie.html` |

Vérifié : 8 contrôles grep + test navigateur local (onglets galerie, textes, horaire).

## ⏳ En attente (dépend du client)

- **Photos** (~6 à remplacer, dont une « communiquée ultérieurement ») : accueil, aquatique (milieu), musculation, 3ᵉ photo multi-sports, dernière actualité
- **Horaires** des autres activités (seul celui de l'aquatique a été fourni)
- **Tarifs** : remplacer « Contactez-nous pour les tarifs » par un PDF téléchargeable → nécessite le document tarifs
- **Documents** : fiche d'inscription / règlement / projet associatif à vérifier

## ❓ À confirmer avec François (ambigu dans le docx)

- **Changement de lieu « Gymnase Broustal — Trappes »** : l'annotation ne précise pas l'activité
  concernée (Fitness ? Musculation ?). Non appliqué pour éviter une erreur d'information
  publique. → à confirmer lors du RV téléphonique.
- Emoji 🥇 : interprété comme « remplacer le 🎯 de la Boccia par 🥇 ».

## 🔴 2ᵉ passe — textes surlignés en ROUGE par François (17/09, après-midi)

Extraction automatique des **43 passages rouges** du docx (script : lecture des runs
`w:color` rouges avec contexte tableau).

| # | Modification (texte rouge du client) | Fichier(s) |
|---|---|---|
| 12 | Aquatique — Public : ajout « **après validation par les maîtres-nageurs lors de la séance d'essai** » | `pages/activite-aquatique.html` |
| 13 | Musculation — bénéfice : « Gagner en force, **équilibre,** endurance et tonicité » | `pages/activite-musculation.html` |
| 14 | Valeur **Bien-être** (version complète) : « … par le sport : se dépasser, se sentir mieux dans son corps et dans sa tête » | `pages/qui-sommes-nous.html` |
| 15 | Valeur **Convivialité** : « Un cadre chaleureux **pour créer des liens** : sorties, repas et moments de partage… » | `pages/qui-sommes-nous.html`, `index.html` |
| 16 | Sensibilisations : « par 1/2 journée **ou journée** complète » | `pages/sensibilisations.html` |

Déjà conformes (vérifiés vs docx) : équitation (paragraphe 🐴 + 2 bénéfices),
musculation « …de chacun : on progresse à son rythme », fitness (virgule step,
indication médicale, sédentarité), multi-sports (basket fauteuil, solo), torball,
âges 5 ans, boccia 🥇.

## ❓ Reste ambigu / à confirmer

- **Changement de lieu « Gymnase Broustal – Trappes »** : les annotations Broustal
  encadrent les remarques Fitness (virgule step, indication médicale, sédentarité), mais
  la fiche Fitness du docx affiche « Gymnase Aviation — Guyancourt ». **Non appliqué** →
  demander à François quelle activité et quel gymnase (+ le plan).
- **Horaires** : seul celui de l'aquatique est fourni (« samedi 10H45 à 12H »). Les
  mentions rouges « Mettre horaire / Mettre les horaires » concernent l'équitation, la
  musculation, le multi-sports et les sorties → valeurs manquantes.
- **Tarifs** : « Demander les tarifs = **Télécharger les tarifs** » + « Permet de
  télécharger » → nécessite le PDF des tarifs (absent de `assets/docs/`).
- **Phrase musculation** : deux variantes rouges (« de chacun : on progresse à son
  rythme » vs « de chaque participant qui progresse à son rythme ») — cosmétique.

## 📸 Photos à remplacer (client)

Accueil · aquatique (celle du milieu) · musculation · 3ᵉ photo multi-sports · dernière
actualité · (« photo à changer : sera communiquée ultérieurement »).

## 🔧 Point technique

Résolu le 17/09 : licence Xcode acceptée par Ams → `git` et `python3` système
fonctionnent. Toutes les modifications sont **commitées et poussées** sur
`github.com/amsClaw/capsaaa-sqy` (branche `master`).
