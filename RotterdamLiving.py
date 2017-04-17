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

class polygon:
    def __init__(self,name,color,list):
        self.name = name
        self.color = color
        self.selected = False
        self.shape = canvas.create_polygon(list, fill=(HexToRGB(color)), outline='black', width=2, tags = self.name)
        canvas.move(self.shape, rs(-400), 0)
        self.selectcolor = 'red'


    def ChangeColor(self, percent):
        basevalue = 255
        colorchange = percent * basevalue // 100
        changedcolor = basevalue
        finalcolor = basevalue - colorchange
        looptime = 20

        for n in range(looptime):
            if changedcolor >= 16 and changedcolor > finalcolor:
                color = (changedcolor, changedcolor, 255)
                canvas.itemconfig(self.shape, fill=HexToRGB(color))
                changedcolor = int(changedcolor - (colorchange / looptime))
                root.update()
            time.sleep(0.00000000000001)

        if finalcolor <= 16:
            color = (16, 16, 255)
        if finalcolor > 16:
            color = (finalcolor, finalcolor, 255)
        canvas.itemconfig(self.shape, fill=HexToRGB(color))
        root.update()

    def ChangeBorderColor(self, color):
        canvas.itemconfig(self.shape, outline=color, width=6)

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

    def Hover(self, event):
        if canvas.find_withtag(CURRENT) == canvas.find_withtag(self.name):
            text.config(text=self.name)

    def spawnchild(self):
        if self.name == "Overschie":
            overschieWijk()
        if self.name == "Hillegersberg-Schiebroek":
            hillegersbergWijk()
        if self.name == "Prins_alexander":
            prinsalexanderWijk()
        if self.name == "Kralingen-Crooswijk":
            kralingenWijk()
        if self.name == "Noord":
            noordWijk()
        if self.name == "Delfshaven":
            delftWijk()
        if self.name == "Centrum":
            centrumWijk()
        if self.name == "Feijenoord":
            feijenoordWijk()
        if self.name == "IJsselmonde":
            ijsselmondeWijk()
        if self.name == "Charlois":
            charloisWijk()
        if self.name == "Waalhaven":
            waalhavenWijk()

class lagenda():
    def __init__(self):
        for i in range(80):
            color = (255 - i*3, 255 - i*3, 255)
            self.shape = canvas.create_rectangle(50,i * 10,100,i * 10 + 10, fill=(HexToRGB(color)), outline='black')
            canvas.move(self.shape,rs(1700),rs(50))
            canvas.create_text(rs(1710),rs(60),text="0%", font=("Helvetica",15,"bold"))
            canvas.create_text(rs(1700), rs(840), text="100%", font=("Helvetica", 15, "bold"))
lagenda = lagenda()


''''This function gets loaded when the area: "Overschie", gets selected'''
def overschieWijk():
    ov1 = polygon("ov1",(16, 16, 255), Polygons.ov1)
    ov2 = polygon("ov2",(16, 16, 255), Polygons.ov2)
    ov3 = polygon("ov3",(16, 16, 255), Polygons.ov3)
    ov4 = polygon("ov4",(16, 16, 255), Polygons.ov4)
    ov5 = polygon("ov5",(16, 16, 255), Polygons.ov5)
    ovlijst = [ov1,ov2,ov3,ov4,ov5]
    wijklist.append(ovlijst)

''''This function gets loaded when the area: "Hillegersberg", gets selected'''
def hillegersbergWijk():
    hill1 = polygon("hill1",(16, 16, 255), Polygons.hill1)
    hill2 = polygon("hill2",(16, 16, 255), Polygons.hill2)
    hill3 = polygon("hill3",(16, 16, 255), Polygons.hill3)
    hill4 = polygon("hill4",(16, 16, 255), Polygons.hill4)
    hill5 = polygon("hill5",(16, 16, 255), Polygons.hill5)
    hillijst = [hill1,hill2,hill3,hill4,hill5]
    wijklist.append(hillijst)

def prinsalexanderWijk():
    pa1 = polygon("pa1",(16, 16, 255), Polygons.pa1)
    pa2 = polygon("pa2",(16, 16, 255), Polygons.pa2)
    pa3 = polygon("pa3",(16, 16, 255), Polygons.pa3)
    pa4 = polygon("pa4",(16, 16, 255), Polygons.pa4)
    pa5 = polygon("pa5",(16, 16, 255), Polygons.pa5)
    pa6 = polygon("pa6",(16, 16, 255), Polygons.pa6)
    palijst = [pa1,pa2,pa3,pa4,pa5,pa6]
    wijklist.append(palijst)

def kralingenWijk():
    kra6 = polygon("kra6",(16, 16, 255), Polygons.kra6)
    kra1 = polygon("kra1",(16, 16, 255), Polygons.kra1)
    kra2 = polygon("kra2",(16, 16, 255), Polygons.kra2)
    kra3 = polygon("kra3",(16, 16, 255), Polygons.kra3)
    kra4 = polygon("kra4",(16, 16, 255), Polygons.kra4)
    kra5 = polygon("kra5",(16, 16, 255), Polygons.kra5)
    kra7 = polygon("kra7",(16, 16, 255), Polygons.kra7)
    kralijst = [kra6,kra1,kra2,kra3,kra4,kra5,kra7]
    wijklist.append(kralijst)

def centrumWijk():
    centr1 = polygon("centr1",(16, 16, 255), Polygons.centr1)
    centr2 = polygon("centr2",(16, 16, 255), Polygons.centr2)
    centr3 = polygon("centr3",(16, 16, 255), Polygons.centr3)
    centr4 = polygon("centr4",(16, 16, 255), Polygons.centr4)
    centr5 = polygon("centr5",(16, 16, 255), Polygons.centr5)
    centr6 = polygon("centr6",(16, 16, 255), Polygons.centr6)
    centlijst = [centr1,centr2,centr3,centr4,centr5,centr6]
    wijklist.append(centlijst)

def noordWijk():
    nrd1 = polygon("nrd1",(16, 16, 255), Polygons.nrd1)
    nrd2 = polygon("nrd2",(16, 16, 255), Polygons.nrd2)
    nrd3 = polygon("nrd3",(16, 16, 255), Polygons.nrd3)
    nrd4 = polygon("nrd4",(16, 16, 255), Polygons.nrd4)
    nrd5 = polygon("nrd5",(16, 16, 255), Polygons.nrd5)
    nrd6 = polygon("nrd6",(16, 16, 255), Polygons.nrd6)
    nrd7 = polygon("nrd7",(16, 16, 255), Polygons.nrd7)
    nrdlijst = [nrd1,nrd2,nrd3,nrd4,nrd5,nrd6,nrd7]
    wijklist.append(nrdlijst)

def delftWijk():
    delf1 = polygon("delf1",(16, 16, 255), Polygons.delf1)
    delf2 = polygon("delf2",(16, 16, 255), Polygons.delf2)
    delf3 = polygon("delf3",(16, 16, 255), Polygons.delf3)
    delf4 = polygon("delf4",(16, 16, 255), Polygons.delf4)
    delf5 = polygon("delf5",(16, 16, 255), Polygons.delf5)
    delf6 = polygon("delf6",(16, 16, 255), Polygons.delf6)
    delf7 = polygon("delf7",(16, 16, 255), Polygons.delf7)
    delf8 = polygon("delf8",(16, 16, 255), Polygons.delf8)
    delflijst = [delf1,delf2,delf3,delf4,delf5,delf6,delf7,delf8]
    wijklist.append(delflijst)

def waalhavenWijk():
    waal1 = polygon("waal1",(16, 16, 255), Polygons.waal1)
    waal2 = polygon("waal2",(16, 16, 255), Polygons.waal2)
    waal3 = polygon("waal3",(16, 16, 255), Polygons.waal3)
    waal4 = polygon("waal4",(16, 16, 255), Polygons.waal4)
    waallijst = [waal1,waal2,waal3,waal4]
    wijklist.append(waallijst)

def charloisWijk():
    char1 = polygon("char1",(16, 16, 255), Polygons.char1)
    char2 = polygon("char2",(16, 16, 255), Polygons.char2)
    char3 = polygon("char3",(16, 16, 255), Polygons.char3)
    char4 = polygon("char4",(16, 16, 255), Polygons.char4)
    char5 = polygon("char5",(16, 16, 255), Polygons.char5)
    char6 = polygon("char6",(16, 16, 255), Polygons.char6)
    char7 = polygon("char7",(16, 16, 255), Polygons.char7)
    charlijst = [char1,char2,char3,char4,char5,char6,char7]
    wijklist.append(charlijst)

def feijenoordWijk():
    fei1 = polygon("fei1",(16, 16, 255), Polygons.fei1)
    fei2 = polygon("fei2",(16, 16, 255), Polygons.fei2)
    fei3 = polygon("fei3",(16, 16, 255), Polygons.fei3)
    fei4 = polygon("fei4",(16, 16, 255), Polygons.fei4)
    fei5 = polygon("fei5",(16, 16, 255), Polygons.fei5)
    fei6 = polygon("fei6",(16, 16, 255), Polygons.fei6)
    fei7 = polygon("fei7",(16, 16, 255), Polygons.fei7)
    fei8 = polygon("fei8",(16, 16, 255), Polygons.fei8)
    fei9 = polygon("fei9",(16, 16, 255), Polygons.fei9)
    feilijst = [fei1,fei2,fei3,fei4,fei5,fei6,fei7,fei8,fei9]
    wijklist.append(feilijst)

def ijsselmondeWijk():
    ijs1 = polygon("ijs1",(16, 16, 255), Polygons.ijs1)
    ijs2 = polygon("ijs2",(16, 16, 255), Polygons.ijs2)
    ijs3 = polygon("ijs3",(16, 16, 255), Polygons.ijs3)
    ijs4 = polygon("ijs4",(16, 16, 255), Polygons.ijs4)
    ijslijst = [ijs1,ijs2,ijs3,ijs4]
    wijklist.append(ijslijst)

wijklist = []


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

def rightclick(event):
    for wijk in polygonsgebieden:
        if canvas.find_withtag(CURRENT) == canvas.find_withtag(wijk.name):
            wijk.Select()

def leftclick(event):
    for wijk in polygonsgebieden:
        if canvas.find_withtag(CURRENT) == canvas.find_withtag(wijk.name):
            wijk.spawnchild()
    for i in wijklist:
        for k in i:
            if canvas.find_withtag(CURRENT) == canvas.find_withtag(k.name):
                for c in wijklist:
                    for p in c:
                        canvas.delete(p.shape)

def hover(event):
    for wijk in polygonsgebieden:
        wijk.Hover(event)


''''when a polygon(area) is clicked, the click method will be activated'''''
canvas.bind('<Button-1>', leftclick, add="+") #Binds the canvas to the click method
canvas.bind('<Button-3>', rightclick, add="+")
canvas.bind('<Motion>', hover)

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
    # elif str(variable.get()) == "Settings":
    #     settings()
    elif str(variable.get()) == "Exit":
        root.destroy()


''''Drop down menu'''
variable = StringVar(root) #Variable will store the page that is selected
variable.set("Home")  # default value is the homebutton
menu_button = OptionMenu(root, variable, "Home", "Woningadvies", "Percentages en cijfers", "About",
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

# def resmenuoptions(event):
#     global variable1
#     if  str(variable1.get()) == (str(screenx) + "x" + str(screeny)):
#         root.geometry('{}x{}'.format(screenx, screeny))
#     elif  str(variable1.get()) == "1280x720": #variable is the drop down menu, when a menu page is selected, the value of the variable changes
#         root.geometry("1280x720")
#     elif  str(variable1.get()) == "1600x900":
#         root.geometry("1600x900")
#     elif str(variable1.get()) == "1920x1080":
#         root.geometry("1920x1080")
#     elif str(variable1.get()) == "4k":
#         root.geometry("3860x2140")
#
# ''''the settings page'''
# def settings():
#     global searchPage, variable1
#     text.config(text="") #Resets the text when it reaches the home button
#     for widget in root.winfo_children():
#         if widget == menu_button or widget == text: #menubutton does not get deleted
#             print("Optionmenu")
#         elif widget == canvas: #canvas does not get deleted
#             print("canvas")
#         else:
#             widget.destroy() #other widgets get deleted and so are their value
#             print(str(widget) + ": Is deleted")
#
#     ''''Resolution'''
#     resolution_text = "Select your screen resolution"
#     resolution1_text = Label(root, text=resolution_text, font=("Helvetica", 15, "bold"))
#     resolution1_text.grid(row=2, column=0, sticky=W)
#
#     ''''The drop down resolution menu'''
#     variable1 = StringVar(root)  #Variable will store the page that is selected
#     variable1.set(str(screenx) + " x " + str(screeny))  # default value of the drop down menu
#     menu_button1 = OptionMenu(root, variable1, (str(screenx) + "x" + str(screeny)), "1280x720", "1600x900", "1920x1080", "4k", command=resmenuoptions)  #The options of the drop down menu
#     menu_button1.config(font=("Helvetica", 20, "bold"), bg="DeepSkyBlue2", fg="white") #Sets the font/size of drop down menu
#     menu_button1.grid(row=3, column=0, sticky=N + W) #Sets position of the drop down menu
#     searchPage = False

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
    button15 = PecButton("schoolgaande en studerende jongeren (18 t/m 22 jr)", 1, 0, screenx / 30, screeny / 150, 0)
    button16 = PecButton("werkende jongeren (18 t/m 22 jr)", 2, 0, screenx / 45, screeny / 150,1)
    button17 = PecButton("werkzoekende jongeren (18 t/m 22 jr)", 3, 0, screenx / 17, screeny / 150,2)
    button18 = PecButton("bewoners met werk(23 t/m 64 jr)", 4, 0, screenx / 17, screeny / 150,3)
    button19 = PecButton("werkzoeknde bewoners(23 t/m 64 jr)", 5, 0, screenx / 22, screeny / 150,4)
    button20 = PecButton("Bewoners (18 jr en ouder) dat kort in Nederland woont", 6, 0, screenx / 22, screeny / 150,5)
    buttonback1 = NewButton("Terug", 7, 0, screenx / 22, screeny / 150)
    buttonback1.pageClick(percentagesEnCijfers) #The back button
    searchPage = True

''''Population/bevolking category, when it gets clicked these buttons appears, and when buttons are clicked they will go to the database function'''
def categoryEnvironment():
    global searchPage
    text.config(text="") #Resets the text when it reaches the home button
    button21 = PecButton("Veiligheidsindex -objectief", 1, 0, screenx / 30, screeny / 150,6)
    button22 = PecButton("Diefstal-objectief", 2, 0, screenx / 45, screeny / 150,7)
    button23 = PecButton("Geweld-objectief", 3, 0, screenx / 17, screeny / 150,8)
    button24 = PecButton("Inbraak-objectief", 4, 0, screenx / 17, screeny / 150,9)
    button25 = PecButton("Vandalisme-objectief", 5, 0, screenx / 22, screeny / 150,10)
    button26 = PecButton("Overlast objectief", 6, 0, screenx / 22, screeny / 150,11)
    buttonback2 = NewButton("Terug", 7, 0, screenx / 22, screeny / 150)
    buttonback2.pageClick(percentagesEnCijfers)
    searchPage = True

''''Population/bevolking category, when it gets clicked these buttons appears, and when buttons are clicked they will go to the database function'''
def categorySafety():
    global searchPage
    text.config(text="") #Resets the text when it reaches the home button
    button27 = PecButton("Milieu objectief", 1, 0, screenx / 30, screeny / 150,12)
    button28 = PecButton("% woningen in geluidscontour vanaf 55 dB", 2, 0, screenx / 45, screeny / 150,13)
    button29 = PecButton("gemiddelde NO2-concentratie 2009 irt grenswaarde 40 µg/m3", 3, 0, screenx / 17, screeny / 150,14)
    button30 = PecButton("% voldoende aanwezig groen (grasveldjes, bomen)", 4, 0, screenx / 17, screeny / 150,15)
    button31 = PecButton("% veel stankoverlast verkeer", 5, 0, screenx / 22, screeny / 150,16)
    button32 = PecButton("% veel geluidsoverlast verkeer", 6, 0, screenx / 22, screeny / 150,17)
    buttonback3 = NewButton("Back", 7, 0, screenx / 22, screeny / 150)
    buttonback3.pageClick(percentagesEnCijfers)
    searchPage = True

''''Population/bevolking category, when it gets clicked these buttons appears, and when buttons are clicked they will go to the database function'''
def categoryTraffic():
    global searchPage
    text.config(text="") #Resets the text when it reaches the home button
    button33 = PecButton("Sociale Index subjectief", 1, 0, screenx / 30, screeny / 150,18)
    button34 = PecButton("Oordeel kwaliteit van leven", 2, 0, screenx / 45, screeny / 150,19)
    button35 = PecButton("Capaciteiten-subjectief", 3, 0, screenx / 17, screeny / 150,20)
    button36 = PecButton("Leefomgeving-subjectief", 4, 0, screenx / 17, screeny / 150,21)
    button37 = PecButton("Meedoen-subjectief", 5, 0, screenx / 22, screeny / 150,22)
    button38 = PecButton("Binding-subjectief", 6, 0, screenx / 22, screeny / 150,23)
    buttonback4 = NewButton("Back", 7, 0, screenx / 22, screeny / 150)
    buttonback4.pageClick(percentagesEnCijfers)
    searchPage = True

''''Population/bevolking category, when it gets clicked these buttons appears, and when buttons are clicked they will go to the database function'''
def categoryServices():
    global searchPage
    text.config(text="") #Resets the text when it reaches the home button
    button39 = PecButton("% woningen met bakker binnen normafstand", 1, 0, screenx / 30, screeny / 150,24)
    button40 = PecButton("% woningen met groenteboer binnen normafstand", 2, 0, screenx / 45, screeny / 150,25)
    button41 = PecButton("% woningen met slager binnen normafstand", 3, 0, screenx / 17, screeny / 150,26)
    button42 = PecButton("% woningen met bushaltes binnen normafstand", 4, 0, screenx / 17, screeny / 150,27)
    button43 = PecButton("% woningen met metrostations binnen normafstand", 5, 0, screenx / 22, screeny / 150,28)
    button44 = PecButton("% woningen met tramhaltes binnen normafstand", 6, 0, screenx / 22, screeny / 150,29)
    buttonback5 = NewButton("Back", 7, 0, screenx / 22, screeny / 150)
    buttonback5.pageClick(percentagesEnCijfers)
    searchPage = True

''''Population/bevolking category, when it gets clicked these buttons appears, and when buttons are clicked they will go to the database function'''
def categoryOther():
    global searchPage
    text.config(text="") #Resets the text when it reaches the home button
    button45 = PecButton("gemiddelde WOZ per m2 woningoppervlakte", 1, 0, screenx / 30, screeny / 150,30)
    button46 = PecButton("drugsoverlast gedurende de jaren 2006-2011", 2, 0, screenx / 45, screeny / 150,31)
    button47 = PecButton("geweldsdelicten gedurende de jaren 2006-2011", 3, 0, screenx / 17, screeny / 150,32)
    button48 = PecButton("tevredenheid gedurende de jaren 2006-2011", 4, 0, screenx / 17, screeny / 150,33)
    button49 = PecButton("fietsendiefstal gedurende de jaren 2006-2011", 5, 0, screenx / 22, screeny / 150,34)
    button50 = PecButton("% vaak hondenpoep", 6, 0, screenx / 22, screeny / 150,35)
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
    if answer == 0:  #the numbers represent the button, each button has his own number. The attribute of the button that stores this is: name
        if len(geselecteerdegebieden)>0:
            PlotBarChart("si2016","PercentageSchoolgaandeEnStuderendeJongeren18TM22jr".lower(),geselecteerdegebieden)
         #The query get send into the showresults function, then the map colour gets changed based on the results from it
    elif answer == 1:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("si2016","PercentageWerkendeJongeren18TM22jr".lower(),geselecteerdegebieden)
    elif answer == 2:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("si2016","PercentageWerkzoekendeJongeren18TM22JrZonderBaan".lower(),geselecteerdegebieden)
    elif answer == 3:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("si2016","PercentageBewoners23TM64JrMetWerk".lower(),geselecteerdegebieden)
    elif answer == 4:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("si2016","PercentageWerkzoekendeBewoners23TM64JrZonderBaan".lower(),geselecteerdegebieden)
    elif answer == 5:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("si2016","PercentageBewoners18JrEnOuderDatNogMaarKortInNederlandWoont".lower(),geselecteerdegebieden)

    elif  answer == 6:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("vi2016","Veiligheidsindex-Objectief".lower(),geselecteerdegebieden)
    elif answer == 7:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("vi2016","Diefstal-Objectief".lower(),geselecteerdegebieden)
    elif answer == 8:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("vi2016","Geweld-Objectief".lower(),geselecteerdegebieden)
    elif answer == 9:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("vi2016","Inbraak-Objectief".lower(),geselecteerdegebieden)
    elif answer == 10:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("vi2016","Vandalisme-Objectief".lower(),geselecteerdegebieden)
    elif answer == 11:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("vi2016","OverlastObjectief".lower(),geselecteerdegebieden)

    elif answer == 12:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("fiob2016","MilieuObjectief".lower(),geselecteerdegebieden)
    elif answer == 13:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("fiob2016","PercentageWoningenInGeluidscontourVanaf55Db".lower(),geselecteerdegebieden)
    elif answer == 14:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("fiob2016","GemiddeldeNo2-Concentratie2009IrtGrenswaarde40µg/M3".lower(),geselecteerdegebieden)
    elif answer == 15:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("fisub2016","PercentageVoldoendeAanwezigGroenGrasveldjes,Bomen".lower(),geselecteerdegebieden)
    elif answer == 16:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("fisub2016","PercentageVeelStankoverlastVerkeer".lower(),geselecteerdegebieden)
    elif answer == 17:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("fisub2016","PercentageVeelGeluidsoverlastVerkeer".lower(),geselecteerdegebieden)

    elif answer == 18:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("si2016","SocialeIndexSubjectief".lower(),geselecteerdegebieden)
    elif answer == 19:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("si2016","OordeelKwaliteitVanLeven".lower(),geselecteerdegebieden)
    elif answer == 20:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("si2016","Capaciteiten-Subjectief".lower(),geselecteerdegebieden)
    elif answer == 21:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("si2016","Leefomgeving-Subjectief".lower(),geselecteerdegebieden)
    elif answer == 22:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("si2016","Meedoen-Subjectief".lower(),geselecteerdegebieden)
    elif answer == 23:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("si2016","Binding-Subjectief".lower(),geselecteerdegebieden)

    elif answer == 24:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("fiob2016","PercentageWoningenMetBakkerBinnenNormafstand".lower(),geselecteerdegebieden)
    elif answer == 25:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("fiob2016","PercentageWoningenMetGroenteboerBinnenNormafstand".lower(),geselecteerdegebieden)
    elif answer == 26:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("fiob2016","PercentageWoningenMetSlagerBinnenNormafstand".lower(),geselecteerdegebieden)
    elif answer == 27:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("fiob2016","PercentageWoningenMetBushaltesBinnenNormafstand".lower(),geselecteerdegebieden)
    elif answer == 28:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("fiob2016","PercentageWoningenMetMetrostationsBinnenNormafstand".lower(),geselecteerdegebieden)
    elif answer == 29:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("fiob2016","PercentageWoningenMetTramhaltesBinnenNormafstand".lower(),geselecteerdegebieden)

    elif answer == 30:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("fiob2016","GemiddeldeWozPerM2Woningoppervlakte".lower(),geselecteerdegebieden)
    elif answer == 31:
        if len(geselecteerdegebieden)>0:
            PlotLineChart("drugsoverlast".lower(),geselecteerdegebieden)
    elif answer == 32:
        if len(geselecteerdegebieden)>0:
            PlotLineChart("geweldsdelicten".lower(), geselecteerdegebieden)
    elif answer == 33:
        if len(geselecteerdegebieden)>0:
            PlotLineChart("tevredenheid".lower(), geselecteerdegebieden)
    elif answer == 34:
        if len(geselecteerdegebieden)>0:
            PlotLineChart("fietsendiefstal".lower(), geselecteerdegebieden)
    elif answer == 35:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("vi2016","PercentageVaakHondenpoep".lower(),geselecteerdegebieden)

for widget in root.winfo_children():
    print(widget)
root.mainloop() #for the loop