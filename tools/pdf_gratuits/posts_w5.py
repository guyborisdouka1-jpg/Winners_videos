import json,re
exec(open('posts.py').read().split('P={')[0])
END="""

💬 Commente « **INTÉRESSÉ** » et je te l'envoie en privé 📩

**Coach Winner**
"""
P={
"2026-12-02":("some-any","""🧺 **« Some » ou « any » ? Tu hésites à chaque fois ?**

« Do you have some… » ou « any » ? La règle est plus simple que tu ne le crois 😉

✅ La règle expliquée en 2 minutes
✅ L'exception : « Would you like some… ? »
✅ Something, anyone, somewhere…
✅ Un exercice avec les réponses""","#grammaire #anglais #winnersenglish"),
"2026-12-03":("dialogue-hotel","""🏨 **À la réception d'un hôtel, tu saurais quoi dire en anglais ?**

Réservation, clé, Wi-Fi, petit-déjeuner… tout se passe en anglais dès ton arrivée 🧳

✅ Un dialogue complet à l'hôtel
✅ La traduction de chaque phrase
✅ **La prononciation écrite en français**
✅ Les mots à retenir pour ton séjour""","#anglais #voyage #winnersenglish"),
"2026-12-04":("small-talk","""☕ **Tu bloques quand il faut faire la conversation en anglais ?**

Au travail, à une fête, dans une file d'attente : les anglophones adorent le « small talk » 😄

✅ 14 phrases pour lancer et garder la conversation
✅ « Me too! », « Really? »… pour réagir
✅ **La prononciation écrite en français**
✅ Un mini-dialogue à une fête""","#anglais #conversation #winnersenglish"),
"2026-12-05":("30-mots-maison","""🏠 **Salon, chambre, canapé, faire la vaisselle… tu sais les dire en anglais ?**

Les mots de la maison, tu les utilises tous les jours. Il est temps de les apprendre 😉

✅ 30 mots : pièces, meubles, tâches ménagères
✅ **La prononciation écrite en français**
✅ Un modèle pour décrire ta maison
✅ Un petit exercice corrigé""","#vocabulaire #anglais #winnersenglish"),
"2026-12-06":("quiz-pieges","""🧠 **15 questions : tombes-tu dans les pièges des francophones ?**

« I am agree », « How many money? »… Teste-toi et découvre ton score 😏

✅ 15 questions A, B ou C
✅ Les réponses et ton résultat
✅ Les 3 règles à retenir
✅ Parfait pour te tester en 5 minutes""","#quiz #anglais #winnersenglish"),
"2026-12-07":("routine-20-verbes","""⏰ **Tu sais raconter ta journée en anglais, du réveil au coucher ?**

Wake up, get dressed, have lunch… ce sont les verbes que tu utiliseras le plus 💪

✅ 20 verbes de la routine avec un exemple
✅ **La prononciation écrite en français**
✅ First, then, finally… pour enchaîner
✅ Un petit exercice à faire""","#anglais #verbes #winnersenglish"),
"2026-12-08":("messages-courts-pro","""💬 **« Désolé, j'ai 10 minutes de retard »… tu l'écrirais comment en anglais ?**

Au travail, on envoie des petits messages toute la journée. Voici les modèles à copier 📲

✅ 9 messages : retard, annulation, relance…
✅ La traduction de chaque message
✅ **La prononciation des expressions clés**
✅ Prêts à copier-coller""","#anglais #travail #winnersenglish"),
}
out={d:{"slug":s,"text":B(t+END+h)} for d,(s,t,h) in P.items()}
json.dump(out,open('posts_w5.json','w'),ensure_ascii=False,indent=1)
