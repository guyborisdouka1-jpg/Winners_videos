SUB = "Fais le test • Ton niveau à la fin !"
B = dict(sub=SUB, levels=True, outro1="", outro2="")
SPECS = {
 "26_vf6": dict(kind="vf", music="suspense", title="VRAI OU FAUX ?", **B, items=[
   dict(s="I have lived here for 3 years.", vrai=True, fix="", note="For + durée"),
   dict(s="She don't understand.", vrai=False, fix="She doesn't understand.", note="He / She : doesn't"),
   dict(s="I'm good in English.", vrai=False, fix="I'm good at English.", note="Good + AT"),
   dict(s="Can you help me, please?", vrai=True, fix="", note="Can + verbe sans to"),
   dict(s="I go to school yesterday.", vrai=False, fix="I went to school yesterday.", note="Hier = passé : went"),
 ]),
 "27_tr6": dict(kind="traduis", music="energie", title="TRADUIS\nSI TU PEUX !", **B, items=[
   dict(fr="Je suis pressé.", en="I'm in a hurry.", note="Pressé = in a hurry"),
   dict(fr="Ça me plaît.", en="I like it.", note="Simple et naturel"),
   dict(fr="Je m'en occupe.", en="I'll take care of it.", note="Très utile au travail"),
   dict(fr="Ce n'est pas grave.", en="It's okay.", note="Aussi : « No worries. »"),
   dict(fr="À tout à l'heure !", en="See you later!", note="Pour dire au revoir"),
 ]),
 "28_fa6": dict(kind="convo", music="mystere", title="TROUVE\nLA FAUTE !", **B, items=[
   dict(lines=[("Awa", "How are you?"), ("Koffi", "I'm fine, and you?"), ("Awa", "I'm fine too, I am arrived.")], bad=2, fix="I'm fine too, I've arrived.", err="I am arrived", ok="I've arrived"),
   dict(lines=[("Koffi", "Do you want some water?"), ("Awa", "No thanks, I am not thirst.")], bad=1, fix="No thanks, I'm not thirsty.", err="not thirst", ok="not thirsty"),
   dict(lines=[("Prof", "Who is absent?"), ("Ama", "Koffi is absent since Monday.")], bad=1, fix="Koffi has been absent since Monday.", err="is absent since", ok="has been absent since"),
   dict(lines=[("Awa", "Where are you going?"), ("Koffi", "I go to the market now.")], bad=1, fix="I'm going to the market now.", err="I go … now", ok="I'm going … now"),
   dict(lines=[("Koffi", "Is this your phone?"), ("Awa", "Yes, it's mine phone.")], bad=1, fix="Yes, it's my phone.", err="mine phone", ok="my phone"),
 ]),
 "29_qz6": dict(kind="quiz", music="classique", title="QUIZ TIME !", **B, items=[
   dict(q="« J'ai besoin d'aide. »", opts=["I need help", "I have need help", "I am need help"], ok=0, note="Avoir besoin = to need"),
   dict(q="« Il fait beau. »", opts=["He is nice", "It's nice weather", "It makes nice"], ok=1, note="La météo = It's…"),
   dict(q="« Je ne sais pas. »", opts=["I no know", "I don't know", "I not know"], ok=1, note="Négation : don't + verbe"),
   dict(q="« Combien ça coûte ? »", opts=["How much is it?", "How many cost?", "How much it cost?"], ok=0, note="Prix = How much"),
   dict(q="« Je me lève à 6 h. »", opts=["I wake up at 6", "I wake up in 6", "I wake me at 6"], ok=0, note="Heure : AT"),
 ]),
 "30_vf7": dict(kind="vf", music="suspense", title="VRAI OU FAUX ?", **B, items=[
   dict(s="I'm agree.", vrai=False, fix="I agree.", note="Agree est déjà un verbe"),
   dict(s="He is taller than his brother.", vrai=True, fix="", note="Adjectif court : -er + than"),
   dict(s="I have 2 brothers.", vrai=True, fix="", note="Posséder = to have ✔"),
   dict(s="Where you live?", vrai=False, fix="Where do you live?", note="Question : do + sujet + verbe"),
   dict(s="I am going to call you tomorrow.", vrai=True, fix="", note="Futur proche : going to"),
 ]),
 "31_tr7": dict(kind="traduis", music="energie", title="TRADUIS\nSI TU PEUX !", **B, items=[
   dict(fr="Il fait trop chaud !", en="It's so hot!", note="La météo = It's…"),
   dict(fr="On commande ?", en="Shall we order?", note="Au restaurant"),
   dict(fr="Ça te va bien !", en="It suits you!", note="Pour un vêtement"),
   dict(fr="Je suis fatigué mais content.", en="I'm tired but happy.", note="But = mais"),
   dict(fr="Bonne nuit !", en="Good night!", note="Le soir, avant de dormir"),
 ]),
 "32_fa7": dict(kind="convo", music="mystere", title="TROUVE\nLA FAUTE !", **B, items=[
   dict(lines=[("Awa", "Do you like your job?"), ("Koffi", "Yes, I like it so much.")], bad=-9, fix="", err="", ok="") if False else
   dict(lines=[("Awa", "Do you like your job?"), ("Koffi", "Yes, I am liking it.")], bad=1, fix="Yes, I like it.", err="I am liking", ok="I like"),
   dict(lines=[("Koffi", "Did you eat?"), ("Awa", "Yes, I already eated.")], bad=1, fix="Yes, I've already eaten.", err="eated", ok="eaten"),
   dict(lines=[("Prof", "Open your books."), ("Ama", "Sorry, I forgot my book at home house.")], bad=1, fix="Sorry, I left my book at home.", err="at home house", ok="at home"),
   dict(lines=[("Awa", "How old is your son?"), ("Koffi", "He has 8 years.")], bad=1, fix="He is 8 years old.", err="He has 8 years", ok="He is 8 years old"),
   dict(lines=[("Koffi", "What's the problem?"), ("Awa", "My phone doesn't works.")], bad=1, fix="My phone doesn't work.", err="doesn't works", ok="doesn't work"),
 ]),
}
