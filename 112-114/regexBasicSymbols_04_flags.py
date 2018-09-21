##                   . ^ $ * + ? { } [ ] \ | ( )

import re

textStr = """Being able to match varying sets of chars is the first thing regular 
expressions 050-2222222 can do that isn’t bat already possible cat xa with the Cat methods available on strings. 
However, if that was the only additional bob@gmail.com batat ct of regexes, they  wouldn’t be much of an advance. 
Another is that xc you caet can specify that caaat 050-050 xb portions caaaaat of the $RE 
must be repeated a # 0503333333 (certain) number caaaaaaat  of times, Be Cool."""


#case-insensitive flag
#pattern = re.compile(r"cat", re.IGNORECASE)


#MULTILINE
#pattern = re.compile(r"^H", re.MULTILINE)

#. any character at all, including a newline
#pattern = re.compile(r".", re.DOTALL)

#VERBOSE
##pattern = re.compile(r"""
##\d+         #kidomet
##[-._]?       #seperator
##\d{7}       #number
##""", re.VERBOSE)


#preform search in text
matches = pattern.finditer(textStr)
for i in matches:
      print(i)


