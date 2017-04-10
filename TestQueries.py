import psycopg2 as p

con = p.connect("dbname='StekOverflow' user='postgres' host='localhost' password='pgadmin2017'")

cur = con.cursor()
wijknaam = "Bospolder"
watwiljezien = "VraagDrukSocialeHuurwoningen"
db = "fiobj2016"

cur.execute("select {} from {} where wijkNaam = '{}'".format(watwiljezien,db,wijknaam))
wijkdata = cur.fetchone()
print(wijkdata[0])

lol = wijkdata[0] * 2

print(lol)