from tkinter import *
root = Tk()
screeny = root.winfo_screenheight() #height

def rs(size):
    ratio = 1080 / size
    return (screeny / ratio)
def rsWijken(size):
    ratio = 1080 / size
    return (screeny / ratio)

overschie = (
rs(904), rs(194), rs(947), rs(183), rs(955), rs(205), rs(1106), rs(109), rs(1176), rs(199), rs(1222), rs(163),
rs(1242), rs(185), rs(1237), rs(355), rs(1109), rs(432), rs(1138), rs(471), rs(1057), rs(479), rs(1017), rs(403),
rs(1059), rs(350), rs(1050), rs(345), rs(1003), rs(366), rs(964), rs(322), rs(949), rs(342))

hillegersberg = (
rs(1242), rs(185), rs(1237), rs(355), rs(1520), rs(282), rs(1499), rs(189), rs(1475), rs(213), rs(1432), rs(195),
rs(1428), rs(172), rs(1387), rs(141), rs(1382), rs(154), rs(1280), rs(90))

prins_alexander= (
rs(1562), rs(454), rs(1661), rs(425), rs(1651), rs(350), rs(1693), rs(337), rs(1650), rs(227), rs(1663), rs(222),
rs(1673), rs(233), rs(1821), rs(141), rs(1791), rs(116), rs(1815), rs(31), rs(1804), rs(12), rs(1617), rs(76),
rs(1680), rs(145), rs(1627), rs(169), rs(1595), rs(134), rs(1499), rs(189))

kralingen = (
rs(1521), rs(282), rs(1562), rs(454), rs(1538), rs(498), rs(1572), rs(594), rs(1489), rs(616), rs(1469), rs(593),
rs(1453), rs(522), rs(1397), rs(500), rs(1382), rs(461), rs(1337), rs(454), rs(1331), rs(330))


noord = (
rs(1331), rs(330), rs(1237), rs(355), rs(1109), rs(432), rs(1136), rs(468), rs(1206), rs(462), rs(1208), rs(455),
rs(1288), rs(443), rs(1337), rs(454))

delftshaven = (
rs(1057), rs(479), rs(1034), rs(546), rs(1048), rs(582), rs(1038), rs(610), rs(1113), rs(596), rs(1227), rs(620),
rs(1262), rs(614), rs(1244), rs(558), rs(1223), rs(553), rs(1247), rs(539), rs(1243), rs(456))

centrum = (
rs(1262), rs(614), rs(1244), rs(558), rs(1223), rs(553), rs(1247), rs(539), rs(1243), rs(461), rs(1206), rs(462),
rs(1208), rs(455), rs(1288), rs(443), rs(1337), rs(454), rs(1382), rs(461), rs(1397), rs(500), rs(1375), rs(506),
rs(1322), rs(574))

feijenoord = (
rs(1397), rs(500), rs(1375), rs(506), rs(1322), rs(574), rs(1262), rs(614), rs(1288), rs(642), rs(1378), rs(617),
rs(1372), rs(694), rs(1361), rs(698), rs(1361), rs(720), rs(1417), rs(772), rs(1454), rs(735), rs(1487), rs(735),
rs(1496), rs(698), rs(1450), rs(605), rs(1469), rs(593), rs(1453), rs(522))

ijsselmonde = (
rs(1572), rs(594), rs(1489), rs(616), rs(1469), rs(593), rs(1450), rs(605), rs(1496), rs(698), rs(1487), rs(735),
rs(1454), rs(735), rs(1417), rs(772), rs(1457), rs(824), rs(1524), rs(831), rs(1574), rs(813), rs(1657), rs(766),
rs(1666), rs(779), rs(1682), rs(769), rs(1712), rs(606), rs(1625), rs(584))

charlois = (
rs(1262), rs(614), rs(1288), rs(642), rs(1378), rs(617), rs(1372), rs(694), rs(1361), rs(698), rs(1361), rs(720),
rs(1417), rs(772), rs(1457), rs(824), rs(1388), rs(820), rs(1315), rs(848), rs(1315), rs(869), rs(1242), rs(871),
rs(1161), rs(839), rs(1201), rs(824), rs(1218), rs(800), rs(1201), rs(792), rs(1199), rs(763), rs(1246), rs(656),
rs(1225), rs(646), rs(1227), rs(620))

waalhaven = (
rs(1161), rs(839), rs(1201), rs(824), rs(1218), rs(800), rs(1201), rs(792), rs(1199), rs(763), rs(1246), rs(656),
rs(1225), rs(646), rs(1227), rs(620), rs(1113), rs(596), rs(1038), rs(610), rs(954), rs(639), rs(862), rs(618),
rs(885), rs(658), rs(917), rs(663), rs(921), rs(647), rs(972), rs(670), rs(962), rs(722), rs(937), rs(743), rs(934),
rs(764), rs(923), rs(765), rs(927), rs(797), rs(1048), rs(795))

ov1 = (
    rsWijken(949), rsWijken(342), rsWijken(964), rsWijken(322), rsWijken(1003), rsWijken(366), rsWijken(1050), rsWijken(345), rsWijken(1035), rsWijken(295), rsWijken(939), rsWijken(304))
ov2 = (
    rsWijken(1050), rsWijken(345), rsWijken(1059), rsWijken(350), rsWijken(1052), rsWijken(359), rsWijken(1073), rsWijken(389), rsWijken(1128), rsWijken(354), rsWijken(1101), rsWijken(310),
    rsWijken(1076), rsWijken(269), rsWijken(1035), rsWijken(295))
ov3 = (rsWijken(1052), rsWijken(359), rsWijken(1017), rsWijken(403), rsWijken(1057), rsWijken(479), rsWijken(1136), rsWijken(468))
ov4 = (rsWijken(1109), rsWijken(432), rsWijken(1173), rsWijken(392), rsWijken(1128), rsWijken(354), rsWijken(1073), rsWijken(389))
ov5 = (
    rsWijken(904), rsWijken(194), rsWijken(947), rsWijken(183), rsWijken(955), rsWijken(205), rsWijken(1106), rsWijken(109), rsWijken(1176), rsWijken(199), rsWijken(1222), rsWijken(163),
    rsWijken(1242), rsWijken(185), rsWijken(1237), rsWijken(355), rsWijken(1173), rsWijken(392), rsWijken(1128), rsWijken(354), rsWijken(1072), rsWijken(269), rsWijken(1035), rsWijken(295),
    rsWijken(939), rsWijken(304))

hill1 = (rsWijken(1242), rsWijken(185), rsWijken(1239), rsWijken(309), rsWijken(1288), rsWijken(310), rsWijken(1363), rsWijken(143), rsWijken(1280), rsWijken(90))
hill2 = (rsWijken(1239), rsWijken(306), rsWijken(1237), rsWijken(355), rsWijken(1356), rsWijken(322), rsWijken(1337), rsWijken(300), rsWijken(1328), rsWijken(312), rsWijken(1298), rsWijken(286),
    rsWijken(1288), rsWijken(310))
hill3 = (
    rsWijken(1298), rsWijken(286), rsWijken(1328), rsWijken(312), rsWijken(1337), rsWijken(300), rsWijken(1356), rsWijken(322), rsWijken(1430), rsWijken(282), rsWijken(1375), rsWijken(226),
    rsWijken(1383), rsWijken(154), rsWijken(1363), rsWijken(143))
hill4 = (
    rsWijken(1382), rsWijken(165), rsWijken(1375), rsWijken(226), rsWijken(1430), rsWijken(282), rsWijken(1475), rsWijken(213), rsWijken(1432), rsWijken(195), rsWijken(1428), rsWijken(172),
    rsWijken(1387), rsWijken(141))
hill5 = (rsWijken(1356), rsWijken(322), rsWijken(1520), rsWijken(282), rsWijken(1499), rsWijken(189), rsWijken(1475), rsWijken(213), rsWijken(1432), rsWijken(195))


pa1 = (
    rsWijken(1499), rsWijken(189), rsWijken(1523), rsWijken(292), rsWijken(1602), rsWijken(269), rsWijken(1650), rsWijken(227), rsWijken(1627), rsWijken(169), rsWijken(1595), rsWijken(134))
pa2 = (rsWijken(1523), rsWijken(292), rsWijken(1543), rsWijken(370), rsWijken(1622), rsWijken(351), rsWijken(1602), rsWijken(269))
pa3 = (
    rsWijken(1543), rsWijken(370), rsWijken(1562), rsWijken(454),rsWijken(1661), rsWijken(425), rsWijken(1654), rsWijken(384), rsWijken(1637), rsWijken(389), rsWijken(1622), rsWijken(351))
pa4 = (
    rsWijken(1622), rsWijken(351), rsWijken(1637), rsWijken(389), rsWijken(1654), rsWijken(384), rsWijken(1651), rsWijken(350), rsWijken(1693), rsWijken(337), rsWijken(1650), rsWijken(227),
    rsWijken(1602), rsWijken(269))
pa5 =  (
    rsWijken(1650), rsWijken(227), rsWijken(1663), rsWijken(222), rsWijken(1673), rsWijken(233), rsWijken(1742), rsWijken(188), rsWijken(1725), rsWijken(163), rsWijken(1719), rsWijken(119),
    rsWijken(1680), rsWijken(145), rsWijken(1627), rsWijken(169))
pa6 =  (
    rsWijken(1680), rsWijken(145), rsWijken(1719), rsWijken(119), rsWijken(1725), rsWijken(163), rsWijken(1742), rsWijken(188), rsWijken(1821), rsWijken(141), rsWijken(1791), rsWijken(116),
    rsWijken(1815), rsWijken(31), rsWijken(1804), rsWijken(12), rsWijken(1617), rsWijken(76))


kra6 = (
    rsWijken(1521), rsWijken(282), rsWijken(1464), rsWijken(296), rsWijken(1380), rsWijken(356), rsWijken(1407), rsWijken(396), rsWijken(1446), rsWijken(417), rsWijken(1447), rsWijken(448),
    rsWijken(1434), rsWijken(481), rsWijken(1468), rsWijken(515), rsWijken(1542), rsWijken(512), rsWijken(1538), rsWijken(498), rsWijken(1562), rsWijken(454))
kra1 = (
    rsWijken(1464), rsWijken(296), rsWijken(1380), rsWijken(356), rsWijken(1393), rsWijken(375), rsWijken(1377), rsWijken(395), rsWijken(1334), rsWijken(379), rsWijken(1331), rsWijken(330))
kra2 = (
    rsWijken(1393), rsWijken(375), rsWijken(1377), rsWijken(395), rsWijken(1334), rsWijken(379), rsWijken(1335), rsWijken(419), rsWijken(1384), rsWijken(420), rsWijken(1407), rsWijken(396))
kra3 = (rsWijken(1335), rsWijken(419), rsWijken(1337), rsWijken(454), rsWijken(1382),rsWijken(461), rsWijken(1384), rsWijken(420))
kra4 = (
    rsWijken(1382), rsWijken(461), rsWijken(1384), rsWijken(420), rsWijken(1407), rsWijken(396), rsWijken(1446), rsWijken(417), rsWijken(1447), rsWijken(448), rsWijken(1434), rsWijken(481))
kra5 = (rsWijken(1382), rsWijken(462), rsWijken(1434), rsWijken(481), rsWijken(1469), rsWijken(515), rsWijken(1453), rsWijken(522), rsWijken(1397), rsWijken(500))
kra7 = (
    rsWijken(1453), rsWijken(522), rsWijken(1469), rsWijken(515), rsWijken(1542), rsWijken(514), rsWijken(1572), rsWijken(594), rsWijken(1489), rsWijken(616), rsWijken(1469), rsWijken(593))


centr1 = (
(1243), rsWijken(461), rsWijken(1206), rsWijken(462), rsWijken(1208), rsWijken(455), rsWijken(1288), rsWijken(443), rsWijken(1299), rsWijken(445), rsWijken(1299), rsWijken(458),
rsWijken(1272), rsWijken(468), rsWijken(1243), rsWijken(470))
centr2 = (rsWijken(1243), rsWijken(470), rsWijken(1272), rsWijken(468), rsWijken(1281), rsWijken(511), rsWijken(1247), rsWijken(539))
centr3 = (
    rsWijken(1247), rsWijken(539), rsWijken(1223), rsWijken(553), rsWijken(1244), rsWijken(558), rsWijken(1245), rsWijken(562), rsWijken(1298), rsWijken(541), rsWijken(1281), rsWijken(511))
centr4 = (
    rsWijken(1299), rsWijken(458), rsWijken(1272), rsWijken(468), rsWijken(1281), rsWijken(511), rsWijken(1298), rsWijken(541), rsWijken(1309), rsWijken(537), rsWijken(1316), rsWijken(501))
centr5 = (
    rsWijken(1299), rsWijken(445), rsWijken(1337), rsWijken(454), rsWijken(1382), rsWijken(461), rsWijken(1397), rsWijken(500), rsWijken(1375), rsWijken(506), rsWijken(1330), rsWijken(563),
    rsWijken(1314), rsWijken(547), rsWijken(1300), rsWijken(547), rsWijken(1298), rsWijken(541), rsWijken(1309), rsWijken(537), rsWijken(1316), rsWijken(501), rsWijken(1299), rsWijken(458),
    rsWijken(1299), rsWijken(445))
centr6 = (
    rsWijken(1245), rsWijken(562), rsWijken(1298), rsWijken(541), rsWijken(1300), rsWijken(547), rsWijken(1314), rsWijken(547), rsWijken(1330), rsWijken(563), rsWijken(1322), rsWijken(574),
    rsWijken(1262), rsWijken(614))


nrd1 = (
    rsWijken(1109), rsWijken(432), rsWijken(1136), rsWijken(468), rsWijken(1168), rsWijken(464), rsWijken(1181), rsWijken(452), rsWijken(1190), rsWijken(395), rsWijken(1173), rsWijken(394))
nrd2 = (
    rsWijken(1173), rsWijken(394), rsWijken(1190), rsWijken(395), rsWijken(1181), rsWijken(452), rsWijken(1168), rsWijken(464), rsWijken(1206), rsWijken(462), rsWijken(1208), rsWijken(455),
    rsWijken(1240), rsWijken(448), rsWijken(1269), rsWijken(412), rsWijken(1243), rsWijken(408), rsWijken(1229), rsWijken(379),rsWijken(1241), rsWijken(370), rsWijken(1237), rsWijken(355))
nrd3 = (
    rsWijken(1237), rsWijken(355), rsWijken(1241), rsWijken(370), rsWijken(1229), rsWijken(379), rsWijken(1243), rsWijken(408), rsWijken(1269), rsWijken(412), rsWijken(1274), rsWijken(404),
    rsWijken(1261), rsWijken(348))
nrd4 = (rsWijken(1261), rsWijken(348), rsWijken(1274), rsWijken(404), rsWijken(1311), rsWijken(364), rsWijken(1310), rsWijken(335))
nrd5 = (
    rsWijken(1310), rsWijken(335), rsWijken(1311), rsWijken(364), rsWijken(1282), rsWijken(398), rsWijken(1323), rsWijken(423), rsWijken(1311), rsWijken(447), rsWijken(1337), rsWijken(454),
    rsWijken(1331), rsWijken(330))
nrd6 = (rsWijken(1282), rsWijken(398), rsWijken(1323), rsWijken(423), rsWijken(1311), rsWijken(447), rsWijken(1295), rsWijken(444), rsWijken(1269), rsWijken(412))
nrd7 = (rsWijken(1269), rsWijken(412), rsWijken(1238), rsWijken(449), rsWijken(1288), rsWijken(443), rsWijken(1295), rsWijken(444))


delf1 = (rsWijken(1243), rsWijken(461), rsWijken(1205), rsWijken(460), rsWijken(1221), rsWijken(552), rsWijken(1247), rsWijken(539))
delf2 = (rsWijken(1205), rsWijken(460), rsWijken(1135), rsWijken(468), rsWijken(1164), rsWijken(506), rsWijken(1186), rsWijken(552), rsWijken(1221), rsWijken(552))
delf3 = (rsWijken(1135), rsWijken(468), rsWijken(1164), rsWijken(506), rsWijken(1186), rsWijken(552), rsWijken(1107), rsWijken(529), rsWijken(1107), rsWijken(495))
delf4 = (rsWijken(1135), rsWijken(468), rsWijken(1057), rsWijken(479), rsWijken(1041), rsWijken(522), rsWijken(1107), rsWijken(529), rsWijken(1107), rsWijken(495))
delf5 = (
    rsWijken(1041), rsWijken(522), rsWijken(1107), rsWijken(529), rsWijken(1124), rsWijken(534), rsWijken(1154), rsWijken(573), rsWijken(1127), rsWijken(598), rsWijken(1113), rsWijken(595),
    rsWijken(1038), rsWijken(610), rsWijken(1048), rsWijken(582), rsWijken(1034), rsWijken(546))
delf6 = (rsWijken(1124), rsWijken(534), rsWijken(1154), rsWijken(573), rsWijken(1180), rsWijken(592), rsWijken(1186), rsWijken(552))
delf7 = (rsWijken(1186), rsWijken(552), rsWijken(1221), rsWijken(552), rsWijken(1244), rsWijken(558), rsWijken(1248), rsWijken(572), rsWijken(1180), rsWijken(592))
delf8 = (
    rsWijken(1154), rsWijken(573), rsWijken(1127),rsWijken(598), rsWijken(1227), rsWijken(620), rsWijken(1262), rsWijken(614), rsWijken(1248), rsWijken(573), rsWijken(1180), rsWijken(592))


waal1 = (
    rsWijken(1048), rsWijken(795), rsWijken(927), rsWijken(797), rsWijken(923), rsWijken(765), rsWijken(934), rsWijken(764), rsWijken(937), rsWijken(743), rsWijken(962), rsWijken(722),
    rsWijken(972), rsWijken(670), rsWijken(921), rsWijken(647), rsWijken(917), rsWijken(663), rsWijken(885), rsWijken(658), rsWijken(862), rsWijken(618), rsWijken(954), rsWijken(639),
    rsWijken(1022), rsWijken(615), rsWijken(1045), rsWijken(673), rsWijken(1062), rsWijken(703), rsWijken(1085), rsWijken(711), rsWijken(1110), rsWijken(762), rsWijken(1095), rsWijken(813))
waal2 = (
    rsWijken(1045), rsWijken(673), rsWijken(1062), rsWijken(703), rsWijken(1085), rsWijken(711), rsWijken(1088), rsWijken(669), rsWijken(1077), rsWijken(635), rsWijken(1056), rsWijken(641),
    rsWijken(1064), rsWijken(663))
waal3 = (
    rsWijken(1085), rsWijken(711), rsWijken(1088), rsWijken(669), rsWijken(1077), rsWijken(635), rsWijken(1056), rsWijken(641), rsWijken(1064), rsWijken(663), rsWijken(1045), rsWijken(673),
    rsWijken(1022), rsWijken(615), rsWijken(1038), rsWijken(610), rsWijken(1113), rsWijken(596), rsWijken(1227), rsWijken(620), rsWijken(1225), rsWijken(646), rsWijken(1246), rsWijken(656),
    rsWijken(1199), rsWijken(763), rsWijken(1139), rsWijken(749), rsWijken(1111), rsWijken(760))
waal4 = (
    rsWijken(1199), rsWijken(763), rsWijken(1139), rsWijken(749), rsWijken(1111), rsWijken(760), rsWijken(1095), rsWijken(813), rsWijken(1161), rsWijken(839), rsWijken(1201), rsWijken(824),
    rsWijken(1218), rsWijken(800), rsWijken(1201), rsWijken(792))


char1 = (
    rsWijken(1262), rsWijken(614), rsWijken(1227), rsWijken(620), rsWijken(1225), rsWijken(646), rsWijken(1246), rsWijken(656), rsWijken(1219), rsWijken(718), rsWijken(1273), rsWijken(729),
    rsWijken(1278), rsWijken(690), rsWijken(1291), rsWijken(668), rsWijken(1257), rsWijken(630), rsWijken(1268), rsWijken(622))
char2 = (
    rsWijken(1268), rsWijken(622), rsWijken(1257), rsWijken(630), rsWijken(1291), rsWijken(668), rsWijken(1339), rsWijken(688), rsWijken(1349), rsWijken(684), rsWijken(1372), rsWijken(694),
    rsWijken(1378), rsWijken(617), rsWijken(1288), rsWijken(642))
char3 = (
    rsWijken(1291), rsWijken(668), rsWijken(1278), rsWijken(690), rsWijken(1274), rsWijken(721), rsWijken(1289), rsWijken(724), rsWijken(1289), rsWijken(714), rsWijken(1333), rsWijken(715),
    rsWijken(1338), rsWijken(724), rsWijken(1361), rsWijken(720), rsWijken(1361), rsWijken(698), rsWijken(1372), rsWijken(694), rsWijken(1349),rsWijken(684), rsWijken(1339), rsWijken(688))
char4 = (
    rsWijken(1219), rsWijken(718), rsWijken(1199), rsWijken(763), rsWijken(1201), rsWijken(792), rsWijken(1218), rsWijken(800), rsWijken(1253), rsWijken(758), rsWijken(1348), rsWijken(772),
    rsWijken(1378), rsWijken(756), rsWijken(1397), rsWijken(819), rsWijken(1457), rsWijken(824), rsWijken(1417), rsWijken(772), rsWijken(1361), rsWijken(720), rsWijken(1338), rsWijken(724),
    rsWijken(1333), rsWijken(715), rsWijken(1289), rsWijken(714), rsWijken(1289), rsWijken(724), rsWijken(1274), rsWijken(721), rsWijken(1273), rsWijken(728))
char5 = (
    rsWijken(1218), rsWijken(800), rsWijken(1253), rsWijken(758), rsWijken(1301), rsWijken(767), rsWijken(1290), rsWijken(824), rsWijken(1239), rsWijken(824), rsWijken(1212), rsWijken(808))
char6 = (
    rsWijken(1301), rsWijken(767), rsWijken(1290), rsWijken(824), rsWijken(1388), rsWijken(820), rsWijken(1397), rsWijken(819), rsWijken(1379), rsWijken(757), rsWijken(1348), rsWijken(772))
char7 = (
    rsWijken(1212), rsWijken(808), rsWijken(1201), rsWijken(824), rsWijken(1161), rsWijken(839), rsWijken(1242), rsWijken(871), rsWijken(1315), rsWijken(869), rsWijken(1315), rsWijken(848),
    rsWijken(1388), rsWijken(820), rsWijken(1239), rsWijken(824))


fei1 = ((1397), rsWijken(500), rsWijken(1375), rsWijken(506), rsWijken(1340), rsWijken(551), rsWijken(1368), rsWijken(558), (1421), rsWijken(510))
fei2 = (rsWijken(1421), rsWijken(510), rsWijken(1453), rsWijken(522), rsWijken(1469), rsWijken(593), rsWijken(1450), rsWijken(605), rsWijken(1394), rsWijken(532))
fei3 = (
    rsWijken(1394), rsWijken(532), rsWijken(1450), rsWijken(605), rsWijken(1429), rsWijken(624), rsWijken(1381), rsWijken(583), rsWijken(1387), rsWijken(573), rsWijken(1368), rsWijken(558))
fei4 = (
    rsWijken(1368), rsWijken(558), rsWijken(1340), rsWijken(551), rsWijken(1322), rsWijken(574), rsWijken(1306), rsWijken(583), rsWijken(1336), rsWijken(600), rsWijken(1378), rsWijken(591),
    rsWijken(1387), rsWijken(573))
fei5 = (rsWijken(1306), rsWijken(583), rsWijken(1336), rsWijken(600), rsWijken(1378), rsWijken(591), rsWijken(1378), rsWijken(617), rsWijken(1288), rsWijken(641), rsWijken(1262), rsWijken(614))
fei6 = (rsWijken(1378), rsWijken(617), rsWijken(1376), rsWijken(635), rsWijken(1429), rsWijken(624), rsWijken(1382), rsWijken(583))
fei7 = (rsWijken(1428), rsWijken(624), rsWijken(1401), rsWijken(631), rsWijken(1430), rsWijken(664), rsWijken(1423), rsWijken(688), rsWijken(1483), rsWijken(671), rsWijken(1450), rsWijken(605))
fei8 = (rsWijken(1401), rsWijken(631), rsWijken(1430), rsWijken(664), rsWijken(1423), rsWijken(688), rsWijken(1372), rsWijken(694), rsWijken(1376), rsWijken(636))
fei9 = (
    rsWijken(1372), rsWijken(694), rsWijken(1361), rsWijken(698), rsWijken(1361), rsWijken(720), rsWijken(1417), rsWijken(772), rsWijken(1454), rsWijken(735), rsWijken(1487), rsWijken(735),
    rsWijken(1496), rsWijken(698), rsWijken(1483), rsWijken(671), rsWijken(1423), rsWijken(688))


ijs1 = (
    rsWijken(1496), rsWijken(698), rsWijken(1487), rsWijken(735), rsWijken(1454), rsWijken(735), rsWijken(1417), rsWijken(772), rsWijken(1457), rsWijken(824), rsWijken(1524), rsWijken(831),
    rsWijken(1553), rsWijken(819))
ijs2 = (
    rsWijken(1485), rsWijken(673), rsWijken(1523), rsWijken(652), rsWijken(1619), rsWijken(644), rsWijken(1682), rsWijken(769), rsWijken(1666), rsWijken(779), rsWijken(1657), rsWijken(766),
    rsWijken(1574), rsWijken(813), rsWijken(1553), rsWijken(819))
ijs3 = (rsWijken(1619), rsWijken(644), rsWijken(1623), rsWijken(621), rsWijken(1705), rsWijken(639), rsWijken(1682), rsWijken(769))
ijs4 = (
    rsWijken(1469), rsWijken(593), rsWijken(1450), rsWijken(605), rsWijken(1485), rsWijken(673), rsWijken(1523), rsWijken(652), rsWijken(1619), rsWijken(644), rsWijken(1623), rsWijken(621),
    rsWijken(1705), rsWijken(639), rsWijken(1712), rsWijken(606), rsWijken(1625), rsWijken(584), rsWijken(1572), rsWijken(594), rsWijken(1489), rsWijken(616))
