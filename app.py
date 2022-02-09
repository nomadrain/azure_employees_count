#!/usr/bin/env python3

import pyodbc
import flask
import json

# from config import *

db_conn_string = "Driver=ODBC Driver 17 for SQL Server;Server=tcp:nomadrain.database.windows.net,1433;Database=nomadrain_db;;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;Authentication=ActiveDirectoryMSI"
# with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:

application = flask.Flask(__name__)
application.config["DEBUG"] = True
application.secret_key = '2989084082039024j2k3l4230942jd02933'


@application.route('/', methods=['GET'])
def all_cdrs():
    result = dict()
    
    with pyodbc.connect(db_conn_string) as conn:
        with conn.cursor() as cursor:
            res = []
            cursor.execute("SELECT TOP 3 name, collation_name FROM sys.databases")
            row = cursor.fetchone()
            while row:
                res.append({'db_name': str(row[0]), 'collation': row[1]})
                row = cursor.fetchone()
            if res:
                result['TOP3'] = res
                return json.dumps(result, ensure_ascii=True, indent=4)


'''
Table: companies

field name, field type, example
company_id, bigint autoincreament primary_key unique constraint, 1
company_name, varchar(100), Everledger
contact_id, varchar(70), company:7b5e22b4-6327-4a6c-a44f-7a2c029efb67
entry_id, varchar(50), 84cd93e4-e02f-4709-a92d-31c508abd1f0
deal_team, varchar(50), Martijn van Heeswijk
    If this should be a list of the team members?
city, varchar(50), London
sector_1, varchar(30), B2B
sector_2, varchar(30), Fintech
linkedIn, nvarchar(100), https://www.linkedin.com/company/everledger
    nvarchar is used for the possible multilingual cases like Chineese
domains, nvarchar(50), everledger.io
    nvarchar is used for the possible multilingual cases like Chineese
    if this is a list and should be presented as a domains table related to companies as M:1


CREATE TABLE dbo.companies(
 [company_id] [bigint] IDENTITY(1,1) NOT NULL,
 [some_column] [varchar](10) NULL
)



'''
