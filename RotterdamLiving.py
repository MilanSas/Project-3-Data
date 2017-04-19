from tkinter import * #Needed for GUI
import matplotlib #Needed for graph
import Polygons
from tkinter import messagebox
matplotlib.use("TKAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from PlotsClass import Plot, PlotBarChart, PlotLineChart, PlotOnMap, PlotWijkAdvies, PlotPieChart
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
hillegersberg_schiebroek = "HillegersbergSchiebroek"
prins_alexander = "PrinsAlexander"
kralingen_crooswijk = "KralingenCrooswijk"
noord = "Noord"
delftshaven = "Delfshaven"
centrum = "RotterdamCentrum"
waalhaven = "Waalhaven"
charlois = "Charlois"
feijenood = "Feijenoord"
ijsselmonde = "Ijsselmonde"
rotterdam = "Rotterdam"

''''Saves last page, '''
searchPage = None

''''The last clicked button from the page: "Percentages en cijfers", are saved in an array, this is for the: "databasePercentagesEnCijfers Function"'''
buttonArray = []

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
    def resetColor(self):
        self.button.config(bg="DeepSkyBlue2")
        setattr(self, 'clicked', False)



''''The Percentage en cijfers buttons'''''
class PecButton:
    def __init__(self,text, row, column, ipadx, ipady, name):

        self.clicked = False
        self.var = 50 - len(text)
        self.button = Button(root, text =(" " + text + str(" "*self.var)), command = self.databaseSender,font=("courier",9,"bold"),bg="DeepSkyBlue2", fg="white")
        self.button.columnconfigure(0,weight=300000)
        self.button.grid(row=row, column=column, sticky=W, ipadx=0, ipady=15)
        self.name = name #this is for the buttonArray to know what is the last button that is clicked
    def click(self):
        if self.clicked == False: #When a button is pressed or depressed, the state of the button change
                self.button.config(bg="DeepSkyBlue4") #Button's colour
                setattr(self, 'clicked', True) #State of the button is set to true.
        elif self.clicked == True:
                 self.button.config(bg="DeepSkyBlue2")
                 setattr(self, 'clicked', False)

    def databaseSender(self):
        buttonArray.append(self.name)
        databasePercentagesEnCijfers()
    def resetColor(self):
        self.button.config(bg="DeepSkyBlue2")
        setattr(self, 'clicked', False)


''''The canvas, important variable. Everything gets drawn on the canvas'''
canvas = Canvas(root, width=screenx,height=screeny) #root is in which window it will get drawn on.
canvasWijk = Canvas(root, width=screenx,height=screeny) #This canvas is for the wijken


''''Function to set polygon's(area) size'''
def rs(size):
    ratio = 1080 / size
    return int(screeny / ratio)

''''Function that changes the size of the wijken'''
def rsWijken(size):
    ratio = 1080 / size
    return int(screeny / ratio)


'''Function that Converts hex to RGB'''
def HexToRGB(rgb):
    #RGB WAARDES MOETEN TUSSEN 16 - 255
    result = ('#' + str(hex(rgb[0]).split('x')[-1]) + str(hex(rgb[1]).split('x')[-1]) + str(hex(rgb[2]).split('x')[-1]))
    return result

''''Function to create the polygons(area's)'''
geselecteerdegebieden = []

if (screeny > 1800):
    image = PhotoImage(file="afbeelding/Noord2160.png")
elif (screeny > 1260):
    image = PhotoImage(file="afbeelding/Noord1440.png")
elif (screeny > 990):
    image = PhotoImage(file="afbeelding/Noord1080.png")
elif (screeny > 810):
    image = PhotoImage(file="afbeelding/Noord900.png")
else:
    image = PhotoImage(file="afbeelding/Noord720.png")

canvas.create_image(rs(850),rs(360),image=image)


class polygon:
    def __init__(self,name,color,list, description):
        self.name = name
        self.waarde = 0
        self.color = color
        self.selected = False
        self.shape = canvas.create_polygon(list, fill=(HexToRGB(color)), outline='black', width=2, tags = self.name)
        canvas.move(self.shape, rs(-400), 0)
        self.selectcolor = HexToRGB((129,170,74))
        self.description = description


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

    def ChosenWijk(self):
        resetwijken()
        canvas.itemconfig(self.shape, fill=HexToRGB((240,240,20)))

    def Select(self):
        if self.selected:
            self.deSelect()
            return
        geselecteerdegebieden.append(self)
        self.selected = True
        canvas.itemconfig(self.shape, outline = self.selectcolor, width = 6)

    def deSelect(self):
        if self in geselecteerdegebieden:
            geselecteerdegebieden.remove(self)
        self.selected = False
        canvas.itemconfig(self.shape, outline='black', width = 2)

    def Hover(self, event):
        if canvas.find_withtag(CURRENT) == canvas.find_withtag(self.name):
            text.config(text=self.description)

    def Reset(self):
        canvas.itemconfig(self.shape, fill=(HexToRGB(self.color)))

    def spawnchild(self):
        if self.name == "Overschie":
            overschieWijk()
        if self.name == "HillegersbergSchiebroek":
            hillegersbergWijk()
        if self.name == "PrinsAlexander":
            prinsalexanderWijk()
        if self.name == "KralingenCrooswijk":
            kralingenWijk()
        if self.name == "Noord":
            noordWijk()
        if self.name == "Delfshaven":
            delftWijk()
        if self.name == "RotterdamCentrum":
            centrumWijk()
        if self.name == "Feijenoord":
            feijenoordWijk()
        if self.name == "IJsselmonde":
            ijsselmondeWijk()
        if self.name == "Charlois":
            charloisWijk()
        if self.name == "Waalhaven":
            waalhavenWijk()

class legenda():
    def __init__(self):
        for i in range(80):
            color = (255 - i*3, 255 - i*3, 255)
            self.shape = canvas.create_rectangle(rs(50),rs(i * 10 + 1),rs(100),rs(i * 10 + 10), fill=(HexToRGB(color)), outline='black')
            canvas.move(self.shape,rs(1700),rs(50))
            canvas.create_text(rs(1710),rs(60),text="0%", font=("Helvetica",15,"bold"))
            canvas.create_text(rs(1700), rs(840), text="100%", font=("Helvetica", 15, "bold"))
legenda = legenda()


''''This function gets loaded when the area: "Overschie", gets selected'''
def overschieWijk():
    ov1 = polygon("ov1",(16, 16, 255), Polygons.ov1, None)
    ov2 = polygon("ov2",(16, 16, 255), Polygons.ov2, None)
    ov3 = polygon("ov3",(16, 16, 255), Polygons.ov3, None )
    ov4 = polygon("ov4",(16, 16, 255), Polygons.ov4, None)
    ov5 = polygon("ov5",(16, 16, 255), Polygons.ov5, None)
    ovlijst = [ov1,ov2,ov3,ov4,ov5]
    wijklist.append(ovlijst)

''''This function gets loaded when the area: "Hillegersberg", gets selected'''
def hillegersbergWijk():
    hill1 = polygon("hill1",(16, 16, 255), Polygons.hill1, None)
    hill2 = polygon("hill2",(16, 16, 255), Polygons.hill2, None)
    hill3 = polygon("hill3",(16, 16, 255), Polygons.hill3, None)
    hill4 = polygon("hill4",(16, 16, 255), Polygons.hill4, None)
    hill5 = polygon("hill5",(16, 16, 255), Polygons.hill5, None)
    hillijst = [hill1,hill2,hill3,hill4,hill5]
    wijklist.append(hillijst)

def prinsalexanderWijk():
    pa1 = polygon("pa1",(16, 16, 255), Polygons.pa1, None)
    pa2 = polygon("pa2",(16, 16, 255), Polygons.pa2, None)
    pa3 = polygon("pa3",(16, 16, 255), Polygons.pa3, None)
    pa4 = polygon("pa4",(16, 16, 255), Polygons.pa4, None)
    pa5 = polygon("pa5",(16, 16, 255), Polygons.pa5,None)
    pa6 = polygon("pa6",(16, 16, 255), Polygons.pa6,None)
    palijst = [pa1,pa2,pa3,pa4,pa5,pa6]
    wijklist.append(palijst)

def kralingenWijk():
    kra6 = polygon("kra6",(16, 16, 255), Polygons.kra6,None)
    kra1 = polygon("kra1",(16, 16, 255), Polygons.kra1,None)
    kra2 = polygon("kra2",(16, 16, 255), Polygons.kra2,None)
    kra3 = polygon("kra3",(16, 16, 255), Polygons.kra3,None)
    kra4 = polygon("kra4",(16, 16, 255), Polygons.kra4,None)
    kra5 = polygon("kra5",(16, 16, 255), Polygons.kra5,None)
    kra7 = polygon("kra7",(16, 16, 255), Polygons.kra7,None)
    kralijst = [kra6,kra1,kra2,kra3,kra4,kra5,kra7]
    wijklist.append(kralijst)

def centrumWijk():
    centr1 = polygon("centr1",(16, 16, 255), Polygons.centr1,None)
    centr2 = polygon("centr2",(16, 16, 255), Polygons.centr2,None)
    centr3 = polygon("centr3",(16, 16, 255), Polygons.centr3,None)
    centr4 = polygon("centr4",(16, 16, 255), Polygons.centr4,None)
    centr5 = polygon("centr5",(16, 16, 255), Polygons.centr5,None)
    centr6 = polygon("centr6",(16, 16, 255), Polygons.centr6,None)
    centlijst = [centr1,centr2,centr3,centr4,centr5,centr6]
    wijklist.append(centlijst)

def noordWijk():
    nrd1 = polygon("nrd1",(16, 16, 255), Polygons.nrd1,None)
    nrd2 = polygon("nrd2",(16, 16, 255), Polygons.nrd2,None)
    nrd3 = polygon("nrd3",(16, 16, 255), Polygons.nrd3,None)
    nrd4 = polygon("nrd4",(16, 16, 255), Polygons.nrd4,None)
    nrd5 = polygon("nrd5",(16, 16, 255), Polygons.nrd5,None)
    nrd6 = polygon("nrd6",(16, 16, 255), Polygons.nrd6,None)
    nrd7 = polygon("nrd7",(16, 16, 255), Polygons.nrd7,None)
    nrdlijst = [nrd1,nrd2,nrd3,nrd4,nrd5,nrd6,nrd7]
    wijklist.append(nrdlijst)

def delftWijk():
    delf1 = polygon("delf1",(16, 16, 255), Polygons.delf1,None)
    delf2 = polygon("delf2",(16, 16, 255), Polygons.delf2,None)
    delf3 = polygon("delf3",(16, 16, 255), Polygons.delf3,None)
    delf4 = polygon("delf4",(16, 16, 255), Polygons.delf4,None)
    delf5 = polygon("delf5",(16, 16, 255), Polygons.delf5,None)
    delf6 = polygon("delf6",(16, 16, 255), Polygons.delf6,None)
    delf7 = polygon("delf7",(16, 16, 255), Polygons.delf7,None)
    delf8 = polygon("delf8",(16, 16, 255), Polygons.delf8,None)
    delflijst = [delf1,delf2,delf3,delf4,delf5,delf6,delf7,delf8]
    wijklist.append(delflijst)

def waalhavenWijk():
    waal1 = polygon("waal1",(16, 16, 255), Polygons.waal1,None)
    waal2 = polygon("waal2",(16, 16, 255), Polygons.waal2,None)
    waal3 = polygon("waal3",(16, 16, 255), Polygons.waal3,None)
    waal4 = polygon("waal4",(16, 16, 255), Polygons.waal4,None)
    waallijst = [waal1,waal2,waal3,waal4]
    wijklist.append(waallijst)

def charloisWijk():
    char1 = polygon("char1",(16, 16, 255), Polygons.char1,None)
    char2 = polygon("char2",(16, 16, 255), Polygons.char2,None)
    char3 = polygon("char3",(16, 16, 255), Polygons.char3,None)
    char4 = polygon("char4",(16, 16, 255), Polygons.char4,None)
    char5 = polygon("char5",(16, 16, 255), Polygons.char5,None)
    char6 = polygon("char6",(16, 16, 255), Polygons.char6,None)
    char7 = polygon("char7",(16, 16, 255), Polygons.char7,None)
    charlijst = [char1,char2,char3,char4,char5,char6,char7]
    wijklist.append(charlijst)

def feijenoordWijk():
    fei1 = polygon("fei1",(16, 16, 255), Polygons.fei1,None)
    fei2 = polygon("fei2",(16, 16, 255), Polygons.fei2,None)
    fei3 = polygon("fei3",(16, 16, 255), Polygons.fei3,None)
    fei4 = polygon("fei4",(16, 16, 255), Polygons.fei4,None)
    fei5 = polygon("fei5",(16, 16, 255), Polygons.fei5,None)
    fei6 = polygon("fei6",(16, 16, 255), Polygons.fei6,None)
    fei7 = polygon("fei7",(16, 16, 255), Polygons.fei7,None)
    fei8 = polygon("fei8",(16, 16, 255), Polygons.fei8,None)
    fei9 = polygon("fei9",(16, 16, 255), Polygons.fei9,None)
    feilijst = [fei1,fei2,fei3,fei4,fei5,fei6,fei7,fei8,fei9]
    wijklist.append(feilijst)

def ijsselmondeWijk():
    ijs1 = polygon("ijs1",(16, 16, 255), Polygons.ijs1,None)
    ijs2 = polygon("ijs2",(16, 16, 255), Polygons.ijs2,None)
    ijs3 = polygon("ijs3",(16, 16, 255), Polygons.ijs3,None)
    ijs4 = polygon("ijs4",(16, 16, 255), Polygons.ijs4,None)
    ijslijst = [ijs1,ijs2,ijs3,ijs4]
    wijklist.append(ijslijst)

wijklist = []

wijkkleur = (150,150,230)
''''The polygons(area's)'''''
overschie_polygon = polygon("Overschie",wijkkleur, Polygons.overschie, "Aantal inwoners: 15.769, oppervlakte: 15,80 km²")
hillegersberg_polygon = polygon("HillegersbergSchiebroek",wijkkleur, Polygons.hillegersberg, "Aantal inwoners: 15.050, oppervlakte: 4,33 km²")
prins_alexander_polygon = polygon("PrinsAlexander",wijkkleur, Polygons.prins_alexander, "Aantal inwoners: 89.225, oppervlakte: 20,24 km²")
kralingen_polygon = polygon("KralingenCrooswijk",wijkkleur, Polygons.kralingen, "Aantal inwoners: 52.000, oppervlakte: 12,9 km²")
noord_polygon = polygon("Noord",wijkkleur, Polygons.noord, "Aantal inwoners: 48.990, oppervlakte: 5,37 km²")
delftshaven_polygon = polygon("Delfshaven",wijkkleur, Polygons.delftshaven, "Aantal inwoners: 74.371, oppervlakte: 5,8 km²")
centrum_polygon = polygon("RotterdamCentrum",wijkkleur, Polygons.centrum, "Aantal inwoners: 31.363, oppervlakte: 4,81 km²")
feijenoord_polygon = polygon("Feijenoord",wijkkleur, Polygons.feijenoord, "Aantal inwoners: 72.300, oppervlakte: 6,44 km²")
ijsselmonde_polygon = polygon("IJsselmonde",wijkkleur, Polygons.ijsselmonde, "Aantal inwoners: 60.780, oppervlakte: 13.12 km²")
charlois_polygon = polygon("Charlois",wijkkleur, Polygons.charlois, "Aantal inwoners: 64.320, oppervlakte: 10.0 km²")
# waalhaven_polygon = polygon("Waalhaven",(220,215,204), Polygons.waalhaven)

canvas.create_text(rs(710),rs(290),text="Overschie\n" , font=("Helvetica",rs(15),"bold"))
canvas.create_text(rs(966),rs(250),text="Hillegersberg-\nSchiebroek", font=("Helvetica",rs(15),"bold"))
canvas.create_text(rs(1200),rs(209),text="Prins Alexander", font=("Helvetica",rs(15),"bold"))
canvas.create_text(rs(1040),rs(400),text="Kralingen-Crooswijk", font=("Helvetica",rs(15),"bold"))
canvas.create_text(rs(860),rs(400),text="Noord", font=("Helvetica",rs(15),"bold"))
canvas.create_text(rs(730),rs(534),text="Delfshaven", font=("Helvetica",rs(15),"bold"))
canvas.create_text(rs(900),rs(514),text="Rotterdam\nCentrum", font=("Helvetica",rs(15),"bold"))
canvas.create_text(rs(1000),rs(580),text="Feijenoord", font=("Helvetica",rs(15),"bold"))
canvas.create_text(rs(1180),rs(700),text="IJsselmonde", font=("Helvetica",rs(15),"bold"))
canvas.create_text(rs(885),rs(735),text="Charlois", font=("Helvetica",rs(15),"bold"))

''''Array that has the polygon area's, this is used to go through the array and then the colour will change. It is used in a database function'''
polygonsgebieden = [overschie_polygon, hillegersberg_polygon, prins_alexander_polygon, kralingen_polygon, noord_polygon, delftshaven_polygon, centrum_polygon, feijenoord_polygon, ijsselmonde_polygon, charlois_polygon]
''''The name of the area that is displayed in the top centre.'''
text = Label(root,width=0, height=1,text="",font=("Helvetica",35,"bold")) #Creates text
text.grid(row=0,column=0,sticky=N) #Draws the text

''''Function that gives mouse positions'''
def motion(event):
    if event.x > 500 and event.y < 279:
        text.config(text="")
    else:
        text.config(text="Rotterdam")

def leftclick(event):
    for wijk in polygonsgebieden:
        if canvas.find_withtag(CURRENT) == canvas.find_withtag(wijk.name):
            wijk.Select()

def rightclick(event):
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

def resetwijken():
    for wijk in polygonsgebieden:
        wijk.Reset()

''''when a polygon(area) is clicked, the click method will be activated'''''
canvas.bind('<Button-1>', leftclick, add="+") #Binds the canvas to the click method
#canvas.bind('<Button-3>', rightclick, add="+")
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
welcome_text = "Klik op de Homeknop op het menu te openen" #Test that appears on the menu
description_text = Label(root,text=welcome_text,font=("Helvetica",15,"bold")) #Sets the text on the page
description_text.grid(row=1,column=0,sticky=W) #Sets the position of the text

''''the home page'''
def home():
    global searchPage
    variable.set("Home")
    resetwijken()
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


''''The about page'''
def about():
    global searchPage
    resetwijken()
    text.config(text="") #Resets the text when it reaches the home button
    for widget in root.winfo_children():
        if widget == menu_button or widget == text: #Optionmenu does not get deleted
            print("Optionmenu")
        elif widget == canvas: #Canvas does not get deleted
            print("canvas")
        else:
            widget.destroy() #Other widgets are deleted and so are their value
            print(str(widget) + " Is deleted")

    about_text = "Gemaakt voor Project 3 Open Data - Hogeschool Rotterdam."
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

    resetwijken()
    text.config(text="") #Resets the text when it reaches the home button
    for widget in root.winfo_children():
        if widget == menu_button or widget == text: #Menu button will not be deleted
            print("Optionmenu is not deleted")
        elif widget == canvas: #Canvas will not be deleted
            print("canvas")
        else:
            widget.destroy() #Other widgets are deleted
            print(str(widget) + " Is deleted")

    button9 = NewButton("Bevolking", 1, 0, screenx / 30, screeny / 150) #Creates button
    button9.pageClick(categoryPopulation) #Goes to the sub categories of the selected button
    button10 = NewButton("Veiligheid", 2, 0, screenx / 45, screeny / 150)
    button10.pageClick(categoryEnvironment)
    button11 = NewButton("Omgeving & Milieu", 3, 0, screenx / 17, screeny / 150)
    button11.pageClick(categorySafety)
    button12 = NewButton("Sociaal", 4, 0, screenx / 17, screeny / 150)
    button12.pageClick(categoryTraffic)
    button13 = NewButton("Voorzieningen", 5, 0, screenx / 22, screeny / 150)
    button13.pageClick(categoryServices)
    button14 = NewButton("Overig", 6, 0, screenx / 18, screeny / 150)
    button14.pageClick(categoryOther)
    button52 = NewButton("Terug", 28, 0, screenx / 600, screeny / 150)  #Currently not used, can be used to give the user stats when clicked
    button52.pageClick(home)
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

        Radiobutton(root, indicatoron=False, text="Belangrijk", variable=self.variable, value=1).grid(column=0,row=self.row1,sticky=W)
        Radiobutton(root, indicatoron=False, text="Onbelangrijk", variable=self.variable, value=2).grid(column=0, row=self.row2, sticky=W)



''''Woningsadvies page'''
def woningsadvies():
    global searchPage
    global bevolking_radioButtons #Reads a global variable, this was one of the best options for this
    global milieu_radioButtons
    global veiligheid_radioButtons
    global verkeer_radioButtons
    global voorzieningen_radioButtons
    resetwijken()
    text.config(text="") #Resets the text when it reaches the home button

    for widget in root.winfo_children():
        if widget == menu_button or widget == text or widget == canvasWijk: #Menu does not get deleted
            print("Optionmenu will not be deleted")
        elif widget == canvas: #Canvas does not get deleted
            print("canvas")
        else:
            widget.destroy()
            print(str(widget) + " Is deleted")

    woningsadvies_text = "Kies wat je belangrijk vind"
    woningsadvies_text1 = "Veiligheid"
    woningsadvies_text2 = "Milieu"
    woningsadvies_text3 = "Sociaal"
    woningsadvies_text4 = "Voorzieningen"
    woningsadvies_text5 = "Fysiek"

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
    button51 = NewButton("Welke wijk is het geschikst?", 28, 0, screenx / 600, 0)
    button51.pageClick(databaseWoningsAdvies)
    canvas.grid(row=2, column=0, sticky=W, rowspan=999, padx=55)
    searchPage = True


''''Population/bevolking category, when it gets clicked these buttons appears, and when buttons are clicked they will go to the database function'''
def categoryPopulation():
    global searchPage
    for widget in root.winfo_children():
        if widget == menu_button or widget == text: #Optionmenu does not get deleted
            print("Optionmenu")
        elif widget == canvas: #Canvas does not get deleted
            print("canvas")
        else:
            widget.destroy() #Other widgets are deleted and so are their value
            print(str(widget) + " Is deleted")


    text.config(text="") #Resets the text when it reaches the home button
    button15 = PecButton("Verdeling afkomst", 1, 0, screenx / 30, screeny / 150, 0)
    button16 = PecButton("Werkende jongeren (18 t/m 22 jr)", 2, 0, screenx / 45, screeny / 150,1)
    button17 = PecButton("Werkzoekende jongeren (18 t/m 22 jr)", 3, 0, screenx / 17, screeny / 150,2)
    button18 = PecButton("Bewoners met werk(23 t/m 64 jr)", 4, 0, screenx / 17, screeny / 150,3)
    button19 = PecButton("Werkzoekende bewoners(23 t/m 64 jr)", 5, 0, screenx / 22, screeny / 150,4)
    button20 = PecButton("Bewoners 18jr en ouder dat kort in Nederland woont", 6, 0, screenx / 22, screeny / 150,5)
    buttonback1 = NewButton("Terug", 7, 0, screenx / 22, screeny / 150)
    buttonback1.pageClick(percentagesEnCijfers) #The back button
    searchPage = True

''''Population/bevolking category, when it gets clicked these buttons appears, and when buttons are clicked they will go to the database function'''
def categoryEnvironment():
    global searchPage
    for widget in root.winfo_children():
        if widget == menu_button or widget == text: #Optionmenu does not get deleted
            print("Optionmenu")
        elif widget == canvas: #Canvas does not get deleted
            print("canvas")
        else:
            widget.destroy() #Other widgets are deleted and so are their value
            print(str(widget) + " Is deleted")

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
    for widget in root.winfo_children():
        if widget == menu_button or widget == text: #Optionmenu does not get deleted
            print("Optionmenu")
        elif widget == canvas: #Canvas does not get deleted
            print("canvas")
        else:
            widget.destroy() #Other widgets are deleted and so are their value
            print(str(widget) + " Is deleted")

    text.config(text="") #Resets the text when it reaches the home button
    button27 = PecButton("Milieu objectief", 1, 0, screenx / 30, screeny / 150,12)
    button28 = PecButton("% woningen in geluidscontour vanaf 55 dB", 2, 0, screenx / 45, screeny / 150,13)
    button29 = PecButton("gemiddelde NO2-concentratie", 3, 0, screenx / 17, screeny / 150,14)
    button30 = PecButton("% voldoende aanwezig groen (grasveldjes, bomen)", 4, 0, screenx / 17, screeny / 150,15)
    button31 = PecButton("% veel stankoverlast verkeer", 5, 0, screenx / 22, screeny / 150,16)
    button32 = PecButton("% veel geluidsoverlast verkeer", 6, 0, screenx / 22, screeny / 150,17)
    buttonback3 = NewButton("Terug", 7, 0, screenx / 22, screeny / 150)
    buttonback3.pageClick(percentagesEnCijfers)
    searchPage = True

''''Population/bevolking category, when it gets clicked these buttons appears, and when buttons are clicked they will go to the database function'''
def categoryTraffic():
    global searchPage
    for widget in root.winfo_children():
        if widget == menu_button or widget == text: #Optionmenu does not get deleted
            print("Optionmenu")
        elif widget == canvas: #Canvas does not get deleted
            print("canvas")
        else:
            widget.destroy() #Other widgets are deleted and so are their value
            print(str(widget) + " Is deleted")

    text.config(text="") #Resets the text when it reaches the home button
    button33 = PecButton("Sociale Index subjectief", 1, 0, screenx / 30, screeny / 150,18)
    button34 = PecButton("Oordeel kwaliteit van leven", 2, 0, screenx / 45, screeny / 150,19)
    button35 = PecButton("Capaciteiten-subjectief", 3, 0, screenx / 17, screeny / 150,20)
    button36 = PecButton("Leefomgeving-subjectief", 4, 0, screenx / 17, screeny / 150,21)
    button37 = PecButton("Meedoen-subjectief", 5, 0, screenx / 22, screeny / 150,22)
    button38 = PecButton("Binding-subjectief", 6, 0, screenx / 22, screeny / 150,23)
    buttonback4 = NewButton("Terug", 7, 0, screenx / 22, screeny / 150)
    buttonback4.pageClick(percentagesEnCijfers)
    searchPage = True

''''Population/bevolking category, when it gets clicked these buttons appears, and when buttons are clicked they will go to the database function'''
def categoryServices():
    global searchPage
    for widget in root.winfo_children():
        if widget == menu_button or widget == text: #Optionmenu does not get deleted
            print("Optionmenu")
        elif widget == canvas: #Canvas does not get deleted
            print("canvas")
        else:
            widget.destroy() #Other widgets are deleted and so are their value
            print(str(widget) + " Is deleted")

    text.config(text="") #Resets the text when it reaches the home button
    button39 = PecButton("% woningen met bakker binnen normafstand", 1, 0, screenx / 30, screeny / 150,24)
    button40 = PecButton("% woningen met groenteboer binnen normafstand", 2, 0, screenx / 45, screeny / 150,25)
    button41 = PecButton("% woningen met slager binnen normafstand", 3, 0, screenx / 17, screeny / 150,26)
    button42 = PecButton("% woningen met bushaltes binnen normafstand", 4, 0, screenx / 17, screeny / 150,27)
    button43 = PecButton("% woningen met metrostations binnen normafstand", 5, 0, screenx / 22, screeny / 150,28)
    button44 = PecButton("% woningen met tramhaltes binnen normafstand", 6, 0, screenx / 22, screeny / 150,29)
    buttonback5 = NewButton("Terug", 7, 0, screenx / 22, screeny / 150)
    buttonback5.pageClick(percentagesEnCijfers)
    searchPage = True

''''Population/bevolking category, when it gets clicked these buttons appears, and when buttons are clicked they will go to the database function'''
def categoryOther():
    global searchPage
    for widget in root.winfo_children():
        if widget == menu_button or widget == text: #Optionmenu does not get deleted
            print("Optionmenu")
        elif widget == canvas: #Canvas does not get deleted
            print("canvas")
        else:
            widget.destroy() #Other widgets are deleted and so are their value
            print(str(widget) + " Is deleted")

    text.config(text="") #Resets the text when it reaches the home button
    button45 = PecButton("gemiddelde WOZ per m2 woningoppervlakte", 1, 0, screenx / 30, screeny / 150,30)
    button46 = PecButton("drugsoverlast gedurende de jaren 2006-2011", 2, 0, screenx / 45, screeny / 150,31)
    button47 = PecButton("geweldsdelicten gedurende de jaren 2006-2011", 3, 0, screenx / 17, screeny / 150,32)
    button48 = PecButton("tevredenheid gedurende de jaren 2006-2011", 4, 0, screenx / 17, screeny / 150,33)
    button49 = PecButton("fietsendiefstal gedurende de jaren 2006-2011", 5, 0, screenx / 22, screeny / 150,34)
    button50 = PecButton("% vaak hondenpoep", 6, 0, screenx / 22, screeny / 150,35)
    buttonback6 = NewButton("Terug", 7, 0, screenx / 22, screeny / 150)
    buttonback6.pageClick(percentagesEnCijfers)
    searchPage = True

woonadviesqueries = []
''''Database query for the page: "Woningsadvies (the user gets data based on selection)'''''
def databaseWoningsAdvies():
    global bevolking_radioButtons
    global milieu_radioButtons
    global veiligheid_radioButtons
    global verkeer_radioButtons
    global voorzieningen_radioButtons

    print(bevolking_radioButtons.get()) #To prove that when a different radiobutton is selected, the value changes
    if bevolking_radioButtons.get() == 1: #gets value of the radiobutton(which button the user selected)
        if ("Veiligheidsindex", "vi2016") not in woonadviesqueries:
            woonadviesqueries.append(("Veiligheidsindex","vi2016"))
    if bevolking_radioButtons.get() == 2:
        if ("Veiligheidsindex","vi2016") in woonadviesqueries:
            woonadviesqueries.remove(("Veiligheidsindex","vi2016"))


    if milieu_radioButtons.get() == 1:
        if ("MilieuObjectief", "fiobj2016") not in woonadviesqueries:
            woonadviesqueries.append(("MilieuObjectief", "fiobj2016"))
    if milieu_radioButtons.get() == 2:
        if ("MilieuObjectief", "fiobj2016") in woonadviesqueries:
            woonadviesqueries.remove(("MilieuObjectief", "fiobj2016"))

    if veiligheid_radioButtons.get() == 1:
        if ("SocialeIndex", "si2016") not in woonadviesqueries:
            woonadviesqueries.append(("SocialeIndex", "si2016"))
    if veiligheid_radioButtons.get() == 2:
        if ("SocialeIndex", "si2016") in woonadviesqueries:
            woonadviesqueries.remove(("SocialeIndex", "si2016"))

    if verkeer_radioButtons.get() == 1:
        if ("VoorzieningenSubjectief", "fisub2016") not in woonadviesqueries:
            woonadviesqueries.append(("VoorzieningenSubjectief", "fisub2016"))
    if verkeer_radioButtons.get() == 2:
        if ("VoorzieningenSubjectief", "fisub2016") in woonadviesqueries:
            woonadviesqueries.remove(("VoorzieningenSubjectief", "fisub2016"))


    if voorzieningen_radioButtons.get() == 1:
        if ("FysiekeIndex", "fisub2016") not in woonadviesqueries:
            woonadviesqueries.append(("FysiekeIndex", "fisub2016"))
    if voorzieningen_radioButtons.get() == 2:
        if ("FysiekeIndex", "fisub2016") in woonadviesqueries:
            woonadviesqueries.remove(("FysiekeIndex", "fisub2016"))

    # print(woonadviesqueries)



    for wijk in polygonsgebieden:
        wijk.waarde = 0


    for i in woonadviesqueries:
        PlotWijkAdvies(i[1], i[0], polygonsgebieden)

''''Database query for the page: "Percentages en cijfers" the plot graphics '''

''''Database query for the page: "Percentages en cijfers"'''
''''This page will be called when buttons from the: "Percentages en cijfers", are selected. The method call is set in the class of the buttons'''
def databasePercentagesEnCijfers():
    global buttonArray #needed because the array has the last selected button of the page: "Percentages en cijfers'
    answer = (buttonArray[-1]) #last selected button gets stored in answer
    print(answer) #To prove that the last selected button is saved in the array
    if answer == 0:  #the numbers represent the button, each button has his own number. The attribute of the button that stores this is: name
        if len(geselecteerdegebieden)==1:
            PlotPieChart(geselecteerdegebieden)
        else:
            messagebox.showinfo("Minimaal 1 gebied.", "Selecteer mini- en maximaal 1 gebied alstublieft.")
            # PlotBarChart("schoolgaande en studerende jongeren (18 t/m 22 jr)","si2016","PercentageSchoolgaandeEnStuderendeJongeren18TM22jr".lower(),geselecteerdegebieden)
         #The query get send into the showresults function, then the map colour gets changed based on the results from it
        # else:
        #     PlotOnMap("si2016","PercentageSchoolgaandeEnStuderendeJongeren18TM22jr".lower(),polygonsgebieden)
    elif answer == 1:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("werkende jongeren (18 t/m 22 jr)","si2016","PercentageWerkendeJongeren18TM22jr".lower(),geselecteerdegebieden)
        else:
            PlotOnMap("si2016","PercentageWerkendeJongeren18TM22jr".lower(),polygonsgebieden)
    elif answer == 2:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("werkzoekende jongeren (18 t/m 22 jr)","si2016","PercentageWerkzoekendeJongeren18TM22JrZonderBaan".lower(),geselecteerdegebieden)
        else:
            PlotOnMap("si2016","PercentageWerkzoekendeJongeren18TM22JrZonderBaan".lower(),polygonsgebieden)
    elif answer == 3:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("werkzoeknde bewoners(23 t/m 64 jr)","si2016","PercentageBewoners23TM64JrMetWerk".lower(),geselecteerdegebieden)
        else:
            PlotOnMap("si2016","PercentageBewoners23TM64JrMetWerk".lower(),polygonsgebieden)
    elif answer == 4:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("werkzoeknde bewoners(23 t/m 64 jr)","si2016","PercentageWerkzoekendeBewoners23TM64JrZonderBaan".lower(),geselecteerdegebieden)
        else:
            PlotOnMap("si2016","PercentageWerkzoekendeBewoners23TM64JrZonderBaan".lower(),polygonsgebieden)
    elif answer == 5:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("Bewoners 18jr en ouder dat kort in Nederland woont","si2016","PercentageBewoners18JrEnOuderDatNogMaarKortInNederlandWoont".lower(),geselecteerdegebieden)
        else:
            PlotOnMap("si2016","PercentageBewoners18JrEnOuderDatNogMaarKortInNederlandWoont".lower(),polygonsgebieden)
    elif  answer == 6:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("Veiligheidsindex -objectief","vi2016","veiligheidsindexobjectief".lower(),geselecteerdegebieden)
        else:
            PlotOnMap("vi2016","veiligheidsindexobjectief".lower(),polygonsgebieden)
    elif answer == 7:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("Diefstal-objectief","vi2016","diefstalobjectief".lower(),geselecteerdegebieden)
        else:
            PlotOnMap("vi2016","diefstalobjectief".lower(),polygonsgebieden)
    elif answer == 8:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("Geweld-objectief","vi2016","geweldobjectief".lower(),geselecteerdegebieden)
        else:
            PlotOnMap("vi2016","geweldobjectief".lower(),polygonsgebieden)
    elif answer == 9:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("Inbraak-objectief","vi2016","inbraakobjectief".lower(),geselecteerdegebieden)
        else:
            PlotOnMap("vi2016","inbraakobjectief".lower(),polygonsgebieden)
    elif answer == 10:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("Vandalisme-objectief","vi2016","vandalismeobjectief".lower(),geselecteerdegebieden)
        else:
            PlotOnMap("vi2016","vandalismeobjectief".lower(),polygonsgebieden)
    elif answer == 11:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("Overlast objectief","vi2016","overlastobjectief".lower(),geselecteerdegebieden)
        else:
            PlotOnMap("vi2016","overlastobjectief".lower(),polygonsgebieden)

    elif answer == 12:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("Milieu objectief","fiobj2016","milieuobjectief".lower(),geselecteerdegebieden)
        else:
            PlotOnMap("fiobj2016","milieuobjectief".lower(),polygonsgebieden)
    elif answer == 13:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("% woningen in geluidscontour vanaf 55 dB","fiobj2016","percentagewoningeningeluidscontourvanaf55db".lower(),geselecteerdegebieden)
        else:
            PlotOnMap("fiobj2016","percentagewoningeningeluidscontourvanaf55db".lower(),polygonsgebieden)
    elif answer == 14:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("gemiddelde NO2-concentratie","fiobj2016","GemiddeldeNo2Concentratie2009IrtGrenswaarde40mgM3".lower(),geselecteerdegebieden)
        else:
            PlotOnMap("fiobj2016","GemiddeldeNo2Concentratie2009IrtGrenswaarde40mgM3".lower(),polygonsgebieden)
    elif answer == 15:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("% voldoende aanwezig groen (grasveldjes, bomen)","fisub2016","PercentageVoldoendeAanwezigGroenGrasveldjesBomen".lower(),geselecteerdegebieden)
        else:
            PlotOnMap("fisub2016","PercentageVoldoendeAanwezigGroenGrasveldjesBomen".lower(),polygonsgebieden)

    elif answer == 16:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("% veel stankoverlast verkeer","fisub2016","PercentageVeelStankoverlastVerkeer".lower(),geselecteerdegebieden)
        else:
            PlotOnMap("fisub2016","PercentageVeelStankoverlastVerkeer".lower(),polygonsgebieden)
    elif answer == 17:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("% veel geluidsoverlast verkeer","fisub2016","PercentageVeelGeluidsoverlastVerkeer".lower(),geselecteerdegebieden)
        else:
            PlotOnMap("fisub2016","PercentageVeelGeluidsoverlastVerkeer".lower(),polygonsgebieden)

    elif answer == 18:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("Sociale Index subjectief","si2016","SocialeIndexSubjectief".lower(),geselecteerdegebieden)
        else:
            PlotOnMap("si2016","SocialeIndexSubjectief".lower(),polygonsgebieden)
    elif answer == 19:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("Oordeel kwaliteit van leven","si2016","OordeelKwaliteitVanLeven".lower(),geselecteerdegebieden)
        else:
            PlotOnMap("si2016","OordeelKwaliteitVanLeven".lower(),polygonsgebieden)
    elif answer == 20:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("Capaciteiten-subjectief","si2016","CapaciteitenSubjectief".lower(),geselecteerdegebieden)
        else:
            PlotOnMap("si2016","CapaciteitenSubjectief".lower(),polygonsgebieden)
    elif answer == 21:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("Leefomgeving-subjectief","si2016","LeefomgevingSubjectief".lower(),geselecteerdegebieden)
        else:
            PlotOnMap("si2016","LeefomgevingSubjectief".lower(),polygonsgebieden)
    elif answer == 22:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("Meedoen-subjectief","si2016","MeedoenSubjectief".lower(),geselecteerdegebieden)
        else:
            PlotOnMap("si2016","MeedoenSubjectief".lower(),polygonsgebieden)
    elif answer == 23:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("Binding-subjectief","si2016","BindingSubjectief".lower(),geselecteerdegebieden)
        else:
            PlotOnMap("si2016","BindingSubjectief".lower(),polygonsgebieden)
    elif answer == 24:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("% woningen met bakker binnen normafstand","fiobj2016","PercentageWoningenMetBakkerBinnenNormafstand".lower(),geselecteerdegebieden)
        else:
            PlotOnMap("fiobj2016","PercentageWoningenMetBakkerBinnenNormafstand".lower(),polygonsgebieden)
    elif answer == 25:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("% woningen met groenteboer binnen normafstand","fiobj2016","PercentageWoningenMetGroenteboerBinnenNormafstand".lower(),geselecteerdegebieden)
        else:
            PlotOnMap("fiobj2016","PercentageWoningenMetGroenteboerBinnenNormafstand".lower(),polygonsgebieden)
    elif answer == 26:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("% woningen met slager binnen normafstand","fiobj2016","PercentageWoningenMetSlagerBinnenNormafstand".lower(),geselecteerdegebieden)
        else:
            PlotOnMap("fiobj2016","PercentageWoningenMetSlagerBinnenNormafstand".lower(),polygonsgebieden)
    elif answer == 27:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("% woningen met bushaltes binnen normafstand","fiobj2016","PercentageWoningenMetBushaltesBinnenNormafstand".lower(),geselecteerdegebieden)
        else:
            PlotOnMap("fiobj2016","PercentageWoningenMetBushaltesBinnenNormafstand".lower(),polygonsgebieden)
    elif answer == 28:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("% woningen met metrostations binnen normafstand","fiobj2016","PercentageWoningenMetMetrostationsBinnenNormafstand".lower(),geselecteerdegebieden)
        else:
            PlotOnMap("fiobj2016","PercentageWoningenMetMetrostationsBinnenNormafstand".lower(),polygonsgebieden)
    elif answer == 29:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("% woningen met tramhaltes binnen normafstand","fiobj2016","PercentageWoningenMetTramhaltesBinnenNormafstand".lower(),geselecteerdegebieden)
        else:
            PlotOnMap("fiobj2016","PercentageWoningenMetTramhaltesBinnenNormafstand".lower(),polygonsgebieden)
    elif answer == 30:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("gemiddelde WOZ per m2 woningoppervlakte","fiobj2016","GemiddeldeWozPerM2Woningoppervlakte".lower(),geselecteerdegebieden)
        else:
            PlotOnMap("fiobj2016","GemiddeldeWozPerM2Woningoppervlakte".lower(),polygonsgebieden)
    elif answer == 31:
        if len(geselecteerdegebieden)>0:
            PlotLineChart("drugsoverlast gedurende de jaren 2006-2011","drugsoverlast".lower(),geselecteerdegebieden)
        else:
            PlotOnMap("drugsoverlast".lower(),"data2011", polygonsgebieden)
    elif answer == 32:
        if len(geselecteerdegebieden)>0:
            PlotLineChart("geweldsdelicten gedurende de jaren 2006-2011","geweldsdelicten".lower(), geselecteerdegebieden)
        else:
            PlotOnMap("geweldsdelicten".lower(), "data2011", polygonsgebieden)
    elif answer == 33:
        if len(geselecteerdegebieden)>0:
            PlotLineChart("tevredenheid gedurende de jaren 2006-2011","tevredenheid".lower(), geselecteerdegebieden)
        else:
            PlotOnMap("tevredenheid".lower(),"data2011",polygonsgebieden)
    elif answer == 34:
        if len(geselecteerdegebieden)>0:
            PlotLineChart("fietsendiefstal gedurende de jaren 2006-2011","fietsendiefstal".lower(), geselecteerdegebieden)
        else:
            PlotOnMap("fietsendiefstal".lower(),"data2011",polygonsgebieden)
    elif answer == 35:
        if len(geselecteerdegebieden)>0:
            PlotBarChart("% vaak hondenpoep","fisub2016","PercentageVaakHondenpoep".lower(),geselecteerdegebieden)
        else:
            PlotOnMap("fisub2016", "PercentageVaakHondenpoep".lower(),polygonsgebieden)

for widget in root.winfo_children():
    print(widget)
root.mainloop() #for the loop
