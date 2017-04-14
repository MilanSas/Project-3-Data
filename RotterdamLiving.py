from tkinter import * #Needed for GUI
import matplotlib #Needed for graph
matplotlib.use("TKAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
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
class polygon:
    def __init__(self,name,color,list):
        self.name = name
        self.color = color
        self.selected = False
        self.shape = canvas.create_polygon(list, fill=(HexToRGB(color)), outline='black', width=2, tags = self.name)
        canvas.move(self.shape, rs(-400), 0)


    def ChangeColor(self, percent):
        colorrange = percent * 255 //100
        for n in range(64, colorrange-15):
            print(255-n)
            color = (255-n, 255-n, 255)
            canvas.itemconfig(self.shape, fill=HexToRGB(color))
            root.update()
            time.sleep(0.0000000001)

    def Select(self):
        if self.selected:
            self.deSelect()
            return
        geselecteerdegebieden.append(self.name)
        self.selected = True
        canvas.itemconfig(self.shape, outline = 'red')

    def deSelect(self):
        geselecteerdegebieden.remove(self.name)
        self.selected = False
        canvas.itemconfig(self.shape, outline='black')




''''This function gets loaded when the area: "Overschie", gets selected'''
def overschieWijk():
    ov1 = polygon("ov1",(120, 50, 120), (
        rsWijken(949), rsWijken(342), rsWijken(964), rsWijken(322), rsWijken(1003), rsWijken(366), rsWijken(1050), rsWijken(345), rsWijken(1035), rsWijken(295), rsWijken(939), rsWijken(304)))
    ov2 = polygon("ov2",(120, 50, 120), (
        rsWijken(1050), rsWijken(345), rsWijken(1059), rsWijken(350), rsWijken(1052), rsWijken(359), rsWijken(1073), rsWijken(389), rsWijken(1128), rsWijken(354), rsWijken(1101), rsWijken(310),
        rsWijken(1076), rsWijken(269), rsWijken(1035), rsWijken(295)))
    ov3 = polygon("ov3",(120, 50, 120), (rsWijken(1052), rsWijken(359), rsWijken(1017), rsWijken(403), rsWijken(1057), rsWijken(479), rsWijken(1136), rsWijken(468)))
    ov4 = polygon("ov4",(120, 50, 120), (rsWijken(1109), rsWijken(432), rsWijken(1173), rsWijken(392), rsWijken(1128), rsWijken(354), rsWijken(1073), rsWijken(389)))
    ov5 = polygon("ov5",(120, 50, 120), (
        rsWijken(904), rsWijken(194), rsWijken(947), rsWijken(183), rsWijken(955), rsWijken(205), rsWijken(1106), rsWijken(109), rsWijken(1176), rsWijken(199), rsWijken(1222), rsWijken(163),
        rsWijken(1242), rsWijken(185), rsWijken(1237), rsWijken(355), rsWijken(1173), rsWijken(392), rsWijken(1128), rsWijken(354), rsWijken(1072), rsWijken(269), rsWijken(1035), rsWijken(295),
        rsWijken(939), rsWijken(304)))

''''This function gets loaded when the area: "Hillegersberg", gets selected'''
def hillegersbergWijk():
    hill1 = polygon("hill1",(120, 50, 120),
                    (rsWijken(1242), rsWijken(185), rsWijken(1239), rsWijken(309), rsWijken(1288), rsWijken(310), rsWijken(1363), rsWijken(143), rsWijken(1280), rsWijken(90)))
    hill2 = polygon("hill2",(120, 50, 120), (
        rsWijken(1239), rsWijken(306), rsWijken(1237), rsWijken(355), rsWijken(1356), rsWijken(322), rsWijken(1337), rsWijken(300), rsWijken(1328), rsWijken(312), rsWijken(1298), rsWijken(286),
        rsWijken(1288), rsWijken(310)))
    hill3 = polygon("hill3",(120, 50, 120), (
        rsWijken(1298), rsWijken(286), rsWijken(1328), rsWijken(312), rsWijken(1337), rsWijken(300), rsWijken(1356), rsWijken(322), rsWijken(1430), rsWijken(282), rsWijken(1375), rsWijken(226),
        rsWijken(1383), rsWijken(154), rsWijken(1363), rsWijken(143)))
    hill4 = polygon("hill4",(120, 50, 120), (
        rsWijken(1382), rsWijken(165), rsWijken(1375), rsWijken(226), rsWijken(1430), rsWijken(282), rsWijken(1475), rsWijken(213), rsWijken(1432), rsWijken(195), rsWijken(1428), rsWijken(172),
        rsWijken(1387), rsWijken(141)))
    hill5 = polygon("hill5",(120, 50, 120),
                    (rsWijken(1356), rsWijken(322), rsWijken(1520), rsWijken(282), rsWijken(1499), rsWijken(189), rsWijken(1475), rsWijken(213), rsWijken(1432), rsWijken(195)))

def prinsalexanderWijk():
    pa1 = polygon("pa1",(120, 50, 120), (
        rsWijken(1499), rsWijken(189), rsWijken(1523), rsWijken(292), rsWijken(1602), rsWijken(269), rsWijken(1650), rsWijken(227), rsWijken(1627), rsWijken(169), rsWijken(1595), rsWijken(134)))
    pa2 = polygon("pa2",(120, 50, 120), (rsWijken(1523), rsWijken(292), rsWijken(1543), rsWijken(370), rsWijken(1622), rsWijken(351), rsWijken(1602), rsWijken(269)))
    pa3 = polygon("pa3",(120, 50, 120), (
        rsWijken(1543), rsWijken(370), rsWijken(1562), rsWijken(454),rsWijken(1661), rsWijken(425), rsWijken(1654), rsWijken(384), rsWijken(1637), rsWijken(389), rsWijken(1622), rsWijken(351)))
    pa4 = polygon("pa4",(120, 50, 120), (
        rsWijken(1622), rsWijken(351), rsWijken(1637), rsWijken(389), rsWijken(1654), rsWijken(384), rsWijken(1651), rsWijken(350), rsWijken(1693), rsWijken(337), rsWijken(1650), rsWijken(227),
        rsWijken(1602), rsWijken(269)))
    pa5 = polygon("pa5",(120, 50, 120), (
        rsWijken(1650), rsWijken(227), rsWijken(1663), rsWijken(222), rsWijken(1673), rsWijken(233), rsWijken(1742), rsWijken(188), rsWijken(1725), rsWijken(163), rsWijken(1719), rsWijken(119),
        rsWijken(1680), rsWijken(145), rsWijken(1627), rsWijken(169)))
    pa6 = polygon("pa6",(120, 50, 120), (
        rsWijken(1680), rsWijken(145), rsWijken(1719), rsWijken(119), rsWijken(1725), rsWijken(163), rsWijken(1742), rsWijken(188), rsWijken(1821), rsWijken(141), rsWijken(1791), rsWijken(116),
        rsWijken(1815), rsWijken(31), rsWijken(1804), rsWijken(12), rsWijken(1617), rsWijken(76)))

def kralingenWijk():
    kra6 = polygon("kra6",(120, 50, 120), (
        rsWijken(1521), rsWijken(282), rsWijken(1464), rsWijken(296), rsWijken(1380), rsWijken(356), rsWijken(1407), rsWijken(396), rsWijken(1446), rsWijken(417), rsWijken(1447), rsWijken(448),
        rsWijken(1434), rsWijken(481), rsWijken(1468), rsWijken(515), rsWijken(1542), rsWijken(512), rsWijken(1538), rsWijken(498), rsWijken(1562), rsWijken(454)))
    kra1 = polygon("kra1",(120, 50, 120), (
        rsWijken(1464), rsWijken(296), rsWijken(1380), rsWijken(356), rsWijken(1393), rsWijken(375), rsWijken(1377), rsWijken(395), rsWijken(1334), rsWijken(379), rsWijken(1331), rsWijken(330)))
    kra2 = polygon("kra2",(120, 50, 120), (
        rsWijken(1393), rsWijken(375), rsWijken(1377), rsWijken(395), rsWijken(1334), rsWijken(379), rsWijken(1335), rsWijken(419), rsWijken(1384), rsWijken(420), rsWijken(1407), rsWijken(396)))
    kra3 = polygon("kra3",(120, 50, 120), (rsWijken(1335), rsWijken(419), rsWijken(1337), rsWijken(454), rsWijken(1382),rsWijken(461), rsWijken(1384), rsWijken(420)))
    kra4 = polygon("kra4",(120, 50, 120), (
        rsWijken(1382), rsWijken(461), rsWijken(1384), rsWijken(420), rsWijken(1407), rsWijken(396), rsWijken(1446), rsWijken(417), rsWijken(1447), rsWijken(448), rsWijken(1434), rsWijken(481)))
    kra5 = polygon("kra5",(120, 50, 120),
                   (rsWijken(1382), rsWijken(462), rsWijken(1434), rsWijken(481), rsWijken(1469), rsWijken(515), rsWijken(1453), rsWijken(522), rsWijken(1397), rsWijken(500)))
    kra7 = polygon("kra7",(120, 50, 120), (
        rsWijken(1453), rsWijken(522), rsWijken(1469), rsWijken(515), rsWijken(1542), rsWijken(514), rsWijken(1572), rsWijken(594), rsWijken(1489), rsWijken(616), rsWijken(1469), rsWijken(593)))

def centrumWijk():
    centr1 = polygon("centr1",(120, 50, 120), (
    (1243), rsWijken(461), rsWijken(1206), rsWijken(462), rsWijken(1208), rsWijken(455), rsWijken(1288), rsWijken(443), rsWijken(1299), rsWijken(445), rsWijken(1299), rsWijken(458),
    rsWijken(1272), rsWijken(468), rsWijken(1243), rsWijken(470)))
    centr2 = polygon("centr2",(120, 50, 120), (rsWijken(1243), rsWijken(470), rsWijken(1272), rsWijken(468), rsWijken(1281), rsWijken(511), rsWijken(1247), rsWijken(539)))
    centr3 = polygon("centr3",(120, 50, 120), (
        rsWijken(1247), rsWijken(539), rsWijken(1223), rsWijken(553), rsWijken(1244), rsWijken(558), rsWijken(1245), rsWijken(562), rsWijken(1298), rsWijken(541), rsWijken(1281), rsWijken(511)))
    centr4 = polygon("centr4",(120, 50, 120), (
        rsWijken(1299), rsWijken(458), rsWijken(1272), rsWijken(468), rsWijken(1281), rsWijken(511), rsWijken(1298), rsWijken(541), rsWijken(1309), rsWijken(537), rsWijken(1316), rsWijken(501)))
    centr5 = polygon("centr5",(120, 50, 120), (
        rsWijken(1299), rsWijken(445), rsWijken(1337), rsWijken(454), rsWijken(1382), rsWijken(461), rsWijken(1397), rsWijken(500), rsWijken(1375), rsWijken(506), rsWijken(1330), rsWijken(563),
        rsWijken(1314), rsWijken(547), rsWijken(1300), rsWijken(547), rsWijken(1298), rsWijken(541), rsWijken(1309), rsWijken(537), rsWijken(1316), rsWijken(501), rsWijken(1299), rsWijken(458),
        rsWijken(1299), rsWijken(445)))
    centr6 = polygon("centr6",(120, 50, 120), (
        rsWijken(1245), rsWijken(562), rsWijken(1298), rsWijken(541), rsWijken(1300), rsWijken(547), rsWijken(1314), rsWijken(547), rsWijken(1330), rsWijken(563), rsWijken(1322), rsWijken(574),
        rsWijken(1262), rsWijken(614)))

def noordWijk():
    nrd1 = polygon("nrd1", (120, 50, 120), (
        rsWijken(1109), rsWijken(432), rsWijken(1136), rsWijken(468), rsWijken(1168), rsWijken(464), rsWijken(1181), rsWijken(452), rsWijken(1190), rsWijken(395), rsWijken(1173), rsWijken(394)))
    nrd2 = polygon("nrd2",(120, 50, 120), (
        rsWijken(1173), rsWijken(394), rsWijken(1190), rsWijken(395), rsWijken(1181), rsWijken(452), rsWijken(1168), rsWijken(464), rsWijken(1206), rsWijken(462), rsWijken(1208), rsWijken(455),
        rsWijken(1240), rsWijken(448), rsWijken(1269), rsWijken(412), rsWijken(1243), rsWijken(408), rsWijken(1229), rsWijken(379),rsWijken(1241), rsWijken(370), rsWijken(1237), rsWijken(355)))
    nrd3 = polygon("nrd3",(120, 50, 120), (
        rsWijken(1237), rsWijken(355), rsWijken(1241), rsWijken(370), rsWijken(1229), rsWijken(379), rsWijken(1243), rsWijken(408), rsWijken(1269), rsWijken(412), rsWijken(1274), rsWijken(404),
        rsWijken(1261), rsWijken(348)))
    nrd4 = polygon("nrd4",(120, 50, 120), (rsWijken(1261), rsWijken(348), rsWijken(1274), rsWijken(404), rsWijken(1311), rsWijken(364), rsWijken(1310), rsWijken(335)))
    nrd5 = polygon("nrd5",(120, 50, 120), (
        rsWijken(1310), rsWijken(335), rsWijken(1311), rsWijken(364), rsWijken(1282), rsWijken(398), rsWijken(1323), rsWijken(423), rsWijken(1311), rsWijken(447), rsWijken(1337), rsWijken(454),
        rsWijken(1331), rsWijken(330)))
    nrd6 = polygon("nrd6",(120, 50, 120),
                   (rsWijken(1282), rsWijken(398), rsWijken(1323), rsWijken(423), rsWijken(1311), rsWijken(447), rsWijken(1295), rsWijken(444), rsWijken(1269), rsWijken(412)))
    nrd7 = polygon("nrd7",(120, 50, 120), (rsWijken(1269), rsWijken(412), rsWijken(1238), rsWijken(449), rsWijken(1288), rsWijken(443), rsWijken(1295), rsWijken(444)))

def delftWijk():
    delf1 = polygon("delf1",(120, 50, 120), (rsWijken(1243), rsWijken(461), rsWijken(1205), rsWijken(460), rsWijken(1221), rsWijken(552), rsWijken(1247), rsWijken(539)))
    delf2 = polygon("delf2",(120, 50, 120),
                    (rsWijken(1205), rsWijken(460), rsWijken(1135), rsWijken(468), rsWijken(1164), rsWijken(506), rsWijken(1186), rsWijken(552), rsWijken(1221), rsWijken(552)))
    delf3 = polygon("delf3",(120, 50, 120),
                    (rsWijken(1135), rsWijken(468), rsWijken(1164), rsWijken(506), rsWijken(1186), rsWijken(552), rsWijken(1107), rsWijken(529), rsWijken(1107), rsWijken(495)))
    delf4 = polygon("delf4",(120, 50, 120),
                    (rsWijken(1135), rsWijken(468), rsWijken(1057), rsWijken(479), rsWijken(1041), rsWijken(522), rsWijken(1107), rsWijken(529), rsWijken(1107), rsWijken(495)))
    delf5 = polygon("delf5",(120, 50, 120), (
        rsWijken(1041), rsWijken(522), rsWijken(1107), rsWijken(529), rsWijken(1124), rsWijken(534), rsWijken(1154), rsWijken(573), rsWijken(1127), rsWijken(598), rsWijken(1113), rsWijken(595),
        rsWijken(1038), rsWijken(610), rsWijken(1048), rsWijken(582), rsWijken(1034), rsWijken(546)))
    delf6 = polygon("delf6",(120, 50, 120), (rsWijken(1124), rsWijken(534), rsWijken(1154), rsWijken(573), rsWijken(1180), rsWijken(592), rsWijken(1186), rsWijken(552)))
    delf7 = polygon("delf7",(120, 50, 120),
                    (rsWijken(1186), rsWijken(552), rsWijken(1221), rsWijken(552), rsWijken(1244), rsWijken(558), rsWijken(1248), rsWijken(572), rsWijken(1180), rsWijken(592)))
    delf8 = polygon("delf8",(120, 50, 120), (
        rsWijken(1154), rsWijken(573), rsWijken(1127),rsWijken(598), rsWijken(1227), rsWijken(620), rsWijken(1262), rsWijken(614), rsWijken(1248), rsWijken(573), rsWijken(1180), rsWijken(592)))

def waalhavenWijk():
    waal1 = polygon("waal1",(120, 50, 120), (
        rsWijken(1048), rsWijken(795), rsWijken(927), rsWijken(797), rsWijken(923), rsWijken(765), rsWijken(934), rsWijken(764), rsWijken(937), rsWijken(743), rsWijken(962), rsWijken(722),
        rsWijken(972), rsWijken(670), rsWijken(921), rsWijken(647), rsWijken(917), rsWijken(663), rsWijken(885), rsWijken(658), rsWijken(862), rsWijken(618), rsWijken(954), rsWijken(639),
        rsWijken(1022), rsWijken(615), rsWijken(1045), rsWijken(673), rsWijken(1062), rsWijken(703), rsWijken(1085), rsWijken(711), rsWijken(1110), rsWijken(762), rsWijken(1095), rsWijken(813)))
    waal2 = polygon("waal2",(120, 50, 120), (
        rsWijken(1045), rsWijken(673), rsWijken(1062), rsWijken(703), rsWijken(1085), rsWijken(711), rsWijken(1088), rsWijken(669), rsWijken(1077), rsWijken(635), rsWijken(1056), rsWijken(641),
        rsWijken(1064), rsWijken(663)))
    waal3 = polygon("waal3",(120, 50, 120), (
        rsWijken(1085), rsWijken(711), rsWijken(1088), rsWijken(669), rsWijken(1077), rsWijken(635), rsWijken(1056), rsWijken(641), rsWijken(1064), rsWijken(663), rsWijken(1045), rsWijken(673),
        rsWijken(1022), rsWijken(615), rsWijken(1038), rsWijken(610), rsWijken(1113), rsWijken(596), rsWijken(1227), rsWijken(620), rsWijken(1225), rsWijken(646), rsWijken(1246), rsWijken(656),
        rsWijken(1199), rsWijken(763), rsWijken(1139), rsWijken(749), rsWijken(1111), rsWijken(760)))
    waal4 = polygon("waal4",(120, 50, 120), (
        rsWijken(1199), rsWijken(763), rsWijken(1139), rsWijken(749), rsWijken(1111), rsWijken(760), rsWijken(1095), rsWijken(813), rsWijken(1161), rsWijken(839), rsWijken(1201), rsWijken(824),
        rsWijken(1218), rsWijken(800), rsWijken(1201), rsWijken(792)))

def charloisWijk():
    char1 = polygon("char1",(120, 50, 120), (
        rsWijken(1262), rsWijken(614), rsWijken(1227), rsWijken(620), rsWijken(1225), rsWijken(646), rsWijken(1246), rsWijken(656), rsWijken(1219), rsWijken(718), rsWijken(1273), rsWijken(729),
        rsWijken(1278), rsWijken(690), rsWijken(1291), rsWijken(668), rsWijken(1257), rsWijken(630), rsWijken(1268), rsWijken(622)))
    char2 = polygon("char2",(120, 50, 120), (
        rsWijken(1268), rsWijken(622), rsWijken(1257), rsWijken(630), rsWijken(1291), rsWijken(668), rsWijken(1339), rsWijken(688), rsWijken(1349), rsWijken(684), rsWijken(1372), rsWijken(694),
        rsWijken(1378), rsWijken(617), rsWijken(1288), rsWijken(642)))
    char3 = polygon("char3",(120, 50, 120), (
        rsWijken(1291), rsWijken(668), rsWijken(1278), rsWijken(690), rsWijken(1274), rsWijken(721), rsWijken(1289), rsWijken(724), rsWijken(1289), rsWijken(714), rsWijken(1333), rsWijken(715),
        rsWijken(1338), rsWijken(724), rsWijken(1361), rsWijken(720), rsWijken(1361), rsWijken(698), rsWijken(1372), rsWijken(694), rsWijken(1349),rsWijken(684), rsWijken(1339), rsWijken(688)))
    char4 = polygon("char4",(120, 50, 120), (
        rsWijken(1219), rsWijken(718), rsWijken(1199), rsWijken(763), rsWijken(1201), rsWijken(792), rsWijken(1218), rsWijken(800), rsWijken(1253), rsWijken(758), rsWijken(1348), rsWijken(772),
        rsWijken(1378), rsWijken(756), rsWijken(1397), rsWijken(819), rsWijken(1457), rsWijken(824), rsWijken(1417), rsWijken(772), rsWijken(1361), rsWijken(720), rsWijken(1338), rsWijken(724),
        rsWijken(1333), rsWijken(715), rsWijken(1289), rsWijken(714), rsWijken(1289), rsWijken(724), rsWijken(1274), rsWijken(721), rsWijken(1273), rsWijken(728)))
    char5 = polygon("char5",(120, 50, 120), (
        rsWijken(1218), rsWijken(800), rsWijken(1253), rsWijken(758), rsWijken(1301), rsWijken(767), rsWijken(1290), rsWijken(824), rsWijken(1239), rsWijken(824), rsWijken(1212), rsWijken(808)))
    char6 = polygon("char6",(120, 50, 120), (
        rsWijken(1301), rsWijken(767), rsWijken(1290), rsWijken(824), rsWijken(1388), rsWijken(820), rsWijken(1397), rsWijken(819), rsWijken(1379), rsWijken(757), rsWijken(1348), rsWijken(772)))
    char7 = polygon("char7",(120, 50, 120), (
        rsWijken(1212), rsWijken(808), rsWijken(1201), rsWijken(824), rsWijken(1161), rsWijken(839), rsWijken(1242), rsWijken(871), rsWijken(1315), rsWijken(869), rsWijken(1315), rsWijken(848),
        rsWijken(1388), rsWijken(820), rsWijken(1239), rsWijken(824)))

def feijenoordWijk():
    fei1 = polygon("fei1",(120, 50, 120),
                   ((1397), rsWijken(500), rsWijken(1375), rsWijken(506), rsWijken(1340), rsWijken(551), rsWijken(1368), rsWijken(558), (1421), rsWijken(510)))
    fei2 = polygon("fei2",(120, 50, 120),
                   (rsWijken(1421), rsWijken(510), rsWijken(1453), rsWijken(522), rsWijken(1469), rsWijken(593), rsWijken(1450), rsWijken(605), rsWijken(1394), rsWijken(532)))
    fei3 = polygon("fei3",(120, 50, 120), (
        rsWijken(1394), rsWijken(532), rsWijken(1450), rsWijken(605), rsWijken(1429), rsWijken(624), rsWijken(1381), rsWijken(583), rsWijken(1387), rsWijken(573), rsWijken(1368), rsWijken(558)))
    fei4 = polygon("fei4",(120, 50, 120), (
        rsWijken(1368), rsWijken(558), rsWijken(1340), rsWijken(551), rsWijken(1322), rsWijken(574), rsWijken(1306), rsWijken(583), rsWijken(1336), rsWijken(600), rsWijken(1378), rsWijken(591),
        rsWijken(1387), rsWijken(573)))
    fei5 = polygon("fei5",(120, 50, 120), (
        rsWijken(1306), rsWijken(583), rsWijken(1336), rsWijken(600), rsWijken(1378), rsWijken(591), rsWijken(1378), rsWijken(617), rsWijken(1288), rsWijken(641), rsWijken(1262), rsWijken(614)))
    fei6 = polygon("fei6",(120, 50, 120), (rsWijken(1378), rsWijken(617), rsWijken(1376), rsWijken(635), rsWijken(1429), rsWijken(624), rsWijken(1382), rsWijken(583)))
    fei7 = polygon("fei7",(120, 50, 120), (
        rsWijken(1428), rsWijken(624), rsWijken(1401), rsWijken(631), rsWijken(1430), rsWijken(664), rsWijken(1423), rsWijken(688), rsWijken(1483), rsWijken(671), rsWijken(1450), rsWijken(605)))
    fei8 = polygon("fei8",(120, 50, 120),
                   (rsWijken(1401), rsWijken(631), rsWijken(1430), rsWijken(664), rsWijken(1423), rsWijken(688), rsWijken(1372), rsWijken(694), rsWijken(1376), rsWijken(636)))
    fei9 = polygon("fei9",(120, 50, 120), (
        rsWijken(1372), rsWijken(694), rsWijken(1361), rsWijken(698), rsWijken(1361), rsWijken(720), rsWijken(1417), rsWijken(772), rsWijken(1454), rsWijken(735), rsWijken(1487), rsWijken(735),
        rsWijken(1496), rsWijken(698), rsWijken(1483), rsWijken(671), rsWijken(1423), rsWijken(688)))

def ijsselmondeWijk():
    ijs1 = polygon("ijs1",(120, 50, 120), (
        rsWijken(1496), rsWijken(698), rsWijken(1487), rsWijken(735), rsWijken(1454), rsWijken(735), rsWijken(1417), rsWijken(772), rsWijken(1457), rsWijken(824), rsWijken(1524), rsWijken(831),
        rsWijken(1553), rsWijken(819)))
    ijs2 = polygon("ijs2",(120, 50, 120), (
        rsWijken(1485), rsWijken(673), rsWijken(1523), rsWijken(652), rsWijken(1619), rsWijken(644), rsWijken(1682), rsWijken(769), rsWijken(1666), rsWijken(779), rsWijken(1657), rsWijken(766),
        rsWijken(1574), rsWijken(813), rsWijken(1553), rsWijken(819)))
    ijs3 = polygon("ijs3",(120, 50, 120), (rsWijken(1619), rsWijken(644), rsWijken(1623), rsWijken(621), rsWijken(1705), rsWijken(639), rsWijken(1682), rsWijken(769)))
    ijs4 = polygon("ijs4",(120, 50, 120), (
        rsWijken(1469), rsWijken(593), rsWijken(1450), rsWijken(605), rsWijken(1485), rsWijken(673), rsWijken(1523), rsWijken(652), rsWijken(1619), rsWijken(644), rsWijken(1623), rsWijken(621),
        rsWijken(1705), rsWijken(639), rsWijken(1712), rsWijken(606), rsWijken(1625), rsWijken(584), rsWijken(1572), rsWijken(594), rsWijken(1489), rsWijken(616)))



''''The polygons(area's)'''''
overschie_polygon = polygon("Overschie",(20, 50, 120), (
rs(904), rs(194), rs(947), rs(183), rs(955), rs(205), rs(1106), rs(109), rs(1176), rs(199), rs(1222), rs(163),
rs(1242), rs(185), rs(1237), rs(355), rs(1109), rs(432), rs(1138), rs(471), rs(1057), rs(479), rs(1017), rs(403),
rs(1059), rs(350), rs(1050), rs(345), rs(1003), rs(366), rs(964), rs(322), rs(949), rs(342)))
hillegersberg_polygon = polygon("Hillegersberg",(20, 50, 120), (
rs(1242), rs(185), rs(1237), rs(355), rs(1520), rs(282), rs(1499), rs(189), rs(1475), rs(213), rs(1432), rs(195),
rs(1428), rs(172), rs(1387), rs(141), rs(1382), rs(154), rs(1280), rs(90)))
prins_alexander_polygon = polygon("Prins_alexander",(20, 50, 120), (
rs(1562), rs(454), rs(1661), rs(425), rs(1651), rs(350), rs(1693), rs(337), rs(1650), rs(227), rs(1663), rs(222),
rs(1673), rs(233), rs(1821), rs(141), rs(1791), rs(116), rs(1815), rs(31), rs(1804), rs(12), rs(1617), rs(76),
rs(1680), rs(145), rs(1627), rs(169), rs(1595), rs(134), rs(1499), rs(189)))
kralingen_polygon = polygon("Kralingen",(20, 50, 120), (
rs(1521), rs(282), rs(1562), rs(454), rs(1538), rs(498), rs(1572), rs(594), rs(1489), rs(616), rs(1469), rs(593),
rs(1453), rs(522), rs(1397), rs(500), rs(1382), rs(461), rs(1337), rs(454), rs(1331), rs(330)))
noord_polygon = polygon("Noord",(20, 50, 120), (
rs(1331), rs(330), rs(1237), rs(355), rs(1109), rs(432), rs(1136), rs(468), rs(1206), rs(462), rs(1208), rs(455),
rs(1288), rs(443), rs(1337), rs(454)))
delftshaven_polygon = polygon("Delftshaven",(20, 50, 120), (
rs(1057), rs(479), rs(1034), rs(546), rs(1048), rs(582), rs(1038), rs(610), rs(1113), rs(596), rs(1227), rs(620),
rs(1262), rs(614), rs(1244), rs(558), rs(1223), rs(553), rs(1247), rs(539), rs(1243), rs(456)))
centrum_polygon = polygon("Centrum",(20, 50, 120), (
rs(1262), rs(614), rs(1244), rs(558), rs(1223), rs(553), rs(1247), rs(539), rs(1243), rs(461), rs(1206), rs(462),
rs(1208), rs(455), rs(1288), rs(443), rs(1337), rs(454), rs(1382), rs(461), rs(1397), rs(500), rs(1375), rs(506),
rs(1322), rs(574)))
feijenoord_polygon = polygon("Feijenoord",(20, 50, 120), (
rs(1397), rs(500), rs(1375), rs(506), rs(1322), rs(574), rs(1262), rs(614), rs(1288), rs(642), rs(1378), rs(617),
rs(1372), rs(694), rs(1361), rs(698), rs(1361), rs(720), rs(1417), rs(772), rs(1454), rs(735), rs(1487), rs(735),
rs(1496), rs(698), rs(1450), rs(605), rs(1469), rs(593), rs(1453), rs(522)))
ijsselmonde_polygon = polygon("Ijsselmonde",(20, 50, 120), (
rs(1572), rs(594), rs(1489), rs(616), rs(1469), rs(593), rs(1450), rs(605), rs(1496), rs(698), rs(1487), rs(735),
rs(1454), rs(735), rs(1417), rs(772), rs(1457), rs(824), rs(1524), rs(831), rs(1574), rs(813), rs(1657), rs(766),
rs(1666), rs(779), rs(1682), rs(769), rs(1712), rs(606), rs(1625), rs(584)))
charlois_polygon = polygon("Charlois",(20, 50, 120), (
rs(1262), rs(614), rs(1288), rs(642), rs(1378), rs(617), rs(1372), rs(694), rs(1361), rs(698), rs(1361), rs(720),
rs(1417), rs(772), rs(1457), rs(824), rs(1388), rs(820), rs(1315), rs(848), rs(1315), rs(869), rs(1242), rs(871),
rs(1161), rs(839), rs(1201), rs(824), rs(1218), rs(800), rs(1201), rs(792), rs(1199), rs(763), rs(1246), rs(656),
rs(1225), rs(646), rs(1227), rs(620)))
waalhaven_polygon = polygon("Waalhaven",(20, 50, 120), (
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
    data = {"Charlois":50, "Overschie":90} #Dictionary to simulate a query, this is to test the query
    for result in data: #goes in the dictionary (the query)
            for gebied in polygonsgebieden: #Goes in the area's array
                if result == "Charlois": #Checks if result from the query is equal to an area
                    result = int(data.get(result)) #Converts the dictionary value to an int
                    charlois_polygon.ChangeColor(100) #Changes color of the area and also change the colour
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

for widget in root.winfo_children():
    print(widget)

root.mainloop() #for the loop