from tkinter import * #Needed for GUI
import matplotlib #Needed for graph
matplotlib.use("TKAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

#TODO read the comments, the symbol: , is after lines. the symbol: '''''' , is to explain the overall code
#TODO when user clicks on an area, that area needs to be zoomed in

root = Tk() #Needed to run

''''Window'''
root.title("Rotterdam Living") #Window title
root.geometry('{}x{}'.format(root.winfo_screenwidth(), root.winfo_screenheight())) #Window doesn't automaticcaly resized this way

''''gets user's screen size (width and height)'''''
screenx = root.winfo_screenwidth() #width
screeny = root.winfo_screenheight() #height

''''Array that will save the last page the user has visited, this is used so elements can be cleared on the screen, it may be helpful for knowing which widgets to delete, but for now it is not used.'''''
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

''''The regular buttons. Every button has a trigger, when button is pressed the state is set to true and vice versa'''
class NewButton:
    def __init__(self,text, row, column, ipadx, ipady): #row = which row, column = which column, ipadx = width, ipady = height
        self.clicked = False #state
        self.button = Button(root, text =text, command = self.click,font=("arial",30,"bold"),bg="DeepSkyBlue2", fg="white")
        self.button.columnconfigure(0,weight=300000) #Weight = that the button get less likely moved when another button takes a lot of space
        self.button.grid(row=row, column=column, sticky=W, ipadx=ipadx, ipady=ipady) #The position and size of the button
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

''''The Percentage en cijfers buttons'''''
class PecButton:
    def __init__(self,text, row, column, ipadx, ipady, name):
        self.clicked = False
        self.button = Button(root, text =text, command = self.databaseSender,font=("arial",30,"bold"),bg="DeepSkyBlue2", fg="white")
        self.button.columnconfigure(0,weight=300000)
        self.button.grid(row=row, column=column, sticky=W, ipadx=ipadx, ipady=ipady)
        self.name = name #this is for the buttonArray to know what is the last button that is clicked

    def databaseSender(self):
        buttonArray.append(self.name) #the clicked button will go in the array
        databasePercentagesEnCijfers() #Opens the databasePercentageEnCijfers method that will create a database query.

''''The last clicked button from the page: "Percentages en cijfers", are saved in an array, this is for the: "databasePercentagesEnCijfers Function"'''
buttonArray = []

'''Trigger for the polygons(area's), to do something with an area when it's clicked'''''
class Trigger:
    def __init__(self, triggerValue,name):
        self.trigger = triggerValue
        self.name = name #name to uniquely identify the area.

''''The canvas, important variable. Everything gets drawn on the canvas'''
canvas = Canvas(root, width=screenx,height=screeny) #root is in which window it will get drawn on.

''''Function to set polygon's(area) size'''
def rs(size):
    ratio = (screeny + screeny/2) / size
    return (screeny / ratio)

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

''''The polygons(area's)'''''
overschie_polygon = polygon((20, 50, 120), (
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

''''Array that has the polygon area's, this is used to go through the array and then the colour will change. It is used in a database function'''
polygonsgebieden = [overschie_polygon, hillegersberg_polygon, prins_alexander_polygon, kralingen_polygon, noord_polygon, delftshaven_polygon, centrum_polygon, feijenoord_polygon, ijsselmonde_polygon, charlois_polygon, waalhaven_polygon]

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


''''With this the selected polygons(area's) are recognized when they are clicked on. '''''
def click(event):
    if str(canvas.find_withtag(CURRENT)) == "(1,)": #every polygon(area) has his own tag
        text.config(text=overschie) #Text changes to the name of the selected area
        for i in List1: #Goes through the array of the area triggers.
            if i.name == "overschie":#Name is the attribute of the area's triggers, this is used to uniquely identify the area
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
canvas.bind('<Button-1>', click, add="+") #Binds the canvas to the click method

''''Canvas that gets drawn'''
canvas.grid(row=2, column=0,sticky=N,rowspan=999,padx=55) #the lower the code(higher line) the later it will get drawn

''''Function that links the drop down menu sections to pages, it redirects to pages'''
def menuSelector(event):
    if  str(variable.get()) == "Home": #variable is the drop down menu, when a menu page is selected, the value of the variable changes
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
variable = StringVar(root) #Variable will store the page that is selected
variable.set("Home")  # default value is the homebutton
menu_button = OptionMenu(root, variable, "Home", "Woningadvies", "Percentages en cijfers", "Settings", "About",
                             "Exit", command=menuSelector) #The pages that are in the drop down menu
menu_button.config(font=("Helvetica", 50, "bold"), bg="DeepSkyBlue2", fg="white") #Changes the font/size of the drop down menu
menu_button.grid(row=0, column=0, sticky=N + W) #Sets the position of the drop down menu

''''Menu Text'''
welcome_text = "Select the home button to see the available options" #Test that appears on the menu
description_text = Label(root,text=welcome_text,font=("Helvetica",15,"bold")) #Sets the text on the page
description_text.grid(row=1,column=0,sticky=W) #Sets the position of the text

''''the home page'''
def home():
    for widget in root.winfo_children(): #checks which wigets(buttons, text etc) are open
        if widget == menu_button: #The menu does not get deleted
            print("Optionmenu")
        elif widget == canvas: #The canvas will not be deleted
            print("canvas")
        else:
            widget.destroy() #Other widgets are destroyed and so are their value
            print(str(widget) + ": Is deleted")

''''the settings page'''
def settings():
    for widget in root.winfo_children():
        if widget == menu_button: #menubutton does not get deleted
            print("Optionmenu")
        elif widget == canvas: #canvas does not get deleted
            print("canvas")
        else:
            widget.destroy() #other widgets get deleted and so are their value
            print(str(widget) + ": Is deleted")

    ''''Resolution'''
    resolution_text = "Select your screen resolution"
    resolution1_text = Label(root, text=resolution_text, font=("Helvetica", 15, "bold"))
    resolution1_text.grid(row=2, column=0, sticky=W)

    ''''The drop down resolution menu'''
    variable1 = StringVar(root)  #Variable will store the page that is selected
    variable1.set(str(screenx) + " x " + str(screeny))  # default value of the drop down menu
    menu_button1 = OptionMenu(root, variable1, "1280x720", "1600x900", "1920x1080", "4k")  #The options of the drop down menu
    menu_button1.config(font=("Helvetica", 20, "bold"), bg="DeepSkyBlue2", fg="white") #Sets the font/size of drop down menu
    menu_button1.grid(row=3, column=0, sticky=N + W) #Sets position of the drop down menu
    lastPageArray.append("settings") #adds last visited page to array, this is currently not used but may be used for later


''''The about page'''
def about():
    for widget in root.winfo_children():
        if widget == menu_button: #Optionmenu does not get deleted
            print("Optionmenu")
        elif widget == canvas: #Canvas does not get deleted
            print("canvas")
        else:
            widget.destroy() #Other widgets are deleted and so are their value
            print(str(widget) + " Is deleted")

    about_text = "This application is made by first year Informatica students of the Hogeschool Rotterdam."
    about1_text = "- Chris Santema"
    about2_text = "- Sebastiaan Van Etten"
    about3_text = "- Stefan Pesic"
    about4_text = "- Milan Sas"
    about5_text = " © 2017 Team NoGo"

    about_information = Label(root, width=0, text=about_text, font=("Helvetica", 20, "bold"))  # puts text on screen
    about_information.grid(row=1, column=0, sticky=W) #Sets the position of the test

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

    lastPageArray.append("about") #Adds last visited page to the array, may be used but is not used now


''''Percentages en cijfers page'''
def percentagesEnCijfers():
    for widget in root.winfo_children():
        if widget == menu_button: #Menu button will not be deleted
            print("Optionmenu is not deleted")
        elif widget == canvas: #Canvas will not be deleted
            print("canvas")
        else:
            widget.destroy() #Other widgets are deleted
            print(str(widget) + " Is deleted")

    button9 = NewButton("Population", 1, 0, screenx / 30, screeny / 150) #Creates button
    button9.pageClick(categoryPopulation) #Goes to the sub categories of the selected button
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
    button52 = NewButton("Give me the statistics", 28, 0, screenx / 600, screeny / 150)  #Currently not used, can be used to give the user stats when clicked
    lastPageArray.append("pec")

''''The woningsadvies radiobuttons, these will catch the value of a button. It knows which button the user has selected'''''
bevolking_radioButtons = IntVar() #The value will change when a certain button is selected. Every button has his own value, and that value the main radiobutton will get
milieu_radioButtons = IntVar()
veiligheid_radioButtons = IntVar()
verkeer_radioButtons = IntVar()
voorzieningen_radioButtons = IntVar()

''''Woningsadvies page'''
def woningsadvies():
    global bevolking_radioButtons #Reads a global variable, this was one of the best options for this
    global milieu_radioButtons
    global veiligheid_radioButtons
    global verkeer_radioButtons
    global voorzieningen_radioButtons

    for widget in root.winfo_children():
        if widget == menu_button: #Menu does not get deleted
            print("Optionmenu will not be deleted")
        elif widget == canvas: #Canvas does not get deleted
            print("canvas")
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
    woningsadvies__headText = Label(root, width=0, text=woningsadvies_text, font=("Helvetica", 20, "bold")) #Creats the text
    woningsadvies__headText.grid(row=2, column=0, sticky=W) #Sets position of the text

    ''''the bevolking/population part with radiobuttons'''''
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

    ''''The Milieu/Economy part with radiobuttons'''
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

    ''''The Veiligheid/Safety part with radiobuttons'''
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

    ''''The verkeer/trafic part with radiobuttons'''
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

    ''''The voorzieningen/services part with radiobuttons'''
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


''''Population/bevolking category, when it gets clicked these buttons appears, and when buttons are clicked they will go to the database function'''
def categoryPopulation():
    button15 = PecButton("Population1_placehholder", 1, 0, screenx / 30, screeny / 150, 0)
    button16 = PecButton("Population2_placeholder", 2, 0, screenx / 45, screeny / 150,1)
    button17 = PecButton("Population3_placeholder", 3, 0, screenx / 17, screeny / 150,2)
    button18 = PecButton("Population4_placeholder", 4, 0, screenx / 17, screeny / 150,3)
    button19 = PecButton("Population5_placeholder", 5, 0, screenx / 22, screeny / 150,4)
    button20 = PecButton("Population6_placeholder", 6, 0, screenx / 22, screeny / 150,5)
    buttonback1 = NewButton("Back", 7, 0, screenx / 22, screeny / 150)
    buttonback1.pageClick(percentagesEnCijfers) #The back button

''''Population/bevolking category, when it gets clicked these buttons appears, and when buttons are clicked they will go to the database function'''
def categoryEnvironment():
    button21 = PecButton("Environmennt1_placehholder", 1, 0, screenx / 30, screeny / 150,6)
    button22 = PecButton("Environment2_placeholder", 2, 0, screenx / 45, screeny / 150,7)
    button23 = PecButton("Environment3_placeholder", 3, 0, screenx / 17, screeny / 150,8)
    button24 = PecButton("Environment4_placeholder", 4, 0, screenx / 17, screeny / 150,9)
    button25 = PecButton("Environment5_placeholder", 5, 0, screenx / 22, screeny / 150,10)
    button26 = PecButton("Environment6_placeholder", 6, 0, screenx / 22, screeny / 150,11)
    buttonback2 = NewButton("Back", 7, 0, screenx / 22, screeny / 150)
    buttonback2.pageClick(percentagesEnCijfers)

''''Population/bevolking category, when it gets clicked these buttons appears, and when buttons are clicked they will go to the database function'''
def categorySafety():
    button27 = PecButton("Safety1_placehholder", 1, 0, screenx / 30, screeny / 150,12)
    button28 = PecButton("Safety2_placeholder", 2, 0, screenx / 45, screeny / 150,12)
    button29 = PecButton("Safety3_placeholder", 3, 0, screenx / 17, screeny / 150,13)
    button30 = PecButton("Safety4_placeholder", 4, 0, screenx / 17, screeny / 150,14)
    button31 = PecButton("Safety5_placeholder", 5, 0, screenx / 22, screeny / 150,15)
    button32 = PecButton("Safety6_placeholder", 6, 0, screenx / 22, screeny / 150,16)
    buttonback3 = NewButton("Back", 7, 0, screenx / 22, screeny / 150)
    buttonback3.pageClick(percentagesEnCijfers)

''''Population/bevolking category, when it gets clicked these buttons appears, and when buttons are clicked they will go to the database function'''
def categoryTraffic():
    button33 = PecButton("Traffic1_placehholder", 1, 0, screenx / 30, screeny / 150,17)
    button34 = PecButton("Traffic2_placeholder", 2, 0, screenx / 45, screeny / 150,18)
    button35 = PecButton("Traffic3_placeholder", 3, 0, screenx / 17, screeny / 150,19)
    button36 = PecButton("Traffic4_placeholder", 4, 0, screenx / 17, screeny / 150,20)
    button37 = PecButton("Traffic5_placeholder", 5, 0, screenx / 22, screeny / 150,21)
    button38 = PecButton("Traffic6_placeholder", 6, 0, screenx / 22, screeny / 150,22)
    buttonback4 = NewButton("Back", 7, 0, screenx / 22, screeny / 150)
    buttonback4.pageClick(percentagesEnCijfers)

''''Population/bevolking category, when it gets clicked these buttons appears, and when buttons are clicked they will go to the database function'''
def categoryServices():
    button39 = PecButton("Services1_placehholder", 1, 0, screenx / 30, screeny / 150,23)
    button40 = PecButton("Services2_placeholder", 2, 0, screenx / 45, screeny / 150,24)
    button41 = PecButton("Services3_placeholder", 3, 0, screenx / 17, screeny / 150,25)
    button42 = PecButton("Services4_placeholder", 4, 0, screenx / 17, screeny / 150,26)
    button43 = PecButton("Services5_placeholder", 5, 0, screenx / 22, screeny / 150,27)
    button44 = PecButton("Services6_placeholder", 6, 0, screenx / 22, screeny / 150,28)
    buttonback5 = NewButton("Back", 7, 0, screenx / 22, screeny / 150)
    buttonback5.pageClick(percentagesEnCijfers)

''''Population/bevolking category, when it gets clicked these buttons appears, and when buttons are clicked they will go to the database function'''
def categoryOther():
    button45 = PecButton("Other1_placehholder", 1, 0, screenx / 30, screeny / 150,29)
    button46 = PecButton("Other2_placeholder", 2, 0, screenx / 45, screeny / 150,30)
    button47 = PecButton("Other3_placeholder", 3, 0, screenx / 17, screeny / 150,31)
    button48 = PecButton("Other4_placeholder", 4, 0, screenx / 17, screeny / 150,32)
    button49 = PecButton("Other5_placeholder", 5, 0, screenx / 22, screeny / 150,33)
    button50 = PecButton("Other6_placeholder", 6, 0, screenx / 22, screeny / 150,34)
    buttonback6 = NewButton("Back", 7, 0, screenx / 22, screeny / 150)
    buttonback6.pageClick(percentagesEnCijfers)

''''Based on the data, the colour of the map changes, the data represents the query that will come in the function'''
def ShowResults(data):
    global polygonsgebieden #The array of area's
    data = {"Charlois":50, "Overschie":90} #Dictionary to simulate a query, this is to test the query
    for result in data: #goes in the dictionary (the query)
            for gebied in polygonsgebieden: #Goes in the area's array
                if result == "Charlois": #Checks if result from the query is equal to an area
                    result = int(data.get(result)) #Converts the dictionary value to an int
                    changecolor(charlois_polygon, result) #Changes color of the area and also change colour based on percentage
                elif result == "Overschie":
                    pass
                elif result == "Hillegersberg":
                    pass
                elif result == "Prins Alexander":
                    pass
                elif result == "Kralingen":
                    pass
                elif result == "Noord":
                    pass
                elif result == "Delftshaven":
                    pass
                elif result == "Noord":
                    pass
                elif result == "Centrum":
                    pass
                elif result == "Feijennoord":
                    pass
                elif result == "Waalhaven":
                    pass

    f = Figure(figsize=(5, 5), dpi=50)
    a = f.add_subplot(111)  # means 1 chart 1 by 1
    a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 2, 4, 4, 3, 5, 3])
    Figure1 = FigureCanvasTkAgg(f, root)
    Figure1.show()
    Figure1.get_tk_widget().grid(row=0, column=0, sticky=N, rowspan=30)


''''Database query for the page: "Woningsadvies (the user gets data based on selection)'''''
def databaseWoningsAdvies():
    global bevolking_radioButtons
    global milieu_radioButtons
    global veiligheid_radioButtons
    global verkeer_radioButtons
    global voorzieningen_radioButtons

    print(bevolking_radioButtons.get()) #To prove that when a different radiobutton is selected, the value changes
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


''''Database query for the page: "Percentages en cijfers" the plot graphics '''
''''Function to have the results from the database change the colour of a polygon(area)'''
def changecolor(object,percent): #object = polygon/area, and the percent is the percentage comes from the query
    red = 0
    green = 0
    if percent <= 30: #If the percentage is a certain ammount, the colour of the area/polygon will change
        red = 255
        green = 16
    elif percent > 30 and percent <= 70:
        red = 255
        green = 255
    elif percent > 70 and percent <= 100:
        green = 255
        red = 16
    color = (red, green, 16) #3th value must be 16 or above
    canvas.itemconfig(object.shape, fill=HexToRGB(color)) #Changes the colour of the area

''''Database query for the page: "Percentages en cijfers"'''
''''This page will be called when buttons from the: "Percentages en cijfers", are selected. The method call is set in the class of the buttons'''
def databasePercentagesEnCijfers():
    global buttonArray #needed because the array has the last selected button of the page: "Percentages en cijfers'
    answer = (buttonArray[-1]) #last selected button gets stored in answer
    print(answer) #To prove that the last selected button is saved in the array
    data = [] #Here comes the query, for every button a new query should be appended to the array

    # TODO ResultQuery = []
    if answer == 0:  #the numbers represent the button, each button has his own number. The attribute of the button that stores this is: name
        ShowResults(data) #The query get send into the showresults function, then the map colour gets changed based on the results from it
    elif answer == 1:
        ShowResults(data)
    elif answer == 2:
        ShowResults(data)
    elif answer == 3:
        ShowResults(data)
    elif answer == 4:
        ShowResults(data)
    elif answer == 5:
        ShowResults(data)

    elif  answer == 6:
        ShowResults(data)
    elif answer == 7:
        ShowResults(data)
    elif answer == 8:
        ShowResults(data)
    elif answer == 9:
        ShowResults(data)
    elif answer == 10:
        ShowResults(data)
    elif answer == 11:
        ShowResults(data)

    elif answer == 12:
        ShowResults(data)
    elif answer == 13:
        ShowResults(data)
    elif answer == 14:
        ShowResults(data)
    elif answer == 15:
        ShowResults(data)
    elif answer == 16:
        ShowResults(data)
    elif answer == 17:
        ShowResults(data)

    elif answer == 18:
        ShowResults(data)
    elif answer == 19:
        ShowResults(data)
    elif answer == 20:
        ShowResults(data)
    elif answer == 21:
        ShowResults(data)
    elif answer == 22:
        ShowResults(data)
    elif answer == 23:
        ShowResults(data)

    elif answer == 24:
        ShowResults(data)
    elif answer == 25:
        ShowResults(data)
    elif answer == 26:
        ShowResults(data)
    elif answer == 27:
        ShowResults(data)
    elif answer == 28:
        ShowResults(data)
    elif answer == 29:
        ShowResults(data)

    elif answer == 30:
        ShowResults(data)
    elif answer == 31:
        ShowResults(data)
    elif answer == 32:
        ShowResults(data)
    elif answer == 33:
        ShowResults(data)
    elif answer == 34:
        ShowResults(data)
    elif answer == 35:
        ShowResults(data)

root.mainloop() #for the loop