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
  // Pixel Meta (Facebook/Instagram) : coller ici le numéro du pixel pour suivre les pubs, ex. "1234567890123456"
  metaPixel: "1967147677422094",
  // Clés d'accès des tests (le tableau Google « Winners – Admin du site » peut les changer)
  cles: { rapide: "WIN2026", placement: "WIN2026" },
  brochure: "brochure.pdf",
  // Couleurs par défaut (celles du logo), utilisées quand aucun programme n'est en cours
  couleurs: { sombre: "#2F3480", principal: "#B83A35", accent: "#F2B33D" },
  // Numéros de paiement mobile (laisser la liste vide [] pour que les gens demandent sur WhatsApp)
  paiement: {
    numeros: ["07 67 03 72 84", "01 41 81 70 78", "05 56 42 35 66"],
    // Moyens de paiement affichés sur la page du programme (bloc « Payer ma place »)
    // Tous ces numéros acceptent aussi Wave. Pour en ajouter un : copier une ligne et changer l'opérateur et le numéro.
    operateurs: [
      { op: "Orange Money ou Wave", num: "07 67 03 72 84" },
      { op: "Moov Money ou Wave",   num: "01 41 81 70 78" },
      { op: "MTN MoMo ou Wave",     num: "05 56 42 35 66" }
    ],
    titulaire: "",
    // Virement bancaire (laisser rib vide "" pour le masquer)
    banque: { nom: "Djamo", titulaire: "Guy Boris Douka", rib: "CI201 01001 111607555481 35" }
  }
};

window.PROGRAMMES = [
  {
    id: "noel-2026",
    lien: "promo-noel",                         // lien publicitaire du site : …/site/#promo-noel
    nom: "PROMO ANGLAIS NOËL",
    emoji: "🎄",
    accroche: "2 mois de cours, novembre et décembre, pour oser enfin parler anglais",
    duree: "2 mois : novembre + décembre 2026",
    visuel: "img/promo_noel.jpg",
    couleurs: { sombre: "#2F3480", principal: "#B83A35", accent: "#F2B33D" },
    afficherDes: "2026-10-01",                 // date à partir de laquelle l'appli montre ce programme
    inscriptions: ["2026-10-26", "2026-11-15"], // ouverture, clôture
    cours: ["2026-11-16", "2026-12-24"],        // début, fin
    prix: 45000,
    prixBarre: 95000,
    acompte: 25000,
    paiementTexte: "45 000 F pour les 2 mois : 25 000 F à l'inscription, 20 000 F avant le 7 décembre",
    reductionAmi: 5000,
    details: [
      ["📅", "<b>2 mois de cours : novembre et décembre</b>, du lundi 16 novembre au jeudi 24 décembre 2026"],
      ["🕑", "<b>2 cours de 2 h</b> par semaine"],
      ["📍", "<b>Présentiel</b> (Cocody Riviera Palmeraie) ou <b>en ligne</b>"],
      ["💳", "<b>45 000 F</b> pour les 2 mois : 25 000 F à l'inscription, 20 000 F avant le 7 décembre"],
      ["📚", "Supports : <b>10 000 F</b> (document de cours, audios, vidéos…)"],
      ["⏳", "Inscriptions ouvertes jusqu'au <b>dimanche 15 novembre</b>"]
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
      ["Je peux payer en deux fois ?", "Oui : 25 000 F à l'inscription, puis 20 000 F avant le 7 décembre."],
      ["C'est quoi les supports à 10 000 F ?", "Ton document de cours, les audios et les vidéos pour pratiquer à la maison entre les séances."],
      ["Quels jours ont lieu les cours ?", "2 séances de 2 h par semaine. Les jours et horaires des groupes te sont communiqués à l'inscription."],
      ["Je suis déjà élève de Winners' English Center…", "Écris à Coach Winner sur WhatsApp, il te dira comment continuer."]
    ],
    agenda: [
      ["2026-10-26", "Ouverture des inscriptions"],
      ["2026-11-14", "Masterclass gratuite (8 h 30 – 12 h) à CHIC SALLE"],
      ["2026-11-15", "Clôture des inscriptions"],
      ["2026-11-16", "Premier cours"],
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
    prix: 0, prixBarre: 0, acompte: 25000, paiementTexte: "",
    reductionAmi: 0,
    details: [], bonus: [], faq: [], agenda: []
  }
  */
];
