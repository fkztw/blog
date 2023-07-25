Title: Convert HTML string to XML string with Python  
Slug: convert-html-string-to-xml-string-with-python  
Date: 2016-08-28 00:47:20  
Authors: fkz  
Category: Note  
Tags: Python, Python 2, Python 3, HTML, XML  
Summary: Just 3 lines of code in both Python 2 and Python 3.  
  
  
## Python 2  
  
```Python2  
from HTMLParser import HTMLParser  
from xml.sax.saxutils import escape  
  
xml_str = escape(HTMLParser().unescape(html_str))  
```  
  
---  
  
## Python 3  
  
### Python 3.3 or older  
  
```Python3  
from html.parser import HTMLParser  
from xml.sax.saxutils import escape  
  
xml_str = escape(HTMLParser().unescape(html_str))  
```  
  
### Pytho 3.4+  
  
```Python3  
import html  
from xml.sax.saxutils import escape  
  
xml_str = escape(html.unescape(html_str))  
```  
  
---  
  
# Reference  
  
+ [How do I unescape HTML entities in a string in Python 3.1? - Stack Overflow](https://stackoverflow.com/questions/2360598/how-do-i-unescape-html-entities-in-a-string-in-python-3-1)  
