#! /usr/bin/python3

import findspark
findspark.init()
from pyspark.sql import SparkSession

sparkSession = SparkSession.builder.appName("pyspark-hdfs2").getOrCreate()

# read.load()는 다양한 옵션을 설정할 수 있다
df1 = sparkSession.read.csv('/home/hduser/employee.csv')  # csv 내의 헤더가 없는 경우
df1 = df1.toDF('num','name','salary','job')        #  컬럼명 추가
df1.show()

df1 = df1.withColumn('salary', df1.salary+5000)
df1.show()

df1.write.csv('newemployee.csv', mode='overwrite', header=True)

df2 = sparkSession.read.load('/home/hduser/pyspark_test/newemployee.csv',
    format='csv', sep=',', inferSchema='true', header='true')
df2.show()
