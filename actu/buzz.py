from PIL import Image, ImageDraw, ImageFont
W,H=1080,1350
NAVY=(47,52,128); RED=(184,58,53); GOLD=(242,179,61); WHITE=(255,255,255); INK=(27,28,51)
P='/usr/share/fonts/truetype/google-fonts/Poppins-'
F=lambda w,s: ImageFont.truetype(P+w+'.ttf',s)
logo=Image.open('/home/claude/Winners_videos/outils/logo_rond.png').convert('RGBA').resize((150,150))
def c(d,y,t,f,col):
    w=d.textlength(t,font=f); d.text(((W-w)/2,y),t,font=f,fill=col)
def make(name,emoji_tag,title1,title2,subtitle,rows,question):
    im=Image.new('RGB',(W,H),NAVY); d=ImageDraw.Draw(im)
    for i in range(0,W,60): d.line([(i,0),(i-400,H)],fill=(52,58,140),width=18)
    im.paste(logo,(40,36),logo)
    d.text((210,60),"WINNERS' ENGLISH CENTER",font=F('Bold',34),fill=WHITE)
    d.text((210,106),"L'actu en anglais 🇬🇧".replace(' 🇬🇧',''),font=F('Medium',30),fill=GOLD)
    d.rounded_rectangle((60,215,1020,255+0),radius=0,fill=NAVY)
    tw=d.textlength(emoji_tag,font=F('Bold',30)); d.rounded_rectangle((W/2-tw/2-30,215,W/2+tw/2+30,265),radius=25,fill=RED); c(d,219,emoji_tag,F('Bold',30),WHITE)
    c(d,290,title1,F('Bold',74),WHITE); c(d,380,title2,F('Bold',74),GOLD)
    c(d,480,subtitle,F('MediumItalic',34),(220,224,255))
    y=560
    for en,fr in rows:
        d.rounded_rectangle((80,y,1000,y+92),radius=24,fill=WHITE)
        fe=44; ff=34
        while d.textlength(en,font=F('Bold',fe))+d.textlength(fr,font=F('Medium',ff))>820: fe-=2; ff-=1
        d.text((115,y+46-fe*0.68),en,font=F('Bold',fe),fill=NAVY)
        w=d.textlength(fr,font=F('Medium',ff)); d.text((965-w,y+46-ff*0.62),fr,font=F('Medium',ff),fill=RED)
        y+=110
    d.rounded_rectangle((60,y+15,1020,y+120),radius=30,fill=GOLD)
    c(d,y+40,question,F('Bold',40),INK)
    c(d,H-70,"Coach Winner  •  WhatsApp 07 67 03 72 84",F('Medium',30),WHITE)
    im.save(name,quality=93)
make('type.jpg','ÇA FAIT POLÉMIQUE',"« HE'S NOT","MY TYPE ! »","« Il n'est pas mon genre »… en anglais",
 [("He's not my type","Il n'est pas mon genre"),("my husband / my wife","mon mari / ma femme"),("love at first sight","le coup de foudre"),("to fall in love","tomber amoureux"),("It's complicated","C'est compliqué")],
 "Et toi ? « My type is… »")
make('respect.jpg','LE LIVE QUI FAIT PARLER',"PARLER AVEC","RESPECT !","On peut ne pas être d'accord… avec respect",
 [("With all due respect…","Sauf votre respect…"),("I disagree","Je ne suis pas d'accord"),("I apologize","Je m'excuse"),("Let's calm down","Calmons-nous"),("Respect your elders","Respecte tes aînés")],
 "Réponds : « I disagree, but… »")
