import json,re
exec(open('posts.py').read().split('P={')[0])
P={
"2026-11-18":("dire-l-heure","""⏰ **« What time is it? »… tu sais répondre sans hésiter ?**

Quarter past, half past, quarter to… beaucoup s'emmêlent les pinceaux 😅

Dans mon PDF gratuit :
✅ la méthode facile pour dire l'heure
✅ past et to expliqués simplement
✅ **La prononciation écrite en français**
✅ un exercice corrigé

💬 Commente « **INTÉRESSÉ** » et je te l'envoie en privé 📩

**Coach Winner**
#anglais #vocabulaire #winnersenglish"""),
"2026-11-19":("dialogue-magasin","""🛍️ **Faire du shopping en anglais, ça te fait peur ?**

Demander ta taille, essayer un vêtement, payer par carte… tout est dans ce dialogue 👕

✅ Un dialogue complet de la vie courante
✅ La traduction de chaque phrase
✅ **La prononciation écrite en français**
✅ Les mots clés à retenir

💬 Commente « **INTÉRESSÉ** » et je te l'envoie en privé 📩

**Coach Winner**
#anglais #dialogue #winnersenglish"""),
"2026-11-20":("12-mots-mal-prononces","""🔊 **Wednesday, island, receipt… tu les prononces comment ?**

Ces 12 mots sont mal prononcés par presque tout le monde 😱 Le secret : les lettres muettes !

✅ La mauvaise et la bonne prononciation
✅ **La prononciation écrite en français**
✅ Une explication simple pour chaque mot

💬 Commente « **INTÉRESSÉ** » et je te l'envoie en privé 📩

**Coach Winner**
#prononciation #anglais #winnersenglish"""),
"2026-11-21":("will-going-to","""🔮 **« I will » ou « I'm going to » ? Tu hésites toujours ?**

Les deux parlent du futur… mais pas de la même façon 🤔

Dans ma mini-leçon gratuite :
✅ la règle expliquée en 2 minutes
✅ des exemples simples
✅ un exercice avec les réponses

💬 Commente « **INTÉRESSÉ** » et je te l'envoie en privé 📩

**Coach Winner**
#grammaire #anglais #winnersenglish"""),
"2026-11-22":("30-adjectifs-personne","""🧑 **Décrire quelqu'un en anglais ? Il te faut ces 30 adjectifs.**

Gentil, drôle, timide, travailleur, têtu… 😄

✅ 30 adjectifs : caractère et physique
✅ **La prononciation écrite en français**
✅ Un exemple pour décrire ton meilleur ami
✅ Un petit exercice à faire

💬 Commente « **INTÉRESSÉ** » et je te l'envoie en privé 📩

**Coach Winner**
#vocabulaire #anglais #winnersenglish"""),
"2026-11-23":("entretien-embauche","""🤝 **Entretien d'embauche en anglais : sois prêt(e) !**

« Tell me about yourself »… et là, c'est le blanc 😰 Plus jamais.

✅ Les 9 questions qu'on te posera
✅ Une réponse modèle pour chacune
✅ **La prononciation écrite en français**
✅ 3 conseils pour le jour J

💬 Commente « **INTÉRESSÉ** » et je te l'envoie en privé 📩

**Coach Winner**
#emploi #anglais #winnersenglish"""),
"2026-11-24":("make-ou-do","""🛠️ **« I did a mistake » ❌ … on dit « I made a mistake » ✅**

Make ou do ? C'est le piège classique des francophones 😅

✅ La règle simple pour ne plus te tromper
✅ 20 expressions à connaître
✅ Un exercice avec les réponses

💬 Commente « **INTÉRESSÉ** » et je te l'envoie en privé 📩

**Coach Winner**
#grammaire #anglais #winnersenglish"""),
}
out={d:{"slug":s,"text":B(t)} for d,(s,t) in P.items()}
json.dump(out,open('posts_w3.json','w'),ensure_ascii=False,indent=1)
