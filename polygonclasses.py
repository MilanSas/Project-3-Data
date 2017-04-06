from tkinter import *
tk = Tk()
tk.resizable(width=False, height=False)
width = tk.winfo_screenwidth()
height = tk.winfo_screenheight()
canvas = Canvas(tk, width=width, height=height)

def rs(size):
    ratio = 1080 / size
    return height / ratio

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

overschie = polygon((20,50,120),(rs(904),rs(194),rs(947),rs(183),rs(955),rs(205),rs(1106),rs(109),rs(1176),rs(199),rs(1222),rs(163),rs(1242),rs(185),rs(1237),rs(355),rs(1109),rs(432),rs(1138),rs(471),rs(1057),rs(479),rs(1017),rs(403),rs(1059),rs(350),rs(1050),rs(345),rs(1003),rs(366),rs(964),rs(322),rs(949),rs(342)))
hillegersberg = polygon((20,50,120),(rs(1242),rs(185),rs(1237),rs(355),rs(1520),rs(282),rs(1499),rs(189),rs(1475),rs(213),rs(1432),rs(195),rs(1428),rs(172),rs(1387),rs(141),rs(1382),rs(154),rs(1280),rs(90)))
prins_alexander = polygon((20,50,120),(rs(1562),rs(454),rs(1661),rs(425),rs(1651),rs(350),rs(1693),rs(337),rs(1650),rs(227),rs(1663),rs(222),rs(1673),rs(233),rs(1821),rs(141),rs(1791),rs(116),rs(1815),rs(31),rs(1804),rs(12),rs(1617),rs(76),rs(1680),rs(145),rs(1627),rs(169),rs(1595),rs(134),rs(1499),rs(189)))
kralingen = polygon((20,50,120),(rs(1521),rs(282),rs(1562),rs(454),rs(1538),rs(498),rs(1572),rs(594),rs(1489),rs(616),rs(1469),rs(593),rs(1453),rs(522),rs(1397),rs(500),rs(1382),rs(461),rs(1337),rs(454),rs(1331),rs(330)))
noord = polygon((20,50,120),(rs(1331),rs(330),rs(1237),rs(355),rs(1109),rs(432),rs(1136),rs(468),rs(1206),rs(462),rs(1208),rs(455),rs(1288),rs(443),rs(1337),rs(454)))
delftshaven = polygon((20,50,120),(rs(1057),rs(479),rs(1034),rs(546),rs(1048),rs(582),rs(1038),rs(610),rs(1113),rs(596),rs(1227),rs(620),rs(1262),rs(614),rs(1244),rs(558),rs(1223),rs(553),rs(1247),rs(539),rs(1243),rs(456)))
centrum = polygon((20,50,120),(rs(1262),rs(614),rs(1244),rs(558),rs(1223),rs(553),rs(1247),rs(539),rs(1243),rs(461),rs(1206),rs(462),rs(1208),rs(455),rs(1288),rs(443),rs(1337),rs(454),rs(1382),rs(461),rs(1397),rs(500),rs(1375),rs(506),rs(1322),rs(574)))
feijenoord = polygon((20,50,120),(rs(1397),rs(500),rs(1375),rs(506),rs(1322),rs(574),rs(1262),rs(614),rs(1288),rs(642),rs(1378),rs(617),rs(1372),rs(694),rs(1361),rs(698),rs(1361),rs(720),rs(1417),rs(772),rs(1454),rs(735),rs(1487),rs(735),rs(1496),rs(698),rs(1450),rs(605),rs(1469),rs(593),rs(1453),rs(522)))
ijsselmonde = polygon((20,50,120),(rs(1572),rs(594),rs(1489),rs(616),rs(1469),rs(593),rs(1450),rs(605),rs(1496),rs(698),rs(1487),rs(735),rs(1454),rs(735),rs(1417),rs(772),rs(1457),rs(824),rs(1524),rs(831),rs(1574),rs(813),rs(1657),rs(766),rs(1666),rs(779),rs(1682),rs(769),rs(1712),rs(606),rs(1625),rs(584)))
charlois = polygon((20,50,120),(rs(1262),rs(614),rs(1288),rs(642),rs(1378),rs(617),rs(1372),rs(694),rs(1361),rs(698),rs(1361),rs(720),rs(1417),rs(772),rs(1457),rs(824),rs(1388),rs(820),rs(1315),rs(848),rs(1315),rs(869),rs(1242),rs(871),rs(1161),rs(839),rs(1201),rs(824),rs(1218),rs(800),rs(1201),rs(792),rs(1199),rs(763),rs(1246),rs(656),rs(1225),rs(646),rs(1227),rs(620)))
waalhaven = polygon((20,50,120),(rs(1161),rs(839),rs(1201),rs(824),rs(1218),rs(800),rs(1201),rs(792),rs(1199),rs(763),rs(1246),rs(656),rs(1225),rs(646),rs(1227),rs(620),rs(1113),rs(596),rs(1038),rs(610),rs(954),rs(639),rs(862),rs(618),rs(885),rs(658),rs(917),rs(663),rs(921),rs(647),rs(972),rs(670),rs(962),rs(722),rs(937),rs(743),rs(934),rs(764),rs(923),rs(765),rs(927),rs(797),rs(1048),rs(795)))


canvas.grid()
tk.mainloop()