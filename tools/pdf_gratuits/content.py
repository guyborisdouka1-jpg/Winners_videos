# Each item: slug, date, title, subtitle, emoji, pages: list of html blocks (2 pages)
exec(open('data.py').read())
def table(rows, cols=3, start=1):
    h='<table>'
    for k,r in enumerate(rows):
        if cols==3: en,pr,fr=r; h+=f'<tr><td class="n">{start+k}</td><td><b>{en}</b><span class="pr">🔊 {pr}</span></td><td class="fr">{fr}</td></tr>'
    return h+'</table>'
pick={0:[0,1,2,3,7],2:[0,1,2,4,8],3:[0,1,4,6,9],6:[0,4,6,7,9],9:[1,4,6,9,2]}
S=[(T[i][0],[T[i][1][j] for j in js]) for i,js in pick.items()]
p1='';p2='';n=1
for k,(t,rows) in enumerate(S):
    blk=f'<h2>{t}</h2>'+table(rows,start=n); n+=len(rows)
    if k<3: p1+=blk
    else: p2+=blk
D=[]
D.append(dict(slug='25-phrases-quotidien',date='2026-11-04',title="25 phrases d'anglais",sub="pour parler au quotidien",emoji='🗣️',
 tip="Lis chaque phrase 3 fois à voix haute en suivant la prononciation en rouge, puis cache l'anglais et retrouve-le à partir du français.",
 p1=p1,p2=p2))
err=[("I have 25 years.","I am 25 (years old).","En anglais, on « est » son âge : verbe <i>to be</i>."),
("I am agree.","I agree.","<i>Agree</i> est déjà un verbe : pas de <i>am</i>."),
("He don't like coffee.","He doesn't like coffee.","Avec he / she / it : <i>doesn't</i>."),
("I am here since Monday.","I have been here since Monday.","Une action qui dure jusqu'à maintenant : <i>have been</i>."),
("Can you explain me?","Can you explain it to me?","On explique <i>quelque chose</i> <b>à</b> quelqu'un."),
("I'm going to the home.","I'm going home.","Pas de <i>to the</i> devant <i>home</i>."),
("She is more tall than me.","She is taller than me.","Adjectif court : on ajoute <i>-er</i>."),
("Informations / advices","Information / advice","Ces mots n'ont pas de pluriel en anglais."),
("I didn't went.","I didn't go.","Après <i>didn't</i>, le verbe reste à la base."),
("Actually, I live in Leeds. (= en ce moment)","Currently, I live in Leeds.","<i>Actually</i> = en réalité ; <i>currently</i> = actuellement."),]
def errt(rows,s):
    h='<table class="err">'
    for k,(w,r,e) in enumerate(rows): h+=f'<tr><td class="n">{s+k}</td><td><span class="bad">❌ {w}</span><span class="good">✅ {r}</span><span class="ex">{e}</span></td></tr>'
    return h+'</table>'
D.append(dict(slug='10-erreurs-francophones',date='2026-11-05',title="Les 10 erreurs",sub="que font tous les francophones en anglais",emoji='❌',
 tip="Ces erreurs viennent du français « traduit mot à mot ». Lis la bonne version à voix haute 3 fois pour remplacer la mauvaise habitude.",
 p1=errt(err[:5],1),p2=errt(err[5:],6)))
voc=[("🖥️","computer","keum-pyou-teur","ordinateur"),("📧","email","î-méïl","courriel"),("📅","meeting","mî-ting","réunion"),("📞","call","kôl","appel"),("📝","report","ri-port","rapport"),("👔","manager","mè-ni-djeur","responsable"),("🤝","colleague","ko-lîg","collègue"),("💼","job","djob","emploi"),("🏢","office","o-fiss","bureau"),("⏰","deadline","dèd-laïn","date limite"),
("📊","project","pro-djèkt","projet"),("💰","salary","sè-la-ri","salaire"),("🧾","invoice","in-voïss","facture"),("📦","delivery","di-li-veu-ri","livraison"),("🛒","customer","keuss-to-meur","client"),("📈","sales","séïlz","ventes"),("🖨️","printer","prin-teur","imprimante"),("📁","file","faïl","dossier / fichier"),("✍️","to sign","tou saïn","signer"),("🗓️","schedule","skè-djoul","emploi du temps"),
("☕","break","bréïk","pause"),("🏖️","holiday","ho-li-déï","congé"),("🤒","sick leave","sik lîv","arrêt maladie"),("📋","task","tâsk","tâche"),("🎯","goal","gol","objectif"),("🧑‍💼","interview","in-teur-vyou","entretien"),("📄","CV / résumé","si-vi","CV"),("🏆","promotion","pro-mo-cheun","promotion"),("👥","team","tîm","équipe"),("💡","idea","aï-dî-eu","idée"),
("🔑","password","pâss-weurd","mot de passe"),("🌐","website","wèb-saït","site web"),("📲","to text","tou tèkst","envoyer un SMS"),("⏳","overtime","o-veur-taïm","heures sup."),("🧮","budget","beu-djit","budget"),("🚚","supplier","seu-plaï-eur","fournisseur"),("🗣️","to negotiate","tou ni-go-chi-éït","négocier"),("✅","approved","eu-prouvd","approuvé"),("❗","urgent","eur-djeunt","urgent"),("👋","to resign","tou ri-zaïn","démissionner")]
def voct(rows):
    h='<div class="voc">'
    for e,en,pr,fr in rows: h+=f'<div><span class="e">{e}</span><b>{en}</b><span class="pr">🔊 {pr}</span><span class="fr">{fr}</span></div>'
    return h+'</div>'
D.append(dict(slug='40-mots-bureau',date='2026-11-06',title="40 mots d'anglais",sub="indispensables au bureau",emoji='💼',
 tip="Colle cette fiche près de ton bureau : chaque jour, apprends 5 mots et utilise-les dans une phrase.",
 p1=voct(voc[:24]),p2=voct(voc[24:])+'<h2>✍️ Utilise-les !</h2><p>Complète : 1. I have a ______ at 10 a.m. (réunion) · 2. Please send me the ______ (facture) · 3. The ______ is Friday (date limite).</p><p class="mu">Réponses : meeting · invoice · deadline</p>'))
less1='''<h2>1️⃣ « I eat » : le present simple</h2><p>Pour ce qui est <b>vrai en général</b>, les <b>habitudes</b>, ce qu'on fait souvent.</p>
<div class="ex2">I <b>eat</b> rice every day. · She <b>works</b> in a bank. · We <b>play</b> football on Sundays.</div>
<p>⚠️ Avec <b>he / she / it</b>, on ajoute <b>-s</b> : he work<b>s</b>, she eat<b>s</b>.<br>Mots-indices : <i>every day, always, usually, often, never</i>.</p>
<h2>2️⃣ « I'm eating » : le present continuous</h2><p>Pour ce qui se passe <b>maintenant</b>, en ce moment.</p>
<div class="ex2">I <b>am eating</b> now. · She <b>is working</b> today. · They <b>are playing</b> right now.</div>
<p>Formule : <b>am / is / are + verbe-ing</b>.<br>Mots-indices : <i>now, right now, at the moment, today, look!</i></p>
<h2>🔎 La différence en une image</h2><table><tr><td>☕ I <b>drink</b> coffee every morning.</td><td class="fr">habitude</td></tr><tr><td>☕ I <b>am drinking</b> coffee now.</td><td class="fr">en ce moment</td></tr></table>'''
less2='''<h2>✍️ À toi de jouer !</h2><p>Choisis la bonne forme :</p><table>
<tr><td class="n">1</td><td>Look! It (rains / is raining).</td></tr><tr><td class="n">2</td><td>Tom (goes / is going) to school every day.</td></tr>
<tr><td class="n">3</td><td>I (watch / am watching) TV right now.</td></tr><tr><td class="n">4</td><td>She always (drinks / is drinking) tea.</td></tr>
<tr><td class="n">5</td><td>We (study / are studying) English at the moment.</td></tr><tr><td class="n">6</td><td>My father (works / is working) in London.</td></tr></table>
<p class="mu">Réponses : 1. is raining · 2. goes · 3. am watching · 4. drinks · 5. are studying · 6. works</p>'''
D.append(dict(slug='present-simple-continuous',date='2026-11-07',title="I eat ou I'm eating ?",sub="la mini-leçon pour ne plus confondre",emoji='📘',
 tip="Retiens la règle : habitude = present simple · maintenant = present continuous.",p1=less1,p2=less2))
dia=[("Waiter","Good evening! A table for two?","goud îv-ning ! eu téï-beul for tou ?","Bonsoir ! Une table pour deux ?"),
("Emma","Yes, please. Can we sit near the window?","yèss plîz. kèn wî sit nîr zeu win-do ?","Oui. Pouvons-nous nous asseoir près de la fenêtre ?"),
("Waiter","Of course. Here is the menu.","ov korss. hîr iz zeu mè-nyou","Bien sûr. Voici le menu."),
("Jack","What do you recommend?","wot dou you rè-ko-mènd ?","Que nous conseillez-vous ?"),
("Waiter","The grilled fish is very good today.","zeu grild fich iz vè-ri goud tou-déï","Le poisson grillé est très bon aujourd'hui."),
("Jack","OK, I'll have the fish, please.","o-kéï, aïl hèv zeu fich, plîz","D'accord, je prends le poisson."),
("Emma","And I'd like a chicken salad.","ènd aïd laïk eu tchi-kin sè-leud","Et je voudrais une salade de poulet."),
("Waiter","Anything to drink?","è-ni-ssing tou drink ?","Quelque chose à boire ?"),
("Emma","Two glasses of orange juice, please.","tou glâ-siz ov o-rindj djouss, plîz","Deux verres de jus d'orange."),
("Jack","Excuse me, can we have the bill?","ex-kyouz mî, kèn wî hèv zeu bil ?","Excusez-moi, l'addition s'il vous plaît ?"),
("Waiter","Here you are. Have a nice evening!","hîr you âr. hèv eu naïss îv-ning !","Voilà. Bonne soirée !")]
def diat(rows):
    h='<table class="dia">'
    for who,en,pr,fr in rows: h+=f'<tr><td class="who">{who}</td><td><b>{en}</b><span class="pr">🔊 {pr}</span><span class="fr2">{fr}</span></td></tr>'
    return h+'</table>'
D.append(dict(slug='dialogue-restaurant',date='2026-11-08',title="Au restaurant",sub="un dialogue complet, avec la prononciation",emoji='🍽️',
 tip="Lis le dialogue à deux : une personne fait Emma et Jack, l'autre fait le serveur. Puis échangez les rôles !",
 p1=diat(dia[:7]),p2=diat(dia[7:])+'<h2>📌 Les mots à retenir</h2><table><tr><td><b>menu</b> = carte</td><td><b>waiter</b> = serveur</td></tr><tr><td><b>bill</b> = addition</td><td><b>I\'ll have…</b> = je prends…</td></tr><tr><td><b>I\'d like…</b> = je voudrais…</td><td><b>to recommend</b> = conseiller</td></tr></table>'))
vb=[("be","was / were","been","être"),("have","had","had","avoir"),("do","did","done","faire"),("go","went","gone","aller"),("say","said","said","dire"),("get","got","got","obtenir"),("make","made","made","fabriquer / faire"),("know","knew","known","savoir"),("think","thought","thought","penser"),("take","took","taken","prendre"),
("see","saw","seen","voir"),("come","came","come","venir"),("give","gave","given","donner"),("find","found","found","trouver"),("tell","told","told","raconter"),("become","became","become","devenir"),("leave","left","left","partir / laisser"),("feel","felt","felt","ressentir"),("bring","brought","brought","apporter"),("begin","began","begun","commencer"),
("keep","kept","kept","garder"),("write","wrote","written","écrire"),("speak","spoke","spoken","parler"),("buy","bought","bought","acheter"),("pay","paid","paid","payer"),("meet","met","met","rencontrer"),("sleep","slept","slept","dormir"),("eat","ate","eaten","manger"),("drink","drank","drunk","boire"),("understand","understood","understood","comprendre")]
def vbt(rows,s):
    h='<table class="vb"><tr><th></th><th>Base</th><th>Passé</th><th>Participe</th><th>Français</th></tr>'
    for k,(a,b,c,d) in enumerate(rows): h+=f'<tr><td class="n">{s+k}</td><td><b>{a}</b></td><td>{b}</td><td>{c}</td><td class="fr">{d}</td></tr>'
    return h+'</table>'
D.append(dict(slug='30-verbes-irreguliers',date='2026-11-09',title="30 verbes irréguliers",sub="les plus utilisés en anglais",emoji='🔁',
 tip="Récite-les par groupes de 5 à voix haute : base – passé – participe. Ex. : go – went – gone.",
 p1=vbt(vb[:18],1),p2=vbt(vb[18:],19)+'<h2>✍️ Mets au passé</h2><p>1. I (go) to London last year. · 2. She (buy) a new phone. · 3. We (eat) pizza yesterday.</p><p class="mu">Réponses : went · bought · ate</p>'))
idi=[("Break the ice","brék zi aïss","Briser la glace","Let's play a game to break the ice."),("It's a piece of cake","its eu pîss ov kéïk","C'est facile","This exercise is a piece of cake!"),("Hit the books","hit zeu bouks","Se mettre à étudier","I have an exam, I need to hit the books."),("Under the weather","eun-deur zeu wè-zeur","Pas en forme","I'm feeling under the weather today."),("Once in a blue moon","weunss in eu blou moun","Très rarement","He calls me once in a blue moon."),("Cost an arm and a leg","kost eun ârm ènd eu lèg","Coûter les yeux de la tête","This car costs an arm and a leg."),("Better late than never","bè-teur léït zèn nè-veur","Mieux vaut tard que jamais","You came! Better late than never."),("Call it a day","kôl it eu déï","Arrêter pour aujourd'hui","It's 8 p.m., let's call it a day."),
("On cloud nine","on klaoud naïn","Aux anges","She got the job, she's on cloud nine!"),("Get the ball rolling","guèt zeu bôl ro-ling","Lancer les choses","Let's get the ball rolling!"),("Keep an eye on","kîp eun aï on","Surveiller","Can you keep an eye on my bag?"),("Spill the beans","spil zeu bînz","Vendre la mèche","Come on, spill the beans!"),("Take it easy","téïk it î-zi","Vas-y doucement / Détends-toi","Take it easy, it's the weekend."),("Speak of the devil","spîk ov zeu dè-veul","Quand on parle du loup…","Speak of the devil, here's Tom!"),("The best of both worlds","zeu bèst ov bos weurldz","Le meilleur des deux mondes","Online classes give you the best of both worlds.")]
def idt(rows,s):
    h='<table>'
    for k,(en,pr,fr,ex) in enumerate(rows): h+=f'<tr><td class="n">{s+k}</td><td><b>{en}</b><span class="pr">🔊 {pr}</span><span class="ex">« {ex} »</span></td><td class="fr">{fr}</td></tr>'
    return h+'</table>'
D.append(dict(slug='15-expressions-natifs',date='2026-11-10',title="15 expressions anglaises",sub="que les natifs adorent",emoji='💬',
 tip="Ces expressions ne se traduisent pas mot à mot ! Apprends le sens et l'exemple ensemble.",p1=idt(idi[:8],1),p2=idt(idi[8:],9)))
