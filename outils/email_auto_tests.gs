// Winners' English Center — email de relance automatique après un test du site
// À installer dans le compte Google winnersenglish04@gmail.com (Déployer > Application Web > Tout le monde)
var MSGN = {
  'Pré-A1': "Vous démarrez l'anglais : on reprend les bases ensemble, pas à pas, sans stress.",
  'A1': "Vous avez les bases. Objectif : parler de vous et du quotidien avec confiance.",
  'A2': "Vous vous débrouillez sur des sujets simples. Objectif : tenir des conversations plus longues et plus fluides.",
  'B1': "Vous avez un bon niveau. Objectif : parler avec aisance, sans chercher vos mots.",
  'B2': "Excellent niveau ! Objectif : affiner votre anglais pour être à l'aise dans toutes les situations.",
  'B2+': "Excellent niveau ! Objectif : affiner votre anglais pour être à l'aise dans toutes les situations."
};
function doPost(e) {
  var d = {}; try { d = JSON.parse(e.postData.contents || '{}'); } catch (x) {}
  var email = String(d.email || '').trim(), nom = String(d.nom || '').slice(0, 60), lv = String(d.niveau || '').split(' ')[0];
  if (d.type === 'inscription') return inscription(d, email, nom);
  if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email) || !MSGN[lv]) return ContentService.createTextOutput('ignoré');
  var cache = CacheService.getScriptCache(); if (cache.get(email)) return ContentService.createTextOutput('déjà envoyé'); cache.put(email, '1', 3600);
  var pren = nom.split(' ')[0] || '';
  var corps = 'Bonjour ' + pren + ',\n\nIci Coach Winner de Winners\' English Center 👋\n\n' +
    'Merci d\'avoir fait notre test ' + (d.test === 'placement' ? 'de placement' : 'de niveau') + '. Votre niveau : ' + lv + (d.score ? ' (' + String(d.score).slice(0, 10) + ')' : '') + '.\n' + MSGN[lv] + '\n\n' +
    'La Promo Anglais Noël (2 mois de cours, novembre + décembre, en présentiel ou en ligne) est faite pour vous.\n' +
    'Découvrez le programme et inscrivez-vous en ligne :\nhttps://winnersenglishcenter.com/site/#promo-noel\n\nÀ très vite !\nCoach Winner\nWinners\' English Center';
  GmailApp.sendEmail(email, 'Votre résultat au test : niveau ' + lv, corps, { name: "Coach Winner – Winners' English Center" });
  return ContentService.createTextOutput('ok');
}

// Email automatique après une inscription à la Promo Noël
function inscription(d, email, nom) {
  if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) return ContentService.createTextOutput('ignoré');
  var cache = CacheService.getScriptCache(); if (cache.get('i:' + email)) return ContentService.createTextOutput('déjà envoyé'); cache.put('i:' + email, '1', 3600);
  var mode = /ligne/.test(String(d.mode || '')) ? 'en ligne' : 'en présentiel';
  var corps = 'Bonjour ' + (nom.split(' ')[0] || '') + ' 👋, ici Coach Winner de Winners\' English Center.\n' +
    'Merci pour votre inscription à la Promo Anglais Noël 🎄 (' + mode + ').\n\n' +
    'Pour réserver votre place :\n💳 25 000 F à l\'inscription, puis il reste 20 000 F à payer avant le 7 décembre.\n📚 Supports de cours : 10 000 F\n' +
    '📲 Wave / Mobile Money : 07 67 03 72 84 · 01 41 81 70 78 · 05 56 42 35 66\nEnvoyez-moi la capture de votre paiement sur WhatsApp (07 67 03 72 84).\n\n' +
    '📝 Si ce n\'est pas encore fait, passez votre test de placement (30 min) : https://winnersenglishcenter.com/placement/ (code : WIN2026)\n\nÀ très vite !\nCoach Winner';
  GmailApp.sendEmail(email, 'Votre inscription à la Promo Anglais Noël 🎄', corps, { name: "Coach Winner – Winners' English Center" });
  return ContentService.createTextOutput('ok');
}
