import matplotlib.pyplot as plt
import numpy as np
import sqlite3

from sqlite3 import Error


jaarTabelNamen = ["tevredenheid", "fietsendiefstal", "geweldsdelicten","drugsoverlast"]
afkomstTabelNamen = ['Nederlanders', 'Marokkanen', 'Turken', 'Kaapverdianen', 'Antilianen', 'Surinamers', 'Zuid-Europeanen', 'Overig']


class Plot:
    def __init__(self, tabelnaam, wijknamenlist):
        self.databaseFile = "Database\StekOverflow.db"
        self.tabelNaam = tabelnaam
        self.wijkNamenList = wijknamenlist
        self.conn = self.create_connection(self.databaseFile)
        self.cur = self.conn.cursor()

    def create_connection(self,db):
        try:
            conn = sqlite3.connect(db)
            return conn
        except Error as e:
            print(e)
        return None

class PlotLineChart(Plot):
    def __init__(self, tabelnaam, wijknamenlist):
        super().__init__(tabelnaam, wijknamenlist)
        self.y = []
        self.jaartallen = [2006, 2007, 2008, 2009, 2011]
        self.g = globals()

        self.generate_empty_lists()
        self.sql_query_linechart()
        self.show_plot()

    def generate_empty_lists(self):
        for namen in (self.wijkNamenList):
            self.g['data_{}'.format(namen)] = []

    def sql_query_linechart(self):
        for namen in (self.wijkNamenList):
            self.cur.execute("select data2006,data2007,data2008,data2009,data2011 from"
                             " {} where wijknaam = '{}'".format(self.tabelNaam, namen))
            self.wijkData = self.cur.fetchone()
            for i in range(len(self.wijkData)):
                self.g['data_{}'.format(namen)].append(self.wijkData[i])

    def show_plot(self):
        for namen in (self.wijkNamenList):
            plt.plot(self.jaartallen, self.g['data_{}'.format(namen)], label=namen, linewidth=1)
            for a, b in zip(self.jaartallen, self.g['data_{}'.format(namen)]):
                plt.text(a, b, str(b))
        plt.ylabel("Percentage")
        plt.xlabel('Jaren')
        plt.title(self.tabelNaam)
        plt.legend()
        plt.show()


class PlotBarChart(Plot):
    def __init__(self,tabelnaam, dataset, wijknamenlist):
        self.dataSet = dataset
        super().__init__(tabelnaam,wijknamenlist)
        self.data = []
        self.overigeTabelNamen = ["fiobj2016", "fisub2016", "si2016", "vi2016"]
        self.aantalWijken = len(self.wijkNamenList)

        self.sql_query_barchart()
        self.show_plot()

    def sql_query_barchart(self):
        for namen in (self.wijkNamenList):
            self.cur.execute("select {} from {} where wijknaam = '{}'".format(self.dataSet, self.tabelNaam, namen))
            b = self.cur.fetchone()
            self.data.append(b[0])

    def show_plot(self):
        y_pos = np.arange(len(self.wijkNamenList))

        plt.bar(y_pos, self.data, align='center', alpha=0.5)
        for a, b in zip(y_pos, self.data):
            plt.text(a, b, str(b))

        plt.xticks(y_pos, self.wijkNamenList)
        plt.ylabel('Cijfer')
        plt.title(self.dataSet)

        plt.show()




