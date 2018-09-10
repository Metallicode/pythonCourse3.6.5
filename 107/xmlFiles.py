import xml.etree.ElementTree as et

##from string
####tree = et.fromstring("xmlTest.xml")

##from file
tree = et.parse("xmlTest.xml")
##print(tree)

#get root
root = tree.getroot()
##print(root)

##traverse
for elem in root:
      for e in elem:
            #print(e.tag, e.text)
            #print(e.tag, e.text, e.attrib["color"])
            #print(e.get('color')) #get attr

##iterate recursively over all the sub-tree
for price in root.iter("cost"):
      print(price.text)
      print(type(price.text))

##find direct children
##for elem in root:
##      if elem.find("bridge") is not None:
##            print(elem.find("bridge").text)

####findall direct children
##for elem in root:
##      for e in elem.findall("bridge"):
##            print(e.text)

###XPath
##for e in root.find('guitar'):
##      print(e)
##      
##for e in root.findall('guitar'):
##      print(e)

###/grandchildren of root -> guitar parent
##for e in root.findall('guitar/cost'):
##      print(e)
##
###/grandchildren of root * parent
##for e in root.findall('*/cost'):
##      print(e)


##get parent
##elem = root[0][2]
##print(elem)
##print(root.find('.//'+elem.tag+'/..'))

#query
##elem = root.findall('guitar/body[@color]')
##print(elem)
##for i in elem:
##      print(i.text)
##      print(i.get("color"))

###find text
##elem = root.findtext('guitar/body[@color]', default=None)
##print(elem)





#####add element
##newItem = et.SubElement(root, "guitar", attrib={"id":"4"})
##new_body = et.SubElement(newItem, "body")
##new_neck = et.SubElement(newItem, "neck")
##new_maker = et.SubElement(newItem, "maker")
##new_cost = et.SubElement(newItem, "cost")
##
##new_body.text = "test"
##new_neck.text = "test"
##new_maker.text = "test"
##new_cost.text = "234"
##
##tree.write("xmlTest.xml")
##



####add from string
##xmlStr = """
##<guitar>
##      <body>mahagoni555</body>
##      <neck>maple555</neck>
##      <maker>gibson555</maker>
##      <cost>500$555</cost>
##</guitar>
##"""
##newElem = et.fromstring(xmlStr)
##
###append
####root.append(newElem)
##
###insert to index
##root.insert(0,newElem)
##tree.write("xmlTest.xml")


#change element
##print(root)
##print(root[0])
##print(root[0].find('cost'))
##print(root[0].find('cost').text)
##root[0].find('cost').text = "467$"
##tree.write("xmlTest.xml")

#remove element
##root.remove(root[1])
##tree.write("xmlTest.xml")







