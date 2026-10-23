/* =====================================================================
   WINNERS' ENGLISH CENTER : SUIVI DES CAMPAGNES PUBLICITAIRES
   - Retient d'où vient le visiteur (pub Facebook, TikTok, campagne…)
   - Ajoute une référence courte aux messages WhatsApp / email
   - Envoie les conversions au Pixel Meta quand CENTRE.metaPixel est rempli
   ===================================================================== */
(function () {
  var C = window.CENTRE || {};
  var store = {};
  try { store = JSON.parse(sessionStorage.getItem('wec_src') || '{}'); } catch (e) {}
  var qs = new URLSearchParams(location.search);
  var hash = (location.hash || '').replace(/^#/, '');
  if (qs.get('utm_source') || qs.get('utm_campaign') || qs.get('fbclid') || qs.get('ttclid')) {
    store = {
      source: qs.get('utm_source') || (qs.get('fbclid') ? 'facebook' : qs.get('ttclid') ? 'tiktok' : ''),
      campagne: qs.get('utm_campaign') || '',
      annonce: qs.get('utm_content') || '',
      page: hash || location.pathname.split('/').filter(Boolean).pop() || 'accueil'
    };
    try { sessionStorage.setItem('wec_src', JSON.stringify(store)); } catch (e) {}
  }
  window.WEC_SRC = store;

  function ref() {
    if (!store.source && !store.campagne) return '';
    var r = [store.source, store.campagne, store.annonce].filter(Boolean).join(' / ');
    return r ? '\n\n(Réf. : ' + r + ')' : '';
  }

  /* ---------- Pixel Meta ---------- */
  var PX = (C.metaPixel || '').replace(/\D/g, '');
  function track(ev, data) {
    try { if (window.fbq) window.fbq('track', ev, data || {}); } catch (e) {}
  }
  window.wecTrack = track;
  if (PX) {
    !function (f, b, e, v, n, t, s) { if (f.fbq) return; n = f.fbq = function () { n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments); }; if (!f._fbq) f._fbq = n; n.push = n; n.loaded = !0; n.version = '2.0'; n.queue = []; t = b.createElement(e); t.async = !0; t.src = v; s = b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t, s); }(window, document, 'script', 'https://connect.facebook.net/en_US/fbevents.js');
    window.fbq('init', PX);
    window.fbq('track', 'PageView');
    if (hash && hash !== 'top') track('ViewContent', { content_name: hash });
  }

  /* ---------- Clics WhatsApp / email = prospects ---------- */
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a) return;
    var h = a.getAttribute('href') || '';
    var isWa = /wa\.me\/|api\.whatsapp\.com/.test(h), isMail = /^mailto:/i.test(h);
    if (!isWa && !isMail) return;
    var r = ref();
    if (r && !a.dataset.ref) {
      try {
        if (isWa) {
          var u = new URL(h, location.href), t = u.searchParams.get('text') || '';
          u.searchParams.set('text', t + r); a.href = u.toString().replace(/\+/g, '%20');
        } else {
          a.href = /[?&]body=/.test(h) ? h.replace(/([?&]body=)([^&]*)/, function (m, p, b) { return p + b + encodeURIComponent(r); }) : h + (h.indexOf('?') < 0 ? '?' : '&') + 'body=' + encodeURIComponent(r);
        }
        a.dataset.ref = '1';
      } catch (err) {}
    }
    track(isWa ? 'Contact' : 'Lead', { content_name: (document.title || '') + (hash ? ' #' + hash : ''), method: isWa ? 'whatsapp' : 'email' });
  }, true);
})();
