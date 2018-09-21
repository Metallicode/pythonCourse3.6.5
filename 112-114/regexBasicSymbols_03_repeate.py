##                   . ^ $ * + ? { } [ ] \ | ( )

import re

textStr = """Being able to match varying sets of chars is the first thing regular 
expressions 050-2222222 can do that isn’t bat already possible cat xa with the Cat methods available on strings. 
However, if that was the only additional bob@gmail.com batat ct of regexes, they  wouldn’t be much of an advance. 
Another is that xc you caet can specify that caaat 050-050 xb portions caaaaat of the $RE 
must be repeated a # 0503333333 (certain) number caaaaaaat  of times, Be Cool."""

#Repeating Things

#literal
#pattern = re.compile(r"cat")

#zero or more times
#pattern = re.compile(r"ca*t")


#one or more times
#pattern = re.compile(r"ca+t")


#one or zero times
#pattern = re.compile(r"ca?t")


#at least m repetitions, and at most n.
#pattern = re.compile(r"ca{3,5}t")


#greed
#pattern = re.compile(r"b[a-z]*t")
#pattern = re.compile(r"b[a-z]*?t")





#preform search in text
matches = pattern.finditer(textStr)
for i in matches:
      print(i)


