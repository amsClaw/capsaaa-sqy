"""Retours de François du 23/10/2026 (« modifs et mise en production ») sur le site statique.

Fitness au gymnase Jean Guimier, nouvelles photos (accueil, Fitness, Multi-Sports), Multi-Sports
dès 12 ans, 8 cavaliers sur Nous rejoindre, Galerie (photos retirées, rubrique Sensibilisations
2025/2026, plus de section « Toutes »). Le tableau des tarifs se remplace à part (fichier PDF).
Photo Fitness du centre : qbia3436 provisoire, en attendant « Remplacement Fitness Centre.JPG ».

Usage : python3 tools/corrections_2026_10_23.py [--ecrire]
"""
import pathlib, re, sys

R = pathlib.Path(__file__).resolve().parent.parent
GUIMIER_Q = "Gymnase+Jean+Guimier+10+avenue+Eug%C3%A8ne+Delacroix+Trappes"


def un(s, old, new, n=1):
    assert s.count(old) == n, (s.count(old), old[:90])
    return s.replace(old, new)


def item(src, label):
    return (f'          <div class="gallery-item"><img src="../assets/photos/{src}" alt="{label}" loading="lazy">'
            f'<span class="gallery-label">{label}</span></div>\n')


def accueil(s):
    s = un(s, 'src="assets/photos/etirements.jpg" alt="Fitness"', 'src="assets/photos/fitness-accueil.jpg" alt="Fitness"')
    return un(s, 'src="assets/photos/pique-nique-base-de-loisirs-saint-quentin.jpg" alt="Multi Sports"',
              'src="assets/photos/multisport-ping-pong-double.jpg" alt="Multi Sports"')


def activites(s):
    s = un(s, 'src="../assets/photos/etirements.jpg" alt="Fitness"', 'src="../assets/photos/fitness-accueil.jpg" alt="Fitness"')
    s = un(s, '<span class="activity-tag">Gymnase Broustal — Trappes</span>', '<span class="activity-tag">Gymnase Jean Guimier — Trappes</span>')
    s = un(s, 'src="../assets/photos/hexg8906-1.jpg" alt="Multi-Sports"', 'src="../assets/photos/multisport-ping-pong-double.jpg" alt="Multi-Sports"')
    return un(s, "selon les envies et capacités, dès 15 ans.", "selon les envies et capacités, dès 12 ans.")


def fitness(s):
    s = un(s, "— Gymnase Broustal, Trappes.", "— Gymnase Jean Guimier, Trappes.")
    s = un(s, "assets/photos/etirements.jpg", "assets/photos/fitness-accueil.jpg", 2)   # og:image + photo de titre
    s = un(s, "Gymnase Broustal — 6 av. Ludwig Van Beethoven, 78190 Trappes",
           "Gymnase Jean Guimier — 10 avenue Eugène Delacroix, 78190 Trappes")
    s = un(s, "query=Gymnase+Broustal+6+avenue+Ludwig+Van+Beethoven+Trappes", "query=" + GUIMIER_Q)
    s = un(s, 'src="../assets/photos/exmf9076.jpg" alt="Fitness — photo CAPSAAA"', 'src="../assets/photos/fitness-gauche.jpg" alt="Fitness — photo CAPSAAA"')
    return un(s, 'src="../assets/photos/img-5562.jpg" alt="Fitness — photo CAPSAAA"', 'src="../assets/photos/fitness-droite.jpg" alt="Fitness — photo CAPSAAA"')


def multisport(s):
    s = un(s, 'content="https://cap-saaa-sqy.fr/assets/photos/hexg8906-1.jpg"', 'content="https://cap-saaa-sqy.fr/assets/photos/multisport-ping-pong-double.jpg"')
    s = un(s, "<p>À partir de 15 ans — tous types de handicap</p>", "<p>À partir de 12 ans — tous types de handicap</p>")
    s = un(s, 'src="../assets/photos/hexg8906-1.jpg" alt="Multi-Sports — photo CAPSAAA"', 'src="../assets/photos/multisport-tir-basket.jpg" alt="Multi-Sports — photo CAPSAAA"')
    return un(s, 'src="../assets/photos/on-se-prepare-a-jouer.jpg" alt="Multi-Sports — photo CAPSAAA"', 'src="../assets/photos/multisport-raquette-fauteuil.jpg" alt="Multi-Sports — photo CAPSAAA"')


def inscriptions(s):
    s = un(s, "Dès 6 ans — 7 cavaliers max", "Dès 6 ans — 8 cavaliers max")
    s = un(s, "<p><strong>Lieu :</strong> Gymnase Broustal — Trappes</p>", "<p><strong>Lieu :</strong> Gymnase Jean Guimier — Trappes</p>")
    return un(s, "<p><strong>Âge :</strong> Dès 15 ans</p>", "<p><strong>Âge :</strong> Dès 12 ans</p>")


def galerie(s):
    # Fitness : les 3 photos remplacées par les nouvelles (celle du centre arrivera plus tard)
    a = s.index('<div class="gallery-section" id="tab-fitness">')
    b = s.index('</div>\n      </div>', a)
    g0 = s.index('<div class="gallery-grid">\n', a) + len('<div class="gallery-grid">\n')
    s = s[:g0] + item("fitness-gauche.jpg", "Fitness") + item("fitness-droite.jpg", "Fitness") + "        " + s[b:]
    s = un(s, '<h2>🤸 Fitness <span class="photo-count">3 photos</span></h2>', '<h2>🤸 Fitness <span class="photo-count">2 photos</span></h2>')
    # photos retirées
    s = un(s, item("anne-et-fessal.jpg", "Anne et Fayçal"), "")
    s = un(s, '<h2>💪 Musculation <span class="photo-count">6 photos</span></h2>', '<h2>💪 Musculation <span class="photo-count">5 photos</span></h2>')
    s = un(s, item("on-se-prepare-a-jouer.jpg", "On se prépare à jouer"), "")
    s = un(s, '<h2>🎯 Multi-Sports <span class="photo-count">4 photos</span></h2>', '<h2>🎯 Multi-Sports <span class="photo-count">3 photos</span></h2>')
    s = un(s, item("img-5563.jpg", "Torball") + item("img-5628.jpg", "Torball"), "")
    # nouvelle rubrique Sensibilisations 2025/2026, après 2024/2025
    nouv = ("\n        <h3 style=\"margin-top:30px\">Actions de sensibilisation 2025/2026</h3>\n        <div class=\"gallery-grid\">\n"
            + item("sensi-passage-de-porte.jpg", "Passage de porte") + item("sensi-basket-fauteuil.jpg", "Basket fauteuil")
            + item("sensi-atelier-sensoriel.jpg", "Atelier sensoriel") + item("sensi-parcours-basket.jpg", "Parcours basket")
            + item("sensi-boccia.jpg", "Boccia") + "        </div>\n")
    a = s.index("<h3>Actions de sensibilisations 2024/2025</h3>")
    fin = s.index("        </div>\n", a) + len("        </div>\n")
    s = s[:fin] + nouv + s[fin:]
    s = un(s, '<h2>♿ Les sensibilisations <span class="photo-count">14 photos</span></h2>', '<h2>♿ Les sensibilisations <span class="photo-count">17 photos</span></h2>')
    # plus de section « Toutes les photos »
    s = un(s, '        <button data-tab="toutes">📸 Toutes</button>\n', "")
    a = s.index("      <!-- ===== TOUTES ===== -->")
    b = s.index("    </div>\n  </section>", a)
    s = s[:a] + s[b:]
    assert "tab-toutes" not in s and "Toutes les photos" not in s
    return s


FICHIERS = {"index.html": accueil, "pages/activites.html": activites, "pages/activite-fitness.html": fitness,
            "pages/activite-multisport.html": multisport, "pages/inscriptions.html": inscriptions, "pages/galerie.html": galerie}

if __name__ == "__main__":
    nouveaux = {f: fn((R / f).read_text()) for f, fn in FICHIERS.items()}
    for f, s in nouveaux.items():
        print(f"{f:32s} {len((R / f).read_text())} → {len(s)} car.")
    if "--ecrire" in sys.argv:
        for f, s in nouveaux.items():
            (R / f).write_text(s)
        print("écrit")
