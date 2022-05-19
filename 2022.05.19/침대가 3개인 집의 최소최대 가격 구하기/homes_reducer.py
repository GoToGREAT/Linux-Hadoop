#! /usr/bin/python3

import sys

threeroom = []

for line in sys.stdin:
	line = line.strip()
	a = line.split('\t')
	sell = int(a[0])
	room = int(a[1])
	if room==3:
		threeroom.append(sell)

if len(threeroom)  != 0:
	print('쓰리룸의 최대 금액 : %s, 최소 금액 : %s' % (max(threeroom), min(threeroom)))