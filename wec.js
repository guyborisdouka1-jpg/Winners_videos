/* =====================================================================
   WINNERS' ENGLISH CENTER : DONNÉES MODIFIABLES PAR LE CENTRE
   Le site lit le tableau Google Sheets « Winners – Admin du site » :
   onglets Formations, Publications et Réglages (clé des tests, bandeau).
   Si le tableau ne répond pas, le site garde la dernière version connue.
   ===================================================================== */
(function () {
  var SHEET = '12iKRmkDdlo7G2UYbGZajUZrnJ0jmcd0LyE1DsFmI1VU';
  var C = window.CENTRE || {};
  var DEF_KEYS = (C.cles) || { rapide: 'WIN2026', placement: 'WIN2026' };
  var n = 0, mem = {};

  function cacheGet(k) { try { return JSON.parse(localStorage.getItem('wec_sh_' + k) || 'null'); } catch (e) { return null; } }
  function cacheSet(k, v) { try { localStorage.setItem('wec_sh_' + k, JSON.stringify(v)); } catch (e) {} }

  /* Lit un onglet : renvoie un tableau de lignes (sans l'en-tête), chaque ligne = tableau de textes */
  function load(name, cb) {
    var cached = cacheGet(name);
    if (cached) { try { cb(cached, true); } catch (e) {} }
    if (mem[name]) { mem[name].push(cb); return; }
    mem[name] = [cb];
    var fn = 'WEC_cb' + (++n), s = document.createElement('script'), done = false;
    window[fn] = function (res) {
      done = true;
      var rows = [];
      try {
        rows = (res.table.rows || []).map(function (r) {
          return (r.c || []).map(function (c) { return c ? String(c.f != null ? c.f : (c.v == null ? '' : c.v)).trim() : ''; });
        }).filter(function (r) { return r.some(function (x) { return x; }); });
      } catch (e) {}
      cacheSet(name, rows);
      (mem[name] || []).forEach(function (f) { try { f(rows, false); } catch (e) {} });
      try { delete window[fn]; } catch (e) { window[fn] = undefined; }
      s.remove();
    };
    s.src = 'https://docs.google.com/spreadsheets/d/' + SHEET + '/gviz/tq?headers=1&sheet=' + encodeURIComponent(name) +
      '&tqx=out:json;responseHandler:' + fn + '&_=' + Math.floor(Date.now() / 300000);
    s.onerror = function () { if (!done && !cached) (mem[name] || []).forEach(function (f) { try { f(null, false); } catch (e) {} }); };
    document.head.appendChild(s);
  }

  var settings = null;
  function readSettings(rows) {
    var o = { rapide: DEF_KEYS.rapide, placement: DEF_KEYS.placement, bandeau: '' };
    (rows || []).forEach(function (r) {
      var k = (r[0] || '').toLowerCase(), v = r[1] || '';
      if (/rapide/.test(k) && v) o.rapide = v;
      else if (/placement/.test(k) && v) o.placement = v;
      else if (/bandeau/.test(k)) o.bandeau = v;
    });
    return o;
  }
  function getSettings(cb) { load('Réglages', function (rows) { if (rows) settings = readSettings(rows); cb(settings || readSettings(null)); }); }

  function normKey(s) { return String(s || '').toUpperCase().replace(/\s+/g, ''); }
  function unlocked(which) { try { return localStorage.getItem('wec_key_' + which) === '1'; } catch (e) { return false; } }
  function keyOk(which, val) {
    var cur = (settings || readSettings(cacheGet('Réglages')))[which] || DEF_KEYS[which];
    return normKey(val) && (normKey(val) === normKey(cur));
  }
  function wa(t) { return 'https://wa.me/' + (C.whatsapp || '2250767037284') + '?text=' + encodeURIComponent(t); }
  var LBL = { rapide: 'test de niveau rapide', placement: 'test de placement' };

  /* Bloc HTML « Clé d'accès » à mettre dans le formulaire du test */
  function keyField(which, style) {
    if (unlocked(which)) return '';
    var msg = "Bonjour Coach Winner ! Je veux passer le " + LBL[which] + " gratuit. Peux-tu m'envoyer la clé d'accès ?";
    return '<div class="wec-key" style="' + (style || '') + 'background:#FFF7E0;border:1px solid #F2B33D;border-radius:12px;padding:12px 14px;margin:10px 0">' +
      '<label for="wec-key-' + which + '" style="display:block;font-weight:700;margin-bottom:6px">🔑 Clé d\'accès au test</label>' +
      '<input id="wec-key-' + which + '" autocomplete="off" autocapitalize="characters" placeholder="Ex : ABC123" style="width:100%;box-sizing:border-box;padding:11px 12px;border:1px solid #d9cfa8;border-radius:10px;font:inherit;text-transform:uppercase">' +
      '<div id="wec-key-err-' + which + '" style="display:none;color:#B83A35;font-size:14px;margin-top:6px">Clé incorrecte. Vérifie-la ou demande-la sur WhatsApp.</div>' +
      '<p style="margin:8px 0 0;font-size:14px">Pas encore de clé ? Elle est <b>gratuite</b> : <a target="_blank" rel="noopener" href="' + wa(msg) + '" style="color:#1f9d55;font-weight:700">demande-la sur WhatsApp</a>.</p></div>';
  }
  /* À appeler au clic sur « Commencer » : renvoie true si on peut démarrer */
  function checkKey(which) {
    if (unlocked(which)) return true;
    var el = document.getElementById('wec-key-' + which), err = document.getElementById('wec-key-err-' + which);
    if (!el) return true;
    if (keyOk(which, el.value)) { try { localStorage.setItem('wec_key_' + which, '1'); } catch (e) {} if (window.wecTrack) window.wecTrack('Lead', { content_name: 'cle_' + which }); return true; }
    if (err) err.style.display = 'block';
    el.focus();
    return false;
  }

  getSettings(function () {});
  window.WEC = { SHEET: SHEET, load: load, settings: getSettings, keyField: keyField, checkKey: checkKey, unlocked: unlocked,
    editUrl: 'https://docs.google.com/spreadsheets/d/' + SHEET + '/edit' };
})();
