
~~~ 

csv to json python    :  
~~~ 
~~~
1 ) 
import csv
import json

csvfile = open('file.csv', 'r')
jsonfile = open('file.json', 'w')

fieldnames = ("FirstName","LastName","IDNumber","Message")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')
~~~	
Reference : 

	http://stackoverflow.com/questions/19697846/python-csv-to-json
	
	
~~~

sql to json 

~~~ 
python 
~~~ 

# DBtoJSON.py
# Author: Vasudev Ram - http://www.dancingbison.com
# Copyright 2014 Vasudev Ram
# DBtoJSON.py is a program to DEMOnstrate how to read 
# SQLite database data and convert it to JSON.

import sys
import sqlite3
import json

try:

    conn = sqlite3.connect('example.db')

    # This enables column access by name: row['column_name']
    conn.row_factory = sqlite3.Row

    curs = conn.cursor()

    # Create table.
    curs.execute('''DROP TABLE IF EXISTS stocks''')
    curs.execute('''CREATE TABLE stocks
                 (date text, trans text, symbol text, qty real, price real)''')

    # Insert a few rows of data.
    curs.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.0)")
    curs.execute("INSERT INTO stocks VALUES ('2007-02-06','SELL','ORCL',200,25.1)")
    curs.execute("INSERT INTO stocks VALUES ('2008-03-06','HOLD','IBM',200,45.2)")

    # Commit the inserted rows.
    conn.commit()

    # Now fetch back the inserted data and write it to JSON.
    curs.execute("SELECT * FROM stocks")
    recs = curs.fetchall()

    print "DB data as a list with a dict per DB record:"
    rows = [ dict(rec) for rec in recs ]
    print rows

    print

    print "DB data as a single JSON string:"
    rows_json = json.dumps(rows)
    print rows_json

except Exception, e:
    print "ERROR: Caught exception: " + repr(e)
    raise e
    sys.exit(1)

# EOF
The program is self-contained; you don't even need to set up a database and a table and populate it beforehand; the code does that. You just run:
python DBtoJSON.py
And here is its output:
DB data as a list with a dict per DB record:
[{'date': u'2006-01-05', 'symbol': u'RHAT', 'trans': u'BUY', 'price': 35.0, 'qty
': 100.0}, {'date': u'2007-02-06', 'symbol': u'ORCL', 'trans': u'SELL', 'price':
 25.1, 'qty': 200.0}, {'date': u'2008-03-06', 'symbol': u'IBM', 'trans': u'HOLD'
, 'price': 45.2, 'qty': 200.0}]

DB data as a single JSON string:
[{"date": "2006-01-05", "symbol": "RHAT", "trans": "BUY", "price": 35.0, "qty":
100.0}, {"date": "2007-02-06", "symbol": "ORCL", "trans": "SELL", "price": 25.1,
 "qty": 200.0}, {"date": "2008-03-06", "symbol": "IBM", "trans": "HOLD", "price"
: 45.2, "qty": 200.0}]
~~~

Reference : 
http://jugad2.blogspot.com/2014/03/database-to-json-in-python.html


php  


http://stackoverflow.com/questions/17317519/php-mysql-data-to-json-file



xml to json 

php : 

http://stackoverflow.com/questions/8830599/php-convert-xml-to-json
http://lostechies.com/seanbiefeld/2011/10/21/simple-xml-to-json-with-php/  


http://www.ibm.com/developerworks/library/x-xml2jsonphp/


perl : 

http://services.packetizer.com/code/xml2json/xml2json
http://www.packetizer.com/xml/xml_to_json.html


python : 

https://github.com/hay/xml2json




in general, a JSON expression is going to be 30% smaller than "equivalent" XML. 






