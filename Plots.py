import psycopg2 as p
import matplotlib.pyplot as plt

con = p.connect("dbname='StekOverflow' user='postgres' host='localhost' password='pgadmin2017'")


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


def plotLine():
    databaseNaam = input("Welke database wil je raadplegen? ")
    wijkNaam = input("Welke wijk wil je zien? ")
    cur = con.cursor()
    cur.execute("select * from {} where wijknaam = '{}'".format(databaseNaam,wijkNaam))
    wijkData_1 = cur.fetchone()

    wijknaam = wijkData_1[1]
    data2006 = wijkData_1[2]
    data2007 = wijkData_1[3]
    data2008 = wijkData_1[4]
    data2009 = wijkData_1[5]
    data2011 = wijkData_1[6]

    x = [2006, 2007, 2008, 2009, 2011]
    y = [data2006, data2007, data2008, data2009, data2011]

    plt.plot(x, y, label=wijkNaam, color='lightblue', linewidth=2)
    for a, b in zip(x, y):
        plt.text(a, b, str(b))

    plt.ylabel(databaseNaam)
    plt.xlabel('Tijd')
    plt.legend()
    plt.show()

# plotLine()



def plotLine_compare():
    databaseNaam = input("Welke database wil je raadplegen? ")
    wijkNaam_1 = input("Welke wijk wil je zien? ")

    cur = con.cursor()
    cur.execute("select * from {} where wijknaam = '{}'".format(databaseNaam,wijkNaam_1))
    wijkData_1 = cur.fetchone()

    wijkNaam_1 = wijkData_1[1]
    data2006_1 = wijkData_1[2]
    data2007_1 = wijkData_1[3]
    data2008_1 = wijkData_1[4]
    data2009_1 = wijkData_1[5]
    data2011_1 = wijkData_1[6]

    wijkNaam_2 = input("Met welke wijk wil je deze vergelijken? ")
    cur.execute("select * from {} where wijknaam = '{}'".format(databaseNaam, wijkNaam_2))
    wijkData_2 = cur.fetchone()

    wijkNaam_2 = wijkData_2[1]
    data2006_2 = wijkData_2[2]
    data2007_2 = wijkData_2[3]
    data2008_2 = wijkData_2[4]
    data2009_2 = wijkData_2[5]
    data2011_2 = wijkData_2[6]

    x = [2006, 2007, 2008, 2009, 2011]
    y = [data2006_1, data2007_1, data2008_1, data2009_1, data2011_1]
    z = [data2006_2, data2007_2, data2008_2, data2009_2, data2011_2]

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