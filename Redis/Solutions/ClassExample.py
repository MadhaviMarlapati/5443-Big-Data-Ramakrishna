import redis
import string
import json
import sys

#Link up with redis 
r = redis.StrictRedis(host='localhost', port=6379, db=0)

# Open file for reading
#f = open('nutrition.json', 'r')
f = open('nutrition.json','r')
# Read one line from file

for line in f:
    # Filter that line, removing non ascii characters
    # Doesn't identify which, just filters
    line = json.loads(filter(lambda x: x in string.printable, line))

    #line is a dictionary with multiple keys, in this case we just
    #want to loop through the 'nutrient' portion
    for nut in line['nutrients']:
        #Set values in a hash with 'key' = '_id'
        r.hmset(nut['_id'],nut)
        #Push that hash onto a list with 'key' = 'tagname'
        r.rpush(nut['tagname'],nut)