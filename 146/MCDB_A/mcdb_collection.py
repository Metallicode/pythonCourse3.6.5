import datetime
import logging

class MCDBCollection:



      def __init__(self, name=""):
            logging.basicConfig(level=logging.DEBUG)
            logging.debug(f"creating collection with name: {name}")
            self.set_collection_name(name)
            self.collection_dict = {}



      def set_collection_name(self, name):       
            if name=="":
                  self.__name = datetime.datetime.now().strftime("%c")
            else:
                  self.__name = name
            logging.debug(f"set_collection_name call to {self.__name}")



      @property
      def name(self):
            logging.debug(f"get name property {self.__name}")
            return self.__name



      def insert_item(self, obj, uid=-1):          
            if uid==-1:
                  item_id = self.create_uniqe_item_id(obj)
            else:
                  item_id=uid
            self.collection_dict[item_id] = obj
            logging.debug(f"inserted item with id: {item_id}")
            return item_id



      def check_if_id_in_collection(self, item_id):
            in_collection =  item_id in self.collection_dict.keys()
            logging.debug(f"id {item_id} is in collection? : {in_collection}")
            return in_collection


            
      def return_item(self, predicate):
            logging.debug(f"filtering on predicate: {predicate}")
            return list(filter(predicate, self.collection_dict.values()))



      def get_id_from_item(self, item):
            logging.debug(f"get_id_from_item: {item}")
            for i in self.collection_dict.keys():
                  if self.collection_dict[i] == item:
                        return i
            return None



      def return_all(self):
            logging.debug(f"return_all from collection {self.__name}")
            return self.collection_dict



      def delete_item(self, item_id=None, predicate=None):
            if item_id is not None:
                  if item_id in self.collection_dict.keys():
                        logging.debug(f"deleting {item_id}")
                        del self.collection_dict[item_id]
                        return "item deleted ok"
            if predicate is not None:
                  items_deleted_counter = 0
                  items_to_del = list(filter(predicate, self.collection_dict.values()))
                  items_to_del_keys = []
                  for k, v in self.collection_dict.items():
                        if v in items_to_del:
                              items_to_del_keys.append(k)
                  for i in items_to_del_keys:
                        del self.collection_dict[i]
                        items_deleted_counter += 1
                  return f"{items_deleted_counter} items deleted ok"



      def drop_collection(self):
            del self.collection_dict
            del self
            logging.debug(f"collection Destroyed ")



      def create_uniqe_item_id(self, obj):
            logging.debug(f"calculating unique id..")
            while True:
                  new_id = hash(str(id(obj)) + str(datetime.datetime.now()))
                  if not self.check_if_id_in_collection(new_id):
                        logging.debug(f"unique id found!")
                        break         
            return new_id
