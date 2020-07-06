
import sqlite3
import datetime

dataRegistro = datetime.datetime.now()


conn = sqlite3.connect('db.sql')

cursor = conn.cursor()

try:
    cursor.execute(""" CREATE TABLE site
                (url text,
                status_code integer,
                status_text text,
                date timestamp)
                """)
    print("Criando Tabela!")
except:
    print("Tabela ja existe!")

status = ['http://www.xxxxxxx.com.br','500','Site ok',dataRegistro]

conn.execute("INSERT INTO site (url,status_code,status_text,date) VALUES (?,?,?,?)",  (status[0],status[1],status[2],status[3]))

conn.commit()



sql = """
        SELECT * FROM site
        WHERE status_code LIKE '500' """

cursor.execute(sql)
print(cursor.fetchall())


