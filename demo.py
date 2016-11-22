# Author: joshwong@cisco.com
# Purpose: Basic pseudo code of steps required for main program + pieces of work


from dataDBconn import connCreate, getDBdata
from chunkWords import process_sentence, chunk_sentence
import random as r


##### Pseudo Code #####


# 1.0 Build Knowledge on instantiate Bot
# 1.1 Pull metadata from structural storage meta data information from a relational database

metaDataSql = "select * from information_schema.columns where table_schema != 'information_schema'"
dbtype = 'mysql'
conn = connCreate(dbtype)
metaDataDF = getDBdata(conn, metaDataSql)
colList = metaDataDF.columns.values.tolist()

column_commentDF = metaDataDF.sort_values(by='COLUMN_COMMENT').COLUMN_COMMENT.drop_duplicates()
table_nameDF = metaDataDF.sort_values(by='TABLE_NAME').TABLE_NAME.drop_duplicates().to_string()
table_schemaDF = metaDataDF.sort_values(by='TABLE_SCHEMA').TABLE_SCHEMA.drop_duplicates().to_string()

print column_commentDF.str.contains("storage")
print r.choice(column_commentDF.values.tolist())

# 1.2 Build metadata around API sets related to storage

# 1.3 Use metadata from DB/API for pos_tag

# 1.4 Use nltk for chunking/chinking/wordnet/corpus creation

# 2.0 Build Actions list
# 2.1 Define capabilities that eRetreive can do

# 3.0 SparkBot integration

# 4.0 UI inputs to meaning

# 5.0 Machine learning







