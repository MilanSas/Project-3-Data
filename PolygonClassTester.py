from tkinter import *
tk = Tk()
tk.resizable(width=False, height=False)
width = tk.winfo_screenwidth()
height = tk.winfo_screenheight()
canvas = Canvas(tk, width=width, height=height)

def rs(size):
    ratio = 1080 / size
    return height / ratio

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


#alle coördinaten hieronder moeten nog in rs() worden gewikkeld om mee te schalen op resolutie. het werkt nu alleen voor 1080p schermen
ov1 = polygon((120,50,120),(949,342,964,322,1003,366,1050,345,1035,295,939,304))
ov2 = polygon((120,50,120),(1050,345,1059,350,1052,359,1073,389,1128,354,1101,310,1076,269,1035,295))
ov3 = polygon((120,50,120),(1052,359,1017,403,1057,479,1136,468))
ov4 = polygon((120,50,120),(1109,432,1173,392,1128,354,1073,389))
ov5 = polygon((120,50,120),(904,194,947,183,955,205,1106,109,1176,199,1222,163,1242,185,1237,355,1173,392,1128,354,1072,269,1035,295,939,304))

hill1 = polygon((120,50,120),(1242,185,1239,309,1288,310,1363,143,1280,90))
hill2 = polygon((120,50,120),(1239,306,1237,355,1356,322,1337,300,1328,312,1298,286,1288,310))
hill3 = polygon((120,50,120),(1298,286,1328,312,1337,300,1356,322,1430,282,1375,226,1383,154,1363,143))
hill4 = polygon((120,50,120),(1382,165,1375,226,1430,282,1475,213,1432,195,1428,172,1387,141))
hill5 = polygon((120,50,120),(1356,322,1520,282,1499,189,1475,213,1432,195))

pa1 = polygon((120,50,120),(1499,189,1523,292,1602,269,1650,227,1627,169,1595,134))
pa2 = polygon((120,50,120),(1523,292,1543,370,1622,351,1602,269))
pa3 = polygon((120,50,120),(1543,370,1562,454,1661,425,1654,384,1637,389,1622,351))
pa4 = polygon((120,50,120),(1622,351,1637,389,1654,384,1651,350,1693,337,1650,227,1602,269))
pa5 = polygon((120,50,120),(1650,227,1663,222,1673,233,1742,188,1725,163,1719,119,1680,145,1627,169))
pa6 = polygon((120,50,120),(1680,145,1719,119,1725,163,1742,188,1821,141,1791,116,1815,31,1804,12,1617,76))

kra6 = polygon((120,50,120),(1521,282,1464,296,1380,356,1407,396,1446,417,1447,448,1434,481,1468,515,1542,512,1538,498,1562,454))
kra1 = polygon((120,50,120),(1464,296,1380,356,1393,375,1377,395,1334,379,1331,330))
kra2 = polygon((120,50,120),(1393,375,1377,395,1334,379,1335,419,1384,420,1407,396))
kra3 = polygon((120,50,120),(1335,419,1337,454,1382,461,1384,420))
kra4 = polygon((120,50,120),(1382,461,1384,420,1407,396,1446,417,1447,448,1434,481))
kra5 = polygon((120,50,120),(1382,462,1434,481,1469,515,1453,522,1397,500))
kra7 = polygon((120,50,120),(1453,522,1469,515,1542,514,1572,594,1489,616,1469,593))

changecolor(charlois, 100)
changecolor(ijsselmonde, 34)
changecolor(centrum, 78)
changecolor(prins_alexander, 9)
changecolor(feijenoord, 51)

canvas.grid()
tk.mainloop()