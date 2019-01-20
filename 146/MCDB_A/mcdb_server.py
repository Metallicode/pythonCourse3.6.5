import logging
import socket
import select
import mcdb
import threading
import json
import re
import ast

class MCDBServer:

      mcdb_syntax_actions = ["GET", "CREATE", "DELETE", "INSERT", "DROP"]
      
      def __init__(self, addr="192.168.1.14",port=666, dbName="default", passwd="ADMIN"):
            FORMAT = '%(module)s   >>>   %(message)s'
            logging.basicConfig(level=logging.DEBUG, format=FORMAT)
            
            logging.debug(f"creating MCDBServer on {addr} {port}")
            
            self.regx_pattern = re.compile(r"\{.+\}")
            self.database = mcdb.MCDB(password= passwd)      
            self.soc = socket.socket()
            self.port = port
            self.soc.bind((addr, port))
            self.start_server()
            

      def start_server(self):
            logging.debug(f"starting server...")
            self.serverStop = False
            self.soc.listen(5)
            self.service_loop()
            

      def stop_server(self):
            logging.debug(f"stop_server")
            self.serverStop = True


      def service_loop(self):
            inputs = [self.soc]
            logging.debug(f"starting server loop")              
            while inputs and not self.serverStop:
                  readables, _, _ = select.select(inputs, [], [])
                  for i in readables:
                        if i is self.soc:
                              client, address = self.soc.accept()
                              inputs.append(client)
                              logging.debug(f"connected to new client {client}")
                              client.send(b"Hello from MCDB Server")

                        else:
                              try:
                                    data = i.recv(1024)
                                    logging.debug(f"got message from client {data.decode()} \t<----- NEW MSG")
                                    t = threading.Thread(target=self.digest_message, args=(data.decode(),i))
                                    t.start()
                                    
                              except Exception as e:
                                    logging.debug(f"error = {e}")
                                    inputs.remove(i)
                                    i.close()
                                    
            logging.debug(f"server loop exit...")

      @staticmethod
      def filter_maker(attr_name, attr_val):
            def inner_func(x):
                  return x[attr_name] == attr_val
            return inner_func


      def digest_message(self, msg, client):
            logging.debug(f"digesting message....{msg}")
            messageItems = msg.split()
            if messageItems[0]=="INSERT":
                  dict_location = self.regx_pattern.search(msg).span()
                  messageItems = [messageItems[0], msg[dict_location[0]: dict_location[1]] ,messageItems[-2],messageItems[-1]]
            self.action_switch(messageItems, client)


      def action_switch(self, action, client):
            logging.debug(f"action_switch ON {action}")
            
            if action[0] not in MCDBServer.mcdb_syntax_actions:
                  logging.warning(f"problem with syntax action")
                  self.response("syntax error", client)

                  
            else:
                  if action[0] == "GET":
                        logging.debug(f"GET call")
                        if action[1] != "?":
                              item = self.database.get_item(collectionName=action[3], item_id=int(action[1]))
                        else:
                              filterF = MCDBServer.filter_maker(action[5],action[6])
                              item = self.database.get_item(collectionName=action[3], filterFunc=filterF)                    
                        logging.debug(f"ok get item {item}")
                        self.response(item, client)

            
                  elif action[0] == "CREATE":
                        logging.debug(f"CREATE action call")                     
                        new_col = self.database.create_collection(action[1])
                        if new_col is not None:
                              self.response(f"collection {new_col.name} created!", client)
                        else:
                              self.response(f"collection {action[1]} not created! change name...", client)

     
                  elif action[0] == "DELETE":
                        logging.debug(f"DELETE action call")
                        if action[1] == "ITEM":
                              logging.debug(f"DELETE ITEM call")
                              if action[2] == "?":
                                    filterFunc = MCDBServer.filter_maker(action[6],action[7])
                                    res_msg = self.database.delete_item(collectionName=action[4],predicate=filterFunc)
                              else:
                                    res_msg = self.database.delete_item(collectionName=action[4], item_id=action[2])
                              self.response(res_msg, client)
                              
                        elif action[1] == "COLLECTION": 
                              logging.debug(f"DELETE COLLECTION call")
                              self.database.delete_collection(action[2])
                              self.response(f"collection {action[2]} deleted ok", client)


            
                  elif action[0] == "INSERT":
                        logging.debug(f"INSERT action call")
                        new_item_as_dict = ast.literal_eval(action[1])
                        item_id = self.database.insert_item(action[3], new_item_as_dict)
                        self.response(item_id, client)


                        
                  elif action[0] == "DROP":
                        logging.debug(f"DROP action call")
                        self.database.drop_db(delFiles=True)
                        self.response("db destroyed!", client)

      def response(self, data, client):
            client.send(json.dumps(data).encode())
            

if __name__ == "__main__":
      p= input("enter your password>>>")
      import os
      os.system('cls' if os.name == 'nt' else 'clear')
      mcserver = MCDBServer(passwd=p)
