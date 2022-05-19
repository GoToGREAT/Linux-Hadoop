#!/usr/bin/python3

#mapperAverage.py

import sys

for line in sys.stdin:
	line = line.strip()
	words = line.split(",")
	
	print('%s\t%s\t%s' % (words[1], words[2], words[3]) )