
#import the regular expression module built in python and use with "re." follow by the regular expression method
import re

#checking if there is a match element
name = "Mandela Thomas"
match_name = re.match("Mandela", name, re.I)


search_name = re.search(r'Mandela', name)
print(search_name)

#using the search and the raw string (r)
programming_lang = "Python, java, perl, r, php, JavaScript, C#, C++"
search_lang = re.search(r"r", programming_lang )
search_lang.group()

#matching all the character in the string
sentence = "Mandela is the ceo of ATSMAS USA and Africa since 2020"

result = re.search(r"\D+", sentence)
result.group()

#searching for none words characters

result = re.search(r"\W+", sentence)
result.group()

#matching with characters at the beginning and end of a string
result = re.search(r"\A", sentence)
result.group()

#matching and transforming case sentence

result = re.findall(r"[A-Z]", sentence) # to upper case
result = re.findall(r"[a-z]", sentence) # to lower case
result = re.findall(r"[abn]", sentence)# show from a, b and n
result = re.findall(r"[^a]", sentence) #include not a match
result = re.findall(r"[0-9]", sentence) # match from 0 to 9
print(result)

#spliting the string
re.split(r" ", sentence)

#using the subn
re.subn(r"\S", "_", sentence)

my_regex_str = '200.10.2.0 255.255.255.0 200.20.5.2 1 205 T#1 S IB 5'

a = re.match(r"255", my_regex_str)
type(a)

a = re.search(r"(.+?) +\d\d(\d)\.([0-9]{2,})\.([0-9]{1,3})\.(\d) +(.+)1 +(\d{3}) +(\w{1})#.+S(\s+)(\w)\w +(.*)", my_regex_str)
a.group(0)

a = re.search(r"(.+?) +\d\d(\d)\.([0-9]{2,})\.([0-9]{1,3})\.(\d) +(.+)1 +(\d{3}) +(\w{1})#.+S(\s+)(\w)\w +(.*)", my_regex_str)
a.group(1)
