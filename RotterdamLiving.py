from tkinter import *
import math



#Background gets loaded
root = Tk() #Needed to run

#TODO methods needs to be filled in
#TODO find better way to resize the picture
#TODO when user hoovers of an area, make it if it's possible the area change colour + change location text



root.title("Rotterdam Living") #Window title
root.geometry('{}x{}'.format(root.winfo_screenwidth(), root.winfo_screenheight())) #allows option boxes(minimize. maximize etc)

#gets user's screen size (width and height)
screenx=root.winfo_screenwidth()
screeny= root.winfo_screenheight()

# #image code below commented out because there is a new image
# #The image
# image = PhotoImage(file="Rotterdamse_kaart.png") #The file
# larger_image = image.zoom(2) #resizes image but there must be a better way
# label = Label(root, image=larger_image) #saves the image
#
# orginal_overschie_photo = PhotoImage(file="overschie_test.png") #area specific file for when the user clicks
# large_overschie_photo = orginal_overschie_photo.zoom(4) #zooms the image to make it bigger.
# label.grid(sticky=N,column=1, row=1,rowspan=999) #loads the image in row 1 of column 1. Sticky is the position

#==================================

#Actual comments
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
        # label.config(image=large_overschie_photo)  # Photo zoom testing and testing
        text.config(text=overschie)  # testing
        Button7_bool = True

    elif Button7_bool == True:
         Button7.config(bg="DeepSkyBlue2")
         # label.config(image=larger_image)  # Photo zoom testing and testing
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

#
#===================================================================================================================
#The polygon below
canvas = Canvas(root, width=screenx,height=screeny)

def rs(size):
    ratio = (screeny + screeny/2) / size
    return (screeny / ratio)

def changecolor(object,color):
    canvas.itemconfig(object.shape, fill=HexToRGB(color))

def HexToRGB(rgb):
    #RGB WAARDES MOETEN TUSSEN 16 - 255
    result = ('#' + str(hex(rgb[0]).split('x')[-1]) + str(hex(rgb[1]).split('x')[-1]) + str(hex(rgb[2]).split('x')[-1]))
    return result



class polygon:
    def __init__(self,color,list):
        self.color = color
        self.shape = canvas.create_polygon(list, fill=HexToRGB(self.color), outline='black', width = 2)
    def changeColour(self): #method for when the user clicks an place, the place's colour changes
        pass
    def resetColur(self): #Method for when the user clicks another place, the previous selected place gets reseted
        pass



overschie_polgon = polygon((20,50,120),(rs(904),rs(194),rs(947),rs(183),rs(955),rs(205),rs(1106),rs(109),rs(1176),rs(199),rs(1222),rs(163),rs(1242),rs(185),rs(1237),rs(355),rs(1109),rs(432),rs(1138),rs(471),rs(1057),rs(479),rs(1017),rs(403),rs(1059),rs(350),rs(1050),rs(345),rs(1003),rs(366),rs(964),rs(322),rs(949),rs(342)))
hillegersberg_polygon = polygon((20,50,120),(rs(1242),rs(185),rs(1237),rs(355),rs(1520),rs(282),rs(1499),rs(189),rs(1475),rs(213),rs(1432),rs(195),rs(1428),rs(172),rs(1387),rs(141),rs(1382),rs(154),rs(1280),rs(90)))
prins_alexander_polygon = polygon((20,50,120),(rs(1562),rs(454),rs(1661),rs(425),rs(1651),rs(350),rs(1693),rs(337),rs(1650),rs(227),rs(1663),rs(222),rs(1673),rs(233),rs(1821),rs(141),rs(1791),rs(116),rs(1815),rs(31),rs(1804),rs(12),rs(1617),rs(76),rs(1680),rs(145),rs(1627),rs(169),rs(1595),rs(134),rs(1499),rs(189)))
kralingen_polygon = polygon((20,50,120),(rs(1521),rs(282),rs(1562),rs(454),rs(1538),rs(498),rs(1572),rs(594),rs(1489),rs(616),rs(1469),rs(593),rs(1453),rs(522),rs(1397),rs(500),rs(1382),rs(461),rs(1337),rs(454),rs(1331),rs(330)))
noord_polygon = polygon((20,50,120),(rs(1331),rs(330),rs(1237),rs(355),rs(1109),rs(432),rs(1136),rs(468),rs(1206),rs(462),rs(1208),rs(455),rs(1288),rs(443),rs(1337),rs(454)))
delftshaven_polygon = polygon((20,50,120),(rs(1057),rs(479),rs(1034),rs(546),rs(1048),rs(582),rs(1038),rs(610),rs(1113),rs(596),rs(1227),rs(620),rs(1262),rs(614),rs(1244),rs(558),rs(1223),rs(553),rs(1247),rs(539),rs(1243),rs(456)))
centrum_polygon = polygon((20,50,120),(rs(1262),rs(614),rs(1244),rs(558),rs(1223),rs(553),rs(1247),rs(539),rs(1243),rs(461),rs(1206),rs(462),rs(1208),rs(455),rs(1288),rs(443),rs(1337),rs(454),rs(1382),rs(461),rs(1397),rs(500),rs(1375),rs(506),rs(1322),rs(574)))
feijenoord_polygon = polygon((20,50,120),(rs(1397),rs(500),rs(1375),rs(506),rs(1322),rs(574),rs(1262),rs(614),rs(1288),rs(642),rs(1378),rs(617),rs(1372),rs(694),rs(1361),rs(698),rs(1361),rs(720),rs(1417),rs(772),rs(1454),rs(735),rs(1487),rs(735),rs(1496),rs(698),rs(1450),rs(605),rs(1469),rs(593),rs(1453),rs(522)))
ijsselmonde_polygon = polygon((20,50,120),(rs(1572),rs(594),rs(1489),rs(616),rs(1469),rs(593),rs(1450),rs(605),rs(1496),rs(698),rs(1487),rs(735),rs(1454),rs(735),rs(1417),rs(772),rs(1457),rs(824),rs(1524),rs(831),rs(1574),rs(813),rs(1657),rs(766),rs(1666),rs(779),rs(1682),rs(769),rs(1712),rs(606),rs(1625),rs(584)))
charlois_polygon = polygon((20,50,120),(rs(1262),rs(614),rs(1288),rs(642),rs(1378),rs(617),rs(1372),rs(694),rs(1361),rs(698),rs(1361),rs(720),rs(1417),rs(772),rs(1457),rs(824),rs(1388),rs(820),rs(1315),rs(848),rs(1315),rs(869),rs(1242),rs(871),rs(1161),rs(839),rs(1201),rs(824),rs(1218),rs(800),rs(1201),rs(792),rs(1199),rs(763),rs(1246),rs(656),rs(1225),rs(646),rs(1227),rs(620)))
waalhaven_polygon = polygon((20,50,120),(rs(1161),rs(839),rs(1201),rs(824),rs(1218),rs(800),rs(1201),rs(792),rs(1199),rs(763),rs(1246),rs(656),rs(1225),rs(646),rs(1227),rs(620),rs(1113),rs(596),rs(1038),rs(610),rs(954),rs(639),rs(862),rs(618),rs(885),rs(658),rs(917),rs(663),rs(921),rs(647),rs(972),rs(670),rs(962),rs(722),rs(937),rs(743),rs(934),rs(764),rs(923),rs(765),rs(927),rs(797),rs(1048),rs(795)))




setattr(overschie_polgon,'color',(170,50,120))
print(overschie_polgon.color)

#The text that will appear on top
text = Label(root,width=0, height=1,text=rotterdam,font=("Helvetica",35,"bold")) #puts image on screen
text.grid(row=0,column=0,sticky=N)

#Text description
percentage = 3 #number stat placeholder 50 is just for an example (placeholder)
bestYear = 2011
percentageDifference = ("{}%").format(percentage)
yearDifference = 2010


rotterdam_description = ("Rotterdam had in {} de laagste criminaliteit ooit, en ruim {} minder dan in {}. ".format(str(bestYear),str(percentageDifference), str(yearDifference)))

text1 = Label(root,width=0, height=1,text=rotterdam_description,font=("Helvetica",19,"bold")) #puts image on screen
text1.grid(row=9,column=0,sticky=S)



#Text city statistics
overschie_statistic = None
hillegersberg_statistic = None
prins_alexander_statistic = None
kralingen_statistic = None
noord_statistic = None
delftshaven_statistic = None
kralingen_crooswijk_statistic = None
waalhaven_statistic = None
charlois_statistic = None
Ijsselmonde_statistic = None
centrum_statistic = None
feijenoord_statistic = None


text_overschie = Label(root,width=0, height=1,text=overschie_statistic,font=("Helvetica",35,"bold")) #puts image on screen
text_overschie.grid(row=8,column=0,sticky=N)

text_hillgersberg = Label(root,width=0, height=1,text=hillegersberg_statistic,font=("Helvetica",35,"bold")) #puts image on screen
text_hillgersberg.grid(row=8,column=0,sticky=N)

text_prins_alexander = Label(root,width=0, height=1,text=prins_alexander_statistic,font=("Helvetica",35,"bold")) #puts image on screen
text_prins_alexander.grid(row=8,column=0,sticky=N)

text_kralingen = Label(root,width=0, height=1,text=kralingen_statistic,font=("Helvetica",35,"bold")) #puts image on screen
text_kralingen.grid(row=8,column=0,sticky=N)

text_noord = Label(root,width=0, height=1,text=noord_statistic,font=("Helvetica",35,"bold")) #puts image on screen
text_noord.grid(row=8,column=0,sticky=N)

text_delfshaven = Label(root,width=0, height=1,text=delftshaven_statistic,font=("Helvetica",35,"bold")) #puts image on screen
text_delfshaven.grid(row=8,column=0,sticky=N)

text_kralingen_crooswijk = Label(root,width=0, height=1,text=kralingen_crooswijk_statistic,font=("Helvetica",35,"bold")) #puts image on screen
text_kralingen_crooswijk.grid(row=8,column=0,sticky=N)

text_waalhaven = Label(root,width=0, height=1,text=waalhaven_statistic,font=("Helvetica",35,"bold")) #puts image on screen
text_waalhaven.grid(row=8,column=0,sticky=N)

text_charlois = Label(root,width=0, height=1,text=charlois_statistic,font=("Helvetica",35,"bold")) #puts image on screen
text_charlois.grid(row=8,column=0,sticky=N)

text_ijsselmonde = Label(root,width=0, height=1,text=Ijsselmonde_statistic,font=("Helvetica",35,"bold")) #puts image on screen
text_ijsselmonde.grid(row=8,column=0,sticky=N)

text_centrum = Label(root,width=0, height=1,text=centrum_statistic,font=("Helvetica",35,"bold")) #puts image on screen
text_centrum.grid(row=8,column=0,sticky=N)

text_feijenoord = Label(root,width=0, height=1,text=feijenoord_statistic,font=("Helvetica",35,"bold")) #puts image on screen
text_feijenoord.grid(row=8,column=0,sticky=N)








#The side buttons
Button1 = Button(root, text ="Milieu", command = milieuMethod,font=("arial",30,"bold"),bg="DeepSkyBlue2", fg="white") #command = method
Button1.columnconfigure(0,weight=3) #weight = if it will get moved when another button takes wide rows
Button1.grid(row=1, column=0, sticky=W,ipadx=screenx/19.5,ipady=screeny/150) #information you can set about a button
#ipadx = the size in width, ipady = the size it takes in height

Button2 = Button(root, text ="Luchtkwaliteit", command = luchtkwaliteitMethod,font=("arial",30,"bold"),bg="DeepSkyBlue2", fg="white")
Button2.columnconfigure(0,weight=3)
Button2.grid(row=2, column=0, sticky=W, ipadx=screenx/213.5,ipady=screeny/150)

Button3 = Button(root, text ="Veiligheid", command = veiligheidMethod,font=("arial",30,"bold"),bg="DeepSkyBlue2", fg="white")
Button3.columnconfigure(0,weight=300000)
Button3.grid(row=3, column=0, sticky=W, ipadx=screenx/35.5, ipady=screeny/150)

Button4 = Button(root, text ="Voorzieningen", command = voorzieningenMethod,font=("arial",30,"bold"),bg="DeepSkyBlue2", fg="white")
Button4.columnconfigure(0,weight=3)
Button4.grid(row=4, column=0,sticky=W,ipadx=screenx/500, ipady=screeny/150)

Button5 = Button(root, text ="Tevredenheid", command = tevredenheidMethod,font=("arial",30,"bold"),bg="DeepSkyBlue2", fg="white")
Button5.columnconfigure(0,weight=3)
Button5.grid(row=5, column=0,sticky=W,ipadx=screenx/140, ipady=screeny/150)

Button6 = Button(root, text ="Huurprijs", command = huurprijsMethod,font=("arial",30,"bold"),bg="DeepSkyBlue2", fg="white")
Button6.columnconfigure(0,weight=3)
Button6.grid(row=6, column=0,sticky=W,ipadx=screenx/32, ipady=screeny/150)

Button7 = Button(root, text ="Koopprijs", command = koopprijsMethod,font=("arial",30,"bold"),bg="DeepSkyBlue2", fg="white")
Button7.columnconfigure(0,weight=5)
Button7.grid(row=7, column=0, sticky=W,ipadx=screenx/34.5, ipady=screeny/150)

Button8 = Button(root, text ="Back", command = backMethod,font=("arial",30,"bold"),bg="DeepSkyBlue2", fg="white")
Button8.columnconfigure(0,weight=3)
Button8.grid(row=8, column=0, sticky=W,ipadx=screenx/17.5, ipady=screeny/150)


#mouse method, gets current mouse possitions
def motion(event):
    if event.x > 500 and event.y < 279: #the mouse positions
        text.config(text="")
    else:
        text.config(text="Rotterdam")
    print(str(event.x) + " " + str(event.y))




#With this the area's/polygons can be selected
def click(event):
    if str(canvas.find_withtag(CURRENT)) == "(1,)":
        text.config(text=overschie)
        overschie_polgon.changeColour()
        canvas.grid()
    elif str(canvas.find_withtag(CURRENT)) == "(2,)":
        text.config(text=hillegersberg_schiebroek)
    elif str(canvas.find_withtag(CURRENT)) == "(3,)":
        text.config(text=prins_alexander)
    elif str(canvas.find_withtag(CURRENT)) == "(4,)":
        text.config(text=kralingen_crooswijk)
    elif str(canvas.find_withtag(CURRENT)) == "(5,)":
        text.config(text=noord)
    elif str(canvas.find_withtag(CURRENT)) == "(6,)":
        text.config(text=delftshaven)
    elif str(canvas.find_withtag(CURRENT)) == "(7,)":
        text.config(text=centrum)
    elif str(canvas.find_withtag(CURRENT)) == "(8,)":
        text.config(text=feijenood)
    elif str(canvas.find_withtag(CURRENT)) == "(9,)":
        text.config(text=ijsselmonde)
    elif str(canvas.find_withtag(CURRENT)) == "(10,)":
        text.config(text=charlois)
    elif str(canvas.find_withtag(CURRENT)) == "(11,)":
        text.config(text=waalhaven)
    else:
        text.config(text="Rotterdam")




#the canvas where the polygons are drawed
canvas.grid(row=2, column=0,sticky=N,rowspan=999,padx=55) #draws the canvas


#when a polygon is clicked, the click method will be activated
canvas.bind('<Button-1>', click, add="+") #mouse method applied to the label(picture) object. Only when on the picture, the method will be activated
# canvas.bind('<Motion>', motion, add="+") #Add makes it possible to adds multiple binds(events to a widget)



root.mainloop()