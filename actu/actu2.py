from PIL import Image, ImageDraw, ImageFont
W,H=1080,1350
NAVY=(47,52,128); RED=(184,58,53); GOLD=(242,179,61); WHITE=(255,255,255); INK=(27,28,51); BG=(250,247,240); CARD=(236,238,248)
P='/usr/share/fonts/truetype/google-fonts/Poppins-'
F=lambda w,s: ImageFont.truetype(P+w+'.ttf',s)
logo=Image.open('/home/claude/Winners_videos/outils/logo_rond.png').convert('RGBA').resize((120,120))
def fit(d,t,w,s,maxw):
    while d.textlength(t,font=F(w,s))>maxw: s-=2
    return F(w,s)
def c(d,y,t,f,col):
    w=d.textlength(t,font=f); d.text(((W-w)/2,y),t,font=f,fill=col)
def make(name,tag,title1,title2,rows,question):
    im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
    d.rectangle((0,0,W,160),fill=NAVY)
    im.paste(logo,(30,20),logo)
    d.text((175,32),"WINNERS' ENGLISH CENTER",font=F('Bold',40),fill=WHITE)
    d.text((175,86),"L'actu en anglais",font=F('Medium',34),fill=GOLD)
    f=F('Bold',36); tw=d.textlength(tag,font=f)
    d.rounded_rectangle((W/2-tw/2-32,190,W/2+tw/2+32,252),radius=31,fill=RED); c(d,196,tag,f,WHITE)
    c(d,268,title1,fit(d,title1,'Bold',92,980),NAVY); c(d,370,title2,fit(d,title2,'Bold',92,980),RED)
    y=500
    for en,fr in rows:
        d.rounded_rectangle((50,y,1030,y+122),radius=22,fill=CARD)
        d.rectangle((50,y+16,60,y+106),fill=GOLD)
        d.text((88,y+8),en,font=fit(d,en,'Bold',54,910),fill=NAVY)
        d.text((88,y+72),fr,font=fit(d,fr,'Medium',36,910),fill=RED)
        y+=134
    d.rounded_rectangle((40,y+8,1040,y+108),radius=28,fill=GOLD)
    c(d,y+28,question,fit(d,question,'Bold',46,940),INK)
    d.rectangle((0,H-62,W,H),fill=NAVY)
    c(d,H-54,"Coach Winner  •  WhatsApp 07 67 03 72 84",F('Bold',32),WHITE)
    im.save(name,quality=95)
make('yan.jpg','⚽ FOOTBALL'.replace('⚽ ',''),"YAN DIOMANDÉ","BRILLE AU REAL !",
 [("to score a goal","marquer un but"),("an assist","une passe décisive"),("the striker","l'attaquant"),("man of the match","l'homme du match"),("a winger","un ailier")],
 "Comment dit-on « but » en anglais ?")
make('u17.jpg','CAN U17 2027',"LES ÉLÉPHANTEAUX","QUALIFIÉS !",
 [("to qualify","se qualifier"),("the final","la finale"),("to beat Ghana","battre le Ghana"),("the team","l'équipe"),("Well done, boys!","Bravo les gars !")],
 "Écris « Well done! » en commentaire")
make('miss.jpg','MISS GRAND INTERNATIONAL',"PRÉSENTE-TOI","COMME UNE MISS",
 [("My name is…","Je m'appelle…"),("I'm from Côte d'Ivoire","Je viens de Côte d'Ivoire"),("I'm proud to…","Je suis fière de…"),("the runner-up","la dauphine"),("Thank you!","Merci !")],
 "Présente-toi en anglais !")
make('layo.jpg','MUSIQUE',"ROSELINE LAYO","NOUVEL ALBUM !",
 [("an album","un album"),("the release","la sortie"),("a hit","un tube"),("featuring (feat.)","en collaboration avec"),("a fan","un(e) fan")],
 "Ta chanson préférée de Roseline Layo ?")
make('ebinto.jpg','CINÉMA IVOIRIEN',"« ÉBINTO »","AU CINÉMA !",
 [("a movie","un film"),("the main actor","l'acteur principal"),("a novel","un roman"),("the trailer","la bande-annonce"),("to watch a movie","regarder un film")],
 "Tu as lu le livre ? Yes or no ?")
make('type.jpg','ÇA FAIT POLÉMIQUE',"« HE'S NOT","MY TYPE ! »",
 [("He's not my type","Il n'est pas mon genre"),("my husband / my wife","mon mari / ma femme"),("love at first sight","le coup de foudre"),("to fall in love","tomber amoureux"),("It's complicated","C'est compliqué")],
 "Et toi ? « My type is… »")
make('respect.jpg','LE LIVE QUI FAIT PARLER',"PARLER AVEC","RESPECT !",
 [("With all due respect…","Sauf votre respect…"),("I disagree","Je ne suis pas d'accord"),("I apologize","Je m'excuse"),("Let's calm down","Calmons-nous"),("Respect your elders","Respecte tes aînés")],
 "Réponds : « I disagree, but… »")
