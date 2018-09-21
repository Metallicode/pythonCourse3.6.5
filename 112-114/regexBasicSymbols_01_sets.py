##                   . ^ $ * + ? { } [ ] \ | ( )

import re

textStr = """Being able to match varying sets of chars is the first thing regular 
expressions 050-2222222 can do that isn’t bat already possible cat xa with the Cat methods available on strings. 
However, if that was the only additional bob@gmail.com batat ct of regexes, they  wouldn’t be much of an advance. 
Another is that xc you caet can specify that caaat 050-050 xb portions caaaaat of the $RE 
must be repeated a # 0503333333 (certain) number caaaaaaat  of times, Be Cool."""

#literal
#pattern = re.compile(r"is")


#[ ] character class, which is a set of characters
#pattern = re.compile(r"[B]")
#pattern = re.compile(r"[BHA]")

#range
#pattern = re.compile(r"[c-h]")
#pattern = re.compile(r"[0-9]")

#no metacharacter
#pattern = re.compile(r"[.$()]")

#'^' as the first character of the class; '^' outside a [] will match'^' .
#pattern = re.compile(r"[^a-x]")

#any any character
#pattern = re.compile(r".[R].")


#preform search in text
matches = pattern.finditer(textStr)
for i in matches:
      print(i)


