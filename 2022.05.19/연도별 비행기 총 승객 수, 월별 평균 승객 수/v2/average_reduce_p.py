#! /usr/bin/python3

import sys

passengers = {'1958':[], '1959':[], '1960':[]}

for line in sys.stdin:
        line = line.strip()
        v, y = line.split('\t', 1)
        passengers[y.strip()].append( int(v.strip()))

avg = {}
avg['1958'] = sum( passengers['1958'])// len(passengers['1958'])
avg['1959'] = sum( passengers['1959'])// len(passengers['1959'])
avg['1960'] = sum( passengers['1960'])// len(passengers['1960'])

print(avg)