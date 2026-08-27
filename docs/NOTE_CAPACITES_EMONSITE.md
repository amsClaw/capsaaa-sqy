# NOTE_CAPACITES_EMONSITE.md

**CAPSAAA-eM 01 — Capacités de la plateforme e-monsite : ce qui est possible / impossible**

- Date : 2026-08-27
- Auteur : Chief of staff (amsfox)
- Statut : **DRAFT v0.1** — basé sur sources publiques + observation du site actuel ; à compléter après création du compte test et exploration réelle du manager (voir §9)
- Issue : AMS-51 (CAPSAAA-eM 01)

---

## 1. Contexte & méthode

Objectif : préparer le terrain pour construire la **version e-monsite** du site CAPSAAA
(site actuel : https://www.cap-saaa-sqy.fr/ ; référence statique V1.2 :
`~/.openclaw/workspace/amsclaw/projects/capsaaa-sqy`, démo https://amsclaw.github.io/capsaaa-sqy/).

Sources utilisées (relevé du 27/08/2026) :
- Page offres e-monsite.com (https://www.e-monsite.com/pages/offres/ + page offre PRO)
- Blog / tutoriels e-monsite (personnalisation CSS, import, domaine, pages, médias)
- Centre d'aide e-monsite + FAQ (accès FTP)
- Source tierce mon-site-web.org (tricks CSS/JS e-monsite — confirmation widget HTML dès le gratuit)
- Observation directe du site actuel (navigateur)

---

## 2. La plateforme en bref

e-monsite = **CMS SaaS français hébergé et fermé** :
- Tout se configure dans le **« manager »** (interface web) — pas d'accès aux fichiers.
- **Pas d'accès FTP** (FAQ officielle : « Vous ne pouvez donc pas transférer [vos fichiers] par FTP :
  vous personnaliserez et configurerez votre site via le manager »).
- Sites gratuits à vie possibles (publicité + lien e-monsite en pied de page).

---

## 3. Offres & tarifs (relevé 27/08/2026)

| Offre | Prix | Stockage | Pages | Membres | Pub | CSS/JS global | Balises META | Zones haut/bas | Page 404 | Langues |
|---|---|---|---|---|---|---|---|---|---|---|
| **GRATUIT** | 0 € | 25 Mo | 10 | 3 | oui + lien e-monsite | non | non | non | non | 1 |
| **PERSO** | 54 €/an | 0,5 Go | 20 | 15 | non | non | non | non | non | 1 |
| **PRO** | 66 €/an (5,50 €/mois) | 3 Go | illimitées | 1 500 | non | **oui** | **oui** | **oui** | **oui** | 5 |
| **BUSINESS** | 186 €/an | 6 Go | illimitées | illimité | non | oui | oui | oui | oui | oui |
| BUSINESS+ | 288 €/an | = BUSINESS + réservation ou RDV | | | | | | | | |
| E-COMMERCE / + | 324 €/an / 660 €/an | 6 Go + boutique en ligne | | | | | | | | |

Points clés :
- **« Personnalisation CSS et Javascript » = badge PRO** (66 €/an). PERSO n'apporte PAS le CSS/JS :
  il retire juste la pub et augmente stockage/pages/membres.
- Autres exclusivités PRO (comparatif officiel « avec/sans PRO ») : balises META, modification des
  zones haut/bas de site, édition de la zone supérieure, page 404 personnalisée, restriction d'accès
  par mot de passe, stats détaillées, 1 000 catégories, carrousel 25 images, espace membres complet,
  newsletter (5/mois, 5 000 mails), import/export CSV d'événements.
- **Nom de domaine : option complémentaire dès 35 €/an** (3 adresses mail pro incluses), domaine
  secondaire dès 20 €/an. BUSINESS inclut le domaine + SSL.

---

## 4. Capacités détaillées

### 4.1 Éditeur de pages
- Éditeur visuel **en lignes / colonnes de widgets** ; outil de création de page par « blocs »
  (disposition image/texte) ; bascule d'un éditeur visuel en **éditeur HTML**.
- Widgets disponibles : texte, image, **Éditeur HTML** (code HTML libre dans une ligne),
  carrousel/diaporama, vidéo (YouTube/Dailymotion/Vimeo), carte Google, lecteur audio, fichiers
  à télécharger, moteur de recherche, formulaire, etc.
- **Widget « Éditeur HTML » : disponible dès la version gratuite** (confirmé par le trick officiel
  « Ajouter une liseuse PDF » de mon-site-web.org : « Cette fonctionnalité est disponible dès la
  version gratuite, avec le widget Editeur HTML » + tutoriel e-monsite « Comment intégrer un code
  HTML issu d'un service externe ? »).
- Pages : catégories, pages sans menu, ancres, liens hypertextes, redirections 301/302.
- **Option CSS par ligne** : affecter un style au contenu d'une ligne donnée sans toucher aux autres
  (dispo via l'éditeur ; périmètre exact à confirmer dans le manager).

### 4.2 Thèmes & personnalisation CSS
- Catalogue de **thèmes responsives gratuits** (le site actuel utilise un thème Bootstrap 4 basique).
- Formulaire de personnalisation du thème (couleurs, polices, etc.).
- **« Mode avancé »** du formulaire : éditer directement la feuille de style du thème (CSS global) —
  réservé à l'offre **PRO** selon le comparatif officiel.
- Zones éditables (haut/bas de site, balises META, scripts, CSS) : **PRO**.

### 4.3 Médias
- Espace de stockage (25 Mo gratuit / 3 Go PRO), **albums photos**, diaporamas, fichiers
  téléchargeables ; **URLs des fichiers récupérables** depuis le manager.
- Players audio/vidéo intégrables dans les pages.

### 4.4 Import / migration
- Import possible depuis **WordPress, Overblog, Tumblr, Blogger** (pages, articles de blog, photos) ;
  import de membres en CSV (espace membres).
- **PAS d'import de fichiers HTML bruts / de site statique** (pas de FTP, pas d'upload de pages).
- Migration sortante : pas d'export complet du site — récupération du contenu manuellement
  (textes, photos via /medias/album/…).

### 4.5 Domaine, SEO & stats
- Domaine : réservation chez e-monsite (dès 35 €/an) **ou transfert d'un domaine existant** vers
  e-monsite (tutoriel officiel « Comment transférer un domaine existant sur e-monsite ? »).
- Balises META (titre/description) : **PRO**. robots.txt : modifiable (tutoriel).
- Stats de fréquentation : simples (gratuit) / détaillées (PRO).

---

## 5. État du site actuel (observé 27/08/2026)

- https://www.cap-saaa-sqy.fr/ tourne sur le plan **GRATUIT** (lien « Créer un site internet avec
  e-monsite » visible en pied de page + bannière cookies/publicité).
- **13 pages** (12 au menu + accueil) alors que la limite affichée de l'offre gratuite est **10 pages**
  → point à éclaircir dans le manager (comptage des pages ? compte grand-père ?) — voir §9.
- Thème Bootstrap 4 basique, titre « 🐴 CAPSAAA accueil », navigation plate (daté).
- Photos hébergées sur le site (/medias/album/…) — déjà récupérées en local pour la V1.2.
- **Domaine cap-saaa-sqy.fr : registrar OVH** (créé 05/2020, expiration 05/2027, holder anonymisé),
  mais **DNS délégué chez e-monsite** (ns1/ns2.e-monsite.com). → Le domaine appartient à
  l'association (géré chez OVH) ; e-monsite n'héberge que le site + la délégation DNS.

---

## 6. Synthèse : possible / impossible

| Question | Réponse |
|---|---|
| Importer les fichiers HTML statiques (V1.2) ? | **NON** — pas de FTP, pas d'import de fichiers bruts |
| CSS personnalisé global (design V1.2) ? | **OUI mais PRO** (66 €/an) — « Mode avancé » du thème |
| JavaScript personnalisé ? | **PRO** (même badge que le CSS) |
| Blocs HTML dans les pages ? | **OUI dès le gratuit** — widget « Éditeur HTML » par ligne |
| Gestion des pages (ajout/édition/redirection) ? | **OUI** — éditeur lignes/colonnes, catégories, 301 |
| Médias / albums / fichiers à télécharger ? | **OUI** — 25 Mo gratuit, albums, URLs de fichiers |
| Nom de domaine attaché ? | **OUI** — option 35 €/an ou transfert ; l'actuel est chez OVH |
| Formulaire de contact ? | **OUI** — widget formulaire natif (dispo gratuit à confirmer) ; sinon widget HTML |
| Statistiques de visite ? | Simples (gratuit) / détaillées (PRO) |
| Traduction (pt/ar/en — exigence association) ? | **Hors gratuit** (1 langue) ; PRO = 5 langues ; widget Google Traduction via HTML à tester |
| Actualités / blog ? | Blog natif e-monsite possible (articles) — à confirmer pour la rubrique « Actualités » |
| Plus de 10 pages ? | **NON en gratuit** (limite affichée) → PRO illimité |

---

## 7. Implications pour le projet CAPSAAA

1. **Le design V1.2 n'est pas reproductible tel quel en gratuit** : pas de CSS global ni de JS sans
   PRO. Deux voies :
   - **Voie A — Gratuit strict (0 €)** : thème e-monsite proche + réglages du formulaire
     (couleurs charte #E8843A / #1E3A5F, police Inter) + **blocs HTML** pour les composants clés
     (bandeaux, cartes activités, galerie, encarts). Limites assumées : pub affichée, 10 pages
     (13 aujourd'hui !), pas de META manuel, 1 langue, pas de JS.
   - **Voie B — PRO (66 €/an)** : CSS/JS global injectable (adapter les sélecteurs V1.2 au thème
     choisi), META, 404, zones haut/bas, pages illimitées, sans pub, 5 langues.
2. **Coût vs bénéfice** : GitHub Pages = 0 € + domaine OVH déjà payé. L'argument fort d'e-monsite
   = **l'association peut gérer elle-même** (éditeur visuel, photos, actualités) sans dépendre de
   nous — c'est le critère qui justifie le budget PRO le cas échéant.
3. **Photos** : ~46 photos en local + poids total à mesurer vs 25 Mo gratuit (risque de dépassement →
   PRO 3 Go).
4. **Domaine** : reste chez OVH dans tous les cas ; si on reste chez e-monsite, on garde la
   délégation DNS actuelle ; si on part vers GitHub Pages, on change les NS/enregistrements chez OVH.
5. **SEO actuel de la V1.2** (meta, OG, JSON-LD) non transposable en gratuit ; en PRO, métas
   possibles page par page.

---

## 8. Approche proposée (à valider par Ams)

- **Étape 1 (AMS-51, en cours)** : créer un **compte e-monsite de test (offre gratuite)** → explorer
  le manager en réel : thèmes, « Mode avancé »/zone CSS, widget « Éditeur HTML », gestion des pages,
  médias, offre/produits, formulaire → compléter cette note + captures → décision **gratuit vs PRO**.
- **Étape 2 (AMS-02, construction)** : selon la décision :
  - **Recommandation initiale** : thème sobre + réglages charte + **blocs HTML** pour les composants
    clés ; passer en PRO seulement si les limites gratuites bloquent (CSS global, pages, pub, langues).
  - Comparatif détaillé thème+CSS vs blocs HTML : issue **CAPSAAA-eM 03**.
- **Contenu** : réutiliser les textes/photos de la V1.2 (déjà validés par l'association), pas de
  repartie de zéro.

---

## 9. Questions ouvertes (à vérifier dans le manager après création du compte)

1. Pourquoi 13 pages sur l'offre gratuite (limite affichée : 10) ?
2. Le widget « Éditeur HTML » accepte-t-il du JS / des iframes dans les blocs (filtrage) ?
3. Le widget formulaire natif est-il disponible en gratuit ?
4. Le widget Google Traduction (pt/ar/en) fonctionne-t-il via un bloc HTML ?
5. Poids total des photos CAPSAAA vs 25 Mo ?
6. Blog natif : peut-il servir de rubrique « Actualités » ?

---

## 10. Sources

- Offres : https://www.e-monsite.com/pages/offres/ · https://www.e-monsite.com/pages/offres/creation-site-pro.html
- Blog CSS : https://www.e-monsite.com/blog/web-design/personnaliser-son-theme-responsive-en-css-bonnes-pratiques.html
- Import : https://www.e-monsite.com/blog/do/tag/importer/
- Tutoriels : https://www.e-monsite.com/pages/tutoriels/tous-les-tutoriels/
- Aide : https://www.e-monsite.com/pages/aides-creation-site/
- FAQ FTP : https://aide.e-monsite.com/hc/fr/articles/200217781 (résumé : pas d'accès FTP, tout via le manager)
- Widget HTML : https://aide.e-monsite.com/hc/fr/articles/201453071 (intégrer un code HTML externe)
- Trick gratuit (widget Éditeur HTML dispo dès le gratuit) : https://www.mon-site-web.org/tricks/css-js-e-monsite/ajouter-une-liseuse-pdf-sur-une-page.html
- Site actuel : https://www.cap-saaa-sqy.fr/ (observation directe 27/08/2026)
- WHOIS cap-saaa-sqy.fr (OVH) + DNS (ns1/ns2.e-monsite.com) — vérifié 27/08/2026
