import json
def B(s):
    o=""
    for c in s:
        if 'A'<=c<='Z': o+=chr(0x1D5D4+ord(c)-65)
        elif 'a'<=c<='z': o+=chr(0x1D5EE+ord(c)-97)
        elif '0'<=c<='9': o+=chr(0x1D7EC+ord(c)-48)
        else: o+=c
    return o
WA="👉 wa.me/2250767037284"
END=f"\n\n🚀 {B('ENGLISH SPRINT')} : le dernier programme de l'année. {B('2 mois')} pour enfin parler, en classe ou en ligne. {B('95.000 F')}. Les inscriptions sont encore ouvertes.\n{WA}\n\n— {B('Coach Winner')}\n#anglais #apprendrelanglais #englishsprint #winnersenglish"
V={
 "08_quiz3": ("Quiz du jour", "5 phrases du quotidien. Compte tes points…"),
 "13_traduis2": ("Traduis si tu peux", "5 phrases qu'on dit tous les jours. Tu les dis comment en anglais ?"),
 "10_vraifaux2": ("Vrai ou faux", "5 phrases. Laquelle est correcte ?"),
 "14_faute2": ("Trouve la faute", "5 conversations, 1 faute dans chacune. Tu la vois ?"),
 "11_devine2": ("Devine le sens", "5 expressions que les anglophones utilisent tout le temps."),
 "12_ordre2": ("Remets dans l'ordre", "5 phrases mélangées. À toi de jouer !"),
 "15_quiz4": ("Quiz du dimanche", "5 questions pour finir la semaine en beauté."),
}
out={}
for k,(t,s) in V.items():
    out[k]=f"🎯 {B(t.upper())} : {B('fais le test, ton niveau à la fin')} 👀\n\n{s}\nRegarde jusqu'au bout pour savoir si tu es {B('Débutant')}, {B('Intermédiaire')} ou {B('Avancé')}.\n\nDis-nous ton niveau en commentaire 👇"+END
Q={"13":"She ___ English very well.","14":"« Je suis d'accord »","15":"« J'ai 25 ans »","16":"« Je cherche du travail »","17":"« Il fait chaud »","18":"« Je suis en retard »","19":"« Je n'ai pas compris »"}
for d,q in Q.items():
    lab = "Complète" if d=="13" else "Comment dire"
    out["q"+d]=f"⚡ {B('TEST RAPIDE')} : {lab} {q} ?\n\n{B('A, B ou C')} ? Réponds en commentaire, puis glisse pour voir la bonne réponse 👉"+END
json.dump(out,open("/home/claude/Winners_videos/semaine_13-19/captions.json","w"),ensure_ascii=False,indent=1)
print(out["08_quiz3"]); print(); print(out["q15"])
