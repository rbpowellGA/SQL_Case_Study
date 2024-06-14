import psycopg2 as pg2
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# Establishes connection with database
conn = pg2.connect(dbname=os.getenv('DBNAME'),
                   user=os.getenv('ADV_WORKS_USER'),
                   password = os.getenv('PASSWORD'),
                   host = os.getenv('HOST'),
                   port = os.getenv('PORT'))

# Creates a var for reference to anything pulled from database
cur = conn.cursor()

'''
Parameters:
    sql_in (str): relative filepath to .sql file
    xlsx_out (str): relative filepath to directory where .xlsx will be stored
    xlsx_name (str or None): If not None, file named xlsx_name.xlsx
                             If None, file named same as sql_in
'''
def convert_sql_to_xlsx(sql_in, xlsx_out, xlsx_name=None):

    # Opens and reads the sql file
    sqlread = open(sql_in, 'r')
    sqlfile = sqlread.read()
    sqlread.close()

    # Executes the query from the sql in the database
    cur.execute(sqlfile)

    # Pandas reads the query
    df = pd.read_sql_query(sqlfile, conn)

    # Sets the name (if not given explicitly)
    if xlsx_name == None:
        # Splits up the file name from the file path
        string_manip = sql_in.split('/')
        # Grabs the file name indice
        string_manip = string_manip[-1]
        # Grabs the file name out of a list into a string, removing the file extension
        xlsx_name = string_manip[:-4]
    
    df.to_excel(f'{xlsx_out}/{xlsx_name}.xlsx', index=False)


convert_sql_to_xlsx('sql_queries/vacation_hour.sql','data')
conn.close()