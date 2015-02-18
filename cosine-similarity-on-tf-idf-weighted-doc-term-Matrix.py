#! /usr/bin/env python

import sys
import math
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
tf_idf = [[0 for x in xrange(int(termid)+1)] for x in xrange(192)]
tfs = [[0 for x in xrange(int(termid)+1)] for x in xrange(192)]
dfs = [0 for x in xrange(int(termid)+1)]

docs = []
for docid in range(1,192):
    # Read documents
    filename = 'data/' + str(docid) + '.txt'
    fr = open(filename)
    string = fr.read()
    
    # Calculate tfs
    for token in string.split():
        if token in terms:
            tfs[docid][terms[token]] += 1

# Calculate dfs
for tid in range(1,int(termid)+1):
    for docid in range(1,192):
        if tfs[docid][tid]:
            dfs[tid] += 1

# Calculate tf-idf
for docid in range(1,192):
    for tid in range(1, int(termid)+1):
        w = 1+math.log10(tfs[docid][tid]) if tfs[docid][tid] else 0
        tf_idf[docid][tid] = w*(math.log10(191/float(dfs[tid])))

# Normalize tf-idf vectors per document
for docid in range(1,192):
    sum = 0
    for tid in range(1,int(termid)+1):
        sum += tf_idf[docid][tid] * tf_idf[docid][tid]
    sum = math.sqrt(sum)
    for tid in range(1,int(termid)+1):
        tf_idf[docid][tid] /= sum

# Do the query: calculate dot products, than sort
for qid in [1,5,40,60]:
    cos_sim = []
    for docid in range(1,192):
        sum = 0
        for tid in range(1,int(termid)+1):
            sum += tf_idf[qid][tid] * tf_idf[docid][tid]
        cos_sim.append((docid, sum))

    cos_sim = sorted(cos_sim, key=lambda k:k[1], reverse=True)

    sys.stdout.write("%s:" %(qid))
    for i in range(10):
        sys.stdout.write("%s" %(cos_sim[i+1][0]))
        if i == 9:
            print ''
        else:
            sys.stdout.write(",")
