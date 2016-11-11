# Author: joshwong@cisco.com
# Purpose: this file will handle the relational DB connection and basic sql extract via a pandas dataframe

import pandas as pd
import pymysql as mysql

def connCreate(dbtype):
    if dbtype == 'mysql':
        conn = mysql.connect(host='', port=3306, user='', passwd='', db='')
    return conn

def getDBdata(conn, sqlstr):
    df = pd.read_sql(sqlstr, conn)
    return df


