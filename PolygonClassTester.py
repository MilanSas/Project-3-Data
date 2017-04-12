from tkinter import *
import random
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

list = [overschie,hillegersberg,prins_alexander,kralingen,noord,delftshaven,centrum,feijenoord,ijsselmonde,charlois,waalhaven]

#alle coördinaten hieronder moeten nog in rs() worden gewikkeld om mee te schalen op resolutie. het werkt nu alleen voor 1080p schermen
ov1 = polygon((120,50,120),(rs(949),rs(342),rs(964),rs(322),rs(1003),rs(366),rs(1050),rs(345),rs(1035),rs(295),rs(939),rs(304)))
ov2 = polygon((120,50,120),(rs(1050),rs(345),rs(1059),rs(350),rs(1052),rs(359),rs(1073),rs(389),rs(1128),rs(354),rs(1101),rs(310),rs(1076),rs(269),rs(1035),rs(295)))
ov3 = polygon((120,50,120),(rs(1052),rs(359),rs(1017),rs(403),rs(1057),rs(479),rs(1136),rs(468)))
ov4 = polygon((120,50,120),(rs(1109),rs(432),rs(1173),rs(392),rs(1128),rs(354),rs(1073),rs(389)))
ov5 = polygon((120,50,120),(rs(904),rs(194),rs(947),rs(183),rs(955),rs(205),rs(1106),rs(109),rs(1176),rs(199),rs(1222),rs(163),rs(1242),rs(185),rs(1237),rs(355),rs(1173),rs(392),rs(1128),rs(354),rs(1072),rs(269),rs(1035),rs(295),rs(939),rs(304)))

hill1 = polygon((120,50,120),(rs(1242),rs(185),rs(1239),rs(309),rs(1288),rs(310),rs(1363),rs(143),rs(1280),rs(90)))
hill2 = polygon((120,50,120),(rs(1239),rs(306),rs(1237),rs(355),rs(1356),rs(322),rs(1337),rs(300),rs(1328),rs(312),rs(1298),rs(286),rs(1288),rs(310)))
hill3 = polygon((120,50,120),(rs(1298),rs(286),rs(1328),rs(312),rs(1337),rs(300),rs(1356),rs(322),rs(1430),rs(282),rs(1375),rs(226),rs(1383),rs(154),rs(1363),rs(143)))
hill4 = polygon((120,50,120),(rs(1382),rs(165),rs(1375),rs(226),rs(1430),rs(282),rs(1475),rs(213),rs(1432),rs(195),rs(1428),rs(172),rs(1387),rs(141)))
hill5 = polygon((120,50,120),(rs(1356),rs(322),rs(1520),rs(282),rs(1499),rs(189),rs(1475),rs(213),rs(1432),rs(195)))

pa1 = polygon((120,50,120),(rs(1499),rs(189),rs(1523),rs(292),rs(1602),rs(269),rs(1650),rs(227),rs(1627),rs(169),rs(1595),rs(134)))
pa2 = polygon((120,50,120),(rs(1523),rs(292),rs(1543),rs(370),rs(1622),rs(351),rs(1602),rs(269)))
pa3 = polygon((120,50,120),(rs(1543),rs(370),rs(1562),rs(454),rs(1661),rs(425),rs(1654),rs(384),rs(1637),rs(389),rs(1622),rs(351)))
pa4 = polygon((120,50,120),(rs(1622),rs(351),rs(1637),rs(389),rs(1654),rs(384),rs(1651),rs(350),rs(1693),rs(337),rs(1650),rs(227),rs(1602),rs(269)))
pa5 = polygon((120,50,120),(rs(1650),rs(227),rs(1663),rs(222),rs(1673),rs(233),rs(1742),rs(188),rs(1725),rs(163),rs(1719),rs(119),rs(1680),rs(145),rs(1627),rs(169)))
pa6 = polygon((120,50,120),(rs(1680),rs(145),rs(1719),rs(119),rs(1725),rs(163),rs(1742),rs(188),rs(1821),rs(141),rs(1791),rs(116),rs(1815),rs(31),rs(1804),rs(12),rs(1617),rs(76)))

kra6 = polygon((120,50,120),(rs(1521),rs(282),rs(1464),rs(296),rs(1380),rs(356),rs(1407),rs(396),rs(1446),rs(417),rs(1447),rs(448),rs(1434),rs(481),rs(1468),rs(515),rs(1542),rs(512),rs(1538),rs(498),rs(1562),rs(454)))
kra1 = polygon((120,50,120),(rs(1464),rs(296),rs(1380),rs(356),rs(1393),rs(375),rs(1377),rs(395),rs(1334),rs(379),rs(1331),rs(330)))
kra2 = polygon((120,50,120),(rs(1393),rs(375),rs(1377),rs(395),rs(1334),rs(379),rs(1335),rs(419),rs(1384),rs(420),rs(1407),rs(396)))
kra3 = polygon((120,50,120),(rs(1335),rs(419),rs(1337),rs(454),rs(1382),rs(461),rs(1384),rs(420)))
kra4 = polygon((120,50,120),(rs(1382),rs(461),rs(1384),rs(420),rs(1407),rs(396),rs(1446),rs(417),rs(1447),rs(448),rs(1434),rs(481)))
kra5 = polygon((120,50,120),(rs(1382),rs(462),rs(1434),rs(481),rs(1469),rs(515),rs(1453),rs(522),rs(1397),rs(500)))
kra7 = polygon((120,50,120),(rs(1453),rs(522),rs(1469),rs(515),rs(1542),rs(514),rs(1572),rs(594),rs(1489),rs(616),rs(1469),rs(593)))

centr1 = polygon((120,50,120),(rs(1243),rs(461),rs(1206),rs(462),rs(1208),rs(455),rs(1288),rs(443),rs(1299),rs(445),rs(1299),rs(458),rs(1272),rs(468),rs(1243),rs(470)))
centr2 = polygon((120,50,120),(rs(1243),rs(470),rs(1272),rs(468),rs(1281),rs(511),rs(1247),rs(539)))
centr3 = polygon((120,50,120),(rs(1247),rs(539),rs(1223),rs(553),rs(1244),rs(558),rs(1245),rs(562),rs(1298),rs(541),rs(1281),rs(511)))
centr4 = polygon((120,50,120),(rs(1299),rs(458),rs(1272),rs(468),rs(1281),rs(511),rs(1298),rs(541),rs(1309),rs(537),rs(1316),rs(501)))
centr5 = polygon((120,50,120),(rs(1299),rs(445),rs(1337),rs(454),rs(1382),rs(461),rs(1397),rs(500),rs(1375),rs(506),rs(1330),rs(563),rs(1314),rs(547),rs(1300),rs(547),rs(1298),rs(541),rs(1309),rs(537),rs(1316),rs(501),rs(1299),rs(458),rs(1299),rs(445)))
centr6 = polygon((120,50,120),(rs(1245),rs(562),rs(1298),rs(541),rs(1300),rs(547),rs(1314),rs(547),rs(1330),rs(563),rs(1322),rs(574),rs(1262),rs(614)))

nrd1 = polygon((120,50,120),(rs(1109),rs(432),rs(1136),rs(468),rs(1168),rs(464),rs(1181),rs(452),rs(1190),rs(395),rs(1173),rs(394)))
nrd2 = polygon((120,50,120),(rs(1173),rs(394),rs(1190),rs(395),rs(1181),rs(452),rs(1168),rs(464),rs(1206),rs(462),rs(1208),rs(455),rs(1240),rs(448),rs(1269),rs(412),rs(1243),rs(408),rs(1229),rs(379),rs(1241),rs(370),rs(1237),rs(355)))
nrd3 = polygon((120,50,120),(rs(1237),rs(355),rs(1241),rs(370),rs(1229),rs(379),rs(1243),rs(408),rs(1269),rs(412),rs(1274),rs(404),rs(1261),rs(348)))
nrd4 = polygon((120,50,120),(rs(1261),rs(348),rs(1274),rs(404),rs(1311),rs(364),rs(1310),rs(335)))
nrd5 = polygon((120,50,120),(rs(1310),rs(335),rs(1311),rs(364),rs(1282),rs(398),rs(1323),rs(423),rs(1311),rs(447),rs(1337),rs(454),rs(1331),rs(330)))
nrd6 = polygon((120,50,120),(rs(1282),rs(398),rs(1323),rs(423),rs(1311),rs(447),rs(1295),rs(444),rs(1269),rs(412)))
nrd7 = polygon((120,50,120),(rs(1269),rs(412),rs(1238),rs(449),rs(1288),rs(443),rs(1295),rs(444)))

delf1 = polygon((120,50,120),(rs(1243),rs(461),rs(1205),rs(460),rs(1221),rs(552),rs(1247),rs(539)))
delf2 = polygon((120,50,120),(rs(1205),rs(460),rs(1135),rs(468),rs(1164),rs(506),rs(1186),rs(552),rs(1221),rs(552)))
delf3 = polygon((120,50,120),(rs(1135),rs(468),rs(1164),rs(506),rs(1186),rs(552),rs(1107),rs(529),rs(1107),rs(495)))
delf4 = polygon((120,50,120),(rs(1135),rs(468),rs(1057),rs(479),rs(1041),rs(522),rs(1107),rs(529),rs(1107),rs(495)))
delf5 = polygon((120,50,120),(rs(1041),rs(522),rs(1107),rs(529),rs(1124),rs(534),rs(1154),rs(573),rs(1127),rs(598),rs(1113),rs(595),rs(1038),rs(610),rs(1048),rs(582),rs(1034),rs(546)))
delf6 = polygon((120,50,120),(rs(1124),rs(534),rs(1154),rs(573),rs(1180),rs(592),rs(1186),rs(552)))
delf7 = polygon((120,50,120),(rs(1186),rs(552),rs(1221),rs(552),rs(1244),rs(558),rs(1248),rs(572),rs(1180),rs(592)))
delf8 = polygon((120,50,120),(rs(1154),rs(573),rs(1127),rs(598),rs(1227),rs(620),rs(1262),rs(614),rs(1248),rs(573),rs(1180),rs(592)))

waal1 = polygon((120,50,120),(rs(1048),rs(795),rs(927),rs(797),rs(923),rs(765),rs(934),rs(764),rs(937),rs(743),rs(962),rs(722),rs(972),rs(670),rs(921),rs(647),rs(917),rs(663),rs(885),rs(658),rs(862),rs(618),rs(954),rs(639),rs(1022),rs(615),rs(1045),rs(673),rs(1062),rs(703),rs(1085),rs(711),rs(1110),rs(762),rs(1095),rs(813)))
waal2 = polygon((120,50,120),(rs(1045),rs(673),rs(1062),rs(703),rs(1085),rs(711),rs(1088),rs(669),rs(1077),rs(635),rs(1056),rs(641),rs(1064),rs(663)))
waal3 = polygon((120,50,120),(rs(1085),rs(711),rs(1088),rs(669),rs(1077),rs(635),rs(1056),rs(641),rs(1064),rs(663),rs(1045),rs(673),rs(1022),rs(615),rs(1038),rs(610),rs(1113),rs(596),rs(1227),rs(620),rs(1225),rs(646),rs(1246),rs(656),rs(1199),rs(763),rs(1139),rs(749),rs(1111),rs(760)))
waal4 = polygon((120,50,120),(rs(1199),rs(763),rs(1139),rs(749),rs(1111),rs(760),rs(1095),rs(813),rs(1161),rs(839),rs(1201),rs(824),rs(1218),rs(800),rs(1201),rs(792)))

char1 = polygon((120,50,120),(rs(1262),rs(614),rs(1227),rs(620),rs(1225),rs(646),rs(1246),rs(656),rs(1219),rs(718),rs(1273),rs(729),rs(1278),rs(690),rs(1291),rs(668),rs(1257),rs(630),rs(1268),rs(622)))
char2 = polygon((120,50,120),(rs(1268),rs(622),rs(1257),rs(630),rs(1291),rs(668),rs(1339),rs(688),rs(1349),rs(684),rs(1372),rs(694),rs(1378),rs(617),rs(1288),rs(642)))
char3 = polygon((120,50,120),(rs(1291),rs(668),rs(1278),rs(690),rs(1274),rs(721),rs(1289),rs(724),rs(1289),rs(714),rs(1333),rs(715),rs(1338),rs(724),rs(1361),rs(720),rs(1361),rs(698),rs(1372),rs(694),rs(1349),rs(684),rs(1339),rs(688)))
char4 = polygon((120,50,120),(rs(1219),rs(718),rs(1199),rs(763),rs(1201),rs(792),rs(1218),rs(800),rs(1253),rs(758),rs(1348),rs(772),rs(1378),rs(756),rs(1397),rs(819),rs(1457),rs(824),rs(1417),rs(772),rs(1361),rs(720),rs(1338),rs(724),rs(1333),rs(715),rs(1289),rs(714),rs(1289),rs(724),rs(1274),rs(721),rs(1273),rs(728)))
char5 = polygon((120,50,120),(rs(1218),rs(800),rs(1253),rs(758),rs(1301),rs(767),rs(1290),rs(824),rs(1239),rs(824),rs(1212),rs(808)))
char6 = polygon((120,50,120),(rs(1301),rs(767),rs(1290),rs(824),rs(1388),rs(820),rs(1397),rs(819),rs(1379),rs(757),rs(1348),rs(772)))
char7 = polygon((120,50,120),(rs(1212),rs(808),rs(1201),rs(824),rs(1161),rs(839),rs(1242),rs(871),rs(1315),rs(869),rs(1315),rs(848),rs(1388),rs(820),rs(1239),rs(824)))

fei1 = polygon((120,50,120),(rs(1397),rs(500),rs(1375),rs(506),rs(1340),rs(551),rs(1368),rs(558),rs(1421),rs(510)))
fei2 = polygon((120,50,120),(rs(1421),rs(510),rs(1453),rs(522),rs(1469),rs(593),rs(1450),rs(605),rs(1394),rs(532)))
fei3 = polygon((120,50,120),(rs(1394),rs(532),rs(1450),rs(605),rs(1429),rs(624),rs(1381),rs(583),rs(1387),rs(573),rs(1368),rs(558)))
fei4 = polygon((120,50,120),(rs(1368),rs(558),rs(1340),rs(551),rs(1322),rs(574),rs(1306),rs(583),rs(1336),rs(600),rs(1378),rs(591),rs(1387),rs(573)))
fei5 = polygon((120,50,120),(rs(1306),rs(583),rs(1336),rs(600),rs(1378),rs(591),rs(1378),rs(617),rs(1288),rs(641),rs(1262),rs(614)))
fei6 = polygon((120,50,120),(rs(1378),rs(617),rs(1376),rs(635),rs(1429),rs(624),rs(1382),rs(583)))
fei7 = polygon((120,50,120),(rs(1428),rs(624),rs(1401),rs(631),rs(1430),rs(664),rs(1423),rs(688),rs(1483),rs(671),rs(1450),rs(605)))
fei8 = polygon((120,50,120),(rs(1401),rs(631),rs(1430),rs(664),rs(1423),rs(688),rs(1372),rs(694),rs(1376),rs(636)))
fei9 = polygon((120,50,120),(rs(1372),rs(694),rs(1361),rs(698),rs(1361),rs(720),rs(1417),rs(772),rs(1454),rs(735),rs(1487),rs(735),rs(1496),rs(698),rs(1483),rs(671),rs(1423),rs(688)))

ijs1 = polygon((120,50,120),(rs(1496),rs(698),rs(1487),rs(735),rs(1454),rs(735),rs(1417),rs(772),rs(1457),rs(824),rs(1524),rs(831),rs(1553),rs(819)))
ijs2 = polygon((120,50,120),(rs(1485),rs(673),rs(1523),rs(652),rs(1619),rs(644),rs(1682),rs(769),rs(1666),rs(779),rs(1657),rs(766),rs(1574),rs(813),rs(1553),rs(819)))
ijs3 = polygon((120,50,120),(rs(1619),rs(644),rs(1623),rs(621),rs(1705),rs(639),rs(1682),rs(769)))
ijs4 = polygon((120,50,120),(rs(1469),rs(593),rs(1450),rs(605),rs(1485),rs(673),rs(1523),rs(652),rs(1619),rs(644),rs(1623),rs(621),rs(1705),rs(639),rs(1712),rs(606),rs(1625),rs(584),rs(1572),rs(594),rs(1489),rs(616)))

for i in list:
    changecolor(i,random.randint(0,100))

canvas.grid()
tk.mainloop()