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

## 🔧 Point technique

`git` et `python3` système sont bloqués sur le Mac : licence Xcode non acceptée
(« sudo xcodebuild -license accept »). Les modifications sont bien sur le disque,
mais **non commitées** tant que ce n'est pas réglé.
