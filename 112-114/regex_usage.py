import re

pat = re.compile(r"(\S+)@(\S+)(\.)\S{3}")

with open("text.txt", "r") as f:
      text = f.read()
      print(text)

#get first location of a match obj 
res = pat.search(text)
print(res)

###match to specipic begining of a string (or slice)
##pat = re.compile(r"\d+-\d+")
##print(text[87:150])
##print(pat.match(text))
##print(pat.match(text[87:150]))

##match to specipic string (or slice) - but only if its a perfect match, no tail
##pat = re.compile(r"\d+-\d+")
##print(text[87:98])
##print(pat.fullmatch(text))
##print(pat.fullmatch(text[87:150]))
##print(pat.fullmatch(text[87:98]))

###split string to list with a pattern
##pat = re.compile(r"\s")
##pat = re.compile(r"\bw")
##splt = pat.split(text)
##print(splt)

###find all words starting with "m" (returns the matched strings)
##pat = re.compile(r"\bm+\w+", re.IGNORECASE)
##res = pat.findall(text)
##for i in res:
##      print(i)
      
#return results iterable
##res = prog.finditer(text)
##for i in res:
##      print(i)






#### match obj
##with open("numbers.txt", "r") as f:
##      text = f.read()
##patr = re.compile(r"\b(050)(-)(\d+)")
##res = patr.finditer(text)
##matchObj = next(res)
##print(matchObj)
##print(matchObj.group(1))
##print(matchObj.group(2))
##print(matchObj.group(3))
###print(matchObj.group(4))
##print(matchObj.group(0))

#indexd ok
##print(matchObj[0])
##print(matchObj[1])
##print(matchObj[2])
##print(matchObj[3])

#get groups tuple
##print(matchObj.groups())

#named groups and dicts
##patr = re.compile(r"\b(?P<kidomet>050)(-)(?P<Mispar>\d+)")
##res = patr.finditer(text)
##matchObj = next(res)
##print(matchObj.groupdict())


      

with open("names.txt", "r") as f:
      text = f.read()

#not if koko is after dodo
##pat = re.compile(r"dodo (?!koko)")
##match = pat.finditer(text)
##for i in match:
##      print(i)


#if dodo comes after koko
##pat = re.compile(r"(?<=koko\W)dodo")
##match = pat.finditer(text)
##for i in match:
##      print(i)



#if dodo NOT comes after koko
##pat = re.compile(r"(?<!koko\W)dodo")
##match = pat.finditer(text)
##for i in match:
##      print(i)



#greed
##htmlStr = """
##<div><h1>Hello this is title</h1></div>
##"""
##
##pet = re.compile(r"<.*>")
##res = pet.search(htmlStr)
##print(res)
##
##
##pet = re.compile(r"<.*?>")
##res = pet.search(htmlStr)
##print(res)


