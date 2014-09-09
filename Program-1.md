csv to json python    :  

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
	
	
	http://stackoverflow.com/questions/19697846/python-csv-to-json
	
	
2 )  

http://jaranto.blogspot.com/2012/12/transform-csv-file-to-json-file-with.html


3 ) 

http://ntare16.wordpress.com/2012/01/26/python-code-to-convert-csv-to-json/ 

Java 

1 ) http://www.studytrails.com/java/json/java-org-json.jsp  





sql to json 




python 

http://stackoverflow.com/questions/10839475/convert-sql-into-json-in-python


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






