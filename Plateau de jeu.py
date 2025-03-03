from tkinter import*
from random import*

pion=0
nbrdude=0
fen=Tk()
fen.title("Horrifying Pirate from Hell - Ultimate Edition")

def Bonus1(pion1):
   global pion
   print("case bonus")
   pion1.grid(row=7,column=5)
   pion=pion+3

def Bonus2(pion1):
   global pion
   print("case bonus2")
   pion1.grid(row=4,column=2)
   pion=pion+3

def Bonus3(pion1):
   global pion
   print("case bonus3")
   pion1.grid(row=1,column=5)
   pion=pion+3

def Malus1(pion1):
   global pion
   print("case malus")
   pion1.grid(row=7,column=9)
   pion=pion-3

def Malus2(pion1):
   global pion
   print("case malus2")
   pion1.grid(row=4,column=2)
   pion=pion-3

def Malus3(pion1):
   global pion
   print("case malus3")
   pion1.grid(row=4,column=9)
   pion=pion-3
   
def Raccourci(pion1):
   global pion
   print("Raccourci")
   pion1.grid(row=4,column=3)
   pion=pion+6

def Raccourci2(pion1):
   global pion
   print("Raccourci2")
   pion1.grid(row=1,column=9)
   pion=pion+6

def Recul(pion1):
   global pion
   print("Recul1")
   pion1.grid(row=4,column=1)
   pion=pion-7

def Recul2(pion1):
   global pion
   print ("Recul2")
   pion1.grid(row=4,column=3)
   pion=pion-15

   
   
   
   

def de():
   global nbrdude
   global pion
   global pion1
   
   nbrdude=randint(1, 6)
   de1b=Label(image=de1)
   de2b=Label(image=de2)
   de3b=Label(image=de3)
   de4b=Label(image=de4)
   de5b=Label(image=de5)
   de6b=Label(image=de6)
      
   if nbrdude==1:
      de1b.grid(row=5,column=14,rowspan=2)
   if nbrdude==2:
      de2b.grid(row=5,column=14,rowspan=2)
   if nbrdude==3:
      de3b.grid(row=5,column=14,rowspan=2)
   if nbrdude==4:
      de4b.grid(row=5,column=14,rowspan=2)
   if nbrdude==5:
      de5b.grid(row=5,column=14,rowspan=2)
   if nbrdude==6:
      de6b.grid(row=5,column=14,rowspan=2)

   pion=pion+nbrdude
   print(pion)
   if pion==3:
      Bonus1(pion1)
   elif pion==5:
      Malus1(pion1)
   elif pion==9:
      Raccourci(pion1)
   elif pion < 11: #################################
      pion1.grid(row=7,column=11-pion) #############
   elif pion ==11:
      Bonus2(pion1)
   elif pion <13: ##################################
      pion1.grid(row=7-(pion-10),column=1) #########
   elif pion==17:
      Malus2(pion1)
   elif pion==20:
      Recul(pion1)
   elif pion==22:
      Raccourci2(pion1)
   elif pion==24:
      Malus3(pion1)
   elif pion <24: ##################################
      pion1.grid(row=4,column=pion-12) #############
   elif pion<26: ###################################
      pion1.grid(row=3-(pion-24),column=11) ########
   elif pion ==29:
      Bonus3(pion1)
   elif pion==30:
      Recul2(pion1)
   elif pion < 36: #################################
      pion1.grid(row=1,column=12-(pion-25)) ########
   elif pion > 36: #################################
      pion1.grid(row=1,column=pion-35) ###########
      pion2=pion-36 ################################
      pion=36-pion2 ################################
   else: ###########################################
      pion1.grid(row=1,column=1)
      print("gagné")###################
   print(pion)
   return pion1



#Dé#

de1=PhotoImage(file="de1.gif")
de2=PhotoImage(file="de2.gif")
de3=PhotoImage(file="de3.gif")
de4=PhotoImage(file="de4.gif")
de5=PhotoImage(file="de5.gif")
de6=PhotoImage(file="de6.gif")

#lIGNE1#
case = PhotoImage(file="case 50.gif")
case_bonus= PhotoImage(file="case bonus 50.gif")
case_malus= PhotoImage(file="case malus 50.gif")
case_recul= PhotoImage(file="case recul 50.gif")
case_raccourci = PhotoImage(file="case raccourci 50.gif")
fond= PhotoImage(file="plateau.gif")
FIX=PhotoImage(file="fixHG.gif")
FIX2=PhotoImage(file="fixBG.gif")
FIX3=PhotoImage(file="fixBD.gif")
FIX4=PhotoImage(file="fixHD.gif")
Plateaudubas=PhotoImage(file="dessousplateau.gif")
Plateaudroite=PhotoImage(file="plateaudroite.gif")

imagefond=Label(image=fond,border=0)
imagefond.grid(row=0,column=0,rowspan=9,columnspan=13)

imagebas=Label(image=Plateaudubas,border=0)
imagebas.grid(row=9,column=0,rowspan=3,columnspan=13)

imagedroite=Label(image=Plateaudroite,border=0)
imagedroite.grid(row=0,column=13,rowspan=10,columnspan=3)

fixtopleft=Label(image=FIX,border=0)
fixtopleft.grid(row=0,column=0)

fixbotleft=Label(image=FIX2,border=0)
fixbotleft.grid(row=8,column=0)

fixbotright=Label(image=FIX3,border=0)
fixbotright.grid(row=8,column=12)

fixtopright=Label(image=FIX4,border=0)
fixtopright.grid(row=0,column=12)

case35=Label(image=case,border=0)
case35.grid(row=1,column=2)

case34=Label(image=case,border=0)
case34.grid(row=1,column=3)

case33=Label(image=case,border=0)
case33.grid(row=1,column=4)

case32=Label(image=case,border=0)
case32.grid(row=1,column=5)

case31=Label(image=case,border=0)
case31.grid(row=1,column=6)

case30=Label(image=case_recul,border=0)
case30.grid(row=1,column=7)

case29=Label(image=case_bonus,border=0)
case29.grid(row=1,column=8)

case28=Label(image=case,border=0)
case28.grid(row=1,column=9)

case27=Label(image=case,border=0)
case27.grid(row=1,column=10)

case26=Label(image=case,border=0)
case26.grid(row=1,column=11)

#COLONNE DROITE#
case25=Label(image=case,border=0)
case25.grid(row=2,column=11)

case24=Label(image=case_malus,border=0)
case24.grid(row=3,column=11)

#LIGNE2#
case23=Label(image=case,border=0)
case23.grid(row=4,column=11)

case22=Label(image=case_raccourci,border=0)
case22.grid(row=4,column=10)

case21=Label(image=case,border=0)
case21.grid(row=4,column=9)

case20=Label(image=case_recul,border=0)
case20.grid(row=4,column=8)

case19=Label(image=case,border=0)
case19.grid(row=4,column=7)

case18=Label(image=case,border=0)
case18.grid(row=4,column=6)

case17=Label(image=case_malus,border=0)
case17.grid(row=4,column=5)

case16=Label(image=case,border=0)
case16.grid(row=4,column=4)

case15=Label(image=case,border=0)
case15.grid(row=4,column=3)

case14=Label(image=case,border=0)
case14.grid(row=4,column=2)

case13=Label(image=case,border=0)
case13.grid(row=4,column=1)

#COLONNE GAUCHE#
case12=Label(image=case,border=0)
case12.grid(row=5,column=1)

case11=Label(image=case_bonus,border=0)
case11.grid(row=6,column=1)

#LIGNE3#
case1=Label(image=case,border=0)
case1.grid(row=7,column=10)

case2=Label(image=case,border=0)
case2.grid(row=7,column=9)

case3=Label(image=case_bonus,border=0)
case3.grid(row=7,column=8)

case4=Label(image=case,border=0)
case4.grid(row=7,column=7)

case5=Label(image=case_malus,border=0)
case5.grid(row=7,column=6)

case6=Label(image=case,border=0)
case6.grid(row=7,column=5)

case7=Label(image=case,border=0)
case7.grid(row=7,column=4)

case8=Label(image=case,border=0)
case8.grid(row=7,column=3)

case9=Label(image=case_raccourci,border=0)
case9.grid(row=7,column=2)

case10=Label(image=case,border=0)
case10.grid(row=7,column=1)

imagepion = PhotoImage(file="Pion.gif")
pion1=Label(image=imagepion,border=0)

Bde=Button(fen,text="Lancer le dé",command=de)
Bde.grid(column=14,row=7)




fen.mainloop()
