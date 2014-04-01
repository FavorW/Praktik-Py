from lxml import etree
from io import StringIO, BytesIO
SearchPart = input("Enter searching part: ")
raw = SearchPart.split(".")
for x in range(10):
    numfile = str(x)
    tree = etree.parse('app'+numfile+'.xml') # Парсинг файла
    PathCont = tree.xpath('/root/mo/'+raw[0]+'/text()')
    if PathCont[0] == raw[1]:
        print ('XML File'+numfile+' = '+PathCont[0])
    else:
        print("Error :  No such element exists in XML File"+numfile)

