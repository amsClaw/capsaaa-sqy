/* ============================================
   CAPSAAA — Actualités (rubrique, PAS un blog)
   ============================================
   Pour ajouter une actualité :
   1. Ajouter une entrée dans le tableau ACTUALITES ci-dessous.
   2. Champs possibles :
      - date       : affichée dans la pastille (ex. "12 août 2026")
      - titre      : titre de la news (obligatoire)
      - corps      : corps de texte (obligatoire)
      - photo      : chemin d'une image (optionnel) — ex. "photos/xxx.jpg" (relatif à assets/)
      - lien       : adresse du lien (optionnel) — page interne (ex. "inscriptions.html") OU adresse externe
      - lienTexte  : texte affiché pour le lien (optionnel)
      - lienExterne: true si le lien pointe vers un site externe (ouvre un nouvel onglet)
   3. Enregistrer le fichier : la page Actualités se met à jour toute seule.
   ============================================ */

const ACTUALITES = [
  {
    date: "12 août 2026",
    titre: "Rentrée 2026/2027 : les inscriptions sont ouvertes !",
    corps: "La nouvelle saison démarre en septembre ! Les inscriptions aux activités aquatiques, à l'équitation adaptée, au fitness, à la musculation et au multi-sports sont ouvertes. Téléchargez la fiche d'inscription dans la section Documents, ou contactez-nous pour venir essayer une activité avant de vous inscrire.",
    photo: "photos/pique-nique-base-de-loisirs-saint-quentin.jpg",
    lien: "inscriptions.html",
    lienTexte: "Voir les inscriptions"
  },
  {
    date: "28 juillet 2026",
    titre: "Une belle journée à la base de loisirs de Saint-Quentin",
    corps: "Notre sortie annuelle à la base de loisirs de Saint-Quentin-en-Yvelines a rassemblé une trentaine d'adhérents et de bénévoles pour un pique-nique convivial et des jeux au bord de l'eau. Merci à tous les participants et aux organisateurs !",
    photo: "photos/photo-2023-06-26-23-16-59.jpg",
    lien: "galerie.html",
    lienTexte: "Voir les photos de la sortie"
  },
  {
    date: "3 juillet 2026",
    titre: "CAPSAAA au forum des associations",
    corps: "Retrouvez-nous en septembre au forum des associations pour découvrir nos activités et échanger avec nos bénévoles. C'est aussi l'occasion de rencontrer nos éducateurs sportifs et de poser toutes vos questions sur le sport adapté à Saint-Quentin-en-Yvelines.",
    lien: "https://www.sqy.fr",
    lienExterne: true,
    lienTexte: "Site de Saint-Quentin-en-Yvelines"
  }
];
