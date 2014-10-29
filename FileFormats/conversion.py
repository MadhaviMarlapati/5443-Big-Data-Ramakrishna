import redis
import string
import yaml
import sys

   

f = open('./GpsFilePoints.yml','r')
# Read one line from file
i = 0
for line in f:
    # Filter that line, removing non ascii characters
    # Doesn't identify which, just filters
	
			i = i + 1
			line = yaml.load(filter(lambda x: x in string.printable, line))
			json = json.dumps(line)
			print json