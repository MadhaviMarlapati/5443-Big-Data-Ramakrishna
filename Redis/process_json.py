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

f = open('./nutrition.json','r')
file = open("nutrition_clean.json", "w")
writeupfile = open("writeup.md", "w")
# Read one line from file
i = 0
j = 0
k = 0


for line in f:
    # Filter that line, removing non ascii characters
    # Doesn't identify which, just filters
	k = k+1
	if is_json(line):
				i = i + 1
				line = json.loads(filter(lambda x: x in string.printable, line))
				file.write(str(line))
	else : 
				j = j+1
print 'GoodLines    '+ str(i)
print j

writeupfile.write('### Json File Processing\n')
writeupfile.write('### Written by Your Name\n')
writeupfile.write('- Total Lines Processed:'+str(k)+'\n')
writeupfile.write('GoodLines    '+ str(i)+'\n')
writeupfile.write('BadLines    '+ str(j))
f.close()
writeupfile.close()
file.close()

		