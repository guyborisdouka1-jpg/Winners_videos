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
