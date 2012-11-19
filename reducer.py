#!/usr/bin/env python
import sys

dic1={}

for line in sys.stdin:
    record=line.strip(" \r\n").split("\t")
    country=record[0]
    count=record[1]
    if country not in dic1:
        dic1[country]=count
    else:
        dic[country]+=1

for key,value in dic1.iteritems():
    print key,value
