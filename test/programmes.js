/* =====================================================================
   WINNERS' ENGLISH CENTER — RÉGLAGES DU CENTRE ET DES PROGRAMMES
   ---------------------------------------------------------------------
   Pour lancer un nouveau programme : ajouter un bloc dans PROGRAMMES.
   L'application choisit toute seule le programme du moment selon les
   dates, et prend ses couleurs, son visuel, ses prix et ses bonus.
   Dates au format "AAAA-MM-JJ".
   ===================================================================== */

window.CENTRE = {
  nom: "Winners' English Center",
  slogan: "I speak English, and you?",
  coach: "Coach Winner",
  whatsapp: "2250767037284",          // format international, sans + ni espaces
  telAffiche: "07 67 03 72 84",
  adresse: "Cocody Riviera Palmeraie, non loin de Chez Samer",
  facebook: "https://www.facebook.com/108178682182393",
  tiktok: "https://www.tiktok.com/@winnersenglish",
  // Couleurs par défaut (celles du logo), utilisées quand aucun programme n'est en cours
  couleurs: { sombre: "#2F3480", principal: "#B83A35", accent: "#F2B33D" },
  // Paiement mobile : laisser vide "" pour que les gens demandent le numéro sur WhatsApp
  paiement: {
    wave: "",
    orangeMoney: "",
    mtnMoney: "",
    moovMoney: "",
    titulaire: ""
  }
};

window.PROGRAMMES = [
  {
    id: "noel-2026",
    nom: "PROMO ANGLAIS NOËL",
    emoji: "🎄",
    accroche: "6 semaines pour oser enfin parler anglais",
    visuel: "img/promo_noel.jpg",
    couleurs: { sombre: "#2F3480", principal: "#B83A35", accent: "#F2B33D" },
    afficherDes: "2026-10-01",                 // date à partir de laquelle l'appli montre ce programme
    inscriptions: ["2026-10-26", "2026-11-08"], // ouverture, clôture
    cours: ["2026-11-09", "2026-12-24"],        // début, fin
    prix: 65000,
    prixBarre: 95000,
    acompte: 35000,
    paiementTexte: "35 000 F à l'inscription, puis 30 000 F début décembre",
    reductionAmi: 5000,
    details: [
      ["📅", "Du <b>lundi 9 novembre au jeudi 24 décembre 2026</b>"],
      ["🕑", "<b>2 cours de 2 h</b> par semaine"],
      ["📍", "<b>Présentiel</b> (Cocody Riviera Palmeraie) ou <b>en ligne</b>"],
      ["💳", "<b>35 000 F</b> à l'inscription, puis <b>30 000 F</b> début décembre"],
      ["⏳", "Inscriptions du <b>26 octobre au 8 novembre</b>"]
    ],
    bonus: [
      ["📝", "Test de niveau gratuit"],
      ["📘", "Livre <b>English Starter</b> offert aux 10 premiers inscrits"],
      ["👫", "<b>5 000 F de réduction</b> chacun si tu viens avec un ami"],
      ["🎉", "<b>Christmas English Party</b> + attestation de fin de formation"],
      ["🌴", "Sortie de groupe + T-shirt après le programme <span class='muted'>(petite participation, détails pendant la formation)</span>"]
    ],
    faq: [
      ["Je suis débutant complet, je peux venir ?", "Oui ! Le test de niveau nous permet de te placer dans le groupe qui te correspond."],
      ["Comment se passent les cours en ligne ?", "En direct avec Coach Winner, avec les mêmes exercices oraux qu'en présentiel. Il te faut juste un téléphone et une connexion."],
      ["Je peux payer en deux fois ?", "Oui : 35 000 F à l'inscription, puis 30 000 F début décembre."],
      ["Quels jours ont lieu les cours ?", "2 séances de 2 h par semaine. Les jours et horaires des groupes te sont communiqués à l'inscription."],
      ["Je suis déjà élève de Winners' English Center…", "Écris à Coach Winner sur WhatsApp, il te dira comment continuer."]
    ],
    agenda: [
      ["2026-10-26", "Ouverture des inscriptions"],
      ["2026-11-08", "Clôture des inscriptions"],
      ["2026-11-09", "Premier cours"],
      ["2026-12-01", "Paiement du 2e versement (30 000 F)"],
      ["2026-12-24", "Dernier cours, Christmas English Party (CHIC SALLE) et remise des attestations"]
    ]
  }

  /* MODÈLE pour le prochain programme (enlever les deux marques de commentaire autour pour l activer) :
  ,{
    id: "rentree-2027",
    nom: "NOM DU PROGRAMME",
    emoji: "🚀",
    accroche: "Phrase d'accroche",
    visuel: "img/visuel_programme.jpg",
    couleurs: { sombre: "#2F3480", principal: "#B83A35", accent: "#F2B33D" },
    afficherDes: "2026-12-26",
    inscriptions: ["2026-12-26", "2027-01-10"],
    cours: ["2027-01-11", "2027-03-05"],
    prix: 0, prixBarre: 0, acompte: 0, paiementTexte: "",
    reductionAmi: 0,
    details: [], bonus: [], faq: [], agenda: []
  }
  */
];
