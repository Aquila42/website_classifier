import awis
from lxml import etree

#Use awis to connect to Alexa here

#Read URLs from file
f = open('urls','r')
urls = []
for line in f:
    urls.append(line.strip())
f.close()

namespaces = {"aws": "http://awis.amazonaws.com/doc/2005-07-11"}
#

url_category = []

for url in urls:
    tree = api.url_info(url,"Categories")
    root = tree.getroot()
    xmlstr = etree.tostring(root)
    doc = etree.fromstring(xmlstr.strip())
    texts = doc.xpath("//aws:Categories/aws:CategoryData/aws:AbsolutePath/text()", namespaces=namespaces)
    if len(texts) < 1:
        #Deal with this
        url_category.append('')
        #print url
        continue
    print url
    category_path = texts[0]
    if category_path.find('Regional'):
        print category_path
        category = category_path[category_path.rfind('/')+1:]
        print category
    else:
        print category_path
        category = category_path[:category_path.find('/')]
        print category
    url_category.append(category)

print len(urls),len(url_category)
print set(url_category)
