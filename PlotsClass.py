import matplotlib.pyplot as plt
import numpy as np
import sqlite3
from sqlite3 import Error


jaartaldata_tabelnamen = ["tevredenheid", "fietsendiefstal", "geweldsdelicten","drugsoverlast"]
afkomstdata_kolomnamen = ['Nederlanders', 'Marokkanen', 'Turken', 'Kaapverdianen', 'Antilianen', 'Surinamers', 'Zuid-Europeanen', 'Overig']
overigedata_tabelnamen = ["fiobj2016", "fisub2016", "si2016", "vi2016"]

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None


class Plot:
    def __init__(self, dbnaam, wknaam):
        self.databasenaam = dbnaam
        self.wijknaam = wknaam
        self.plottitel = self.databasenaam + " in " + self.wijknaam

class PlotLineChart(Plot):
    def show_plot(self):
        database = "Database\StekOverflow.db"
        conn = create_connection(database)
        cur = conn.cursor()
        plt.style.use('ggplot')
        y = []
        jaartaldata_kolomnamen = [2006, 2007, 2008, 2009, 2011]

        cur.execute("select data2006,data2007,data2008,data2009,data2011 from {} where wijknaam = '{}'".format(self.databasenaam, self.wijknaam))
        wijkdata = cur.fetchone()

        for i in range(len(wijkdata)):
            y.append(wijkdata[i])

        plt.plot(jaartaldata_kolomnamen, y, label=self.wijknaam, color='lightblue', linewidth=2)
        for a, b in zip(jaartaldata_kolomnamen, y):
            plt.text(a, b, str(b))

        plt.ylabel(self.databasenaam + " %")
        plt.xlabel('Jaren')
        plt.legend()
        plt.title(self.plottitel, bbox={'facecolor': '0.8', 'pad': 5})
        plt.show()


Lineplot1 = PlotLineChart("tevredenheid","Carnisse")
Lineplot1.show_plot()

