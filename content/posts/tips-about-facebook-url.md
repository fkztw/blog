Title: Facebook 網址的一些黑魔法  
Slug: tips-about-facebook-url  
Date: 2018-01-02 23:02:27  
Authors: m157q  
Category: Note  
Tags: Facebook, 2018 iT 邦幫忙鐵人賽  
Summary: 其實 Facebook 的網址列針對單一使用者時，已經可以算是 API 了，所以可以透過在網址列加上一些東西，拿到某個使用者滿多進一步的訊息的，這篇文章會稍微介紹一下。  
Modified: 2019-06-25 21:06:27  
  
  
### 2019/06/25 UPDATE  
  
Facebook no longer accepts Graph Search URLs.  
Check related sources below:  
  
- <https://gist.github.com/nemec/2ba8afa589032f20e2d6509512381114>  
- <https://intelx.io/tools?tab=facebook>  
- <https://sowdust.github.io/fb-search/>  
  
---  
  
## TL;DR  
  
<https://netbootcamp.org/facebookpeoplesearchtips/>  
  
---  
  
## 前言  
  
去年因為一些事件得知 Facebook 的網址列可以針對單一使用者作滿多查詢的，當下就有紀錄起來，但遲遲沒有整理成一篇文章。其實也是看到有人講了以後去做了些查詢，發現這篇英文文章：[Facebook People Search Tips | OSINT Training by Bob Brasich](https://netbootcamp.org/facebookpeoplesearchtips/) 整理的挺完整的，所以這篇文章算是擷取整理這篇文章的內容，然後以中文呈現。  
  
---  
  
## 要先知道什麼是 Facebook User ID  
  
首先，你要知道你想查詢的使用者在 Facebook 上的 ID 是什麼，對這個有點概念的人都會知道這是一串流水號，而最常見的例子就是 Facebook 創辦人 Mark Zuckerburg 本人的 Facebook ID 是 4，所以你只要連到 <https://www.facebook.com/4>，就會連到 Mark Zuckerburg 本人的 Facebook 頁面，而每一位 Facebook 使用者都會有這樣一個不與其他使用者重複的流水號作為其 Facebook 的 ID。  
  
在接下來的使用方式裡頭，一定要拿到使用者的 ID，拿到使用者自己自訂的唯一 username 是沒用的。  
  
---  
  
## 要怎麼拿到 Facebook 使用者的 ID？  
  
如果該名使用者沒有自訂 username 的話，只要連到該名 Facebook 使用者的個人頁面後，檢查一下網址列，就會看到最後面應該會是一串數字，那個就是該名使用者的 Facebook ID。  
  
如果該名使用者有自訂 username 的話，你連到他的 Facebook 個人頁面應該會看到網址最後面就是他自訂的 username，而不會是 Facebook User ID。這時候可以透過這個網頁來做查詢：<https://findmyfbid.in>，這個網站本身就有教學了，用法也很簡單。  
  
一樣是連到該名 Facebook 使用者的個人頁面，把他的網址複製下來，然後貼到 <https://findmyfbid.in> 進行查詢就行了。如果有順利查詢到的話，就會得到代表該名 Facebook 使用者的一串數字，即為其 ID。  
  
---  
  
## 拿到 ID 後？  
  
就可以進入正題了，一般人在 Facebook 進行搜尋的時候，應該普遍都是透過網頁上方的 Search bar 進行搜尋吧？這些查詢的結果都是透過 API 進行搜尋的，其實可以透過修改網址直接得到查詢結果，操作方式也不難，以下簡單講解。  
  
---  
  
## 基本格式  
  
最基本的網址格式長的像這樣：  
  
`https://www.facebook.com/search/str/$FACEBOOK_USER_ID`  
  
也可以是  
  
`fb.com/search/str/$FACEBOOK_USER_ID`  
  
以 Mark Zuckerburg 為例的話，就會是：  
  
`https://www.facebook.com/search/str/4`  
  
或是  
  
`fb.com/search/4`  
  
知道了這個基本格式以後，接下來會加上的參數都是加在後面，就可以得到相對應的搜尋結果，這個方法可以用在所有的使用者身上，但得到的結果會是以你登入的 Facbeook 帳號權限而定，並不會得到該名使用者所有的資訊，除非你是查詢你目前登入的 Facebook 使用者。  
  
---  
  
## 基本參數  
  
以下參數都是直接接在上面提到的基本格式字串的後面就行了，會是這樣的形式：  
  
`fb.com/search/str/$FACEBOOK_USER_ID/$OPTION`  
  
舉例來說，如果選項是下面提到的 `/photos-by/` 的話，就會是這樣使用：  
  
[`fb.com/search/4/photos-by/`](http://fb.com/search/4/photos-by/)  
  
其他參數依此類推，以下就列出有哪些參數可以使用，因為這些參數其實都已經和使用英文版 Facebook 搜尋時會顯示的一般英文一樣了，所以就不多做說明，有興趣的人可以試一試。  
  
### 和發文有關的  
  
+ `/stories-by/`  
+ `/stories-liked/`  
+ `/stories-commented/`  
+ `/stories-publishers/`  
+ `/stories-tagged/`  
+ `/stories-media-tagged/`  
+ `/stories-in/`  
+ `/stories-topic/`  
+ `/stories-news/`  
+ `/stories-recent/`  
+ `/reshare-stories-by/`  
+ `/reviews-at/`  
+ `/hashtag/`  
  
### 和照片有關的  
  
+ `/photos-by/`  
+ `/photos-uploaded/`  
+ `/photos-of/`  
+ `/photos-tagged/`  
+ `/photos-in/`  
+ `/photos-keyword/`  
+ `/photos-liked/`  
+ `/photos-commented/`  
+ `/photos-interested/`  
+ `/photos-interacted/`  
+ `/photos-recommended-for/`  
+ `/recent-photos/`  
  
### 和按讚有關的  
  
+ `/stories-liked/`  
+ `/photos-liked/`  
  
### 和留言有關的  
  
+ `/stories-commented/`  
+ `/photos-commented/`  
  
### 和打卡、地點、評論有關的  
  
+ `/recent-places-visited/`  
+ `/places-visited/`  
+ `/places-checked-in/`  
+ `/visitors/`  
+ `/places-named/`  
+ `/places-in/`  
+ `/places-near/`  
+ `/places-reviewed/`  
+ `/pages-in/`  
+ `/stories-at/`  
+ `/reviews-at/`  
+ `/events-at/`  
+ `/events-near/`  
+ `/residents/`  
+ `/home-residents/`  
+ `/users-birth-place/`  
  
---  
  
## 結論  
  
善用這些搜尋網址可能可以在 Facebook 上做更有效的搜尋，有些是透過預設的搜尋介面比較難選取到的部份，參考的這篇文章：[Facebook People Search Tips | OSINT Training by Bob Brasich](https://netbootcamp.org/facebookpeoplesearchtips/) 裡頭還有提到一些更進階的小技巧，可以結合兩個參數做搜尋，例如搜尋某間公司擁有某個名字的 Facebook 使用者、搜尋住處在某個地方擁有某個姓名的使用者、……等等，像下面這些參數就是可以用來做更進階一些搜尋用的參數：  
  
+ 和時間有關的  
    + `/yesterday/`  
    + `/today/`  
    + `/this-week/`  
    + `/last-week/`  
    + `/recent/`  
    + `/this-month/`  
    + `/last-month/`  
    + `/this-year/`  
    + `/last-year/`  
    + `/YEAR/`  
    + `/before/ /after/`  
+ 和關鍵字有關的  
    + `/stories-keyword/`  
    + `/photos-keyword/`  
+ 和名字有關的  
    + `/users-named/`  
    + `/pages-named/`  
  
這部份必須要在網址最後加上 `/intersect/`，表示取這幾個選項的交集做搜尋，格式也有稍稍的不太一樣，這邊就不做詳細的介紹，有興趣的人可以再點下面參考文章的第一篇進去察看，裏面有滿多實際例子的。  
  
---  
  
## 參考資料  
  
+ [Facebook People Search Tips | OSINT Training by Bob Brasich](https://netbootcamp.org/facebookpeoplesearchtips/)  
+ [Find Facebook ID in two simple steps | Find Facebook ID](https://findmyfbid.in/)  
