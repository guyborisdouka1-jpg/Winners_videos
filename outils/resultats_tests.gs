// Winners' English Center — réception des résultats des tests du site
// Chaque test terminé : 1 ligne dans l'onglet « Tests » + alerte WhatsApp (CallMeBot) + alerte Gmail.

var TELEPHONE = '+2250767037284';   // numéro WhatsApp qui reçoit les alertes
var CLE_CALLMEBOT = 'A_REMPLIR';    // code reçu de CallMeBot

function doPost(e) {
  var d = {};
  try { d = JSON.parse(e.postData.contents || '{}'); } catch (x) {}
  var ss = SpreadsheetApp.getActive();
  var sh = ss.getSheetByName('Tests') || ss.insertSheet('Tests');
  if (sh.getLastRow() === 0) {
    sh.appendRow(['Date', 'Test', 'Nom', 'Téléphone', 'Niveau', 'Score', 'Détail', 'Relancé ?']);
    sh.setFrozenRows(1);
    sh.getRange(1, 1, 1, 8).setFontWeight('bold');
  }
  var date = Utilities.formatDate(new Date(), 'Africa/Abidjan', 'dd/MM/yyyy HH:mm');
  sh.appendRow([date, d.test || '', d.nom || '', "'" + (d.tel || ''), d.niveau || '', d.score || '', d.detail || '', '']);

  var msg = '🆕 Test terminé (' + (d.test || '') + ')\n' +
            'Nom : ' + (d.nom || '') + '\n' +
            'Tél : ' + (d.tel || 'non donné') + '\n' +
            'Niveau : ' + (d.niveau || '') + '\n' +
            'Score : ' + (d.score || '') + '\n' + date;

  if (CLE_CALLMEBOT && CLE_CALLMEBOT !== 'A_REMPLIR') {
    try {
      UrlFetchApp.fetch('https://api.callmebot.com/whatsapp.php?phone=' + encodeURIComponent(TELEPHONE) +
        '&text=' + encodeURIComponent(msg) + '&apikey=' + encodeURIComponent(CLE_CALLMEBOT), { muteHttpExceptions: true });
    } catch (x) {}
  }
  try {
    MailApp.sendEmail(Session.getEffectiveUser().getEmail(), '🆕 Test : ' + (d.nom || '') + ' – ' + (d.niveau || ''), msg);
  } catch (x) {}
  return ContentService.createTextOutput('ok');
}

// Pour essayer sans le site : exécuter cette fonction depuis l'éditeur.
function essai() {
  doPost({ postData: { contents: JSON.stringify({ test: 'Essai', nom: 'Test Coach', tel: '07 00 00 00 00', niveau: 'A2', score: '20/40', detail: 'essai' }) } });
}
