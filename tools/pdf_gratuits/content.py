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
# ---------- Semaine 2 : 11 au 17 novembre ----------
quiz=[("« Je suis fatigué » se dit :","I have tired","I am tired","I tired","B"),
("Complète : She ___ English every day.","study","studys","studies","C"),
("« Combien ça coûte ? »","How much is it?","How many is it?","How cost it?","A"),
("Le passé de « buy » :","buyed","bought","brought","B"),
("« J'ai 30 ans »","I have 30 years","I am 30","I make 30 years","B"),
("Complète : I'm good ___ English.","in","at","on","B"),
("« Il pleut »","It rains now","It's raining","It is rain","B"),
("Complète : There ___ two cars.","is","are","have","B"),
("« Je suis d'accord »","I agree","I am agree","I'm agreed","A"),
("Complète : I was born ___ 1995.","on","at","in","C"),
("« Réunion » en anglais :","reunion","meeting","assembly","B"),
("Complète : He ___ like coffee.","don't","doesn't","not","B"),
("« Pouvez-vous répéter ? »","Can you repeat, please?","Can you say again me?","You repeat?","A"),
("Complète : I have lived here ___ 2020.","for","since","from","B"),
("« Actually » veut dire :","actuellement","en réalité","activement","B"),
("Complète : She is ___ than her sister.","more tall","taller","tallest","B"),
("« Je cherche mes clés »","I'm looking for my keys","I search my keys","I look my keys","A"),
("Complète : ___ you like tea?","Do","Are","Does","A"),
("« Un conseil » :","an advice","a piece of advice","one advices","B"),
("Complète : See you ___ Monday!","in","at","on","C")]
def quizt(rows,s):
    h='<table>'
    for k,(q,a,b,c,_) in enumerate(rows): h+=f'<tr><td class="n">{s+k}</td><td><b>{q}</b><span class="fr2">A. {a} &nbsp;·&nbsp; B. {b} &nbsp;·&nbsp; C. {c}</span></td></tr>'
    return h+'</table>'
qans=' · '.join(f'{i+1}. {r[4]}' for i,r in enumerate(quiz))
D.append(dict(slug='quiz-20-questions',date='2026-11-11',title="Quiz : quel est ton niveau ?",sub="20 questions pour tester ton anglais",emoji='🎯',
 tip="Réponds sans regarder les réponses, compte tes points à la fin, puis lis ton résultat. Sois honnête !",
 p1=quizt(quiz[:11],1),p2=quizt(quiz[11:],12)+f'<p class="mu">Réponses : {qans}</p><h2>📊 Ton résultat</h2><table><tr><td><b>0 à 8</b></td><td class="fr">Débutant : les bases d\'abord, tu vas vite progresser 💪</td></tr><tr><td><b>9 à 15</b></td><td class="fr">Intermédiaire : tu comprends, maintenant il faut parler 🗣️</td></tr><tr><td><b>16 à 20</b></td><td class="fr">Avancé : bravo ! Viens pratiquer l\'oral 🔥</td></tr></table>'))
ff=[("actually","ak-tchou-eu-li","en réalité","actuellement = currently"),("library","laï-breu-ri","bibliothèque","librairie = bookshop"),("eventually","i-vèn-tchou-eu-li","finalement","éventuellement = possibly"),("to attend","tou eu-tènd","assister à","attendre = to wait"),("sensible","sèn-si-beul","raisonnable","sensible = sensitive"),("a journey","eu djeur-ni","un voyage","journée = day"),("to pretend","tou pri-tènd","faire semblant","prétendre = to claim"),("a coin","eu koïn","une pièce de monnaie","coin = corner"),("a lecture","eu lèk-tcheur","un cours magistral","lecture = reading"),("a car","eu kâr","une voiture","car (bus) = coach"),
("deception","di-sèp-cheun","tromperie","déception = disappointment"),("to rest","tou rèst","se reposer","rester = to stay"),("a location","eu lo-kéï-cheun","un endroit","location = rental"),("to assist","tou eu-sist","aider","assister = to attend"),("chance","tchânss","hasard / occasion","chance = luck")]
def fft(rows,s):
    h='<table>'
    for k,(en,pr,fr,trap) in enumerate(rows): h+=f'<tr><td class="n">{s+k}</td><td><b>{en}</b><span class="pr">🔊 {pr}</span><span class="ex">⚠️ {trap}</span></td><td class="fr">✅ {fr}</td></tr>'
    return h+'</table>'
D.append(dict(slug='15-faux-amis',date='2026-11-12',title="15 faux amis",sub="les mots anglais qui te piègent",emoji='⚠️',
 tip="Un « faux ami » ressemble à un mot français mais ne veut pas dire la même chose. Lis bien la ligne ⚠️ : c'est le piège à éviter.",
 p1=fft(ff[:8],1),p2=fft(ff[8:],9)+'<h2>✍️ Corrige la phrase</h2><p>1. I went to the <i>librairie</i> to borrow a book. · 2. <i>Actually</i>, I live in Boston (= en ce moment). · 3. I need to <i>rester</i> after work (= me reposer).</p><p class="mu">Réponses : library · Currently · rest</p>'))
iol1='''<h2>⏰ Pour le temps</h2><table>
<tr><td><b>AT</b></td><td>une heure précise : <b>at</b> 7 o'clock, <b>at</b> noon, <b>at</b> night, <b>at</b> the weekend</td></tr>
<tr><td><b>ON</b></td><td>un jour, une date : <b>on</b> Monday, <b>on</b> 14 November, <b>on</b> my birthday</td></tr>
<tr><td><b>IN</b></td><td>un mois, une année, une saison, un moment de la journée : <b>in</b> May, <b>in</b> 2026, <b>in</b> summer, <b>in</b> the morning</td></tr></table>
<h2>📍 Pour le lieu</h2><table>
<tr><td><b>AT</b></td><td>un point précis : <b>at</b> the bus stop, <b>at</b> home, <b>at</b> work, <b>at</b> school</td></tr>
<tr><td><b>ON</b></td><td>une surface : <b>on</b> the table, <b>on</b> the wall, <b>on</b> the bus, <b>on</b> Facebook</td></tr>
<tr><td><b>IN</b></td><td>à l'intérieur, une ville, un pays : <b>in</b> the box, <b>in</b> my bag, <b>in</b> London, <b>in</b> Canada</td></tr></table>
<h2>🔺 L'astuce de la pyramide</h2><div class="ex2"><b>IN</b> = grand (pays, année) → <b>ON</b> = moyen (rue, jour) → <b>AT</b> = petit et précis (adresse, heure)</div>'''
iol2='''<h2>✍️ À toi de jouer : in, on ou at ?</h2><table>
<tr><td class="n">1</td><td>The meeting is ___ 10 a.m.</td></tr><tr><td class="n">2</td><td>I was born ___ 1998.</td></tr>
<tr><td class="n">3</td><td>See you ___ Saturday!</td></tr><tr><td class="n">4</td><td>My keys are ___ the table.</td></tr>
<tr><td class="n">5</td><td>She lives ___ Manchester.</td></tr><tr><td class="n">6</td><td>I'm ___ work right now.</td></tr>
<tr><td class="n">7</td><td>We go to the beach ___ summer.</td></tr><tr><td class="n">8</td><td>I saw it ___ Instagram.</td></tr></table>
<p class="mu">Réponses : 1. at · 2. in · 3. on · 4. on · 5. in · 6. at · 7. in · 8. on</p>'''
D.append(dict(slug='in-on-at',date='2026-11-13',title="IN, ON ou AT ?",sub="la mini-leçon des prépositions",emoji='📍',
 tip="Retiens la pyramide : IN pour le plus grand, ON pour le moyen, AT pour le plus précis.",p1=iol1,p2=iol2))
air=[("Agent","Good morning. Your passport, please.","goud mor-ning. yor pâss-port, plîz","Bonjour. Votre passeport, s'il vous plaît."),
("Sarah","Here you are.","hîr you âr","Le voici."),
("Agent","Where are you flying to today?","wèr âr you flaï-ing tou tou-déï ?","Où allez-vous aujourd'hui ?"),
("Sarah","To New York.","tou nyou york","À New York."),
("Agent","Do you have any bags to check in?","dou you hèv è-ni bègz tou tchèk in ?","Avez-vous des bagages à enregistrer ?"),
("Sarah","Yes, just one suitcase.","yèss, djeust weun sout-kéïss","Oui, une seule valise."),
("Agent","Would you like a window or an aisle seat?","woud you laïk eu win-do or eun aïl sît ?","Côté hublot ou côté couloir ?"),
("Sarah","A window seat, please.","eu win-do sît, plîz","Côté hublot, s'il vous plaît."),
("Agent","Here is your boarding pass. Gate 12.","hîr iz yor bor-ding pâss. guéït twèlv","Voici votre carte d'embarquement. Porte 12."),
("Sarah","What time does boarding start?","wot taïm deuz bor-ding stârt ?","À quelle heure commence l'embarquement ?"),
("Agent","At 9:30. Have a nice flight!","èt naïn ssêr-ti. hèv eu naïss flaït !","À 9 h 30. Bon vol !")]
D.append(dict(slug='dialogue-aeroport',date='2026-11-14',title="À l'aéroport",sub="un dialogue complet, avec la prononciation",emoji='✈️',
 tip="Lis le dialogue à deux : une personne fait Sarah, l'autre fait l'agent. Puis échangez les rôles !",
 p1=diat(air[:7]),p2=diat(air[7:])+'<h2>📌 Les mots à retenir</h2><table><tr><td><b>flight</b> = vol</td><td><b>suitcase</b> = valise</td></tr><tr><td><b>to check in</b> = enregistrer</td><td><b>boarding pass</b> = carte d\'embarquement</td></tr><tr><td><b>gate</b> = porte</td><td><b>aisle seat</b> = siège côté couloir</td></tr><tr><td><b>delayed</b> = en retard</td><td><b>departure / arrival</b> = départ / arrivée</td></tr></table>'))
em1='''<h2>📧 Le modèle à copier</h2><div class="ex2" style="font-size:10.3pt;line-height:1.55">
<b>Subject:</b> Request for information<br><br>Dear Mr Smith,<br><br>I hope you are well.<br>
I am writing to ask for more information about your English courses.<br>
Could you please send me the prices and the schedule?<br><br>
Thank you in advance for your help.<br>I look forward to hearing from you.<br><br>Best regards,<br>Anna Brown</div>
<h2>🧩 Les 3 parties d'un email</h2><table>
<tr><td class="n">1</td><td><b>L'ouverture</b><span class="fr2">Dear Mr / Ms + nom (formel) · Hi Tom (collègue)</span></td></tr>
<tr><td class="n">2</td><td><b>Le message</b><span class="fr2">Pourquoi tu écris, en 2 ou 3 phrases courtes</span></td></tr>
<tr><td class="n">3</td><td><b>La fermeture</b><span class="fr2">Best regards (formel) · Thanks / Cheers (collègue)</span></td></tr></table>'''
emph=[("I am writing to…","J'écris pour…"),("Please find attached…","Veuillez trouver ci-joint…"),("Could you please…?","Pourriez-vous…?"),("I would like to…","Je voudrais…"),("Thank you for your email.","Merci pour votre email."),("Sorry for the late reply.","Désolé pour la réponse tardive."),("Let me know if…","Dites-moi si…"),("I look forward to hearing from you.","Dans l'attente de votre réponse."),("Best regards,","Cordialement,")]
em2='<h2>💬 9 phrases à réutiliser</h2><table>'+''.join(f'<tr><td class="n">{i+1}</td><td><b>{a}</b></td><td class="fr">{b}</td></tr>' for i,(a,b) in enumerate(emph))+'</table><h2>✍️ À toi !</h2><p>Écris un email à ton manager pour demander un jour de congé (<i>a day off</i>) vendredi. Utilise au moins 3 phrases ci-dessus.</p>'
D.append(dict(slug='email-professionnel',date='2026-11-15',title="Écrire un email pro",sub="en anglais, avec le modèle à copier",emoji='📧',
 tip="Un bon email en anglais est court et poli. Copie le modèle, adapte-le à ta situation, et c'est envoyé !",p1=em1,p2=em2))
pv=[("get up","guèt eup","se lever","I get up at 6 every day."),("wake up","wéïk eup","se réveiller","I woke up late today."),("look for","louk for","chercher","I'm looking for my phone."),("find out","faïnd aout","découvrir","I found out the truth."),("give up","guiv eup","abandonner","Never give up!"),("turn on / off","teurn on / of","allumer / éteindre","Turn off the light, please."),("put on","pout on","mettre (un vêtement)","Put on your jacket."),("take off","téïk of","enlever / décoller","The plane takes off at 9."),("pick up","pik eup","ramasser / aller chercher","I'll pick you up at 5."),("call back","kôl bèk","rappeler","Can you call me back?"),
("come back","keum bèk","revenir","I'll come back tomorrow."),("go out","go aout","sortir","Let's go out tonight!"),("sit down","sit daoun","s'asseoir","Please sit down."),("look after","louk âf-teur","s'occuper de","She looks after her son."),("run out of","reun aout ov","ne plus avoir de","We ran out of milk."),("fill in","fil in","remplir (un formulaire)","Fill in this form, please."),("set up","sèt eup","installer / créer","I set up my new phone."),("carry on","kè-ri on","continuer","Carry on, you're doing well!"),("check in","tchèk in","s'enregistrer","We checked in at the hotel."),("hang up","hèng eup","raccrocher","Don't hang up!")]
def pvt(rows,s):
    h='<table>'
    for k,(en,pr,fr,ex) in enumerate(rows): h+=f'<tr><td class="n">{s+k}</td><td><b>{en}</b><span class="pr">🔊 {pr}</span><span class="ex">« {ex} »</span></td><td class="fr">{fr}</td></tr>'
    return h+'</table>'
D.append(dict(slug='20-phrasal-verbs',date='2026-11-16',title="20 phrasal verbs",sub="indispensables au quotidien",emoji='🔗',
 tip="Un phrasal verb = un verbe + une petite particule (up, on, off…) qui change le sens. Apprends-les avec leur exemple !",
 p1=pvt(pv[:10],1),p2=pvt(pv[10:],11)))
tel=[("Hello, this is Anna speaking.","hè-lo, ziss iz è-na spî-king","Allô, c'est Anna."),("Could I speak to Mr Smith, please?","koud aï spîk tou miss-teur smiss, plîz ?","Pourrais-je parler à M. Smith ?"),("Who's calling, please?","houz kô-ling, plîz ?","Qui est à l'appareil ?"),("Hold on, please.","hold on, plîz","Ne quittez pas."),("I'll put you through.","aïl pout you srou","Je vous le passe."),("He's not available right now.","hîz not eu-véï-leu-beul raït nao","Il n'est pas disponible pour le moment."),("Can I take a message?","kèn aï téïk eu mè-sidj ?","Puis-je prendre un message ?"),("Could you call back later?","koud you kôl bèk léï-teur ?","Pouvez-vous rappeler plus tard ?"),("Sorry, I didn't catch that.","so-ri, aï di-deunt kètch zèt","Pardon, je n'ai pas compris."),
("Could you speak more slowly?","koud you spîk mor slo-li ?","Pouvez-vous parler plus lentement ?"),("Can you spell that, please?","kèn you spèl zèt, plîz ?","Pouvez-vous l'épeler ?"),("The line is bad.","zeu laïn iz bèd","La ligne est mauvaise."),("I'll send you a text.","aïl sènd you eu tèkst","Je vous envoie un SMS."),("What's your number?","wots yor neum-beur ?","Quel est votre numéro ?"),("Thanks for calling.","sènks for kô-ling","Merci d'avoir appelé."),("Talk to you soon. Bye!","tôk tou you soun. baï !","À bientôt. Au revoir !")]
def telt(rows,s):
    h='<table>'
    for k,(en,pr,fr) in enumerate(rows): h+=f'<tr><td class="n">{s+k}</td><td><b>{en}</b><span class="pr">🔊 {pr}</span></td><td class="fr">{fr}</td></tr>'
    return h+'</table>'
D.append(dict(slug='telephone-anglais',date='2026-11-17',title="Au téléphone",sub="16 phrases pour appeler en anglais",emoji='📞',
 tip="Au téléphone, on ne voit pas la personne : c'est plus dur ! Garde cette fiche à côté de toi pendant tes appels.",
 p1=telt(tel[:9],1),p2=telt(tel[9:],10)))
# ---- Semaine 3 : 18 → 24 novembre ----
h1='''<h2>❓ Demander l'heure</h2><table><tr><td><b>What time is it?</b><span class="pr">🔊 wot taïm iz it ?</span></td><td class="fr">Quelle heure est-il ?</td></tr>
<tr><td><b>Do you have the time?</b><span class="pr">🔊 dou you hèv zeu taïm ?</span></td><td class="fr">Vous avez l'heure ?</td></tr></table>
<h2>1️⃣ La méthode facile : l'heure + les minutes</h2><div class="ex2">7:15 → <b>seven fifteen</b> (sè-veun fif-tîn) · 9:40 → <b>nine forty</b> (naïn for-ti) · 11:05 → <b>eleven oh five</b> (i-lè-veun o faïv)</div>
<h2>2️⃣ La méthode classique : past et to</h2><table>
<tr><td>🕒 3:00</td><td><b>three o'clock</b><span class="pr">🔊 srî o-klok</span></td><td class="fr">trois heures pile</td></tr>
<tr><td>🕒 3:10</td><td><b>ten past three</b><span class="pr">🔊 tèn pâst srî</span></td><td class="fr">3 h 10 (past = après)</td></tr>
<tr><td>🕒 3:15</td><td><b>a quarter past three</b><span class="pr">🔊 eu kwor-teur pâst srî</span></td><td class="fr">3 h et quart</td></tr>
<tr><td>🕞 3:30</td><td><b>half past three</b><span class="pr">🔊 hâf pâst srî</span></td><td class="fr">3 h et demie</td></tr>
<tr><td>🕓 3:45</td><td><b>a quarter to four</b><span class="pr">🔊 eu kwor-teur tou for</span></td><td class="fr">4 h moins le quart (to = avant)</td></tr>
<tr><td>🕓 3:50</td><td><b>ten to four</b><span class="pr">🔊 tèn tou for</span></td><td class="fr">4 h moins 10</td></tr></table>
<h2>☀️ Le matin ou le soir ?</h2><p><b>a.m.</b> (éï-èm) = de minuit à midi · <b>p.m.</b> (pî-èm) = de midi à minuit<br><b>noon</b> (noun) = midi · <b>midnight</b> (mid-naït) = minuit</p>'''
h2='''<h2>✍️ À toi de jouer : écris l'heure en anglais</h2><table>
<tr><td class="n">1</td><td>8:00</td><td class="n">5</td><td>2:45</td></tr><tr><td class="n">2</td><td>10:30</td><td class="n">6</td><td>6:20</td></tr>
<tr><td class="n">3</td><td>4:15</td><td class="n">7</td><td>9:55</td></tr><tr><td class="n">4</td><td>12:00 (le jour)</td><td class="n">8</td><td>1:05</td></tr></table>
<p class="mu">Réponses : 1. eight o'clock · 2. half past ten · 3. a quarter past four · 4. noon / twelve o'clock · 5. a quarter to three · 6. twenty past six · 7. five to ten · 8. five past one</p>
<h2>💬 Phrases utiles</h2><table>
<tr><td><b>At what time…?</b><span class="pr">🔊 èt wot taïm…?</span></td><td class="fr">À quelle heure… ?</td></tr>
<tr><td><b>I'm on time.</b><span class="pr">🔊 aïm on taïm</span></td><td class="fr">Je suis à l'heure.</td></tr>
<tr><td><b>Sorry, I'm late.</b><span class="pr">🔊 so-ri, aïm léït</span></td><td class="fr">Désolé, je suis en retard.</td></tr>
<tr><td><b>It's early.</b><span class="pr">🔊 its eur-li</span></td><td class="fr">Il est tôt.</td></tr></table>'''
D.append(dict(slug='dire-l-heure',date='2026-11-18',title="Quelle heure est-il ?",sub="dire l'heure en anglais sans se tromper",emoji='⏰',
 tip="Commence par la méthode facile (seven fifteen), puis entraîne-toi avec past et to en regardant ta montre plusieurs fois par jour.",p1=h1,p2=h2))
shop=[("Assistant","Hello! Can I help you?","hè-lo ! kèn aï hèlp you ?","Bonjour ! Je peux vous aider ?"),
("Lucy","Yes, I'm looking for a blue shirt.","yèss, aïm lou-king for eu blou cheurt","Oui, je cherche une chemise bleue."),
("Assistant","What size are you?","wot saïz âr you ?","Quelle taille faites-vous ?"),
("Lucy","Medium, I think.","mî-di-eum, aï sink","Médium, je crois."),
("Assistant","Here you are. The fitting room is over there.","hîr you âr. zeu fi-ting roum iz o-veur zèr","Voici. La cabine d'essayage est là-bas."),
("Lucy","It's a bit too small. Do you have a large?","its eu bit tou smôl. dou you hèv eu lârdj ?","C'est un peu petit. Vous avez du large ?"),
("Assistant","Yes, here it is.","yèss, hîr it iz","Oui, la voici."),
("Lucy","Perfect! How much is it?","peur-fikt ! hao meutch iz it ?","Parfait ! Combien ça coûte ?"),
("Assistant","It's on sale today: twenty pounds.","its on séïl tou-déï : twèn-ti paoundz","Elle est en promo aujourd'hui : 20 livres."),
("Lucy","Great, I'll take it. Can I pay by card?","gréït, aïl téïk it. kèn aï péï baï kârd ?","Super, je la prends. Je peux payer par carte ?"),
("Assistant","Of course. Here's your receipt. Have a nice day!","ov korss. hîrz yor ri-sît. hèv eu naïss déï !","Bien sûr. Voici votre ticket. Bonne journée !")]
D.append(dict(slug='dialogue-magasin',date='2026-11-19',title="Dans un magasin",sub="un dialogue complet, avec la prononciation",emoji='🛍️',
 tip="Lis le dialogue à deux : une personne fait Lucy, l'autre fait le vendeur. Puis remplace « shirt » par « dress », « shoes »… et recommence !",
 p1=diat(shop[:7]),p2=diat(shop[7:])+'<h2>📌 Les mots à retenir</h2><table><tr><td><b>size</b> = taille</td><td><b>fitting room</b> = cabine d\'essayage</td></tr><tr><td><b>too small / too big</b> = trop petit / trop grand</td><td><b>on sale</b> = en promotion</td></tr><tr><td><b>How much is it?</b> = combien ?</td><td><b>receipt</b> = ticket de caisse</td></tr><tr><td><b>I\'ll take it</b> = je le prends</td><td><b>cash / card</b> = espèces / carte</td></tr></table>'))
pron=[("comfortable","kom-for-ta-ble","keumf-teu-beul","On « avale » le milieu : 3 syllabes seulement."),
("vegetable","vé-gé-ta-ble","vèdj-teu-beul","Le 2ᵉ « e » ne se prononce pas."),
("Wednesday","ouèd-nèss-dé","wènz-déï","Le « d » est muet : comme « Wens-day »."),
("island","is-land","aï-leund","Le « s » est muet."),
("receipt","ré-cé-ipt","ri-sît","Le « p » est muet."),
("clothes","klo-tèss","klôdz","Une seule syllabe !"),
("recipe","ré-cipe","rè-si-pi","3 syllabes, le « e » final se prononce."),
("chocolate","cho-co-la-te","tcho-kleut","2 syllabes seulement."),
("women","ou-o-mèn","wi-min","Le « o » se dit « i »."),
("answer","an-sou-eur","ân-seur","Le « w » est muet."),
("knife","k-naïf","naïf","Le « k » devant « n » est toujours muet."),
("listen","lis-tèn","li-seun","Le « t » est muet.")]
def pront(rows,s):
    h='<table class="err">'
    for k,(w,bad,good,e) in enumerate(rows): h+=f'<tr><td class="n">{s+k}</td><td><b style="font-size:13pt">{w}</b><span class="bad">❌ {bad}</span><span class="good">✅ 🔊 {good}</span><span class="ex">{e}</span></td></tr>'
    return h+'</table>'
D.append(dict(slug='12-mots-mal-prononces',date='2026-11-20',title="12 mots anglais",sub="que presque tout le monde prononce mal",emoji='🔊',
 tip="Lis la bonne prononciation (en vert) 5 fois à voix haute. Le secret : en anglais, beaucoup de lettres sont muettes !",
 p1=pront(pron[:6],1),p2=pront(pron[6:],7)))
wg1='''<h2>1️⃣ WILL : décider maintenant, promettre, prévoir</h2><p>Quand tu décides <b>au moment où tu parles</b>, pour une promesse, ou une prévision sans preuve.</p>
<div class="ex2">The phone is ringing. I<b>'ll</b> answer it! · I <b>will</b> call you tomorrow, I promise. · I think it <b>will</b> rain.</div>
<p>Formule : <b>will + verbe</b> (I'll, you'll, she'll…) · Négatif : <b>won't</b> (wont) = will not</p>
<h2>2️⃣ GOING TO : un projet déjà décidé, une preuve</h2><p>Quand c'est <b>déjà prévu</b> avant de parler, ou quand on <b>voit</b> que ça va arriver.</p>
<div class="ex2">I'<b>m going to</b> visit my aunt this weekend. · Look at the clouds! It'<b>s going to</b> rain.</div>
<p>Formule : <b>am / is / are + going to + verbe</b> · 🔊 à l'oral : <i>gonna</i> (go-na)</p>
<h2>🔎 La différence en une image</h2><table><tr><td>🛒 « There's no milk! » — « OK, I<b>'ll</b> buy some. »</td><td class="fr">décision immédiate</td></tr><tr><td>🛒 I<b>'m going to</b> buy milk after work.</td><td class="fr">déjà prévu</td></tr></table>'''
wg2='''<h2>✍️ À toi de jouer : will ou going to ?</h2><table>
<tr><td class="n">1</td><td>« I'm cold. » — « I (will / am going to) close the window. »</td></tr>
<tr><td class="n">2</td><td>We (will / are going to) travel to Boston next month. We have the tickets.</td></tr>
<tr><td class="n">3</td><td>Don't worry, I (will / am going to) help you.</td></tr>
<tr><td class="n">4</td><td>Look! That glass (will / is going to) fall!</td></tr>
<tr><td class="n">5</td><td>I think Chelsea (will / is going to) win the match.</td></tr>
<tr><td class="n">6</td><td>She (will / is going to) start a new job on Monday. She signed the contract.</td></tr></table>
<p class="mu">Réponses : 1. will · 2. are going to · 3. will · 4. is going to · 5. will · 6. is going to</p>'''
D.append(dict(slug='will-going-to',date='2026-11-21',title="Will ou going to ?",sub="la mini-leçon pour parler du futur",emoji='🔮',
 tip="Retiens la règle : décision sur le moment = will · projet déjà décidé = going to.",p1=wg1,p2=wg2))
adj=[("😊","kind","kaïnd","gentil"),("😂","funny","feu-ni","drôle"),("🙈","shy","chaï","timide"),("🤗","friendly","frènd-li","sympathique"),("😴","lazy","léï-zi","paresseux"),("💪","hard-working","hârd-weur-king","travailleur"),("🧠","smart","smârt","intelligent"),("🤞","honest","o-nist","honnête"),("🙏","polite","po-laït","poli"),("😠","rude","roud","impoli"),("🎁","generous","djè-neu-reuss","généreux"),("🙄","selfish","sèl-fich","égoïste"),
("⏳","patient","péï-cheunt","patient"),("😌","calm","kâm","calme"),("🦁","brave","bréïv","courageux"),("😁","cheerful","tchîr-foul","joyeux"),("🐂","stubborn","steu-beurn","têtu"),("🗣️","talkative","tô-keu-tiv","bavard"),("🤝","reliable","ri-laï-eu-beul","fiable"),("👑","bossy","bo-si","autoritaire"),("😎","confident","kon-fi-deunt","sûr de soi"),("😟","nervous","neur-veuss","nerveux"),("🎨","creative","kri-éï-tiv","créatif"),("🧹","tidy","taï-di","ordonné"),
("📏","tall","tôl","grand"),("🔽","short","chort","petit"),("🌿","slim","slim","mince"),("👶","young","yeung","jeune"),("🌹","beautiful","byou-ti-foul","belle"),("🕴️","handsome","hèn-seum","beau (homme)")]
D.append(dict(slug='30-adjectifs-personne',date='2026-11-22',title="30 adjectifs",sub="pour décrire une personne",emoji='🧑',
 tip="Pour chaque mot, pense à une personne que tu connais qui lui correspond : c'est le meilleur moyen de ne plus l'oublier !",
 p1=voct(adj[:24]),p2=voct(adj[24:])+'''<p class="mu">⚠️ <b>handsome</b> se dit plutôt pour un homme, <b>beautiful</b> / <b>pretty</b> pour une femme.</p>
<h2>✍️ Décris quelqu'un !</h2><div class="ex2">My friend Emily is <b>tall</b> and <b>slim</b>. She is <b>kind</b>, <b>funny</b> and very <b>hard-working</b>. But she is a bit <b>stubborn</b>! 😄</div>
<p>À toi : décris ton meilleur ami en 3 phrases, avec au moins 4 adjectifs de la fiche.</p><p class="mu">Astuce : <b>a bit</b> (eu bit) = un peu · <b>very</b> (vè-ri) = très · <b>so</b> (so) = tellement</p>'''))
itv=[("Tell me about yourself.","tèl mî eu-baout yor-sèlf","Parlez-moi de vous.","I'm Daniel. I have a degree in marketing and three years of experience in sales."),
("Why do you want this job?","waï dou you wont ziss djob ?","Pourquoi voulez-vous ce poste ?","Because I love working with customers and I want to grow with your company."),
("What are your strengths?","wot âr yor strèngs ?","Quelles sont vos qualités ?","I'm hard-working, reliable and I learn quickly."),
("What is your main weakness?","wot iz yor méïn wîk-niss ?","Quel est votre principal défaut ?","Sometimes I'm too perfectionist, but I'm learning to manage my time."),
("Where do you see yourself in five years?","wèr dou you sî yor-sèlf in faïv yîrz ?","Où vous voyez-vous dans 5 ans ?","I see myself as a team manager in this company."),
("Why did you leave your last job?","waï did you lîv yor lâst djob ?","Pourquoi avez-vous quitté votre dernier poste ?","I was looking for new challenges."),
("Can you work in a team?","kèn you weurk in eu tîm ?","Savez-vous travailler en équipe ?","Yes, of course. I enjoy sharing ideas with my colleagues."),
("When can you start?","wèn kèn you stârt ?","Quand pouvez-vous commencer ?","I can start next Monday."),
("Do you have any questions?","dou you hèv è-ni kwès-tcheunz ?","Avez-vous des questions ?","Yes. What does a typical day look like in this job?")]
def itvt(rows,s):
    h='<table>'
    for k,(q,pr,fr,a) in enumerate(rows): h+=f'<tr><td class="n">{s+k}</td><td><b>{q}</b><span class="pr">🔊 {pr}</span><span class="fr2">{fr}</span><span class="ex">💬 « {a} »</span></td></tr>'
    return h+'</table>'
D.append(dict(slug='entretien-embauche',date='2026-11-23',title="L'entretien d'embauche",sub="9 questions en anglais + les réponses modèles",emoji='🤝',
 tip="Adapte chaque réponse modèle à TON parcours, écris-la, puis répète-la à voix haute devant un miroir jusqu'à la dire sans lire.",
 p1=itvt(itv[:5],1),p2=itvt(itv[5:],6)+'<h2>⭐ 3 conseils le jour J</h2><p>1. Souris et dis <b>« Nice to meet you »</b> (naïss tou mît you) en serrant la main.<br>2. Réponds en phrases courtes et simples : c\'est mieux qu\'une longue phrase pleine d\'erreurs.<br>3. Tu n\'as pas compris ? Dis <b>« Could you repeat that, please? »</b> (koud you ri-pît zèt, plîz ?)</p>'))
md1='''<h2>🛠️ MAKE = créer, fabriquer, produire</h2><p>Quand on <b>crée quelque chose</b> qui n'existait pas avant.</p>
<div class="ex2"><b>make</b> a cake (un gâteau) · <b>make</b> a mistake (une erreur) · <b>make</b> a decision (une décision) · <b>make</b> money (de l'argent) · <b>make</b> a phone call (un appel) · <b>make</b> friends (se faire des amis) · <b>make</b> a noise (du bruit) · <b>make</b> a plan (un plan) · <b>make</b> the bed (le lit) · <b>make</b> an effort (un effort)</div>
<h2>✅ DO = faire une activité, une tâche</h2><p>Pour le <b>travail</b>, les <b>tâches</b>, les activités en général.</p>
<div class="ex2"><b>do</b> homework (les devoirs) · <b>do</b> the dishes (la vaisselle) · <b>do</b> sport (du sport) · <b>do</b> business (des affaires) · <b>do</b> a favour (un service) · <b>do</b> your best (de ton mieux) · <b>do</b> the shopping (les courses) · <b>do</b> an exercise (un exercice) · <b>do</b> a job (un travail) · <b>do</b> nothing (rien)</div>
<h2>🔊 Prononciation</h2><p><b>make</b> → méïk · made → méïd &nbsp;|&nbsp; <b>do</b> → dou · did → did · done → deun</p>
<h2>🔎 Le piège classique</h2><table><tr><td><span class="bad">❌ I did a mistake.</span><span class="good">✅ I made a mistake.</span></td></tr></table>'''
md2='''<h2>✍️ À toi de jouer : make ou do ?</h2><table>
<tr><td class="n">1</td><td>Can you ___ me a favour?</td></tr><tr><td class="n">2</td><td>I need to ___ a decision today.</td></tr>
<tr><td class="n">3</td><td>She ___ her homework every evening.</td></tr><tr><td class="n">4</td><td>Don't ___ a noise, the baby is sleeping!</td></tr>
<tr><td class="n">5</td><td>I ___ sport three times a week.</td></tr><tr><td class="n">6</td><td>He ___ a lot of money last year.</td></tr>
<tr><td class="n">7</td><td>Who is going to ___ the dishes?</td></tr><tr><td class="n">8</td><td>It's OK to ___ mistakes when you learn.</td></tr></table>
<p class="mu">Réponses : 1. do · 2. make · 3. does · 4. make · 5. do · 6. made · 7. do · 8. make</p>'''
D.append(dict(slug='make-ou-do',date='2026-11-24',title="Make ou Do ?",sub="la règle + 20 expressions à connaître",emoji='🛠️',
 tip="Retiens l'idée : MAKE = je crée quelque chose · DO = je fais une tâche, une activité.",p1=md1,p2=md2))
# ---- Semaine du 25 novembre au 1er décembre 2026 ----
med=[("Doctor","Good morning. Please, have a seat.","goud mor-ning. plîz, hèv eu sît","Bonjour. Asseyez-vous, je vous prie."),
("Sarah","Thank you, doctor.","ssènk you, dok-teur","Merci, docteur."),
("Doctor","What's the problem?","wots zeu pro-bleum ?","Quel est le problème ?"),
("Sarah","I have a headache and a sore throat.","aï hèv eu hè-déïk ènd eu sor ssrôt","J'ai mal à la tête et mal à la gorge."),
("Doctor","How long have you had it?","haou long hèv you hèd it ?","Depuis combien de temps ?"),
("Sarah","Since Monday. I also have a fever.","sinss meun-déï. aï ol-so hèv eu fî-veur","Depuis lundi. J'ai aussi de la fièvre."),
("Doctor","Let me check your temperature.","lèt mî tchèk yor tèm-preu-tcheur","Laissez-moi prendre votre température."),
("Doctor","It's just a bad cold. Nothing serious.","its djeust eu bèd kold. neu-ssing sî-ri-euss","C'est juste un gros rhume. Rien de grave."),
("Sarah","Do I need any medicine?","dou aï nîd è-ni mèd-sinn ?","Ai-je besoin de médicaments ?"),
("Doctor","Take these tablets twice a day, after meals.","téïk zîz tè-bleuts twaïss eu déï, âf-teur mîlz","Prenez ces comprimés deux fois par jour, après les repas."),
("Doctor","And drink a lot of water. Get some rest.","ènd drink eu lot ov wô-teur. guèt seum rèst","Et buvez beaucoup d'eau. Reposez-vous."),
("Sarah","Thank you very much. Goodbye!","ssènk you vè-ri meutch. goud-baï !","Merci beaucoup. Au revoir !")]
D.append(dict(slug='dialogue-medecin',date='2026-11-25',title="Chez le médecin",sub="un dialogue complet, avec la prononciation",emoji='🩺',
 tip="Lis le dialogue à deux : une personne fait Sarah, l'autre fait le médecin. Puis remplace « headache » par « stomachache » (mal au ventre) et recommence !",
 p1=diat(med[:7]),p2=diat(med[7:])+'<h2>📌 Les mots à retenir</h2><table><tr><td><b>headache</b> (hè-déïk) = mal de tête</td><td><b>stomachache</b> (steu-meuk-éïk) = mal au ventre</td></tr><tr><td><b>sore throat</b> (sor ssrôt) = mal de gorge</td><td><b>fever</b> (fî-veur) = fièvre</td></tr><tr><td><b>cough</b> (kof) = toux</td><td><b>a cold</b> (eu kold) = un rhume</td></tr><tr><td><b>tablets</b> (tè-bleuts) = comprimés</td><td><b>prescription</b> (pris-krip-cheun) = ordonnance</td></tr><tr><td><b>I feel sick</b> (aï fîl sik) = je me sens malade</td><td><b>It hurts here</b> (it heurts hîr) = j\'ai mal ici</td></tr></table>'))
cui=[("🔪","knife","naïf","couteau"),("🍴","fork","fork","fourchette"),("🥄","spoon","spoun","cuillère"),("🍽️","plate","pléït","assiette"),("🥣","bowl","bôl","bol"),("🥛","glass","glâss","verre"),("☕","cup","keup","tasse"),("🍳","frying pan","fraï-ing pèn","poêle"),("🍲","pot","pot","marmite"),("🧊","fridge","fridj","frigo"),("🔥","cooker","kou-keur","cuisinière (appareil)"),("♨️","oven","eu-veun","four"),
("🚰","sink","sink","évier"),("🧂","salt","solt","sel"),("🌶️","pepper","pè-peur","poivre / piment"),("🧅","onion","eu-nyeun","oignon"),("🍅","tomato","to-mâ-to","tomate"),("🥔","potato","po-téï-to","pomme de terre"),("🍚","rice","raïss","riz"),("🍗","chicken","tchi-kin","poulet"),("🐟","fish","fich","poisson"),("🥩","meat","mît","viande"),("🫒","oil","oïl","huile"),("🥚","egg","ègg","œuf"),
("✂️","to cut","tou keut","couper"),("🍳","to fry","tou fraï","frire"),("💧","to boil","tou boïl","faire bouillir"),("🥢","to stir","tou steur","remuer"),("🧽","to wash","tou wôch","laver"),("👩‍🍳","to cook","tou kouk","cuisiner")]
D.append(dict(slug='30-mots-cuisine',date='2026-11-26',title="30 mots de la cuisine",sub="ustensiles, aliments et verbes",emoji='🍳',
 tip="Ce soir, en cuisinant, nomme en anglais chaque objet que tu touches : « knife, plate, onion… ». C'est la meilleure façon de les retenir !",
 p1=voct(cui[:24]),p2=voct(cui[24:])+'''<p class="mu">⚠️ Piège : <b>a cooker</b> = la cuisinière (l'appareil) · <b>a cook</b> = le cuisinier (la personne) !</p>
<h2>🍳 Une mini-recette : fried eggs</h2><div class="ex2">Put some <b>oil</b> in the <b>frying pan</b>. Break two <b>eggs</b>. Add <b>salt</b> and <b>pepper</b>. <b>Fry</b> for three minutes. Put the eggs on a <b>plate</b>. Enjoy! 😋</div>
<h2>✍️ Complète !</h2><p>1. I eat soup with a ______ (cuillère) · 2. Put the milk in the ______ (frigo) · 3. ______ the onions (couper) · 4. ______ the water (faire bouillir)</p><p class="mu">Réponses : spoon · fridge · cut · boil</p>'''))
mm1='''<h2>1️⃣ MANY : ce qu'on peut compter</h2><p>Avec un nom au <b>pluriel</b> : des choses qu'on peut compter (1, 2, 3…).</p>
<div class="ex2">How <b>many</b> brothers do you have? · I don't have <b>many</b> friends here. · There aren't <b>many</b> cars today.</div>
<h2>2️⃣ MUCH : ce qu'on ne peut pas compter</h2><p>Avec un nom <b>sans pluriel</b> : l'eau, l'argent, le temps…</p>
<div class="ex2">How <b>much</b> water do you drink? · I don't have <b>much</b> time. · How <b>much</b> is it? (= combien ça coûte ?)</div>
<h2>3️⃣ A LOT OF : marche avec les deux</h2><p>Dans les phrases <b>affirmatives</b>, on dit plutôt <b>a lot of</b>. <i>Much</i> et <i>many</i> s'utilisent surtout dans les <b>questions</b> et les phrases <b>négatives</b>.</p>
<div class="ex2">I have <b>a lot of</b> friends. · She drinks <b>a lot of</b> water.</div>
<p>🔊 <b>many</b> → mè-ni · <b>much</b> → meutch · <b>a lot of</b> → eu lot ov</p>
<h2>⚠️ Les pièges : ces mots ne se comptent pas en anglais</h2><table><tr><td><b>money</b> = argent</td><td><b>bread</b> = pain</td><td><b>information</b> = informations</td></tr><tr><td><b>advice</b> = conseils</td><td><b>homework</b> = devoirs</td><td><b>furniture</b> = meubles</td></tr></table><p class="mu">❌ How many money? → ✅ How much money?</p>'''
mm2='''<h2>✍️ À toi de jouer : much, many ou a lot of ?</h2><table>
<tr><td class="n">1</td><td>How ______ brothers do you have?</td></tr><tr><td class="n">2</td><td>How ______ is this phone?</td></tr>
<tr><td class="n">3</td><td>Sorry, I don't have ______ time today.</td></tr><tr><td class="n">4</td><td>How ______ water do you drink every day?</td></tr>
<tr><td class="n">5</td><td>She doesn't have ______ friends in London.</td></tr><tr><td class="n">6</td><td>We have ______ homework this week!</td></tr>
<tr><td class="n">7</td><td>How ______ eggs do we need for the cake?</td></tr><tr><td class="n">8</td><td>My father drinks ______ coffee.</td></tr></table>
<p class="mu">Réponses : 1. many · 2. much · 3. much · 4. much · 5. many · 6. a lot of · 7. many · 8. a lot of</p>
<h2>🎁 Bonus : a few / a little (un peu, quelques)</h2><div class="ex2"><b>a few</b> friends = quelques amis (on compte) · <b>a little</b> sugar = un peu de sucre (on ne compte pas)</div>
<p class="mu">🔊 a few → eu fyou · a little → eu li-teul</p>'''
D.append(dict(slug='much-many',date='2026-11-27',title="Much ou many ?",sub="la mini-leçon pour dire « beaucoup »",emoji='🔢',
 tip="Pose-toi une seule question : est-ce que je peux compter ? Oui → many · Non → much · Phrase affirmative → a lot of.",p1=mm1,p2=mm2))
dir1=[("Excuse me, where is the bank?","ex-kyouz mî, wèr iz zeu bènk ?","Excusez-moi, où est la banque ?"),
("How can I get to the station?","haou kèn aï guèt tou zeu stéï-cheun ?","Comment aller à la gare ?"),
("Is it far from here?","iz it fâr from hîr ?","C'est loin d'ici ?"),
("Is there a pharmacy near here?","iz zèr eu fâr-meu-si nîr hîr ?","Y a-t-il une pharmacie près d'ici ?"),
("Can you show me on the map?","kèn you cho mî on zeu mèp ?","Pouvez-vous me montrer sur le plan ?")]
dir2=[("Go straight on.","go stréït on","Allez tout droit."),
("Turn left. / Turn right.","teurn lèft / teurn raït","Tournez à gauche. / à droite."),
("Take the second street on the left.","téïk zeu sè-keund strît on zeu lèft","Prenez la 2ᵉ rue à gauche."),
("It's next to the supermarket.","its nèkst tou zeu sou-peur-mâr-kit","C'est à côté du supermarché."),
("It's opposite the church.","its o-peu-zit zeu tcheurtch","C'est en face de l'église."),
("It's between the bank and the hotel.","its bi-twîn zeu bènk ènd zeu ho-tèl","C'est entre la banque et l'hôtel."),
("It's on the corner.","its on zeu kor-neur","C'est au coin de la rue.")]
dir3=[("It's about five minutes on foot.","its eu-baout faïv mi-nits on fout","C'est à environ 5 minutes à pied."),
("You can't miss it!","you kânt miss it !","Vous ne pouvez pas le rater !"),
("Sorry, could you speak more slowly, please?","so-ri, koud you spîk mor slo-li, plîz ?","Pardon, pouvez-vous parler plus lentement ?")]
D.append(dict(slug='demander-son-chemin',date='2026-11-28',title="Demander son chemin",sub="15 phrases pour ne jamais te perdre",emoji='🗺️',
 tip="Apprends d'abord les 5 questions, puis entraîne-toi à comprendre les réponses : gauche, droite, tout droit, à côté de, en face de.",
 p1='<h2>❓ Pour demander</h2>'+table(dir1)+'<h2>➡️ Pour comprendre la réponse</h2>'+table(dir2,start=6),
 p2=table(dir3,start=13)+'''<h2>💬 Mini-dialogue à Londres</h2><div class="ex2">🧳 <b>Tourist:</b> Excuse me, how can I get to the post office?<br>🙋 <b>Man:</b> Go straight on and take the first street on the right. It's next to the bank.<br>🧳 <b>Tourist:</b> Is it far?<br>🙋 <b>Man:</b> No, about three minutes on foot.<br>🧳 <b>Tourist:</b> Thank you so much!</div>
<h2>✍️ Traduis en anglais</h2><p>1. Tournez à droite. · 2. C'est en face de la banque. · 3. C'est loin d'ici ?</p><p class="mu">Réponses : 1. Turn right. · 2. It's opposite the bank. · 3. Is it far from here?</p>'''))
qw=[("What?","wot","quoi ? quel ?","What is your name?"),("Where?","wèr","où ?","Where do you live?"),("When?","wèn","quand ?","When is your birthday?"),
("Who?","hou","qui ?","Who is your teacher?"),("Why?","waï","pourquoi ?","Why are you late? — Because… (bi-koz)"),("How?","haou","comment ?","How are you?"),
("Which?","witch","lequel ? quel ? (choix)","Which colour do you prefer, red or blue?"),("Whose?","houz","à qui ?","Whose bag is this?"),("How much / How many?","haou meutch / haou mè-ni","combien ?","How much is it? · How many children do you have?")]
def qwt(rows):
    h='<table>'
    for k,(w,pr,fr,ex) in enumerate(rows): h+=f'<tr><td class="n">{k+1}</td><td><b>{w}</b><span class="pr">🔊 {pr}</span></td><td class="fr">{fr}</td><td><span class="ex">{ex}</span></td></tr>'
    return h+'</table>'
qw2='''<h2>📌 Les questions avec HOW</h2><table><tr><td><b>How old…?</b> = quel âge</td><td><b>How long…?</b> = combien de temps</td></tr><tr><td><b>How far…?</b> = à quelle distance</td><td><b>How often…?</b> = à quelle fréquence</td></tr></table>'''
qw2b='''<h2>🔎 La structure à retenir</h2><div class="ex2">Mot interrogatif + <b>do / does / did</b> + sujet + verbe → Where <b>do</b> you work? · What <b>does</b> she want?<br>Avec le verbe <b>be</b> : on inverse simplement → Where <b>is</b> the bank? · How old <b>are</b> you?</div>
<table><tr><td><span class="bad">❌ Where you live?</span><span class="good">✅ Where do you live?</span></td><td><span class="bad">❌ What you want?</span><span class="good">✅ What do you want?</span></td></tr></table>'''
qw3='''<h2>✍️ À toi de jouer : trouve le bon mot</h2><table>
<tr><td class="n">1</td><td>______ is your name? — My name is Kevin.</td></tr><tr><td class="n">2</td><td>______ do you live? — In Manchester.</td></tr>
<tr><td class="n">3</td><td>______ are you? — I'm fine, thanks.</td></tr><tr><td class="n">4</td><td>______ is your birthday? — In May.</td></tr>
<tr><td class="n">5</td><td>______ is that man? — He's my uncle.</td></tr><tr><td class="n">6</td><td>______ are you sad? — Because I lost my phone.</td></tr>
<tr><td class="n">7</td><td>______ old are you? — I'm thirty.</td></tr><tr><td class="n">8</td><td>______ shoes are these? — They're Anna's.</td></tr></table>
<p class="mu">Réponses : 1. What · 2. Where · 3. How · 4. When · 5. Who · 6. Why · 7. How · 8. Whose</p>'''
D.append(dict(slug='mots-interrogatifs',date='2026-11-29',title="What, Where, When… ?",sub="les mots pour poser toutes tes questions",emoji='❓',
 tip="Une question en anglais commence presque toujours par l'un de ces mots. Apprends-les par cœur, puis pose 5 questions à un ami aujourd'hui !",
 p1=qwt(qw)+qw2,p2=qw2b+qw3))
days=[("Monday","meun-déï","lundi"),("Tuesday","tyouz-déï","mardi"),("Wednesday","wènz-déï","mercredi"),("Thursday","sseurz-déï","jeudi"),("Friday","fraï-déï","vendredi"),("Saturday","sè-teur-déï","samedi"),("Sunday","seun-déï","dimanche")]
months=[("January","djè-nyou-è-ri"),("February","fè-brou-è-ri"),("March","mârtch"),("April","éï-pril"),("May","méï"),("June","djoun"),("July","djou-laï"),("August","ô-geust"),("September","sèp-tèm-beur"),("October","ok-to-beur"),("November","no-vèm-beur"),("December","di-sèm-beur")]
dt1='<h2>📅 Les 7 jours</h2><table>'+''.join(f'<tr><td><b>{a}</b><span class="pr">🔊 {b}</span></td><td class="fr">{c}</td></tr>' for a,b,c in days)+'</table>'
dt1+='<h2>🗓️ Les 12 mois</h2><table>'+''.join('<tr>'+''.join(f'<td><b>{a}</b><span class="pr">🔊 {b}</span></td>' for a,b in months[i:i+3])+'</tr>' for i in range(0,12,3))+'</table>'
dt1+='<p class="mu">⚠️ En anglais, les jours et les mois prennent <b>toujours une majuscule</b> : Monday, December.</p>'
dt2='''<h2>🥇 Les nombres ordinaux (1er, 2e, 3e…)</h2><table>
<tr><td><b>1st</b> first <span class="pr">🔊 feurst</span></td><td><b>2nd</b> second <span class="pr">🔊 sè-keund</span></td><td><b>3rd</b> third <span class="pr">🔊 sseurd</span></td><td><b>4th</b> fourth <span class="pr">🔊 forss</span></td></tr>
<tr><td><b>5th</b> fifth <span class="pr">🔊 fifs</span></td><td><b>12th</b> twelfth <span class="pr">🔊 twèlfs</span></td><td><b>20th</b> twentieth <span class="pr">🔊 twèn-ti-eus</span></td><td><b>31st</b> thirty-first <span class="pr">🔊 sseur-ti feurst</span></td></tr></table>
<p>Règle : on ajoute <b>-th</b>, sauf pour <b>1st, 2nd, 3rd</b> (et 21st, 22nd, 23rd, 31st).</p>
<h2>🗣️ Dire la date</h2><div class="ex2">✍️ On écrit : <b>1st December</b> ou <b>December 1st</b><br>🗣️ On dit : « <b>the first of December</b> » 🔊 zeu feurst ov di-sèm-beur</div>
<p><b>What's the date today?</b> (wots zeu déït tou-déï ?) — It's the first of December.<br><b>When is your birthday?</b> — It's on the fourteenth of July.</p>
<p>Prépositions : <b>on</b> Monday · <b>on</b> 1st December · <b>in</b> December · <b>in</b> 2026 (twèn-ti twèn-ti siks)</p>
<h2>✍️ Écris ces dates en toutes lettres</h2><p>1. 3/12 · 2. 22/05 · 3. 31/10</p><p class="mu">Réponses : 1. the third of December · 2. the twenty-second of May · 3. the thirty-first of October</p>'''
D.append(dict(slug='dire-la-date',date='2026-11-30',title="Dire la date",sub="jours, mois et nombres ordinaux",emoji='📅',
 tip="Chaque matin, dis la date du jour à voix haute en anglais : « Today is Monday, the first of December ». En une semaine, c'est acquis !",p1=dt1,p2=dt2))
pol=[("Give me water.","Could I have some water, please?","« Could I have… ? » = pourrais-je avoir… ? 🔊 koud aï hèv"),
("I want a coffee.","I'd like a coffee, please.","« I'd like » = je voudrais : bien plus poli que « I want ». 🔊 aïd laïk"),
("Close the door.","Could you close the door, please?","« Could you… ? » transforme un ordre en demande polie."),
("What?","Sorry? / Pardon?","« What? » tout seul paraît impoli. 🔊 so-ri ? / pâr-deun ?"),
("Repeat!","Sorry, could you repeat that, please?","🔊 so-ri, koud you ri-pît zèt, plîz ?"),
("Move!","Excuse me, can I get past?","Pour passer devant quelqu'un. 🔊 ex-kyouz mî, kèn aï guèt pâst ?"),
("Wait.","Just a moment, please.","🔊 djeust eu mo-meunt, plîz"),
("You are wrong.","I'm not sure I agree.","Pour contredire en douceur. 🔊 aïm not chour aï eu-grî"),
("Help me.","Would you mind helping me?","« Would you mind + -ing ? » = ça vous dérangerait de… ? 🔊 woud you maïnd"),
("No.","No, thank you.","Toujours « thank you » après un refus. 🔊 no, ssènk you"),
("I need the bill.","Could we have the bill, please?","🔊 koud wî hèv zeu bil, plîz ?"),
("Bye.","Thanks for your help. Have a nice day!","🔊 ssènks for yor hèlp. hèv eu naïss déï !")]
def polt(rows,s):
    h='<table class="err">'
    for k,(w,r,e) in enumerate(rows): h+=f'<tr><td class="n">{s+k}</td><td><span class="bad" style="text-decoration:none">😬 Trop direct : {w}</span><span class="good">✅ {r}</span><span class="ex">{e}</span></td></tr>'
    return h+'</table>'
D.append(dict(slug='etre-poli-anglais',date='2026-12-01',title="Être poli en anglais",sub="12 phrases trop directes… et la version polie",emoji='🎩',
 tip="En anglais, « please », « could you » et « sorry » sont partout. Une phrase correcte mais trop directe peut paraître impolie : voici comment l'adoucir.",
 p1=polt(pol[:6],1),p2=polt(pol[6:],7)+'<h2>💡 Sorry ou Excuse me ?</h2><div class="ex2"><b>Excuse me</b> = <i>avant</i> de déranger quelqu\'un (pour attirer l\'attention, pour passer).<br><b>Sorry</b> = <i>après</i>, pour s\'excuser (tu as bousculé quelqu\'un, tu es en retard).</div>'))
# ---- Semaine du 2 au 8 décembre 2026 ----
sa1='''<h2>1️⃣ SOME : dans les phrases affirmatives</h2><p><b>Some</b> = « du, de la, des, quelques ». On l'utilise quand on <b>affirme</b> quelque chose.</p>
<div class="ex2">I have <b>some</b> money. · There is <b>some</b> milk in the fridge. · She bought <b>some</b> apples.</div>
<h2>2️⃣ ANY : dans les questions et les négations</h2><p><b>Any</b> = « du, des » dans une <b>question</b>, et « pas de, aucun » dans une phrase <b>négative</b>.</p>
<div class="ex2">Do you have <b>any</b> questions? · There isn't <b>any</b> sugar. · I don't have <b>any</b> brothers.</div>
<h2>3️⃣ L'exception à connaître : offrir et demander poliment</h2><p>Quand on <b>propose</b> ou qu'on <b>demande</b> quelque chose poliment, on garde <b>some</b>, même dans une question.</p>
<div class="ex2">Would you like <b>some</b> tea? (proposer) · Could I have <b>some</b> water, please? (demander)</div>
<p>🔊 <b>some</b> → seum · <b>any</b> → è-ni · <b>Would you like</b> → woud you laïk</p>
<h2>🧩 Les mots de la même famille</h2><table>
<tr><td><b>something</b> <span class="pr">🔊 seum-ssing</span><span class="fr2">quelque chose</span></td><td><b>anything</b> <span class="pr">🔊 è-ni-ssing</span><span class="fr2">quelque chose (?) / rien (–)</span></td></tr>
<tr><td><b>someone</b> <span class="pr">🔊 seum-weun</span><span class="fr2">quelqu'un</span></td><td><b>anyone</b> <span class="pr">🔊 è-ni-weun</span><span class="fr2">quelqu'un (?) / personne (–)</span></td></tr>
<tr><td><b>somewhere</b> <span class="pr">🔊 seum-wèr</span><span class="fr2">quelque part</span></td><td><b>anywhere</b> <span class="pr">🔊 è-ni-wèr</span><span class="fr2">quelque part (?) / nulle part (–)</span></td></tr></table>'''
sa2='''<h2>🔎 Exemples avec la famille SOME / ANY</h2><div class="ex2">I want to eat <b>something</b>. · Is there <b>anything</b> to eat? · I didn't see <b>anyone</b>.<br><b>Someone</b> is at the door! · Let's go <b>somewhere</b> nice. · I can't find my keys <b>anywhere</b>.</div>
<h2>✍️ À toi de jouer : some ou any ?</h2><table>
<tr><td class="n">1</td><td>There is ______ bread on the table.</td></tr><tr><td class="n">2</td><td>Do you have ______ children?</td></tr>
<tr><td class="n">3</td><td>We don't have ______ milk left.</td></tr><tr><td class="n">4</td><td>Would you like ______ coffee?</td></tr>
<tr><td class="n">5</td><td>I bought ______ new shoes yesterday.</td></tr><tr><td class="n">6</td><td>Is there ______ problem?</td></tr>
<tr><td class="n">7</td><td>Could I have ______ water, please?</td></tr><tr><td class="n">8</td><td>She didn't say ______thing.</td></tr></table>
<p class="mu">Réponses : 1. some · 2. any · 3. any · 4. some · 5. some · 6. any · 7. some · 8. anything</p>'''
D.append(dict(slug='some-any',date='2026-12-02',title="Some ou any ?",sub="la mini-leçon pour dire « du, des, quelques »",emoji='🧺',
 tip="La règle de base : phrase affirmative → some · question ou négation → any. Et pour proposer ou demander poliment → some !",p1=sa1,p2=sa2))
hot=[("Receptionist","Good evening. Welcome to the Grand Hotel.","goud îv-ning. wèl-keum tou zeu grènd ho-tèl","Bonsoir. Bienvenue au Grand Hotel."),
("Mark","Hello. I have a reservation. My name is Mark Taylor.","hè-lo. aï hèv eu rè-zeur-véï-cheun. maï néïm iz mârk téï-leur","Bonjour. J'ai une réservation. Je m'appelle Mark Taylor."),
("Receptionist","Yes, Mr Taylor. A single room for three nights?","yèss, miss-teur téï-leur. eu sin-gueul roum for ssrî naïts ?","Oui, M. Taylor. Une chambre simple pour trois nuits ?"),
("Mark","That's right.","zèts raït","C'est exact."),
("Receptionist","Can I see your passport, please?","kèn aï sî yor pâss-port, plîz ?","Puis-je voir votre passeport ?"),
("Mark","Here you are. Is breakfast included?","hîr you âr. iz brèk-feust in-klou-did ?","Le voici. Le petit-déjeuner est-il compris ?"),
("Receptionist","Yes, from 7 to 10 a.m., on the first floor.","yèss, from sè-veun tou tèn éï-èm, on zeu feurst flor","Oui, de 7 h à 10 h, au premier étage."),
("Mark","What's the Wi-Fi password?","wots zeu waï-faï pâss-weurd ?","Quel est le mot de passe du Wi-Fi ?"),
("Receptionist","It's on this card. Here is your key. Room 214.","its on ziss kârd. hîr iz yor kî. roum tou weun for","Il est sur cette carte. Voici votre clé. Chambre 214."),
("Mark","Thank you. What time is check-out?","ssènk you. wot taïm iz tchèk-aout ?","Merci. À quelle heure faut-il libérer la chambre ?"),
("Receptionist","At 11 a.m. Enjoy your stay!","èt i-lè-veun éï-èm. in-djoï yor stéï !","À 11 h. Bon séjour !")]
D.append(dict(slug='dialogue-hotel',date='2026-12-03',title="À l'hôtel",sub="un dialogue complet, avec la prononciation",emoji='🏨',
 tip="Lis le dialogue à deux : une personne fait Mark, l'autre fait la réceptionniste. Puis échangez les rôles et changez le nombre de nuits !",
 p1=diat(hot[:6]),p2=diat(hot[6:])+'<h2>📌 Les mots à retenir</h2><table><tr><td><b>a reservation / a booking</b> = une réservation</td><td><b>a single / double room</b> = chambre simple / double</td></tr><tr><td><b>check-in / check-out</b> = arrivée / départ</td><td><b>the key</b> (kî) = la clé</td></tr><tr><td><b>breakfast included</b> = petit-déj. compris</td><td><b>the lift</b> (lift) = l\'ascenseur</td></tr><tr><td><b>a towel</b> (taou-eul) = une serviette</td><td><b>The air conditioning doesn\'t work.</b> = La clim ne marche pas.</td></tr></table>'))
st1=[("Hi! How's it going?","haï ! haouz it go-ing ?","Salut ! Comment ça va ?"),
("Nice to meet you.","naïss tou mît you","Ravi(e) de te rencontrer."),
("What do you do?","wot dou you dou ?","Qu'est-ce que tu fais dans la vie ?"),
("Where are you from?","wèr âr you from ?","D'où viens-tu ?"),
("How do you know Tom?","haou dou you no tom ?","Comment connais-tu Tom ?"),
("Lovely weather today, isn't it?","leuv-li wè-zeur tou-déï, i-zeunt it ?","Il fait beau aujourd'hui, non ?"),
("What do you do in your free time?","wot dou you dou in yor frî taïm ?","Que fais-tu pendant ton temps libre ?"),
("Did you have a good weekend?","did you hèv eu goud wîk-ènd ?","Tu as passé un bon week-end ?")]
st2=[("Really? That's interesting!","rî-li ? zèts in-trèss-ting !","Vraiment ? C'est intéressant !"),
("Me too! / Me neither.","mî tou ! / mî naï-zeur","Moi aussi ! / Moi non plus."),
("Oh, I see.","o, aï sî","Ah, je vois."),
("It was nice talking to you.","it woz naïss tô-king tou you","C'était sympa de parler avec toi."),
("Let's keep in touch!","lèts kîp in teutch !","Restons en contact !"),
("See you around!","sî you eu-raound !","À un de ces jours !")]
D.append(dict(slug='small-talk',date='2026-12-04',title="Le small talk",sub="14 phrases pour lancer une conversation",emoji='☕',
 tip="Le « small talk », c'est la petite conversation légère : au travail, à une fête, dans une file d'attente. Les anglophones adorent ça !",
 p1='<h2>🚀 Pour lancer la conversation</h2>'+table(st1)+'<h2>👂 Pour réagir et garder le fil</h2>'+table(st2[:3],start=9),
 p2='<h2>👋 Pour terminer poliment</h2>'+table(st2[3:],start=12)+'''<h2>💬 Mini-dialogue à une fête</h2><div class="ex2">🙋‍♀️ <b>Lucy:</b> Hi! I'm Lucy. Nice to meet you.<br>🙋 <b>Ben:</b> Nice to meet you too. I'm Ben. How do you know Tom?<br>🙋‍♀️ <b>Lucy:</b> We work together. What do you do, Ben?<br>🙋 <b>Ben:</b> I'm a nurse. And I love football.<br>🙋‍♀️ <b>Lucy:</b> Really? Me too! Let's keep in touch!</div>
<h2>⚠️ Les sujets à éviter</h2><p>En small talk, on évite l'argent (salaire), la religion et la politique. On préfère : le travail, la météo, le week-end, les loisirs, le sport.</p>
<h2>✍️ Traduis en anglais</h2><p>1. D'où viens-tu ? · 2. Moi aussi ! · 3. C'était sympa de parler avec toi.</p><p class="mu">Réponses : 1. Where are you from? · 2. Me too! · 3. It was nice talking to you.</p>'''))
mai=[("🏠","house","haouss","maison"),("🏢","flat","flèt","appartement"),("🛋️","living room","li-ving roum","salon"),("🛏️","bedroom","bèd-roum","chambre"),("🛁","bathroom","bâss-roum","salle de bain"),("🍳","kitchen","kit-cheun","cuisine"),("🚽","toilet","toï-lit","toilettes"),("🚪","door","dor","porte"),("🪟","window","win-do","fenêtre"),("🧱","wall","wôl","mur"),("🪜","stairs","stèrz","escalier"),("🌳","garden","gâr-deun","jardin"),
("🛋️","sofa","so-feu","canapé"),("🪑","chair","tchèr","chaise"),("🍽️","table","téï-beul","table"),("🛏️","bed","bèd","lit"),("🚿","shower","chaou-eur","douche"),("👔","wardrobe","wor-drob","armoire"),("📺","TV","tî-vî","télé"),("💡","lamp","lèmp","lampe"),("🪞","mirror","mi-reur","miroir"),("🖼️","picture","pik-tcheur","tableau / photo"),("🔑","key","kî","clé"),("❄️","air conditioner","èr keun-di-cheu-neur","climatiseur"),
("🧹","to clean","tou klîn","nettoyer"),("🧺","to tidy up","tou taï-di eup","ranger"),("👕","to do the laundry","tou dou zeu lôn-dri","faire la lessive"),("🛏️","to make the bed","tou méïk zeu bèd","faire le lit"),("🍽️","to do the dishes","tou dou zeu di-chiz","faire la vaisselle"),("😴","to go to bed","tou go tou bèd","aller se coucher")]
D.append(dict(slug='30-mots-maison',date='2026-12-05',title="30 mots de la maison",sub="pièces, meubles et tâches ménagères",emoji='🏠',
 tip="Fais le tour de ta maison et nomme chaque pièce et chaque objet en anglais. Tu peux même coller des petits papiers dessus !",
 p1=voct(mai[:24]),p2=voct(mai[24:])+'''<p class="mu">⚠️ Piège : <b>a flat</b> (UK) = <b>an apartment</b> (US) · <b>the toilet</b> (UK) = <b>the bathroom / restroom</b> (US)</p>
<h2>🏠 Décris ta maison</h2><div class="ex2">I live in a small <b>flat</b>. There are two <b>bedrooms</b>, a <b>living room</b>, a <b>kitchen</b> and a <b>bathroom</b>. My favourite room is the <b>living room</b> because there is a big <b>sofa</b>. 😊</div>
<p>🔊 <b>There is</b> (zèr iz) = il y a (1 chose) · <b>There are</b> (zèr âr) = il y a (plusieurs)</p>
<h2>✍️ Complète !</h2><p>1. I sleep in my ______ (chambre) · 2. Can you ______ (faire la vaisselle)? · 3. Close the ______ (fenêtre), please. · 4. I take a ______ (douche) every morning.</p><p class="mu">Réponses : bedroom · do the dishes · window · shower</p>'''))
qv=[("« Je suis d'accord » :","I am agree","I agree","I'm agreeing","B"),
("« Un conseil » :","an advice","some advices","a piece of advice","C"),
("« Actually » veut dire :","en réalité","actuellement","activement","A"),
("« Une librairie » :","a library","a bookshop","a bookstore and library","B"),
("« Je me suis levé tôt » :","I woke up early","I woked up early","I wake up early","A"),
("« Je fais une erreur » :","I do a mistake","I make a mistake","I have a mistake","B"),
("« J'ai faim » :","I have hunger","I am hungry","I have hungry","B"),
("« Elle a 30 ans » :","She has 30 years","She is 30","She have 30","B"),
("« Sensible » en anglais veut dire :","raisonnable","sensible","sensuel","A"),
("« Assister à une réunion » :","to assist a meeting","to attend a meeting","to watch a meeting","B"),
("« Je suis ici depuis 2 ans » :","I am here since 2 years","I have been here for 2 years","I am here for 2 years","B"),
("« Combien d'argent ? » :","How many money?","How much money?","How lot money?","B"),
("« Il ne travaille pas » :","He don't work","He doesn't works","He doesn't work","C"),
("« Je vais à la maison » :","I go to the home","I'm going home","I'm going to home","B"),
("« Explique-moi » :","Explain me","Explain to me","Explain it me","B")]
qva=' · '.join(f'{i+1}. {r[4]}' for i,r in enumerate(qv))
D.append(dict(slug='quiz-pieges',date='2026-12-06',title="Quiz : les 15 pièges",sub="évites-tu les erreurs des francophones ?",emoji='🧠',
 tip="Pour chaque question, choisis A, B ou C sans regarder les réponses. Compte tes points à la fin, puis relis les explications.",
 p1=quizt(qv[:9],1),p2=quizt(qv[9:],10)+f'''<p class="mu">Réponses : {qva}</p><h2>📊 Ton résultat</h2><table><tr><td><b>0 à 6</b></td><td class="fr">Les pièges du français te jouent des tours : c'est normal, on corrige ça ensemble 💪</td></tr><tr><td><b>7 à 11</b></td><td class="fr">Pas mal ! Encore quelques réflexes à prendre 🔥</td></tr><tr><td><b>12 à 15</b></td><td class="fr">Excellent ! Tu penses déjà en anglais 🏆</td></tr></table>
<h2>💡 Les 3 règles à retenir</h2><div class="ex2">1. On <b>est</b> son âge et sa faim : <i>I am 30 · I am hungry</i>.<br>2. <b>Advice, money, information</b> : pas de pluriel.<br>3. Avec <b>he / she / it</b> : <i>doesn't</i> + verbe sans -s.</div>'''))
rv=[("to wake up","tou wéïk eup","se réveiller","I wake up at 6."),("to get up","tou guèt eup","se lever","I get up at 6:15."),("to take a shower","tou téïk eu chaou-eur","prendre une douche","I take a shower."),("to get dressed","tou guèt drèst","s'habiller","I get dressed quickly."),("to brush my teeth","tou breuch maï tîss","me brosser les dents","I brush my teeth."),("to have breakfast","tou hèv brèk-feust","prendre le petit-déjeuner","I have breakfast at 7."),("to leave home","tou lîv hom","partir de chez moi","I leave home at 7:30."),("to take the bus","tou téïk zeu beuss","prendre le bus","I take the bus to work."),("to start work","tou stârt weurk","commencer le travail","I start work at 8."),("to have lunch","tou hèv leunch","déjeuner","I have lunch at 12:30."),
("to finish work","tou fi-nich weurk","finir le travail","I finish work at 5."),("to come back home","tou keum bèk hom","rentrer à la maison","I come back home at 6."),("to cook dinner","tou kouk di-neur","préparer le dîner","I cook dinner."),("to have dinner","tou hèv di-neur","dîner","We have dinner at 8."),("to watch TV","tou wotch tî-vî","regarder la télé","I watch TV."),("to relax","tou ri-lèks","se détendre","I relax on the sofa."),("to check my phone","tou tchèk maï fon","regarder mon téléphone","I check my phone."),("to read","tou rîd","lire","I read a book."),("to go to bed","tou go tou bèd","aller se coucher","I go to bed at 10."),("to fall asleep","tou fôl eu-slîp","s'endormir","I fall asleep quickly.")]
D.append(dict(slug='routine-20-verbes',date='2026-12-07',title="Ma journée en anglais",sub="20 verbes pour raconter ta routine",emoji='⏰',
 tip="Raconte ta journée à voix haute, du réveil au coucher, avec ces 20 verbes. Et n'oublie pas : avec he / she, on ajoute un -s (she wakes up) !",
 p1=pvt(rv[:11],1),p2=pvt(rv[11:],12)+'''<h2>🗣️ Les mots pour enchaîner</h2><p><b>First</b> (feurst) = d'abord · <b>Then</b> (zèn) = ensuite · <b>After that</b> (âf-teur zèt) = après ça · <b>Finally</b> (faï-neu-li) = enfin</p>
<div class="ex2"><b>First</b>, I wake up at 6. <b>Then</b>, I take a shower and I have breakfast. <b>After that</b>, I take the bus to work. <b>Finally</b>, I go to bed at 10.</div>
<h2>✍️ À toi !</h2><p>Raconte la journée de ta sœur ou de ton frère (attention au -s) : <i>She wakes up at…</i></p>'''))
ms=[("Arriver en retard","Hi Tom, sorry, I'm running 10 minutes late. I'll be there soon.","Salut Tom, désolé, j'ai 10 minutes de retard. J'arrive bientôt."),
("Annuler un rendez-vous","Hello Ms Brown, I'm afraid I have to cancel our meeting tomorrow. I'm very sorry.","Bonjour Mme Brown, je crains de devoir annuler notre réunion de demain. Je suis vraiment désolé(e)."),
("Reporter","Could we move our meeting to Friday at 3 p.m.? Would that work for you?","Pourrait-on déplacer notre réunion à vendredi 15 h ? Cela vous conviendrait-il ?"),
("Confirmer","Hi Anna, just to confirm: we're meeting on Monday at 10 a.m. See you then!","Salut Anna, juste pour confirmer : on se voit lundi à 10 h. À lundi !"),
("Relancer","Hi James, just following up on my last email. Any news?","Salut James, je reviens vers toi au sujet de mon dernier email. Des nouvelles ?"),
("Remercier","Thank you so much for your help today. I really appreciate it.","Merci beaucoup pour ton aide aujourd'hui. Je l'apprécie vraiment."),
("Demander un service","Could you send me the file when you have a moment? Thanks!","Pourrais-tu m'envoyer le fichier quand tu as un moment ? Merci !"),
("Être absent","Hi Sarah, I'm sick today, so I won't come to the office. I'll check my emails.","Salut Sarah, je suis malade aujourd'hui, je ne viendrai pas au bureau. Je regarderai mes emails."),
("Répondre plus tard","Got your message, thanks! I'll get back to you this afternoon.","Bien reçu ton message, merci ! Je te réponds cet après-midi.")]
def mst(rows,s):
    h='<table>'
    for k,(sit,en,fr) in enumerate(rows): h+=f'<tr><td class="n">{s+k}</td><td><span class="pr" style="font-weight:800">{sit}</span><b>{en}</b><span class="fr2">{fr}</span></td></tr>'
    return h+'</table>'
D.append(dict(slug='messages-courts-pro',date='2026-12-08',title="9 messages pros",sub="s'excuser, annuler, relancer… les modèles à copier",emoji='💬',
 tip="Au travail, on écrit beaucoup de petits messages rapides. Copie ces modèles, change juste le nom et l'heure, et c'est envoyé !",
 p1=mst(ms[:5],1),p2=mst(ms[5:],6)+'''<h2>🔊 Les expressions clés à prononcer</h2><table>
<tr><td><b>I'm running late</b><span class="pr">🔊 aïm reu-ning léït</span><span class="fr2">je suis en retard</span></td><td><b>I'm afraid…</b><span class="pr">🔊 aïm eu-fréïd</span><span class="fr2">je crains que… (poli)</span></td></tr>
<tr><td><b>Just following up</b><span class="pr">🔊 djeust fo-lo-ing eup</span><span class="fr2">je reviens vers toi</span></td><td><b>I'll get back to you</b><span class="pr">🔊 aïl guèt bèk tou you</span><span class="fr2">je te recontacte</span></td></tr></table>
<h2>✍️ À toi !</h2><p>Écris un message à ton collègue Mike pour lui dire que tu as 15 minutes de retard.</p><p class="mu">Exemple : Hi Mike, sorry, I'm running 15 minutes late. I'll be there soon.</p>'''))
