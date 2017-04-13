import matplotlib.pyplot as plt
import numpy as np
import sqlite3
from sqlite3 import Error


jaartaldata_tabelnamen = ["tevredenheid", "fietsendiefstal", "geweldsdelicten","drugsoverlast"]
afkomstdata_kolomnamen = ['Nederlanders', 'Marokkanen', 'Turken', 'Kaapverdianen', 'Antilianen', 'Surinamers', 'Zuid-Europeanen', 'Overig']
overigedata_tabelnamen = ["fiobj2016", "fisub2016", "si2016", "vi2016"]

class Plot:
    def __init__(self, dbnaam, wknaam):
        self.database_file = "Database\StekOverflow.db"
        self.databasenaam = dbnaam
        self.wijknaam = wknaam
        self.plottitel = self.databasenaam + " in " + self.wijknaam
        self.conn = self.create_connection(self.database_file)
        self.cur = self.conn.cursor()

    def create_connection(self,db):
        try:
            conn = sqlite3.connect(db)
            return conn
        except Error as e:
            print(e)
        return None

class PlotLineChart(Plot):
    y = []
    jaartallen = [2006, 2007, 2008, 2009, 2011]

    def sql_query(self):
        self.cur.execute("select data2006,data2007,data2008,data2009,data2011 from {} where wijknaam = '{}'".format(self.databasenaam, self.wijknaam))
        self.wijkdata = self.cur.fetchone()

        for i in range(len(self.wijkdata)):
            self.y.append(self.wijkdata[i])

    def show_plot(self):
        self.sql_query()
        plt.plot(self.jaartallen, self.y, label=self.wijknaam, color='lightblue', linewidth=2)
        for a, b in zip(self.jaartallen, self.y):
            plt.text(a, b, str(b))

        plt.ylabel(self.databasenaam + " %")
        plt.xlabel('Jaren')
        plt.legend()
        plt.title(self.plottitel, bbox={'facecolor': '0.8', 'pad': 5})
        plt.show()


Lineplot1 = PlotLineChart("tevredenheid","Carnisse")
Lineplot1.show_plot()

