import json,asyncio,os
from playwright.async_api import async_playwright
B={
'25-phrases-quotidien':("25 phrases d'anglais","pour parler au quotidien",["🗣️ Saluer, se présenter","💼 Au travail","✈️ En voyage","🔊 Prononciation en français"]),
'10-erreurs-francophones':("Les 10 erreurs","que font tous les francophones",["❌ « I have 25 years »","❌ « I am agree »","✅ Les bonnes phrases","💡 Expliqué simplement"]),
'40-mots-bureau':("40 mots d'anglais","indispensables au bureau",["📧 Email, meeting…","🧾 Facture, client…","🎯 Objectif, équipe…","🔊 Prononciation en français"]),
'present-simple-continuous':("I eat ou I'm eating ?","la mini-leçon pour ne plus confondre",["📘 La règle en 2 minutes","🔎 Exemples simples","✍️ Exercice + réponses","🎯 Fini les erreurs"]),
'dialogue-restaurant':("Au restaurant","un dialogue complet en anglais",["🍽️ Commander un plat","🥤 Demander à boire","🧾 Demander l'addition","🔊 Prononciation en français"]),
'30-verbes-irreguliers':("30 verbes irréguliers","les plus utilisés en anglais",["🔁 go – went – gone","📋 Tableau clair","🇫🇷 Traduction","✍️ Petit exercice"]),
'15-expressions-natifs':("15 expressions anglaises","que les natifs adorent",["🍰 « A piece of cake »","🧊 « Break the ice »","🌙 « Once in a blue moon »","🔊 Prononciation en français"]),
"quiz-20-questions":("Quiz : quel est ton niveau ?","20 questions pour te tester",["🎯 20 questions A, B, C","✅ Les réponses","📊 Ton niveau à la fin","💪 Débutant à avancé"]),
'15-faux-amis':("15 faux amis","les mots anglais qui te piègent",["⚠️ « Actually » ≠ actuellement","📚 « Library » ≠ librairie","✅ Le vrai sens","🔊 Prononciation en français"]),
'in-on-at':("IN, ON ou AT ?","la mini-leçon des prépositions",["⏰ Pour le temps","📍 Pour le lieu","🔺 L'astuce de la pyramide","✍️ Exercice + réponses"]),
'dialogue-aeroport':("À l'aéroport","un dialogue complet en anglais",["✈️ L'enregistrement","🧳 Les bagages","🎫 La carte d'embarquement","🔊 Prononciation en français"]),
'email-professionnel':("Écrire un email pro","en anglais, avec le modèle",["📧 Le modèle à copier","🧩 Les 3 parties","💬 9 phrases utiles","✍️ À toi d'écrire"]),
'20-phrasal-verbs':("20 phrasal verbs","indispensables au quotidien",["🔗 get up, give up…","💬 Un exemple pour chacun","🇫🇷 Traduction","🔊 Prononciation en français"]),
'telephone-anglais':("Au téléphone","16 phrases pour appeler en anglais",["📞 Se présenter","⏳ « Hold on, please »","📝 Prendre un message","🔊 Prononciation en français"]),
}
import sys
NEW=sys.argv[1:] or list(B)
T=open('visuel_template.html').read()
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1080,'height':1350})
        for s,(t1,t2,li) in [(k,v) for k,v in B.items() if k in NEW]:
            h=T
            import re
            h=re.sub(r'<h1>.*?</h1>',f'<h1>{t1}<br><em>{t2}</em></h1>',h,flags=re.S)
            h=re.sub(r'<div class="cv">.*?</div><div class="pages">',f'<div class="cv" style="padding:0"><img src="cov-{s}.jpg" style="width:100%;height:100%;object-fit:cover;object-position:top;border-radius:0"></div><div class="pages">',h,flags=re.S)
            h=re.sub(r'<ul>.*?</ul>','<ul>'+''.join(f'<li>{x}</li>' for x in li)+'</ul>',h,flags=re.S)
            h=h.replace('src="logo.png"','src="logo.png"')
            if len(t1)>20: h=h.replace('h1{font-size:76px','h1{font-size:66px')
            open(f'v-{s}.html','w').write(h)
            await pg.goto('file://'+os.path.abspath(f'v-{s}.html')); await pg.wait_for_timeout(900)
            await pg.screenshot(path=f'visuel-{s}.jpg',type='jpeg',quality=90)
        await b.close()
asyncio.run(main())
