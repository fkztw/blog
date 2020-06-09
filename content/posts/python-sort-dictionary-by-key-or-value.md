Title: [Python] Sort dictionary by key or value
Date: 2013-05-10 16:33
Author: m157q
Category: Note
Tags: Python, Sort, Python 3
Slug: python-sort-dictionary-by-key-or-value
  
  
#in python3.3  
<!--more-->  
  
>(k, v) == (key, value)  
  
---  
  
####sort by key  
```python  
for k, v in sorted(h.items(), key = lambda t:t[0]):  
    print("%s: %s" % (k, v))  
```  
> t[0] means key  
  
---  
  
####sort by value  
```python  
for k, v in sorted(h.items(), key = lambda t:t[1]):  
    print("%s: %s" % (k, v))  
```  
> t[1] means value  
  
  
--  
