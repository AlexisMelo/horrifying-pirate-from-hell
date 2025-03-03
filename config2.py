#from PIL import ImageTk
from tkinter import*
import os
conf=Tk()

canvas= Canvas(conf,width=500,height=700)
canvas.pack()

Nom1=StringVar()
Nom2=StringVar()
Nom3=StringVar()
Nom4=StringVar()

def Augmenter(Joueurs):
    global Nbjoueurs
    Nbjoueurs=Nbjoueurs+1
    
    if Nbjoueurs==2:
        canvas.create_image(250,400,image=chiffre2)
        canvas.create_image(250,130,image=joueur_2)
    elif Nbjoueurs==3:       
        canvas.create_image(250,400,image=chiffre3)
        canvas.create_image(250,130,image=joueur_3)
    elif Nbjoueurs==4:      
        canvas.create_image(250,400,image=chiffre4)
        canvas.create_image(250,130,image=joueur_4)
    else:
        canvas.create_image(250,400,image=chiffre1)
        canvas.create_image(250,130,image=joueur_1)
        Nbjoueurs=1
        
    return Nbjoueurs

def Diminuer(Joueurs):
    global Nbjoueurs
    Nbjoueurs=Nbjoueurs-1
    
    if Nbjoueurs==1:
        canvas.create_image(250,400,image=chiffre1)
        canvas.create_image(250,130,image=joueur_1)
    elif Nbjoueurs==2:       
        canvas.create_image(250,400,image=chiffre2)
        canvas.create_image(250,130,image=joueur_2)
    elif Nbjoueurs==3:      
        canvas.create_image(250,400,image=chiffre3)
        canvas.create_image(250,130,image=joueur_3)
    else:
        canvas.create_image(250,400,image=chiffre4)
        canvas.create_image(250,130,image=joueur_4)
        Nbjoueurs=4
        
    return Nbjoueurs

def Quitter(teub):
    conf.destroy()

def MainMenu(Menuprincipal):
    conf.destroy()
    os.system("MenuPrincipal.py")
    
    
def Enter(config2):
    global Nbjoueurs
    canvas.delete("all")
    canvas.create_image(0,0,image=Fond)
    canvas.create_image(255,50,image=Titre)
    canvas.create_image(250,110,image=Names)
    canvas.create_image(250,660,image=Start,tag="STAR")
    canvas.tag_bind("STAR","<Button-1>",start)
    canvas.create_image(80,670,image=Back,tag="BAK")
    canvas.create_image(420,670,image=Exit,tag="EXI")
    canvas.tag_bind("BAK","<Button-1>",back)
    if Nbjoueurs==1:
        config1joueur()
    elif Nbjoueurs==2:
        config2joueur()
    elif Nbjoueurs==3:
        config3joueur()
    else:
        config4joueur()

    return Nbjoueurs

def start(jeu):
    conf.destroy()
    names=open("names.txt","w")
    names.write(Nom1.get()+"\n")
    names.write(Nom2.get()+"\n")
    names.write(Nom3.get()+"\n")
    names.write(Nom4.get())
    names.close()
    colors=open("colors.txt","w")
    if Nbjoueurs==1:
        colors.write(str(colorJ1)+"\n")
    elif Nbjoueurs==2:
        colors.write(str(colorJ1)+"\n")
        colors.write(str(colorJ2)+"\n")
    elif Nbjoueurs==3:
        colors.write(str(colorJ1)+"\n")
        colors.write(str(colorJ2)+"\n")
        colors.write(str(colorJ3)+"\n")
    else:
        colors.write(str(colorJ1)+"\n")
        colors.write(str(colorJ2)+"\n")
        colors.write(str(colorJ3)+"\n")
        colors.write(str(colorJ4))
    colors.close()
    Participants=open("Nombre.txt","w")
    Participants.write(str(Nbjoueurs))
    Participants.close()
    os.system("Plateau de jeu.py")
    
def config1joueur():
    global Nom1
    canvas.create_image(400,400,image=red)
    canvas.create_image(170,370,image=PL1R)
    canvas.create_image(470,400,image=fdroit,tag="1JflJ1")
    canvas.tag_bind("1JflJ1","<Button-1>",Swap1JJ1)
    nom1=Entry(canvas,textvariable=Nom1,fg="white",width=40,bg="black",bd=10,justify=CENTER)
    canvas.create_window(160,420,window=nom1)

def Swap1JJ1(SWAPJ1):
    global colorJ1
    colorJ1=colorJ1+1
    if colorJ1==2:
        canvas.create_image(400,400,image=blue)
        canvas.create_image(170,370,image=PL1B)
    elif colorJ1==3:
        canvas.create_image(400,400,image=yellow)
        canvas.create_image(170,370,image=PL1J)
    elif colorJ1==4:
        canvas.create_image(400,400,image=green)
        canvas.create_image(170,370,image=PL1V)
    else:
        colorJ1=1
        canvas.create_image(400,400,image=red)
        canvas.create_image(170,370,image=PL1R)

def config2joueur():
    canvas.create_image(400,250,image=red)
    canvas.create_image(170,220,image=PL1R)
    canvas.create_image(470,250,image=fdroit,tag="2JflJ1")
    canvas.tag_bind("2JflJ1","<Button-1>",Swap2JJ1)
    nom1=Entry(canvas,textvariable=Nom1,fg="white",width=40,bg="black",bd=10,justify=CENTER)
    canvas.create_window(160,270,window=nom1)

    canvas.create_image(90,450,image=blue)
    canvas.create_image(340,420,image=PL2B)
    canvas.create_image(20,450,image=fgauch,tag="2JflJ2")
    canvas.tag_bind("2JflJ2","<Button-1>",Swap2JJ2)
    nom2=Entry(canvas,textvariable=Nom2,fg="white",width=40,bg="black",bd=10,justify=CENTER)
    canvas.create_window(330,470,window=nom2)

def Swap2JJ1(SWAPJ1):
    global colorJ1
    colorJ1=colorJ1+1
    if colorJ1==2:
        canvas.create_image(400,250,image=blue)
        canvas.create_image(170,220,image=PL1B)
    elif colorJ1==3:
        canvas.create_image(400,250,image=yellow)
        canvas.create_image(170,220,image=PL1J)
    elif colorJ1==4:
        canvas.create_image(400,250,image=green)
        canvas.create_image(170,220,image=PL1V)
    else:
        colorJ1=1
        canvas.create_image(400,250,image=red)
        canvas.create_image(170,220,image=PL1R)

def Swap2JJ2(SWAPJ2):
    global colorJ2
    colorJ2=colorJ2+1
    if colorJ2==2:
        canvas.create_image(90,450,image=blue)
        canvas.create_image(340,420,image=PL2B)
    elif colorJ2==3:
        canvas.create_image(90,450,image=yellow)
        canvas.create_image(340,420,image=PL2J)
    elif colorJ2==4:
        canvas.create_image(90,450,image=green)
        canvas.create_image(340,420,image=PL2V)
    else:
        colorJ2=1
        canvas.create_image(90,450,image=red)
        canvas.create_image(340,420,image=PL2R)

def config3joueur():
    canvas.create_image(400,230,image=red)
    canvas.create_image(170,200,image=PL1R)
    canvas.create_image(470,230,image=fdroit,tag="3JflJ1")
    canvas.tag_bind("3JflJ1","<Button-1>",Swap3JJ1)
    nom1=Entry(canvas,textvariable=Nom1,fg="white",width=40,bg="black",bd=10,justify=CENTER)
    canvas.create_window(160,250,window=nom1)

    canvas.create_image(90,380,image=blue)
    canvas.create_image(340,350,image=PL2B)
    canvas.create_image(20,380,image=fgauch,tag="3JflJ2")
    canvas.tag_bind("3JflJ2","<Button-1>",Swap3JJ2)
    nom2=Entry(canvas,textvariable=Nom2,fg="white",width=40,bg="black",bd=10,justify=CENTER)
    canvas.create_window(330,400,window=nom2)

    canvas.create_image(400,530,image=green)
    canvas.create_image(170,500,image=PL3V)
    canvas.create_image(470,530,image=fdroit,tag="3JflJ3")
    canvas.tag_bind("3JflJ3","<Button-1>",Swap3JJ3)
    nom3=Entry(canvas,textvariable=Nom3,fg="white",width=40,bg="black",bd=10,justify=CENTER)
    canvas.create_window(160,550,window=nom3)

def Swap3JJ1(SWAPJ1):
    global colorJ1
    colorJ1=colorJ1+1
    if colorJ1==2:
        canvas.create_image(400,230,image=blue)
        canvas.create_image(170,200,image=PL1B)
    elif colorJ1==3:
        canvas.create_image(400,230,image=yellow)
        canvas.create_image(170,200,image=PL1J)
    elif colorJ1==4:
        canvas.create_image(400,230,image=green)
        canvas.create_image(170,200,image=PL1V)
    else:
        colorJ1=1
        canvas.create_image(400,230,image=red)
        canvas.create_image(170,200,image=PL1R)

def Swap3JJ2(SWAPJ2):
    global colorJ2
    colorJ2=colorJ2+1
    if colorJ2==2:
        canvas.create_image(90,380,image=blue)
        canvas.create_image(340,350,image=PL2B)
    elif colorJ2==3:
        canvas.create_image(90,380,image=yellow)
        canvas.create_image(340,350,image=PL2J)
    elif colorJ2==4:
        canvas.create_image(90,380,image=green)
        canvas.create_image(340,350,image=PL2V)
    else:
        colorJ2=1
        canvas.create_image(90,380,image=red)
        canvas.create_image(340,350,image=PL2R)

def Swap3JJ3(SWAPJ3):
    global colorJ3
    colorJ3=colorJ3+1
    if colorJ3==2:
        canvas.create_image(400,530,image=blue)
        canvas.create_image(170,500,image=PL3B)
    elif colorJ3==3:
        canvas.create_image(400,530,image=yellow)
        canvas.create_image(170,500,image=PL3J)
    elif colorJ3==4:
        canvas.create_image(400,530,image=green)
        canvas.create_image(170,500,image=PL3V)
    else:
        colorJ3=1
        canvas.create_image(400,530,image=red)
        canvas.create_image(170,500,image=PL3R)
    
def config4joueur():

    canvas.create_image(410,200,image=red)
    canvas.create_image(170,170,image=PL1R)
    canvas.create_image(480,200,image=fdroit,tag="4JflJ1")
    canvas.tag_bind("4JflJ1","<Button-1>",Swap4JJ1)
    nom1=Entry(canvas,textvariable=Nom1,fg="white",width=40,bg="black",bd=10,justify=CENTER)
    canvas.create_window(160,220,window=nom1)

    canvas.create_image(90,320,image=blue)
    canvas.create_image(340,290,image=PL2B)
    canvas.create_image(20,320,image=fgauch,tag="4JflJ2")
    canvas.tag_bind("4JflJ2","<Button-1>",Swap4JJ2)
    nom2=Entry(canvas,textvariable=Nom2,fg="white",width=40,bg="black",bd=10,justify=CENTER)
    canvas.create_window(330,340,window=nom2)
    
    canvas.create_image(410,440,image=green)
    canvas.create_image(170,410,image=PL3V)
    canvas.create_image(480,440,image=fdroit,tag="4JflJ3")
    canvas.tag_bind("4JflJ3","<Button-1>",Swap4JJ3)
    nom3=Entry(canvas,textvariable=Nom3,fg="white",width=40,bg="black",bd=10,justify=CENTER)
    canvas.create_window(160,460,window=nom3)
 
    canvas.create_image(90,560,image=yellow)
    canvas.create_image(340,530,image=PL4J)
    canvas.create_image(20,560,image=fgauch,tag="4JflJ4")
    canvas.tag_bind("4JflJ4","<Button-1>",Swap4JJ4)
    nom3=Entry(canvas,textvariable=Nom4,fg="white",width=40,bg="black",bd=10,justify=CENTER)
    canvas.create_window(330,580,window=nom3)
    
def Swap4JJ1(SWAPJ1):
    global colorJ1
    colorJ1=colorJ1+1
    if colorJ1==2:
        canvas.create_image(410,200,image=blue)
        canvas.create_image(170,170,image=PL1B)
    elif colorJ1==3:
        canvas.create_image(410,200,image=yellow)
        canvas.create_image(170,170,image=PL1J)
    elif colorJ1==4:
        canvas.create_image(410,200,image=green)
        canvas.create_image(170,170,image=PL1V)
    else:
        colorJ1=1
        canvas.create_image(410,200,image=red)
        canvas.create_image(170,170,image=PL1R)

def Swap4JJ2(SWAPJ2):
    global colorJ2
    colorJ2=colorJ2+1
    if colorJ2==2:
        canvas.create_image(90,320,image=blue)
        canvas.create_image(340,290,image=PL2B)
    elif colorJ2==3:
        canvas.create_image(90,320,image=yellow)
        canvas.create_image(340,290,image=PL2J)
    elif colorJ2==4:
        canvas.create_image(90,320,image=green)
        canvas.create_image(340,290,image=PL2V)
    else:
        colorJ2=1
        canvas.create_image(90,320,image=red)
        canvas.create_image(340,290,image=PL2R)

def Swap4JJ3(SWAPJ3):
    global colorJ3
    colorJ3=colorJ3+1
    if colorJ3==2:
        canvas.create_image(410,440,image=blue)
        canvas.create_image(170,410,image=PL3B)
    elif colorJ3==3:
        canvas.create_image(410,440,image=yellow)
        canvas.create_image(170,410,image=PL3J)
    elif colorJ3==4:
        canvas.create_image(410,440,image=green)
        canvas.create_image(170,410,image=PL3V)
    else:
        colorJ3=1
        canvas.create_image(410,440,image=red)
        canvas.create_image(170,410,image=PL3R)

def Swap4JJ4(SWAPJ4):
    global colorJ4
    colorJ4=colorJ4+1
    if colorJ4==2:
        canvas.create_image(90,560,image=blue)
        canvas.create_image(340,530,image=PL4B)
    elif colorJ4==3:
        canvas.create_image(90,560,image=yellow)
        canvas.create_image(340,530,image=PL4J)
    elif colorJ4==4:
        canvas.create_image(90,560,image=green)
        canvas.create_image(340,530,image=PL4V)
    else:
        colorJ4=1
        canvas.create_image(90,560,image=red)
        canvas.create_image(340,530,image=PL4R)


    
def back(config1):
    global colorJ1
    global Nbjoueurs
    canvas.delete("all")
    canvas.create_image(0,0,image=Fond)
    canvas.create_image(255,50,image=Titre)
    canvas.create_image(250,200,image=Number)
    canvas.create_image(250,650,image=Valider,tag="Valid")
    canvas.create_image(250,300,image=flechehaut,tag="KEK")
    canvas.create_image(250,500,image=flechebas,tag="KEK1")
    canvas.create_image(250,400,image=chiffre1)
    canvas.create_image(250,130,image=joueur_1)
    canvas.create_image(65,670,image=Menu,tag="MEN")
    canvas.create_image(435,670,image=Exit,tag="EXI")
    colorJ1=1
    colorJ2=2
    colorJ3=3
    colorj4=4
    Nbjoueurs=1
    
Nbjoueurs=1
colorJ1=1
colorJ2=2
colorJ3=3
colorJ4=4                        

#images#

flechehaut=PhotoImage(file="arrowtop.gif")
flechebas=PhotoImage(file="arrowbot.gif")
chiffre1=PhotoImage(file="chiffre1.gif")
chiffre2=PhotoImage(file="chiffre2.gif")
chiffre3=PhotoImage(file="chiffre3.gif")
chiffre4=PhotoImage(file="chiffre4.gif")
joueur_1=PhotoImage(file="1player.gif")
joueur_2=PhotoImage(file="2player.gif")
joueur_3=PhotoImage(file="3player.gif")
joueur_4=PhotoImage(file="4player.gif")
red=PhotoImage(file="RED.gif")
blue=PhotoImage(file="BLUE.gif")
yellow=PhotoImage(file="YELLOW.gif")
green=PhotoImage(file="GREEN.gif")
Names=PhotoImage(file="names and colors.gif")
PressStart=PhotoImage(file="Press start .gif")
Start=PhotoImage(file="START.gif")
Back=PhotoImage(file="BACK.gif")
PL1R=PhotoImage(file="PL1 ROUGE.gif")
Exit=PhotoImage(file="EXIT.gif")
fgauch=PhotoImage(file="Flèche gauche.gif")
fdroit=PhotoImage(file="Flèche droite.gif")
PL1R=PhotoImage(file="PL1 ROUGE.gif")
PL1V=PhotoImage(file="PL1 VERT.gif")
PL1B=PhotoImage(file="PL1 BLEU.gif")
PL1J=PhotoImage(file="PL1 JAUNE.gif")
PL2R=PhotoImage(file="PL2 ROUGE.gif")
PL2V=PhotoImage(file="PL2 VERT.gif")
PL2B=PhotoImage(file="PL2 BLEU.gif")
PL2J=PhotoImage(file="PL2 JAUNE.gif")
PL3R=PhotoImage(file="PL3 ROUGE.gif")
PL3V=PhotoImage(file="PL3 VERT.gif")
PL3B=PhotoImage(file="PL3 BLEU.gif")
PL3J=PhotoImage(file="PL3 JAUNE.gif")
PL4R=PhotoImage(file="PL4 ROUGE.gif")
PL4V=PhotoImage(file="PL4 VERT.gif")
PL4B=PhotoImage(file="PL4 BLEU.gif")
PL4J=PhotoImage(file="PL4 JAUNE.gif")
Menu=PhotoImage(file="MENU.gif")

Fond=PhotoImage(file="FOND.gif")
canvas.create_image(0,0,image=Fond)
Titre=PhotoImage(file="titre.gif")
canvas.create_image(255,50,image=Titre)
Number=PhotoImage(file="Number of players.gif")
canvas.create_image(250,200,image=Number)
Valider=PhotoImage(file="Valider.gif")
canvas.create_image(250,650,image=Valider,tag="Valid")
canvas.tag_bind("Valid","<Button-1>",Enter)
canvas.create_image(435,670,image=Exit,tag="EXI")
canvas.tag_bind("EXI","<Button-1>",Quitter)
canvas.create_image(65,670,image=Menu,tag="MEN")
canvas.tag_bind("MEN","<Button-1>",MainMenu)


canvas.create_image(250,300,image=flechehaut,tag="KEK")
canvas.tag_bind("KEK","<Button-1>",Augmenter)

canvas.create_image(250,500,image=flechebas,tag="KEK1")
canvas.tag_bind("KEK1","<Button-1>",Diminuer)

canvas.create_image(250,400,image=chiffre1)
canvas.create_image(250,130,image=joueur_1)

conf.mainloop()

