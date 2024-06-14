# SQL_Case_Study
## Overview
This program takes in .sql files and converts them into .xlsx, either by single file or by directory.

## Creating a .env for database variables
Create .env file with the following information:
``` bash
DBNAME = 
ADV_WORKS_USER = 
PASSWORD = 
HOST = 
PORT = 
```

## Calling for a directory of .sql files to be converted into .xlsx files from the Command Line Interface (CLI)
By default, the sql.py program will be listening for help, verbose, quiet, and two positional arguements (-s, -x).
``` bash
options:
  -h, --help     show this help message and exit
  -v, --verbose  Option for more explicit answer
  -q, --quiet    Option for if you already have an understanding of the programs full function
  -s S           The directory to pull sql files from
  -x X           The directory to store xlsx files in
```
For example, if given the command:
``` bash
python sql.py -v -s sql_queries -x data
```
The output would appear as:
``` bash
sql_queries sql files have been saved as .xlsx in the directory data
```
## Calling for a single file conversion
Either inside the sql.py or imported into another file, the convert_sql_to_xlsx_from_cli() will take in
``` python
Parameters:
    sql_in (str): relative filepath to .sql file
    xlsx_out (str): relative filepath to directory where .xlsx will be stored
    xlsx_name (str or None): If not given a name, file name will be same as .sql file as a .xlsx
                             If name is given, file will be named as xlsx_name.xlsx
```

## Importing a function elsewhere for conversion of a .sql file directory into .xlsx files
By calling the convert_directory_of_queries() function, rather than specifying in the CLI, the function can be called elsewhere given
``` python
Parameters:
    sql_in_dir (str): relative filepath to directory
                        containing .sql files
    xlsx_out_dir (str): relative filepath to directory
                        where .xlsx will be stored
                        files named same as sql_in
```
