import tkinter as tk
from tkinter import Canvas
import matplotlib
matplotlib.use("TKAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
''''Function to set polygon's(area) size'''

''''Function to create the polygons(area's)'''


''''gets user's screen size (width and height)'''''

class RotterdamMap:
    def __init__(self, canvas, controller):
        self.canvas = canvas
        self.controller = controller
        self.overschie_polygon = polygon((20, 50, 120), (
            self.rs(904), self.rs(194), self.rs(947), self.rs(183), self.rs(955), self.rs(205), self.rs(1106), self.rs(109), self.rs(1176), self.rs(199), self.rs(1222),
            self.rs(163),
            self.rs(1242), self.rs(185), self.rs(1237), self.rs(355), self.rs(1109), self.rs(432), self.rs(1138), self.rs(471), self.rs(1057), self.rs(479), self.rs(1017),
            self.rs(403),
            self.rs(1059), self.rs(350), self.rs(1050), self.rs(345), self.rs(1003), self.rs(366), self.rs(964), self.rs(322), self.rs(949), self.rs(342)),canvas)
        self.hillegersberg_polygon = polygon((20, 50, 120), (
            self.rs(1242), self.rs(185), self.rs(1237), self.rs(355), self.rs(1520), self.rs(282), self.rs(1499), self.rs(189), self.rs(1475), self.rs(213), self.rs(1432),
            self.rs(195),
            self.rs(1428), self.rs(172), self.rs(1387), self.rs(141), self.rs(1382), self.rs(154), self.rs(1280), self.rs(90)),canvas)
        self.prins_alexander_polygon = polygon((20, 50, 120), (
            self.rs(1562), self.rs(454), self.rs(1661), self.rs(425), self.rs(1651), self.rs(350), self.rs(1693), self.rs(337), self.rs(1650), self.rs(227), self.rs(1663),
            self.rs(222),
            self.rs(1673), self.rs(233), self.rs(1821), self.rs(141), self.rs(1791), self.rs(116), self.rs(1815), self.rs(31), self.rs(1804), self.rs(12), self.rs(1617),
            self.rs(76),
            self.rs(1680), self.rs(145), self.rs(1627), self.rs(169), self.rs(1595), self.rs(134), self.rs(1499), self.rs(189)),canvas)
        self.kralingen_polygon = polygon((20, 50, 120), (
            self.rs(1521), self.rs(282), self.rs(1562), self.rs(454), self.rs(1538), self.rs(498), self.rs(1572), self.rs(594), self.rs(1489), self.rs(616), self.rs(1469),
            self.rs(593),
            self.rs(1453), self.rs(522), self.rs(1397), self.rs(500), self.rs(1382), self.rs(461), self.rs(1337), self.rs(454), self.rs(1331), self.rs(330)),canvas)
        self.noord_polygon = polygon((20, 50, 120), (
            self.rs(1331), self.rs(330), self.rs(1237), self.rs(355), self.rs(1109), self.rs(432), self.rs(1136), self.rs(468), self.rs(1206), self.rs(462), self.rs(1208),
            self.rs(455),
            self.rs(1288), self.rs(443), self.rs(1337), self.rs(454)),canvas)
        self.delftshaven_polygon = polygon((20, 50, 120), (
            self.rs(1057), self.rs(479), self.rs(1034), self.rs(546), self.rs(1048), self.rs(582), self.rs(1038), self.rs(610), self.rs(1113), self.rs(596), self.rs(1227),
            self.rs(620),
            self.rs(1262), self.rs(614), self.rs(1244), self.rs(558), self.rs(1223), self.rs(553), self.rs(1247), self.rs(539), self.rs(1243), self.rs(456)),canvas)
        self.centrum_polygon = polygon((20, 50, 120), (
            self.rs(1262), self.rs(614), self.rs(1244), self.rs(558), self.rs(1223), self.rs(553), self.rs(1247), self.rs(539), self.rs(1243), self.rs(461), self.rs(1206),
            self.rs(462),
            self.rs(1208), self.rs(455), self.rs(1288), self.rs(443), self.rs(1337), self.rs(454), self.rs(1382), self.rs(461), self.rs(1397), self.rs(500), self.rs(1375),
            self.rs(506),
            self.rs(1322), self.rs(574)),canvas)
        self.feijenoord_polygon = polygon((20, 50, 120), (
            self.rs(1397), self.rs(500), self.rs(1375), self.rs(506), self.rs(1322), self.rs(574), self.rs(1262), self.rs(614), self.rs(1288), self.rs(642), self.rs(1378),
            self.rs(617),
            self.rs(1372), self.rs(694), self.rs(1361), self.rs(698), self.rs(1361), self.rs(720), self.rs(1417), self.rs(772), self.rs(1454), self.rs(735), self.rs(1487),
            self.rs(735),
            self.rs(1496), self.rs(698), self.rs(1450), self.rs(605), self.rs(1469), self.rs(593), self.rs(1453), self.rs(522)),canvas)
        self.ijsselmonde_polygon = polygon((20, 50, 120), (
            self.rs(1572), self.rs(594), self.rs(1489), self.rs(616), self.rs(1469), self.rs(593), self.rs(1450), self.rs(605), self.rs(1496), self.rs(698), self.rs(1487),
            self.rs(735),
            self.rs(1454), self.rs(735), self.rs(1417), self.rs(772), self.rs(1457), self.rs(824), self.rs(1524), self.rs(831), self.rs(1574), self.rs(813), self.rs(1657),
            self.rs(766),
            self.rs(1666), self.rs(779), self.rs(1682), self.rs(769), self.rs(1712), self.rs(606), self.rs(1625), self.rs(584)), canvas)
        self.charlois_polygon = polygon((20, 50, 120), (
            self.rs(1262), self.rs(614), self.rs(1288), self.rs(642), self.rs(1378), self.rs(617), self.rs(1372), self.rs(694), self.rs(1361), self.rs(698), self.rs(1361),
            self.rs(720),
            self.rs(1417), self.rs(772), self.rs(1457), self.rs(824), self.rs(1388), self.rs(820), self.rs(1315), self.rs(848), self.rs(1315), self.rs(869), self.rs(1242),
            self.rs(871),
            self.rs(1161), self.rs(839), self.rs(1201), self.rs(824), self.rs(1218), self.rs(800), self.rs(1201), self.rs(792), self.rs(1199), self.rs(763), self.rs(1246),
            self.rs(656),
            self.rs(1225), self.rs(646), self.rs(1227), self.rs(620)),canvas)
        self.waalhaven_polygon = polygon((20, 50, 120), (
            self.rs(1161), self.rs(839), self.rs(1201), self.rs(824), self.rs(1218), self.rs(800), self.rs(1201), self.rs(792), self.rs(1199), self.rs(763), self.rs(1246),
            self.rs(656),
            self.rs(1225), self.rs(646), self.rs(1227), self.rs(620), self.rs(1113), self.rs(596), self.rs(1038), self.rs(610), self.rs(954), self.rs(639), self.rs(862),
            self.rs(618),
            self.rs(885), self.rs(658), self.rs(917), self.rs(663), self.rs(921), self.rs(647), self.rs(972), self.rs(670), self.rs(962), self.rs(722), self.rs(937), self.rs(743),
            self.rs(934),
            self.rs(764), self.rs(923), self.rs(765), self.rs(927), self.rs(797), self.rs(1048), self.rs(795)),canvas)

        self.polygonsgebieden = [self.overschie_polygon, self.hillegersberg_polygon, self.prins_alexander_polygon, self.kralingen_polygon,
                            self.noord_polygon, self.delftshaven_polygon, self.centrum_polygon, self.feijenoord_polygon,
                            self.ijsselmonde_polygon, self.charlois_polygon, self.waalhaven_polygon]

    def rs(self, size):
        ratio = (self.controller.winfo_screenheight()+ self.controller.winfo_screenheight()/ 2) / size
        return (self.controller.winfo_screenheight() / ratio)


class polygon():
    def __init__(self,color,list, canvas):
        self.color = color
        self.shape = canvas.create_polygon(list, fill=self.HexToRGB(self.color), outline='black', width = 2)


    def HexToRGB(self, rgb):
        # RGB WAARDES MOETEN TUSSEN 16 - 255
        result = (
            '#' + str(hex(rgb[0]).split('x')[-1]) + str(hex(rgb[1]).split('x')[-1]) + str(hex(rgb[2]).split('x')[-1]))
        return result

LARGE_FONT = ("Verdana", 12)

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Page1, Page2):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()




class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        canvas = Canvas(parent, width = controller.winfo_screenwidth()-150, height =controller.winfo_screenheight())
        rotterdam = RotterdamMap(canvas, controller)
        canvas.grid(row=0, column=1)

        button = tk.Button(self, text="Visit Page 1",
                           command=lambda: controller.show_frame(Page1))
        button.pack()

        button2 = tk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(Page2))
        button2.pack()


class Page1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(Page2))
        button2.pack()


class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(Page1))
        button2.pack()

root = App()
root.mainloop() #for the loop