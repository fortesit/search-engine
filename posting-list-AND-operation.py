#! /usr/bin/env python

from sys import argv
script, q1, q2 = argv

fw = open('b.txt', 'w+')
doc1 = set()
doc2 = set()

for docid in range(1,192):
	filename = 'data/' + str(docid) + '.txt'
	fr = open(filename)
	string = fr.read()

	for token in string.split():
		if token == q1:
			doc1.add(docid)
		if token == q2:
			doc2.add(docid)

result = sorted(list(set(doc1) & set(doc2)))
for i in result:
	fw.write(str(i) + '\n')
