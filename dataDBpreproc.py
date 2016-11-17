# Author: Josh - joshwong@cisco.com

# Purpose: this file is for doing meta data preprocessing


from dataDBconn import connCreate, getDBdata

metaDataSql = "select * from information_schema.columns where table_schema != 'information_schema'"
dbtype = 'mysql'
conn = connCreate(dbtype)
metaDataDF = getDBdata(conn, metaDataSql)
colList = metaDataDF.columns.values.tolist()

#table_name = 'TABLE_NAME'
#print metaDataDF.loc[metaDataDF[table_name] == 'application_dimension']
#print metaDataDF.ix[metaDataDF[table_name] == 'storage_dimension']

column_commentDF = metaDataDF.sort_values(by='COLUMN_COMMENT').COLUMN_COMMENT.drop_duplicates()

topic = 'storage'

def pre_proc_data_fetch(colList,topic):
    for words in colList:
        print metaDataDF[words].drop_duplicates()
    return 0

# pre_proc_data_fetch(colList, topic)


# prints 3 columns where a search criteria filters
print metaDataDF[['TABLE_NAME','COLUMN_NAME','COLUMN_COMMENT']].where(metaDataDF['COLUMN_NAME'].str.contains('url') == True).drop_duplicates().dropna()

print metaDataDF['COLUMN_COMMENT'].iloc[:2].where(metaDataDF['TABLE_NAME'] == 'application_dimension').drop_duplicates()

tableName = ''
searchName = ''

urlKeyValueSQL = "SELECT name, url FROM %s WHERE name = '%s'" % (tableName,searchName)

print urlKeyValueSQL

keyValueData = getDBdata(conn, urlKeyValueSQL)

