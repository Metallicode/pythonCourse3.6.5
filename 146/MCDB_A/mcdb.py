from mcdb_collection import MCDBCollection as dbc
from mcdb_encryptor import MCEncryptor as encryptor
import datetime
import logging
import json
import ast
from os import listdir, remove
from os.path import isfile , join
import threading

class MCDB:

      def __init__(self, db_name="", dirPath="collections/", password="ADMIN"):
            logging.basicConfig(level=logging.DEBUG)
            self.set_db_name(db_name)
            self.cryptor = encryptor(password)
            self.dirPath = dirPath
            self.collections = []
            self.sync_memory_collection_to_disk()
            
            logging.debug(f"db created!")



      def sync_memory_collection_to_disk(self):
            allCollections = self.get_all_collections_names()
            for i in allCollections:
                  self.sync_collection(i, syncToMeme=False)
                        


      def get_all_collections_names(self):
            in_memory_collections = [f.name for f in self.collections]
            onlyfiles = [f[:-5] for f in listdir(self.dirPath) if isfile(join(self.dirPath, f))]
            return list(set(onlyfiles+in_memory_collections))


            
      def create_collection(self, collection_name):
            all_collection_names = self.get_all_collections_names()
            if collection_name in all_collection_names:
                  logging.debug(f"collection {collection_name} is in use! try again with different name")
                  return None
            new_col = dbc(collection_name)
            self.collections.append(new_col)
            logging.debug(f"collection {collection_name} created!")
            self.sync_collection(collection_name)
            return new_col



      def insert_collection(self, collection):
            self.collections.append(collection)
            logging.debug(f"new collection {collection.name} inserted to db collections")            


      def delete_collection(self, collection_name):
            col, idx = self.get_collection(collection_name)
            if col is not None:
                  if self.collections[idx] is not None:
                        del self.collections[idx]
                        self.sync_collection(collection_name)
                        logging.debug(f"collection {collection_name} deleted ok!")


                 
      def get_collection(self, collection_name):
            for i in range(len(self.collections)):
                  if self.collections[i].name == collection_name:
                          return self.collections[i], i

            return None, -1



      def get_item(self, collectionName, item_id=None, filterFunc=None):
            self.sync_collection(collectionName)
            collection = self.get_collection(collectionName)[0]
            if item_id is not None:
                  return collection.collection_dict[item_id]
            elif filterFunc is not None:
                  return collection.return_item(filterFunc)

            

      def sync_collection(self, collection_name, syncToMeme=True):
            if syncToMeme:
                  t = threading.Thread(target=self.save_collection_state_to_file, args=(collection_name,))
                  t.start()
                  t.join()
            t2 = threading.Thread(target=self.read_collection_from_file, args=(collection_name,))
            t2.start()
            t2.join()      



      def save_collection_state_to_file(self, collection_name):
            col, idx = self.get_collection(collection_name)

            strList = []

            if col is not None:
                  for k, v in col.collection_dict.items():
                        if type(v) != dict and type(v) != str:
                              strList.append((json.dumps(v.__dict__),k))
                        else:
                              strList.append((json.dumps(v),k))

                  
                  logging.debug(f"writing collection to disk!")
                  with open(f"{self.dirPath}{col.name}.pydb", "wb") as f:
                        col_str = self.cryptor.return_encrypted(json.dumps(strList))
##                        col_str = json.dumps(strList) ###no encryption
                        f.write(col_str.encode())



      def read_collection_from_file(self, collection_name):
            logging.debug(f"reading collection from disk!")
            with open(f"{self.dirPath}{collection_name}.pydb", "rb") as f:
                  col_str = self.cryptor.return_decrypted(f.read())
##                  col_str = f.read() ### no encryption
                  from_json = json.loads(col_str)
                  new_col = dbc(collection_name)
                  for i in from_json:
                        new_col.insert_item(ast.literal_eval(i[0]), i[1])

                  self.delete_collection(collection_name)
                  self.insert_collection(new_col)
                  return new_col


                  
      def set_db_name(self, db_name):
            if db_name is "":
                  db_name = datetime.datetime.now().strftime("%c")
            self.db_name = db_name


      def insert_item(self, collectionName, item):
            self.sync_collection(collectionName)
            collection = self.get_collection(collectionName)[0]
            item_id = collection.insert_item(item)
            self.sync_collection(collectionName)
            return item_id


      def delete_item(self, collectionName, item_id=None, filterFunc=None):
            self.sync_collection(collectionName)
            collection = self.get_collection(collectionName)[0]
            if item_i is not None:
                  msg = collection.delete_item(item_id=item_id)
            elif filterFunc is not None:
                  msg = collection.delete_item(predicate=item_id)
            self.sync_collection(collectionName)
            return msg

      def drop_db(self, delFiles=False):
            logging.debug(f"drop db!")
            for c in self.collections:
                  del c
            self.collections  = []
            if delFiles:
                  logging.debug(f"deleting db files!")
                  fileNames = [self.dirPath+c.name+".pydb" for c in listdir(self.dirPath) if isfile(join(self.dirPath, c))]
                  for c in fileNames:
                        os.remove(c)


                        
