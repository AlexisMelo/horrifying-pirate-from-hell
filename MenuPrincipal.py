from tkinter import*
import os

def Fenetre(Clique):
    root.destroy()
    os.system("config2.py")

def Creds(Clique):
    Fen2=Tk()
    Fen2.title( " Crédits ")
    Fen2.mainloop()
    
root=Tk()

canvas = Canvas(root,width=1020,height=820)
canvas.pack()

#images#

fond=PhotoImage(file="Menu image.gif")
bouton=PhotoImage(file="Bouton.gif")
credit=PhotoImage(file="Credits.gif")

#Image de fond#

canvas.create_image(0,0,image=fond,anchor=NW)

#Bouton jouer#

canvas.create_image(564,288,image=bouton,tag="Jouer")
canvas.tag_bind("Jouer","<Button-1>",Fenetre)

#Bouton Crédits#

canvas.create_image(966,784,image=credit,tag="Crédits")
canvas.tag_bind("Crédits","<Button-1>" ,Creds)
                





























































root.mainloop()
