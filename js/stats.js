/* ============================================================
 * CAPSAAA — Statistiques de visite (RGPD friendly)
 * ------------------------------------------------------------
 * Désactivé par défaut. Activation en 2 minutes :
 *
 *   Option A (recommandée — RGPD friendly, données auto-hébergées)
 *     Matomo (Cloud ou auto-hébergé) :
 *       1. Créer un site « CAPSAAA » dans Matomo.
 *       2. Copier l'URL du serveur (ex: https://xxx.matomo.cloud)
 *          et l'ID du site (siteId, ex: 1) dans CAPSAAA_STATS.
 *       3. Le consentement (setConsentGiven) est géré ici ;
 *          activer aussi « Exiger le consentement » dans Matomo
 *          (Vie privée > Utilisateurs) si souhaité.
 *
 *   Option B — Google Analytics 4
 *     Remplacer ce fichier par le snippet GA4 fourni par Google
 *     (Mesurer > Flux de données > Web > balise).
 *
 *   Option C — Cloudflare Web Analytics
 *     Si le site est servi par Cloudflare Pages : coller le beacon
 *     <script defer src="https://static.cloudflareinsights.com/beacon.min.js" ...>
 *     dans le <head> des pages (pas besoin de ce fichier).
 * ============================================================ */
const CAPSAAA_STATS = {
  matomoUrl: "",        // ex: "https://capsaaa.matomo.cloud"
  matomoSiteId: 0,      // ex: 1
};

(function () {
  if (!CAPSAAA_STATS.matomoUrl || !CAPSAAA_STATS.matomoSiteId) return;
  var _paq = (window._paq = window._paq || []);
  _paq.push(["setConsentGiven"]);
  _paq.push(["trackPageView"]);
  _paq.push(["enableLinkTracking"]);
  (function () {
    var u = CAPSAAA_STATS.matomoUrl;
    _paq.push(["setTrackerUrl", u + "/matomo.php"]);
    _paq.push(["setSiteId", String(CAPSAAA_STATS.matomoSiteId)]);
    var d = document,
      g = d.createElement("script"),
      s = d.getElementsByTagName("script")[0];
    g.async = true;
    g.src = u + "/matomo.js";
    s.parentNode.insertBefore(g, s);
  })();
})();
