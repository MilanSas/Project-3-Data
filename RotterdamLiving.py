from tkinter import *

#TODO methods (button functionality) needs to be filled in
#TODO find better way to resize the picture
#TODO when user hoovers of an area, make it if it's possible the area change colour + change location text
#TODO when user clicks on an area, that area needs to be zoomed in
#TODO Add names for the objects


#Background gets loaded
root = Tk() #Needed to run

root.title("Rotterdam Living") #Window title
root.geometry('{}x{}'.format(root.winfo_screenwidth(), root.winfo_screenheight())) #allows option boxes(minimize. maximize etc)

#gets user's screen size (width and height)
screenx=root.winfo_screenwidth()
screeny= root.winfo_screenheight()



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

#Trigger for the buttons, when a button is pressed the state changes (true, false)
#Sticky = position, column = in which column, row = in which row.
class NewButton:
    def __init__(self,text, row, column, ipadx, ipady):
        self.clicked = False
        self.button = Button(root, text =text, command = self.click,font=("arial",30,"bold"),bg="DeepSkyBlue2", fg="white")
        self.button.columnconfigure(0,weight=300000)
        self.button.grid(row=row, column=column, sticky=W, ipadx=ipadx, ipady=ipady)
        # command = method
        # weight = if it will get moved when another button takes wide rows
        # information you can set about a button
        # ipadx = the size in width, ipady = the size it takes in height

    def click(self):
            if self.clicked == False: #When a button is pressed or depressed, the state of the booleans change
                self.button.config(bg="green") #Button's colour changes
                setattr(self, 'clicked', True) #State of the button is set to true.
            elif self.clicked == True:
                 self.button.config(bg="DeepSkyBlue2")
                 setattr(self, 'clicked', False)


#triggers for the buttons
#methods that are going to run when the an user clicks a certain button
class Trigger:
    def __init__(self, triggerValue,name):
        self.trigger = triggerValue
        self.name = name
    def __str__(self):
        return self.name

#===================================================================================================================
#The polygon below



canvas = Canvas(root, width=screenx,height=screeny)

def rs(size):
    ratio = (screeny + screeny/2) / size
    return (screeny / ratio)

def changecolor(object,percent):
    red = 0
    green = 0
    if percent < 7:
        red = 255
        green = 16
    elif percent > 93:
        green = 255
        red = 16
    elif percent > 50:
        green = 255
        red = int((100 - percent) * 5.1)
    elif percent <= 50:
        red = 255
        green = int(percent * 5.1)
    color = (red, green, 16)
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


#The text that will appear on top
text = Label(root,width=0, height=1,text=rotterdam,font=("Helvetica",35,"bold")) #puts image on screen
text.grid(row=0,column=0,sticky=N)

#the text that appears on the bottom that displays the numbers in text, it tells a story
def percentage():
    # Text description
    percentage = 3  # number stat placeholder 50 is just for an example (placeholder)
    bestYear = 2011
    percentageDifference = ("{}%").format(percentage)
    yearDifference = 2010

    rotterdam_description = (
    "Rotterdam had in {} de laagste criminaliteit ooit, en ruim {} minder dan in {}. ".format(str(bestYear),
                                                                                              str(percentageDifference),
                                                                                              str(yearDifference)))

    text1 = Label(root, width=0, height=1, text=rotterdam_description,
                  font=("Helvetica", 19, "bold"))  # puts image on screen
    text1.grid(row=9, column=0, sticky=S)




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


#The side buttons, put in a function so that they can called when needed
def sideButtons():
    button1 = NewButton("Millieu", 1, 0, screenx / 19.5, screeny / 150)
    button2 = NewButton("Luchtkwailiteit", 2, 0, screenx / 213.5, screeny / 150)
    button3 = NewButton("Veiligheid", 3, 0, screenx / 35.5, screeny / 150)
    button4 = NewButton("Voorzieningen", 4, 0, screenx / 500, screeny / 150)
    button5 = NewButton("Tevredenheid", 5, 0, screenx / 140, screeny / 150)
    button6 = NewButton("Huurprijs", 6, 0, screenx / 32, screeny / 150)
    button7 = NewButton("Koopprijs", 7, 0, screenx / 34.5, screeny / 150)
    button8 = NewButton("Koopprijs", 8, 0, screenx / 17.5, screeny / 150)




#mouse method, gets current mouse possitions
def motion(event):
    if event.x > 500 and event.y < 279: #the mouse positions
        text.config(text="")
    else:
        text.config(text="Rotterdam")
    print(str(event.x) + " " + str(event.y))

#triggers for when an area gets selected
overschie_trigger = Trigger(False, "overschie")
hillegersberg_trigger = Trigger(False,"hillegersberg")
prins_alexander_trigger = Trigger(False, "prinsAlexander")
noord_trigger = Trigger(False,"noord")
kralingen_crooswijk_trigger = Trigger(False, "kralingenCrooswijk")
centrum_trigger = Trigger(False, "centrum")
delftshaven_trigger = Trigger(False, "delftshaven")
waalhaven_trigger = Trigger(False, "waalhaven")
charlois_trigger = Trigger(False, "charlois")
feijenood_trigger = Trigger(False, "feijenoord")
ijsselmonde_trigger = Trigger(False, "ijsselmonde")


#Triggers for when an area is selected
List1 = [overschie_trigger, hillegersberg_trigger,prins_alexander_trigger,noord_trigger, kralingen_crooswijk_trigger, centrum_trigger, delftshaven_trigger, waalhaven_trigger, charlois_trigger, feijenood_trigger, ijsselmonde_trigger]


#With this the area's/polygons can be selected
def click(event):
    if str(canvas.find_withtag(CURRENT)) == "(1,)":
        text.config(text=overschie)
        for i in List1:
            if i.name == "overschie":
                setattr(i, 'trigger', True)

            else:
                setattr(i, 'trigger', False)
                print(i.trigger)

    elif str(canvas.find_withtag(CURRENT)) == "(2,)":
        text.config(text=hillegersberg_schiebroek)
        for i in List1:
            if i.name == "hillegersberg":
                setattr(i, 'trigger', True)

            else:
                setattr(i, 'trigger', False)
                print(i.trigger)


    elif str(canvas.find_withtag(CURRENT)) == "(3,)":
        text.config(text=prins_alexander)
        for i in List1:
            if i.name == "prinsAlexander":
                setattr(i, 'trigger', True)

            else:
                setattr(i, 'trigger', False)
                print(i.trigger)

    elif str(canvas.find_withtag(CURRENT)) == "(4,)":
        text.config(text=kralingen_crooswijk)
        for i in List1:
            if i.name == "kralingenCrooswijk":
                setattr(i, 'trigger', True)

            else:
                setattr(i, 'trigger', False)
                print(i.trigger)

    elif str(canvas.find_withtag(CURRENT)) == "(5,)":
        text.config(text=noord)
        for i in List1:
            if i.name == "noord":
                setattr(i, 'trigger', True)

            else:
                setattr(i, 'trigger', False)
                print(i.trigger)


    elif str(canvas.find_withtag(CURRENT)) == "(6,)":
        text.config(text=delftshaven)
        for i in List1:
            if i.name == "delftshaven":
                setattr(i, 'trigger', True)

            else:
                setattr(i, 'trigger', False)
                print(i.trigger)

    elif str(canvas.find_withtag(CURRENT)) == "(7,)":
        text.config(text=centrum)
        for i in List1:
            if i.name == "centrum":
                setattr(i, 'trigger', True)

            else:
                setattr(i, 'trigger', False)
                print(i.trigger)


    elif str(canvas.find_withtag(CURRENT)) == "(8,)":
        text.config(text=feijenood)
        for i in List1:
            if i.name == "feijenoord":
                setattr(i, 'trigger', True)

            else:
                setattr(i, 'trigger', False)
                print(i.trigger)



    elif str(canvas.find_withtag(CURRENT)) == "(9,)":
        text.config(text=ijsselmonde)
        for i in List1:
            if i.name == "ijsselmonde":
                setattr(i, 'trigger', True)

            else:
                setattr(i, 'trigger', False)
                print(i.trigger)

    elif str(canvas.find_withtag(CURRENT)) == "(10,)":
        text.config(text=charlois)
        for i in List1:
            if i.name == "charlois":
                setattr(i, 'trigger', True)

            else:
                setattr(i, 'trigger', False)
                print(i.trigger)

    elif str(canvas.find_withtag(CURRENT)) == "(11,)":
        text.config(text=waalhaven)
        for i in List1:
            if i.name == "waalhaven":
                setattr(i, 'trigger', True)

            else:
                setattr(i, 'trigger', False)
                print(i.trigger)





#when a polygon is clicked, the click method will be activated
canvas.bind('<Button-1>', click, add="+") #mouse method applied to the label(picture) object. Only when on the picture, the method will be activated
# canvas.bind('<Motion>', motion, add="+") #Add makes it possible to adds multiple binds(events to a widget)


#draws on top of the screen, this makes everything dissapear. The lower the code, the later it will get drawn
#the canvas where the polygons are drawed
canvas.grid(row=2, column=0,sticky=N,rowspan=999,padx=55) #draws the canvas

#Drop down menu
variable = StringVar(root)
variable.set("Home") # default value
w = OptionMenu(root, variable, "Home", "Woningadvies", "Percentages en cijfers", "Settings", "About", "Exit")
w.config(font=("Helvetica",50,"bold"),bg="DeepSkyBlue2", fg="white")
w.grid(row=0,column=0,sticky=N+W)

#the texts displayed on the screen
welcome_text = "Select the home button to see the available options"

#The menu description
description_text = Label(root,text=welcome_text,font=("Helvetica",15,"bold")) #puts image on screen
description_text.grid(row=1,column=0,sticky=W)



root.mainloop()