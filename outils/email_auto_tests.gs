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
