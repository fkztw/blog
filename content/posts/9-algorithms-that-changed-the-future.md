Title: 《改變世界的九大演算法》  
Slug: 9-algorithms-that-changed-the-future  
Date: 2016-09-18 18:39:31  
Authors: fkz  
Category: Reading  
Tags: Algorithm, Computer Science  
Summary: 《改變世界的九大演算法》讀後感  
Modified: 2016-09-19 22:38  
  
  
![front cover](/files/9-algorithms-that-changed-the-future/front-cover.jpg)  
![back cover](/files/9-algorithms-that-changed-the-future/back-cover.jpg)  
  
---  
  
## Preface  
  
這本書在 5 月多的時候逛信義誠品的時候就有看到了，  
當時稍微翻了一下，  
覺得寫還不錯，  
但因為已經有買其他的書了，  
而且覺得書的性質比較偏向科普，  
內容應該都知道，  
所以當時沒買。  
然後今年 COSCUP 2016 的時候在天瓏的攤位又看到這本，  
就買來看了。  
  
---  
  
## Note & Thought  
  
裏面所講的九大演算法就是在封底有提到的：  
（其實我覺得不應該說演算法， 應該說是資訊技術好像比較恰當。）  
  
1. Search Engine Indexing  
2. Page Rank  
    + 促成 Google 崛起的那篇論文的一些基本概念。  
3. Public-key Cryptography  
    + 講些對稱加密和非對稱加密的基礎概念，還有當然一定會提到一下 RSA，沒有細講。  
4. Error-correcting Codes  
    + Error Detection 和 Error Correction 都有提到，我印象中沒有提到 Grey code，然後 Hamming Code 只有帶過而已，但基本上就是講 Hamming Code 的概念。  
5. Pattern Recognition  
    + 人工智慧的部份，一定會提到的 NIST 的手寫辨識等等。  
6. Data Compression  
    + 壓縮的技術，這部份個人覺得是計概書和大學課程比較少著墨的部份。簡單講解了一些基本的資料壓縮的概念。  
7. Databases  
    + 一定會提到的關聯式資料庫之父： [Edgar F. Codd](https://en.wikipedia.org/wiki/Edgar_F._Codd)。提到了 Relational Algebra，然後再以 SQL 作為例子講一下儲存在資料庫裡的範例，對於 NoSQL 就沒有提及了。  
8. Digital Signature  
    + 這部份跟講加密的那個章節有些關聯，也是本書裏面章節篇幅比較長的部份，花了滿多時間在試圖簡化整個數位簽章的概念，讓讀者可以更好理解。  
9. 如果存在的話將會很了不起的演算法  
    + 其實我沒有很明白作者這裡指的是什麼，第十一章的結論中有一節提到「頗具潛力的演算法」，提到以下幾種：  
        + 新的但還未出現的跟 Pattern Recoginization 有關的演算法  
        + [Zero-knowledge Protocol](https://en.wikipedia.org/wiki/Zero-knowledge_proof)  
            + 和資訊安全有關，不知道是不是因為比較新，所以在修密碼學和資安概論的時候都沒看過這東西。  
        + Distributed Hash Table  
        + Byzantine fault tolerance （拜占庭容錯）  
            + 看來跟之前在 COSCUP 2016 的 Docker Workshop 學到的[拜占庭將軍問題](https://zh.wikipedia.org/zh-tw/%E6%8B%9C%E5%8D%A0%E5%BA%AD%E5%B0%86%E5%86%9B%E9%97%AE%E9%A2%98)是一樣的東西，在講 Distributed Computing 中，點對點通訊時如何處理錯誤的訊息。  
  
作者也有在前言裡頭講到，  
他挑的這些都已經是目前普通人天天都會用到的東西了，  
所以這本書並不適合對演算法已經有一定程度瞭解的人閱讀，  
因為不是想像中的去比較各個領域中演算法的優缺點。）  
  
裏面印象比較深刻的就是第四章講非對稱加密的部份，  
用了混合油漆的例子來比喻 Diffie-Hellman Key exchange 及非對稱加密的過程。  
這裡有[一部影片](https://www.youtube.com/watch?v=YEBfamv-_do)跟[一則 tweet](https://mobile.twitter.com/JZdziarski/status/753640015108841472) 作為詮釋。  
要是我當年修密碼學的時候可以早點知道這樣的解釋也許會學的比較好吧？  
  
之前修密碼學的時候，  
剛碰到這部份也是有點一頭霧水。  
尤其是一開始的部份沒理解清楚的話，  
到之後的 X.509 憑證交換的部份又會更難理解。  
  
這邊又想到之前看到[一則 tweet](https://twitter.com/JZdziarski/status/753223642297892864) 用 emoji 來講 Public Key Infrastructure，也是很簡單易懂。  
因為覺得很重要，所以截個圖好了。  
![Explain PKI in emoji way](/files/9-algorithms-that-changed-the-future/pki-emoji.png)  
  
  
這本書本來就定位為科普書籍，  
所以作者儘量以非常簡單的例子來比喻，  
我覺得這是本書值得看的部份。  
  
適合對資訊技術有興趣但沒有相關基礎的大眾閱讀，  
我不會說他很平易近人，  
即便作者已經用很簡單且省去很多細節的方式描述，  
但畢竟描述的都是一些有重大影響力的論文或是概念，  
所以還是會需要些時間來瞭解。  
但真的已經比普通大學資工課程裡所學的內容還易懂，  
個人覺得挺適合高中畢業已經考上大學資工系的學生當成簡單的計概書來唸唸。  
  
以我這個修完大學資工系課程的學生來說，  
大部分的內容都是我已經知道的基本概念，  
但還是有學到我不曾聽過的東西，  
像是：Zero-knowledge protocol，  
而且書中有些比喻真的是修課的時候沒有理解到的。  
  
這本書是 2012 年出版的，  
比較有印象的是在第十章探討電腦能夠解決哪些問題的極限時，  
還把電腦無法像人一樣駕駛汽車列了出來，  
但在今年，自動駕駛已經不是什麼稀奇的事了，  
真的感受到科技變革的快速。  
  
個人覺得這本書比較可惜的部份是對網際網路這塊沒提到，  
例如網路的通訊原理、TCP/IP、ARPA Net、World Wide Web 的出現等等。  
然後可能是因為譯者不是資工相關領域的，  
所以有些跟資工領域相關的翻譯我自己覺得是有點怪怪的，  
沒那麼到位的感覺。  
  
總體而言我還是覺得這本書可以看一下，  
但對於資工領域相關知識和歷史已經有一定程度瞭解的人來說，  
我就不建議閱讀這本書了，  
因為看了一定會覺得這本書省略了太多的細節 XD  
（比如說在提到某個演算法的時候沒有提到作者、  
提到著名的 [1956 Dartmouth Conference](https://en.wikipedia.org/wiki/Dartmouth_Conferences) 的時候，  
沒有提到 Marvin Minsky, John McCarthy，  
只有說 Claude Shannon 有參與）  
  
---  
  
## Related Links  
  
+ [9 Algorithms that Changed the Future - Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/9_Algorithms_that_Changed_the_Future)  
+ [Zero-knowledge Protocol](https://en.wikipedia.org/wiki/Zero-knowledge_proof)  
+ [拜占庭將軍問題](https://zh.wikipedia.org/zh-tw/%E6%8B%9C%E5%8D%A0%E5%BA%AD%E5%B0%86%E5%86%9B%E9%97%AE%E9%A2%98)  
+ [Public key cryptography - Diffie-Hellman Key Exchange (full version) - YouTube](https://www.youtube.com/watch?v=YEBfamv-_do)  
+ [Jonathan Zdziarski on Twitter: "Diffie-Hellman-Merkle: 💙 - 💙 Common Color  💛 - ❤️ + Secret Colors 💚 - 💜 = Mixture 💜 - 💚 < Swap 💛 - ❤️ + Secret Color ⚫️ - ⚫️ = Common Secret"](https://twitter.com/JZdziarski/status/753640015108841472)  
+ [Jonathan Zdziarski on Twitter: "PKI / PGP Primer: 🔑 Public Key 🗝 Private Key 📝 Message  📝+🔑 = 🔒✉️ Encrypted 🔒✉️+🗝 = 🔓📝 Decrypted 📝+🗝 = 🔏✉️ Signed 🔏✉️ + 🔑 = 👤 Authenticated"](https://twitter.com/JZdziarski/status/753223642297892864)  
