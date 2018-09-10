import xml.etree.ElementTree as et
import os.path

class Product:
      def __init__(self, pname, ptext, pbrand, pcost, isVip):
            self.name = pname
            self.text = ptext
            self.brand = pbrand
            self.cost = pcost
            self.isVip = isVip

      def __repr__(self):
            return f"Product({self.name}, {self.text}, {self.brand}, {self.cost})"

class storeDatabase:
      def __init__(self, database_name):
            self.database_name = database_name + ".xml"
            self.__initDb(self.database_name)

      def __create_db_file(self, full_name):
            root = et.Element("products")
            tree = et.ElementTree(root)
            tree.write(full_name)

      def __initDb(self, fname):
            #check if xml file exists
            if not os.path.isfile(fname):
                  self.__create_db_file(fname)

      #create xml string from data
      @staticmethod
      def create_xml_string_from_obj(product):
            return f"<product isVIP='{product.isVip}'><name>{product.name}</name><text>{product.text}</text><brand>{product.brand}</brand><cost>{product.cost}</cost></product>"

      def add_Product(self, product):
            newStr = self.__class__.create_xml_string_from_obj(product)
            tree = et.parse(self.database_name)
            root = tree.getroot()
            root.append(et.fromstring(newStr))
            tree.write(self.database_name)

      def get_Products(self):
            tree = et.parse(self.database_name)
            root = tree.getroot()
            p = [Product(prod.find('name').text, prod.find('text').text, prod.find('brand').text, prod.find('cost').text, bool(prod.get('isVip'))) for prod in root]
            return p

      def delete_product(self, obj):
            tree = et.parse(self.database_name)
            root = tree.getroot()
            for elem in root:
                  if(elem.find('name').text == obj.name):
                        root.remove(elem)
            tree.write(self.database_name)
            

            

sdb = storeDatabase("testdb_01")
p1 = Product("testName", "testText", "testBrand", "testCost", True)
p2 = Product("testName2", "testText2", "testBrand2", "testCost2", False)
p3 = Product("testName3", "testText3", "testBrand3", "testCost3", False)
sdb.add_Product(p1)
sdb.add_Product(p2)
sdb.add_Product(p3)
list_of_products = sdb.get_Products()

print(list_of_products)

element_toRemove = list_of_products[2]
print(element_toRemove)

sdb.delete_product(element_toRemove)

list_of_products = sdb.get_Products()
print(list_of_products)

