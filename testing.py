from tkinter import *

#Background gets loaded
root = Tk() #Needed to run

#TODO methods needs to be filled in
#TODO transparant buttons for the locations
#TODO find better way to resize the picture



root.title("Rotterdam Living") #Window title
root.geometry('{}x{}'.format(root.winfo_screenwidth(), root.winfo_screenheight())) #allows option boxes(minimize. maximize etc)

#gets user's screen size (width and height)
screenx=root.winfo_screenwidth()
screeny= root.winfo_screenheight()

#The image
image = PhotoImage(file="Rotterdamse_kaart.png") #The file
larger_image = image.zoom(2) #resizes image but there must be a better way
label = Label(root, image=larger_image) #saves the image

orginal_overschie_photo = PhotoImage(file="overschie_test.png") #area specific file for when the user clicks
large_overschie_photo = orginal_overschie_photo.zoom(4) #zooms the image to make it bigger.
label.grid(sticky=N,column=1, row=1,rowspan=999) #loads the image in row 1 of column 1. Sticky is the position

#Sticky = position, column = in which column, row = in which row.
#Grid is similar to Microsoft Excel, the samer type of layout

#Text
overschie = "Overschie" #the name of the area's that will get loaded when a user clicks the area
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

#Button triggers, when a button get pressed, theses booleans will be changed.
Button1_bool = False
Button2_bool = False
Button3_bool = False
Button4_bool = False
Button5_bool = False
Button6_bool = False
Button7_bool = False
Button8_bool = False


#The text that will appear on top
text = Label(root,  width=0, height=1,text=rotterdam,font=("Helvetica",35,"bold"),) #puts image on screen
text.grid(row=0,column=1,sticky=N) #loads the image


#methods that are going to run when the an user clicks a certain button
def milieuMethod():
    global Button1_bool #imports the global variable

    if Button1_bool == False: #When a button is pressed or depressed, the state of the booleans change
        Button1.config(bg="green") #Button's colour changes
        Button1_bool = True
    elif Button1_bool == True:
         Button1.config(bg="DeepSkyBlue2")
         Button1_bool = False


def luchtkwaliteitMethod():
    global Button2_bool

    if Button2_bool == False:
        Button2.config(bg="green")
        Button2_bool = True
    elif Button2_bool == True:
         Button2.config(bg="DeepSkyBlue2")
         Button2_bool = False


def veiligheidMethod():
    global Button3_bool

    if Button3_bool == False:
        Button3.config(bg="green")
        Button3_bool = True
    elif Button3_bool == True:
         Button3.config(bg="DeepSkyBlue2")
         Button3_bool = False

def voorzieningenMethod():
    global Button4_bool

    if Button4_bool == False:
        Button4.config(bg="green")
        Button4_bool = True
    elif Button4_bool == True:
         Button4.config(bg="DeepSkyBlue2")
         Button4_bool = False

def tevredenheidMethod():
    global Button5_bool
    if Button5_bool == False:
        Button5.config(bg="green")
        Button5_bool = True
    elif Button5_bool == True:
         Button5.config(bg="DeepSkyBlue2")
         Button5_bool = False

def huurprijsMethod():
    global Button6_bool

    if Button6_bool == False:
        Button6.config(bg="green")
        Button6_bool = True
    elif Button6_bool == True:
         Button6.config(bg="DeepSkyBlue2")
         Button6_bool = False


def koopprijsMethod():
    global Button7_bool
    if Button7_bool == False:
        Button7.config(bg="green")
        label.config(image=large_overschie_photo)  # Photo zoom testing and testing
        text.config(text=overschie)  # testing
        Button7_bool = True

    elif Button7_bool == True:
         Button7.config(bg="DeepSkyBlue2")
         label.config(image=larger_image)  # Photo zoom testing and testing
         text.config(text=overschie)  # testing
         Button7_bool = False


#closes window
def backMethod():
    global Button8_bool
    if Button8_bool == False:
         root.destroy() #this closes the window
    elif Button8_bool == True:
         Button8.config(bg="DeepSkyBlue2")
         Button8_bool = False




#catches current position of the mouse and changes name based on mouse position
#This method will also seve as to detect were the user clicks on the map
def motion(event):
    print("Mouse position: (%s %s)" %(event.x,event.y))
    if event.x < 500 and event.y < 279: #the mouse positions
        text.config(text=overschie) #changes the text that appears on the top
    elif event.x > 550 and event.y < 279:
        text.config(text=hillegersberg_schiebroek)
    else:
        text.config(text=rotterdam)

label.bind('<Motion>',motion) #mouse method applied to the label(picture) object. Only when on the picture, the method will be activated

#The side buttons
Button1 = Button(root, text ="Milieu", command = milieuMethod,font=("arial",30,"bold"),bg="DeepSkyBlue2", fg="white") #command = method
Button1.columnconfigure(0,weight=3) #weight = if it will get moved when another button takes wide rows
Button1.grid(row=1, column=0, sticky=W,ipadx=screenx/19.5,ipady=screeny/150) #information you can set about a button
#ipadx = the size in width, ipady = the size it takes in height

Button2 = Button(root, text ="Luchtkwaliteit", command = luchtkwaliteitMethod,font=("arial",30,"bold"),bg="DeepSkyBlue2", fg="white")
Button2.columnconfigure(0,weight=3)
Button2.grid(row=2, column=0, sticky=W, ipadx=screenx/213.5,ipady=screeny/150)

Button3 = Button(root, text ="Veiligheid", command = veiligheidMethod,font=("arial",30,"bold"),bg="DeepSkyBlue2", fg="white")
Button3.columnconfigure(0,weight=3)
Button3.grid(row=3, column=0, sticky=W, ipadx=screenx/35.5, ipady=screeny/150)

Button4 = Button(root, text ="Voorzieningen", command = voorzieningenMethod,font=("arial",30,"bold"),bg="DeepSkyBlue2", fg="white")
Button4.columnconfigure(0,weight=3)
Button4.grid(row=4, column=0,sticky=W,ipadx=screenx/500, ipady=screeny/150)

Button5 = Button(root, text ="Tevredenheid", command = tevredenheidMethod,font=("arial",30,"bold"),bg="DeepSkyBlue2", fg="white")
Button5.columnconfigure(0,weight=3)
Button5.grid(row=5, column=0,sticky=W,ipadx=screenx/140, ipady=screeny/150)

Button6 = Button(root, text ="Huurpprijs", command = huurprijsMethod,font=("arial",30,"bold"),bg="DeepSkyBlue2", fg="white")
Button6.columnconfigure(0,weight=3)
Button6.grid(row=6, column=0,sticky=W,ipadx=screenx/41, ipady=screeny/150)

Button7 = Button(root, text ="Koopprijs", command = koopprijsMethod,font=("arial",30,"bold"),bg="DeepSkyBlue2", fg="white")
Button7.columnconfigure(0,weight=5)
Button7.grid(row=7, column=0, sticky=W,ipadx=screenx/34.5, ipady=screeny/150)

Button8 = Button(root, text ="Back", command = backMethod,font=("arial",30,"bold"),bg="DeepSkyBlue2", fg="white")
Button8.columnconfigure(0,weight=3)
Button8.grid(row=8, column=0, sticky=W,ipadx=screenx/17.5, ipady=screeny/150)



#The main loop
root.mainloop()


