SUB = "Fais le test • Ton niveau à la fin !"
B = dict(sub=SUB, levels=True, outro1="", outro2="")
SPECS = {
 "19_vf4": dict(kind="vf", music="suspense", title="VRAI OU FAUX ?", **B, items=[
   dict(s="I am agree with you.", vrai=False, fix="I agree with you.", note="Agree est déjà un verbe"),
   dict(s="She works in a bank.", vrai=True, fix="", note="He / She : verbe + s"),
   dict(s="I didn't went to school.", vrai=False, fix="I didn't go to school.", note="Après didn't : verbe de base"),
   dict(s="There are many people here.", vrai=True, fix="", note="Il y a (pluriel) = there are"),
   dict(s="Explain me this word.", vrai=False, fix="Explain this word to me.", note="Explain something TO someone"),
 ]),
 "20_tr4": dict(kind="traduis", music="energie", title="TRADUIS\nSI TU PEUX !", **B, items=[
   dict(fr="Je suis d'accord.", en="I agree.", note="Jamais « I am agree »"),
   dict(fr="Ça ne fait rien.", en="It doesn't matter.", note="Aussi : « No problem. »"),
   dict(fr="Je reviens tout de suite.", en="I'll be right back.", note="Très utilisé à l'oral"),
   dict(fr="Qu'est-ce qui se passe ?", en="What's going on?", note="Aussi : « What's happening? »"),
   dict(fr="Bon courage !", en="Good luck!", note="Pour encourager quelqu'un"),
 ]),
 "21_fa4": dict(kind="convo", music="mystere", title="TROUVE\nLA FAUTE !", **B, items=[
   dict(lines=[("Awa", "What time is it?"), ("Koffi", "It's three hours.")], bad=1, fix="It's three o'clock.", err="three hours", ok="three o'clock"),
   dict(lines=[("Koffi", "How is your mother?"), ("Awa", "She is fine, thanks. She is a nurse.")], bad=-1, fix="", err="", ok="") if False else
   dict(lines=[("Koffi", "Can you help me?"), ("Awa", "Yes, I can to help you.")], bad=1, fix="Yes, I can help you.", err="can to help", ok="can help"),
   dict(lines=[("Prof", "Where do you live?"), ("Ama", "I live at Cocody.")], bad=1, fix="I live in Cocody.", err="at Cocody", ok="in Cocody"),
   dict(lines=[("Awa", "Do you have a car?"), ("Koffi", "No, I don't have no car.")], bad=1, fix="No, I don't have a car.", err="don't have no", ok="don't have a"),
   dict(lines=[("Koffi", "Why are you late?"), ("Awa", "Because there was many traffic.")], bad=1, fix="Because there was a lot of traffic.", err="many traffic", ok="a lot of traffic"),
 ]),
 "22_qz5": dict(kind="quiz", music="classique", title="QUIZ TIME !", **B, items=[
   dict(q="« Il travaille tous les jours. »", opts=["He work every day", "He works every day", "He working every day"], ok=1, note="He / She : verbe + s"),
   dict(q="« Je suis né en 2000. »", opts=["I am born in 2000", "I was born in 2000", "I born in 2000"], ok=1, note="Être né = was born"),
   dict(q="« Tu peux m'appeler ? »", opts=["Can you call me?", "Can you to call me?", "You can call me?"], ok=0, note="Can + verbe sans to"),
   dict(q="« J'habite ici depuis 5 ans. »", opts=["I live here since 5 years", "I've lived here for 5 years", "I living here 5 years"], ok=1, note="Depuis + durée = for"),
   dict(q="« Il n'y a pas d'eau. »", opts=["There is no water", "It has no water", "There are not water"], ok=0, note="Il n'y a pas = there is no"),
 ]),
 "23_vf5": dict(kind="vf", music="suspense", title="VRAI OU FAUX ?", **B, items=[
   dict(s="I'm boring in class.", vrai=False, fix="I'm bored in class.", note="Bored = je m'ennuie"),
   dict(s="We have been friends for years.", vrai=True, fix="", note="For + durée"),
   dict(s="He can speaks French.", vrai=False, fix="He can speak French.", note="Après can : verbe sans s"),
   dict(s="I'm interested in music.", vrai=True, fix="", note="Interested + in"),
   dict(s="Let's discuss about it.", vrai=False, fix="Let's discuss it.", note="Discuss sans about"),
 ]),
 "24_tr5": dict(kind="traduis", music="energie", title="TRADUIS\nSI TU PEUX !", **B, items=[
   dict(fr="On sort ce soir ?", en="Shall we go out tonight?", note="Aussi : « Let's go out tonight! »"),
   dict(fr="J'ai très faim.", en="I'm starving.", note="Plus fort que « I'm hungry »"),
   dict(fr="C'est délicieux !", en="It's delicious!", note="Aussi : « It's so good! »"),
   dict(fr="L'addition, s'il vous plaît.", en="The bill, please.", note="Au restaurant"),
   dict(fr="Je me suis bien amusé.", en="I had a great time.", note="Pour dire merci après une sortie"),
 ]),
 "25_fa5": dict(kind="convo", music="mystere", title="TROUVE\nLA FAUTE !", **B, items=[
   dict(lines=[("Awa", "Are you married?"), ("Koffi", "No, I am celibate.")], bad=1, fix="No, I'm single.", err="celibate", ok="single"),
   dict(lines=[("Koffi", "Did you like the film?"), ("Awa", "Yes, it was very interested.")], bad=1, fix="Yes, it was very interesting.", err="interested", ok="interesting"),
   dict(lines=[("Prof", "Any questions?"), ("Ama", "Yes, what means this word?")], bad=1, fix="Yes, what does this word mean?", err="what means", ok="what does … mean"),
   dict(lines=[("Awa", "When is your birthday?"), ("Koffi", "It's in 12 May.")], bad=1, fix="It's on 12 May.", err="in 12 May", ok="on 12 May"),
   dict(lines=[("Koffi", "How long are you here?"), ("Awa", "I am here since Monday.")], bad=1, fix="I've been here since Monday.", err="I am here since", ok="I've been here since"),
 ]),
}
