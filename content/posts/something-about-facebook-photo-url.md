Title: Something about Facebook Photo URL  
Date: 2014-04-15 19:40  
Author: fkz  
Category: Note  
Tags: facebook, URL  
Slug: something-about-facebook-photo-url  
Modified: 2015-10-26 14:57  
Summary: 因為好奇而研究了一下一長串的 Facebook URL  
  
  
有 Facebook 相關開發經驗的應該就不必看了  
  
以最近很紅的一段網址來舉例  
  
```  
https://www.facebook.com/photo.php?fbid=710043139058199&set=a.231514793577705.59041.100001575585223&type=1  
```  
  
+ 其中 `fbid=710043139058199`，710043139058199 為此照片的ID，把這串數字接在 `www.facebook.com/` 後面，就會連到該張照片的網址。ex: <https://www.facebook.com/710043139058199> (看不到別怪我) (非循序流水號，估計跟使用者有關係)  
+ 再來是 `set=a.231514793577705.59041.100001575585223`，這邊可以看到三串數字，分別由 . 隔開。  
    + a 估計為 Album 的意思  
    + `231514793577705` 代表該相片所在的相簿。接在 `www.facebook.com/` 後面，可以直接連結到該相簿。 ex:<https://www.facebook.com/231514793577705> (看不到也別怪我)  
    + `59041` 目前未知  
    + `100001575585223` 代表照片上傳者的 Facebook uid。 接在 `www.facebook.com/` 後面，可以直接連結到該使用者的 Facebook 頁面。 ex:<https://www.facebook.com/100001575585223> (看不到還是別怪我)  
+ type 只是相片檢視的模式，不重要。  
  
上面三種不同的連結必須在該使用者有開放相對應的瀏覽權限才看得到  
  
---  
  
另外有一種長這樣，這種應該比較少看到。  
  
`https://www.facebook.com/photo.php?fbid=A&set=t.B&type=3&theater`  
  
+ `fbid=A`: A 和上述的一樣，不再進行贅述。  
+ `set=t.B`  
    + t 估計為 timeline 的意思  
    + 而 B 也會是某個使用者的 Facebook uid。前面接上 `www.facebook.com/` 一樣可以連結到該使用者的 Facebook 個人頁面。  
  
以上自己無聊試出來的  
  
其中 Facebook uid 是流水號，也就是相鄰的數字都會是某個 FB 使用者。  
這個我想很多人應該都知道。  
  
然後官方提供的 <http://graph.facebook.com> 不錯用  
後面接上 /id 就會有 Open Graph 的資料出現  
(官方工具是在 <https://developers.facebook.com/tools/explorer/> 須登入才能使用)  
雖然這部分也會有預設權限就是  
只要對方沒開放瀏覽權限，一樣看不到  
  
有空再來 Google 相關的東西或者翻翻 Facebook API 之類的文件，也許會有啥收穫。  
