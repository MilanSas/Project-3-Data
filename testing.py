from tkinter import *


#TODO methods needs to be filled in
#TODO transparant buttons for the locations
#TODO find better way to resize the picture


#Background gets loaded
root = Tk() #Needed to run
root.title("Rotterdam Living") #Window title
root.geometry('{}x{}'.format(root.winfo_screenwidth(), root.winfo_screenheight())) #allows option boxes(minimize. maximize etc)

#gets user's screen size
screenx=root.winfo_screenwidth()
screeny= root.winfo_screenheight()

#The image
image = PhotoImage(file="Rotterdamse_kaart.png") #The file
larger_image = image.zoom(2) #resizes image but there must be a better way
label = Label(root, image=larger_image) #saves the image

orginal_overschie_photo = PhotoImage(file="overschie_test.png") #area specific file for when the user clicks
large_overschie_photo = orginal_overschie_photo.zoom(4)

label.grid(sticky=N,column=1, row=1,rowspan=999) #loads the image in row 1 of column 1. Sticky is the position
#Sticky = position, column = in which column, row = in which row.
#Grid is similar to Microsoft Excel, the samer type of layout

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
rotterdam = "Rotterdam"

#Text
text = Label(root,  width=0, height=1,text=rotterdam,font=("Helvetica",35,"bold"),) #puts image on screen
text.grid(row=0,column=1,sticky=N) #loads the image


#methods that are going to run when the an user clicks a certain button
def textChanger():
    pass

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
    label.config(image=large_overschie_photo) #Photo zoom testing


#closes window
def backMethod():
    root.destroy()


#catches current position of the mouse and changes name based on mouse position
def motion(event):
    print("Mouse position: (%s %s)" %(event.x,event.y))
    if event.x < 500 and event.y < 279:
        text.config(text=overschie)
    elif event.x > 550 and event.y < 279:
        text.config(text=hillegersberg_schiebroek)

label.bind('<Motion>',motion) #mouse method applied to the label(picture) object. Only when on the picture, the method will be activated



#The buttons
Button1 = Button(root, text ="Milieu", command = milieuMethod,font=("arial",30,"bold")) #command = method
Button1.columnconfigure(0,weight=3) #weight = if it will get moved when another button takes wide rows
Button1.grid(row=1, column=0, sticky=W,ipadx=screenx/20,ipady=screeny/75) #information you can set about a button
#ipadx = the size in width, ipady = the size it takes in height

Button2 = Button(root, text ="Luchtkwaliteit", command = luchtkwaliteitMethod,font=("arial",30,"bold"))
Button2.columnconfigure(0,weight=3)
Button2.grid(row=2, column=0, sticky=W, ipadx=screenx/175,ipady=screeny/75)

Button3 = Button(root, text ="Veiligheid", command = veiligheidMethod,font=("arial",30,"bold"))
Button3.columnconfigure(0,weight=3)
Button3.grid(row=3, column=0, sticky=W, ipadx=screenx/35, ipady=screeny/75)

Button4 = Button(root, text ="Voorzieningen", command = voorzieningenMethod,font=("arial",30,"bold"))
Button4.columnconfigure(0,weight=3)
Button4.grid(row=4, column=0,sticky=W,ipadx=screenx/300, ipady=screeny/75)

Button5 = Button(root, text ="Tevredenheid", command = tevredenheidMethod,font=("arial",30,"bold"))
Button5.columnconfigure(0,weight=3)
Button5.grid(row=5, column=0,sticky=W,ipadx=screenx/110, ipady=screeny/75)

Button6 = Button(root, text ="Huurpprijs", command = huurprijsMethod,font=("arial",30,"bold"))
Button6.columnconfigure(0,weight=3)
Button6.grid(row=6, column=0,sticky=W,ipadx=screenx/40, ipady=screeny/75)

Button7 = Button(root, text ="Koopprijs", command = koopprijsMethod,font=("arial",30,"bold"))
Button7.columnconfigure(0,weight=5)
Button7.grid(row=7, column=0, sticky=W,ipadx=screenx/35, ipady=screeny/75)

Button8 = Button(root, text ="Back", command = backMethod,font=("arial",30,"bold"))
Button8.columnconfigure(0,weight=3)
Button8.grid(row=8, column=0, sticky=W,ipadx=screenx/18, ipady=screeny/75)





#The main loop
root.mainloop()