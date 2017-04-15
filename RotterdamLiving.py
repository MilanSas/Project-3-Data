from tkinter import * #Needed for GUI
import matplotlib #Needed for graph
import Polygons
matplotlib.use("TKAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from PlotsClass import Plot, PlotBarChart, PlotLineChart, PlotOnMap
import time
#TODO read the comments, the symbol: , is after lines. the symbol: '''''' , is to explain the overall code
#TODO when user clicks on an area, that area needs to be zoomed in

root = Tk() #Needed to run
root.resizable(width=False, height=False)#no free-resizable possible while running

''''gets user's screen size (width and height)'''''
screenx = root.winfo_screenwidth() #width
screeny = root.winfo_screenheight() #height

''''Window'''
root.title("Rotterdam Living") #Window title
root.geometry('{}x{}'.format(screenx, screeny)) #Window doesn't automaticcaly resized this way



''''Array that will save the last page the user has visited, this is used so elements can be cleared on the screen, it may be helpful for knowing which widgets to delete, but for now it is not used.'''''

''''Area Text (names of the area that get loaded when user clicks the area'''''
overschie = "Overschie"
hillegersberg_schiebroek = "Hillegersberg-Schiebroek"
prins_alexander = "Prins Alexander"
kralingen_crooswijk = "Kralingen-Crooswijk"
noord = "Noord"
delftshaven = "Delfshaven"
centrum = "Centrum"
waalhaven = "Waalhaven"
charlois = "Charlois"
feijenood = "Feijenoord"
ijsselmonde = "Ijsselmonde"
rotterdam = "Rotterdam"

''''Saves last page, '''
searchPage = None

''''The regular buttons. Every button has a trigger, when button is pressed the state is set to true and vice versa'''
class NewButton:
    def __init__(self,text, row, column, ipadx, ipady): #row = which row, column = which column, ipadx = width, ipady = height
        self.clicked = False #state
        self.var = 28 - len(text)
        self.button = Button(root, text =(" " + text+ str(" "*self.var)), command = self.click,font=("courier",15,"bold"),bg="DeepSkyBlue2", fg="white")
        self.button.columnconfigure(0,weight=300000) #Weight = that the button get less likely moved when another button takes a lot of space
        self.button.grid(row=row, column=column, sticky=W, ipadx=0, ipady=ipady) #The position and size of the button

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
        self.var = 28 - len(text)

        self.button = Button(root, text =(" " + text + str(" "*self.var)), command = self.databaseSender,font=("courier",15,"bold"),bg="DeepSkyBlue2", fg="white")
        self.button.columnconfigure(0,weight=300000)
        self.button.grid(row=row, column=column, sticky=W, ipadx=0, ipady=ipady)
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
canvasWijk = Canvas(root, width=screenx,height=screeny) #This canvas is for the wijken



''''Function to set polygon's(area) size'''
def rs(size):
    ratio = 1080 / size
    return (screeny / ratio)

''''Function that changes the size of the wijken'''
def rsWijken(size):
    ratio = 1080 / size
    return (screeny / ratio)


'''Function that Converts hex to RGB'''
def HexToRGB(rgb):
    #RGB WAARDES MOETEN TUSSEN 16 - 255
    result = ('#' + str(hex(rgb[0]).split('x')[-1]) + str(hex(rgb[1]).split('x')[-1]) + str(hex(rgb[2]).split('x')[-1]))
    return result

''''Function to create the polygons(area's)'''
geselecteerdegebieden = []

numcolor = 0
def getcolor():
    global numcolor
    selectcolors = ['red', 'cyan', 'hot pink', 'orange', 'saddle brown', 'green2', 'yellow', 'dark green', 'purple1',
                    'SlateGray4', 'khaki2']
    color = selectcolors[numcolor]
    numcolor += 1
    return color


class polygon:
    def __init__(self,name,color,list):
        self.name = name
        self.color = color
        self.selected = False
        self.shape = canvas.create_polygon(list, fill=(HexToRGB(color)), outline='black', width=2, tags = self.name)
        canvas.move(self.shape, rs(-400), 0)
        self.selectcolor = getcolor()


    def ChangeColor(self, percent):
        colorchange = percent * 255 //100
        changedcolor = 255
        for n in range(20):
            if changedcolor >= 16:
                color = (changedcolor, changedcolor, 255)
                canvas.itemconfig(self.shape, fill=HexToRGB(color))
                changedcolor = changedcolor - (colorchange // 20)
                root.update()
                time.sleep(0.00000000000001)
        finalcolor = 255 - colorchange
        if finalcolor < 16:
            color = (16, 16, 255)
            canvas.itemconfig(self.shape, fill=HexToRGB(color))
            root.update()
        else:
            color = (finalcolor, finalcolor, 255)
            canvas.itemconfig(self.shape, fill=HexToRGB(color))
            root.update()



    def Select(self):
        if self.selected:
            self.deSelect()
            return
        geselecteerdegebieden.append(self)
        self.selected = True
        canvas.itemconfig(self.shape, outline = self.selectcolor, width = 6)

    def deSelect(self):
        geselecteerdegebieden.remove(self)
        self.selected = False
        canvas.itemconfig(self.shape, outline='black', width = 2)

class lagenda():
    def __init__(self):
        self.pos = 100
        for i in range(80):
            color = (255 - i*3, 255 - i*3, 255)
            self.shape = canvas.create_rectangle(50,i * 10,100,i * 10 + 10, fill=(HexToRGB(color)), outline='black')
            canvas.move(self.shape,rs(1700),rs(50))
lagenda = lagenda()



''''This function gets loaded when the area: "Overschie", gets selected'''
def overschieWijk():
    ov1 = polygon("ov1",(120, 50, 120), Polygons.ov1)
    ov2 = polygon("ov2",(120, 50, 120), Polygons.ov2)
    ov3 = polygon("ov3",(120, 50, 120), Polygons.ov3)
    ov4 = polygon("ov4",(120, 50, 120), Polygons.ov4)
    ov5 = polygon("ov5",(120, 50, 120), Polygons.ov5)
    ovlijst = [ov1,ov2,ov3,ov4,ov5]

''''This function gets loaded when the area: "Hillegersberg", gets selected'''
def hillegersbergWijk():
    hill1 = polygon("hill1",(120, 50, 120), Polygons.hill1)
    hill2 = polygon("hill2",(120, 50, 120), Polygons.hill2)
    hill3 = polygon("hill3",(120, 50, 120), Polygons.hill3)
    hill4 = polygon("hill4",(120, 50, 120), Polygons.hill4)
    hill5 = polygon("hill5",(120, 50, 120), Polygons.hill5)
    hillijst = [hill1,hill2,hill3,hill4,hill5]

def prinsalexanderWijk():
    pa1 = polygon("pa1",(120, 50, 120), Polygons.pa1)
    pa2 = polygon("pa2",(120, 50, 120), Polygons.pa2)
    pa3 = polygon("pa3",(120, 50, 120), Polygons.pa3)
    pa4 = polygon("pa4",(120, 50, 120), Polygons.pa4)
    pa5 = polygon("pa5",(120, 50, 120), Polygons.pa5)
    pa6 = polygon("pa6",(120, 50, 120), Polygons.pa6)
    palijst = [pa1,pa2,pa3,pa4,pa5,pa6]

def kralingenWijk():
    kra6 = polygon("kra6",(120, 50, 120), Polygons.kra6)
    kra1 = polygon("kra1",(120, 50, 120), Polygons.kra1)
    kra2 = polygon("kra2",(120, 50, 120), Polygons.kra2)
    kra3 = polygon("kra3",(120, 50, 120), Polygons.kra3)
    kra4 = polygon("kra4",(120, 50, 120), Polygons.kra4)
    kra5 = polygon("kra5",(120, 50, 120), Polygons.kra5)
    kra7 = polygon("kra7",(120, 50, 120), Polygons.kra6)
    kralijst = [kra6,kra1,kra2,kra3,kra4,kra5,kra7]

def centrumWijk():
    centr1 = polygon("centr1",(120, 50, 120), Polygons.centr1)
    centr2 = polygon("centr2",(120, 50, 120), Polygons.centr2)
    centr3 = polygon("centr3",(120, 50, 120), Polygons.centr3)
    centr4 = polygon("centr4",(120, 50, 120), Polygons.centr4)
    centr5 = polygon("centr5",(120, 50, 120), Polygons.centr5)
    centr6 = polygon("centr6",(120, 50, 120), Polygons.centr6)
    centlijst = [centr1,centr2,centr3,centr4,centr5,centr6]

def noordWijk():
    nrd1 = polygon("nrd1",(120, 50, 120), Polygons.nrd1)
    nrd2 = polygon("nrd2",(120, 50, 120), Polygons.nrd2)
    nrd3 = polygon("nrd3",(120, 50, 120), Polygons.nrd3)
    nrd4 = polygon("nrd4",(120, 50, 120), Polygons.nrd4)
    nrd5 = polygon("nrd5",(120, 50, 120), Polygons.nrd5)
    nrd6 = polygon("nrd6",(120, 50, 120), Polygons.nrd6)
    nrd7 = polygon("nrd7",(120, 50, 120), Polygons.nrd7)
    nrdlijst = [nrd1,nrd2,nrd3,nrd4,nrd5,nrd6,nrd7]

def delftWijk():
    delf1 = polygon("delf1",(120, 50, 120), Polygons.delf1)
    delf2 = polygon("delf2",(120, 50, 120), Polygons.delf2)
    delf3 = polygon("delf3",(120, 50, 120), Polygons.delf3)
    delf4 = polygon("delf4",(120, 50, 120), Polygons.delf4)
    delf5 = polygon("delf5",(120, 50, 120), Polygons.delf5)
    delf6 = polygon("delf6",(120, 50, 120), Polygons.delf6)
    delf7 = polygon("delf7",(120, 50, 120), Polygons.delf7)
    delf8 = polygon("delf8",(120, 50, 120), Polygons.delf8)
    delflijst = [delf1,delf2,delf3,delf4,delf5,delf6,delf7,delf8]

def waalhavenWijk():
    waal1 = polygon("waal1",(120, 50, 120), Polygons.waal1)
    waal2 = polygon("waal2",(120, 50, 120), Polygons.waal2)
    waal3 = polygon("waal3",(120, 50, 120), Polygons.waal3)
    waal4 = polygon("waal4",(120, 50, 120), Polygons.waal4)
    waallijst = [waal1,waal2,waal3,waal4]

def charloisWijk():
    char1 = polygon("char1",(120, 50, 120), Polygons.char1)
    char2 = polygon("char2",(120, 50, 120), Polygons.char2)
    char3 = polygon("char3",(120, 50, 120), Polygons.char3)
    char4 = polygon("char4",(120, 50, 120), Polygons.char4)
    char5 = polygon("char5",(120, 50, 120), Polygons.char5)
    char6 = polygon("char6",(120, 50, 120), Polygons.char6)
    char7 = polygon("char7",(120, 50, 120), Polygons.char7)
    charlijst = [char1,char2,char3,char4,char5,char6,char7]

def feijenoordWijk():
    fei1 = polygon("fei1",(120, 50, 120), Polygons.fei1)
    fei2 = polygon("fei2",(120, 50, 120), Polygons.fei2)
    fei3 = polygon("fei3",(120, 50, 120), Polygons.fei3)
    fei4 = polygon("fei4",(120, 50, 120), Polygons.fei4)
    fei5 = polygon("fei5",(120, 50, 120), Polygons.fei5)
    fei6 = polygon("fei6",(120, 50, 120), Polygons.fei6)
    fei7 = polygon("fei7",(120, 50, 120), Polygons.fei7)
    fei8 = polygon("fei8",(120, 50, 120), Polygons.fei8)
    fei9 = polygon("fei9",(120, 50, 120), Polygons.fei9)
    feilijst = [fei1,fei2,fei3,fei4,fei5,fei6,fei7,fei8,fei9]

def ijsselmondeWijk():
    ijs1 = polygon("ijs1",(120, 50, 120), Polygons.ijs1)
    ijs2 = polygon("ijs2",(120, 50, 120), Polygons.ijs2)
    ijs3 = polygon("ijs3",(120, 50, 120), Polygons.ijs3)
    ijs4 = polygon("ijs4",(120, 50, 120), Polygons.ijs4)
    ijslijst = [ijs1,ijs2,ijs3,ijs4]



''''The polygons(area's)'''''
overschie_polygon = polygon("Overschie",(20, 50, 120), Polygons.overschie)
hillegersberg_polygon = polygon("Hillegersberg-Schiebroek",(20, 50, 120), Polygons.hillegersberg)
prins_alexander_polygon = polygon("Prins_alexander",(20, 50, 120), Polygons.prins_alexander)
kralingen_polygon = polygon("Kralingen-Crooswijk",(20, 50, 120), Polygons.kralingen)
noord_polygon = polygon("Noord",(20, 50, 120), Polygons.noord)
delftshaven_polygon = polygon("Delfshaven",(20, 50, 120), Polygons.delftshaven)
centrum_polygon = polygon("Centrum",(20, 50, 120), Polygons.centrum)
feijenoord_polygon = polygon("Feijenoord",(20, 50, 120), Polygons.feijenoord)
ijsselmonde_polygon = polygon("IJsselmonde",(20, 50, 120), Polygons.ijsselmonde)
charlois_polygon = polygon("Charlois",(20, 50, 120), Polygons.charlois)
waalhaven_polygon = polygon("Waalhaven",(20, 50, 120), Polygons.waalhaven)



''''Array that has the polygon area's, this is used to go through the array and then the colour will change. It is used in a database function'''
polygonsgebieden = [overschie_polygon, hillegersberg_polygon, prins_alexander_polygon, kralingen_polygon, noord_polygon, delftshaven_polygon, centrum_polygon, feijenoord_polygon, ijsselmonde_polygon, charlois_polygon, waalhaven_polygon]
polygonsgebieden2 = [overschie_polygon, hillegersberg_polygon, prins_alexander_polygon, kralingen_polygon, noord_polygon, delftshaven_polygon, feijenoord_polygon, ijsselmonde_polygon, charlois_polygon]
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
    if str(canvas.find_withtag(CURRENT)) == "(1,)" and searchPage == True: #every polygon(area) has his own tag
        text.config(text=overschie) #Text changes to the name of the selected area
        for i in List1: #Goes through the array of the area triggers.
            if i.name == "overschie":#Name is the attribute of the area's triggers, this is used to uniquely identify the area
                setattr(i, 'trigger', True) #sets the clicked area to true
                overschieWijk() #The wijken get drawn
            else:
                setattr(i, 'trigger', False) #set the other area's to false
                print(i.trigger)

    elif str(canvas.find_withtag(CURRENT)) == "(2,)" and searchPage == True: #Checks if the page is the right page.
        text.config(text=hillegersberg_schiebroek)
        for i in List1:
            if i.name == "hillegersberg":
                setattr(i, 'trigger', True)
                hillegersbergWijk() #The wijken get drawn


            else:
                setattr(i, 'trigger', False)
                print(i.trigger)

    elif str(canvas.find_withtag(CURRENT)) == "(3,)" and searchPage == True:
        text.config(text=prins_alexander)
        for i in List1:
            if i.name == "prinsAlexander":
                setattr(i, 'trigger', True)
                prinsalexanderWijk() #The wijken get drawn

            else:
                setattr(i, 'trigger', False)
                print(i.trigger)

    elif str(canvas.find_withtag(CURRENT)) == "(4,)" and searchPage == True:
        text.config(text=kralingen_crooswijk)
        for i in List1:
            if i.name == "kralingenCrooswijk":
                setattr(i, 'trigger', True)
                kralingenWijk() #The wijken get drawn

            else:
                setattr(i, 'trigger', False)
                print(i.trigger)

    elif str(canvas.find_withtag(CURRENT)) == "(5,)" and searchPage == True:
        text.config(text=noord)
        for i in List1:
            if i.name == "noord":
                setattr(i, 'trigger', True)
                noordWijk() #The wijken get drawn

            else:
                setattr(i, 'trigger', False)
                print(i.trigger)


    elif str(canvas.find_withtag(CURRENT)) == "(6,)" and searchPage == True:
        text.config(text=delftshaven)
        for i in List1:
            if i.name == "delftshaven":
                setattr(i, 'trigger', True)
                delftWijk()

            else:
                setattr(i, 'trigger', False)
                print(i.trigger)

    elif str(canvas.find_withtag(CURRENT)) == "(7,)" and searchPage == True:
        text.config(text=centrum)
        for i in List1:
            if i.name == "centrum":
                setattr(i, 'trigger', True)
                centrumWijk()

            else:
                setattr(i, 'trigger', False)
                print(i.trigger)


    elif str(canvas.find_withtag(CURRENT)) == "(8,)" and searchPage == True:
        text.config(text=feijenood)
        for i in List1:
            if i.name == "feijenoord":
                setattr(i, 'trigger', True)
                feijenoordWijk()

            else:
                setattr(i, 'trigger', False)
                print(i.trigger)

    elif str(canvas.find_withtag(CURRENT)) == "(9,)" and searchPage == True:
        text.config(text=ijsselmonde)
        for i in List1:
            if i.name == "ijsselmonde":
                setattr(i, 'trigger', True)
                ijsselmondeWijk()
            else:
                setattr(i, 'trigger', False)
                print(i.trigger)

    elif str(canvas.find_withtag(CURRENT)) == "(10,)" and searchPage == True:
        text.config(text=charlois)
        for i in List1:
            if i.name == "charlois":
                setattr(i, 'trigger', True)
                charloisWijk()

            else:
                setattr(i, 'trigger', False)
                print(i.trigger)

    elif str(canvas.find_withtag(CURRENT)) == "(11,)" and searchPage == True:
        text.config(text=waalhaven)
        for i in List1:
            if i.name == "waalhaven":
                setattr(i, 'trigger', True)
                waalhavenWijk()

            else:
                setattr(i, 'trigger', False)
                print(i.trigger)

def rightclick(event):
    for wijk in polygonsgebieden:
        if canvas.find_withtag(CURRENT) == canvas.find_withtag(wijk.name):
            wijk.Select()

''''when a polygon(area) is clicked, the click method will be activated'''''
canvas.bind('<Button-1>', click, add="+") #Binds the canvas to the click method
canvas.bind('<Button-3>', rightclick, add="+")

''''Canvas that gets drawn'''
canvas.grid(row=2, column=0,sticky=N,rowspan=999,padx=55) #the lower the code(higher line) the later it will get drawn

''''Function that links the drop down menu sections to pages, it redirects to pages'''
def menuSelector(event):
    if  str(variable.get()) == "Home": #variable is the drop down menu, when a menu page is selected, the value of the variable changes
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
menu_button.config(font=("Helvetica", 20, "bold"), bg="DeepSkyBlue2", fg="white") #Changes the font/size of the drop down menu
menu_button.grid(row=0, column=0, sticky=N + W) #Sets the position of the drop down menu

''''Menu Text'''
welcome_text = "Select the home button to see the available options" #Test that appears on the menu
description_text = Label(root,text=welcome_text,font=("Helvetica",15,"bold")) #Sets the text on the page
description_text.grid(row=1,column=0,sticky=W) #Sets the position of the text

''''the home page'''
def home():
    global searchPage
    text.config(text="") #Resets the text when it reaches the home button
    for widget in root.winfo_children(): #checks which wigets(buttons, text etc) are open
        if widget == menu_button or widget == text: #The menu does not get deleted
            print("Optionmenu")
        elif widget == canvas: #The canvas will not be deleted
            print("canvas")
        else:
            widget.destroy() #Other widgets are destroyed and so are their value
            print(str(widget) + ": Is deleted")
    searchPage = False

def resmenuoptions(event):
    global variable1
    if  str(variable1.get()) == (str(screenx) + "x" + str(screeny)):
        root.geometry('{}x{}'.format(screenx, screeny))
    elif  str(variable1.get()) == "1280x720": #variable is the drop down menu, when a menu page is selected, the value of the variable changes
        root.geometry("1280x720")
    elif  str(variable1.get()) == "1600x900":
        root.geometry("1600x900")
    elif str(variable1.get()) == "1920x1080":
        root.geometry("1920x1080")
    elif str(variable1.get()) == "4k":
        root.geometry("3860x2140")

''''the settings page'''
def settings():
    global searchPage, variable1
    text.config(text="") #Resets the text when it reaches the home button
    for widget in root.winfo_children():
        if widget == menu_button or widget == text: #menubutton does not get deleted
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
    menu_button1 = OptionMenu(root, variable1, (str(screenx) + "x" + str(screeny)), "1280x720", "1600x900", "1920x1080", "4k", command=resmenuoptions)  #The options of the drop down menu
    menu_button1.config(font=("Helvetica", 20, "bold"), bg="DeepSkyBlue2", fg="white") #Sets the font/size of drop down menu
    menu_button1.grid(row=3, column=0, sticky=N + W) #Sets position of the drop down menu
    searchPage = False

''''The about page'''
def about():
    global searchPage
    text.config(text="") #Resets the text when it reaches the home button
    for widget in root.winfo_children():
        if widget == menu_button or widget == text: #Optionmenu does not get deleted
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

    searchPage = False


''''Percentages en cijfers page'''
def percentagesEnCijfers():
    global searchPage
    text.config(text="") #Resets the text when it reaches the home button
    for widget in root.winfo_children():
        if widget == menu_button or widget == text: #Menu button will not be deleted
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
    searchPage = False


''''The woningsadvies radiobuttons, these will catch the value of a button. It knows which button the user has selected'''''
bevolking_radioButtons = IntVar() #The value will change when a certain button is selected. Every button has his own value, and that value the main radiobutton will get
milieu_radioButtons = IntVar()
veiligheid_radioButtons = IntVar()
verkeer_radioButtons = IntVar()
voorzieningen_radioButtons = IntVar()

class categorie():
    def __init__(self,textvar,textrow,fontsize,row1,row2,row3,row4,variable):
        self.txt = textvar
        self.txtrow = textrow
        self.fontsize = fontsize
        self.row1 = row1
        self.row2 = row2
        self.row3 = row3
        self.row4 = row4
        self.variable = variable

        text = Label(root, width=0, text=self.txt, font=("Helvetica", self.fontsize, "bold"))
        text.grid(row=self.txtrow, column=0, sticky=W)

        Radiobutton(root, indicatoron=False, text="3 or lower", variable=self.variable, value=1).grid(column=0,row=self.row1,sticky=W)
        Radiobutton(root, indicatoron=False, text="Between 3 and 5.5", variable=self.variable, value=2).grid(column=0, row=self.row2, sticky=W)
        Radiobutton(root, indicatoron=False, text="Between 5.5 and 7", variable=self.variable, value=3).grid(column=0, row=self.row3, sticky=W)
        Radiobutton(root, indicatoron=False, text="7 or higher", variable=self.variable, value=4).grid(column=0,row=self.row4,sticky=W)


''''Woningsadvies page'''
def woningsadvies():
    global searchPage
    global bevolking_radioButtons #Reads a global variable, this was one of the best options for this
    global milieu_radioButtons
    global veiligheid_radioButtons
    global verkeer_radioButtons
    global voorzieningen_radioButtons
    text.config(text="") #Resets the text when it reaches the home button

    for widget in root.winfo_children():
        if widget == menu_button or widget == text or widget == canvasWijk: #Menu does not get deleted
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
    woningsadvies__headText = Label(root, width=0, text=woningsadvies_text, font=("Helvetica", 15, "bold")) #Creats the text
    woningsadvies__headText.grid(row=2, column=0, sticky=W) #Sets position of the text

    ''''the bevolking/population part with radiobuttons'''''
    categorie(woningsadvies_text1,3,10,4,5,6,7,bevolking_radioButtons)

    ''''The Milieu/Economy part with radiobuttons'''
    categorie(woningsadvies_text2,8, 10, 9, 10, 11, 12, milieu_radioButtons)

    ''''The Veiligheid/Safety part with radiobuttons'''
    categorie(woningsadvies_text3,13, 10, 14, 15, 16, 17, veiligheid_radioButtons)

    ''''The verkeer/trafic part with radiobuttons'''
    categorie(woningsadvies_text4,18, 10, 19, 20, 21, 22, verkeer_radioButtons)

    ''''The voorzieningen/services part with radiobuttons'''
    categorie(woningsadvies_text5,23, 10, 24, 25, 26, 27, voorzieningen_radioButtons)

    ''''the button wich makes everything caculate'''
    button51 = NewButton("I am ready to see my living options ", 28, 0, screenx / 600, 0)
    button51.pageClick(databaseWoningsAdvies)
    canvas.grid(row=2, column=0, sticky=W, rowspan=999, padx=55)
    searchPage = True


''''Population/bevolking category, when it gets clicked these buttons appears, and when buttons are clicked they will go to the database function'''
def categoryPopulation():
    global searchPage
    text.config(text="") #Resets the text when it reaches the home button
    button15 = PecButton("hieriets", 1, 0, screenx / 30, screeny / 150, 0)
    button16 = PecButton("hiernog iets met een lange lengte", 2, 0, screenx / 45, screeny / 150,1)
    button17 = PecButton("wejo", 3, 0, screenx / 17, screeny / 150,2)
    button18 = PecButton("pfffff lol oke", 4, 0, screenx / 17, screeny / 150,3)
    button19 = PecButton("zeg maar niet te lang ok", 5, 0, screenx / 22, screeny / 150,4)
    button20 = PecButton("Population6_placeholder", 6, 0, screenx / 22, screeny / 150,5)
    buttonback1 = NewButton("Back", 7, 0, screenx / 22, screeny / 150)
    buttonback1.pageClick(percentagesEnCijfers) #The back button
    searchPage = True

''''Population/bevolking category, when it gets clicked these buttons appears, and when buttons are clicked they will go to the database function'''
def categoryEnvironment():
    global searchPage
    text.config(text="") #Resets the text when it reaches the home button
    button21 = PecButton("Environmennt1_placehholder", 1, 0, screenx / 30, screeny / 150,6)
    button22 = PecButton("Environment2_placeholder", 2, 0, screenx / 45, screeny / 150,7)
    button23 = PecButton("Environment3_placeholder", 3, 0, screenx / 17, screeny / 150,8)
    button24 = PecButton("Environment4_placeholder", 4, 0, screenx / 17, screeny / 150,9)
    button25 = PecButton("Environment5_placeholder", 5, 0, screenx / 22, screeny / 150,10)
    button26 = PecButton("Environment6_placeholder", 6, 0, screenx / 22, screeny / 150,11)
    buttonback2 = NewButton("Back", 7, 0, screenx / 22, screeny / 150)
    buttonback2.pageClick(percentagesEnCijfers)
    searchPage = True

''''Population/bevolking category, when it gets clicked these buttons appears, and when buttons are clicked they will go to the database function'''
def categorySafety():
    global searchPage
    text.config(text="") #Resets the text when it reaches the home button
    button27 = PecButton("Safety1_placehholder", 1, 0, screenx / 30, screeny / 150,12)
    button28 = PecButton("Safety2_placeholder", 2, 0, screenx / 45, screeny / 150,12)
    button29 = PecButton("Safety3_placeholder", 3, 0, screenx / 17, screeny / 150,13)
    button30 = PecButton("Safety4_placeholder", 4, 0, screenx / 17, screeny / 150,14)
    button31 = PecButton("Safety5_placeholder", 5, 0, screenx / 22, screeny / 150,15)
    button32 = PecButton("Safety6_placeholder", 6, 0, screenx / 22, screeny / 150,16)
    buttonback3 = NewButton("Back", 7, 0, screenx / 22, screeny / 150)
    buttonback3.pageClick(percentagesEnCijfers)
    searchPage = True

''''Population/bevolking category, when it gets clicked these buttons appears, and when buttons are clicked they will go to the database function'''
def categoryTraffic():
    global searchPage
    text.config(text="") #Resets the text when it reaches the home button
    button33 = PecButton("Traffic1_placehholder", 1, 0, screenx / 30, screeny / 150,17)
    button34 = PecButton("Traffic2_placeholder", 2, 0, screenx / 45, screeny / 150,18)
    button35 = PecButton("Traffic3_placeholder", 3, 0, screenx / 17, screeny / 150,19)
    button36 = PecButton("Traffic4_placeholder", 4, 0, screenx / 17, screeny / 150,20)
    button37 = PecButton("Traffic5_placeholder", 5, 0, screenx / 22, screeny / 150,21)
    button38 = PecButton("Traffic6_placeholder", 6, 0, screenx / 22, screeny / 150,22)
    buttonback4 = NewButton("Back", 7, 0, screenx / 22, screeny / 150)
    buttonback4.pageClick(percentagesEnCijfers)
    searchPage = True

''''Population/bevolking category, when it gets clicked these buttons appears, and when buttons are clicked they will go to the database function'''
def categoryServices():
    global searchPage
    text.config(text="") #Resets the text when it reaches the home button
    button39 = PecButton("Services1_placehholder", 1, 0, screenx / 30, screeny / 150,23)
    button40 = PecButton("Services2_placeholder", 2, 0, screenx / 45, screeny / 150,24)
    button41 = PecButton("Services3_placeholder", 3, 0, screenx / 17, screeny / 150,25)
    button42 = PecButton("Services4_placeholder", 4, 0, screenx / 17, screeny / 150,26)
    button43 = PecButton("Services5_placeholder", 5, 0, screenx / 22, screeny / 150,27)
    button44 = PecButton("Services6_placeholder", 6, 0, screenx / 22, screeny / 150,28)
    buttonback5 = NewButton("Back", 7, 0, screenx / 22, screeny / 150)
    buttonback5.pageClick(percentagesEnCijfers)
    searchPage = True

''''Population/bevolking category, when it gets clicked these buttons appears, and when buttons are clicked they will go to the database function'''
def categoryOther():
    global searchPage
    text.config(text="") #Resets the text when it reaches the home button
    button45 = PecButton("Other1_placehholder", 1, 0, screenx / 30, screeny / 150,29)
    button46 = PecButton("Other2_placeholder", 2, 0, screenx / 45, screeny / 150,30)
    button47 = PecButton("Other3_placeholder", 3, 0, screenx / 17, screeny / 150,31)
    button48 = PecButton("Other4_placeholder", 4, 0, screenx / 17, screeny / 150,32)
    button49 = PecButton("Other5_placeholder", 5, 0, screenx / 22, screeny / 150,33)
    button50 = PecButton("Other6_placeholder", 6, 0, screenx / 22, screeny / 150,34)
    buttonback6 = NewButton("Back", 7, 0, screenx / 22, screeny / 150)
    buttonback6.pageClick(percentagesEnCijfers)
    searchPage = True

''''Based on the data, the colour of the map changes, the data represents the query that will come in the function'''
def ShowResults(data):
    global polygonsgebieden #The array of area's
    data = [] #Dictionary to simulate a query, this is to test the query
    for result in data: #goes in the dictionary (the query)
            for gebied in polygonsgebieden: #Goes in the area's array
                if result == "Charlois": #Checks if result from the query is equal to an area
                    result = int(data.get(result)) #Converts the dictionary value to an int
                     #Changes color of the area and also change the colour
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

    # f = Figure(figsize=(5, 5), dpi=50)
    # a = f.add_subplot(111)  # means 1 chart 1 by 1
    # a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 2, 4, 4, 3, 5, 3])
    # Figure1 = FigureCanvasTkAgg(f, root)
    # Figure1.show()
    # Figure1.get_tk_widget().grid(row=0, column=0, sticky=N, rowspan=30)


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

''''Database query for the page: "Percentages en cijfers"'''
''''This page will be called when buttons from the: "Percentages en cijfers", are selected. The method call is set in the class of the buttons'''
def databasePercentagesEnCijfers():
    global buttonArray #needed because the array has the last selected button of the page: "Percentages en cijfers'
    answer = (buttonArray[-1]) #last selected button gets stored in answer
    print(answer) #To prove that the last selected button is saved in the array
    #Here comes the query, for every button a new query should be appended to the array
    data =[]
    if answer == 0:  #the numbers represent the button, each button has his own number. The attribute of the button that stores this is: name
        if len(geselecteerdegebieden)>0:
            for i in geselecteerdegebieden:
                print(i.name)
                PlotLineChart("geweldsdelicten", geselecteerdegebieden)
         #The query get send into the showresults function, then the map colour gets changed based on the results from it
    elif answer == 1:
        PlotOnMap("geweldsdelicten", polygonsgebieden2)
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

for widget in root.winfo_children():
    print(widget)

root.mainloop() #for the loop