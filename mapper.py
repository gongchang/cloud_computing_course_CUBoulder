#!/usr/bin/env python

import sys

for line in sys.stdin:
    record=line.strip(" \r\n").split(",")
    country=record[4]
    if len(country)==2:
        print country,1