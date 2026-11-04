import base64,json,sys
from playwright.sync_api import sync_playwright
exec(open('content.py').read())
logo='data:image/png;base64,'+base64.b64encode(open('logo.png','rb').read()).decode()
CSS='''@page{size:A4;margin:0}*{box-sizing:border-box}body{margin:0;font-family:Inter,sans-serif;color:#1B1C33;font-size:10.3pt}
.pg{width:210mm;height:297mm;padding:10mm 13mm;position:relative;overflow:hidden;page-break-after:always}
.band{background:#2F3480;color:#fff;margin:-10mm -13mm 6mm;padding:9mm 13mm 8mm;display:flex;align-items:center;gap:14px}
.band img{width:24mm;border-radius:50%;background:#fff}.band .k{display:inline-block;background:#F2B33D;color:#1B1C33;font-weight:900;padding:3px 11px;border-radius:20px;font-size:9.5pt}
.band h1{margin:4px 0 0;font-size:27pt;line-height:1;font-weight:900}.band h1 em{color:#F2B33D;font-style:normal;display:block;font-size:15pt;margin-top:4px}
.band .by{margin-left:auto;text-align:right;font-size:9pt;opacity:.9}
.hd{display:flex;align-items:center;gap:10px;border-bottom:3px solid #F2B33D;padding-bottom:5px;margin-bottom:4px}.hd img{width:30px}.hd b{color:#2F3480}.hd span{margin-left:auto;color:#B83A35;font-weight:700;font-size:9pt}
h2{color:#2F3480;font-size:13pt;margin:8px 0 4px}p{margin:4px 0}
table{width:100%;border-collapse:collapse}td,th{padding:4.5px 6px;border-bottom:1px solid #e6e2d6;vertical-align:top;text-align:left}
td.n{width:8mm;color:#fff;background:#2F3480;text-align:center;font-weight:800}td b{font-size:11pt}
.pr{display:block;color:#B83A35;font-size:9pt}td.fr{width:55mm;color:#4a5068}.fr2{display:block;color:#4a5068;font-size:9.3pt}
.ex{display:block;color:#4a5068;font-size:9.3pt;font-style:italic}.bad{display:block;color:#B83A35;text-decoration:line-through}.good{display:block;font-weight:800;color:#17663a;font-size:11.5pt}
.err td{padding:7px 6px}.who{width:18mm;font-weight:800;color:#2F3480}.vb th{background:#F2B33D;color:#1B1C33}.vb td{padding:3.6px 6px}
.voc{display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px}.voc div{border:1px solid #e6e2d6;border-radius:8px;padding:5px 7px}.voc .e{float:right;font-size:15pt}.voc b{display:block;font-size:11pt}.voc .fr{display:block;color:#4a5068;font-size:9pt}
.ex2{background:#f1f2ff;border-radius:8px;padding:8px 10px;margin:4px 0;font-size:11pt}
.tip{background:#FFF7E0;border-left:5px solid #F2B33D;padding:7px 11px;border-radius:6px;margin:4px 0 6px;font-size:9.6pt}.mu{color:#5b6478;font-size:9pt}
.promo{position:absolute;left:13mm;right:13mm;bottom:10mm;background:#2F3480;color:#fff;border-radius:12px;padding:10px 14px;display:grid;grid-template-columns:1.25fr 1fr;gap:10px;font-size:9.6pt}
.promo h3{margin:0 0 4px;color:#F2B33D;font-size:12.5pt}.promo ul{margin:0;padding-left:15px}.promo li{margin:1px 0}.promo .c{background:#B83A35;border-radius:9px;padding:8px 10px;line-height:1.55;font-weight:700}.promo a{color:#FFE08A}
'''
def html(d):
    promo=f'''<div class="promo"><div><h3>🚀 Passe à l'étape suivante !</h3>Lire, c'est bien. <b>Oser parler</b> avec un coach, c'est ce qui change tout :<ul>
<li>👥 Cours en petit groupe, au centre ou en ligne</li><li>🗣️ Speaking Weekend chaque samedi soir</li><li>🏠 Cours à domicile et cours privés</li></ul></div>
<div class="c">🎯 Test de niveau gratuit :<br><a href="https://winnersenglishcenter.com/appli/">winnersenglishcenter.com/appli</a><br>🌐 <a href="https://winnersenglishcenter.com">winnersenglishcenter.com</a><br>💬 <a href="https://wa.me/2250767037284">WhatsApp 07 67 03 72 84</a></div></div>'''
    return f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet"><style>{CSS}</style></head><body>
<div class="pg"><div class="band"><img src="{logo}"><div><span class="k">🎁 PDF GRATUIT</span><h1>{d['emoji']} {d['title']}<em>{d['sub']}</em></h1></div><div class="by">par <b>Coach Winner</b><br>Winners' English Center</div></div>
<div class="ct"><div class="tip">💡 {d['tip']}</div>{d['p1']}</div></div>
<div class="pg"><div class="hd"><img src="{logo}"><b>Winners' English Center</b><span>{d['title']}</span></div><div class="ct">{d['p2']}</div>{promo}</div></body></html>'''
idx=[]
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":794,"height":1123})
    for d in D:
        open(d['slug']+'.html','w').write(html(d))
        pg.goto('file://'+__import__('os').path.abspath(d['slug']+'.html')); pg.wait_for_timeout(900)
        js='''()=>{const out=[];document.querySelectorAll('.pg').forEach(p=>{const c=p.querySelector('.ct');const lim=()=>(p.querySelector('.promo')?p.querySelector('.promo').getBoundingClientRect().top:p.getBoundingClientRect().bottom)-14;let z=1.8;c.style.zoom=z;while(z>1&&c.getBoundingClientRect().bottom>lim()){z=Math.round((z-0.05)*100)/100;c.style.zoom=z;}out.push(z);});return out;}'''
        print(d['slug'],'zoom',pg.evaluate(js))
        ov=pg.evaluate("[...document.querySelectorAll('.pg')].map(p=>{const pr=p.querySelector('.promo');const kids=[...p.children].filter(c=>!c.classList.contains('promo'));const last=kids[kids.length-1].getBoundingClientRect().bottom-p.getBoundingClientRect().top;return Math.round(last)+'/'+Math.round(pr?pr.getBoundingClientRect().top-p.getBoundingClientRect().top:p.getBoundingClientRect().height)})")
        print(d['slug'],ov)
        pg.pdf(path=d['slug']+'.pdf',format='A4',print_background=True,prefer_css_page_size=True)
        idx.append({k:d[k] for k in ('slug','date','title','sub','emoji')})
    b.close()
json.dump(idx,open('index.json','w'),ensure_ascii=False,indent=1)
