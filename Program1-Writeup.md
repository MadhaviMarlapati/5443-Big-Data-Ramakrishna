# File Types & Importance  

JSON has the advantage of super-easy parsing in JavaScript, though you'll probably have to find and introduce a library in other languages.

XML has the advantage of more common usage across languages, useful for the storage you mention; and also valuable for passing around through different systems.

YAML has libraries for all languages, but is somewhat less commonly used, so you are more likely to have to find and introduce a library; whereas XML libraries are more commonly bundled, and JSON is automatically parseable in JavaScript.

For small, lightweight apps author  personally think XML is overkill , author says that he  prefer YAML in that case. for interaction with javascript use json. If you truly need to define your own grammar (read: schema) then xml is it.

Reference : http://stackoverflow.com/questions/3951047/xml-vs-yaml-vs-json?rq=1

# Why Python &  yaml to json 
I would like to choose python.I would like to  convert yml to json .
Because Python is an easy to use language which has awesome libraries that work very well . 
And   yml is light-weight and well-suited for hierarchical data representation, it also has a compact syntax for relational data

in general, a JSON expression is going to be 30% smaller than "equivalent" XML. 



### YAML To JSON : 


Technically YAML is a superset of JSON. This means that, in theory at least, a YAML parser can understand JSON, but not necessarily the other way around.

In general, there are certain features have  YAML that are not available in JSON.

As @jdupont pointed out, YAML is visually easier to look at. In fact the YAML homepage is itself valid YAML, yet it is easy for a human to read.
YAML has the ability to reference other items within a YAML file using "anchors." Thus it can handle relational information as one might find in a MySQL database.
YAML is more robust about embedding other serialization formats such as JSON or XML within a YAML file.
Right now, AJAX and other web technologies tend to use JSON. YAML is currently being used more for offline data processes.




### YAML To JSON Using python  : 

~~~
import yaml
import json
 
yml = """
---
  foo: bar
"""
data = yaml.load(yml)
json = json.dumps(data)
 
print(json)
~~~



###csv to json using  python    :  

~~~
 
import csv
import json

csvfile = open('file.csv', 'r')
jsonfile = open('file.json', 'w')

fieldnames = ("FirstName","LastName","IDNumber","Message")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')

Reference : 

	http://stackoverflow.com/questions/19697846/python-csv-to-json
	
	
~~~



### sql to json  using python 


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


Reference : 
http://jugad2.blogspot.com/2014/03/database-to-json-in-python.html

~~~



### sql to json  using php 
~~~

$result = mysql_query(your sql here);    
$data = array();
while ($row = mysql_fetch_assoc($result)) {
    // Generate the output in desired format
    $data = array(
        'cols' => ....
        'rows' => ....
        'p' => ...
    );
}

$json_data = json_encode($data);
file_put_contents('your_json_file.json', $json_data);

Reference : 

http://stackoverflow.com/questions/17317519/php-mysql-data-to-json-file

~~~

### xml to json  using php : 

~~~

<?php   
class XmlToJson {
    public function Parse ($url) {
        $fileContents= file_get_contents($url);
        $fileContents = str_replace(array("\n", "\r", "\t"), '', $fileContents);
        $fileContents = trim(str_replace('"', "'", $fileContents));
        $simpleXml = simplexml_load_string($fileContents);
        $json = json_encode($simpleXml);

        return $json;
    }
}
?>


Reference : http://stackoverflow.com/questions/8830599/php-convert-xml-to-json

~~~

### xml to json using python : 

https://github.com/hay/xml2json/blob/master/xml2json.py


# which of the files compresses the best using zip 

Some types of files compress better than others. Some data files, such as text files, picture files in the BMP format, and certain text style database files can often be compressed by 90% or more. There are some other types of files, such as program files, that may compress by 50% or so.

Other types of files often will not compress well. For example, most multimedia files will not, as they already exist in a highly compressed state.


# which of the files compresses the best using gzip

Gzip reduces the size of the named files using Lempel-Ziv coding (LZ77). Whenever possible, each file is replaced by one with the extension .gz, while keeping the same ownership modes, access and modification times. (The default extension is -gz for VMS, z for MSDOS, OS/2 FAT, Windows NT FAT and Atari.) If no files are specified, or if a file name is "-", the standard input is compressed to the standard output. Gzip will only attempt to compress regular files.






