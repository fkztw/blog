Title: [Python] Mutable v.s Hashable  
Date: 2013-06-05 09:31  
Author: m157q  
Category: Note  
Tags: Python, Python 3, mutable, hashable  
Slug: python-mutable-vs-hashable  
  
  
  
Before talk about this, let's see some definitions.  
  
<!--more-->  
  
Mutable Def:  
    [Mutable objects can change their value but keep their id().][1]  
  
Immutable Def:  
    [An object with a fixed value. Immutable objects include numbers, strings and  
tuples. Such an object cannot be altered. A new object has to be created if  
a different value has to be stored. They play an important role in places where  
a constant hash value is needed, for example as a key in a dictionary.][2]  
  
  
Hashable Def:  
  
    [An object is _hashable_ if it has a hash value which never changes during  
its lifetime (it needs a __hash__()method), and can be compared to other objects  
(it needs an __eq__() method). Hashable objects which compare equal must have  
the same hash value.][3]  
  
[    Hashability makes an object usable as a dictionary key and a set member,  
because these data structures use the hash value internally.][3]  
  
[    All of Python’s immutable built-in objects are hashable, while no mutable  
containers (such as lists or dictionaries) are. Objects which are instances  
of user-defined classes are hashable by default; they all compare unequal (except  
with themselves), and their hash value is their id().][3]  
  
  
    [Objects whose value can change are said to be mutable][4][; ][4]  
  
   [Objects whose value is unchangeable once they are created are called _immutable_. (The value of an immutable container object that contains a reference to  a mutable object can change when the latter’s value is changed; however the  container is still considered immutable, because the collection of objects  it contains cannot be changed. So, immutability is not strictly the same as  having an unchangeable value, it is more subtle.) ][4]  
    [An object’s mutability is determined by its type; for instance, numbers,  
strings and tuples are immutable, while dictionaries, sets and lists are mutable.][4]  
  
  
  
We can use hash() to check if an object is hashable.  
  
But there seems no method to check if an object is mutable or not.  
  
Google "python mutable check". Seems many people use hash() to check if an  
object is mutable or not...  
  
  
  
Python documentation said "[All of Python’s immutable built-in objects are  
hashable, while no mutable containers (such as lists or dictionaries) are.][3]"  
  
  
  
So... the questions are:  
  
1. Is there any hashable built-in object is mutable?  
  
2. Is there any un-hashable built-in objects is immutable?  
  
If the answers of the two questions above is "No".  
Then,   
  
3. Can we create an user defined type that is hashable but mutable?  
  
4. Can we create an user defined type that is not hashable but immutable?  
  
  
  
If the answers of the four questions above is "No".  
  
Does it mean that we can use hash() to check if an object is mutable or not?  
  
---  
  
Refs:  
[http://stackoverflow.com/questions/2671376/hashable-immutable][5]  
[http://docs.python.org/3/reference/datamodel.html#object.__hash__][6]  
[http://docs.python.org/3/tutorial/classes.html][7]  
[http://eli.thegreenplace.net/2012/03/30/python-objects-types-classes-and-instances-a-glossary/][8]  
[http://stackoverflow.com/questions/4374006/check-for-mutability-in-python][9]  
[http://stackoverflow.com/questions/4418741/im-able-to-use-a-mutable-object-as-a-dictionary-key-in-python-is-this-not-disa][10]  
[http://www.velocityreviews.com/forums/t734950-how-to-test-for-atomicity-mutability-hashability.html][11]  
  
  
  
[1]: http://docs.python.org/3/glossary.html#term-mutable  
[2]: http://docs.python.org/3/glossary.html#term-immutable  
[3]: http://docs.python.org/3/glossary.html#term-hashable  
[4]: http://docs.python.org/3/reference/datamodel.html  
[5]: http://stackoverflow.com/questions/2671376/hashable-immutable  
[6]: http://docs.python.org/3/reference/datamodel.html#object.__hash__  
[7]: http://docs.python.org/3/tutorial/classes.html  
[8]: http://eli.thegreenplace.net/2012/03/30/python-objects-types-classes-and-instances-a-glossary/  
[9]: http://stackoverflow.com/questions/4374006/check-for-mutability-in-python  
[10]: http://stackoverflow.com/questions/4418741/im-able-to-use-a-mutable-object-as-a-dictionary-key-in-python-is-this-not-disa  
[11]: http://www.velocityreviews.com/forums/t734950-how-to-test-for-atomicity-mutability-hashability.html  
