#!/usr/bin/env python3
"""Génère les PDF téléchargeables pour le site CAPSAAA (assets/docs/)."""
import os
from fpdf import FPDF

OUT = os.path.join(os.path.dirname(__file__), "..", "assets", "docs")
os.makedirs(OUT, exist_ok=True)

BLUE = (30, 58, 95)
ORANGE = (232, 132, 58)
GREY = (90, 90, 90)

FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"


class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.add_font("Arial", "", FONT_REG)
        self.add_font("Arial", "B", FONT_BOLD)

    def header(self):
        self.set_font("Arial", "B", 10)
        self.set_text_color(*BLUE)
        self.cell(0, 8, "CAPSAAA — CAP Sport Art Aventure Amitié", new_x="LMARGIN", new_y="NEXT", align="L")
        self.set_font("Arial", "", 8)
        self.set_text_color(*GREY)
        self.cell(0, 5, "Association loi 1901 — 14 rue Mansart, 78190 Trappes — capaaasqy@hotmail.fr — 06 03 41 45 30",
                  new_x="LMARGIN", new_y="NEXT", align="L")
        self.set_draw_color(*ORANGE)
        self.set_line_width(0.6)
        self.line(10, self.get_y() + 1, 200, self.get_y() + 1)
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "", 8)
        self.set_text_color(*GREY)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def section(self, title):
        self.set_font("Arial", "B", 12)
        self.set_text_color(*ORANGE)
        self.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def line_fields(self, fields):
        self.set_font("Arial", "", 10)
        self.set_text_color(0, 0, 0)
        for label in fields:
            self.cell(0, 7, label, new_x="LMARGIN", new_y="NEXT")
            self.set_draw_color(180, 180, 180)
            self.line(12, self.get_y() + 1, 198, self.get_y() + 1)
            self.ln(6)


# ============ FICHE D'INSCRIPTION ============
pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.set_text_color(*BLUE)
pdf.cell(0, 10, "FICHE D'INSCRIPTION — SAISON 2026/2027", new_x="LMARGIN", new_y="NEXT", align="C")
pdf.ln(2)
pdf.set_font("Arial", "", 9)
pdf.set_text_color(*GREY)
pdf.cell(0, 5, "À retourner complétée et signée à CAPSAAA — 14 rue Mansart, 78190 Trappes",
         new_x="LMARGIN", new_y="NEXT", align="C")
pdf.cell(0, 5, "ou par email : capaaasqy@hotmail.fr", new_x="LMARGIN", new_y="NEXT", align="C")
pdf.ln(6)

pdf.section("1. Renseignements sur le pratiquant")
pdf.line_fields([
    "Nom :", "Prénom :", "Date de naissance :", "Adresse :", "Code postal / Ville :",
    "Téléphone :", "Email :", "Personne à prévenir en cas d'urgence (nom + téléphone) :",
])

pdf.section("2. Activité(s) choisie(s)")
pdf.line_fields([
    "[ ] Activités aquatiques (Piscine Monquaut — Trappes)",
    "[ ] Équitation adaptée (Club SQY Équitation — Île aux Loisirs)",
    "[ ] Musculation (Gymnase Aviation — Guyancourt)",
    "[ ] Fitness (Salle Auguste-Renoir — Guyancourt)",
    "[ ] Multi-Sports (Gymnase Aviation — Guyancourt)",
])

pdf.section("3. Santé")
pdf.line_fields([
    "Certificat médical de non-contre-indication à la pratique sportive adaptée : [ ] fourni  [ ] à fournir",
    "Particularités / recommandations médicales (allergies, traitement, matériel spécifique…) :",
])

pdf.section("4. Autorisations et engagement")
pdf.set_font("Arial", "", 10)
pdf.multi_cell(0, 6,
    "J'autorise CAPSAAA à utiliser les photos prises lors des activités pour la communication interne "
    "et les supports de l'association (site internet, affiches, réseaux sociaux).  [ ] Oui   [ ] Non\n\n"
    "J'accepte le règlement intérieur de l'association et m'engage à respecter les consignes des encadrants "
    "et les règles de sécurité propres à chaque activité.\n\n"
    "Pour les mineurs : autorisation parentale obligatoire. Le parent ou tuteur légal signe ci-dessous.",
    new_x="LMARGIN", new_y="NEXT")
pdf.ln(4)
pdf.line_fields([
    "Date :", "Signature du pratiquant (ou du représentant légal pour un mineur) :",
])

pdf.output(os.path.join(OUT, "fiche-inscription-capsaaa.pdf"))

# ============ RÈGLEMENT INTÉRIEUR ============
pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.set_text_color(*BLUE)
pdf.cell(0, 10, "RÈGLEMENT INTÉRIEUR — CAPSAAA", new_x="LMARGIN", new_y="NEXT", align="C")
pdf.ln(6)

sections = [
    ("Article 1 — Objet",
     "Le présent règlement intérieur complète les statuts de l'association CAPSAAA (CAP Sport Art Aventure "
     "Amitié), association loi 1901 d'intérêt général, agréée Jeunesse et Sports et affiliée à la Fédération "
     "Française des Sports pour Tous. Il s'applique à tous les adhérents, accompagnants et bénévoles."),
    ("Article 2 — Adhésion",
     "L'adhésion est ouverte à toute personne, à partir de 6 ans et sans limite d'âge, en situation de handicap "
     "(physique, psychique, mental ou sensoriel) ainsi qu'aux personnes valides souhaitant pratiquer une activité "
     "à un rythme adapté. Elle est validée après inscription, règlement de la cotisation et, le cas échéant, "
     "présentation d'un certificat médical de non-contre-indication."),
    ("Article 3 — Activités",
     "Les activités proposées sont : les activités aquatiques (Piscine Monquaut, Trappes), l'équitation adaptée "
     "(Club SQY Équitation, Île aux Loisirs), la musculation et le multi-sports (Gymnase Aviation, Guyancourt), "
     "le fitness (Salle Auguste-Renoir, Guyancourt), ainsi que les sorties et événements organisés par l'association. "
     "Les horaires et lieux sont communiqués en début de saison et peuvent être adaptés par le bureau."),
    ("Article 4 — Sécurité et encadrement",
     "Chaque activité est encadrée par des éducateurs sportifs diplômés ou des bénévoles formés. Les consignes de "
     "sécurité données par les encadrants doivent être strictement respectées. Les pratiquants non autonomes doivent "
     "être accompagnés d'un adulte valide. Tout incident ou malaise doit être signalé immédiatement à l'encadrant."),
    ("Article 5 — Tenue et matériel",
     "Une tenue adaptée à chaque activité est requise (maillot de bain et bonnet pour la piscine, tenue de sport "
     "pour le gymnase, chaussures fermées adaptées). Le matériel mis à disposition (fauteuil de mise à l'eau, "
     "Motomed, etc.) doit être utilisé avec soin."),
    ("Article 6 — Assiduité et annulations",
     "En cas d'absence ou d'annulation, l'adhérent prévient l'association dans la mesure du possible. Les séances "
     "annulées par l'association (fermeture d'équipement, météo, etc.) seront rattrapées ou remboursées selon les "
     "modalités fixées par le bureau."),
    ("Article 7 — Comportement",
     "Les adhérents s'engagent à adopter un comportement respectueux envers les autres pratiquants, les encadrants "
     "et le matériel. L'association se réserve le droit d'exclure temporairement ou définitivement tout adhérent "
     "dont le comportement compromettrait la sécurité ou le bon déroulement des activités."),
    ("Article 8 — Assurance",
     "Chaque adhérent bénéficie de la couverture de l'association dans le cadre de l'affiliation à la Fédération "
     "Française des Sports pour Tous. L'association décline toute responsabilité pour les dommages causés par un "
     "adhérent en dehors du cadre des activités."),
    ("Article 9 — Image",
     "Des photos peuvent être prises lors des activités pour la communication de l'association. Toute personne "
     "pouvant y figurer dispose d'un droit d'opposition à exercer auprès du bureau."),
    ("Article 10 — Tarifs et cotisations",
     "Les montants des cotisations sont fixés par l'assemblée générale et communiqués lors de l'inscription. "
     "Le paiement de la cotisation conditionne la participation aux activités."),
    ("Article 11 — Modification du règlement",
     "Toute modification du présent règlement intérieur est soumise à l'approbation du conseil d'administration "
     "ou de l'assemblée générale."),
]
for title, body in sections:
    pdf.set_font("Arial", "B", 11)
    pdf.set_text_color(*ORANGE)
    pdf.cell(0, 7, title, new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Arial", "", 10)
    pdf.set_text_color(0, 0, 0)
    pdf.multi_cell(0, 5.5, body, new_x="LMARGIN", new_y="NEXT")
    pdf.ln(3)

pdf.output(os.path.join(OUT, "reglement-interieur-capsaaa.pdf"))

print("PDF générés :")
for f in sorted(os.listdir(OUT)):
    p = os.path.join(OUT, f)
    print(f"  {p} ({os.path.getsize(p)} octets)")
