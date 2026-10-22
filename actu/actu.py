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
make('yan.jpg','FOOTBALL',"YAN DIOMANDÉ","BRILLE AU REAL !","Parle foot comme un pro… en anglais ⚽".replace(' ⚽',''),
 [("to score a goal","marquer un but"),("an assist","une passe décisive"),("the striker","l'attaquant"),("man of the match","homme du match"),("a winger","un ailier")],
 "Comment dit-on « but » en anglais ?")
make('u17.jpg','CAN U17 2027',"LES ÉLÉPHANTEAUX","QUALIFIÉS !","Commente le match en anglais 🐘".replace(' 🐘',''),
 [("to qualify","se qualifier"),("the final","la finale"),("to beat Ghana","battre le Ghana"),("the team","l'équipe"),("Well done, boys!","Bravo les gars !")],
 "Écris « Well done! » en commentaire 🐘".replace(' 🐘',''))
make('miss.jpg','MISS GRAND INTERNATIONAL',"PRÉSENTE-TOI","COMME UNE MISS","Bravo Marlène Kany Kouassi, 5e dauphine !",
 [("My name is…","Je m'appelle…"),("I'm from Côte d'Ivoire","Je viens de Côte d'Ivoire"),("I'm proud to…","Je suis fière de…"),("the runner-up","la dauphine"),("Thank you!","Merci !")],
 "Présente-toi en anglais en commentaire !")
make('layo.jpg','MUSIQUE',"ROSELINE LAYO","NOUVEL ALBUM !","« Divas », attendu le 27 novembre 🎤".replace(' 🎤',''),
 [("an album","un album"),("the release","la sortie"),("a hit","un tube"),("featuring (feat.)","en collaboration avec"),("a fan","un(e) fan")],
 "Ta chanson préférée de Roseline Layo ?")
make('ebinto.jpg','CINÉMA IVOIRIEN',"« ÉBINTO »","AU CINÉMA !","Le roman d'Amadou Koné devient un film 🎬".replace(' 🎬',''),
 [("a movie","un film"),("the main actor","l'acteur principal"),("a novel","un roman"),("the trailer","la bande-annonce"),("to watch a movie","regarder un film")],
 "Tu as lu le livre ? Yes or no ?")
