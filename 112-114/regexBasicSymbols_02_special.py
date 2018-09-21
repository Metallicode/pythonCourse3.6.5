##                   . ^ $ * + ? { } [ ] \ | ( )

import re

textStr = """Being able to match varying sets of chars is the first thing regular 
expressions 050-2222222 can do that isn’t bat already possibl BkaB cat xa with the Cat methods available on strings. 
However, if that was the only additional bob@gmail.com batat ct of regexes, they  wouldn’t be much of an advance. 
Another is that xc you caet can specBify that caaat 050-050 xb portions caaaaat of the $RE 
must be repeated a # 0503333333 (certain) number caaaaaaat  of times, Be Cool."""

#special sequences
"""\d    \D    \s    \S    \w    \W    """

#any decimal digit. same as [0-9]
#pattern = re.compile(r"\d")

#any non-digit. same as [^0-9]
#pattern = re.compile(r"\D")


#any whitespace character. same as [ \t\n\r\f\v]
#pattern = re.compile(r"\s")

#any non whitespace character. same as [^ \t\n\r\f\v]
#pattern = re.compile(r"\S")


#any alphanumeric character. same as [a-zA-Z0-9_]
#pattern = re.compile(r"\w")

#any non-alphanumeric character. same as [a-zA-Z0-9_]
#pattern = re.compile(r"\W")



#More Metacharacters
"""\A    \Z    \b    \B"""

#only at the start of the string
#pattern = re.compile(r"B")
#pattern = re.compile(r"\AB")

#(same as)
#pattern = re.compile(r"^B")


#only at the end of the string
#pattern = re.compile(r"l")
#pattern = re.compile(r"l\Z")

#(same as)
#pattern = re.compile(r"B$")

#only at the start or/and end of a word
#pattern = re.compile(r"B")
#pattern = re.compile(r"\bB")
#pattern = re.compile(r"B\b")


#not in begining of a word
#pattern = re.compile(r"\BB")
#not in end of a word
#pattern = re.compile(r"B\B")

#inside a word
#pattern = re.compile(r"\BB\B")

# or operator
#pattern = re.compile(r"x(a|b|c)")

#preform search in text
matches = pattern.finditer(textStr)
for i in matches:
      print(i)


