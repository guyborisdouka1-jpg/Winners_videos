SUB = "Fais le test • Ton niveau à la fin !"
SPECS = {
 "16_vraifaux3": dict(kind="vf", music="suspense", title="VRAI OU FAUX ?", sub=SUB, levels=True, outro1="", outro2="", items=[
   dict(s="He don't like rice.", vrai=False, fix="He doesn't like rice.", note="He / She : doesn't"),
   dict(s="I'm looking for a job.", vrai=True, fix="", note="Chercher = look for"),
   dict(s="She is more tall than me.", vrai=False, fix="She is taller than me.", note="Adjectif court : -er + than"),
   dict(s="We went to the market yesterday.", vrai=True, fix="", note="Go → went au passé"),
   dict(s="I have 20 years.", vrai=False, fix="I am 20 years old.", note="L'âge se dit avec to be"),
 ]),
 "17_traduis3": dict(kind="traduis", music="energie", title="TRADUIS\nSI TU PEUX !", sub=SUB, levels=True, outro1="", outro2="", items=[
   dict(fr="J'ai faim.", en="I'm hungry.", note="Avoir faim = to be hungry"),
   dict(fr="Je n'ai pas le temps.", en="I don't have time.", note="Aussi : « I'm busy. »"),
   dict(fr="Ça dépend.", en="It depends.", note="Très utile à l'oral"),
   dict(fr="Tu as raison.", en="You're right.", note="Avoir raison = to be right"),
   dict(fr="On se voit demain.", en="See you tomorrow.", note="Pour dire au revoir"),
 ]),
 "18_faute3": dict(kind="convo", music="mystere", title="TROUVE\nLA FAUTE !", sub=SUB, levels=True, outro1="", outro2="", items=[
   dict(lines=[("Awa", "Are you hungry?"), ("Koffi", "Yes, I have hunger.")], bad=1, fix="Yes, I'm hungry.", err="I have hunger", ok="I'm hungry"),
   dict(lines=[("Koffi", "Where is your sister?"), ("Awa", "She is in the school.")], bad=1, fix="She is at school.", err="in the school", ok="at school"),
   dict(lines=[("Prof", "Did you finish?"), ("Ama", "Yes, I finished since one hour.")], bad=1, fix="Yes, I finished an hour ago.", err="since one hour", ok="an hour ago"),
   dict(lines=[("Awa", "Do you speak English?"), ("Koffi", "Yes, I speak a little bit English.")], bad=1, fix="Yes, I speak a little English.", err="a little bit English", ok="a little English"),
   dict(lines=[("Koffi", "Is it far?"), ("Awa", "No, it's near of the bank.")], bad=1, fix="No, it's near the bank.", err="near of", ok="near"),
 ]),
}
