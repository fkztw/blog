Title: [Cpp] [Online Judge] UVa 11332 Summing Digits
Date: 2013-04-29 20:48
Author: fkz
Category: Cpp
Tags: Cpp 
Slug: cpp-online-judge-uva-11332-summing-digits
Status: draft

[http://uva.onlinejudge.org/external/113/11332.html][1]    
    
2013/04/29 基礎程式檢定考題之一    
(共7題 我寫了三題 只對一題Orz 這是唯一對的一題 算是水題 AC率很高)    
    
    
雖然說是水題 我還是用了很爛的方法= ="    
    
看到題目給的說明 我就寫了個遞迴的版本 (大概是大一上修小黃的計概遺毒?    
    
    
  
遞迴版本長這樣: [https://gist.github.com/M157q/faccf2be88ab924a6091][2]  
  
    
  
真的是超級慢!! 很慢很慢= =   
  
    
  
後來才發現原來以前寫過... 唉... 是很快的版本...  
  
    
  
其實題目很簡單 就只是要把一個數字個別位數的值相加  
  
    
  
一直重複 直到得到的數是個位數為止  
  
    
  
主要就是字串處理的東西 用到了 <cstring> 的 strlen(), memset() 和 sprintf()  
  
    
  
我覺得 sprintf 算是蠻重要的  
  
    
  
<cstdlib> 的 atoi() 是把 array 轉成 int  
  
    
  
而要將 int 轉成 array 的話 使用 <cstdio> 的 sprintf 就能夠辦到  
  
ex: sprintf(str, "%d", int)  
  
    
  
詳細可見 [http://www.cplusplus.com/reference/cstdio/sprintf/][3]   
  
    
  
以下是非遞迴的版本: [https://gist.github.com/M157q/d6b0cb7bf5486b4659fa][4]  
  
    
  
看來還是得花時間好好把該學會的東西學會啊Orz    
    
    
2013/05/08:    
看到一個更簡單的寫法    
[https://github.com/ackoroa/UVa-Solutions/blob/master/UVa%2011332%20-%20Summing%20Digits/src/UVa%2011332%20-%20Summing%20Digits.cpp][5]    
    
這個寫法又更簡潔了    
[http://www.knightzone.org/wordpress/archives/1816][6]  
  
  
  
[1]: http://uva.onlinejudge.org/external/113/11332.html  
[2]: https://gist.github.com/M157q/faccf2be88ab924a6091  
[3]: http://www.cplusplus.com/reference/cstdio/sprintf/  
[4]: https://gist.github.com/M157q/d6b0cb7bf5486b4659fa  
[5]: https://github.com/ackoroa/UVa-Solutions/blob/master/UVa%2011332%20-%20Summing%20Digits/src/UVa%2011332%20-%20Summing%20Digits.cpp  
[6]: http://www.knightzone.org/wordpress/archives/1816  
