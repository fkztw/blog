Title: Magic of Python list slicing  
Slug: magic-of-python-list-slicing  
Date: 2015-05-25 04:16:38  
Authors: fkz  
Category: Note  
Tags: Python, List, Slicing, Magic  
Summary: Some tricks for the list slicing in Python.  
Modified: 2015-06-23 05:47:38  
  
主要是想查 Python 要怎麼漂亮的寫 prepend 一個 item 到 list 時  
找到了這篇 [append integer to beginning of list in python - Stack Overflow](http://stackoverflow.com/questions/17911091/append-integer-to-beginning-of-list-in-python)  
  
主要就三種寫法：  
  
+ 第一種，把 item 塞進一個 list 然後再加上原本的 list  
```python  
l = [item] + l  
```  
  
+ 第二種，用 built-in 的 list.insert  
```python  
l.insert(0, item)  
```  
  
+ 第三種，評分最低、也是引起我好奇的寫法  
```python  
l[:0] = [item]  
```  
  
試了一下，發現真的可以這樣做，但在這之前從來沒看過這寫法。  
於是就去翻了一下官方的文件  
[5. Data Structures — Python 3.4.3 documentation](https://docs.python.org/3.4/tutorial/datastructures.html)  
發現裡頭有類似的東西，以前都沒仔細看。  
  
```python  
list.append(x)  
Add an item to the end of the list. Equivalent to a[len(a):] = [x].  
  
list.extend(L)  
Extend the list by appending all the items in the given list. Equivalent to a[len(a):] = L.  
```  
  
雖然只有 append 的部分，但可以看出有點相似，  
跟 Apua 經過一番討論後，整理了一下重點：  
  
---  
  
+ prepend  
```python  
l[:0] = [x]  
```  
等於  
```python  
l.insert(0, x)  
```  
  
---  
  
+ list.append  
```python  
l[len(l):] = [x]  
```  
等於  
```python  
l.append(x)  
```  
等於  
```python  
l.insert(len(l), x)  
```  
  
---  
  
+ list.extend  
```python  
l[len(l):] = [a, b, c]  
```  
等於  
```python  
l.extend([a, b, c])  
```  
  
---  
  
prepend 和 append 的變化型都沒啥特別的，  
用 insert 和 append 的可讀性其實比較高。  
主要是 extend 的變化型有些有趣的東西可以討論。  
例如：  
  
```python  
l[i:i] = [a, b, c]  
```  
  
這會在 l 原本的的 i-1 和 i 中 insert a, b, c 這三個 elements，  
可以看作是可 insert 任意位置的 list.extend，  
原本的 extend 只能把 iter 展開後加到 l 的最後面，  
但這樣的寫法突破了這種限制。  
例如：  
  
```python  
>>> l = [1, 2, 3, 4, 5]  
>>> l[2:2] = [-1, -2, -3]  
>>> l  
[1, 2, -1, -2, -3, 3, 4, 5]  
```  
  
然後也可以把 l[i:i] = [a, b, c] 的兩個 i 換成一般正常使用的 slicing 方式，  
被 slicing 選擇出來的區段就會直接被 a, b, c 取代掉。  
例如：  
  
```python  
>>> l = [1, 2, 3, 4, 5]  
>>> l[1:4] = [0, 0, 0]  
>>> l  
[1, 0, 0, 0, 5]  
```  
  
真的是第一次知道這種神奇的寫法...  
Apua 猜測 list 的實作應該是跟 linked list 有關  
之後有空的話來仔細看一下 python list 的實作好了  
  
