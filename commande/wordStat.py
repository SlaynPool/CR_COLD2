#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyspark import SparkContext
sc=SparkContext(appName="WordStats")
lines=sc.textFile('file:///root/file1.txt')
print(lines)
lines.collect()
words=lines.flatMap(lambda x: x.split())
words.collect()
tuples=words.map(lambda x: (x, 1))
tuples.collect()
res=tuples.reduceByKey(lambda a,b: a+b)
res.collect()
mostUsed=sc.parallelize([res.takeOrdered(5, key = lambda x: -x[1])])
mostUsed.collect()
mostUsed.saveAsTextFile('file:///root/data_out3')

