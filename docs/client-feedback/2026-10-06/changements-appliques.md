# Retours de François du 05/10/2026 (mail du 06/10) — suivi

Source : `Corrections Site CAPSAAA le 05.docx` (images extraites dans `images/`, dans l'ordre du document).
Les captures de François viennent de la **version e-monsite**.

| Demande | Statique | e-monsite | Statut |
|---|---|---|---|
| Supprimer la rubrique Blog | — (pas de blog) | entrée « Blog » masquée dans le menu (case « affichée » décochée, réversible) ; module conservé (il alimente la liste d'Actualités) | fait (13/10, accord d'Ams) |
| Bandeau du haut toujours visible au défilement | déjà le cas | `#navbar` en `position:sticky` sur les 8 pages de contenu | fait (Contact et /blog/ = pages module, non modifiables en gratuit) |
| « CAP » et « Sport » en orange | fait | fait | fait |
| Photo de la piscine réduite et rognée | déjà rognée (380 px) | 560 px de large × 340 px de haut, cadrée sur les nageurs | fait — interprétation, à faire valider |
| Supprimer « Découvrir nos activités » | fait | fait | fait |
| Supprimer la zone Nos valeurs | fait | fait | fait |
| Cartes de l'accueil : photo + nom + « En savoir plus » | fait (grille 3 × 2) | fait | fait |
| « …et des activités » après « …sportifs diplômés » | fait | fait | fait |
| 5 boutons « En savoir plus » qui menaient à Contact | déjà vers les fiches | vers `/pages/nos-activites.html#<sport>` | fait |
| Une page par activité (seul le contenu du sport) | pages séparées existantes | une seule page (limite 10 pages) : avec `#sport`, seul ce sport s'affiche + « ← Retour aux activités » | fait |
| Supprimer « Toutes nos activités » | n'existait pas | fait | fait |
| Page Activités : présentation + grille de cartes + « Envie de nous rejoindre ? » | déjà le cas | sommaire remplacé par la grille de cartes | fait |
| Aquatique : supprimer « + bénévoles » | fait | fait | fait |
| Équitation : 8 cavaliers max | fait (2 endroits) | fait (2 endroits) | fait |
| Fitness : photos à changer | — | — | **attend les photos de François** |
| Multi-Sports : 1re photo = tennis de table | photo principale échangée avec la 1re de la galerie | idem | fait |
| Sensibilisations : « Parcours malvoyants » + atelier « Ateliers sensoriels » | fait | fait | fait |
| Partenaires : retirer les commentaires sous les logos | fait (logos seuls) | fait (logos seuls) | fait |

Sauvegarde e-monsite avant modification : `~/projets/capsaaa-e-monsite/docs/corrections-2026-10-05/avant/`
(rejouable : `tools/corrections_2026_10_05.py`, restauration en réécrivant les blocs « avant » avec `tools/modifier_blocs.py`).
