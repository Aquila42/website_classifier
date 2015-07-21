'''
Extract words from URLs in the topic files
'''

import nltk, enchant
import urllib2
from bs4 import BeautifulSoup
punctuation = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~',"''",'""','--','//']
label = "travel"
path = "../features/"+label #The folder that contains the bag-of-words files
f = open(path,'r')

words = {}
d = enchant.Dict("en_US")
for url in f:
    try:
        valid_url = urllib2.urlopen(url,None,1)
        html = valid_url.read()
        print url
    except:
        continue
    soup = BeautifulSoup(html, 'html.parser')
    raw = soup.get_text().strip()
    #print raw
    ascii_raw = raw.encode("ascii","ignore")
    tokens = nltk.word_tokenize(ascii_raw)
    for word in tokens:
        for item in punctuation:
            if word.find(item):
                continue
        if len(word) == 1:
            continue
        try:
            if d.check(word) is False:
                continue
        except:
            continue
        if word.isalpha():
            word = word.lower()
            if word not in words.keys():
                words[word] = 1
            else:
                words[word] += 1


f.close()
path = "../features/"+label+"_freq"
f = open(path,'w')
for word in words.keys():
    f.write(word+" "+str(words[word])+"\n")
f.close()

