
"""
is a language-independent data format for storing and exchanging data.
 It is a text-based format and it can easily be sent to and from a
 server, and used as a data format by any programming language.
 """
#covert json to python

#import the json module
import json

print("Convert Json To Python")

#json data
myjson_data = '{"Toyota": 2024, "BMW": 2023, "ford": 2019}'

data = json.loads(myjson_data)

print(data)


#convert python to json
print("Convert Python To Json")
mypython_data = {
     "Toyota": 2024,
     "BMW": 2023,
     "ford": 2019
     }
mydata = json.dumps(mypython_data)
print(mydata)
#write and read json file

with open('json.txt', 'w') as json_file:
  json.dump(mypython_data, json_file)

print("Read from the created and write to json file")
my_json = open("json.txt", 'r')
print(my_json.readlines())
