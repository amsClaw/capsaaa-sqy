# 📊 Guide simple : créer le compte Google Analytics du site CAPSAAA

> **Pour qui ?** François et les membres de l'association (aucune connaissance technique requise).
> **Pourquoi ?** Pour savoir combien de personnes visitent le site, quelles pages elles regardent, et d'où elles viennent.
> **Durée :** environ 15 minutes, une seule fois.

---

## 🎯 Ce que vous saurez grâce à cet outil

- Combien de **visites** le site reçoit (par jour, par semaine, par mois)
- Quelles **pages** sont les plus consultées (Activités ? Galerie ? Contact ?)
- D'où viennent les visiteurs (Google, Facebook, lien direct…)
- Sur quel **appareil** ils naviguent (téléphone ou ordinateur)
- Depuis quelle **ville / région** ils se connectent

**Rien à installer, rien à payer.** C'est un service gratuit de Google.

---

## 📝 Étape 1 : Préparer votre compte Google

1. Il faut un **compte Google** (Gmail) pour continuer.
   - Si l'association en a déjà un → utilisez-le.
   - Sinon, créez-en un ici : https://accounts.google.com/signup
   - ⚠️ **Conseil** : utilisez l'adresse de l'association (capaaasqy@hotmail.fr) ou créez une adresse dédiée comme `capsaaa.site@gmail.com`. Cela évitera que le suivi dépende d'une personne en particulier.

---

## 🖥️ Étape 2 : Créer le compte Analytics

1. Ouvrez votre navigateur et allez sur : **https://analytics.google.com**
2. Si demandé, **connectez-vous avec le compte Google** de l'étape 1.
3. Vous arrivez sur une page d'accueil → cliquez sur **« Commencer à mesurer »** (ou « Start measuring »).
4. Renseignez le formulaire de création du **compte** :
   - **Nom du compte** : `CAPSAAA`
   - **Partage de données** : laissez les cases par défaut (ce n'est pas bloquant)
   - Cliquez sur **Suivant**.
5. Puis renseignez la **propriété** (c'est le site lui-même) :
   - **Nom de la propriété** : `Site CAPSAAA`
   - **Fuseau horaire** : `(GMT+01:00) Paris`
   - **Devise** : `Euro (€)`
   - Cliquez sur **Suivant**.
6. Renseignez les informations sur l'**entreprise** (sans importance, vous pouvez répondre simplement) :
   - Secteur : `Associations / à but non lucratif`
   - Taille : `1-10`
   - Cliquez sur **Créer**.
7. Acceptez les **conditions d'utilisation** si demandé.

✅ Votre compte Analytics est créé !

---

## 🌐 Étape 3 : Créer le « flux de données » (l'étape importante)

C'est ici qu'on dit à Google : « le site à suivre, c'est celui-là ».

1. Dans le menu de gauche, cliquez sur **Administrateur** (icône ⚙️ en bas à gauche).
2. Dans la colonne **Propriété**, cliquez sur **Flux de données** (ou « Data streams »).
3. Cliquez sur le bouton **+ Ajouter un flux de données** (bleu).
4. Choisissez **Web** (l'icône du globe 🌐).
5. Renseignez :
   - **URL du site** : `https://www.cap-saaa-sqy.fr` (l'adresse définitive du site)
   - **Nom du flux** : `Site CAPSAAA`
6. Cliquez sur **Créer le flux**.

Vous arrivez sur la page de détails du flux. 👉 **Important : notez le numéro qui commence par « G- »** (exemple : `G-XXXXXXXXXX`). C'est l'**identifiant de mesure** — c'est ce numéro que nous devons recevoir pour brancher le site dessus.

---

## ✉️ Étape 4 : Nous transmettre l'identifiant

1. Sur la page du flux, repérez le champ **« Identifiant de mesure »** (il commence par `G-`).
2. **Copiez ce numéro** (clic droit → Copier).
3. **Envoyez-le-nous par mail** avec une petite phrase, par exemple :
   > « Bonjour, voici l'identifiant de mesure du site : G-XXXXXXXXXX »

C'est tout ! 🎉 Nous nous occupons de l'installer sur le site (quelques minutes de notre côté).

---

## 👀 Étape 5 (plus tard) : Consulter les statistiques

Après quelques jours, vous pourrez voir les visites :

1. Allez sur **https://analytics.google.com** (connecté avec le même compte).
2. Cliquez sur **Rapports** dans le menu de gauche.
3. Puis **« Aperçu »** (ou « Rapports en temps réel » pour voir les visites du moment).
4. Vous verrez : le nombre de visiteurs, les pages vues, les pays, les appareils…
   - 💡 **Astuce** : Google Analytics met ~24 à 48 h pour afficher les données complètes. Le premier jour, ne soyez pas surpris si les chiffres sont faibles.

---

## ❓ Questions fréquentes

**« Est-ce que ça coûte de l'argent ? »**
Non. La version gratuite de Google Analytics suffit largement pour le site de l'association.

**« Est-ce que je dois installer quelque chose sur mon ordinateur ? »**
Non. Tout se passe dans le navigateur internet, comme pour consulter vos mails.

**« Est-ce que les visiteurs doivent faire quelque chose ? »**
Non. Le compteur fonctionne tout seul, en arrière-plan, sans rien demander aux visiteurs.

**« J'ai perdu mon identifiant G-…, comment le retrouver ? »**
Connectez-vous sur analytics.google.com → **Administrateur** ⚙️ → **Flux de données** → cliquez sur votre flux → l'identifiant est affiché en haut de la page.

**« On peut voir les statistiques à plusieurs ? »**
Oui. Ajoutez d'autres membres de l'association : **Administrateur** ⚙️ → **Gestion des accès** → bouton **+** → entrez leur adresse mail → rôle **Lecteur** (ils pourront voir les chiffres sans rien casser).

---

*Document préparé par l'équipe de développement du site CAPSAAA — pour toute question, écrivez-nous.*
