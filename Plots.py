import psycopg2 as p
import matplotlib.pyplot as plt

con = p.connect("dbname='StekOverflow' user='postgres' host='localhost' password='pgadmin2017'")

def plotLine():
    y = []

    databaseNaam = input("Welke database wil je raadplegen? ")
    wijkNaam = input("Welke wijk wil je zien? ")
    cur = con.cursor()
    cur.execute("select data2006,data2007,data2008,data2009,data2011 from {} where wijknaam = '{}'".format(databaseNaam,wijkNaam))
    wijkData_1 = cur.fetchone()

    for i in range(len(wijkData_1)):
            y.append(wijkData_1[i])

    x = [2006, 2007, 2008, 2009, 2011]


    plt.plot(x, y, label=wijkNaam, color='lightblue', linewidth=2)
    for a, b in zip(x, y):
        plt.text(a, b, str(b))

    plt.ylabel(databaseNaam)
    plt.xlabel('Tijd')
    plt.legend()
    plt.show()

# plotLine()


def plotLine_compare():
    x = [2006, 2007, 2008, 2009, 2011]
    y = []
    z = []
    databaseNaam = input("Welke database wil je raadplegen? ")
    wijkNaam_1 = input("Welke wijk wil je zien? ")

    cur = con.cursor()
    cur.execute("select data2006,data2007,data2008,data2009,data2011 from {} where wijknaam = '{}'".format(databaseNaam,wijkNaam_1))
    wijkData_1 = cur.fetchone()

    for i in range(len(wijkData_1)):

            y.append(wijkData_1[i])

    wijkNaam_2 = input("Met welke wijk wil je deze vergelijken? ")
    cur.execute("select data2006,data2007,data2008,data2009,data2011 from {} where wijknaam = '{}'".format(databaseNaam, wijkNaam_2))
    wijkData_2 = cur.fetchone()


    for j in range(len(wijkData_2)):
            z.append(wijkData_2[j])

    plt.plot(x, y, label=wijkNaam_1, color='blue', linewidth=2)
    for a, b in zip(x, y):
        plt.text(a, b, str(b))

    plt.plot(x, z, label=wijkNaam_2, color='red', linewidth=2)
    for a, b in zip(x, z):
        plt.text(a, b, str(b))

    plt.ylabel(databaseNaam)
    plt.xlabel('Tijd')
    plt.legend()
    plt.show()

plotLine_compare()

def pieChart():
    databaseNaam = input("Welke database wil je raadplegen? ")
    wijkNaam = input("Welke wijk wil je zien? ")
    cur = con.cursor()
    cur.execute("select * from {} where wijknaam = '{}'".format(databaseNaam,wijkNaam))
    wijkData_1 = cur.fetchone()

    wijknaam = wijkData_1[1]
    data_Ned = wijkData_1[4]
    data_Mar = wijkData_1[5]
    data_Tur = wijkData_1[6]
    data_Kaa = wijkData_1[7]
    data_Ant = wijkData_1[8]
    data_Sur = wijkData_1[9]
    data_Zui = wijkData_1[10]
    data_Ove = wijkData_1[11]

    labels = 'Nederlanders', 'Marokkanen', 'Turken', 'Kaapverdianen', 'Antilianen', 'Surinamers', 'Zuid-Europeanen', 'Overig'
    sizes = [data_Ned, data_Mar, data_Tur, data_Kaa, data_Ant, data_Sur, data_Zui, data_Ove]
    explode = (0, 0, 0, 0, 0, 0, 0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=False, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title(wijknaam, bbox={'facecolor': '0.8', 'pad': 5})
    plt.show()

# pieChart()