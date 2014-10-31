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
writeupfile1 = open("nutirentIdSet.txt", "w")
writeupfile2 = open("nutIdHash.txt", "w")
writeupfile3 = open("nutTagnameSet.txt", "w")
writeupfile4 = open("nutTagnameAsKey_Hash.txt", "w")
writeupfile5 = open("nutIdList_topLevelIdAsKey.txt", "w")
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
				# add nutrient id to set 
				r.sadd('nutIdset', jsonline['_id'])
				# add nutrient id to hash as key 
				r.hset('nutIdHash', jsonline['_id'], jsonline['tagname'])
				# add tagname of nutrients to set 
				r.sadd('nutTagset', jsonline['tagname'])
				# add tagname of nutrient as key to hash
				r.hset('nutTagNameHash', jsonline['tagname'], jsonline['_id'])
				#all nutrient id's in a list 
				r.rpush('nutIdList', jsonline['_id'])
				list = r.lrange('nutIdList',  0 ,-1 )
	#top level id as key and nutrient list as value 
	r.lpush(line['_id'],list)
	# writes list data to file 
	writeupfile5.write(str(r.lrange(line['_id'],0,-1)))
# writes set data to file 	
writeupfile1.write(str(r.smembers('nutIdset')))
# writes hash data to file 
writeupfile2.write(str(r.hgetall('nutIdHash')))
# write set data to file 
writeupfile3.write(str(r.smembers('nutTagset')))
# write hash data to file 
writeupfile4.write(str(r.hgetall('nutTagNameHash')))

# closes the file writer 
writeupfile1.close()
writeupfile2.close()
writeupfile3.close()
writeupfile4.close()
writeupfile5.close()