#Keys are unique
#key indexed
#changeable

dictionary_a = {1:"bill", 2:"john", 3:"james", 4:"bob"}
print(dictionary_a)
print(dictionary_a[1])
print(dictionary_a[2])

dictionary_b = {"bob": "050123456", "bill": "038667674", "momo":"054123654"}
print(dictionary_b["bob"])
print(dictionary_b["bill"])
print(dictionary_b["momo"])

#dict function
newDict = dict(first="01_element",sec="02_element",third="03_element")
print(newDict)
print(newDict["first"])
print(newDict["sec"])
print(newDict["third"])

print("\n")

#delete item
del newDict["first"]
print(newDict)
print("\n")

#add item
newDict["new_item"] = "a value"
print(newDict)
print("\n")

#get all keys/values
print(newDict.keys())
print(newDict.values())
print("\n")

#get all items (key/value pairs)
print(newDict.items())

##x = newDict.items()
##lst = list(x)
##print(type(lst[0]))
##print(type(x))
print("\n")


#looping
for i in newDict.keys():
      print(newDict[i])

print("\n")

#clear
newDict.clear()
print(newDict)
#print("\n")
#del newDict
print("\n")

#create from keys
newDict = dict.fromkeys(("key01","key02","key03","key04"))
print(newDict)
newDict02 = dict.fromkeys(("key01","key02","key03","key04"), 999)
print(newDict02)
print("\n")

#get
print(newDict02.get("key01"))
print(newDict02.get("key50", "no value"))
print("\n")

#has_key ->
print("key01" in newDict02)
print("donky" in newDict02)
print("\n")

#set Default
print(newDict02)
print(newDict02.setdefault("key01", "bob"))
print(newDict02.setdefault("key50", "bob"))
print(newDict02["key50"])
print(newDict02)


