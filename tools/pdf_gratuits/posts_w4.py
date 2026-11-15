import json,re
exec(open('posts.py').read().split('P={')[0])
END="""

💬 Commente « **INTÉRESSÉ** » et je te l'envoie en privé 📩

**Coach Winner**
"""
P={
"2026-11-25":("dialogue-medecin","""🩺 **Chez le médecin, tu saurais expliquer où tu as mal… en anglais ?**

Mal de tête, fièvre, toux… quand on est malade, ce n'est pas le moment de chercher ses mots 🤒

✅ Un dialogue complet chez le médecin
✅ La traduction de chaque phrase
✅ **La prononciation écrite en français**
✅ Les 10 mots de la santé à connaître""","#anglais #dialogue #winnersenglish"),
"2026-11-26":("30-mots-cuisine","""🍳 **Couteau, poêle, marmite… tu les connais en anglais ?**

La cuisine, c'est le meilleur endroit pour apprendre du vocabulaire tous les jours 😋

✅ 30 mots : ustensiles, aliments, verbes
✅ **La prononciation écrite en français**
✅ Une mini-recette en anglais
✅ Un petit exercice corrigé""","#vocabulaire #anglais #winnersenglish"),
"2026-11-27":("much-many","""🔢 **« How much » ou « How many » ? Tu hésites encore ?**

« How many money? » ❌ C'est l'erreur que j'entends tout le temps 😅

✅ La règle expliquée en 2 minutes
✅ A lot of, a few, a little
✅ Les mots pièges : money, advice…
✅ Un exercice avec les réponses""","#grammaire #anglais #winnersenglish"),
"2026-11-28":("demander-son-chemin","""🗺️ **Perdu(e) dans une ville anglophone ? Plus jamais !**

« How can I get to the station? »… et surtout, comprendre la réponse 😉

✅ 15 phrases pour demander et comprendre
✅ Gauche, droite, tout droit, en face de…
✅ **La prononciation écrite en français**
✅ Un mini-dialogue à Londres""","#anglais #voyage #winnersenglish"),
"2026-11-29":("mots-interrogatifs","""❓ **What, Where, When, Who, Why… tu les mélanges ?**

Toutes les questions en anglais commencent par l'un de ces mots. Les connaître, c'est pouvoir tout demander 💪

✅ Les 9 mots interrogatifs expliqués
✅ How old, how long, how often…
✅ L'erreur « Where you live? » ❌
✅ Un exercice avec les réponses""","#grammaire #anglais #winnersenglish"),
"2026-11-30":("dire-la-date","""📅 **Demain, c'est « the first of December »… tu sais le dire ?**

1st, 2nd, 3rd, 4th… les dates en anglais piègent beaucoup de monde 😅

✅ Les jours et les mois
✅ Les nombres ordinaux simplement
✅ **La prononciation écrite en français**
✅ Un petit exercice corrigé""","#anglais #vocabulaire #winnersenglish"),
"2026-12-01":("etre-poli-anglais","""🎩 **« Give me water »… correct, mais très impoli en anglais !**

En anglais, une phrase trop directe peut vexer sans que tu le saches 😬

✅ 12 phrases trop directes et leur version polie
✅ Could you, I'd like, would you mind…
✅ Sorry ou Excuse me ?
✅ **La prononciation écrite en français**""","#anglais #politesse #winnersenglish"),
}
out={d:{"slug":s,"text":B(t+END+h)} for d,(s,t,h) in P.items()}
json.dump(out,open('posts_w4.json','w'),ensure_ascii=False,indent=1)
