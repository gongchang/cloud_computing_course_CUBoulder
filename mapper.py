#!/usr/bin/env python

import sys

for line in sys.stdin:
    record=line.strip(" \r\n").split(",")
    #state is the 6th field of the record
    country=record[5]
    #print record
    
    #the length of the state abbreviation is 2, but " and " will have
    #a size of 1 each.Therefore, the total size should be 4
    if len(country)==4:
        print country,1