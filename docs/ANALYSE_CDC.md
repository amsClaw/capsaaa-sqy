# Analyse comparative : CDC vs Version actuelle

> Cahier des charges v1 (mars 2026) — François LECOMBE
> Version actuelle développée par Ams (juillet 2026)

## Légende

| Symbole | Signification |
|---|---|
| ✅ | Déjà fait |
| 🟡 | Partiellement fait / à adapter |
| 🔴 | Pas fait |
| ⬜ | Hors scope / à décider |

---

## 1. Contenu & arborescence

| Rubrique CDC | Statut | Commentaire | Action |
|---|---|---|---|
| **Accueil** (photo, adresse, actu) | ✅ | Photo + adresse OK. Actu non présente mais peut venir du blog | Ajouter une section actu si blog créé |
| **Institutionnel / Origine** | ✅ | Présent dans Qui sommes-nous | RAS |
| **Dirigeants / CA** | ✅ | Bureau + CA listés | RAS |
| **CAPSAAA en chiffres et images** | ✅ | Stats animées sur l'accueil | RAS |
| **Nous joindre** (adresse, tél, formulaire) | ✅ | Page contact complète | RAS |
| **Activités** (5 activités détaillées) | ✅ | 5 activités avec lieu, horaire, description | RAS |
| **Blog interactif** (publication + commentaires) | 🔴 | Pas de blog dans la version actuelle | **À créer** (section blog ou actu) |
| **Actualités** | 🟡 | Pas de section dédiée. À voir si distincte du blog ou fusionnée | Clarifier avec François |
| **Partenaires** | ✅ | Logos + rôles présents | RAS |
| **Liens utiles** | ✅ | Présent sur la page Partenaires | RAS |
| **Documents** (fiches inscription…) | 🟡 | Liens vers docs d'inscription à intégrer | Ajouter section téléchargements |

## 2. Fonctionnalités

| Fonction CDC | Statut | Commentaire | Action |
|---|---|---|---|
| **Design moderne, responsive** | ✅ | Fait | RAS |
| **Charte graphique orange** | ✅ | Orange #E8843A | RAS |
| **Couleur spécifique par activité** (ex: bleu pour piscine) | 🟡 | Pas dans la version actuelle | Option esthétique légère à ajouter |
| **Navigation mobile** | ✅ | Menu hamburger, responsive | RAS |
| **Galerie photos / lightbox** | ✅ | 7 albums, 48 photos | RAS |
| **Blog / commentaires** | 🔴 | Pas de backend | **À décider** (solution statique ou dynamique) |
| **Statistiques de trafic** | 🔴 | Pas d'analytics | Ajouter Matomo (gratuit, RGPD friendly) ou Google Analytics |
| **Référencement SEO** "sport + handicap" | 🟡 | Balises meta de base présentes | Optimiser le SEO (mots-clés, descriptions, balises) |
| **Administrateur non-informaticien** peut modifier le site | 🔴 | Site statique = modification dans le code | **Point clé** : voir ci-dessous |
| **Traduction automatique** | 🔴 | Pas de multilangue | Gadget à priori, option Google Traduction intégré |
| **Formulaire de contact fonctionnel** | 🟡 | UI présente mais pas de backend | Ajouter Formspree / Netlify Forms |
| **Sécurité du site** | ✅ | Site statique = pas de surface d'attaque | RAS |

## 3. Hébergement & technique

| Point CDC | Statut | Commentaire | Action |
|---|---|---|---|
| **AssoConnect** | ⬜ | Pas une obligation selon Ams. Option si besoin futur | Ignorer pour la V1 |
| **Hébergement** | 🔴 | Pas encore déployé | Déploiement à prévoir |
| **Nom de domaine** cap-saaa-sqy.fr | 🟡 | Transfert à accompagner si nécessaire | À voir avec François |
| **Formation utilisateur** | 🔴 | À prévoir si admin non-technique | Planifier après V1 |
| **Assistance & maintenance** | 🔴 | À définir avec François | Cadrer le contrat |
| **Promotion & référencement** | 🔴 | À accompagner | SEO + annuaire |

---

## 4. Bilan synthétique

| Niveau | Nb de points |
|---|---|
| ✅ Déjà fait | **12** |
| 🟡 Partiellement / à adapter | **5** |
| 🔴 Pas fait | **6** |
| ⬜ Hors scope V1 | **2** |

**Ta version couvre ~65% du CDC** sans les fonctionnalités qui demandent un backend (blog, admin, analytics).

---

## 5. Recommandation pour la discussion avec François

### Priorité Haute (à faire ABSOLUMENT)
1. **Rendre le formulaire de contact fonctionnel** (Formspree = 5 min, gratuit)
2. **Ajouter Matomo Analytics** (gratuit, RGPD, auto-hébergé ou cloud)
3. **Optimiser le SEO** pour "sport handicap Saint-Quentin-en-Yvelines"

### Priorité Moyenne (à proposer mais laisser François décider)
4. **Blog simple** → solution statique (page dédiée, mise à jour par Ams ou François via échange email/fichier)
5. **Section Documents** (fiches d'inscription, règlement en PDF téléchargeable)
6. **Couleur par activité** (touche esthétique rapide)

### Priorité Basse / Optionnelle (nice-to-have)
7. **Traduction automatique** (Google Translate widget = 1 ligne de code)
8. **Interface admin pour non-informaticien** → soit CMS statique (Hugo, Jekyll) soit verrouiller qu'Ams gère les màj

### Hors scope V1
9. **AssoConnect** → on verra plus tard si besoin
10. **Blog avec commentaires** → nécessite un vrai backend, pas pertinent pour une V1

---

## 6. Points à clarifier avec François

Avant de coder, ces questions méritent une réponse :

1. **Blog ou actualités ?** Veut-il vraiment un blog (publication régulière, commentaires) ou simplement une page actu qu'on met à jour ponctuellement ?
2. **Qui gère le contenu après livraison ?** Toi ? Lui ? Un bénévole ? Ça conditionne le choix technique.
3. **Le domaine cap-saaa-sqy.fr** est-il déjà chez OVH ou ailleurs ? Faut-il le transférer ?
4. **Budget / contrepartie ?** Gratuit pour l'asso ou rémunéré ? (Important pour cadrer l'effort)
