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

cur.execute('''
        SELECT person.firstname, person.lastname, employee.jobtitle, emailaddress.emailaddress, employee.vacationhours
        FROM humanresources.employee
        JOIN person.person using(businessentityid)
        JOIN person.emailaddress using(businessentityid)
        WHERE employee.vacationhours > %(vh)s
         ;''', {'vh':vh})
for line in cur:
    print(line)

#conn.commit()
conn.close()