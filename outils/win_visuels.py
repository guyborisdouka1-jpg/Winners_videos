"""Visuels WIN COURS À DOMICILE (1080x1350) — bleu marine + vert, ton sérieux."""
import os
from PIL import Image, ImageDraw, ImageFont
W, H = 1080, 1350
FP = "/usr/share/fonts/truetype/google-fonts/Poppins-"
SYM = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
def f(wt, s): return ImageFont.truetype(FP + wt + ".ttf", s)
def sym(s): return ImageFont.truetype(SYM, s)
NAVY = (14, 37, 84); NAVY2 = (24, 54, 116); GREEN = (22, 163, 110); GREEN_L = (214, 243, 230)
WHITE = (255, 255, 255); SOFT = (198, 212, 238); GOLD = (244, 196, 70); INK = (20, 30, 55)
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "win"); os.makedirs(OUT, exist_ok=True)

def wrap(d, text, font, maxw):
    out = []
    for para in text.split("\n"):
        line = ""
        for w in para.split(" "):
            t = (line + " " + w).strip()
            if d.textlength(t, font=font) <= maxw or not line: line = t
            else: out.append(line); line = w
        out.append(line)
    return out
def centered(d, y, text, font, fill, maxw=940, lh=1.25):
    lines = wrap(d, text, font, maxw); h = int(font.size * lh)
    y0 = y - (len(lines) - 1) * h // 2
    for j, l in enumerate(lines): d.text((W // 2, y0 + j * h), l, font=font, fill=fill, anchor="mm")
    return len(lines) * h

def base(dark=True):
    im = Image.new("RGB", (W, H), NAVY if dark else WHITE); d = ImageDraw.Draw(im)
    if dark:
        d.ellipse((680, -260, 1400, 420), fill=NAVY2); d.ellipse((-340, 1060, 300, 1640), fill=NAVY2)
    # wordmark
    d.rounded_rectangle((50, 50, 140, 140), 22, fill=GREEN)
    d.text((95, 95), "W", font=f("Bold", 62), fill=WHITE, anchor="mm")
    tc = WHITE if dark else NAVY
    d.text((160, 78), "WIN COURS", font=f("Bold", 38), fill=tc, anchor="lm")
    d.text((160, 120), "À DOMICILE", font=f("Bold", 38), fill=GREEN, anchor="lm")
    # footer
    d.rectangle((0, H - 120, W, H), fill=GREEN)
    d.text((W // 2, H - 80), "0767037284", font=f("Bold", 46), fill=WHITE, anchor="mm")
    d.text((W // 2, H - 35), "Partout à Abidjan  •  Cocody Riviera Palmeraie", font=f("Medium", 28), fill=WHITE, anchor="mm")
    return im, d

def check_row(d, x, y, text, color=WHITE, size=40):
    d.ellipse((x, y - 26, x + 52, y + 26), fill=GREEN)
    d.text((x + 26, y), "✓", font=sym(32), fill=WHITE, anchor="mm")
    d.text((x + 76, y), text, font=f("Bold", size), fill=color, anchor="lm")

# 1 Présentation
im, d = base()
centered(d, 330, "Un répétiteur sérieux,\nchez vous.", f("Bold", 74), WHITE)
centered(d, 500, "Chaque enfant porte en lui une réussite\nqui ne demande qu'à éclore.", f("Italic", 36), SOFT)
for k, t in enumerate(["Toutes les matières", "Du primaire à la Terminale", "Tarif mensuel adapté", "Répétiteur remplacé si besoin"]):
    check_row(d, 150, 650 + k * 95, t)
d.rounded_rectangle((200, 1050, 880, 1150), 50, fill=WHITE)
d.text((540, 1100), "Appelez-nous dès aujourd'hui", font=f("Bold", 38), fill=NAVY, anchor="mm")
im.save(f"{OUT}/WIN1_presentation.png")

# 2 Comment ça marche
im, d = base(False)
centered(d, 250, "Comment ça marche ?", f("Bold", 66), NAVY)
steps = [("Vous nous appelez", "et vous nous parlez de votre enfant"), ("Nous écoutons son besoin", "classe, matières, horaires, quartier"),
         ("Nous choisissons le bon répétiteur", "adapté à votre enfant"), ("Premier cours chez vous", "dans le calme de la maison"),
         ("Nous suivons ses progrès", "et remplaçons le répétiteur si besoin")]
for k, (a, b2) in enumerate(steps):
    y = 380 + k * 155
    if k < 4: d.line((115, y + 45, 115, y + 110), fill=GREEN, width=6)
    d.ellipse((70, y - 45, 160, y + 45), fill=GREEN)
    d.text((115, y), str(k + 1), font=f("Bold", 48), fill=WHITE, anchor="mm")
    d.text((190, y - 18), a, font=f("Bold", 40), fill=NAVY, anchor="lm")
    d.text((190, y + 28), b2, font=f("Medium", 30), fill=(90, 100, 125), anchor="lm")
im.save(f"{OUT}/WIN2_comment_ca_marche.png")

# 3 Question
im, d = base()
centered(d, 320, "Parents, dites-nous :", f("Medium", 40), SOFT)
centered(d, 430, "Quelle matière fait soupirer\nvotre enfant le soir ?", f("Bold", 60), WHITE)
for k, t in enumerate(["Mathématiques", "Français", "Anglais", "Physique-Chimie / SVT"]):
    y = 590 + k * 115
    d.rounded_rectangle((120, y, 960, y + 92), 26, fill=WHITE)
    d.ellipse((140, y + 14, 204, y + 78), fill=GREEN)
    d.text((172, y + 46), "ABCD"[k], font=f("Bold", 36), fill=WHITE, anchor="mm")
    d.text((230, y + 46), t, font=f("Bold", 38), fill=NAVY, anchor="lm")
centered(d, 1100, "Répondez en commentaire", f("Bold", 42), GOLD)
im.save(f"{OUT}/WIN3_question.png")

# 4 Recrutement
im, d = base()
d.rounded_rectangle((300, 210, 780, 290), 40, fill=GOLD)
d.text((540, 250), "NOUS RECRUTONS", font=f("Bold", 42), fill=NAVY, anchor="mm")
centered(d, 410, "Des répétiteurs\nà domicile", f("Bold", 76), WHITE)
centered(d, 570, "Ce professeur qui change une vie,\nce peut être vous.", f("Italic", 36), SOFT)
for k, t in enumerate(["Enseignants, étudiants, diplômés", "Toutes les matières", "Du primaire à la Terminale", "Élèves près de chez vous"]):
    check_row(d, 150, 710 + k * 85, t, size=38)
d.rounded_rectangle((120, 1040, 960, 1160), 30, fill=WHITE)
d.text((540, 1078), "Écrivez-nous sur WhatsApp :", font=f("Medium", 32), fill=NAVY, anchor="mm")
d.text((540, 1125), "matières • niveau d'études • commune", font=f("Bold", 32), fill=GREEN, anchor="mm")
im.save(f"{OUT}/WIN4_recrutement.png")

# 5 Trois signes
im, d = base(False)
centered(d, 260, "3 signes que votre enfant\na besoin d'un répétiteur", f("Bold", 56), NAVY)
signs = [("Ses notes glissent", "trimestre après trimestre"), ("Il fuit ses cahiers", "« je n'ai rien à faire »"), ("Il perd confiance", "« je suis nul »")]
for k, (a, b2) in enumerate(signs):
    y = 430 + k * 200
    d.rounded_rectangle((80, y, 1000, y + 170), 30, fill=GREEN_L)
    d.text((150, y + 85), str(k + 1), font=f("Bold", 90), fill=GREEN, anchor="mm")
    d.text((230, y + 60), a, font=f("Bold", 44), fill=NAVY, anchor="lm")
    d.text((230, y + 115), b2, font=f("Medium", 34), fill=(90, 100, 125), anchor="lm")
centered(d, 1080, "Ne laissez pas le doute s'installer.", f("Bold", 42), NAVY)
im.save(f"{OUT}/WIN5_trois_signes.png")

# 6 Examens
im, d = base()
centered(d, 300, "Le grand jour se prépare\ndès aujourd'hui", f("Bold", 62), WHITE)
for k, t in enumerate(["CEPE", "BEPC", "BAC"]):
    x = 140 + k * 280
    d.ellipse((x, 470, x + 240, 710), fill=GREEN if k != 1 else GOLD)
    d.text((x + 120, 590), t, font=f("Bold", 58), fill=WHITE if k != 1 else NAVY, anchor="mm")
for k, t in enumerate(["Consolider les bases", "S'entraîner sur de vrais sujets", "Gagner méthode et confiance"]):
    check_row(d, 150, 800 + k * 85, t, size=38)
centered(d, 1090, "Votre enfant passe un examen ? Parlons-en.", f("Bold", 36), GOLD)
im.save(f"{OUT}/WIN6_examens.png")

# 7 Garantie
im, d = base()
d.ellipse((340, 220, 740, 620), fill=GREEN)
d.ellipse((370, 250, 710, 590), outline=WHITE, width=8)
d.text((540, 385), "GARANTIE", font=f("Bold", 58), fill=WHITE, anchor="mm")
d.text((540, 475), "REMPLACEMENT", font=f("Bold", 31), fill=WHITE, anchor="mm")
centered(d, 720, "Le répétiteur ne convient pas ?", f("Bold", 52), WHITE)
centered(d, 820, "Nous le remplaçons.", f("Bold", 64), GOLD)
centered(d, 960, "Votre confiance est précieuse.\nLa réussite de votre enfant l'est encore plus.", f("Italic", 36), SOFT)
im.save(f"{OUT}/WIN7_garantie.png")
print(sorted(os.listdir(OUT)))
