import psycopg2 as pg2
import pandas as pd
from datetime import datetime
import os
from dotenv import load_dotenv
import argparse

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

"""
Runs each query in sql_in_dir directory,
    stores each result as .xlsx in xlsx_out_dir.

Parameters:
    sql_in_dir (str): relative filepath to directory
                        containing .sql files
    xlsx_out_dir (str): relative filepath to directory
                        where .xlsx will be stored
                        files named same as sql_in
"""

def convert_directory_of_queries(sql_in_dir, xlsx_out_dir):

    for file in os.listdir(sql_in_dir):
        f = f'{sql_in_dir}/{file}'
        convert_sql_to_xlsx(f, xlsx_out_dir)

"""
Converts directory of sql queries to xlsx from CLI.
"""

def convert_sql_to_xlsx_from_cli():
    parser = argparse.ArgumentParser(description="Converts directory of sql queries to xlsx from CLI.")

    # Specifies options that conflict with one another, in this case verbose and quiet
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true", help="Option for more explicit answer")
    group.add_argument("-q", "--quiet", action="store_true", help="Option for if you already have an understanding of the program's full function")

    # Our two variable arguements
    parser.add_argument("-s", type=str, help="The directory to pull sql files from")  # Arguements
    parser.add_argument("-x", type=str, help="The directory to store xlsx files in")

    # Parses the arguements given into variables and calls our function
    args = parser.parse_args()  
    convert_directory_of_queries(args.s, args.x)

    # Checking for our verbose and quiet flags
    if args.quiet:  # If quiet flag is present, give the answer only
        print("Data saved")
    elif args.verbose:  # If verbose is present, give more descript answer
        print(f"{args.s} sql files have been saved as .xlsx in the directory {args.x}")
    else:  # Default format for answering
        print(f"{args.s} saved to {args.x}")

# Runs cli if running the file directly
if __name__ == '__main__':
    load_dotenv()

    # Establishes connection with database
    conn = pg2.connect(dbname=os.getenv('DBNAME'),
                    user=os.getenv('ADV_WORKS_USER'),
                    password = os.getenv('PASSWORD'),
                    host = os.getenv('HOST'),
                    port = os.getenv('PORT'))

    # Creates a var for reference to anything pulled from database
    cur = conn.cursor()
    #Listens for CLI inputs
    convert_sql_to_xlsx_from_cli()
    #Closes the db connection
    conn.close()