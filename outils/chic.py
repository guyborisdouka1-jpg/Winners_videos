from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
FP="/usr/share/fonts/truetype/google-fonts/Poppins-"
def f(w,s): return ImageFont.truetype(FP+w+".ttf",s)
SRC="/home/claude/Winners_videos/chic_salle/"; OUT=SRC+"semaine_13-19/"
W,H=1080,1350; BORD=(128,18,40); GOLD=(232,184,74); WHITE=(255,255,255); DARK=(20,14,18)
def photo(n,h=H):
    im=Image.open(SRC+f"salle_{n}.jpg").convert("RGB"); r=max(W/im.width,h/im.height)
    im=im.resize((int(im.width*r)+1,int(im.height*r)+1)); x=(im.width-W)//2; y=(im.height-h)//2
    return im.crop((x,y,x+W,y+h))
def grad(im,top=0,bottom=1):
    g=Image.new("L",(1,H)); 
    for y in range(H):
        t=y/H; a=0
        if bottom and t>.45: a=int(235*min(1,(t-.45)/.4))
        if top and t<.28: a=max(a,int(200*(1-t/.28)))
        g.putpixel((0,y),a)
    sh=Image.new("RGB",(W,H),DARK); im.paste(sh,(0,0),g.resize((W,H))); return im
def brand(d):
    d.rounded_rectangle((40,40,400,120),20,fill=BORD)
    d.text((220,80),"CHIC SALLE",font=f("Bold",44),fill=GOLD,anchor="mm")
def foot(d):
    d.rectangle((0,H-100,W,H),fill=BORD)
    d.text((W//2,H-50),"📍 Cocody Riviera Palmeraie  •  07 67 03 72 84".replace("📍 ",""),font=f("Bold",36),fill=WHITE,anchor="mm")
def wrap(d,t,fo,mw):
    out=[];l=""
    for w in t.split():
        s=(l+" "+w).strip()
        if d.textlength(s,font=fo)<=mw or not l: l=s
        else: out.append(l); l=w
    return out+[l]
def ctext(d,y,t,fo,fill,mw=960,lh=1.2):
    for i,l in enumerate(wrap(d,t,fo,mw)): d.text((W//2,y+i*int(fo.size*lh)),l,font=fo,fill=fill,anchor="mm")
def chips(d,y,items):
    fo=f("Bold",34); x=60; row=[]
    for it in items:
        w=int(d.textlength(it,font=fo))+50
        if x+w>W-60: y+=80; x=60
        d.rounded_rectangle((x,y,x+w,y+62),31,fill=WHITE); d.text((x+w//2,y+31),it,font=fo,fill=BORD,anchor="mm"); x+=w+16
def save(im,n): im.save(OUT+n,quality=92)

# P1 carrousel découverte (4 slides)
im=grad(photo(1),top=1); d=ImageDraw.Draw(im); brand(d)
ctext(d,920,"Votre salle de formation & réunion",f("Bold",62),WHITE)
ctext(d,1080,"Formations • Masterclass • Réunions • Séminaires",f("Medium",36),GOLD)
d.text((W-60,1180),"Glissez  >>",font=f("Bold",36),fill=WHITE,anchor="rm"); foot(d); save(im,"p1_1.jpg")
im=grad(photo(4)); d=ImageDraw.Draw(im); brand(d)
ctext(d,880,"Format réunion",f("Bold",70),GOLD); ctext(d,975,"Une grande table pour 20 personnes, face à l'écran",f("Medium",38),WHITE,900)
foot(d); save(im,"p1_2.jpg")
im=grad(photo(5)); d=ImageDraw.Draw(im); brand(d)
ctext(d,880,"Format formation",f("Bold",70),GOLD); ctext(d,975,"Disposition en classe, idéale pour vos ateliers et cours",f("Medium",38),WHITE,900)
foot(d); save(im,"p1_3.jpg")
im=Image.new("RGB",(W,H),BORD); d=ImageDraw.Draw(im); brand(d)
d.rounded_rectangle((40,40,400,120),20,fill=DARK); d.text((220,80),"CHIC SALLE",font=f("Bold",44),fill=GOLD,anchor="mm")
ctext(d,240,"Tout est déjà là",f("Bold",72),GOLD)
chips(d,340,["20 places","Climatisation","Wi-Fi","Écran TV","Tableau blanc","Bureau","Coin pause-déjeuner"])
d.rounded_rectangle((90,640,990,1010),40,fill=WHITE)
ctext(d,700,"TARIFS PROMO",f("Bold",44),BORD)
for i,(a,b) in enumerate([("1 heure","7 000 F"),("Demi-journée (5 h)","35 000 F"),("Journée (10 h)","60 000 F")]):
    y=785+i*72; d.text((150,y),a,font=f("Medium",40),fill=DARK,anchor="lm"); d.text((930,y),b,font=f("Bold",44),fill=BORD,anchor="rm")
ctext(d,1110,"Réservez votre date sur WhatsApp",f("Bold",44),WHITE); ctext(d,1180,"07 67 03 72 84",f("Bold",64),GOLD)
save(im,"p1_4.jpg")

# P2 Pour qui
im=grad(photo(7),top=1); d=ImageDraw.Draw(im); brand(d)
ctext(d,700,"Votre prochaine…",f("Medium",46),WHITE)
for i,t in enumerate(["MASTERCLASS","RÉUNION D'ÉQUIPE","FORMATION","SESSION D'ENTRETIENS"]):
    ctext(d,790+i*80,t,f("Bold",62),GOLD)
ctext(d,1150,"…se passe ici.",f("Bold",54),WHITE); foot(d); save(im,"p2.jpg")

# P3 tarifs
im=grad(photo(3),top=1); d=ImageDraw.Draw(im); brand(d)
d.rounded_rectangle((70,560,1010,1180),44,fill=WHITE)
ctext(d,640,"Combien ça coûte ?",f("Bold",58),BORD)
for i,(a,b) in enumerate([("1 heure","7 000 F"),("Demi-journée (5 h)","35 000 F"),("Journée (10 h)","60 000 F")]):
    y=770+i*110; d.line((130,y+52,950,y+52),fill=(235,225,228),width=3)
    d.text((130,y),a,font=f("Medium",46),fill=DARK,anchor="lm"); d.text((950,y),b,font=f("Bold",54),fill=BORD,anchor="rm")
ctext(d,1125,"Tarifs promo • climatisation et Wi-Fi inclus",f("Medium",32),(110,90,95))
foot(d); save(im,"p3.jpg")

# P4 fin d'année
im=grad(photo(6),top=1); d=ImageDraw.Draw(im); brand(d)
ctext(d,840,"Formation ou séminaire de fin d'année ?",f("Bold",64),WHITE,920)
ctext(d,1030,"Bloquez votre date dès maintenant",f("Bold",46),GOLD)
d.rounded_rectangle((240,1105,840,1195),45,fill=GOLD); d.text((540,1150),"WhatsApp : 07 67 03 72 84",font=f("Bold",38),fill=DARK,anchor="mm")
foot(d); save(im,"p4.jpg")
print("ok")
