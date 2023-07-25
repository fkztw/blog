Title: [Cpp] [Online Judge] UVa 737 Gleaming the Cubes  
Date: 2013-04-29 20:16  
Author: fkz  
Category: Note  
Tags: Cpp, Online Judge, abs  
Slug: cpp-online-judge-uva-737-gleaming-the-cubes  
  
2013/04/29 基礎程式檢定考題之一  
(共7題 我寫了三題 只對一題Orz 後來花時間把沒寫完的兩題寫完 這是其中一題)  
  
[http://uva.onlinejudge.org/external/7/737.html][1]  
  
<!--more-->  
  
這題是被 Compiler 雷到... 答案算是已經寫出來了...Orz  
  
上機考的電腦是用 gcc 4.2.x 在本地端 compile 沒有噴 error  
  
考完後在自己的筆電上的 gcc 4.8.0 測試也沒噴 error  
  
結果上傳上去就噴 error 說找不到適合的 overloaded function 可用  
  
究竟程式檢定 server 用的 compiler 是哪一個啊@_@?  
  
但結果追根究底是因為我沒搞清楚 `abs()` 這個 function...  
  
`cstdlib` 和 `cmath` 都有 `abs()` 這個 function  
  
`cstdlib` 的 `abs()` 是給整數型態用的 `cmath` 的 `abs()` 是給浮點數型態用的  
  
而我在這裡要取的是整數型態的絕對值 所以應該要 `#include <cstdlib>`  
  
結果我記錯 寫了 `#include <cmath>` (然後就是悲劇Orz  
  
請參閱  
[http://www.cplusplus.com/reference/cstdlib/abs/][2]  
裏面有提到  
  
>In C++, this function is also overloaded in header [cmath][3] for floating-point types (see [cmath abs][4]),  
>in header [complex][5] for complex numbers (see [complex abs][6]),  
>and in header [valarray][7] for valarrays (see [valarray abs][8]).  
  
所以其實很多 library 裏面都有 `abs()` 這個 function  
這裡就不細講了 有興趣的人請自行參閱  
  
而 `cmath` 的 `abs()` 也有提到  
[http://www.cplusplus.com/reference/cmath/abs/][9]  
  
>These convenience abs overloads are exclusive of C++.  
>In C, [abs][10] is only declared in [cstdlib][11] (and only operates on integral values).  
  
所以在 C 裏面  
只有 `<stdlib.h>` 裏面有 `abs()` 這個 function 而且還只能給整數型態用  
因為沒有 function overloading  
(看到這個就覺得我應該用 C 寫的Orz  老實說其實自己寫一個也很快Orz  
  
```c  
int abs(int a)  
{  
    return ((a < 0) ? -a : a);  
}  
```  
  
這樣就行了...  
反正後來總算是寫出來了 也找到了錯誤 應該值得高興(吧？  
以下是我的 code  
  
[https://gist.github.com/M157q/c92d437af7f7d497de67][12]  
  
  
  
[1]: http://uva.onlinejudge.org/external/7/737.html  
[2]: http://www.cplusplus.com/reference/cstdlib/abs/  
[3]: http://www.cplusplus.com/cmath  
[4]: http://www.cplusplus.com/cmath:abs  
[5]: http://www.cplusplus.com/complex  
[6]: http://www.cplusplus.com/complex:abs  
[7]: http://www.cplusplus.com/valarray  
[8]: http://www.cplusplus.com/valarray:abs  
[9]: http://www.cplusplus.com/reference/cmath/abs/  
[10]: http://www.cplusplus.com/abs  
[11]: http://www.cplusplus.com/cstdlib  
[12]: https://gist.github.com/M157q/c92d437af7f7d497de67  
