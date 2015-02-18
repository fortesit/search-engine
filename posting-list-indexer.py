#! /usr/bin/env python

from sys import argv
script, query = argv

fw = open('a.txt', 'w+')
fw.write('word:' + query + '\n')

for docid in range(1,192):
	filename = 'data/' + str(docid) + '.txt'
	fr = open(filename)
	string = fr.read()

	frequency = 0
	position_list = []
	position = 0
	for token in string.split():
		if token == query:
			position_list.append(position)
			frequency += 1
		position += 1

	if frequency > 0:
		fw.write(str(docid) + ',' + str(frequency) + ':')
		for i in position_list:
			fw.write(' ' + str(i))
		fw.write('\n')
