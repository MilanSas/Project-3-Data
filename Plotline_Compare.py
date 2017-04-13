import psycopg2 as p
import matplotlib.pyplot as plt

con = p.connect("dbname='StekOverflow' user='postgres' host='localhost' password='pgadmin2017'")

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