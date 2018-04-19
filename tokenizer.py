import tokenize
import token
from training_data import getData
import nltk
from nltk import trigrams
import numpy as np
from collections import Counter

data, target = getData()
numb = 5

print("---",target[numb]['truthMedian']," ",target[numb]['truthClass'])

feature = data[numb]['targetTitle']
print(feature)

splitter = nltk.data.load('tokenizers/punkt/english.pickle')
sent_pos = {'id': data[numb]['id']}
sent_only_pos = []

if len(feature[0]) == 1:
    for sent in splitter.tokenize(feature.strip()):
        tokenizer = nltk.word_tokenize(sent)
        pos_tags = nltk.pos_tag(tokenizer)
        for p in pos_tags:
            sent_only_pos.append(p[1])
        sent_pos.update({'pos_tags':sent_only_pos})
        trigrams_list = list(trigrams(tokenizer))
    print(sent_pos)
else:
    a=1
    for line in feature:
        for sent in splitter.tokenize(line.strip()):
            tokenizer = nltk.word_tokenize(sent)
            pos_tags = nltk.pos_tag(tokenizer)
            a = a+1
            for p in pos_tags:
                sent_only_pos.append(p[1])
            sent_pos.update({'pos_tags': sent_only_pos})
            trigrams_list = list(trigrams(tokenizer))
    print(sent_pos)

print("*********** TRIGRAMMI POS ***********")
trigrams_pos = list(trigrams(sent_pos['pos_tags']))
print(trigrams_pos)
