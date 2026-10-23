/* =====================================================================
   WINNERS' ENGLISH CENTER — CONTENU PÉDAGOGIQUE
   Prononciation écrite « à la française » entre crochets.
   La syllabe en MAJUSCULES est celle qu'on appuie.
   ===================================================================== */

window.NIVEAUX = [
  { id: "debutant", nom: "Débutant", sous: "A1 • Les bases", emoji: "🌱" },
  { id: "intermediaire", nom: "Intermédiaire", sous: "A2-B1 • Je me débrouille", emoji: "🚀" },
  { id: "avance", nom: "Avancé", sous: "B1-B2 • Je veux être fluide", emoji: "🏆" }
];

window.LECONS = [
  /* ----------------------------- DÉBUTANT ----------------------------- */
  {
    id: "d1", niveau: "debutant", emoji: "👋", titre: "Saluer et se présenter",
    intro: "Les premières phrases à connaître pour commencer une conversation, au bureau, au restaurant ou en voyage.",
    points: [
      ["Hello! / Hi!", "Bonjour ! / Salut !", "hè-LO-ou / HAÏ"],
      ["Good morning", "Bonjour (le matin)", "goud MOR-ning"],
      ["Good evening", "Bonsoir", "goud I-ve-ning"],
      ["How are you?", "Comment vas-tu ?", "hao AR iou"],
      ["I'm fine, thank you. And you?", "Je vais bien, merci. Et toi ?", "aïm FAÏN, SÈNK-iou. ènd IOU"],
      ["My name is Emma.", "Je m'appelle Emma.", "maï NÈÏM iz A-ya"],
      ["Nice to meet you!", "Enchanté(e) !", "naïs tou MIT iou"],
      ["Goodbye! See you later!", "Au revoir ! À plus tard !", "goud-BAÏ. SI iou LÈÏ-teur"]
    ],
    astuce: "« Good night » ne veut pas dire bonsoir : on le dit seulement pour aller dormir ou en partant tard le soir. Pour dire bonsoir en arrivant : « Good evening ».",
    quiz: [
      ["Il est 19 h, tu arrives à une réunion. Tu dis…", ["Good night", "Good evening", "Good morning"], 1, "On dit « Good evening » en arrivant le soir. « Good night » sert à se quitter ou à aller dormir."],
      ["Quelqu'un te dit « How are you? ». Tu réponds…", ["I'm fine, thank you.", "I'm 25.", "My name is Emma."], 0, "« How are you? » = Comment vas-tu ? On répond « I'm fine, thank you »."],
      ["« Nice to meet you » veut dire…", ["À bientôt", "Enchanté(e)", "Bonne nuit"], 1, "On le dit quand on rencontre quelqu'un pour la première fois."],
      ["Complète : « My ___ is Jack. »", ["call", "name", "am"], 1, "« My name is… » = Je m'appelle…"]
    ]
  },
  {
    id: "d2", niveau: "debutant", emoji: "🧱", titre: "Le verbe « to be » (être)",
    intro: "Le verbe le plus important de l'anglais. Il sert à dire qui tu es, comment tu vas, où tu es… et même ton âge !",
    points: [
      ["I am (I'm)", "Je suis", "aï AM / AÏM"],
      ["You are (you're)", "Tu es / Vous êtes", "iou AR / IOR"],
      ["He is / She is / It is", "Il est / Elle est / C'est", "hi IZ / chi IZ / it IZ"],
      ["We are / They are", "Nous sommes / Ils sont", "oui AR / dzèï AR"],
      ["I'm not tired.", "Je ne suis pas fatigué(e).", "aïm NOT TAÏ-eurd"],
      ["Are you ready?", "Es-tu prêt(e) ?", "ar iou RÈ-di"],
      ["I am 25 (years old).", "J'ai 25 ans.", "aï am TOUÈN-ti FAÏV"],
      ["I'm hungry. / I'm cold.", "J'ai faim. / J'ai froid.", "aïm HEUN-gri / aïm KO-old"]
    ],
    astuce: "Piège classique : en anglais on n'« a » pas son âge, on l'« est ». On dit « I am 25 », jamais « I have 25 years ». Pareil pour la faim, la soif, le froid : I'm hungry, I'm thirsty, I'm cold.",
    quiz: [
      ["Comment dit-on « J'ai 30 ans » ?", ["I have 30 years.", "I am 30.", "I have 30."], 1, "Avec l'âge, on utilise « to be » : I am 30."],
      ["Complète : « They ___ my friends. »", ["is", "am", "are"], 2, "They → are."],
      ["Complète : « She ___ a teacher. »", ["is", "are", "be"], 0, "He / She / It → is."],
      ["« J'ai faim » se dit…", ["I have hungry.", "I'm hungry.", "I hungry."], 1, "On dit « I'm hungry » (je suis affamé)."]
    ]
  },
  {
    id: "d3", niveau: "debutant", emoji: "🔢", titre: "Les nombres et l'argent",
    intro: "Indispensable pour donner son numéro, demander un prix ou parler d'une date.",
    points: [
      ["one, two, three, four, five", "1, 2, 3, 4, 5", "ouann, tou, sri, for, faïv"],
      ["six, seven, eight, nine, ten", "6, 7, 8, 9, 10", "siks, SÈ-ven, èït, naïn, tèn"],
      ["thirteen / thirty", "13 / 30", "seur-TINE / SEUR-ti"],
      ["a hundred / a thousand", "100 / 1 000", "e HEUN-dred / e SAO-zend"],
      ["How much is it?", "C'est combien ?", "hao MEUTCH iz it"],
      ["It's five dollars.", "Ça fait 5 dollars.", "its faïv DO-leuz"],
      ["What's your phone number?", "Quel est ton numéro ?", "ouats ior FO-oun NEUM-beur"],
      ["It's too expensive!", "C'est trop cher !", "its tou iks-PÈN-siv"]
    ],
    astuce: "Écoute bien la syllabe appuyée : thirTEEN (13) se dit avec la fin forte et longue, THIRty (30) avec le début fort. C'est comme ça que les Anglais font la différence.",
    quiz: [
      ["« How much is it? » veut dire…", ["Combien en veux-tu ?", "C'est combien ?", "Il y en a combien ?"], 1, "« How much » sert à demander un prix."],
      ["Comment écrit-on 15 ?", ["fiveteen", "fifteen", "fifty"], 1, "15 = fifteen. 50 = fifty."],
      ["« C'est trop cher ! » se dit…", ["It's too expensive!", "It's very cheap!", "It's too much money!"], 0, "Expensive = cher. Cheap = pas cher."],
      ["1 000 se dit…", ["a hundred", "a thousand", "a million"], 1, "100 = a hundred, 1 000 = a thousand."]
    ]
  },
  {
    id: "d4", niveau: "debutant", emoji: "❓", titre: "Poser des questions",
    intro: "Les mots en « WH » pour poser toutes les questions du quotidien.",
    points: [
      ["What?", "Quoi ? / Quel ?", "OUAT"],
      ["Where?", "Où ?", "OUÈR"],
      ["When?", "Quand ?", "OUÈN"],
      ["Who?", "Qui ?", "HOU"],
      ["Why? — Because…", "Pourquoi ? — Parce que…", "OUAÏ — bi-KOZ"],
      ["How?", "Comment ?", "HAO"],
      ["Where do you live?", "Où habites-tu ?", "ouèr dou iou LIV"],
      ["What time is it?", "Quelle heure est-il ?", "ouat TAÏM iz it"]
    ],
    astuce: "Pour une question avec un verbe d'action, on ajoute « do » (ou « does » avec he/she) : « Where do you work? », « What does she want? ».",
    quiz: [
      ["« Où travailles-tu ? »", ["Where you work?", "Where do you work?", "Where are you work?"], 1, "Question avec un verbe d'action → do : Where do you work?"],
      ["« Why » veut dire…", ["Qui", "Pourquoi", "Quand"], 1, "Why = pourquoi ; la réponse commence souvent par « Because »."],
      ["Pour demander l'heure, on dit…", ["What hour is it?", "What time is it?", "How time is it?"], 1, "On dit « What time is it? »."],
      ["Complète : « ___ is your brother? » (Qui est ton frère ?)", ["What", "Who", "Where"], 1, "Who = qui (une personne)."]
    ]
  },

  /* --------------------------- INTERMÉDIAIRE -------------------------- */
  {
    id: "i1", niveau: "intermediaire", emoji: "⏱️", titre: "Présent simple ou présent en -ing ?",
    intro: "En anglais il y a deux présents : un pour les habitudes, un pour ce qui se passe maintenant.",
    points: [
      ["I work every day.", "Je travaille tous les jours. (habitude)", "aï OUEURK È-vri dèï"],
      ["I'm working now.", "Je suis en train de travailler. (maintenant)", "aïm OUEUR-king NAO"],
      ["She goes to church on Sunday.", "Elle va à l'église le dimanche.", "chi GO-OUZ tou TCHEURTCH on SEUN-dèï"],
      ["Look! It's raining.", "Regarde ! Il pleut.", "louk. its RÈÏ-ning"],
      ["He doesn't eat meat.", "Il ne mange pas de viande.", "hi DEU-zent it MIT"],
      ["What are you doing?", "Qu'est-ce que tu fais (là) ?", "ouat ar iou DOU-ing"]
    ],
    astuce: "Au présent simple, n'oublie jamais le « s » avec he / she / it : She works, He lives, It costs.",
    quiz: [
      ["« Elle habite à London. »", ["She live in London.", "She lives in London.", "She is live in London."], 1, "Habitude/fait permanent + she → lives."],
      ["Ton ami t'appelle et tu es en train de manger. Tu dis…", ["I eat.", "I'm eating.", "I eating."], 1, "Action en cours → be + -ing : I'm eating."],
      ["« Il ne parle pas anglais. »", ["He doesn't speak English.", "He don't speak English.", "He not speak English."], 0, "Avec he/she/it : doesn't + verbe."],
      ["Complète : « Every morning, I ___ coffee. »", ["drink", "am drinking", "drinks"], 0, "Every morning = habitude → présent simple."]
    ]
  },
  {
    id: "i2", niveau: "intermediaire", emoji: "⏪", titre: "Raconter au passé",
    intro: "Pour raconter ce que tu as fait hier, le week-end dernier ou l'année passée.",
    points: [
      ["I worked yesterday.", "J'ai travaillé hier.", "aï OUEURKT IÈS-teur-dèï"],
      ["We visited Grand-Bassam.", "Nous avons visité Grand-Bassam.", "oui VI-zi-tid"],
      ["I went to the market.", "Je suis allé(e) au marché.", "aï OUÈNT tou dze MAR-kit"],
      ["She bought a new phone.", "Elle a acheté un nouveau téléphone.", "chi BOT e niou FO-oun"],
      ["Did you see the match?", "Tu as vu le match ?", "did iou SI dze MATCH"],
      ["I didn't sleep well.", "Je n'ai pas bien dormi.", "aï DI-dent slip OUÈL"]
    ],
    astuce: "Verbes réguliers : on ajoute -ed (work → worked). Les irréguliers s'apprennent par cœur : go → went, buy → bought, see → saw, eat → ate, have → had. Dans une question ou une négation, le verbe revient à la base : Did you go? / I didn't go.",
    quiz: [
      ["Passé de « go » :", ["goed", "went", "gone"], 1, "go → went (irrégulier)."],
      ["« Tu as mangé ? »", ["Did you ate?", "Did you eat?", "Do you ate?"], 1, "Après « did », le verbe reste à la base : eat."],
      ["« Je n'ai pas vu le film. »", ["I didn't see the movie.", "I didn't saw the movie.", "I not saw the movie."], 0, "Didn't + verbe de base."],
      ["Complète : « Last year, we ___ in Boston. »", ["live", "lived", "living"], 1, "Last year → passé : lived."]
    ]
  },
  {
    id: "i3", niveau: "intermediaire", emoji: "🔮", titre: "Parler du futur",
    intro: "Will pour une décision ou une promesse, going to pour un projet déjà prévu.",
    points: [
      ["I'll call you tonight.", "Je t'appelle ce soir.", "aïl KOL iou tou-NAÏT"],
      ["I'm going to travel in December.", "Je vais voyager en décembre. (c'est prévu)", "aïm GO-ing tou TRA-vel"],
      ["It will rain tomorrow.", "Il va pleuvoir demain.", "it ouil RÈÏN tou-MO-ro"],
      ["Are you going to come?", "Tu vas venir ?", "ar iou GO-ing tou KEUM"],
      ["I won't be late.", "Je ne serai pas en retard.", "aï OUO-ount bi LÈÏT"],
      ["See you next week!", "À la semaine prochaine !", "si iou NÈKST ouik"]
    ],
    astuce: "« I won't » = « I will not ». Attention à la prononciation : won't [ouo-ount] n'est pas want [ouant] (vouloir).",
    quiz: [
      ["Le téléphone sonne. Tu décides sur le moment : « Je réponds ! »", ["I'm going to answer!", "I'll answer!", "I answer!"], 1, "Décision prise sur le moment → will."],
      ["« Je ne viendrai pas. »", ["I won't come.", "I want come.", "I will no come."], 0, "Won't = will not."],
      ["Ton voyage est déjà réservé. Tu dis…", ["I'll travel to Paris.", "I'm going to travel to Paris.", "I travel to Paris."], 1, "Projet déjà prévu → going to."],
      ["Complète : « It ___ be hot tomorrow. »", ["will", "is", "going"], 0, "It will be hot = il fera chaud."]
    ]
  },
  {
    id: "i4", niveau: "intermediaire", emoji: "🪤", titre: "Les faux amis",
    intro: "Ces mots ressemblent au français… mais ne veulent pas dire la même chose !",
    points: [
      ["actually", "en fait (pas « actuellement »)", "AK-tchou-è-li"],
      ["currently", "actuellement", "KEU-rent-li"],
      ["library", "bibliothèque (pas « librairie »)", "LAÏ-bre-ri"],
      ["bookshop", "librairie", "BOUK-chop"],
      ["sensible", "raisonnable (pas « sensible »)", "SÈN-si-bel"],
      ["sensitive", "sensible", "SÈN-si-tiv"],
      ["to attend", "assister à (pas « attendre »)", "e-TÈND"],
      ["to wait", "attendre", "OUÈÏT"]
    ],
    astuce: "Quand un mot anglais ressemble trop au français, méfie-toi et vérifie. « Eventually » = finalement (pas éventuellement), « a coin » = une pièce de monnaie.",
    quiz: [
      ["« I attended the meeting » veut dire…", ["J'ai attendu la réunion", "J'ai assisté à la réunion", "J'ai organisé la réunion"], 1, "To attend = assister à."],
      ["« Actuellement, je suis au chômage. »", ["Actually, I'm unemployed.", "Currently, I'm unemployed.", "Eventually, I'm unemployed."], 1, "Actuellement = currently."],
      ["« library » veut dire…", ["librairie", "bibliothèque", "liberté"], 1, "Library = bibliothèque ; librairie = bookshop."],
      ["« Elle est très sensible. »", ["She is very sensible.", "She is very sensitive.", "She is very sensation."], 1, "Sensible (émotif) = sensitive."]
    ]
  },

  /* ------------------------------ AVANCÉ ------------------------------ */
  {
    id: "a1", niveau: "avance", emoji: "🔗", titre: "Le present perfect (since / for)",
    intro: "Le temps qui relie le passé au présent : une expérience, ou une action qui dure encore.",
    points: [
      ["I have lived here since 2019.", "J'habite ici depuis 2019.", "aï hav LIVD hir sins…"],
      ["I have worked here for 3 years.", "Je travaille ici depuis 3 ans.", "aï hav OUEURKT hir for…"],
      ["Have you ever been to Canada?", "Es-tu déjà allé(e) au Canada ?", "hav iou È-veur BIN tou KA-na-da"],
      ["I've never seen snow.", "Je n'ai jamais vu la neige.", "aïv NÈ-veur SIN sno-ou"],
      ["She has just arrived.", "Elle vient d'arriver.", "chi haz DJEUST e-RAÏVD"],
      ["We haven't finished yet.", "Nous n'avons pas encore fini.", "oui HA-vent FI-nicht IÈT"]
    ],
    astuce: "Since + un point de départ (since Monday, since 2019). For + une durée (for two weeks, for 3 years). Et pour « depuis », jamais le présent simple : « I live here since 2019 » est faux.",
    quiz: [
      ["« Je travaille ici depuis 2020. »", ["I work here since 2020.", "I have worked here since 2020.", "I worked here since 2020."], 1, "Action qui dure encore → present perfect + since."],
      ["Complète : « I've known him ___ ten years. »", ["since", "for", "during"], 1, "Durée → for."],
      ["« Es-tu déjà allé à Paris ? »", ["Did you ever go to Paris?", "Have you ever been to Paris?", "Are you ever gone to Paris?"], 1, "Expérience de vie → Have you ever been…?"],
      ["« Elle vient de partir. »", ["She has just left.", "She just has leave.", "She comes to leave."], 0, "Venir de = have just + participe."]
    ]
  },
  {
    id: "a2", niveau: "avance", emoji: "🔀", titre: "Les phrases avec « if »",
    intro: "Pour parler de conditions réelles ou imaginaires.",
    points: [
      ["If it rains, I'll stay at home.", "S'il pleut, je resterai à la maison.", "if it RÈÏNZ, aïl STÈÏ"],
      ["If I were rich, I would travel.", "Si j'étais riche, je voyagerais.", "if aï OUEUR RITCH, aï woud TRA-vel"],
      ["If I had known, I would have come.", "Si j'avais su, je serais venu(e).", "if aï had NO-OUN…"],
      ["What would you do if…?", "Que ferais-tu si… ?", "ouat woud iou DOU if"],
      ["Unless you study, you won't pass.", "Si tu n'étudies pas, tu ne réussiras pas.", "eun-LÈS iou STEU-di"],
      ["I wish I spoke English fluently.", "J'aimerais parler anglais couramment.", "aï OUICH aï SPO-OUK… FLOU-ent-li"]
    ],
    astuce: "Jamais « will » juste après « if » : on dit « If it rains », pas « If it will rain ». Et pour l'imaginaire, « If I were » marche pour tout le monde (I, he, she).",
    quiz: [
      ["« S'il vient, je lui parlerai. »", ["If he will come, I'll talk to him.", "If he comes, I'll talk to him.", "If he came, I'll talk to him."], 1, "Pas de will après if : If he comes…"],
      ["« Si j'étais toi, je partirais. »", ["If I was you, I will go.", "If I were you, I would go.", "If I am you, I would go."], 1, "Situation imaginaire : If I were…, I would…"],
      ["« Unless » veut dire…", ["à moins que / si… ne… pas", "parce que", "même si"], 0, "Unless = sauf si, à moins que."],
      ["Complète : « If I ___ the time, I would help you. »", ["have", "had", "will have"], 1, "Imaginaire → passé : If I had…"]
    ]
  },
  {
    id: "a3", niveau: "avance", emoji: "💼", titre: "Réussir un entretien en anglais",
    intro: "Les phrases clés pour un entretien d'embauche ou une bourse.",
    points: [
      ["Tell me about yourself.", "Parlez-moi de vous.", "tèl mi e-BAOT ior-SÈLF"],
      ["I have three years of experience in sales.", "J'ai 3 ans d'expérience dans la vente.", "…iks-PI-ri-ens in SÈÏLZ"],
      ["My main strength is…", "Ma principale qualité est…", "maï mèïn STRÈNGS iz"],
      ["I'm a fast learner.", "J'apprends vite.", "aïm e fast LEUR-neur"],
      ["I work well under pressure.", "Je travaille bien sous pression.", "…EUN-deur PRÈ-cheur"],
      ["Why should we hire you?", "Pourquoi devrions-nous vous embaucher ?", "ouaï choud oui HAÏ-eur iou"],
      ["Do you have any questions for us?", "Avez-vous des questions ?", "dou iou hav È-ni KOUÈS-tchenz"],
      ["Thank you for your time.", "Merci pour votre temps.", "SÈNK-iou for ior TAÏM"]
    ],
    astuce: "Prépare ta présentation en 4 phrases : qui tu es, ton expérience, ta qualité principale avec un exemple, et pourquoi ce poste. Et réponds toujours « Yes » à « Do you have any questions? » avec une vraie question.",
    quiz: [
      ["« Tell me about yourself » : tu commences par…", ["My name is… I have … years of experience in…", "I am 30 years.", "Yes, I want the job."], 0, "On se présente avec son parcours et son expérience."],
      ["« J'apprends vite » :", ["I learn fastly.", "I'm a fast learner.", "I'm learning quick."], 1, "Expression naturelle : I'm a fast learner."],
      ["« strength » veut dire…", ["faiblesse", "point fort / qualité", "salaire"], 1, "Strength = point fort. Weakness = point faible."],
      ["À la fin de l'entretien, tu dis…", ["Bye bye!", "Thank you for your time.", "Give me the job."], 1, "Formule polie : Thank you for your time."]
    ]
  },
  {
    id: "a4", niveau: "avance", emoji: "🧩", titre: "Les phrasal verbs du quotidien",
    intro: "Un verbe + une petite particule = un nouveau sens. Les anglophones les utilisent tout le temps.",
    points: [
      ["to give up", "abandonner", "giv EUP"],
      ["to find out", "découvrir, apprendre", "faïnd AOT"],
      ["to look for", "chercher", "LOUK for"],
      ["to look after", "s'occuper de", "louk AF-teur"],
      ["to turn off / to turn on", "éteindre / allumer", "teurn OF / teurn ON"],
      ["to get up", "se lever", "guèt EUP"],
      ["to run out of", "manquer de, être à court de", "reun AOT ov"],
      ["to put off", "reporter, remettre à plus tard", "pout OF"]
    ],
    astuce: "Apprends-les dans une phrase, pas seuls : « Don't give up! », « We've run out of sugar », « The meeting was put off until Monday ».",
    quiz: [
      ["« Je cherche mes clés. »", ["I'm looking after my keys.", "I'm looking for my keys.", "I'm looking out my keys."], 1, "Look for = chercher."],
      ["« N'abandonne pas ! »", ["Don't give up!", "Don't give in!", "Don't get up!"], 0, "Give up = abandonner."],
      ["« Éteins la télé. »", ["Turn on the TV.", "Turn off the TV.", "Turn out the TV."], 1, "Turn off = éteindre."],
      ["« We've run out of bread » veut dire…", ["On a couru acheter du pain", "On n'a plus de pain", "On a trop de pain"], 1, "Run out of = ne plus avoir de."]
    ]
  }
];

/* ------------------------------ FLASHCARDS ------------------------------ */
window.FLASHCARDS = [
  { theme: "Salutations", emoji: "👋", cartes: [
    ["Good morning", "Bonjour (matin)", "goud MOR-ning"], ["Good afternoon", "Bon après-midi", "goud af-teur-NOUN"],
    ["How are you doing?", "Comment ça va ?", "hao ar iou DOU-ing"], ["Long time no see!", "Ça fait longtemps !", "long taïm no-ou SI"],
    ["Welcome!", "Bienvenue !", "OUÈL-keum"], ["Take care!", "Prends soin de toi !", "tèïk KÈR"],
    ["Have a nice day!", "Bonne journée !", "hav e naïs DÈÏ"], ["Sorry, excuse me", "Pardon, excusez-moi", "SO-ri, iks-KIOUZ mi"]
  ]},
  { theme: "Au travail", emoji: "💼", cartes: [
    ["a meeting", "une réunion", "e MI-ting"], ["a salary", "un salaire", "e SA-le-ri"],
    ["a boss / a manager", "un patron / un responsable", "e BOS / e MA-ni-djeur"], ["a colleague", "un(e) collègue", "e KO-lig"],
    ["a deadline", "une date limite", "e DÈD-laïn"], ["to apply for a job", "postuler à un emploi", "tou e-PLAÏ for e DJOB"],
    ["a day off", "un jour de congé", "e dèï OF"], ["I'm busy", "Je suis occupé(e)", "aïm BI-zi"]
  ]},
  { theme: "Voyage", emoji: "✈️", cartes: [
    ["a passport", "un passeport", "e PAS-port"], ["a ticket", "un billet", "e TI-kit"],
    ["the airport", "l'aéroport", "dzi ÈR-port"], ["a flight", "un vol", "e FLAÏT"],
    ["luggage", "les bagages", "LEU-guidj"], ["Where is the exit?", "Où est la sortie ?", "ouèr iz dzi ÈK-sit"],
    ["I'd like a room", "Je voudrais une chambre", "aïd laïk e ROUM"], ["Can you help me?", "Pouvez-vous m'aider ?", "kèn iou HÈLP mi"]
  ]},
  { theme: "Au marché", emoji: "🛒", cartes: [
    ["How much is it?", "C'est combien ?", "hao MEUTCH iz it"], ["cheap", "pas cher", "TCHIP"],
    ["expensive", "cher", "iks-PÈN-siv"], ["Can you reduce the price?", "Tu peux diminuer ?", "kèn iou ri-DIOUS dze PRAÏS"],
    ["the change", "la monnaie", "dze TCHÈÏNDJ"], ["a bag", "un sac", "e BAG"],
    ["fresh fish", "du poisson frais", "frèch FICH"], ["I'll take it", "Je le prends", "aïl TÈÏK it"]
  ]},
  { theme: "Football", emoji: "⚽", cartes: [
    ["to score a goal", "marquer un but", "tou SKOR e GO-OUL"], ["the referee", "l'arbitre", "dze rè-fe-RI"],
    ["a penalty", "un penalty", "e PÈ-nel-ti"], ["the goalkeeper", "le gardien", "dze GO-OUL-ki-peur"],
    ["a draw", "un match nul", "e DRO"], ["to win / to lose", "gagner / perdre", "tou OUIN / tou LOUZ"],
    ["the fans", "les supporters", "dze FANZ"], ["What a goal!", "Quel but !", "ouat e GO-OUL"]
  ]},
  { theme: "Famille & amour", emoji: "❤️", cartes: [
    ["my husband / my wife", "mon mari / ma femme", "maï HEUZ-bend / maï OUAÏF"], ["my parents", "mes parents", "maï PÈ-rents"],
    ["my brother / my sister", "mon frère / ma sœur", "maï BREU-dzeur / maï SIS-teur"], ["to fall in love", "tomber amoureux", "tou fol in LEUV"],
    ["a wedding", "un mariage", "e OUÈ-ding"], ["I miss you", "Tu me manques", "aï MIS iou"],
    ["my best friend", "mon/ma meilleur(e) ami(e)", "maï BÈST frènd"], ["He's not my type", "Il n'est pas mon genre", "hiz NOT maï TAÏP"]
  ]},
  { theme: "Noël & fêtes", emoji: "🎄", cartes: [
    ["Merry Christmas!", "Joyeux Noël !", "MÈ-ri KRIS-mes"], ["Happy New Year!", "Bonne année !", "HA-pi niou IIR"],
    ["a gift / a present", "un cadeau", "e GUIFT / e PRÈ-zent"], ["a party", "une fête", "e PAR-ti"],
    ["to celebrate", "fêter, célébrer", "tou SÈ-le-brèït"], ["Cheers!", "Santé !", "TCHIIRZ"],
    ["Best wishes!", "Meilleurs vœux !", "bèst OUI-chiz"], ["Christmas Eve", "le réveillon de Noël", "KRIS-mes IV"]
  ]}
];

/* ---------------------------- PHRASE DU JOUR ---------------------------- */
window.PHRASES = [
  ["Nice to meet you!", "Enchanté(e) de te rencontrer !", "naïs tou MIT iou"],
  ["Could you repeat, please?", "Tu peux répéter, s'il te plaît ?", "koud iou ri-PIT, pliz"],
  ["I'm on my way.", "Je suis en route.", "aïm on maï OUÈÏ"],
  ["How much is it?", "Ça coûte combien ?", "hao MEUTCH iz it"],
  ["Can you speak more slowly?", "Tu peux parler plus lentement ?", "kèn iou spik mor SLO-OU-li"],
  ["I'm looking forward to it.", "J'ai hâte.", "aïm LOU-king FOR-oueurd tou it"],
  ["What do you do for a living?", "Qu'est-ce que tu fais dans la vie ?", "ouat dou iou DOU for e LI-ving"],
  ["Let me think about it.", "Laisse-moi y réfléchir.", "lèt mi SINK e-baot it"],
  ["It's up to you.", "C'est toi qui décides.", "its EUP tou iou"],
  ["I'm used to it.", "J'en ai l'habitude.", "aïm IOUST tou it"],
  ["Take your time.", "Prends ton temps.", "tèïk ior TAÏM"],
  ["I didn't get that.", "Je n'ai pas compris.", "aï DI-dent GUÈT dzat"],
  ["Never mind.", "Ce n'est pas grave / Laisse tomber.", "NÈ-veur MAÏND"],
  ["I'm running late.", "Je suis en retard.", "aïm REU-ning LÈÏT"],
  ["Tell me about yourself.", "Parle-moi de toi.", "tèl mi e-BAOT ior-SÈLF"],
  ["What's your strength?", "Quel est ton point fort ?", "ouats ior STRÈNGS"],
  ["I can't wait!", "J'ai trop hâte !", "aï KANT OUÈÏT"],
  ["Keep the change.", "Gardez la monnaie.", "kip dze TCHÈÏNDJ"],
  ["It doesn't matter.", "Ça n'a pas d'importance.", "it DEU-zent MA-teur"],
  ["See you later!", "À plus tard !", "SI iou LÈÏ-teur"],
  ["I'm fed up.", "J'en ai marre.", "aïm fèd EUP"],
  ["Merry Christmas and Happy New Year!", "Joyeux Noël et bonne année !", "MÈ-ri KRIS-mes ènd HA-pi niou IIR"],
  ["Practice makes perfect.", "C'est en forgeant qu'on devient forgeron.", "PRAK-tis mèïks PEUR-fikt"],
  ["Break a leg!", "Bonne chance ! (avant un examen, un spectacle…)", "brèïk e LÈG"],
  ["I'm all ears.", "Je suis tout ouïe.", "aïm ol IIRZ"],
  ["That makes sense.", "Ça a du sens / Je comprends.", "dzat mèïks SÈNS"],
  ["Better late than never.", "Mieux vaut tard que jamais.", "BÈ-teur lèït dzen NÈ-veur"],
  ["Could you help me, please?", "Tu peux m'aider, s'il te plaît ?", "koud iou HÈLP mi, pliz"],
  ["Where are you from?", "Tu viens d'où ?", "ouèr ar iou FROM"],
  ["I speak English, and you?", "Je parle anglais, et toi ?", "aï spik ING-lich, ènd IOU"]
];

/* ----------------------------- MINI-DÉFI ----------------------------- */
window.DEFIS = [
  ["Comment dit-on « Je suis en retard » ?", ["I'm late.", "I'm later.", "I have late."], 0],
  ["« I have 25 years » est…", ["Correct", "Incorrect : on dit « I am 25 »"], 1],
  ["Complète : « She ___ in London. »", ["live", "lives", "living"], 1],
  ["Que veut dire « actually » ?", ["Actuellement", "En fait / en réalité"], 1],
  ["« Je suis d'accord » se dit…", ["I am agree.", "I agree."], 1],
  ["Complète : « I'm good ___ English. »", ["in", "at", "on"], 1],
  ["Que veut dire « library » ?", ["Librairie", "Bibliothèque"], 1],
  ["« J'ai froid » se dit…", ["I have cold.", "I'm cold."], 1],
  ["Passé de « buy » :", ["buyed", "bought", "brought"], 1],
  ["« Depuis 2020 » :", ["for 2020", "since 2020", "from 2020"], 1]
];
