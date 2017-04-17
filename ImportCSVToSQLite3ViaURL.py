import pandas as pd
from sqlalchemy import create_engine

class import_data:
    def __init__(self):
        self.engine = create_engine('sqlite:///Database\StekOverflow.db')

        self.geweldsdelicten_data = pd.read_csv('https://raw.githubusercontent.com/MilanSas/Project-3-Data/master/Data/Geweldsdelicten2006-2011.csv', sep=';')
        self.fietsendiefstal_data = pd.read_csv('https://raw.githubusercontent.com/MilanSas/Project-3-Data/master/Data/Fietsendiefstal2006-2011.csv', sep=';')
        self.drugsoverlast_data = pd.read_csv('https://raw.githubusercontent.com/MilanSas/Project-3-Data/master/Data/Geweldsdelicten2006-2011.csv', sep=';')
        self.tevredenheid_data = pd.read_csv('https://raw.githubusercontent.com/MilanSas/Project-3-Data/master/Data/Tevredenheid2006-2011.csv', sep=';')
        self.afkomst_data = pd.read_csv('https://raw.githubusercontent.com/MilanSas/Project-3-Data/master/Data/Afkomst.csv', sep=';')
        self.vi2016_data = pd.read_csv('https://raw.githubusercontent.com/MilanSas/Project-3-Data/master/Data/VI2016.csv', sep=';', encoding='latin-1')
        self.si2016_data = pd.read_csv('https://raw.githubusercontent.com/MilanSas/Project-3-Data/master/Data/SI2016.csv', sep=';', encoding='latin-1')
        self.fisub2016_data = pd.read_csv('https://raw.githubusercontent.com/MilanSas/Project-3-Data/master/Data/FIsub2016.csv', sep=';', encoding='latin-1')
        self.fiobj2016_data = pd.read_csv('https://raw.githubusercontent.com/MilanSas/Project-3-Data/master/Data/FIobj2016.csv', sep=';', encoding='latin-1')

        self.lower_columns()
        self.create_database()

    def lower_columns(self):
        self.geweldsdelicten_data.columns = [c.lower() for c in self.geweldsdelicten_data.columns] # sql haat hoofdletters
        self.fietsendiefstal_data.columns = [c.lower() for c in self.fietsendiefstal_data.columns]
        self.drugsoverlast_data.columns = [c.lower() for c in self.drugsoverlast_data.columns]
        self.tevredenheid_data.columns = [c.lower() for c in self.tevredenheid_data.columns]
        self.afkomst_data.columns = [c.lower() for c in self.afkomst_data.columns]
        self.vi2016_data.columns = [c.lower() for c in self.vi2016_data.columns]
        self.si2016_data.columns = [c.lower() for c in self.si2016_data.columns]
        self.fisub2016_data.columns = [c.lower() for c in self.fisub2016_data.columns]
        self.fiobj2016_data.columns = [c.lower() for c in self.fiobj2016_data.columns]

    def create_database(self):
        self.geweldsdelicten_data.to_sql("geweldsdelicten", self.engine)
        self.fietsendiefstal_data.to_sql("fietsendiefstal", self.engine)
        self.drugsoverlast_data.to_sql("drugsoverlast", self.engine)
        self.tevredenheid_data.to_sql("tevredenheid", self.engine)
        self.afkomst_data.to_sql("afkomst", self.engine)
        self.vi2016_data.to_sql("vi2016", self.engine)
        self.si2016_data.to_sql("si2016", self.engine)
        self.fisub2016_data.to_sql("fisub2016", self.engine)
        self.fiobj2016_data.to_sql("fiobj2016", self.engine)

import_data()

