import json,re
def bold(s):
    o=''
    for c in s:
        if 'A'<=c<='Z':o+=chr(0x1D5D4+ord(c)-65)
        elif 'a'<=c<='z':o+=chr(0x1D5EE+ord(c)-97)
        elif '0'<=c<='9':o+=chr(0x1D7EC+ord(c)-48)
        else:o+=c
    return o
B=lambda t:re.sub(r'\*\*(.+?)\*\*',lambda m:bold(m.group(1)),t)
P={
"2026-11-05":("10-erreurs-francophones","""❌ **« I have 25 years »… toi aussi tu dis ça ?**

C'est l'une des **10 erreurs** que font presque tous les francophones en anglais 😅

Dans mon PDF gratuit :
✅ les 10 erreurs les plus courantes
✅ la bonne phrase à dire à la place
✅ une explication simple pour ne plus te tromper

💬 Commente **« INTÉRESSÉ »** et je te l'envoie en privé 📩

**Coach Winner**
#anglais #erreurs #winnersenglish"""),
"2026-11-06":("40-mots-bureau","""💼 **Tu travailles dans un bureau ? Ces 40 mots sont pour toi.**

Meeting, invoice, deadline, customer… les mots qu'on entend chaque jour au travail 🏢

✅ 40 mots avec leur traduction
✅ **La prononciation écrite en français**
✅ Un petit exercice pour les retenir

💬 Écris **« INTÉRESSÉ »** en commentaire, il arrive dans ta messagerie 📩

**Coach Winner**
#anglaispro #vocabulaire #winnersenglish"""),
"2026-11-07":("present-simple-continuous","""🤔 **« I eat » ou « I'm eating » ? Tu hésites ?**

Dans ma mini-leçon gratuite, je t'explique la différence **en 2 minutes**, avec des exemples simples et un exercice corrigé 📘

Fini la confusion, pour de bon !

💬 Commente **« INTÉRESSÉ »** pour la recevoir en privé 🎁

**Coach Winner**
#grammaire #anglais #winnersenglish"""),
"2026-11-08":("dialogue-restaurant","""🍽️ **Commander au restaurant en anglais, tu sais faire ?**

Je t'offre un **dialogue complet** : la table, le plat, la boisson, l'addition… avec **la prononciation écrite en français** 🔊

Lis-le à deux, et tu seras prêt(e) pour ton prochain voyage ✈️

💬 Tape **« INTÉRESSÉ »** en commentaire et je te l'envoie en privé 📩

**Coach Winner**
#dialogue #anglais #winnersenglish"""),
"2026-11-09":("30-verbes-irreguliers","""🔁 **go – went – gone… tu les connais tous ?**

Voici les **30 verbes irréguliers** les plus utilisés en anglais, dans un tableau clair avec la traduction 📋

👉 Ceux que tu entendras le plus souvent
👉 Avec un petit exercice pour t'entraîner

💬 Commente **« INTÉRESSÉ »** et reçois ton PDF gratuit en privé !

**Coach Winner**
#verbesirreguliers #anglais #winnersenglish"""),
"2026-11-10":("15-expressions-natifs","""🍰 **« It's a piece of cake »… ça ne parle pas de gâteau !**

Découvre **15 expressions anglaises** que les natifs utilisent tout le temps, avec leur vrai sens et un exemple 💬

✅ Break the ice, once in a blue moon…
✅ **La prononciation écrite en français**

💬 Écris **« INTÉRESSÉ »** juste en dessous, je te l'envoie en privé 📩

**Coach Winner**
#expressions #anglais #winnersenglish"""),
}
json.dump({d:{"slug":s,"text":B(t)} for d,(s,t) in P.items()},open('posts.json','w'),ensure_ascii=False,indent=1)
