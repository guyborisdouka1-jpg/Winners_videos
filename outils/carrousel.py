"""Carrousels + images humour (1080x1350, format 4:5 : Facebook et TikTok)."""
import os
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 1080, 1350
FP = "/usr/share/fonts/truetype/google-fonts/Poppins-"
def f(wt, s): return ImageFont.truetype(FP + wt + ".ttf", s)
NAVY = (30, 34, 110); NAVY2 = (46, 49, 146); RED = (190, 45, 45); GOLD = (245, 190, 70); WHITE = (255, 255, 255)
GREEN = (40, 170, 90); SOFT = (205, 205, 235); BLACK = (22, 22, 30)
LOGO = Image.open(os.path.join(HERE, "logo_rond.png")).convert("RGBA")
OUT = os.path.join(HERE, "images"); os.makedirs(OUT, exist_ok=True)

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
def block(d, x, y, text, font, fill, maxw, anchor="la", lh=1.25):
    lines = wrap(d, text, font, maxw)
    for j, l in enumerate(lines): d.text((x, y + j * int(font.size * lh)), l, font=font, fill=fill, anchor=anchor)
    return len(lines) * int(font.size * lh)
def centered(d, y, text, font, fill, maxw=940, lh=1.25):
    lines = wrap(d, text, font, maxw); h = int(font.size * lh)
    y0 = y - (len(lines) - 1) * h // 2
    for j, l in enumerate(lines): d.text((W // 2, y0 + j * h), l, font=font, fill=fill, anchor="mm")

def frame(k=None, n=None):
    im = Image.new("RGB", (W, H), NAVY); d = ImageDraw.Draw(im)
    d.ellipse((650, -330, 1450, 420), fill=NAVY2); d.ellipse((-380, 1050, 380, 1750), fill=NAVY2)
    lg = LOGO.resize((150, 150), Image.LANCZOS); im.paste(lg, (50, 45), lg)
    d.text((220, 95), "WINNERS'", font=f("Bold", 38), fill=GOLD, anchor="lm")
    d.text((220, 145), "ENGLISH CENTER", font=f("Bold", 38), fill=WHITE, anchor="lm")
    if k is not None:
        d.rounded_rectangle((880, 85, 1030, 155), 35, fill=RED)
        d.text((955, 120), f"{k}/{n}", font=f("Bold", 34), fill=WHITE, anchor="mm")
    d.rectangle((0, H - 110, W, H), fill=RED)
    d.text((W // 2, H - 55), "0767037284  •  Cocody Riviera Palmeraie", font=f("Bold", 36), fill=WHITE, anchor="mm")
    return im, d

def cover(title, sub, k, n):
    im, d = frame(k, n)
    centered(d, 560, title, f("Bold", 84), GOLD, 900, 1.15)
    centered(d, 820, sub, f("Medium", 42), SOFT, 860)
    d.rounded_rectangle((330, 1000, 750, 1090), 45, fill=WHITE)
    d.text((540, 1045), "Glisse pour voir  >>", font=f("Bold", 36), fill=NAVY, anchor="mm")
    return im

def cards(title, rows, k, n, note=None):
    """rows : liste de (gros texte, petit texte)"""
    im, d = frame(k, n)
    centered(d, 260, title, f("Bold", 54), GOLD, 940)
    y = 340; avail = (1040 if not note else 930) - y
    hh = min(185, (avail - 25 * (len(rows) - 1)) // len(rows))
    for big, small in rows:
        d.rounded_rectangle((60, y, 1020, y + hh), 30, fill=WHITE)
        bf = f("Bold", 46 if len(big) < 30 else 38)
        if small:
            d.text((100, y + hh * 0.38), big, font=bf, fill=NAVY, anchor="lm")
            d.text((100, y + hh * 0.72), small, font=f("Medium", 32), fill=RED, anchor="lm")
        else:
            d.text((100, y + hh / 2), big, font=bf, fill=NAVY, anchor="lm")
        y += hh + 25
    if note: centered(d, 1000, note, f("Bold", 36), WHITE, 940)
    return im

def cta(line1, line2):
    im, d = frame()
    centered(d, 470, line1, f("Bold", 70), GOLD, 920, 1.15)
    centered(d, 680, line2, f("Bold", 48), WHITE, 900)
    d.rounded_rectangle((140, 830, 940, 1060), 40, fill=WHITE)
    d.text((540, 895), "Cours d'anglais • Inscriptions", font=f("Bold", 42), fill=NAVY, anchor="mm")
    d.text((540, 990), "0767037284", font=f("Bold", 78), fill=RED, anchor="mm")
    centered(d, 1150, "I speak English, and you ?", f("Italic", 40), SOFT)
    return im

def humour(text, bg, name):
    text = text.replace(" »", "\u00a0»").replace("« ", "«\u00a0").replace(" :", "\u00a0:")
    im = Image.new("RGB", (W, H), bg); d = ImageDraw.Draw(im)
    font = f("Bold", 66 if len(text) < 120 else 56)
    lines = wrap(d, text, font, 900); lh = int(font.size * 1.3)
    y0 = 620 - (len(lines) * lh) // 2
    for j, l in enumerate(lines): d.text((W // 2, y0 + j * lh), l, font=font, fill=WHITE, anchor="mm")
    lg = LOGO.resize((120, 120), Image.LANCZOS); im.paste(lg, (W // 2 - 300, 1160), lg)
    d.text((W // 2 - 160, 1200), "Winners' English Center", font=f("Bold", 38), fill=WHITE, anchor="lm")
    d.text((W // 2 - 160, 1250), "0767037284", font=f("Medium", 34), fill=GOLD if bg != RED else WHITE, anchor="lm")
    im.save(os.path.join(OUT, name + ".png"))

CAROUSELS = {
 "C1_presenter": [
   lambda: cover("Te présenter en anglais", "10 phrases simples pour ne plus bloquer", 1, 6),
   lambda: cards("Ton nom et ton âge", [("My name is Koffi.", "Je m'appelle Koffi."), ("I'm 24 years old.", "J'ai 24 ans."), ("Nice to meet you!", "Enchanté(e) !")], 2, 6),
   lambda: cards("D'où tu viens, où tu vis", [("I'm from Bouaké.", "Je viens de Bouaké."), ("I live in Cocody.", "J'habite à Cocody.")], 3, 6),
   lambda: cards("Ce que tu fais", [("I'm a student.", "Je suis étudiant(e)."), ("I work in a bank.", "Je travaille dans une banque."), ("I'm learning English.", "J'apprends l'anglais.")], 4, 6),
   lambda: cards("Ce que tu aimes", [("I like football.", "J'aime le football."), ("I love music.", "J'adore la musique.")], 5, 6,
                 note="À toi ! Présente-toi en anglais en commentaire"),
   lambda: cta("À toi de jouer !", "Présente-toi en 2 phrases\nen commentaire, on corrige !"),
 ],
 "C2_make_do": [
   lambda: cover("MAKE ou DO ?", "Ne te trompe plus jamais", 1, 6),
   lambda: cards("On dit MAKE", [("make a mistake", "faire une erreur"), ("make a decision", "prendre une décision"), ("make money", "gagner de l'argent"), ("make friends", "se faire des amis")], 2, 6),
   lambda: cards("On dit DO", [("do your homework", "faire tes devoirs"), ("do the dishes", "faire la vaisselle"), ("do sport", "faire du sport"), ("do your best", "faire de ton mieux")], 3, 6),
   lambda: cards("À toi : MAKE ou DO ?", [("1. ___ a cake", None), ("2. ___ the shopping", None), ("3. ___ a noise", None), ("4. ___ a favour", None)], 4, 6,
                 note="Écris tes réponses en commentaire avant de glisser !"),
   lambda: cards("Réponses", [("1. MAKE a cake", "faire un gâteau"), ("2. DO the shopping", "faire les courses"), ("3. MAKE a noise", "faire du bruit"), ("4. DO a favour", "rendre service")], 5, 6),
   lambda: cta("Combien sur 4 ?", "Écris ton score\nen commentaire !"),
 ],
 "C3_faux_amis": [
   lambda: cover("Les faux amis", "Ces mots anglais qui te piègent", 1, 6),
   lambda: cards("Attention !", [("Actually", "= en fait (pas « actuellement »)"), ("Library", "= bibliothèque (pas « librairie »)")], 2, 6),
   lambda: cards("Attention !", [("Eventually", "= finalement (pas « éventuellement »)"), ("Sensible", "= raisonnable (pas « sensible »)")], 3, 6),
   lambda: cards("Attention !", [("Attend", "= assister à (pas « attendre »)"), ("Chance", "= possibilité (la chance = luck)")], 4, 6),
   lambda: cards("Et pour dire…", [("Actuellement", "Currently"), ("Attendre", "To wait"), ("Sensible", "Sensitive")], 5, 6),
   lambda: cta("Tu en connaissais combien ?", "Dis-le en commentaire\net tag un ami !"),
 ],
}
HUMOUR = [
 ("H1_how_are_you", "Quand on te dit « How are you ? »\net tu réponds « I'm fine, thank you, and you ? » en 0,2 seconde.\n\nRéflexe de CM2.", RED),
 ("H2_resolution", "Moi en janvier :\n« Cette année je parle anglais. »\n\nMoi en décembre :\n« Yes… No… OK. »", BLACK),
 ("H3_any_questions", "Prof : « Any questions ? »\n\nToute la classe : …\n\nProf : « Very good ! »", NAVY2),
 ("H4_films", "Je comprends tout dans les films en anglais.\n\nAvec les sous-titres en français.", RED),
]

if __name__ == "__main__":
    for name, slides in CAROUSELS.items():
        for k, s in enumerate(slides, 1): s().save(os.path.join(OUT, f"{name}_{k}.png"))
    for name, text, bg in HUMOUR: humour(text, bg, name)
    print(sorted(os.listdir(OUT)))

CAROUSELS2 = {
 "C4_restaurant": [
   lambda: cover("Au restaurant en anglais", "Les phrases pour commander et payer", 1, 6),
   lambda: cards("Pour commander", [("Can I see the menu, please?", "Je peux voir le menu ?"), ("I'd like the chicken, please.", "Je voudrais le poulet."), ("Can I have some water?", "Je peux avoir de l'eau ?")], 2, 6),
   lambda: cards("Pour payer", [("Can I have the bill, please?", "L'addition, s'il vous plaît."), ("Can I pay by card?", "Je peux payer par carte ?"), ("Keep the change!", "Gardez la monnaie !")], 3, 6),
   lambda: cards("À toi : comment dire…", [("« Je voudrais du riz. »", None), ("A. I want rice.", None), ("B. I'd like some rice.", None), ("C. I like rice.", None)], 4, 6,
                 note="Réponds A, B ou C en commentaire !"),
   lambda: cards("Réponse : B", [("I'd like some rice.", "I'd like = je voudrais (poli)"), ("I like rice.", "= j'aime le riz (autre sens !)")], 5, 6),
   lambda: cta("Tu avais trouvé ?", "Dis-le en commentaire\net tag ton ami gourmand !"),
 ],
 "C5_in_on_at": [
   lambda: cover("IN, ON ou AT ?", "Les prépositions de temps et de lieu", 1, 6),
   lambda: cards("Pour le temps", [("AT 8 o'clock", "à 8 heures (une heure précise)"), ("ON Monday", "lundi (un jour)"), ("IN October / IN 2026", "en octobre / en 2026")], 2, 6),
   lambda: cards("Pour les lieux", [("AT home / AT school", "à la maison / à l'école"), ("IN Cocody", "à Cocody (une ville, un quartier)"), ("ON the bus", "dans le bus")], 3, 6),
   lambda: cards("À toi : IN, ON ou AT ?", [("1. ___ Friday", None), ("2. ___ night", None), ("3. ___ the morning", None), ("4. ___ the weekend", None)], 4, 6,
                 note="Écris tes réponses en commentaire avant de glisser !"),
   lambda: cards("Réponses", [("1. ON Friday", None), ("2. AT night", None), ("3. IN the morning", None), ("4. AT the weekend", "(en anglais américain : ON the weekend)")], 5, 6),
   lambda: cta("Combien sur 4 ?", "Écris ton score\nen commentaire !"),
 ],
 "C6_travail": [
   lambda: cover("L'anglais au travail", "6 phrases pour faire pro", 1, 6),
   lambda: cards("Par e-mail ou message", [("Could you send me the file?", "Tu peux m'envoyer le fichier ?"), ("Sorry for the delay.", "Désolé pour le retard."), ("I'll get back to you.", "Je reviens vers toi.")], 2, 6),
   lambda: cards("En réunion", [("Let's schedule a meeting.", "Organisons une réunion."), ("Could you repeat, please?", "Tu peux répéter, s'il te plaît ?"), ("I'm on it!", "Je m'en occupe !")], 3, 6),
   lambda: cards("À éviter", [("« I am agree »", "On dit : I agree"), ("« Discuss about »", "On dit : discuss the project")], 4, 6),
   lambda: cards("Ta phrase préférée ?", [("1. I'll get back to you.", None), ("2. I'm on it!", None), ("3. Sorry for the delay.", None)], 5, 6,
                 note="Réponds 1, 2 ou 3 en commentaire !"),
   lambda: cta("Tu vas l'utiliser demain ?", "Partage à un collègue\nqui en a besoin !"),
 ],
 "C7_test_niveau": [
   lambda: cover("Mini-test : quel est ton niveau ?", "3 questions • Note tes réponses", 1, 6),
   lambda: cards("1. She ___ to school every day.", [("A. go", None), ("B. goes", None), ("C. going", None)], 2, 6),
   lambda: cards("2. I've lived here ___ 2020.", [("A. for", None), ("B. from", None), ("C. since", None)], 3, 6),
   lambda: cards("3. If I ___ rich, I would travel.", [("A. were", None), ("B. am", None), ("C. will be", None)], 4, 6),
   lambda: cards("Réponses : 1B • 2C • 3A", [("0 ou 1 bonne réponse", "Débutant : on commence ensemble !"), ("2 bonnes réponses", "Intermédiaire : continue !"), ("3 bonnes réponses", "Avancé : bravo !")], 5, 6),
   lambda: cta("Quel est ton niveau ?", "Écris-le en commentaire,\non te conseille !"),
 ],
}
HUMOUR2 = [
 ("H5_repeat", "Le prof : « Repeat after me. »\n\nMoi : « Repeat after me. »", BLACK),
 ("H6_cv", "Quand tu sais dire « Yes », « No » et « Thank you »…\n\net tu écris « Anglais : courant » sur ton CV.", NAVY2),
 ("H7_chanson", "Moi qui chante cette chanson en anglais depuis 5 ans :\n\nToujours aucune idée de ce qu'elle raconte.", RED),
]
if __name__ == "__main__":
    for name, slides in CAROUSELS2.items():
        for k, s in enumerate(slides, 1): s().save(os.path.join(OUT, f"{name}_{k}.png"))
    for name, text, bg in HUMOUR2: humour(text, bg, name)
