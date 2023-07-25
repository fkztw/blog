Title: 《編程人生》(Coders at Work)  
Slug: coders-at-work  
Date: 2016-06-16 10:07:42  
Authors: fkz  
Category: Reading  
Tags: Programmer, Book  
Summary: 《編程人生》讀後感  
Modified: 2016-06-16 20:54  
  
  
# 前言  
  
其實這篇算重寫一次...  
之前其實有寫好了，  
而且當時已經拖了一個多月，  
但是因為跟 git 還是不夠熟，  
在為了新的 Makefile 做一些新的實驗時，  
不小心把 git repo 搞炸了，  
所以只好重新 clone...  
然後就拖到了現在，  
算起來離看完這本書過了三個月了，  
只好憑印象寫一下心得，  
剛好順便復習一下裡頭的內容。  
  
---  
  
# 心得  
  
原文是這本：  
  
+ [Coders at Work: Reflections on the Craft of Programming](http://www.codersatwork.com/)  
  
於 2009/09/16 出版  
  
但我看的是在若水堂買的簡中翻譯版，分成上下冊兩本：  
  
+ [編程人生：15 位軟件先驅訪談錄 (上卷)](http://www.waterlike.com.tw/bookdata.asp?NO=TP3C153043)  
+ [編程人生：15 位軟件先驅訪談錄 (下卷)](http://www.waterlike.com.tw/bookdata.asp?NO=TP3C153044)  
  
於 2015/01 出版 （竟然隔了 5 年多才被翻譯，個人覺得有點罕見。）  
  
作者總共訪談了 15 位在資訊界都有著極大貢獻的人物，  
上冊的 8 位：  
  
+ 第 1 篇 [Jamie Zawinski](http://www.codersatwork.com/jamie-zawinski.html)  
    + Mozilla 計劃的先驅及主要貢獻者之一  
    + XScreenSaver 的 Contributor  
+ 第 2 篇 [Brad Fitzpatrick](http://www.codersatwork.com/brad-fitzpatrick.html)  
    + LiveJournal, Memcached, OpenID 的 Owner  
+ 第 3 篇 [Douglas Crockford](http://www.codersatwork.com/douglas-crockford.html)  
    + "JavaScript: The Good Parts" 的作者  
    + Yahoo! 資深 JavaScript 架構師  
+ 第 4 篇 [Brendan Eich](http://www.codersatwork.com/brendan-eich.html)  
    + JavaScript 之父  
    + Mozilla 計劃的共同發起人，當過 Mozilla 的 CTO 和 CEO  
+ 第 5 篇 [Joshua Bloch](http://www.codersatwork.com/joshua-bloch.html)  
    + "Effective Java" 的作者  
    + 曾任職於 Sun 和 Google，在 Google 是擔任 Chief Java Architect  
+ 第 6 篇 [Joe Armstrong](http://www.codersatwork.com/joe-armstrong.html)  
    + Erlang 之父  
+ 第 7 篇 [Simon Peyton Jones](http://www.codersatwork.com/simon-peyton-jones.html)  
    + Haskell Contributor, Glasgow Haskell Compiler (GHC) 的主力開發者和架構師  
+ 第 8 篇 [Peter Norvig](http://www.codersatwork.com/peter-norvig.html)  
    + Director of Research at Google  
    + co-author, with Stuart Russell, of "Artificial Intelligence: A Modern Approach"  
    + was head of the Computational Sciences Division (now the Intelligent Systems Division) at NASA Ames Research Center  
  
下冊的 7 位：  
  
+ 第 1 篇 [Guy Steele](http://www.codersatwork.com/guy-steele.html)  
    + <https://en.wikipedia.org/wiki/Guy_L._Steele_Jr.>  
    + 寫過非常多種程式語言  
    + 參與過許多程式語言的制定過程，是 Common Lisp 和 Scheme 的作者之一，也參與了 Fortran, C, ECMAScript 的標準制定過程。  
    + 曾被 Bill Joy 邀請加入 Sun 幫忙訂定 Java 的標準。  
    + ACM Grace Murray Hopper Award 1988 年得主。  
+ 第 2 篇 [Dan Ingalls](http://www.codersatwork.com/dan-ingalls.html)  
    + <https://en.wikipedia.org/wiki/Daniel_Henry_Holmes_Ingalls,_Jr.>  
    + 物件導向先驅之一  
    + 對於 Smalltalk 程式語言貢獻極多，1976 年設計了 bytecoded virtual machine 使得 Smalltalk 得以實作。  
    + ACM Grace Murray Hopper Award 1984 年得主。  
+ 第 3 篇 [L Peter Deutsch](http://www.codersatwork.com/l-peter-deutsch.html)  
    + <https://en.wikipedia.org/wiki/L_Peter_Deutsch>  
    + 11 歲開始寫程式，過沒多久就開始在 MIT 閒晃，在 PDP-1 上實作 Lisp，和比自己年紀大了快兩倍的 MIT Hackers 一起寫程式。（有出現在[《黑客列傳：電腦革命俠客誌》（Hackers: Heroes of the Computer Revolution）](http://www.books.com.tw/products/0010548392) 這本書裏面）  
    + 在 UC Berkeley 當大二生的時候，他參與了 Project Genie（最早的 minicomputer-based timesharing system 之一），他負責撰寫這個作業系統大部分的 kernel。  
    + 在 Project Genie 商業化失敗後，他到了 Xerox PARC 這間公司，負責 Interlisp system 和 Smalltalk virtual machine，協助 JIT compilation 技術的部份。  
+ 第 4 篇 [Ken Thompson](http://www.codersatwork.com/ken-thompson.html)  
    + <https://en.wikipedia.org/wiki/Ken_Thompson>  
    + MULTICS, UNIX, B programming language, Plan 9, UTF-8, golang  
    + 1983 年圖靈獎得主之一 （和 Dennis Ritchie 共同獲得）  
+ 第 5 篇 [Fran Allen](http://www.codersatwork.com/fran-allen.html)  
    +  <https://en.wikipedia.org/wiki/Frances_E._Allen>  
    + 2006 年圖靈獎得主  
    + 在 IBM 待了 45 年，負責一系列的編譯器相關的專案。  
    + 似乎是這本書的受訪者裡頭唯一一位女性  
+ 第 6 篇 [Bernie Cosell](http://www.codersatwork.com/bernie-cosell.html)  
    + 參與了 ARPANET 早期使用的 IMP (Interface Message Processors) 的實作。  
    + 在 BBN 待了 26 年，基本上裡面的專案都有碰，因其精湛的除錯技巧，而贏得了 Master debugger 跟 Fixer 的稱號。  
+ 第 7 篇 [Donald Knuth](http://www.codersatwork.com/donald-knuth.html) （高德納）  
    + <https://en.wikipedia.org/wiki/Donald_Knuth>  
    + "The Art of Computer Programming" 一書的作者  
    + TeX, METAFONT  
    + 1971 年 Grace Murray Hopper Award 得主、1974 年圖靈獎得主、1995 年 John von Neumann Medal 得主、...  
  
因為作者 Peter Siebel 本身也是會寫程式的人，  
然後對整個圈子的生態和歷史也很瞭解，  
所以問的許多問題都還蠻犀利的，  
除了問每一位受訪者共同的問題，像是：  
  
+ 「你對其他工程師推薦哪些書籍？」  
+ 「你有看完 The Art of Programming 嗎？你對這本書的想法是什麼？」  
+ 「你覺得自己應該算是下列哪一項：藝術家？工程師？建築師？專家？程式設計師？」  
+ 「你覺得數學對於寫程式有沒有幫助？是不是每一位寫程式的人都要會的？」  
+ 「在你寫程式的生涯中，遇到最棘手的 Bug 是哪類型的？你當時怎麼解決的？」  
+ 「如果讓你重選一次，你還會寫程式嗎？」（我記得應該有這問題，沒有的話就是我記錯了。）  
  
其中也有針對受訪者詢問不同的軟體工程相關問題：  
  
+ 「你認為 Pair Programming 對於寫程式有沒有幫助？」  
+ 「你對 Agile Programming, Extreme Programming 和 Waterfall 有什麼看法？」  
+ 「你認為 unit testing 是不是必須的？」  
+ 「你對於 Marting Fowler 的《人月神話》和《沒有銀彈》有什麼看法？」  
+ 「你開發一個程式的時候是習慣 Top-down 還是 Bottom-up？」  
+ 「接手一個程式的時候你是傾向重寫它還是瞭解之前的人在寫什麼然後試圖修改它？」  
+ 「你有寫文件的習慣嗎？你覺得寫文件的重要性如何？」  
+ 「你對 Code Review 有什麼看法？你覺得對開發有幫助嗎？」  
  
也會針對受訪者問個別的問題：  
  
+ Jamin Zawinski  
    + Netscape 和 Firefox 當時的狀況  
    + Lisp  
+ Brad Fitzpatrick  
    + LiveJournal, Memcached, OpenID, Go  
+ Douglas Crockford  
    + JavaScript, JSON, JSLint, JSMin, FORTRAN  
+ Brendan Eich  
    + JavaScript 的誕生、設計過程、優缺點以及未來有哪些計劃  
+ Joshua Bloch  
    + Java 還有關於 SUN 和在 Google 的經驗  
+ Joe Armstrong  
    + Erlang 的開發過程和未來的想法  
+ Simon Peyton Jones  
    + Haskell 和開發 GHC 的經驗談  
+ Peter Norvig  
    + NASA, AI, Google  
+ Guy Steele  
    + （忘了）  
+ Dan Ingalls  
    + （忘了）  
+ LPeter Deutsch  
    + （忘了）  
+ Ken Thompson  
    + 針對 UNIX 的開發還有問一些 Denis Ritchie 的事  
+ Fran Allen  
    + （忘了）  
+ Bernie Cosell  
    + （忘了）  
+ Donald Knuth  
    + 問 LaTeX 還有 The Art of Programming  
  
而且由於受訪者的領域和慣用語言不盡相同，  
所以每個人的想法也都不太一樣，  
但也沒有說誰對誰錯的問題，  
每個人都因為自己的成長過程和人格特質而對寫程式這件事有不同的見解，  
我想這也證明了這個圈子的多元性。  
  
但其中也有一致認同的地方，  
像是：  
  
+ 「數學雖然不是必須的，但對寫程式有一定程度以上的幫助。」  
+ 「寫程式是很花時間及講求經驗的」  
  
我覺得如果有個把作者問所有受訪者的共同問題和回答整合起來的筆記應該會很有趣。  
  
整本書看下來讓我覺得就像是看著作者和受訪者在眼前對談，  
甚至從文字中的描述我就能感受到每位受訪者不同的風格，  
所以我選擇慢慢品嚐，然後就花了兩個月才看完。Orz  
不知道為啥我看程式相關的書籍的速度都特別慢...  
之後應該會選擇看快一點吧，  
反正正常看也是會忘，  
看太慢也是會忘，  
那倒不如看快一點還有機會多看幾次。  
  
---  
  
# References  
  
+ [Coders at Work: Reflections on the Craft of Programming](http://www.codersatwork.com/)  
+ [Coders at work - Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Coders_at_work)  
+ [PARC (company) - Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/PARC_(company))  
+ [ruanyf on Twitter: "Erlang语言的发明者Armstrong回忆说：“刚进公司时，我喜欢帮别人Debug，同事会买杯啤酒感谢我。后来，我们就用啤酒表示bug的难度，这个是两杯啤酒bug，那个是三杯啤酒bug……” #书摘"](https://twitter.com/ruanyf/status/743420600840912898)  
