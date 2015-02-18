#! /usr/bin/env python

from sys import argv
script, q1, q2, k = argv

fw = open('c.txt', 'w+')

for docid in range(1,192):
	filename = 'data/' + str(docid) + '.txt'
	fr = open(filename)
	string = fr.read()

	pp1 = []
	pp2 = []
	l = []
	position = 0
	for token in string.split():
		if token == q1:
			pp1.append(position)
		if token == q2:
			pp2.append(position)
		position += 1

	for i in pp1:
		for j in pp2:
			if abs(i - j) <= int(k):
				l.append(j)
			elif j > i:
				break
		while l and abs(l[0] - i) > int(k):
			l.pop(0)
		prev_ps = -1
		for ps in l:
			if ps != prev_ps:
				fw.write(str(docid) + ' ' + str(i) + ' ' + str(ps) + '\n')
			prev_ps = ps
	
