import psycopg2 as p
import matplotlib.pyplot as plt

con = p.connect("dbname='StekOverflow' user='postgres' host='localhost' password='pgadmin2017'")

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

plotLine()