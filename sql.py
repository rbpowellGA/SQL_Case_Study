import psycopg2 as pg2
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

vh = input('vacation hours threshold: ')

conn = pg2.connect(dbname=os.getenv('DBNAME'),
                   user=os.getenv('ADV_WORKS_USER'),
                   password = os.getenv('PASSWORD'),
                   host = os.getenv('HOST'),
                   port = os.getenv('PORT'))

cur = conn.cursor()

cur.execute()
       
for line in cur:
    print(line)

#conn.commit()
conn.close()