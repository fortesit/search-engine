#! /usr/bin/env python

import sys
from sys import argv
from collections import defaultdict

# Read dictionary.txt
filename = 'data/dictionary.txt'
fr = open(filename)
string = fr.read()

# Initialize matrix
terms = defaultdict(int)
for line in string.splitlines():
    termid, term = line.split()
    terms[term] = int(termid)
Matrix = [[0 for x in xrange(int(termid)+1)] for x in xrange(192)]

docs = []
for docid in range(1,192):
    # Read documents
    filename = 'data/' + str(docid) + '.txt'
    fr = open(filename)
    string = fr.read()

    # Assign values to Matrix
    for token in string.split():
        if token in terms:
            Matrix[docid][terms[token]] = 1

# Calculate Jaccard Coefficient
for qid in [1,5,40,60]:
    jaccard_list = []
    for docid in range(1,192):
        if docid in [1,5,40,60]:
            continue
        intersect_count = 0
        union_count = 0
        for tid in range(1,int(termid)+1):
            intersect_count += (Matrix[qid][tid] and Matrix[docid][tid])
            union_count += (Matrix[qid][tid] or Matrix[docid][tid])
        jaccard_list.append((docid, intersect_count/float(union_count)))
    
    jaccard_list = sorted(jaccard_list, key=lambda k:k[1], reverse=True)

    sys.stdout.write("%s:" %(qid))
    for i in range(10):
        sys.stdout.write("%s" %(jaccard_list[i][0]))
        if i == 9:
            print ''
        else:
            sys.stdout.write(",")
