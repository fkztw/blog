Title: 20160918 - 你所不知道的 C 語言：指標篇 復刻！  
Slug: guts-c-pointers  
Date: 2016-09-18 23:01:17  
Authors: fkz  
Category: Note  
Tags: C, GUTS, jserv, pointers  
Summary: Jserv 線上 C 語言講座《0918 - 你所不知道的 C 語言：指標篇 復刻！》筆記  
Modified: 2016-09-20 01:17  
  
  
這篇嚴格來說不算筆記，  
大概只算 jserv 語錄 （？）  
想真的瞭解內容的話還是得看共筆就是。  
  
從晚上九點才開始聽，  
而且一開始在是剛到臺北下統聯後，  
在要回租屋處的捷運上邊搭邊聽的，  
所以其實無法太詳細紀錄。  
  
---  
  
## Links  
  
+ 影片：<https://www.youtube.com/watch?v=Eiu2Le-xjmg>  
+ 共筆：<http://hackfoldr.org/dykc/s0rlzR8wVtm>  
+ 聊天室：<https://gitter.im/embedded2015/guts-general>  
  
---  
  
## Note  
  
+ 「我去天瓏書店翻書的時候，看到有些書提到『雙指標』，但其實根本沒有雙指標這種東西，只有『指標的指標』，這兩個是完全不同的東西，就像『雙馬尾』跟『馬尾的馬尾』是完全不同的東西，所以拜託看到有『雙指標』的 C 語言的書就不要買了。」  
+ 「要看懂 C 語言的規格書，你得先會微積分。所以微積分很重要的，趕快去複習一下。」(註：Function Designator 的部份)  
```c  
// 這句應該是指 function designator 的這種狀況  
  
int main() {  
    return (********puts)("Hello");  
}  
  
// 不管有幾個 * 結果都一樣  
// 就像 e^x 對 x 微分不管微幾次結果都是 e^x  
```  
+ 「Function Designator 的 Designator 不要唸成跟 Design 一樣，它的 i 是短音的。」  
    + 附上音標  
```  
$ zdict designator  
designator  
KK[͵dɛzɪgˋnetɚ] DJ[͵dezigˋneitə]  
n.名詞  
  1. 指示者；指定者  
```  
+ 「lvalue 和 rvalue 是很複雜的東西，不是只有在等號左邊或等號右邊的意思，今天時間不夠，所以我不想跟你講。」  
+ 「很多人都以為字串很簡單，但不對，自從 C99 以後，字串非常複雜。」  
+ 「世界上有個很神奇的 Compiler 叫作 Microsoft C compiler，他不支援直接使用 UTF-8。」  
+ 「C 的 Array 只是 Pointer 的 syntax sugar，但寫法並不是所有情況都可以互換，只有當作 function definition 的 parameter 時可以互換。如果是 extern 的時候換成 pointer 方式的寫法的話，產生出來的組合語言是完全不一樣的，這件事說來慚愧，我是寫了程式 10 年以後才知道的，是某次在處理 JVM 的程式碼的時候發現的。」  
+ 「C 其實沒有 Array 這個東西，真正的名字是 Array Subscripting，它只是一種 pointer 的表示法。」  
+ 「你之所以看不懂 Linux Kernel，往往不是因為 Linux Kernel 很複雜，而是你不懂 C 語言。」  
+ 「在 C99，有個很麻煩的東西叫 lvalue，l 不是 left，不是在等號左邊的意思，而是 object locator, l 是 locator 的意思。然後這在 C++ 裏面又被重新定義了，這又是另外一回事了。」  
+ 「C 從 1972 被發明出來開始是沒有 float 的，只有 double，float 在 1985 的 IEEE754 制定時才出現，然後在 1989 年才確定。」  
+ 「C 和 C++ 在 1999 年以後就兵分兩路了，雖然他們還是有共同的地方，但請把他們兩個當作不同的語言來學。」  
+ 「如果你貿然得想從 Linux Kernel 去學習作業系統和 C 語言的話，往往會吃很大的虧，因為 Linux Kernel 用到了很多 C 語言的東西，而且還用到了不少 Undefined Behavior。」  
+ 和作業系統相關概念的共筆：<http://hackfoldr.org/oscar>。  
+ 歡迎訂閱這個粉絲專頁 <https://www.facebook.com/JservFans/> 會不時的分享一些和 Open Source 有關的消息。  
