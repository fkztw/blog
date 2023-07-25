Title: SITCON 2015 - Android Repackaged App Detection System  
Slug: sitcon-2015-android-repackaged-app-detection-system  
Date: 2015-03-11 23:14:27  
Authors: fkz  
Category: Talk  
Tags: Conf, SITCON, Python, Perl, Java, JavaScript, Scrapy, NetworkX, SAAF, node.js, d3.js, Android, Note, Thought  
Summary: 今年投稿 SITCON 有幸又被錄取為講者，對於目前沒有打算唸研究所的我，應該也是最後一年當講者了吧，記錄一下今年的感想。  
Modified: 2015-03-12 00:05:27  
  
  
先說說關於今年 SITCON 的感想好了  
關於 Talk 的部分可能會敘述比較長XD  
  
## 關於 SITCON 2015  
  
今年我除了聽最前面兩場由梁伯嵩及 Kaede 主講的 keynote 以外  
其他都沒有聽 因為都在做簡報 XDrz  這種趕死線的壞習慣真的該改...  
（但不知道為啥每次靈感都會在死線前有如泉湧）  
  
能夠見到看到 CCCA 創社社長梁伯嵩先生的演講真的很感動  
從網路的起始開始講起  
再提到當時 CCCA 在交大做的那些開路先鋒的事  
至今在社辦都還找得到當年的文件、書籍及辦活動留下來的物品  
雖然現在待的這個社團或許在歷史上有些紛紛擾擾  
但我仍認為這個社團的前身就是 CCCA  
以過去那些 CCCA 的前輩為榜樣  
參加 Conf 真的是讓自己疲憊的身心再次注入熱血的動力  
  
Kaede 介紹的廣義的駭客  
現場有些學生可能無法接受  
但看過許多駭客文化的介紹或許就比較能夠了解  
Hacker 是無論哪個領域都有的  
只要你非常專注于該領域 然後闖出了一番傑出的表現 甚至是造福這個世界  
都可以被稱作為 Hacker  這是個尊稱 而不是被現今媒體抹滅的污名  
  
今年最猛的大概就是在 R0 的超華麗的導播設備了  
據說是跟金馬獎用的同一套  
還有在 R0 比較後面的區域加掛了螢幕  
讓後面的人也能清楚看見台上的人的演說神情  
真的很過癮  
感謝辛苦的工作人員們 帶給我這麼一場精彩的會議  
  
剩下的時間真的都是在趕簡報  
順便跟剛好遇到的 jserv 聊天  
真的很佩服 jserv 的犧牲奉獻精神  
在聊天的過程中也感受到自己的某些觀念還不夠成熟  
跟資工相關的許多觀念也還唸的不夠透徹  
意識到自己只是一味的喜歡 coding  
卻忽略了 Algorithm, Data Structure, Operating System, Computer Organization, Assembly 等等  
那些課本上的知識  
或許是因為當時被迫考試的關係 才感到厭惡  
現在回頭過來其實蠻後悔自己沒有認真把那些前人的智慧化為己用  
是時候趁著這股動力和熱血 把那些遺忘的觀念複習一下了  
偷偷附上一張與 jserv 的合照  
![with jserv](/files/sitcon-2015-android-repackaged-app-detection-system/jserv.jpg)  
圖片原連結：<https://www.flickr.com/photos/sitcon/16818827202/in/set-72157649003614643>  
  
雖然第一年因為幫忙 Open House 而沒參與到 SITCON (當時還在台科大舉辦)  
但第二屆和第三屆都有幸成為講者  
也許也是最後一次了吧  
目前沒有繼續往研究所升學的打算  
大概今年就要去從容就義 報效國家了XD  
真的希望資訊教育能夠持續的推廣下去  
  
---  
  
## 關於本次的 Talk  
  
### Android Repackaged App Detection System  
  
本次演講的投影片在此  
<https://speakerdeck.com/fkz/sitcon2015-android-repackaged-app-detection-system-by-shunyi>  
<script async class="speakerdeck-embed" data-id="6ab309bf1d5f42ecbeb4bace486631e8" data-ratio="1.33333333333333" src="//speakerdeck.com/assets/embed.js"></script>  
  
主要就是介紹在大學時做的專題  
因為嘗試將許多現有的開放原始碼軟體整合起來  
剛好跟今年的主題 The Ture Hacker 相呼應  
投影片裡也有提到原因  
主要就是 esr ([Eric S. Raymond - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/Eric_S._Raymond))  
在網路上的一篇知名文章 [How To Become A Hacker](http://www.catb.org/esr/faqs/hacker-howto.html)  
裡頭提到了  
  
> **No problem should ever have to be solved twice.**  
> Creative brains are a valuable, limited resource.  
> They shouldn't be wasted on re-inventing the wheel when there are so many fascinating new problems waiting out there.  
  
這個專題真的結合了很多現有的 Open Source 專案去達到我們想做的事  
最後一頁的投影片列出了所有用到的 Open Source 專案  
過程中也學到了很多東西  
Dalvik, smali, baksmali, Data Dependence, Flow Dependence, ...  
嘗試了很多語言和相關的專案  
  
+ Perl  
+ Python  
    + Scrapy  
    + NetworkX  
+ Java  
    + Unofficial Google Play API  
    + SAAF  
+ JavaScript  
    + Node.js  
    + D3.js  
  
其實中間也 survey 了很多不同的工具  
雖然最後沒有採用  
依稀記得的有  
Wala, graph-tool 以及各種 Unofficial Android third party marketplace API  
也很感謝陳仲寬學長在這過程之中給我們很大的幫忙  
無論是在傳授給我們相關的知識亦或是給予我們相關論文來閱讀  
還有國科會計劃申請書的參考範本也是來自學長當年的申請書  
  
雖然這個專案離我們當初構想的最後完成體還差的有點多  
原本預計還要加入 Machine Learning 讓判斷相似度的部分可以更自動及更有系統地分析  
以及想要利用 Open Stack 亦或是 Docker 進行部署  
採用雲端運算加快相似度比對的速度  
這些都因為自身能力不足  
而無法如期的完成到這個部分  
老實說 就連相似度的 threshold 要訂在哪我們都還不是很有把握  
  
話說國科會計劃的結報好像也快到了該交出的死線日期了  
至少三月底前要交出吧？  
希望可以利用這幾天的時間把結報寫一寫  
然後把 Source Code 整理後釋出  
因為要用到各種不同的 Open Source Project  
所以開始學習怎麼用 git submodule  
Python 純粹是因為個人喜好所以採用  
而 JavaScript 則是當時想碰 所以就用了  
也感謝我的好夥伴兼好室友江泓樂配合我採用各種程式語言的任性  
感謝強者小樂常常在看論文方面給我蠻大的幫助  
因為我不是那麼喜歡看論文XDrz  
以及在我大三同時兼任  
系計中助教、Open House 資訊組組長、網路福利社社長、汪汪社副社長  
還修了一堆課 忙碌到擠不出什麼時間 導致有時無故缺席 meeting 的時候  
還能包容我 告訴我預計的進度應該到哪  
  
Trace 許多 Source Code 之後  
仍然深深感到自己的能力不足  
看 Code 及理解 Code 的速度不夠快  
在自己撰寫程式碼的方面  
也明顯感受到了開發經驗與速度的不足  
各種方面都還有待加強  
  
在農曆新年後 以這場 Talk 作為新年的開始  
希望新的一年 自己也能不斷地學習新的知識  
把想唸的書唸完 繼續增強自己的開發能力  
向那些 True Hackers 看齊 利用自己所掌握的資訊開發能力  
努力讓這個世界變得更好  
  
寫到這邊突然好想再重看一次[黑客列傳：電腦革命俠客誌(25週年紀念版)](http://www.books.com.tw/products/0010548392)  
讓自己回到半世紀前 感受當時那些時代先驅們的熱血精神  
  
---  
  
## SITCON 2015 相簿連結  
+ [Sitcon 2015 - an album on Flickr](https://www.flickr.com/photos/sitcon/sets/72157649003614643/)  
+ [Sitcon2015 幕後花絮 - an album on Flickr](https://www.flickr.com/photos/sitcon/sets/72157649027037894/)  
+ [SITCON2015 by 海哥 - an album on Flickr](https://www.flickr.com/photos/sitcon/sets/72157650915441780/) // 這個拍超多妹子...  
