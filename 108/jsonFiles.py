import json

##
##jsonString = """
##{
##"ppl" : [
##      {
##            "name":"bob",
##            "age":23
##      },
##      {
##            "name":"bill",
##            "age":41
##      },
##      {
##            "name":"tom",
##            "age":35
##      }]
##}
##"""
##
##json_data = json.loads(jsonString)
##
##print(json_data)
##print(json_data["ppl"])
##
##for p in json_data["ppl"]:
##      print(f"{p['name']}   {p['age']}")
##
##json_data["ppl"].append(dict(name="john", age=99))
##print(json_data)
##
##
##jsonString = json.dumps(json_data)
##json_data = json.loads(jsonString)
##
##for p in json_data["ppl"]:
##      print(f"{p['name']}   {p['age']}")


##
##with open("basicJson.json", "r") as f:
##      json_data = json.load(f)

##print(type(json_data["key_07"]))

##newData = {'newKey2' : 'newData2', 'newKey3' : 5, 'newKey4' : 5.5, 'newKey5' : None }
##json_data.update(newData)
##
##with open("basicJson.json", "w") as f:
##      json.dump(json_data, f,indent=4 )

##json_data['newKey123'] = "this is a new value"

##del json_data['newKey']
##
##
##with open("basicJson.json", "w") as f:
##      json.dump(json_data, f,indent=4 )
