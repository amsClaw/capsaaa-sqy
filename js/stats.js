/* ============================================================
 * CAPSAAA — Statistiques de visite (Google Analytics 4)
 * ------------------------------------------------------------
 * DÉSACTIVÉ par défaut : tant que gaMeasurementId est vide,
 * ce fichier ne charge rien (aucun script, aucun cookie).
 *
 * Activation (une fois le client connecté — ~15 min, sans
 * prérequis technique, voir docs/GUIDE_GOOGLE_ANALYTICS_SIMPLE.md) :
 *   1. Le client crée le compte GA4 + le flux de données web
 *      (le guide simple lui a été fourni).
 *   2. Il nous transmet l'identifiant de mesure « G-XXXXXXXXXX ».
 *   3. Coller cet identifiant dans CAPSAAA_STATS.gaMeasurementId.
 *   4. Publier. Les données apparaissent sous 24-48 h.
 *
 * Note RGPD : GA4 anonymise les adresses IP par défaut.
 * Si un bandeau de consentement cookies est ajouté plus tard,
 * activer le Consent Mode GA4 (gtag('consent', ...)).
 * ============================================================ */
const CAPSAAA_STATS = {
  gaMeasurementId: "", // ex: "G-XXXXXXXXXX" — à renseigner quand François l'aura transmis
};

(function () {
  const id = CAPSAAA_STATS.gaMeasurementId;
  if (!id) return; // pas d'ID → aucun chargement, aucun suivi

  // 1) Chargement de la balise gtag.js
  const s = document.createElement("script");
  s.async = true;
  s.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(id);
  document.head.appendChild(s);

  // 2) dataLayer + fonction gtag (les appels avant le chargement
  //    de gtag.js sont mis en file et rejoués par la balise)
  window.dataLayer = window.dataLayer || [];
  function gtag() {
    window.dataLayer.push(arguments);
  }
  window.gtag = gtag;

  // 3) Configuration de la propriété (envoie automatiquement
  //    la page_vue sur chaque page)
  gtag("js", new Date());
  gtag("config", id);
})();
