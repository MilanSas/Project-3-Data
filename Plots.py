import psycopg2 as psy
import matplotlib.pyplot as plt
import numpy as np


con = psy.connect("dbname='StekOverflow' user='postgres' host='localhost' password='pgadmin2017'")

def plotline():
    databasenamen_tijd_list = ["tevredenheid", "fietsendiefstal", "geweldsdelicten","drugsoverlast"]
    x = [2006, 2007, 2008, 2009, 2011]
    y = []

    databasenaam_input = input("Welke database wil je raadplegen? {} ".format(databasenamen_tijd_list))
    wijknaam_input = input("Welke wijk wil je zien? ")
    cur = con.cursor()

    cur.execute("select data2006,data2007,data2008,data2009,data2011 from {} where wijknaam = '{}'".format(databasenaam_input,wijknaam_input))
    wijkdata_1 = cur.fetchone()

    for i in range(len(wijkdata_1)):
            y.append(wijkdata_1[i])


    plt.plot(x, y, label=wijknaam_input, color='lightblue', linewidth=2)
    for a, b in zip(x, y):
        plt.text(a, b, str(b))

    plt.ylabel(databasenaam_input + " %")
    plt.xlabel('Jaren')
    plt.legend()
    plt.show()

plotline()


def plotline_compare():
    x = [2006, 2007, 2008, 2009, 2011]
    y = []
    z = []

    cur = con.cursor()

    databasenaam_input = input("Welke database wil je raadplegen? ")

    wijknaam_input = input("Welke wijk wil je zien? ")
    cur.execute("select data2006,data2007,data2008,data2009,data2011 from {} where wijknaam = '{}'".format(databasenaam_input,wijknaam_input))
    wijkdata_1 = cur.fetchone()

    for i in range(len(wijkdata_1)):

            y.append(wijkdata_1[i])

    wijknaam_input2 = input("Met welke wijk wil je deze vergelijken? ")

    cur.execute("select data2006,data2007,data2008,data2009,data2011 from {} where wijknaam = '{}'".format(databasenaam_input, wijknaam_input2))
    wijkdata_2 = cur.fetchone()


    for j in range(len(wijkdata_2)):
            z.append(wijkdata_2[j])

    plt.plot(x, y, label=wijknaam_input, color='blue', linewidth=2)
    for a, b in zip(x, y):
        plt.text(a, b, str(b))

    plt.plot(x, z, label=wijknaam_input2, color='red', linewidth=2)
    for a, b in zip(x, z):
        plt.text(a, b, str(b))

    plt.ylabel(databasenaam_input)
    plt.xlabel('Tijd')
    plt.legend()
    plt.show()

# plotline_compare()

def pieChart():
    databasenaam_input = input("Welke database wil je raadplegen? ")
    wijknaam_input = input("Welke wijk wil je zien? ")
    cur = con.cursor()
    cur.execute("select * from {} where wijknaam = '{}'".format(databasenaam_input,wijknaam_input))
    wijk_data_1 = cur.fetchone()


    data_ned = wijk_data_1[4]
    data_mar = wijk_data_1[5]
    data_tur = wijk_data_1[6]
    data_kaa = wijk_data_1[7]
    data_ant = wijk_data_1[8]
    data_sur = wijk_data_1[9]
    data_zui = wijk_data_1[10]
    data_ove = wijk_data_1[11]

    labels = 'Nederlanders', 'Marokkanen', 'Turken', 'Kaapverdianen', 'Antilianen', 'Surinamers', 'Zuid-Europeanen', 'Overig'
    sizes = [data_ned, data_mar, data_tur, data_kaa, data_ant, data_sur, data_zui, data_ove]
    explode = (0, 0, 0, 0, 0, 0, 0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=False, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title(wijknaam_input, bbox={'facecolor': '0.8', 'pad': 5})
    plt.show()

# pieChart()


def barChart():
    wijknamen = []
    data = []
    databasenamen_list = ["fiobj2016", "fisub2016", "si2016", "vi2016"]
    databasenaam_input = input("Welke Database wil je raadplegen? {}: ".format(databasenamen_list))
    dataset_input = input("Welke Dataset wil je zien?")
    hoeveel_wijken = int(input("Hoeveel wijken wil je vergelijken? "))

    cur = con.cursor()

    for i in range(hoeveel_wijken):
        wijknaam_input = input("Welke wijken wil je zien? ")
        wijknamen.append(wijknaam_input)
        cur.execute("select {} from {} where wijknaam = '{}'".format(dataset_input, databasenaam_input, wijknaam_input))
        b = cur.fetchone()
        data.append(b[0])

    y_pos = np.arange(len(wijknamen))

    plt.bar(y_pos, data, align='center', alpha=0.5)
    for a, b in zip(y_pos, data):
        plt.text(a, b, str(b))

    plt.xticks(y_pos, wijknamen)
    plt.ylabel('Cijfer')
    plt.title(dataset_input)

    plt.show()

barChart()