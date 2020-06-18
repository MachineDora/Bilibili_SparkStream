# -*- coding:utf-8 -*-
from __future__ import print_function

from pyspark import SparkContext,SparkConf
from pyspark.streaming import StreamingContext

def write_file(filename, iter):
    with open(filename, 'w',encoding='utf-8') as f:
        for record in iter:
            f.write(str(record))
            f.write('\n')

def write(iter):
    filename = 'D:/PY/Spark/file/tags_count.txt'
    write_file(filename, iter)

def write_2(iter):
    filename = 'D:/PY/Spark/file/tags.txt'
    write_file(filename, iter)


if __name__ == "__main__":
    sc = SparkContext("local", "pythonStreaming")
    ssc = StreamingContext(sc, 3)
    #sc=SparkContext(conf=conf)
    lines=ssc.textFileStream("log/")
    lines.pprint()
    words=lines.flatMap(lambda line:line.split("\n"))
    pairs=words.map(lambda word:(word,1))
    wordcounts=pairs.reduceByKey(lambda a,b:a+b)
    rdd=wordcounts
    rdd.foreachRDD(lambda rdd:rdd.foreachPartition(write))
    # with open("D:/PY/Spark/all.txt",'r') as fp:
    #    content=fp.read().splitlines()
    #    rdd=sc.parallelize(content)
    #    resultRdd = rdd.map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b).sortBy(_toGirl,True)
    #    resultcoll=resultRdd.collect()
    #    for line in resultcoll:
    #        with open("D:/PY/Spark/all_wordcount.txt", 'a')as f:
    #            f.write(str(line)+'\n')
    #sc.stop()
    #print(lines.map(lambda x:x.split('\n')).reduceByKey(lambda a, b:a+b))
    ssc.start()
    ssc.awaitTermination()
    #pairs=line.map(lambda word:(word,1))
    #wordcounts=pairs.reduceByKey(lambda a,b:a+b)
    #sortResult=wordcounts.foreachRDD(lambda rdd:rdd.foreachPartition(write))
    #lines.flatMap(lambda x: x.split("\n")) \
    #    .map(lambda word:(word,1))\
    #    .reduceByKey(lambda a, b: a+b) \
    #    .foreachRDD(lambda rdd: rdd.foreachPartition(write))




