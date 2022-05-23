#!/usr/bin/env python
# coding: utf-8

# # Hive 데이터베이스에 접근하는 외부 파이썬 프로그램의 예

# cd hive-3.1.2/bin
# hiveserver2
# 
# cd hive-3.1.2/bin
# beeline 
# !connect jdbc:hive2://localhost:10000/userdb;

# In[1]:


from impala.dbapi import connect

conn = connect(host='192.168.184.128', port=10000, database="userdb", auth_mechanism='PLAIN')
cursor = conn.cursor()
cursor.execute('select * from employee')
print(cursor.fetchall())


# In[2]:


from impala.dbapi import connect

conn = connect(host='192.168.184.128', port=10000, database="userdb", auth_mechanism='PLAIN')
cursor = conn.cursor()
cursor.execute('select * from employee')

for row in cursor.fetchall():
    num,name,salary,destination = row
    print("{}\t{}\t{}\t{}".format(num,name,salary,destination))


# In[3]:


from impala.dbapi import connect

conn = connect(host='192.168.184.128', port=10000, database="userdb", auth_mechanism='PLAIN')
cursor = conn.cursor()
cursor.execute('select * from employee')

for row in cursor.fetchall():
    num,name,salary,destination = row
    print("{}\t{:12}\t{}\t{}".format(num,name,salary,destination))


# In[ ]:





# In[ ]:


import pandas as pd
df = pd.DataFrame(data={'A':[2,4,8],
                   'B':[5,8,2],
                   'C':[9,5,7]})


# In[ ]:


print(df)


# In[ ]:


df.sum() # 세로계산


# In[ ]:


df.sum(axis=1) #가로계산


# In[ ]:





# # Spark_Test

# In[ ]:


import findspark
findspark.init()

import pyspark              # only run after findspark.init()
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.sql('''select 'spark' as hello ''')
df.show()


# In[ ]:




