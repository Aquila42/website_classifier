import gzip
import bson.json_util as json
import urllib2
from BeautifulSoup import BeautifulSoup
import traceback

#Open the mongo dump here

f = open('data_subset','r')
urls = []
try:
    #with gzip.open( mongo_dump ) as f:
        for line in f:
            event = json.loads(line)
            #print event
            url = event['httpref']
            try:
                valid_url = urllib2.urlopen(url,None,1)
                html = BeautifulSoup(valid_url)
                print url
                try:
                    print html.title.string
                except:
                    print "No title"
                urls.append(url)
            except:
                continue

except Exception as e:
    #traceback.print_stack()
    print e

f = open('urls', 'w')
for url in urls:
    f.write(url+'\n')
