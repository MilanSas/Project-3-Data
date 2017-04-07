import pandas as pd
import psycopg2 as p

con = p.connect("dbname='StekOverflow' user='postgres' host='localhost' password='pgadmin2017'")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS geweldsdelicten")
cur.execute("DROP TABLE IF EXISTS fietsendiefstal")
cur.execute("DROP TABLE IF EXISTS drugsoverlast")
cur.execute("DROP TABLE IF EXISTS tevredenheid")
cur.execute("DROP TABLE IF EXISTS afkomst")
cur.execute("DROP TABLE IF EXISTS datatry")

con.commit()


gd = pd.read_csv('c:/Users/chris_e6ug8um/Documents/GitHub/Project-3-Data/Data/Geweldsdelicten.csv', sep=';')
fd = pd.read_csv('c:/Users/chris_e6ug8um/Documents/GitHub/Project-3-Data/Data/Fietsendiefstal.csv', sep=';')
do = pd.read_csv('c:/Users/chris_e6ug8um/Documents/GitHub/Project-3-Data/Data/Drugsoverlast.csv', sep=';')
th = pd.read_csv('c:/Users/chris_e6ug8um/Documents/GitHub/Project-3-Data/Data/Tevredenheid.csv', sep=';')
af = pd.read_csv('c:/Users/chris_e6ug8um/Documents/GitHub/Project-3-Data/Data/Afkomst.csv', sep=';')
dt = pd.read_csv('c:/Users/chris_e6ug8um/Documents/GitHub/Project-3-Data/Data/Datatrytest.csv', sep=';', encoding='latin-1')

gd.columns = [c.lower() for c in gd.columns] #postgres doesn't like capitals or spaces
fd.columns = [c.lower() for c in fd.columns]
do.columns = [c.lower() for c in do.columns]
th.columns = [c.lower() for c in th.columns]
af.columns = [c.lower() for c in af.columns]
dt.columns = [c.lower() for c in dt.columns]

from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:pgadmin2017@localhost:5432/StekOverflow')

gd.to_sql("geweldsdelicten", engine)
fd.to_sql("fietsendiefstal", engine)
do.to_sql("drugsoverlast", engine)
th.to_sql("tevredenheid", engine)
af.to_sql("afkomst", engine)
dt.to_sql("datatry", engine)

