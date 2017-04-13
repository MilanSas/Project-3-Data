import pandas as pd
import psycopg2 as psy

con = psy.connect("dbname='StekOverflow' user='postgres' host='localhost' password='pgadmin2017'")
cur = con.cursor()

# cur.execute("DROP TABLE IF EXISTS geweldsdelicten")
# cur.execute("DROP TABLE IF EXISTS fietsendiefstal")
# cur.execute("DROP TABLE IF EXISTS drugsoverlast")
# cur.execute("DROP TABLE IF EXISTS tevredenheid")
# cur.execute("DROP TABLE IF EXISTS afkomst")
# cur.execute("DROP TABLE IF EXISTS datatry")
# cur.execute("DROP TABLE IF EXISTS vi2016")
# cur.execute("DROP TABLE IF EXISTS si2016")
# cur.execute("DROP TABLE IF EXISTS fisub2016")
# cur.execute("DROP TABLE IF EXISTS fiobj2016")

con.commit()

geweldsdelicten_data = pd.read_csv('https://raw.githubusercontent.com/MilanSas/Project-3-Data/master/Data/Geweldsdelicten2006-2011.csv', sep=';')
fietsendiefstal_data = pd.read_csv('https://raw.githubusercontent.com/MilanSas/Project-3-Data/master/Data/Fietsendiefstal2006-2011.csv', sep=';')
drugsoverlast_data = pd.read_csv('https://raw.githubusercontent.com/MilanSas/Project-3-Data/master/Data/Geweldsdelicten2006-2011.csv', sep=';')
tevredenheid_data = pd.read_csv('https://raw.githubusercontent.com/MilanSas/Project-3-Data/master/Data/Tevredenheid2006-2011.csv', sep=';')
afkomst_data = pd.read_csv('https://raw.githubusercontent.com/MilanSas/Project-3-Data/master/Data/Afkomst.csv', sep=';')
vi_data = pd.read_csv('https://raw.githubusercontent.com/MilanSas/Project-3-Data/master/Data/VI2016.csv', sep=';', encoding='latin-1')
si_data = pd.read_csv('https://raw.githubusercontent.com/MilanSas/Project-3-Data/master/Data/SI2016.csv', sep=';', encoding='latin-1')
fisub2016_data = pd.read_csv('https://raw.githubusercontent.com/MilanSas/Project-3-Data/master/Data/FIsub2016.csv', sep=';', encoding='latin-1')
fiobj2016_data = pd.read_csv('https://raw.githubusercontent.com/MilanSas/Project-3-Data/master/Data/FIobj2016.csv', sep=';', encoding='latin-1')


geweldsdelicten_data.columns = [c.lower() for c in geweldsdelicten_data.columns] # sql haat hoofdletters
fietsendiefstal_data.columns = [c.lower() for c in fietsendiefstal_data.columns]
drugsoverlast_data.columns = [c.lower() for c in drugsoverlast_data.columns]
tevredenheid_data.columns = [c.lower() for c in tevredenheid_data.columns]
afkomst_data.columns = [c.lower() for c in afkomst_data.columns]
vi_data.columns = [c.lower() for c in vi_data.columns]
si_data.columns = [c.lower() for c in si_data.columns]
fisub2016_data.columns = [c.lower() for c in fisub2016_data.columns]
fiobj2016_data.columns = [c.lower() for c in fiobj2016_data.columns]

from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:pgadmin2017@localhost:5432/StekOverflow')

geweldsdelicten_data.to_sql("geweldsdelicten", engine)
fietsendiefstal_data.to_sql("fietsendiefstal", engine)
drugsoverlast_data.to_sql("drugsoverlast", engine)
tevredenheid_data.to_sql("tevredenheid", engine)
afkomst_data.to_sql("afkomst", engine)

vi_data.to_sql("vi2016", engine)
si_data.to_sql("si2016", engine)
fisub2016_data.to_sql("fisub2016", engine)
fiobj2016_data.to_sql("fiobj2016", engine)