# NOTE_CAPACITES_EMONSITE.md

**CAPSAAA-eM 01 — Capacités de la plateforme e-monsite : ce qui est possible / impossible**

- Date : 2026-08-27
- Auteur : Chief of staff (amsfox)
- Statut : **v1.0** — sources publiques + **exploration réelle du manager (compte test gratuit)** + captures d'écran ; approche validée par Ams (27/08)
- Issue : AMS-51 (CAPSAAA-eM 01)

---

## 1. Contexte & méthode

Objectif : préparer le terrain pour construire la **version e-monsite** du site CAPSAAA
(site actuel : https://www.cap-saaa-sqy.fr/ ; référence statique V1.2 :
`~/.openclaw/workspace/amsclaw/projects/capsaaa-sqy`, démo https://amsclaw.github.io/capsaaa-sqy/).

Méthode en 2 passes :
1. **Sources publiques** (offres e-monsite.com, blog, centre d'aide, FAQ FTP, tricks tiers,
   observation du site actuel) — relevé du 27/08/2026.
2. **Exploration réelle du manager** sur le compte test gratuit (créé le 27/08/2026) —
   vérification directe des fonctionnalités. Captures dans `docs/captures/emonsite/`.

---

## 2. La plateforme en bref

e-monsite = **CMS SaaS français hébergé et fermé** :
- Tout se configure dans le **« manager »** (interface web) — pas d'accès aux fichiers.
- **Pas d'accès FTP** (FAQ officielle : « Vous ne pouvez donc pas transférer [vos fichiers] par FTP :
  vous personnaliserez et configurerez votre site via le manager »).
- Sites gratuits à vie possibles (publicité + lien e-monsite en pied de page).

---

## 3. Offres & tarifs (relevé 27/08/2026 — site public + manager)

| Offre | Prix | Stockage | Pages | Membres | Pub | CSS/JS global | Balises META | Zones haut/bas | Page 404 | Langues |
|---|---|---|---|---|---|---|---|---|---|---|
| **GRATUIT** | 0 € | **25 Mo** (confirmé manager) | 10 | 3 | oui + lien e-monsite | non | page par page (voir §4.6) | non | non | 1 |
| **PERSO** | 54 €/an | 500 Mo | 20 | 15 | non | non | non | non | non | 1 |
| **PRO** | **66 €/an** (confirmé manager) | **2500 Mo** (2,5 Go — chiffre du manager) | illimitées | 1 500 | non | **oui** | **oui** | **oui** | **oui** | **oui (minima PRO)** |
| **BUSINESS** | 186 €/an | 6 Go | illimitées | illimité | non | oui | oui | oui | oui | oui |
| BUSINESS+ | 288 €/an | = BUSINESS + réservation ou RDV | | | | | | | | |
| E-COMMERCE / + | 324 €/an / 660 €/an | 6 Go + boutique | | | | | | | | |

Points clés (confirmés dans le manager, onglet « Pro » du design) :
- **« Personnalisation CSS et Javascript » = badge PRO** : l'onglet « Experts » du design contient
  les zones CSS et Javascript avec un badge « Pro » (capture `03_experts_css_js_pro.png`).
- PRO : **2500 Mo** (message officiel : « 20 fois plus d'espace : 2500 Mo contre 25 Mo gratuit et
  500 Mo Perso ») — à noter : le site public affiche « 3 Go », le manager dit 2,5 Go.
- Autres avantages PRO affichés : sans publicité, espace membres communautaire, statistiques
  détaillées, newsletters (5/mois, 5 000 mails).
- **« L'abonnement PRO n'intègre PAS le nom de domaine »** (message officiel du manager) :
  domaine = option **35 €/an** en complément ; Pack SMS = 15 €/an.
- **Multilingue = PRO confirmé** (Réglages → Langues : « Version PRO requise à minima » ;
  pas de traducteur automatique, traductions manuelles).

---

## 4. Capacités détaillées — vérifiées dans le manager (compte gratuit)

### 4.1 Éditeur de pages (lignes / colonnes / widgets)
- Éditeur **en lignes et colonnes** ; chaque colonne accueille un **widget** parmi :
  **Éditeur visuel** (texte enrichi), **Image**, **Vidéo**, **Éditeur HTML** (code libre),
  **Fichier à télécharger**, **Autres widgets** (capture `02_widget_choisi_editeur_html.png`).
- **Le widget « Éditeur HTML » est bien présent dès le gratuit** (choisisseur de colonne) —
  c'est la brique clé pour injecter du HTML par page sans PRO.
- **Styles de lignes prédéfinis** (pinceau) : « Ligne en surbrillance », « Séparation de ligne »,
  « Accordéon », etc. + **styles de colonnes**.
- **CSS/classes par ligne et par colonne** : champs `cssClass`, `cssId`, `cssStyle` sur chaque
  ligne/colonne + options complètes (fond couleur/image/vidéo, formes, bordures, marges/paddings
  y compris mobile, alignement, largeur max 1320px…) — **sans PRO** (CSS localisé, pas global).
- Contenus de cellules (texte enrichi) testés : **enregistrement et rendu public OK**
  (page « Test HTML CAPSAAA » créée et publiée).
- **Gestion des pages** : explorer avec catégories, ordre manuel, publier/dépublier, **dupliquer**,
  corbeille, « Ajouter une page », définition de la page d'accueil (par catégorie).

### 4.2 Thèmes & personnalisation
- Catalogue de **30+ thèmes responsives** (Basic, My Iceland, Blurfest, Le Naturel, On the Road,
  La Maison, Mystic, FC Aulan, TerraBio, Vividnews, École Havendier, Mairie d'Atlantis, etc.)
  avec filtres (secteur d'activité, profil, couleurs) et aperçus.
- **« Mes thèmes sauvegardés »** + **« Historique des modifications du thème »** (sauvegarde/
  restauration d'une version personnalisée) — utile pour la construction.
- **Apparence (Configuration → Apparence)** : onglet **Général** complet **en gratuit** :
  largeur du site (max 1320px), couleur de fond, motif, couleurs des éléments, typographie
  (Google Fonts dispo), logo et titre, navigation/menu, boutons, entête, pied de page, images,
  formulaires, fil d'ariane, listes, styles prédéfinis.
- Onglet **Experts** = zones **CSS** et **Javascript** globales → **PRO** (capture
  `03_experts_css_js_pro.png`). Attention : le CSS injecté n'est pas conservé si on change de thème.

### 4.3 Médias & stockage
- **25 Mo confirmés** (compteur réel : « 1,6 Mo sur 25 Mo » sur le site test).
- Gestionnaire d'images : répertoires, upload (gif/jpg/png), albums ; gestionnaire de fichiers.
- Modules **Album photos** et **Galerie vidéos** activables (gratuit).

### 4.4 Modules (disponibles en gratuit, activation libre)
- **Activés par défaut** : Pages, Annuaire, Contact (le formulaire de contact du site actuel
  est donc reproductible sans PRO).
- **Activables sans PRO** : **Blog** (→ peut servir de rubrique « Actualités »), Agenda,
  Album photos, Galerie vidéos, Sondages, Forum, Livre d'or, Réservation, Boutique (module
  externe, prise de commande sans paiement CB).

### 4.5 Import / migration
- Import possible depuis **WordPress, Overblog, Tumblr, Blogger** (contenu) ; import de membres CSV.
- **PAS d'import de fichiers HTML bruts / de site statique** (pas de FTP, pas d'upload de pages).
- Migration sortante : pas d'export complet — récupération manuelle (textes, photos).

### 4.6 SEO, domaine & réglages
- **SEO par page présent dans le formulaire gratuit** : titre, mots-clés, description, **meta
  additionnels**, **URI personnalisée** (slug), **noindex** — champs visibles sur l'offre gratuite
  (gating au moment de l'enregistrement à confirmer ; en PRO c'est garanti). Robots.txt modifiable.
- **Plugins par page** : accès restreint aux membres, **accès par mot de passe**, fil d'ariane.
- Réglages globaux (Configuration → Réglages) : **HelloAsso** (dons — pertinent association),
  API Google, Domaines, **Google Fonts**, Infos légales, **Redirections**, Page 404, Popups,
  Modération, Structures de paiement (Wuro).
- Domaine : réservation chez e-monsite (35 €/an) ou transfert ; l'actuel cap-saaa-sqy.fr est chez
  **OVH** (DNS délégué chez e-monsite) → le domaine reste à l'association dans tous les cas.

### 4.7 Compte & connexion
- Création du compte test : **par lien magique envoyé par e-mail** (pas de mot de passe initial ;
  e-monsite propose aussi « Se connecter avec Google »). Un mot de passe généré est stocké dans
  `~/.hermes/secrets/e-monsite.txt` (chmod 600) pour un usage futur si le compte l'exige.

---

## 5. État du site actuel (observé 27/08/2026)

- https://www.cap-saaa-sqy.fr/ tourne sur le plan **GRATUIT** (lien « Créer un site internet avec
  e-monsite » en pied de page + bannière publicitaire/cookies).
- **13 pages** (12 au menu + accueil) alors que la limite affichée de l'offre gratuite est **10 pages**
  → compte « grand-père » probable (créé avant un durcissement) ; à ne pas reproduire sur le nouveau site.
- Thème Bootstrap 4 basique, navigation plate (daté).
- Photos déjà récupérées en local pour la V1.2.
- Domaine : registrar OVH (expiration 05/2027), DNS délégué chez e-monsite.

---

## 6. Synthèse : possible / impossible

| Question | Réponse | Preuve |
|---|---|---|
| Importer les fichiers HTML statiques (V1.2) ? | **NON** — pas de FTP, pas d'import de fichiers bruts | FAQ + manager |
| CSS personnalisé **global** (design V1.2) ? | **OUI mais PRO** (66 €/an) — onglet « Experts » | capture 03 |
| JavaScript **global** ? | **PRO** (même zone Experts) | capture 03 |
| **Blocs HTML dans les pages** ? | **OUI dès le gratuit** — widget « Éditeur HTML » par colonne | capture 02 |
| CSS **par ligne/colonne** (classes, fonds, bordures…) ? | **OUI en gratuit** (CSS localisé) | manager |
| Gestion des pages (ajout/édition/duplication/redirection) ? | **OUI** — explorer, catégories, dupliquer, publier | manager |
| Médias / albums / fichiers à télécharger ? | **OUI** — 25 Mo gratuit, albums, fichiers | manager |
| Blog / Actualités ? | **OUI en gratuit** — module Blog activable | manager |
| Formulaire de contact ? | **OUI en gratuit** — module Contact actif par défaut | manager |
| Multilingue (pt/ar/en — exigence association) ? | **PRO (minima)** — sinon widget Google Traduction via HTML à tester | Réglages → Langues |
| Nom de domaine attaché ? | **OUI** — option 35 €/an (non inclus dans PRO) | manager |
| Statistiques de visite ? | Simples (gratuit) / détaillées (PRO) | manager |
| Plus de 10 pages ? | **NON en gratuit** (limite affichée) → PRO illimité | offre publique |
| SEO par page (titre/description/meta) ? | Champs **présents en gratuit** (à confirmer à l'enregistrement) ; garanti PRO | formulaire page |

---

## 7. Implications pour le projet CAPSAAA

1. **Le design V1.2 n'est pas reproductible tel quel en gratuit** : pas de CSS global ni de JS sans
   PRO. Deux voies :
   - **Voie A — Gratuit strict (0 €)** : thème sobre + réglages charte (#E8843A / #1E3A5F, Inter)
     + **styles de lignes prédéfinis** + **blocs HTML** par page + CSS par ligne/colonne.
     Limites assumées : pub affichée, 10 pages (13 aujourd'hui → réorganiser), 1 langue, pas de JS
     global, pas de META global (mais SEO par page semble dispo).
   - **Voie B — PRO (66 €/an)** : CSS/JS global injectable (adapter les sélecteurs V1.2 au thème),
     META, 404, zones haut/bas, pages illimitées, sans pub, multilingue (minima).
2. **Coût vs bénéfice** : GitHub Pages = 0 € + domaine OVH déjà payé. L'argument fort d'e-monsite
   = **l'association peut gérer elle-même** (éditeur visuel, photos, actualités) sans dépendre de
   nous — c'est le critère qui justifie le budget PRO le cas échéant.
3. **Photos** : ~46 photos en local ; poids à mesurer vs 25 Mo gratuit (risque de dépassement → PRO).
4. **Domaine** : reste chez OVH dans tous les cas ; garder la délégation DNS actuelle si on reste
   chez e-monsite, changer les NS si on part vers GitHub Pages.
5. **Bons points découverts** : HelloAsso (dons) intégré, module Blog pour « Actualités », module
   Contact natif, pages protégées par mot de passe (utile pour un espace membres simple).

---

## 8. Approche de construction — **VALIDÉE par Ams (27/08)**

- **Étape 1 (AMS-51 — cette issue, terminée)** : compte e-monsite de test (offre gratuite) créé
  → exploration réelle du manager réalisée → note complétée + captures.
- **Étape 2 (AMS-02, construction)** — approche validée « explorer en gratuit d'abord » :
  - Thème sobre + réglages charte + **blocs HTML** pour les composants clés (bandeaux, cartes
    activités, galerie, encarts) + styles de lignes/colonnes ;
  - **Passage PRO (66 €/an) seulement si les limites gratuites bloquent** (CSS global, pages > 10,
    pub, multilingue) — jamais de souscription sans validation Ams ;
  - Comparatif détaillé thème+CSS vs blocs HTML : issue **CAPSAAA-eM 03**.
- **Contenu** : réutiliser les textes/photos de la V1.2 (déjà validés par l'association).

---

## 9. Questions ouvertes (état après exploration)

1. ~~Pourquoi 13 pages sur l'offre gratuite (limite 10) ?~~ → compte « grand-père » probable ;
   le nouveau site devra respecter 10 pages en gratuit.
2. **Le widget « Éditeur HTML » accepte-t-il du JS / des iframes** (filtrage) ? → widget présent en
   gratuit ; **test réel à faire à la construction** (l'automatisation n'a pas pu valider le
   commit d'un bloc HTML — à tester en cliquant dans l'UI).
3. ~~Formulaire natif en gratuit ?~~ → **OUI** (module Contact actif par défaut).
4. ~~Google Traduction via bloc HTML ?~~ → à tester avec le widget HTML (dépend de la réponse en 2).
5. **Poids total des photos CAPSAAA vs 25 Mo** → à mesurer (photos en local).
6. ~~Blog natif pour « Actualités » ?~~ → **OUI** (module Blog activable).
7. SEO par page : champs présents en gratuit — **confirmer qu'ils s'enregistrent sans PRO**.

---

## 10. Compte e-monsite de test

- Site : **https://capsaaa-site-de-test.e-monsite.com** (sous-domaine libre réservé).
- Email de connexion : **amsfox@gmail.com** (validé par Ams).
- Connexion : **lien magique** envoyé par e-mail (login sans mot de passe).
- Offre : **GRATUITE** (aucun coût). Aucune souscription payante sans validation d'Ams.
- Identifiants/mot de passe généré : `~/.hermes/secrets/e-monsite.txt` (chmod 600 — ne jamais
  afficher dans un chat).
- Pages de test créées : « Test HTML CAPSAAA » (publiée) — contenu de test texte enrichi.

---

## 11. Captures d'écran (docs/captures/emonsite/)

| Fichier | Contenu |
|---|---|
| 01_dashboard.png | Tableau de bord du manager (site test) |
| 02_widget_choisi_editeur_html.png | Choisisseur de widget par colonne (Éditeur visuel / Image / Vidéo / **Éditeur HTML** / Fichier à télécharger / Autres widgets) |
| 03_experts_css_js_pro.png | Onglet « Experts » : zones CSS + Javascript avec badge **Pro** |
| 04_offre_pro_66eur.png | Offre PRO 66 €/an + domaine 35 €/an (écran du manager) |
| 05_pages_explorer.png | Explorer des pages (7 pages du thème + test) |
| 06_site_public_test.png | Site public de test (accueil) |

---

## 12. Sources

- Offres : https://www.e-monsite.com/pages/offres/ · https://www.e-monsite.com/pages/offres/creation-site-pro.html
- Blog CSS : https://www.e-monsite.com/blog/web-design/personnaliser-son-theme-responsive-en-css-bonnes-pratiques.html
- Import : https://www.e-monsite.com/blog/do/tag/importer/
- Tutoriels : https://www.e-monsite.com/pages/tutoriels/tous-les-tutoriels/
- Aide : https://www.e-monsite.com/pages/aides-creation-site/
- FAQ FTP : https://aide.e-monsite.com/hc/fr/articles/200217781
- Widget HTML : https://aide.e-monsite.com/hc/fr/articles/201453071
- Trick gratuit (widget Éditeur HTML dispo dès le gratuit) : https://www.mon-site-web.org/tricks/css-js-e-monsite/ajouter-une-liseuse-pdf-sur-une-page.html
- Site actuel : https://www.cap-saaa-sqy.fr/ (observation directe 27/08/2026)
- WHOIS cap-saaa-sqy.fr (OVH) + DNS (ns1/ns2.e-monsite.com) — vérifié 27/08/2026
- **Exploration réelle du manager** (compte test gratuit, 27/08/2026) — captures ci-dessus
