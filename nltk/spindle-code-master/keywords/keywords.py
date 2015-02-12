#!/usr/local/bin/python
# -*- coding: utf-8 -*-


from collections import defaultdict
import sys,os
import math
import json
from stopwords import stopwords as my_stopwords
from bnc import fdistBNC, sumBNC

def ngrams(words, n=2):
    return (tuple(words[i:i+n]) for i in range(0, len(words) - (n - 1)))

def keywords_and_ngrams(input, nKeywords=100, thresholdLL=19, nBigrams=25, thresholdBigrams=2):

    fdistText = defaultdict(int)
    sumText = 0
    listWords = []
    listSentences = []
    
    if isinstance(input,str):
        listSentences = [input]
    else:
        listSentences = input
    
    for line in listSentences:
        for w in line.split():
            w = w.lower()
            listWords.append(w)
            sumText = sumText+1
            if w not in my_stopwords and w.isalpha() and len(w) > 2:
                fdistText[w] = fdistText[w]+1

    dicLL = {}

    for k, v in fdistText.items():
        a = fdistBNC.get(k)
        b = fdistText.get(k)
        c = sumBNC
        d = sumText
        if a == None:
            a = 0
        if b == None:
            b = 0
        E1 = float(c)*((float(a)+float(b))/ (float(c)+float(d)))
        E2 = float(d)*((float(a)+float(b))/ (float(c)+float(d)))
        if a == 0:
            logaE1 = 0
        else:
            logaE1 = math.log(a/E1)  
        dicLL[k] = float(2* ((a*logaE1)+(b*math.log(b/E2))))

    sortedLL = sorted(dicLL, key=dicLL.__getitem__, reverse=True)
    listKeywords = [(k, dicLL[k]) for k in sortedLL if k.isalpha() and dicLL[k] > thresholdLL]

    keywords = [keyw[0] for keyw in listKeywords]
    counts = defaultdict(int)
    for ng in ngrams(listWords, 2):
        counts[ng] += 1

    listBigrams = []
    for c, ng in sorted(((c, ng) for ng, c in counts.iteritems()), reverse=True):
        w0 = ng[0]
        w1 = ng[1]
        if w0 in keywords and w1 in keywords and c>thresholdBigrams:
            listBigrams.append((ng, c))
    return (listKeywords[0:nKeywords], listBigrams[0:nBigrams])



if __name__=="__main__":
    if len(sys.argv) < 2:
        sys.stderr.write("Usage: python %s <text.txt>\n" % (sys.argv[0],))
    else:
        d = keywords_and_ngrams(open(sys.argv[1]),"r").readlines(), 100, 19, 25, 2)
        print json.dumps(d)

