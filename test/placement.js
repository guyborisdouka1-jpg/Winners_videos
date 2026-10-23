/* =====================================================================
   WINNERS' ENGLISH CENTER : TEST DE PLACEMENT (A1 à B2)
   Questions originales du centre. 4 parties de difficulté croissante.
   type "choice" : options + a = numéro de la bonne réponse (0 = première)
   type "text"   : a = liste des réponses acceptées (majuscules et points ignorés)
   ===================================================================== */
window.PLACEMENT = {
  titre: "Test de placement",
  duree: "30 à 40 minutes",
  parts: [
  { level: "A1", titre: "Partie 1 : Débutant (A1)", exercises: [
    { titre: "Choisis la bonne réponse", type: "choice", items: [
      { q: "Are you a student?", options: ["Yes, I am.", "Yes, I do.", "Yes, I student."], a: 0 },
      { q: "Where do you live?", options: ["I'm 25.", "I live in London.", "I'm a teacher."], a: 1 },
      { q: "What's her name?", options: ["Her name is Emma.", "His name is Emma.", "My name is Emma."], a: 0 },
      { q: "Do they speak English?", options: ["Yes, they speak.", "Yes, they do.", "Yes, they are."], a: 1 },
      { q: "How are you?", options: ["I'm fine, thank you.", "I'm Paul.", "I'm from Leeds."], a: 0 }
    ]},
    { titre: "Complète avec am, is ou are", type: "text", banque: "am / is / are", items: [
      { q: "I ___ a teacher.", a: ["am"] },
      { q: "She ___ my sister.", a: ["is"] },
      { q: "We ___ happy today.", a: ["are"] },
      { q: "It ___ cold this morning.", a: ["is"] },
      { q: "You ___ late!", a: ["are"] }
    ]},
    { titre: "Écris le nombre en lettres, en anglais", type: "text", items: [
      { q: "15", a: ["fifteen"] },
      { q: "40", a: ["forty"] },
      { q: "72", a: ["seventy-two", "seventy two"] },
      { q: "100", a: ["one hundred", "a hundred", "hundred"] }
    ]},
    { titre: "Quelle couleur ? Écris-la en anglais", type: "text", items: [
      { q: "Le ciel, la mer", a: ["blue"] },
      { q: "Le lait, la neige", a: ["white"] },
      { q: "Une banane mûre, le soleil", a: ["yellow"] }
    ]},
    { titre: "In, on ou at ?", type: "choice", items: [
      { q: "My birthday is ___ March.", options: ["in", "on", "at"], a: 0 },
      { q: "The class starts ___ 9 o'clock.", options: ["in", "on", "at"], a: 2 },
      { q: "We have English ___ Monday.", options: ["in", "on", "at"], a: 1 },
      { q: "I sleep well ___ night.", options: ["in", "on", "at"], a: 2 }
    ]},
    { titre: "There is ou There are ?", type: "choice", items: [
      { q: "___ a book on the table.", options: ["There is", "There are"], a: 0 },
      { q: "___ ten students in the class.", options: ["There is", "There are"], a: 1 },
      { q: "___ some water in the bottle.", options: ["There is", "There are"], a: 0 }
    ]},
    { titre: "Écoute : Daniel se présente", type: "choice", audio: "audio1.mp3", consigne: "Écoute l'audio (2 écoutes maximum), puis réponds.", items: [
      { q: "What is Daniel's job?", options: ["He's a teacher.", "He's a taxi driver.", "He's a doctor."], a: 1 },
      { q: "How many children does he have?", options: ["One", "Two", "Three"], a: 1 },
      { q: "What time does he get up?", options: ["At five o'clock", "At seven o'clock", "At nine o'clock"], a: 0 },
      { q: "What does he do on Sundays?", options: ["He goes shopping.", "He works.", "He plays football."], a: 2 }
    ]}
  ]},
  { level: "A2", titre: "Partie 2 : Élémentaire (A2)", exercises: [
    { titre: "Mets le verbe au passé (past simple)", type: "text", items: [
      { q: "Yesterday, I (watch) ___ a film.", a: ["watched"] },
      { q: "Last year, we (go) ___ to Canada.", a: ["went"] },
      { q: "She (buy) ___ a new phone last week.", a: ["bought"] },
      { q: "They (not / come) ___ to class yesterday.", a: ["didn't come", "did not come"] }
    ]},
    { titre: "Écris la bonne forme de l'adjectif", type: "text", items: [
      { q: "My car is (fast) ___ than your car.", a: ["faster"] },
      { q: "This book is (interesting) ___ than that one.", a: ["more interesting"] },
      { q: "She is the (good) ___ student in the class.", a: ["best"] }
    ]},
    { titre: "Choisis le bon mot interrogatif", type: "choice", items: [
      { q: "___ is that man? He's my uncle.", options: ["Who", "Where", "What"], a: 0 },
      { q: "___ does the bus leave? At 7 a.m.", options: ["Where", "When", "Who"], a: 1 },
      { q: "___ is this shirt? Twenty dollars.", options: ["How many", "How old", "How much"], a: 2 },
      { q: "___ are you sad? Because I lost my keys.", options: ["Why", "How", "Which"], a: 0 },
      { q: "___ you see the match last night?", options: ["Do", "Did", "Were"], a: 1 }
    ]},
    { titre: "Présent simple ou présent continu ?", type: "choice", items: [
      { q: "Look! It ___ .", options: ["rains", "is raining", "rain"], a: 1 },
      { q: "I usually ___ tea in the morning.", options: ["drink", "am drinking", "drinks"], a: 0 },
      { q: "What ___ right now?", options: ["do you do", "are you doing", "you doing"], a: 1 },
      { q: "He ___ to work every day.", options: ["go", "goes", "is go"], a: 1 }
    ]}
  ]},
  { level: "B1", titre: "Partie 3 : Intermédiaire (B1)", exercises: [
    { titre: "Choisis la bonne réponse", type: "choice", items: [
      { q: "I ___ to London three times.", options: ["have been", "went", "am"], a: 0 },
      { q: "She ___ to Manchester in 2020.", options: ["has moved", "moved", "moves"], a: 1 },
      { q: "___ you ever ___ sushi?", options: ["Did / eat", "Have / eaten", "Do / eat"], a: 1 },
      { q: "We have lived here ___ ten years.", options: ["since", "for", "during"], a: 1 },
      { q: "If it rains tomorrow, we ___ at home.", options: ["stay", "will stay", "would stay"], a: 1 },
      { q: "If I ___ rich, I would travel around the world.", options: ["am", "were", "will be"], a: 1 },
      { q: "Look at those clouds! It ___ rain.", options: ["is going to", "will to", "goes"], a: 0 },
      { q: "The woman ___ lives next door is a nurse.", options: ["who", "which", "where"], a: 0 },
      { q: "This is the house ___ I was born.", options: ["which", "who", "where"], a: 2 }
    ]},
    { titre: "Lis le texte : vrai ou faux ?", type: "choice",
      texte: "Jack is 28. He works in a bank in central London. Every morning he takes the bus at 6:30 because the traffic is terrible. He started Spanish lessons last month because his company wants to work with clients from Mexico and Spain. He finds speaking difficult, but he practises every evening with a friend.",
      items: [
      { q: "Jack drives to work.", options: ["Vrai", "Faux"], a: 1 },
      { q: "He started Spanish lessons a month ago.", options: ["Vrai", "Faux"], a: 0 },
      { q: "His company works only with British clients.", options: ["Vrai", "Faux"], a: 1 },
      { q: "Speaking is easy for him.", options: ["Vrai", "Faux"], a: 1 },
      { q: "He practises with a friend.", options: ["Vrai", "Faux"], a: 0 }
    ]},
    { titre: "Écoute : le message de Marc", type: "choice", audio: "audio3.mp3", consigne: "Écoute le message vocal (2 écoutes maximum), puis réponds.", items: [
      { q: "Why can't Marc come to the meeting?", options: ["He is ill.", "His flight was cancelled.", "He is on holiday."], a: 1 },
      { q: "When will he be back?", options: ["Tomorrow morning", "On Friday morning", "On Thursday evening"], a: 2 },
      { q: "What does he ask Sarah to do?", options: ["Move the meeting to Friday", "Cancel the meeting", "Book a hotel room"], a: 0 },
      { q: "What is the problem if he joins online?", options: ["He has no computer.", "The hotel internet isn't very good.", "He has no time."], a: 1 }
    ]}
  ]},
  { level: "B2", titre: "Partie 4 : Avancé (B2)", exercises: [
    { titre: "Choisis la bonne réponse", type: "choice", items: [
      { q: "By the time we arrived, the film ___ .", options: ["had already started", "has already started", "already starts"], a: 0 },
      { q: "I wish I ___ more time to study.", options: ["have", "had", "will have"], a: 1 },
      { q: "The report ___ by the manager yesterday.", options: ["wrote", "was written", "has written"], a: 1 },
      { q: "She asked me where ___ .", options: ["I lived", "did I live", "do I live"], a: 0 },
      { q: "You ___ have told me! I would have helped you.", options: ["should", "must", "can"], a: 0 },
      { q: "He's used to ___ early.", options: ["get up", "getting up", "got up"], a: 1 },
      { q: "Despite ___ tired, she finished the work.", options: ["be", "being", "she was"], a: 1 },
      { q: "Hardly ___ the door when the phone rang.", options: ["I had opened", "had I opened", "I opened"], a: 1 }
    ]},
    { titre: "Vocabulaire et expressions", type: "choice", items: [
      { q: "Can you ___ the meeting until Friday? (= reporter)", options: ["put off", "put on", "put up"], a: 0 },
      { q: "I need to ___ my English before the interview. (= réviser)", options: ["brush up on", "look up", "give up"], a: 0 },
      { q: "« To make up your mind » veut dire :", options: ["se décider", "se maquiller", "oublier"], a: 0 },
      { q: "« Actually » veut dire :", options: ["en fait", "actuellement", "activement"], a: 0 }
    ]}
  ]}
  ]
};
