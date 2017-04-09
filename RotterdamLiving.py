from tkinter import *

#To read the comments, the symbol: #, is after lines. the symbol: '''''' , is to explain the overall code.
#TODO when user hoovers of an area, make it if it's possible the area change colour + change location text
#TODO when user clicks on an area, that area needs to be zoomed in

root = Tk() #Needed to run

''''Window'''
root.title("Rotterdam Living") #Window title
root.geometry('{}x{}'.format(root.winfo_screenwidth(), root.winfo_screenheight())) #Window doesn't resize

''''gets user's screen size (width and height)'''''
screenx = root.winfo_screenwidth()
screeny = root.winfo_screenheight()

''''Array that will save the last page the user has visited, this is used so elements can be cleared on the screen.'''''
lastPageArray = [] #The name of the elements(pages): home, woon, pec, about, settings


''''Area Text (names of the area that get loaded when user clicks the area'''''
overschie = "Overschie"
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

''''The buttons. Every button has a trigger, when button is pressed the state is set to true and vice versa'''
class NewButton:
    def __init__(self,text, row, column, ipadx, ipady):
        self.clicked = False #state
        self.button = Button(root, text =text, command = self.click,font=("arial",30,"bold"),bg="DeepSkyBlue2", fg="white")
        self.button.columnconfigure(0,weight=300000)
        self.button.grid(row=row, column=column, sticky=W, ipadx=ipadx, ipady=ipady) #position of the button
        # command = method
        # weight = if it will get moved when another button takes wide rows
        # information you can set about a button
        # ipadx = the size in width, ipady = the size it takes in height

    def click(self):
            if self.clicked == False: #When a button is pressed or depressed, the state of the button change
                self.button.config(bg="green") #Button's colour
                setattr(self, 'clicked', True) #State of the button is set to true.
            elif self.clicked == True:
                 self.button.config(bg="DeepSkyBlue2")
                 setattr(self, 'clicked', False)
    def pageClick(self,page): #changes the method of the button
        self.button.config(command=page)
    def clickReset(self): # resets click
        self.clicked = False

'''Trigger for the polygons(area's)'''''
class Trigger:
    def __init__(self, triggerValue,name):
        self.trigger = triggerValue
        self.name = name #name to uniquely identify the object. For example in a for loop
    def __str__(self):
        return self.name

''''The canvas, important variable. Everything gets drawn on the canvas'''
canvas = Canvas(root, width=screenx,height=screeny) #root is in which window it will get drawn on.

''''Function to set polygon's(area) size'''
def rs(size):
    ratio = (screeny + screeny/2) / size
    return (screeny / ratio)

#TODO fix changeColor function to return the right area colours based on the result of the database.
''''Function to have the results from the database influence the colour of a polygon(area)'''
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

'''Function that Converts hex to RGB'''
def HexToRGB(rgb):
    #RGB WAARDES MOETEN TUSSEN 16 - 255
    result = ('#' + str(hex(rgb[0]).split('x')[-1]) + str(hex(rgb[1]).split('x')[-1]) + str(hex(rgb[2]).split('x')[-1]))
    return result

''''Function to create the polygons(area's)'''
class polygon:
    def __init__(self,color,list):
        self.color = color
        self.shape = canvas.create_polygon(list, fill=HexToRGB(self.color), outline='black', width = 2)

''''Function that draws the polygons(area's)'''''
def polygons():
    overschie_polgon = polygon((20, 50, 120), (
    rs(904), rs(194), rs(947), rs(183), rs(955), rs(205), rs(1106), rs(109), rs(1176), rs(199), rs(1222), rs(163),
    rs(1242), rs(185), rs(1237), rs(355), rs(1109), rs(432), rs(1138), rs(471), rs(1057), rs(479), rs(1017), rs(403),
    rs(1059), rs(350), rs(1050), rs(345), rs(1003), rs(366), rs(964), rs(322), rs(949), rs(342)))
    hillegersberg_polygon = polygon((20, 50, 120), (
    rs(1242), rs(185), rs(1237), rs(355), rs(1520), rs(282), rs(1499), rs(189), rs(1475), rs(213), rs(1432), rs(195),
    rs(1428), rs(172), rs(1387), rs(141), rs(1382), rs(154), rs(1280), rs(90)))
    prins_alexander_polygon = polygon((20, 50, 120), (
    rs(1562), rs(454), rs(1661), rs(425), rs(1651), rs(350), rs(1693), rs(337), rs(1650), rs(227), rs(1663), rs(222),
    rs(1673), rs(233), rs(1821), rs(141), rs(1791), rs(116), rs(1815), rs(31), rs(1804), rs(12), rs(1617), rs(76),
    rs(1680), rs(145), rs(1627), rs(169), rs(1595), rs(134), rs(1499), rs(189)))
    kralingen_polygon = polygon((20, 50, 120), (
    rs(1521), rs(282), rs(1562), rs(454), rs(1538), rs(498), rs(1572), rs(594), rs(1489), rs(616), rs(1469), rs(593),
    rs(1453), rs(522), rs(1397), rs(500), rs(1382), rs(461), rs(1337), rs(454), rs(1331), rs(330)))
    noord_polygon = polygon((20, 50, 120), (
    rs(1331), rs(330), rs(1237), rs(355), rs(1109), rs(432), rs(1136), rs(468), rs(1206), rs(462), rs(1208), rs(455),
    rs(1288), rs(443), rs(1337), rs(454)))
    delftshaven_polygon = polygon((20, 50, 120), (
    rs(1057), rs(479), rs(1034), rs(546), rs(1048), rs(582), rs(1038), rs(610), rs(1113), rs(596), rs(1227), rs(620),
    rs(1262), rs(614), rs(1244), rs(558), rs(1223), rs(553), rs(1247), rs(539), rs(1243), rs(456)))
    centrum_polygon = polygon((20, 50, 120), (
    rs(1262), rs(614), rs(1244), rs(558), rs(1223), rs(553), rs(1247), rs(539), rs(1243), rs(461), rs(1206), rs(462),
    rs(1208), rs(455), rs(1288), rs(443), rs(1337), rs(454), rs(1382), rs(461), rs(1397), rs(500), rs(1375), rs(506),
    rs(1322), rs(574)))
    feijenoord_polygon = polygon((20, 50, 120), (
    rs(1397), rs(500), rs(1375), rs(506), rs(1322), rs(574), rs(1262), rs(614), rs(1288), rs(642), rs(1378), rs(617),
    rs(1372), rs(694), rs(1361), rs(698), rs(1361), rs(720), rs(1417), rs(772), rs(1454), rs(735), rs(1487), rs(735),
    rs(1496), rs(698), rs(1450), rs(605), rs(1469), rs(593), rs(1453), rs(522)))
    ijsselmonde_polygon = polygon((20, 50, 120), (
    rs(1572), rs(594), rs(1489), rs(616), rs(1469), rs(593), rs(1450), rs(605), rs(1496), rs(698), rs(1487), rs(735),
    rs(1454), rs(735), rs(1417), rs(772), rs(1457), rs(824), rs(1524), rs(831), rs(1574), rs(813), rs(1657), rs(766),
    rs(1666), rs(779), rs(1682), rs(769), rs(1712), rs(606), rs(1625), rs(584)))
    charlois_polygon = polygon((20, 50, 120), (
    rs(1262), rs(614), rs(1288), rs(642), rs(1378), rs(617), rs(1372), rs(694), rs(1361), rs(698), rs(1361), rs(720),
    rs(1417), rs(772), rs(1457), rs(824), rs(1388), rs(820), rs(1315), rs(848), rs(1315), rs(869), rs(1242), rs(871),
    rs(1161), rs(839), rs(1201), rs(824), rs(1218), rs(800), rs(1201), rs(792), rs(1199), rs(763), rs(1246), rs(656),
    rs(1225), rs(646), rs(1227), rs(620)))
    waalhaven_polygon = polygon((20, 50, 120), (
    rs(1161), rs(839), rs(1201), rs(824), rs(1218), rs(800), rs(1201), rs(792), rs(1199), rs(763), rs(1246), rs(656),
    rs(1225), rs(646), rs(1227), rs(620), rs(1113), rs(596), rs(1038), rs(610), rs(954), rs(639), rs(862), rs(618),
    rs(885), rs(658), rs(917), rs(663), rs(921), rs(647), rs(972), rs(670), rs(962), rs(722), rs(937), rs(743), rs(934),
    rs(764), rs(923), rs(765), rs(927), rs(797), rs(1048), rs(795)))


''''The name of the area that is displayed in the top centre.'''
text = Label(root,width=0, height=1,text="",font=("Helvetica",35,"bold")) #Creates text
text.grid(row=0,column=0,sticky=N) #Draws the text


''''Function that gives mouse positions'''
def motion(event):
    if event.x > 500 and event.y < 279:
        text.config(text="")
    else:
        text.config(text="Rotterdam")

'''triggers for when an area gets selected'''''
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


''''Array of the trigger objects'''
List1 = [overschie_trigger, hillegersberg_trigger,prins_alexander_trigger,noord_trigger, kralingen_crooswijk_trigger, centrum_trigger, delftshaven_trigger, waalhaven_trigger, charlois_trigger, feijenood_trigger, ijsselmonde_trigger]


''''With this the selected polygons(area's) are recognized'''''
def click(event):
    if str(canvas.find_withtag(CURRENT)) == "(1,)": #every polygon(area) has his own tag
        text.config(text=overschie)
        for i in List1:
            if i.name == "overschie":
                setattr(i, 'trigger', True) #sets the clicked area to true

            else:
                setattr(i, 'trigger', False) #set the other area's to false
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



''''when a polygon(area) is clicked, the click method will be activated'''''
canvas.bind('<Button-1>', click, add="+") #binds the canvas to a method


''''Canvas that gets drawn'''
canvas.grid(row=2, column=0,sticky=N,rowspan=999,padx=55) #the lower the code(higher line) the later it will get drawn

''''Function that links the drop down menu sections to pages, it redirects to pages'''
def menuSelector(event):
    if  str(variable.get()) == "Home":
        lastPageArray.append("home") #When user visits a page, the page name will be added to the array
        home() #goes to the home page
    elif  str(variable.get()) == "Woningadvies":
         woningsadvies()
    elif str(variable.get()) == "Percentages en cijfers":
        percentagesEnCijfers()
    elif str(variable.get()) == "About":
        about()
    elif str(variable.get()) == "Settings":
        settings()
    elif str(variable.get()) == "Exit":
        root.destroy()

''''Drop down menu'''
variable = StringVar(root)
variable.set("Home")  # default value of the homebutton
menu_button = OptionMenu(root, variable, "Home", "Woningadvies", "Percentages en cijfers", "Settings", "About",
                             "Exit", command=menuSelector)
menu_button.config(font=("Helvetica", 50, "bold"), bg="DeepSkyBlue2", fg="white")
menu_button.grid(row=0, column=0, sticky=N + W)


''''Menu Text'''
welcome_text = "Select the home button to see the available options"
description_text = Label(root,text=welcome_text,font=("Helvetica",15,"bold")) #puts image on screen
description_text.grid(row=1,column=0,sticky=W)

''''the home page'''
def home():
    for widget in root.winfo_children(): #checks which wigets(buttons, text etc) are open
        if str(widget) == ".!optionmenu": #only the menu does not get deleted
            print("Not deleting optionmenu")
        elif str(widget) == ".!canvas": #the canvas only gets forgotten(hidden) and not deleted.
            widget.grid_forget()
            print("Canvas is forgotten")
        else:
            widget.destroy() #Other widgets are destroyed and so are their value
            print(str(widget) + " Is deleted")

''''the settings page'''
def settings():
    for widget in root.winfo_children():
        if str(widget) == ".!optionmenu":
            print("Not deleting optionmenu")
        elif str(widget) == ".!canvas":
            widget.grid_forget()
            print("Canvas is forgotten")
        else:
            widget.destroy()
            print(str(widget) + " Is deleted")

    ''''Resolution'''
    resolution_text = "Select your screen resolution"
    resolution1_text = Label(root, text=resolution_text, font=("Helvetica", 15, "bold"))  # puts image on screen
    resolution1_text.grid(row=2, column=0, sticky=W)

    ''''The drop down resolution menu'''
    variable1 = StringVar(root)
    variable1.set(str(screenx) + " x " + str(screeny))  # default value
    menu_button1 = OptionMenu(root, variable1, "1280x720", "1600x900", "1920x1080", "4k")
    menu_button1.config(font=("Helvetica", 20, "bold"), bg="DeepSkyBlue2", fg="white")
    menu_button1.grid(row=3, column=0, sticky=N + W)
    lastPageArray.append("settings") #adds last visited page to array


''''The about page'''
def about():
    for widget in root.winfo_children():
        if str(widget) == ".!optionmenu":
            print("Not deleting the optionmenu")
        elif str(widget) == ".!canvas":
            widget.grid_forget()
            print("Canvas is forgotten")
        else:
            widget.destroy()
            print(str(widget) + " Is deleted")

    about_text = "This application is made by first year Informatica students of the Hogeschool Rotterdam."
    about1_text = "- Chris Santema"
    about2_text = "- Sebastiaan Van Etten"
    about3_text = "- Stefan Pesic"
    about4_text = "- Milan Sas"
    about5_text = " © 2017 Team NoGo"

    about_information = Label(root, width=0, text=about_text, font=("Helvetica", 20, "bold"))  # puts text on screen
    about_information.grid(row=1, column=0, sticky=W)

    about_information1 = Label(root, width=0, text=about1_text, font=("Helvetica", 20, "bold"))
    about_information1.grid(row=2, column=0, sticky=W)

    about_information2 = Label(root, width=0, text=about2_text, font=("Helvetica", 20, "bold"))
    about_information2.grid(row=3, column=0, sticky=W)

    about_information3 = Label(root, width=0, text=about3_text, font=("Helvetica", 20, "bold"))
    about_information3.grid(row=4, column=0, sticky=W)

    about_information4 = Label(root, width=0, text=about4_text, font=("Helvetica", 20, "bold"))
    about_information4.grid(row=5, column=0, sticky=W)

    about_information5 = Label(root, width=0, text=about5_text, font=("Helvetica", 20, "bold"))
    about_information5.grid(row=6, column=0, sticky=W)

    lastPageArray.append("about")


''''Percentages en cijfers page'''
def percentagesEnCijfers():
    for widget in root.winfo_children():
        if str(widget) == ".!optionmenu":
            print("Optionmenu is not deleted")
        elif str(widget) == ".!canvas":
            widget.grid_forget()
            print("Canvas is forgotten")
        else:
            widget.destroy()
            print(str(widget) + " Is deleted")

    button9 = NewButton("Population", 1, 0, screenx / 30, screeny / 150)
    button9.pageClick(categoryPopulation) #Goes to the sub categories
    button10 = NewButton("Environment", 2, 0, screenx / 45, screeny / 150)
    button10.pageClick(categoryEnvironment)
    button11 = NewButton("Safety", 3, 0, screenx / 17, screeny / 150)
    button11.pageClick(categorySafety)
    button12 = NewButton("Traffic", 4, 0, screenx / 17, screeny / 150)
    button12.pageClick(categoryTraffic)
    button13 = NewButton("Services", 5, 0, screenx / 22, screeny / 150)
    button13.pageClick(categoryServices)
    button14 = NewButton("Overig", 6, 0, screenx / 18, screeny / 150)
    button14.pageClick(categoryOther)
    lastPageArray.append("pec")
    button52 = NewButton("Give me the statistics", 28, 0, screenx / 600, screeny / 150)

''''The woningsadvies radiobuttons, these will catch the value of a button. It knows which button the user has selected'''''
bevolking_radioButtons = IntVar()
milieu_radioButtons = IntVar()
veiligheid_radioButtons = IntVar()
verkeer_radioButtons = IntVar()
voorzieningen_radioButtons = IntVar()

''''Woningsadvies page'''
def woningsadvies():
    global bevolking_radioButtons
    global milieu_radioButtons
    global veiligheid_radioButtons
    global verkeer_radioButtons
    global voorzieningen_radioButtons

    for widget in root.winfo_children():
        if str(widget) == ".!optionmenu":
            print("Optionmenu will not be deleted")
        elif str(widget) == ".!canvas":
            widget.grid_forget()
            print("Canvas is forgotten")
        else:
            widget.destroy()
            print(str(widget) + " Is deleted")

    woningsadvies_text = "Select your importance on the categories below"
    woningsadvies_text1 = "Population"
    woningsadvies_text2 = "Environment"
    woningsadvies_text3 = "Safety"
    woningsadvies_text4 = "Traffic"
    woningsadvies_text5 = "Services"

    ''''The selection buttons'''''
    woningsadvies__headText = Label(root, width=0, text=woningsadvies_text, font=("Helvetica", 20, "bold"))
    woningsadvies__headText.grid(row=2, column=0, sticky=W)

    ''''the bevolking/population part'''''
    bevolking_text = Label(root, width=0, text=woningsadvies_text1, font=("Helvetica", 20, "bold"))
    bevolking_text.grid(row=3, column=0, sticky=W)

    Radiobutton(root, indicatoron=False, text="3 or lower", variable=bevolking_radioButtons, value=1).grid(column=0,
                                                                                                           row=4,
                                                                                                           sticky=W)
    Radiobutton(root, indicatoron=False, text="Between 3 and 5.5", variable=bevolking_radioButtons, value=2).grid(
        column=0, row=5, sticky=W)
    Radiobutton(root, indicatoron=False, text="Between 5.5 and 7", variable=bevolking_radioButtons, value=3).grid(
        column=0, row=6, sticky=W)
    Radiobutton(root, indicatoron=False, text="7 or higher", variable=bevolking_radioButtons, value=4).grid(column=0,
                                                                                                            row=7,
                                                                                                            sticky=W)

    ''''The Milieu/Economy part'''
    milieu_text = Label(root, width=0, text=woningsadvies_text2, font=("Helvetica", 20, "bold"))
    milieu_text.grid(row=8, column=0, sticky=W)
    Radiobutton(root, indicatoron=False, text="3 or lower", variable=milieu_radioButtons, value=1).grid(column=0, row=9,
                                                                                                        sticky=W)
    Radiobutton(root, indicatoron=False, text="Between 3 and 5.5", variable=milieu_radioButtons, value=2).grid(column=0,
                                                                                                               row=10,
                                                                                                               sticky=W)
    Radiobutton(root, indicatoron=False, text="Between 5.5 and 7", variable=milieu_radioButtons, value=3).grid(column=0,
                                                                                                               row=11,
                                                                                                               sticky=W)
    Radiobutton(root, indicatoron=False, text="7 or higher", variable=milieu_radioButtons, value=4).grid(column=0,
                                                                                                         row=12,
                                                                                                         sticky=W)

    ''''The Veiligheid/Safety part'''
    veiligheid_text = Label(root, width=0, text=woningsadvies_text3, font=("Helvetica", 20, "bold"))
    veiligheid_text.grid(row=13, column=0, sticky=W)
    Radiobutton(root, indicatoron=False, text="3 or lower", variable=veiligheid_radioButtons, value=1).grid(column=0,
                                                                                                            row=14,
                                                                                                            sticky=W)
    Radiobutton(root, indicatoron=False, text="Between 3 and 5.5", variable=veiligheid_radioButtons, value=2).grid(
        column=0, row=15, sticky=W)
    Radiobutton(root, indicatoron=False, text="Between 5.5 and 7", variable=veiligheid_radioButtons, value=3).grid(
        column=0, row=16, sticky=W)
    Radiobutton(root, indicatoron=False, text="7 or higher", variable=veiligheid_radioButtons, value=4).grid(column=0,
                                                                                                             row=17,
                                                                                                             sticky=W)

    ''''The verkeer/trafic part'''
    verkeer_text = Label(root, width=0, text=woningsadvies_text4, font=("Helvetica", 20, "bold"))
    verkeer_text.grid(row=18, column=0, sticky=W)

    Radiobutton(root, indicatoron=False, text="3 or lower", variable=verkeer_radioButtons, value=1).grid(column=0,
                                                                                                         row=19,
                                                                                                         sticky=W)
    Radiobutton(root, indicatoron=False, text="Between 3 and 5.5", variable=verkeer_radioButtons, value=2).grid(
        column=0, row=20, sticky=W)
    Radiobutton(root, indicatoron=False, text="Between 5.5 and 7", variable=verkeer_radioButtons, value=3).grid(
        column=0, row=21, sticky=W)
    Radiobutton(root, indicatoron=False, text="7 or higher", variable=verkeer_radioButtons, value=4).grid(column=0,
                                                                                                          row=22,
                                                                                                          sticky=W)

    ''''The voorzieningen/services part'''
    voorzieningen_text = Label(root, width=0, text=woningsadvies_text5, font=("Helvetica", 20, "bold"))
    voorzieningen_text.grid(row=23, column=0, sticky=W)

    Radiobutton(root, indicatoron=False, text="3 or lower", variable=voorzieningen_radioButtons, value=1).grid(column=0,
                                                                                                               row=24,
                                                                                                               sticky=W)
    Radiobutton(root, indicatoron=False, text="Between 3 and 5.5", variable=voorzieningen_radioButtons, value=2).grid(
        column=0, row=25, sticky=W)
    Radiobutton(root, indicatoron=False, text="Between 5.5 and 7", variable=voorzieningen_radioButtons, value=3).grid(
        column=0, row=26, sticky=W)
    Radiobutton(root, indicatoron=False, text="7 or higher", variable=voorzieningen_radioButtons, value=4).grid(
        column=0, row=27, sticky=W,comnmand=databaseWoningsAdvies())
    lastPageArray.append("woon")
    button51 = NewButton("I am ready to see my living options ", 28, 0, screenx / 600, screeny / 150)
    button51.pageClick(databaseWoningsAdvies)
    canvas.grid(row=2, column=0, sticky=N, rowspan=999, padx=55)
    polygons()

''''The buttonarray to remember the previous clicked button for the database method to know which method to activate'''
buttonArray = []

''''Population/bevolking category, when it gets clicked these buttons appears'''
def categoryPopulation():
    global buttonArray
    button15 = NewButton("Population1_placehholder", 1, 0, screenx / 30, screeny / 150)
    button16 = NewButton("Population2_placeholder", 2, 0, screenx / 45, screeny / 150)
    button17 = NewButton("Population3_placeholder", 3, 0, screenx / 17, screeny / 150)
    button18 = NewButton("Population4_placeholder", 4, 0, screenx / 17, screeny / 150)
    button19 = NewButton("Population5_placeholder", 5, 0, screenx / 22, screeny / 150)
    button20 = NewButton("Population6_placeholder", 6, 0, screenx / 22, screeny / 150)
    buttonback1 = NewButton("Back", 7, 0, screenx / 22, screeny / 150)
    buttonback1.pageClick(percentagesEnCijfers)


    '''Gives which button is clicked'''
    #TODO refine it so the function correctly gives the button which is pressed and then to have the function: "databasePercentagesEnCijfers()" process it
    if button15.clicked == True:
        return 0
    elif button16.clicked == False:
        return 1
    elif button17.clicked == False:
        return 2
    elif button18.clicked == False:
        return 3
    elif button19.clicked == False:
        return 4
    elif button20.clicked == False:
        return 5
    else:
        return None

''''Environment/milieu category, when it gets clicked these buttons appears'''
def categoryEnvironment():
    button21 = NewButton("Environmennt1_placehholder", 1, 0, screenx / 30, screeny / 150)
    button22 = NewButton("Environment2_placeholder", 2, 0, screenx / 45, screeny / 150)
    button23 = NewButton("Environment3_placeholder", 3, 0, screenx / 17, screeny / 150)
    button24 = NewButton("Environment4_placeholder", 4, 0, screenx / 17, screeny / 150)
    button25 = NewButton("Environment5_placeholder", 5, 0, screenx / 22, screeny / 150)
    button26 = NewButton("Environment6_placeholder", 6, 0, screenx / 22, screeny / 150)
    buttonback2 = NewButton("Back", 7, 0, screenx / 22, screeny / 150)
    buttonback2.pageClick(percentagesEnCijfers)

''''Safety/veiligheid category, when it gets clicked these buttons appears'''
def categorySafety():
    button27 = NewButton("Safety1_placehholder", 1, 0, screenx / 30, screeny / 150)
    button28 = NewButton("Safety2_placeholder", 2, 0, screenx / 45, screeny / 150)
    button29 = NewButton("Safety3_placeholder", 3, 0, screenx / 17, screeny / 150)
    button30 = NewButton("Safety4_placeholder", 4, 0, screenx / 17, screeny / 150)
    button31 = NewButton("Safety5_placeholder", 5, 0, screenx / 22, screeny / 150)
    button32 = NewButton("Safety6_placeholder", 6, 0, screenx / 22, screeny / 150)
    buttonback3 = NewButton("Back", 7, 0, screenx / 22, screeny / 150)
    buttonback3.pageClick(percentagesEnCijfers)

''''Traffic/verkeer category, when it gets clicked these buttons appears'''
def categoryTraffic():
    button33 = NewButton("Traffic1_placehholder", 1, 0, screenx / 30, screeny / 150)
    button34 = NewButton("Traffic2_placeholder", 2, 0, screenx / 45, screeny / 150)
    button35 = NewButton("Traffic3_placeholder", 3, 0, screenx / 17, screeny / 150)
    button36 = NewButton("Traffic4_placeholder", 4, 0, screenx / 17, screeny / 150)
    button37 = NewButton("Traffic5_placeholder", 5, 0, screenx / 22, screeny / 150)
    button38 = NewButton("Traffic6_placeholder", 6, 0, screenx / 22, screeny / 150)
    buttonback4 = NewButton("Back", 7, 0, screenx / 22, screeny / 150)
    buttonback4.pageClick(percentagesEnCijfers)

''''Services/voorzieningen category, when it gets clicked these buttons appears'''
def categoryServices():
    button39 = NewButton("Services1_placehholder", 1, 0, screenx / 30, screeny / 150)
    button40 = NewButton("Services2_placeholder", 2, 0, screenx / 45, screeny / 150)
    button41 = NewButton("Services3_placeholder", 3, 0, screenx / 17, screeny / 150)
    button42 = NewButton("Services4_placeholder", 4, 0, screenx / 17, screeny / 150)
    button43 = NewButton("Services5_placeholder", 5, 0, screenx / 22, screeny / 150)
    button44 = NewButton("Services6_placeholder", 6, 0, screenx / 22, screeny / 150)
    buttonback5 = NewButton("Back", 7, 0, screenx / 22, screeny / 150)
    buttonback5.pageClick(percentagesEnCijfers)

''''Other/overig category, when it gets clicked these buttons appears'''
def categoryOther():
    button45 = NewButton("Other1_placehholder", 1, 0, screenx / 30, screeny / 150)
    button46 = NewButton("Other2_placeholder", 2, 0, screenx / 45, screeny / 150)
    button47 = NewButton("Other3_placeholder", 3, 0, screenx / 17, screeny / 150)
    button48 = NewButton("Other4_placeholder", 4, 0, screenx / 17, screeny / 150)
    button49 = NewButton("Other5_placeholder", 5, 0, screenx / 22, screeny / 150)
    button50 = NewButton("Other6_placeholder", 6, 0, screenx / 22, screeny / 150)
    buttonback6 = NewButton("Back", 7, 0, screenx / 22, screeny / 150)
    buttonback6.pageClick(percentagesEnCijfers)


''''Database query for the page: "Woningsadvies (the user gets data based on selection)'''''
def databaseWoningsAdvies():
    global bevolking_radioButtons
    global milieu_radioButtons
    global veiligheid_radioButtons
    global verkeer_radioButtons
    global voorzieningen_radioButtons

    if bevolking_radioButtons.get() == 0: #gets value of the radiobutton(which button the user selected)
        pass
    if bevolking_radioButtons.get() == 1:
        pass
    if bevolking_radioButtons.get() == 2:
        pass
    if bevolking_radioButtons.get() == 3:
        pass
    if bevolking_radioButtons.get() == 4:
        pass

    if milieu_radioButtons.get() == 0:
        pass
    if milieu_radioButtons.get() == 1:
        pass
    if milieu_radioButtons.get() == 2:
        pass
    if milieu_radioButtons.get() == 3:
        pass
    if milieu_radioButtons.get() == 4:
        pass

    if veiligheid_radioButtons.get() == 0:
        pass
    if veiligheid_radioButtons.get() == 1:
        pass
    if veiligheid_radioButtons.get() == 2:
        pass
    if veiligheid_radioButtons.get() == 3:
        pass
    if veiligheid_radioButtons.get() == 4:
        pass

    if verkeer_radioButtons.get() == 0:
        pass
    if verkeer_radioButtons.get() == 1:
        pass
    if verkeer_radioButtons.get() == 2:
        pass
    if verkeer_radioButtons.get() == 3:
        pass
    if verkeer_radioButtons.get() == 4:
        pass

    if voorzieningen_radioButtons.get() == 0:
        pass
    if voorzieningen_radioButtons.get() == 1:
        pass
    if voorzieningen_radioButtons.get() == 2:
        pass
    if voorzieningen_radioButtons.get() == 3:
        pass
    if voorzieningen_radioButtons.get() == 4:
        pass


''''Database query for the page: "Percentages en cijfers" '''
def databasePercentagesEnCijfers():
    #TODO refine the method. When a button is selected the program must know which button and then execute the querry
    if buttonArray in range(0, 7): #checks what the previous selected buton was , this way it knows which method to activate
        answer = categoryPopulation()   #result(which button is pressed) gets assigned to answer variable
    elif buttonArray in range(0,7):
        answer1 = categoryEnvironment()
    elif buttonArray in range(0,7):
        answer2 = categorySafety()
    elif buttonArray in range(0,7):
        answer3 = categoryTraffic()
    elif buttonArray in range(0,7):
        answer3 = categoryTraffic()
    elif buttonArray in range(0,7):
        answer4 = categoryServices()
    elif buttonArray in range(0,7):
        answer5 = categoryOther()


    if answer != None: #the result is stored in answer, based on the result, a certain database querry will be executed
        if answer == 0: #the numbers are buttons.
            pass
        elif answer == 1:
            pass
        elif answer == 2:
            pass
        elif answer == 3:
            pass
        elif answer == 4:
            pass
        elif answer == 5:
            pass

    if answer != None:
        if  answer1 == 0:
            pass
        elif answer1 == 1:
            pass
        elif answer1 == 2:
            pass
        elif answer1 == 3:
            pass
        elif answer1 == 4:
            pass
        elif answer1 == 5:
            pass

    elif answer2 != None:
        if answer2 == 0:
            pass
        elif answer2 == 1:
            pass
        elif answer2 == 2:
            pass
        elif answer2 == 3:
            pass
        elif answer2 == 4:
            pass
        elif answer2 == 5:
            pass

    elif answer3 != None:
        if answer3 == 0:
            pass
        elif answer3 == 1:
            pass
        elif answer3 == 2:
            pass
        elif answer3 == 3:
            pass
        elif answer3 == 4:
            pass
        elif answer3 == 5:
            pass
    elif answer4 != None:
        if answer4 == 0:
            pass
        elif answer4 == 1:
            pass
        elif answer4 == 2:
            pass
        elif answer4 == 3:
            pass
        elif answer4 == 4:
            pass
        elif answer4 == 5:
            pass

    elif answer5 != None:
        if answer5 == 0:
            pass
        elif answer5 == 1:
            pass
        elif answer5 == 2:
            pass
        elif answer5 == 3:
            pass
        elif answer5 == 4:
            pass
        elif answer5 == 5:
            pass


root.mainloop() #for the loop