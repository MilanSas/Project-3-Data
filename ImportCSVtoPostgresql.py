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
cur.execute("DROP TABLE IF EXISTS vi2016")
cur.execute("DROP TABLE IF EXISTS si2016")
cur.execute("DROP TABLE IF EXISTS fisub2016")
cur.execute("DROP TABLE IF EXISTS fiobj2016")


con.commit()


gd = pd.read_csv('c:/Users/chris_e6ug8um/Documents/GitHub/Project-3-Data/Data/Geweldsdelicten2006-2011.csv', sep=';')
fd = pd.read_csv('c:/Users/chris_e6ug8um/Documents/GitHub/Project-3-Data/Data/Fietsendiefstal2006-2011.csv', sep=';')
do = pd.read_csv('c:/Users/chris_e6ug8um/Documents/GitHub/Project-3-Data/Data/Drugsoverlast2006-2011.csv', sep=';')
th = pd.read_csv('c:/Users/chris_e6ug8um/Documents/GitHub/Project-3-Data/Data/Tevredenheid2006-2011.csv', sep=';')
af = pd.read_csv('c:/Users/chris_e6ug8um/Documents/GitHub/Project-3-Data/Data/Afkomst.csv', sep=';')
# dt = pd.read_csv('c:/Users/chris_e6ug8um/Documents/GitHub/Project-3-Data/Data/Datatrytest.csv', sep=';', encoding='latin-1')
vi = pd.read_csv('c:/Users/chris_e6ug8um/Documents/GitHub/Project-3-Data/Data/VI2016.csv', sep=';', encoding='latin-1')
si = pd.read_csv('c:/Users/chris_e6ug8um/Documents/GitHub/Project-3-Data/Data/SI2016.csv', sep=';', encoding='latin-1')
fisub2016 = pd.read_csv('c:/Users/chris_e6ug8um/Documents/GitHub/Project-3-Data/Data/FIsub2016.csv', sep=';', encoding='latin-1')
fiobj2016 = pd.read_csv('c:/Users/chris_e6ug8um/Documents/GitHub/Project-3-Data/Data/FIobj2016.csv', sep=';', encoding='latin-1')

gd.columns = [c.lower() for c in gd.columns] # sql haat hoofdletters
fd.columns = [c.lower() for c in fd.columns]
do.columns = [c.lower() for c in do.columns]
th.columns = [c.lower() for c in th.columns]
af.columns = [c.lower() for c in af.columns]
# dt.columns = [c.lower() for c in dt.columns]
vi.columns = [c.lower() for c in vi.columns]
si.columns = [c.lower() for c in si.columns]
fisub2016.columns = [c.lower() for c in fisub2016.columns]
fiobj2016.columns = [c.lower() for c in fiobj2016.columns]


from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:pgadmin2017@localhost:5432/StekOverflow')

gd.to_sql("geweldsdelicten", engine)
fd.to_sql("fietsendiefstal", engine)
do.to_sql("drugsoverlast", engine)
th.to_sql("tevredenheid", engine)
af.to_sql("afkomst", engine)
# dt.to_sql("datatry", engine)
vi.to_sql("vi2016", engine)
si.to_sql("si2016", engine)
fisub2016.to_sql("fisub2016", engine)
fiobj2016.to_sql("fiobj2016", engine)