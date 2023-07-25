Title: [Cpp] [Online Judge] UVa 10579 Fibonacci Numbers  
Date: 2013-04-29 19:57  
Author: fkz  
Category: Note  
Tags: Cpp, Online Judge, Big Number  
Slug: cpp-online-judge-uva-10579-fibonacci-numbers  
  
2013/04/29 基礎程式檢定考題之一  
(共7題 我寫了三題 只對一題Orz 後來花時間把沒寫完的兩題寫完 這是其中一題)  
  
[http://uva.onlinejudge.org/external/105/10579.html][1]  
  
<!--more-->  
  
這題必須要用大數加法才能做出來  
  
題目說答案不會超過 1000 位數  
  
我在考試的時候還很開心的用 unsigned long long 去算答案= ="  
  
unsigned long long 最大值是 2^64 -1 == 1.8446744073709551615 × 10^19  
  
也就是只能完全計算到 18 位數和一點點 19 位數 超過以後就會 overflow...  
  
我還在那邊試很久= =" 想說怎麼測資都沒對 大概是上機考的時候太緊張了吧= =""  
  
對大數不太熟悉 剛好就用這題來練習  
  
Big number 就是把原本的 int 分開成 int array 去儲存  
  
每個 element 都代表一個位數 作法就像小學時候學的直式加法一樣  
  
所以可以一直加下去 只要用來儲存答案位數的 int array 給的夠大就行  
  
以下是我的 code  
  
[https://gist.github.com/M157q/53d3dc8586ddee57e240][2]  
  
因為有點懶的打英文 所以用了中文註解...  
  
  
  
  
[1]: http://uva.onlinejudge.org/external/105/10579.html  
[2]: https://gist.github.com/M157q/53d3dc8586ddee57e240  
