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
# read data  from file 
f = open('./nutrition.json','r')
# write data to file 
file = open("nutrition_clean.json", "w")
writeupfile = open("writeup.md", "w")
# Read one line from file
i = 0 # TO Count good line 
j = 0 # TO Count bad line 
k = 0 # TO Count total  line 


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
print k
print i*j/100

writeupfile.write('### Json File Processing\n')
writeupfile.write('### Written by Your Name\n')
writeupfile.write('- Total Lines Processed:  '+str(k)+'\n')
writeupfile.write('- Good Lines Processed:   '+str(i)+'\n')
writeupfile.write('- Bad Lines Processed:    '+str(j)+'\n')
writeupfile.write('- Ratio of  Good Vs Bad   '+str((i*j)/100)+'\n')
f.close()
writeupfile.close()
file.close()

		