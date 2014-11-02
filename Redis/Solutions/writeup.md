# 1 What are the number of unique food "items" in the file ? 

r.hset('UniqueItems', line['_id'], line['foodGroup'])
print r.hgetall('UniqueItems')

I have to count the  unique top level  id's. hset is used and key as id .
 Then r.hgetall gives the number of unique food "items" in the file.


 
 Output:

Unique items: 8194

 
# 2 How many unique nutrients are there?

~~~
for line in f:
    # Filter that line, removing non ascii characters
    # Doesn't identify which, just filters
	if is_json(line):
			i = i + 1
			line = json.loads(filter(lambda x: x in string.printable, line))
			nut =  line['nutrients']
			for jsonline in nut: 
				#print jsonline
				r.hset('nut', jsonline['_id'], jsonline['tagname'])
print r.hgetall('nut')

~~~


In the inner loop where iterating nutrients ,  id 's of nutrients are 
stored into hashset as key. Then r.hgetall gives unique nutrient nutrients.



Output:

Unique nutrients: 148


# 3 What are the top 5 most commonly occuring nutrient? 

~~~

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

~~~ 

Output:

Id's of the nutrients most occured 
['1', '208', '205', '204', '203']

1. 1 
2. 208  
3. 205
4. 204
5. 203 


In the inner loop where iterating each nutrient ,
 r.zincrby increments the  count of the id.(Indirectly it is counting the number of times id is repeated).
 r.zrange('myset', 0, 5,desc=True) gives the top 5 most commonly occuring nutrients.
 
 
# 4 

 I tried to print the output on console. 

# 5
~~~
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
	r.lpush(line['_id'],list
~~~ 
In the inner loop where i iterated the nutrients i added 
tags and id's to the set , hash , list as discussed below . 

I wrote the data to different files using the command like  
 open("nutirentIdSet.txt", "w") . And "w" means it data will be written to the specified file . 
 For Each sub part in this question 5  i created a seperate file . 

#### 5.1    r.sadd('nutIdset', jsonline['_id']) 
		 stores  all id's for nutrients in a set and r.smembers gives the values in set. 

#### 5.2    r.hset('nutIdHash', jsonline['_id'], jsonline['tagname'])
		stores all nutrients in a hash with thier id's as keys and r.hgetall gives 
		all the fields and values in a hash 
				
#### 5.3    r.sadd('nutTagset', jsonline['tagname']) 
		stores all tagnames in a set and r.smembers gives the values in set and 
		r.hgetall gives all the fields and values in a hash 


#### 5.4    r.hset('nutTagNameHash', jsonline['tagname'], jsonline['_id'])
		stores all nutrients in a hash with tagnames as keys and 
		r.hgetall gives all the fields and values in a hash 

#### 5.5    Store all nutrient id's in a list with the item id (top level _id) as the key.
	~~~
	#all nutrient id's in a list 
				r.rpush('nutIdList', jsonline['_id'])
				list = r.lrange('nutIdList',  0 ,-1 )
	#top level id as key and nutrient list as value 
	r.lpush(line['_id'],list
	~~~
	r.rpush add the nutrient id's to the lise . r.lrange returns the nutrient id's list. 
	r.lpush push add the list to the top level id  where top level id of the food item is the key. 
	
	
