'''def convert_sql_to_xlsx(sql_in, xlsx_out, xlsx_name=None):
    """
    Runs query in given .sql file, stores result as .xlsx file.

    Parameters:
        sql_in (str): relative filepath to .sql file
        xlsx_out (str): relative filepath to directory where .xlsx will be stored
        xlsx_name (str or None): If not None, file named xlsx_name.xlsx
                                 If None, file named same as sql_in

    Returns:
        None
    """
    pass'''

import psycopg2 as pg2
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv, error

load_dotenv()

# Establishes connection with database
conn = pg2.connect(dbname=os.getenv('DBNAME'),
                   user=os.getenv('ADV_WORKS_USER'),
                   password = os.getenv('PASSWORD'),
                   host = os.getenv('HOST'),
                   port = os.getenv('PORT'))

# Creates a var for reference to anything pulled from database
cur = conn.cursor()

# Given a sql file, an output path, and (optional) a name, queries the db and saves the results to the specified file path under the given name,
#  Or under the name of the sql file given
def convert_sql_to_xlsx(sql_in, xlsx_out, xlsx_name=None):

    # Opens and reads the sql file
    sqlread = open(sql_in, 'r')
    sqlfile = sqlread.read()
    sqlread.close()

    # Executes the query from the sql in the database
    try:
        cur.execute(sqlfile)
    except:
        print(error)

    
    df = pd.read_sql_query(sqlfile, conn)
    if xlsx_name == None:
        xlsx_name = sql_in[:-3]

    df.to_excel(f'{xlsx_out}/{xlsx_name}.xlsx', index=False)
#conn.commit()



convert_sql_to_xlsx('sql_queries/vacation_hour.sql','data','test')
conn.close()