#!/usr/bin/python3

import sys

y1958 = []
y1959 = []
y1960 = []
count = 0

for line in sys.stdin:
	a,b,c = line.split('\t')
	
	try:
		a = int(a)
		b = int(b)
		c = int(c)
	except ValueError:
		continue

	y1958.append(a)
	y1959.append(b)
	y1960.append(c)
	count = count+1

sum1958 = 0
sum1959 = 0
sum1960 = 0

for i in y1958:
	sum1958 = sum1958+int(i)
for i in y1959:
	sum1959 = sum1959+int(i)
for i in y1960:
	sum1960 = sum1960+int(i)

print("1958년 총 승객 수 : ", sum1958, "/ 평균 승객 수 : ", sum1958/count)
print("1959년 총 승객 수 : ", sum1959, "/ 평균 승객 수 : ", sum1959/count)
print("1960년 총 승객 수 : ", sum1960, "/ 평균 승객 수 : ", sum1960/count)
