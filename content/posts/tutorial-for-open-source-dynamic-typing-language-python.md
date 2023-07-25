Title: 開放源碼的動態程式設計語言體驗營 - Python  
Date: 2013-04-09 15:42  
Author: fkz  
Category: Conf/Meetup  
Tags: Python, Tutorial  
Slug: tutorial-for-open-source-dynamic-typing-language-python  
Modified: 2015-10-27 11:20  
  
  
### Event  
  
+ [Activities - 開放源碼的動態程式設計語言體驗營 - Python - OpenFoundry](http://www.openfoundry.org/en/activities/details/366)  
  
### Slides  
  
+ [Downloads | 03/09 開放源碼的動態程式設計語言體驗營 - Python | 2013年-活動/研討會 | 歷年活動／研討會簡報 | 活動 / 研討會相關 - OpenFoundry](http://www.openfoundry.org/tw/slides-download/cat_view/35/711/712)  
    + 備份  
        + [Day 1](https://github.com/M157q/fkz.github.io/raw/source/content/files/tutorial-for-open-source-dynamic-typing-language-python/0309_programming-with-python-basic.pdf)  
        + [Day 2](https://github.com/M157q/fkz.github.io/raw/source/content/files/tutorial-for-open-source-dynamic-typing-language-python/0310_programming-with-python-adv.pdf)  
  
### Videos  
+ [自由軟體鑄造場_20130309_開放源碼的動態程式設計語言體驗營 - Python_Mosky_01 - YouTube](https://www.youtube.com/watch?v=cUYu6v6b_oY&list=PLuW7NCGvKlyXZxvnpZxwu6AUeSdqkcmbm)  
+ [自由軟體鑄造場_20130310_開放源碼的動態程式設計語言體驗營 - Python_Mosky_01 - YouTube](https://www.youtube.com/watch?v=AXpV-sUIYqI&list=PLuW7NCGvKlyU82s5TX8LqGk9arydf9m9Z)  
  
  
上個月去台北大同大學跟 Mosky 學 Python 做的一些筆記  
同樣的筆記我也有放在 gist 上，但是純文字版。  
  
+ [20130309-mosky-python-day1 · GitHub](https://gist.github.com/M157q/5124618)  
+ [20130309-mosky-python-day2 · GitHub](https://gist.github.com/M157q/5128627)  
  
> Mosky 真的超萌而且聲音超好聽的 >////<  
  
### 後記 (2015/10/26)  
  
> 寫這篇筆記的當時還不太熟 Markdown  
> 所以 gist 是略帶 Markdown 語法的純文字版  
> 當時因為懶惰，所以把純文字直接複製貼上到 blog 就沒管了  
> 最近在整理舊的 blog 文章，整理到這篇。  
> 因為純文字版本在 Pelican 上 rendering 的效果很恐怖  
> 所以這邊的版本是從純文字修改為 Markdown 的版本  
> 同時也修正了一些當年筆記上的錯誤和補充一些內容  
> 轉眼間接觸 Python 已經兩年半了呢  
> 這些當年看起來內容很生澀的筆記，現在也都懂了  
> 這種感覺有點神奇  
> 目前愈來愈喜歡 Python 這個語言了  
> 至於內文把 Python 的 P 全用成小寫 p，我實在懶的改，意思有到就好了嘛(?)  
> 或許哪天我的強迫症發作了，我又會回來改這篇文章也說不定。  
> 筆記看似很多，其實仍然因為打字速度不夠快的原因，沒紀錄到很完整，但大概有八成了吧  
  
  
---  
  
### [PyPI](https://pypi.python.org/pypi) - commit your python project  
  
### project -  a blog system  
  
> Dynamic typing, Static typing, Functor, Closure  我還不熟的東西  
  
---  
  
# Day 1 - 2013.03.09  
  
## Python 2 or 3 ?  
  
+ 2.7 是 2.x 最後一個 release  
+ python 目前全力投入 3.x 的開發  
+ 3.x is easier for newcomer  
+ 2.x has more third-party lib  
+ 轉換 Syntax  
    + 2to3.py (官方)  
    + 3to2.py(非官方)  
+ 2.x 有 backported features 因為和 3.x 平行開發，所以會把 3.x 的一些 features 拿回來用  
+ Use Python 3 if you can.    用 python3 就對了(?  
+ 根據你要用的 library 選擇 2.x 或 3.x  
+ 課程會以 python2.7 為主, 但會介紹 3.x 中的改變  
  
  
一般看到的都是 cpython , 對 c/c++ 提供較好的相容性,  
可以在 c/c++ 中寫 python 的 module, 然後在 python 中 import 進來  
主流都是用 cpython, 一般的 document 也都是以 cpython 為主  
  
## byte code  
  
## Python Shell  
  
* `-c`: 直接執行一行式  
```  
python -c 'print "hello, world"'    # python2  
python -c 'print("hello, world")'   # python3  
```  
  
* `-m`: 使用module  
```  
python -m SimpleHTTPServer [port]   # python2  
python -m http.server [port]        # python3  
```  
  
  
## hello.py  
  
* 用 4 個空白 不要用 tab  
* `:` 是一個 block 開始的意思  
* 換行就代表一個 statement 的結束  
```python  
__name__  # the name of module  
if __name__ == '__main__':  # 類似 C 裏面的 main 函數  
```  
  
  
## Common types  
  
+ Characteristics  
    * Mutable / Immutable (是否可變動)  
        * Immutable 不可變動  
            * ex: Hashable `(__hash__)`  
            * python 的變數可視為純 pointer  
            * Immutable 代表該變數指向的物件是不可變動的  
    * Ordered / Unordered  
        * Iterable `(__iter__)`  
    * Numeric (Immutable, Hashable)  
        * integer  
        * float  
        * long  
        * complex  
          * `1+1j`  
          * 小寫 j 或大寫 J 都可以  
        * boolean  
          * `True`, `False`  
          * 開頭要大寫  
    * Sequence (Iterable, Ordered, Mutable/Immutable)  
        * string  
    * Mapping  
        * dictionary  
    * Set  
  
  
> a = 'string'  
> 1. 先建立 string 這個 object  
> 2. 再建立 a 這個 pointer  
> 3. 再把 a 指向 string  
> 4. 所以 string 是 Immutable，但可以讓 a 指向其他的 object  
  
  
### Interger, Float and Long  
  
+ `divmod(被除數, 除數)`  
    + 回傳商數和餘數(tuple)  
+ `5//2`  
    + 取商的 floor  
+ `5**0.5`  
    + `**0.5` 就是取 square root  
+ `bin(整數)`  
    + 可以將該整數以 binary 表示  
+ `float(整數)`  
    + 可以將該整數轉成 float 表示  
  
  
### Complex  
+ `complex(0,1) == 0+1j`  
+ `a = 3.0 + 4.0j`  
    + `a.real == 3.0`  
    + `a.imag == 4.0`  
    + `abs(a)`  
        + 算出該複數在複數平面上跟原點的距離  
        + 等同於 `sqrt(a.real**2 + a.imag**2)`  
  
  
### Boolean  
  
+ `not False`  
    + 在 python 中直接打 `not` 就好  
+ `True and False`  
    + 在 python 中直接打 `and` 就好  
+ `True or False`  
    + 在 python 中直接打 `or` 就好  
+ `False` 的值就是 `0`  
    + `False + 1 == 1`  
+ `True`  的值就是 `1`  
    + `True + 1 == 2`  
+ python 裏面的 float 有做過處理所以 `10 == 10.0` 是 `True`  
+ `x is y`  
    + 判斷 x 和 y 是否真的指向同一個 object  
    + 比 `==` 嚴謹，`==` 只在乎值是否相同，而不考慮是否為同一個 object  
  
  
### String and Unicode  
  
+ python 的單引號和雙引號是一樣的意思  
+ String (immutable seq.)  
    + python 中的字串是不能更改的  
    + `r'字串\n'`  
        + r 代表 raw string  
        + 在 r'' 裏面的跳脫字元不會被轉譯  
    + `'''字串'''`  
        + 多行字串 (會幫你紀錄換行符)  
        + 通常python裏面的多行註解也是這樣寫  
+ Unicode (Immutable seq.)  
    + `u'字串'`  
        + 代表裏面存的編碼是 unicode  
    + `ur'字串'`  
        + 代表 raw string 裏面存的編碼是 unicode  
        + ur 的順序是固定的 不可以寫成 ru  
    + `u'''字串'''`  
        + 代表裏面存的編碼是 unicode  
    + `ord(字元)`  
        + 將字元轉成 ascii  
    + `chr(ascii編碼)`  
        + 將 ascii 編碼轉成字元  
    + `unichr(unicode編碼)`  
        + 將 unicode 編碼轉成 unicode 字串  
    + Decoding (str -> unicode)  
        + `'中文'.decode('utf-8') == unicode('中文', 'utf-8')`  
    + Encoding (unicode -> str)  
        + `u'中文'.encode('utf-8')`  
    + python2 設計的時候沒有考慮到 unicode 的問題  
    + python3 的 str 就是 unicode  
        + 新的型態 `bytes` (Immutable seq.)  
+ 常用 method (詳細的 method 請參見 python 的 doc)  
    + `decode()`  
    + `encode()`  
    + `endswith()`  
    + `find()`  
    + `format()`  
    + `join()`  
    + `lower()`  
    + `partition()`  
    + `replace()`  
    + `split()`  
    + `startwith()`  
    + `strip()`  
    + `upper()`  
+ string formatting  
    + modulo (`%`)  
        + `%r`  
            + representation  
            + `'Hello, %s' % name`  
                + 用 `name` 的內容取代 `%s`  
    + `str.format()`  
        + `'Hello, {}'.format(name)`  
  
  
### List and tuple  
  
| List (Mutable seq.)    |    Tuple (Immutable seq.) |  
|:----------------------:|:-------------------------:|  
|     [] or list()       |       () or tuple()       |  
|       ['item']         |         ('item', ) # 只有一個的情況下要加逗點 |  
|  元素可以放不同的型態  |  元素可以放不同的型態     |  
  
+ List 在 python 中的實作是用 array, 所以會比較慢  
  
  
### Sequence  
  
+ Immutable seq. 支援的操作  
    + `x in s`  
        + 查 `s` 是不是在 `x` 裏面, 結果會回傳 `boolean`  
    + `x not in s`  
        + 搜尋是用 linear search, 效能上要注意一下  
    + `s + t`  
    + `s * n`  
    + `slice`  
    + `string.len()`  
    + `string.index(a)`  
        + 如果沒找到 `a` 的話會跳出 except 的訊息  
    + `string.count(a)`  
        + 計算 string 裏面 `a` 出現幾次  
+ Mutable seq. 支援的操作  
    + `s[1] = x`  
    + `s[i:j] = t`  
    + `del s[i:j]`  
    + `s[i:j:k]`  
    + `s.append(x)`  
    + `s.insert(i,x)`  
    + `s.pop([i])`  
    + `s.remove(x)`  
    + `s.extend(x)`  
        + 擴充 `s`  
    + `s.append(x)`  
        + 將 `x` 加進去變成元素  
    + `in-place`  
    + `s.sort()`  
        + 內建的 sort 是 [Timsort](https://en.wikipedia.org/wiki/Timsort), 是個改良板的 [merge sort](https://en.wikipedia.org/wiki/Merge_sort)  
    + `s.reverse()`  
        + 把 seq. 顛倒過來  
+ Sequence 支援 比較 的動作  
+ Slicing and slice  
    + `s[:]    # a copy of the whole array`  
  
  
## Mapping  
+ Dictionary (Mutable map)  
    + 就是 key-value pairs  
    + `{'A':1, 'B':2, 'C':3}`  
    + `dict(A=1, B=2, C=3)`  
    + 實作是用 B tree 所以不會照順序,  
    + 如果要照順序的話可以用 collections 的 ordered dictionary  
        + `collections.OrderedDict()`  
    + 或是把 key 存在一個 list 裏面  
+ `zip()`  
```python  
k = 'ABC'  
v = [1,2,3]  
pairs = zip(k,v)  
  
# pairs 會變成 [('A', 1), ('B', 2), ('C', 3)]  
# dict(pairs) 是 {'A': 1, 'C': 3, 'B': 2}  
```  
+ dictionary 可以用 string 當 key, list 就不行  
+ 支援的操作 (k is the name of key)  
    + `len(d)`  
    + `d[k]`    
    + `d[k] = v (Mutable)`  
    + `del d[k]`  
    + `k in d, k not in d`  
    + `d.copy()`  
    + `d.get(key[, default])`  
    + `d.setdefault(key[, default])`  
    + `d.items(), d.keys(), d.values()`  
        + 在 python 3 裏面這 3 個函式回傳的都是 iter 不是 list  
    + `d.pop(key[, default])`  
    + `d.update([other])`  
        + `d.update(dict(...))`  
  
  
## None  
+ 是個 object, 有點類似 c 裏面的 `NULL`  
+ 可以用 python 先簡單寫出演算法並證明自己的想法, 再用 C 去實作出來  
  
  
## Set (mutable set)  
  
```python  
set()   # python2  
set('ABC') == set(['A', 'B', 'C'])  
{'A', 'B', 'C'} # python3  
  
# s 代表 set  
len(s)  
x in s, x not in s  
s.add(elem)  
s.discard(elem)  
s.pop()  
s |= other_s  
s &= other_s  
s | other_s  
s & other_s  
```  
  
  
## Flow Control  
  
+ 注意冒號和縮排    
  
  
### if-else  
  
+ condition 不需要用 `()` 包起來  
  
```python  
if condition_1:  
elif condition_2:  
...  
elif condition_N:  
else:  
```  
  
  
### 被視為 False 的值  
  
+ `None`  
+ `False`  
+ Zeros  
    + `0`  
    + `0.0`  
    + `0L`  
    + `0j`  
+ Empty containers  
    + `''`  
    + `[]`  
    + `{}`  
+ `__nonzero__()` or` __len__()` return `0` or `False`  
  
> 注意:  
> `if [0]`: 和 `if [[]]`: 後的敘述會被執行  
> 因為 [] 裏面有包含東西就不會被視為空的  
> () 和 {} 也是同樣的道理  
  
  
### for (for-each 的性質, python 裏面只有這種for)  
+ `for [item] in [iterable]:`  
+ `for i in range(3):`  
    + 會建個 list 出來, 比較浪費資源  
+ `for i in xrange(3):`  
    + xrange 只會建個 iter, 比較節省資源  
+ python3 沒有 `xrange()`, 因為 python3 的 `range()` 就是 python2 的 `xrange()`  
+ python3 裏面把很多東西都改成比較節省資源的方式  
  
```python  
for i, item in enumerate(sth):  
    print i, item  
  
# i 會是從0開始的 index, item 就是 sth 裏面的 element  
```  
  
+ python 的 `for` 可以 iterate all of iterable object  
+ `iter(sth)`  
    + 可以把 sth 轉成 iter 後回傳  
  
  
### while  
  
```python  
tasks = [...]  
while tasks:  
    ...  
  
# 當 tasks 變成 empty 的時候就跳出迴圈  
```  
  
  
### break, continue (都只能用在 loop 裏面)  
  
就跟 C 一樣,  
可能可以讓 python 執行的更快  
因為python是 interpretation  
提前結束的話可以少跑一些程式  
所以 python 鼓勵使用 `break` 和 `continue`  
  
  
### The else Clause on Loops (while, for)  
  
```python  
loops:  
    ...  
else:  
```  
  
上面的迴圈如果沒有被 `break` 提前結束的話  
就會進入 `else`  
可以用來取代平常設定的 flag  
  
---  
  
# Day 2 - 2013.03.10  
  
+ [今日投影片](http://j.mp/mosky-python)  
+ [最新版投影片](http://j.mp/mosky-py)  
  
  
## print  
  
+ `print 'Print', 'multiple'`  
    + Print 和 multiple 中間會有空白  
        + 在 python2 裏面拿不掉  
        + 可以用 `sys` 裏面的 `write` 代替就沒有空白  
+ `print`  
    + 印一個新行  
+ `print()`  
    + python2 會印一對括號  
    + python3 會印一個新行  
+ `print('End with a space.', end='')`  
    + 會把最後因為逗號出現的空白去掉  
+ `print('A', 'B', 'C', sep=',')`  
    + `sep` 預設是一個空白  
  
  
## Sequence Comparison  
  
python 裏面沒有字元 只有長度為1的字串  
所以 `'A' > 65` 是 `True`  
通常不會拿 字串 和 整數 做比較  
在 python3 裏面用 seq 跟不是 seq 的型態比較會出現 type error  
  
  
## if-else 補充 (類似 Ternary 的用法)  
  
+ Python 中並沒有 C 的 `?:` (ternary operator)，但可以用下面這寫法來達到  
+ `[exp. if conditon true] if [condition] else [exp. if condition false]`  
  
也就是說，C 裡頭的  
```c  
a = 0 ? 'a' : 'b';  
```  
等同於 Python 裡頭的  
```python  
a = 'a' if 0 else 'b'  
```  
  
  
## try  
  
```python  
# python2  
try:  
    ...  
except LookupError, e:  
    ...  
except (IndexError, KeyError), e:  
    ...  
else:  
    ...  
finally:  
    ...  
```  
  
```python  
# python3  
try:  
    ...  
except LookupError as e:  
    ...  
except (IndexError, KeyError) as e:  
    ...  
else:  
    ...  
finally:  
    ...  
```  
  
+  避免使用 `Exception` (所有 exceptions 的父類別, 會抓到所有的例外)  
    +  除非是在頂層, 如果 except 後面不寫東西, 也是代表抓所有的例外  
+  `try` 裏面的 code 要儘量減少, 儘量把要執行的 code 放在 else  
+  `finally` 用來寫意外發生的時候要如何善後的code  
+  `raise KeyError('xxxxx')`  
  
  
## def  
  
+ 定義一個function  
+ 如果沒寫回傳值的話，會回傳`None`  
  
### unpack 用法  
  
```python  
f(1, 2) == f(*(1, 2))  
f(y=2, x=1) == f(**{'y':2, 'x':1})  
  
def f(*args):       # *args 代表接受任意長度的參數  
    return args     # 回傳一個 tuple  
  
def f(**kargs):     # **kargs 可以接受 keyword argument  
    return kargs    # 回傳一個 key 和 value 對應的 dictionary  
  
def f(x, *args):  
    return x, args  
  
def f(x, **kargs):  
    return x, kargs  
  
def f(*args, y):    # Syntax Error, 特定的argument要放在 *args 前面  
    return args  
  
def f(*args, **kargs): # 接收所有的參數  
    return args, kargs # 可以透過這樣的寫法  
                       # 將所有參數原封不動傳給另外一個function  
                       # 最好是 hack 別人的 library 或是  
                       # 要修正自己的 function 時再用  
  
# def statement in python3  
    def f(*args, k):    # python3 比較彈性 這樣寫不會噴 syntax error  
        return k, args  # 但 k 只能用 keyword argument 指定  
                        # 因為所有 position 指定的方式都會被 *args 吃掉  
  
# python functions are first-class functions  
# you can pass functions as arguments and assign functions to variables  
# like function pointer in c  
```  
  
### A trap of the default value  
  
參見 `ex_defval_trap.py`  
  
這是新手很容易遇到的一個問題之一  
list 是在 function define 的時候就建立了, 不是在 function 被 called 的時候  
所以 `list = []` 這個方式並不會在每次呼叫該 function 的時候把 list 清空  
只有在該 fuction 第一次被呼叫時，該 list 會是空的  
所以避免用 Mutable types 來當 default value  
如果要用的話 可以使用類似下面這種方式  
  
```python  
def (items=None):  
    if items is None:  
        items = []  
    items.append(1)  
    return items    
# 這樣就可以每次把list清空  
```  
  
  
## Swap two variables in Python  
  
```python  
x, y = [1, 2]  
x, y = (1, 2)  
# x == 1 , y == 2  
# 可用 y, x = x, y 直接做 swap  
```  
  
  
## File object  
  
### Read  
  
```python  
f = open('input.txt')  
print f.read()  
f.seek(0)  
  
for line in f:  
    print line,  
  
f.close()        
```  
  
### Write  
  
```python  
f = open('output.txt', 'w')  
f.write('a line.\n') # 要記得加換行符  
f.close()  
```  
  
### csv module  
  
```python  
import csv  
  
with open('ex_csv.csv') as f:  
        for row in csv.reader(f):  
            print row  
```  
  
  
## Documentation  
  
+ <http://docs.python.org/2/>  
+ <http://docs.python.org/3/>  
+ `help($name)`  
+ `dir($name)`  
+ `'\n'.join(dir($name))`  
+ `pydoc $name`  
  
### Your Documentation  
  
+ 可以自己寫 pydoc 說明自己寫的東西  
+ 可以用 python 來寫測試其他語言的工具  
    + Data model 有許多 special method (__xxx__) 的詳細說明  
  
  
## Scope  
  
+ function scope  
    + scopes are decided by functions.  
  
  
### The LEGB Rule (python 變數查找的規則)  
  
+ 變數查找順序依序為  
    + local  
    + enclosed  
    + global  
    + built-in  
  
  
## [clime](http://clime.mosky.tw)  
+ 自動將 python code 轉為 command line 介面的 script  
+ `locals()[sys.argv[1]]()`  
  
  
## Module and Package  
  
```python  
import module   # module.py  
  
# 資料夾底下有 __init__.py 的話 就是 python 的 package  
import package  # __init__.py , package 指的是該資料夾的名字  
import package.module # package/module.py  
import .module  # package/module.py  
```  
  
`$ python -m package.module`  
  
+ 不要把自訂的 module 的名字取的跟 built-in module 的名字一樣  
  
  
## Typing  
  
+ python is not static typing, is dynamic typing  
+ Dynamic typing  
    + check types in run time  
    + a variable just points to an object  
    + 一個變數的 reference counter 歸零後, 就會被 GC 回收  
+ Duck Typing  
    + 不在乎你是什麼, 只在乎你會做什麼事  
    + A style of dynamic typing  
    + 如果真的要檢查type的話, 可以用  
        + `if hasattr(x, '__iter__')`  
            + 用來選擇使用者輸入的type  
        + `assert hasattr(x, '__iter__'), 'x must be iterable'`  
+ string 和 integer 都支援 += 這個 operator  
+ item vs. items  
+ employee vs. employee_name  
+ args vs. kargs  
+ 寫好 Documentation 很重要  
  
### Protocol  
  
+ iterator Protocol  
    + object which supports `__iter__()` and `next()`  
+ readable  
    + object which supports `read()`  
  
### Weak typing  
  
+ It converts the type if you do an operation not supported with original type  
  
> python 不是 weak typing !  
> weak typing 和 dynamic typing 是不同的  
  
### Strong typing  
  
+ python 是 strong typing  
+ `1 + 'a'` 會噴 Exception  
  
  
## Comprehension  
  
+ list comprehension  
  
```python  
[i for i in range(10)]              # for 的前面是個 exp. 後面是疊代的條件  
[i for i in range(10) if i % 2]     # [1, 3, 5, 7, 9]  
[i for i in range(10) if not i % 2] # [0, 2, 4, 6, 8]  
```  
    + 可以用這樣的方式很快的檢測使用者輸入的資料  
    + 可以是巢狀的  
+ generator comprehension  
    + `(i for i in range(10))`  
        + 回傳的值不是 tuple，而是 generator  
    + lazy evaluation  
        + save memory  
        + 會等到真的必須要求值的時候才會計算  
+ Other Comprehensions  
    + set comprehension  
        + `set(i for i in range(10)) # python2 or 3`  
        + `{i for i in range(10)}    # python3 only`  
    + dict Comprehension  
        + `dict((i,i) for i in range(10)) # python2 or 3`  
        + `{i:i for i in range(10)}       # python3 only`  
  
  
## Functional Technique  
  
### any() / all()  
  
```python  
all( i % 2 == 0 for i in seq )  
# seq 裏面只要有一個條件不符合的話 就會回傳false  
  
# 如果 iterable 是空的話，all() 會回傳 True  
all(())  
all([])  
all({})  
# 三者的結果皆為 True  
```  
  
```python  
any( i % 2 == 0 for i in seq )  
# seq 裏面只要有一個條件符合的話 就會回傳true  
  
# 如果 iterable 是空的話，any() 會回傳 False  
any(())  
any([])  
any({})  
# 三者的結果皆為 False  
```  
  
#### 用 list comprehension 和 any() / all() 產生 100 內的質數表  
  
```python  
[n for n in range(2,100) if not any(n % i == 0 for i in range(2,n))]  
  
[n for n in range(2,100) if all(n % i != 0 for i in range(2,n))]  
  
# 寫的時候先考慮後面每個 element 的條件  
```  
  
### lamda expression  
  
```python  
lambda [args]: [expression]  
# 其實就是一個小型的 function  
```  
  
#### anonymous function  
+ a single expression  
```python  
f = lambda x: g(x)+h(x)  
  
do(lambda x, y: (x+y)*(x-y), 10, 20)  
```  
  
#### use sort with lambda  
  
```python  
# 想要讓 dict 按照 value 的順序排列, 而不是 key 的順序  
d  = dict(a=300, b=200, c=100)  
keys = d.keys()  
keys.sort(key=lambda k: d[k])  
for k in keys:  
    print k, d[k]  
```  
  
  
### 利用 unpack 和 zip 達到轉置矩陣的效果  
  
```python  
r = [('a', 'b'), ('c', 'd')]  
r = zip(*r) # 先把 r 拆開, 再重新拼起來  
```  
  
  
### map/filter  
  
### reduce  
  
+ 兩個兩個運算後回傳結果  
+ python3 的 `reduce()` 已經不是 built-in function  
    + 要用的話要記得 `import functools`  
    + 然後用 `functools.reduce()`  
  
### partial  
  
+ [9.8. functools — Higher-order functions and operations on callable objects — Python 2.7.10 documentation](https://docs.python.org/2/library/functools.html#functools.partial)  
+ [10.2. functools — Higher-order functions and operations on callable objects — Python 3.5.0 documentation](https://docs.python.org/3/library/functools.html#functools.partial)  
  
  
### Closure  
  
+ [認識 Lambda/Closure（3）Python 對 Lambda/Closure 的支援 by caterpillar | CodeData](http://www.codedata.com.tw/java/understanding-lambda-closure-3-python-support/)  
+ [Python/Cookbook/Closure - Python Taiwan Wiki](http://wiki.python.org.tw/Python/Cookbook/Closure)  
+ [fcamel 技術隨手記: Python 的 Closure](http://fcamel-life.blogspot.tw/2010/02/python-closure.html)  
+ [Closures & Generators - Dive Into Python 3](http://www.diveintopython3.net/generators.html)  
  
  
### yield  
  
+ coroutine  
+ 用 `yield` 取代 `return` 的話, 會回傳 generator  
    + 可以被疊代, 比較不耗記憶體  
  
  
## OOP in python  
  
### The `class` Statement  
  
```python  
class Example(object):  
    class_attribute = 1  
  
    def method(self, ...):  
        pass  
  
example = Example()  
print example  
```  
+ Everythin in Python is `object`.  
    + Class is also an `object`  
+ All `class` inherit the `object` (new-style classes)  
+ Support multiple inheritance  
    + Searching attributes / methods like BFS.  
  
### Bound and Unbound Method  
  
+ bound method (instance method)  
    + `c.m(...)`  
+ unbound  
    + `def m(self, ...):`  
    + `C.m(c, ...)`  
  
### Class Method and Static Method  
  
+ class method  
```python  
@classmethod  
def m(cls, ...):  
```  
  
+ static method  
```python  
@staticmethod  
def m(...):  
```  
  
+ ref  
    + [oop - Python @classmethod and @staticmethod for beginner? - Stack Overflow](http://stackoverflow.com/questions/12179271/python-classmethod-and-staticmethod-for-beginner)  
    + [Python 中的 classmethod 和 staticmethod 有什么具体用途？ - Python - 知乎](http://www.zhihu.com/question/20021164)  
    + [Difference between @staticmethod and @classmethod in Python - Python Central](http://pythoncentral.io/difference-between-staticmethod-and-classmethod-in-python/)  
    + [迷失霧的迷思: python @classmethod and @ staticmethod 的不同(筆記)](http://missions5.blogspot.tw/2014/12/python-classmethod-and-staticmethod.html)  
  
  
## The Data Model of Python  
  
+ Special methods  
    + `__init__`  
    + `__str__`  
    + `__repr__`  
    + `__getitem__`  
        + `x[key]`  
    + `__setitem__`  
        + `x[key] = value`  
    + `__delitem__`  
        + `del x[key]`  
+ ref  
    + [3. Data model — Python 2.7.10 documentation](https://docs.python.org/2/reference/datamodel.html)  
    + [3. Data model — Python 3.5.0 documentation](https://docs.python.org/3/reference/datamodel.html)  
  
  
## Useful Libraies  
  
+ `collections`  
+ `re`  
+ `random`  
+ `datetime`  
+ `decimal`  
    + 寫金融軟體的話要用 `decimal` 不要用 `float`  
+ `pickle`  
+ `json`  
+ `timeit`  
    + 對程式做計時, 看效率  
+ `doctest`  
+ `unittest`  
+ `pdb`  
    + debugger  
+ `requests` (3rd party)  
    + 拿來送 http request 的, 內建的 `urlib` 很難用  
+ `flask` (3rd party)  
    + a web framework  
