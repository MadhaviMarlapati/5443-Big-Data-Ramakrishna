import redis
import string
import json
import sys

def is_json(myjson):
   try:
      json_object = json.loads(myjson)
   except ValueError, e:
      return False
   return True

   
#Link up with redis 
r = redis.Redis(host='localhost', port=6379, db=0)

f = open('../nutrition_clean.json','r')
# Read one line from file
i = 0
for line in f:
    # Filter that line, removing non ascii characters
    # Doesn't identify which, just filters
	if is_json(line):
			i = i + 1
			line = json.loads(filter(lambda x: x in string.printable, line))
			nut =  line['nutrients']
			for jsonline in nut: 
				#print jsonline['_id']
				 r.zincrby('myset',1,jsonline['_id'])
print r.zrange('myset', 0, 5,desc=True)


