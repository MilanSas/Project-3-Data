#Import Tkinter
from tkinter import *
from tkinter import messagebox

#Background gets loaded
root = Tk()

#Resizes the image
root.resizable(width=True, height=True)
root.geometry('{}x{}'.format(root.winfo_screenwidth(), root.winfo_screenheight()))

#gets current screen size
screenx=root.winfo_screenwidth()
screeny= root.winfo_screenheight()

#The image
image = PhotoImage(file="Rotterdamse_kaart.png")
larger_image = image.zoom(1)
label = Label(image=larger_image,background="red")
label.grid()

#Text
overschie = "Overschie" #the name of the area's that will get loaded when a user clicks a button
hillegersberg_schiebroek = "Hillegersberg-schiebroek"
prins_alexander = "Prins Alexander"
kralingen_crooswijk = "Kralingen Crooswijk"
noord = "Noord"
delftshaven = "Delfshaven"
centrum = "Centrum"
waalhaven = "Waalhaven"
charlois = "Charlois"
feijenood = "Feijenoord"
ijsselmonde = "Ijsselmonde"

def textChanger(): #method that is going to change the text based on the user's input
    pass

text = Label(root,  width=60, height=5,text=charlois,font=("arial",35,"bold"),)
text.grid()

#Methods that run when a button is pressed
def milieuMethod():
   pass

def luchtkwaliteitMethod():
   pass

def veiligheidMethod():
    pass

def voorzieningenMethod():
    pass

def tevredenheidMethod():
    pass

def huurprijsMethod():
    pass

def koopprijsMethod():
    pass

def backMethod():
    pass


#Buttons
Button1 = Button(root, text ="Milieu", command = milieuMethod)
Button1.grid(row=0, column=1, columnspan=1, sticky=W+E,ipady=10) #information you can set about a button

Button2 = Button(root, text ="Luchtkwaliteit", command = luchtkwaliteitMethod())
Button2.grid(row=1, column=1, columnspan=1,sticky=W+E,ipady=30,ipadx=30)

Button3 = Button(root, text ="Veiligheid", command = veiligheidMethod())
Button3.grid(row=2, column=1, columnspan=1,sticky=W+E,ipady=30)

Button4 = Button(root, text ="Voorzieningen", command = voorzieningenMethod())
Button4.grid(row=3, column=1, columnspan=1,sticky=W+E,ipady=30)

Button5 = Button(root, text ="Tevredenheid", command = tevredenheidMethod())
Button5.grid(row=4, column=1, columnspan=1,sticky=W+E,ipady=30)

Button6 = Button(root, text ="Gemiddelde huurpprijs", command = huurprijsMethod())
Button6.grid(row=5, column=1, columnspan=1,sticky=W+E)

Button7 = Button(root, text ="Gemiddelde koopprijs", command = koopprijsMethod())
Button7.grid(row=6, column=1, columnspan=1,sticky=W+E)

Button8 = Button(root, text ="Back", command = backMethod())
Button8.grid(row=6, column=1, columnspan=1,sticky=W+E)

#Mouse position
x = root.winfo_pointerx()
y = root.winfo_pointery()

#Loops
root.mainloop()