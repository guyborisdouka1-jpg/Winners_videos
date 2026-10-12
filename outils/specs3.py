import copy
from specs2 import SPECS as S2
SUB = "Fais le test • Ton niveau à la fin !"
SPECS = {}
for k in ["08_quiz3", "10_vraifaux2", "11_devine2", "12_ordre2"]:
    s = copy.deepcopy(S2[k]); s["levels"] = True; s["sub"] = SUB; SPECS[k] = s
SPECS["13_traduis2"] = dict(kind="traduis", music="energie", title="TRADUIS\nSI TU PEUX !", sub=SUB, levels=True,
  outro1="", outro2="", items=[
  dict(fr="Je suis fatigué.", en="I'm tired.", note="Fatigué = tired"),
  dict(fr="Ça ne me dérange pas.", en="I don't mind.", note="Très poli et très utilisé"),
  dict(fr="Je n'ai pas compris.", en="I didn't understand.", note="Après didn't : verbe de base"),
  dict(fr="Tu peux répéter ?", en="Can you repeat, please?", note="Aussi : « Sorry? »"),
  dict(fr="Je suis en retard.", en="I'm late.", note="Jamais « I'm in retard »"),
])
SPECS["14_faute2"] = dict(kind="convo", music="mystere", title="TROUVE\nLA FAUTE !", sub=SUB, levels=True,
  outro1="", outro2="", items=[
  dict(lines=[("Awa", "How old are you?"), ("Koffi", "I have 25 years.")],
       bad=1, fix="I'm 25 years old.", err="I have 25 years", ok="I'm 25 years old"),
  dict(lines=[("Koffi", "Do you agree with me?"), ("Awa", "Yes, I am agree.")],
       bad=1, fix="Yes, I agree.", err="I am agree", ok="I agree"),
  dict(lines=[("Awa", "Where is Koffi?"), ("Ama", "He don't come today.")],
       bad=1, fix="He isn't coming today.", err="He don't come", ok="He isn't coming"),
  dict(lines=[("Prof", "Any questions?"), ("Koffi", "Yes. Can you explain me this word?")],
       bad=1, fix="Can you explain this word to me?", err="explain me", ok="explain … to me"),
  dict(lines=[("Awa", "Did you see the match?"), ("Koffi", "Yes, I watched it yesterday."), ("Awa", "It was very interested!")],
       bad=2, fix="It was very interesting!", err="very interested", ok="very interesting"),
])
SPECS["15_quiz4"] = dict(kind="quiz", music="classique", title="QUIZ TIME !", sub=SUB, levels=True,
  outro1="", outro2="", items=[
  dict(q="« Je travaille ici depuis 2 ans. »", opts=["I work here since 2 years", "I've worked here for 2 years", "I working here for 2 years"], ok=1, note="Depuis + durée = present perfect + for"),
  dict(q="« Il pleut. »", opts=["It's raining", "He rains", "It rain"], ok=0, note="La météo = It's…"),
  dict(q="« Je cherche mon téléphone. »", opts=["I search my phone", "I'm looking for my phone", "I find my phone"], ok=1, note="Chercher = look for"),
  dict(q="« Elle est plus grande que moi. »", opts=["She is more tall than me", "She is taller than me", "She is tallest than me"], ok=1, note="Adjectif court : -er + than"),
  dict(q="« Je n'aime pas ça. »", opts=["I don't like it", "I not like it", "I no like it"], ok=0, note="Négation : don't + verbe"),
])
