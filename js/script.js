/* ============================================
   CAPSAAA — JavaScript
   ============================================ */

document.addEventListener('DOMContentLoaded', function() {

  // ---- Mobile Nav Toggle ----
  const navToggle = document.querySelector('.nav-toggle');
  const navMenu = document.querySelector('.nav-menu');

  if (navToggle && navMenu) {
    navToggle.addEventListener('click', function() {
      this.classList.toggle('active');
      navMenu.classList.toggle('open');
    });

    // Close menu on link click
    navMenu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        navToggle.classList.remove('active');
        navMenu.classList.remove('open');
      });
    });
  }

  // ---- Active nav link based on current page ----
  const currentPath = window.location.pathname;
  document.querySelectorAll('.nav-menu a').forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPath ||
        (currentPath.endsWith('/') && href === 'index.html') ||
        (currentPath.endsWith('index.html') && href === 'index.html') ||
        (currentPath.endsWith(href) && href !== 'index.html' && href !== '/')) {
      link.classList.add('active');
    }
  });

  // ---- Smooth scroll for anchor links ----
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#') return;
      const target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });

  // ---- Lightbox (Gallery) ----
  const lightbox = document.getElementById('lightbox');
  const lightboxImg = lightbox ? lightbox.querySelector('img') : null;
  const lightboxClose = lightbox ? lightbox.querySelector('.lightbox-close') : null;

  if (lightbox && lightboxImg) {
    document.querySelectorAll('.gallery-item').forEach(item => {
      item.addEventListener('click', function() {
        const img = this.querySelector('img');
        if (img) {
          lightboxImg.src = img.src;
          lightboxImg.alt = img.alt;
          lightbox.classList.add('open');
          document.body.style.overflow = 'hidden';
        }
      });
    });

    function closeLightbox() {
      lightbox.classList.remove('open');
      document.body.style.overflow = '';
    }

    if (lightboxClose) {
      lightboxClose.addEventListener('click', closeLightbox);
    }

    lightbox.addEventListener('click', function(e) {
      if (e.target === this) closeLightbox();
    });

    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape') closeLightbox();
    });
  }

  // ---- Counter Animation (stats) ----
  const counters = document.querySelectorAll('.stat-item h3');
  if (counters.length > 0) {
    let countersAnimated = false;

    function animateCounters() {
      if (countersAnimated) return;
      countersAnimated = true;

      counters.forEach(counter => {
        const target = parseInt(counter.getAttribute('data-target'));
        if (isNaN(target)) return;

        const duration = 2000;
        const step = Math.max(1, Math.floor(target / 60));
        let current = 0;

        const updateCounter = () => {
          current += step;
          if (current < target) {
            counter.textContent = current + (counter.textContent.includes('%') ? '%' : '');
            requestAnimationFrame(updateCounter);
          } else {
            counter.textContent = target + (counter.textContent.includes('%') ? '%' : '');
          }
        };

        updateCounter();
      });
    }

    // Intersection Observer for counter animation
    const statsSection = document.querySelector('.stats-grid');
    if (statsSection) {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            animateCounters();
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.3 });
      observer.observe(statsSection);
    }
  }

  // ---- Contact form — envoi standard FormSubmit (V1.2.2) :
  // le submit natif du formulaire part vers formsubmit.co (action du <form>),
  // avec captcha « je ne suis pas un robot » vérifié côté serveur (le captcha
  // ne fonctionne pas en mode AJAX). Les champs required gèrent la validation.

  // ---- Actualités : rendu depuis js/actualites.js (facile à mettre à jour) ----
  // #actualites-list = page complète | #actualites-home = aperçu accueil (2 max)
  // Les chemins du fichier de données sont relatifs à la racine du site :
  // on ajoute le préfixe selon que la page courante est dans /pages/ ou à la racine.
  const inPages = window.location.pathname.indexOf('/pages/') !== -1;
  const P = { assets: inPages ? '../assets/' : 'assets/', pages: inPages ? '' : 'pages/' };
  const newsContainers = document.querySelectorAll('#actualites-list, #actualites-home');
  if (newsContainers.length && typeof ACTUALITES !== 'undefined') {
    newsContainers.forEach(function(newsContainer) {
      const isHome = newsContainer.id === 'actualites-home';
      const items = isHome ? ACTUALITES.slice(0, 2) : ACTUALITES;
      if (items.length === 0) {
        newsContainer.innerHTML = '<p class="news-empty">Aucune actualité pour le moment. Revenez bientôt !</p>';
      } else {
        newsContainer.innerHTML = items.map(function(n) {
          const photo = n.photo
            ? '<div class="news-item-img"><img src="' + P.assets + n.photo + '" alt="' + n.titre + '" loading="lazy"></div>'
            : '';
          const ext = n.lien && /^https?:\/\//.test(n.lien);
          const lien = n.lien
            ? '<p><a class="news-link" href="' + (ext ? n.lien : P.pages + n.lien) + '"' + (ext || n.lienExterne ? ' target="_blank" rel="noopener"' : '') + '>' + n.lienTexte + ' →</a></p>'
            : '';
          return '<article class="news-item' + (n.photo ? ' has-photo' : '') + '">' + photo +
            '<div class="news-item-body">' +
            '<span class="news-date">' + n.date + '</span>' +
            '<h3>' + n.titre + '</h3>' +
            '<p>' + n.corps + '</p>' +
            lien +
            '</div></article>';
        }).join('');
      }
    });
  }

});
