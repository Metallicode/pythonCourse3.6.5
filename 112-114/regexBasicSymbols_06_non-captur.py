##                   . ^ $ * + ? { } [ ] \ | ( )

import re

textStr = """Being able to match varying sets of chars is the first thing regular 
expressions 050-2222222 can do that isn’t bat already possible cat xa with the Cat methods available on strings. 
However, if that was the only additional bob@gmail.com batat ct of regexes, they  wouldn’t be much of an advance. 
Another is that xc you caet can specify that caaat 050-050 xb portions caaaaat of the $RE 
must be repeated a # 0503333333 (certain) number caaaaaaat  of times, Be Cool."""

#only if pattern is followed by 
#pattern = re.compile(r"can (?=do)")

#only if pattern is not followed by 
#pattern = re.compile(r"can (?!do)")

#only if preceded by a match
#pattern = re.compile(r"(?<=can) do")

#only if not preceded by a match
#pattern = re.compile(r"(?<!can) do")


#preform search in text
matches = pattern.finditer(textStr)
for i in matches:
      print(i)


