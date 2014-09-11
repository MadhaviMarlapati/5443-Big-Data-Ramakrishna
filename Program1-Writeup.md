# I would like to convert yaml to json 


### YAML To JSON : 


Technically YAML is a superset of JSON. This means that, in theory at least, a YAML parser can understand JSON, but not necessarily the other way around.

In general, there are certain features have  YAML that are not available in JSON.

As @jdupont pointed out, YAML is visually easier to look at. In fact the YAML homepage is itself valid YAML, yet it is easy for a human to read.
YAML has the ability to reference other items within a YAML file using "anchors." Thus it can handle relational information as one might find in a MySQL database.
YAML is more robust about embedding other serialization formats such as JSON or XML within a YAML file.
Right now, AJAX and other web technologies tend to use JSON. YAML is currently being used more for offline data processes.




# I would like to convert   yaml to json using python 


Because Python is an easy to use language which has awesome libraries that work very well . 
And   yml is light-weight and well-suited for hierarchical data representation, it also has a compact syntax for relational data

in general, a JSON expression is going to be 30% smaller than "equivalent" XML. 




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






# File Types & Importance  

JSON has the advantage of super-easy parsing in JavaScript, though you'll probably have to find and introduce a library in other languages.

XML has the advantage of more common usage across languages, useful for the storage you mention; and also valuable for passing around through different systems.

YAML has libraries for all languages, but is somewhat less commonly used, so you are more likely to have to find and introduce a library; whereas XML libraries are more commonly bundled, and JSON is automatically parseable in JavaScript.

For small, lightweight apps author  personally think XML is overkill , author  says that he  prefer YAML in that case. If you truly need to define your own grammar (read: schema) then xml is it.

Reference : http://stackoverflow.com/questions/3951047/xml-vs-yaml-vs-json?rq=1



# which of the files compresses the best using zip 

Some types of files compress better than others. Some data files, such as text files, picture files in the BMP format, and certain text style database files can often be compressed by 90% or more. There are some other types of files, such as program files, that may compress by 50% or so.

Other types of files often will not compress well. For example, most multimedia files will not, as they already exist in a highly compressed state.


# which of the files compresses the best using gzip

Gzip reduces the size of the named files using Lempel-Ziv coding (LZ77). Whenever possible, each file is replaced by one with the extension .gz, while keeping the same ownership modes, access and modification times. (The default extension is -gz for VMS, z for MSDOS, OS/2 FAT, Windows NT FAT and Atari.) If no files are specified, or if a file name is "-", the standard input is compressed to the standard output. Gzip will only attempt to compress regular files.






