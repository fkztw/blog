Title: Facebook Developer Circle: Taipei - Meetup #2  
Slug: facebook-developer-circle-taipei-meetup-2  
Date: 2017-06-22 21:41:20  
Authors: fkz  
Category: Conf/Meetup  
Tags: Facebook, Meetup  
Summary: Note for Facebook Developer Circle: Taipei - Meetup #2  
  
  
+ Event Link: <https://fdctaipei.kktix.cc/events/fdc201706>  
  
---  
  
## Facebook Messenger Platform 現況  
  
Speaker: Sean Liu (urAD co-founder)  
  
### Agenda  
  
+ 為什麼我要做 Bot 相關產品  
+ NLP 的理想與現實  
+ Facebook Messenger Platform 發展方向的一些轉折  
+ Bot 的管理實務  
+ ID Matching  
+ Bot 與 Ad-Tech  
  
### Why Messenger Platform?  
  
+ 下載 App 的人愈來愈少  
+ App 的市場都集中在超級大的 App 上  
+ Messenger Bot 可以利用既有的社交圖譜  
+ 一鍵式 Payment  
+ 微信是非常好的成功案例  
    + 微信 Bot: 微信公眾好  
    + 微信小程序  
    + 創造出了依附在社交圈的龐大經濟體系  
+ Bot 能接觸到我們過往所無法接觸到的私密對話  
    + 人們在使用對話的時候與其平常在網路上的行為是更真實的  
+ 但是，Bot 如何創造價值  
  
### NLP 的理想與現實  
  
+ urAD 和 ChocoLab 合作開發的 CHOCO TV BOT  
    + 花了很多時間在制定彼此之間的 API 格式  
    + 需要從 CHOCO LAB 的 API 拿到影劇和演員的資料建立 Entity  
    + 影劇的別名，例如：冰與火之歌 == 權力的遊戲  
    + 劇名、季數、集數  
+ 現實是你根本無法預期使用者會怎麼跟 Bot 對話，使用者也根本不在乎，常常都會出現 Bot 無法理解的語句，毫無規則可言。  
+ 資料的整理梳理和 NLP 的分詞斷句花了不少時間  
+ Bot vs Google Search?  
    + 做的要死要活的還不如拿去 Google Search 請它幫你？  
    + 想找尋某個特定的場景劇情發生時是在哪一集  
        + 可以把截圖抓出來  
        + NLP 分析使用者的問句  
        + 把影片中的每個 frame 用 ffmpeg 抓出來，丟到 Google Cloud Vision 或 IBM Watson 認出截圖中的 objects，再去建 index。（但建一部影片的 index 的成本極高）  
+ NLP 和 ML 不是黑魔法  
    + 必須要花時間建立 entity 和 [utterance](https://en.wikipedia.org/wiki/Utterance) 並不時修正補強  
+ Context （對話脈絡）  
    + 使用者要找某部作品  
    + 又問了這部劇的演員還演過哪齣劇  
    + 又問了這部劇的平均收視率是多少  
    + Bot 只能回答第一個問題，因為它並不像人一樣預設就可以記住上文的東西 (Context free?)  
+ api.ai, wit.ai, IBM Watson NLP api 有提供前後文關聯的機制  
    + 會幫你去尋找之前的問句的 Entity  
    + 但當 intent 的數量太多的時候，會遇到問題  
  
### Facebook Messenger Platform 發展方向的一些轉折  
  
+ Quick reply  
+ Persistent menu 從 5 個改成 3x5x5 個 menu  
+ Composer Drawer  
    + Messenger 對話欄輸入框最左邊的 + 號 (邊緣人調查 XDDD  
+ Chat Extensions  
+ 小結： AI 還太遙遠，WebView 優先。  
    + 在真的願意花時間和成本去解決 NLP 和 ML 的資料訓練以前，必須要一段不短的時間。  
  
### Bot 的管理實務  
  
+ 和接下來講的 Business Manager 和 ID Matching 有點關係  
  
#### Tokens  
  
Facebook User 不盡然等於 Messenger User  
  
+ User Access Token  
    + 使用者透過 OAuth 去授權你的 Facebook App 後所取得的 Access Token  
+ Page Access Token  
    + 透過 User Access Token 取得 User 的 Facebook 帳號下，擁有管理 Page 權限的 Access Token。  
        + > 這串到底是在工三小 XDDDDD  
+ App Access Token  
+ System User Access Token  
+ Admin System User Access Token  
  
### ID Matching  
  
Global User ID vs ASID vs PSID  
  
> 萬惡的層層 ID 限制 XD  
  
+ ASID: App-Scoped ID  
+ PSID: Page-Scoped ID  
    + 使用者與某個 Bot 互動後，該 Bot 所獲得代表該名使用者的 ID  
    + 只有在該 Bot 有效  
+ ASID 可以重新在 Facebook 上找到使用者，但 PSID 不行  
    + 透過 Facebook Graph API 用 ASID 去找到該名使用者  
+ Messenger Bot Platform 2.0 推出的 ID Matching  
    + 讓開發者可以透過 PSID 找到該名使用者的 ASID  
    + 讓開發者可以拿到使用者的資料回去 Messenger Bot，強化 CRM (Customer Relationship Management)  
    + 對企業很重要，因為可以拿來做廣告 XDDD  
        + 可以餵 ASID 和 PSID 來投放廣告  
+ ID Matching 是完全開放的 API 但有些嚴苛的限制  
    + 必須要 App 和 Bot 都歸在同個 Business Manager 底下才能作用  
    + Secret Proof 必須要用到 App Access Token，而 Secret Proof 是必須要帶在 ID Matching request 的 Payload 裡面的。  
    + 一定兩個都要是 owner 嗎？還是說只要是有被分享就可以？  
    + 一個 BM 目前可以建 10 個 System User 和一個 System Admin User  
    + System User 可以不用是一個真的人，有點像是資源歸類的角色。  
    + 強烈建議把 Bot 和 Page 的管理都放在 BM 底下，而不是某個 User。  
  
---  
  
## 快速上手 Messenger API 輕鬆打造自己的智能客服  
  
+ Speaker: Ian Lin (Chatisfy CTO)  
  
  
### Messenger API 能做什麼？  
  
+ 比較具有代表性的 Chat Bot  
    + eBay ShopBot  
        + 可以透過文字輸入和圖片上傳找到商品  
    + Madison Reed  
        + 用問題引導的方式，理解客戶的需求並推薦適合的染髮劑，點選商品就會引到進入官網購買。  
    + 台鐵時刻通  
        + 輸入起迄點就會答覆最近時刻班次、票價和火車動態，也可以直接線上訂票（用 WebView 開啟台鐵訂票網頁）  
    + Her/Him  
        + 隨機找陌生人聊天，還能推薦你聊天話題，在雙方同意情況下可以交換 Facebook  
  
### 要如何開始建立聊天機器人？  
  
1. 建立 Facebook App 和粉絲專頁  
2. 設定 Webhook  
    + 欄位設定  
        + 回呼網址  
        + 驗證權杖  
        + 訂閱欄位  
    + Messaging Referral  
        + m.me  
        + ?ref=xxx  
3. 取得粉絲專頁的 Access Token  
4. 粉絲團訂閱應用程式  
  
### 有什麼方法可以更快速建立聊天機器人嗎？  
  
+ Chatisfy （偷打廣告 XD 雖然有用過是真的還不錯用就是了  
  
  
---  
  
  
## 從 0 到 20000 MAU  
  
Speaker: Howard Chang  
  
+ 「嗨，大家好，我是 Her/Him, Her/Her, Him/Him 開發者，因為太長，所以我都簡稱 H/H 開發者。」  
    + > XDDD  
+ 「剛剛看了一下，已經到 25000 MAU 了。」  
+ 「媒體帶來的是大量的曝光但幾乎都不是有真正交友需求的受眾，都是那些會看科技新聞的人，就像在座的各位。」  
    + > 靠北 XDDD  
+ 「上個禮拜辦了個叫作『拉拉網路獵愛』的線下聚會，會後她們討論交過幾個女朋友的單位是用『打』在算的，聽到都跪在地上了。」  
+ 用什麼工具來計算 Messenger Bot 的使用者流量  
    + Google Analytics  
        + 比較難應用，但還是有埋  
    + Botmize  
        + 針對中文有做些斷句斷詞  
    + Dashbot  
        + 全球最大的 Chat Bot 分析工具  
    + Botmetrics  
