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
    explode = (0, 0, 0, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=False, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title(wijknaam, bbox={'facecolor': '0.8', 'pad': 5})
    plt.show()

pieChart()