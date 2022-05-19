#!/usr/bin/python3

import sys

for line in sys.stdin:
	line = line.strip()
	values = line.split(',')
	try:
		sell = int(values[0])
		room = int(values[4])
	except:
		continue

	print('%s\t%s' % (sell,room))