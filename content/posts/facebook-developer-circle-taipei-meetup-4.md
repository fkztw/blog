Title: Facebook Developer Circle: Taipei - Meetup #4  
Slug: facebook-developer-circle-taipei-meetup-4  
Date: 2017-09-27 21:50:52  
Authors: fkz  
Category: Conf/Meetup  
Tags: Facebook  
Summary: Note for Facebook Developer Circle: Taipei - Meetup #4  
  
  
Event link: <https://fdctaipei.kktix.cc/events/fdc201709>  
  
---  
  
## 用 OLAMI 打造各種形式的中文聊天機器人  
講者：Ryan Hang (威盛電子 OLAMI Team)  
  
+ OLAMI 中文自然語言處理平台 （威盛電子開發）  
    + <https://olami.ai>  
    + 歷程  
        + 5 年前開始做，從 rule-based 開始，還沒用 Machine Learning。  
        + 到現在都還是很推薦用 rule-based，為什麼？  
            + Machine Learning 的開發速度較緩慢，更新的速度可能更不上產品的需求，rule-based 就比較容易做到。  
+ OLAMI AI 對話系統資訊流概觀  
    + 輸入 => NLI 自然語言互動系統 (+ 客製化語意理解) =>  
+ IoT 語音互動  
    + OLAMI Voice Kit  
+ Live Demo  
    + 速度還滿快的，感覺可以試試看，API 接一接應該不難。  
  
---  
  
## 商務 Chatbot 體驗設計要訣  
講者：Calvin Lin (Yoctol)  
  
+ Business Chatbot 簡介  
    + 目的為實際商業應用，非純娛樂性質  
    + 主要功能包含  
        + 智慧客服：自動回覆常見問題，減少客服人員負擔。  
        + 訊息推播：文章訂閱、優惠訊息、活動通知  
        + 資訊查詢：查詢最新優惠、查股價、物流到貨查詢  
        + 商業互動：下單付款、預約登記、風險屬性評測  
+ Chatbot 體驗的關鍵問題  
    + 預設用途  
        + 可以輸入任意文字並得到適當的回應  
        + 期待過高 => 體驗不如預期 => 失望  
        + Business Chatbot 的限制  
            + 不能呼攏使用者  
            + 回覆內容要可控制  
                + 完全生成式的流程在商業應用上是有疑慮的，因為不知道會回出什麼樣的內容。  
    + 指意  
        + 文字輸入框太過於自由，會讓使用者不知道要輸入什麼。得不到使用者期望的回答就會造成使用者的失望進而不想繼續使用。  
        + 為 Chatbot 添加指意  
            + 選單式引導(Generic Template, Button Template, Image map (LINE))  
            + 適時的文字提示（例句提示、Quick Reply）  
+ NLP 對體驗的影響  
    + 影響能力範圍  
        + 極致的 NLP：  
            + 可以輸入任意文字並得到適當的回覆 => 滿足預設用途  
            + 使用者體驗會超極好，但實務上基本上做不太到，開發成本過高。  
        + 完全沒有 NLP  
            + 封鎖輸入框 => 能力大幅受限  
    + NLP 的實作方式  
        + 完全字串比對、關鍵字  
        + 正規表達式  
        + RNN （遞迴式類神經網路）  
            + 輸入一些同樣意思的例句，讓 AI 去歸納和推論這些都是相同的意思。  
            + 實作比較複雜，訓練難度也比較高，會花比較多時間。  
            + 需要一點時間計算，所以在實務上回應使用者的時間會有點太長。  
        + 視情況而定  
            + 比較明確的狀況使用字串比對或正規表達式，速度會比較快，使用者體驗會比較好。  
            + 比較複雜的狀況就採用 RNN  
+ 體驗設計要訣  
    1. 不同的使用者族群  
        + 既有客戶  
            + 有明確的問題想問 => 確保重要的問題能被回應  
        + 新客戶、潛在客戶  
            + 認真想瞭解，但沒有明確的問題 => 引導客戶探索主要功能  
        + 湊熱鬧的路人  
            + 只是剛好路過看到一個 bot，隨便玩一玩覺得你什麼都答不出來，然後說一句「好笨」就走了。XD  
            + 隨便玩 => 明確提示使用範圍，縮小期望落差。  
    2. 開場引導  
        + 用了 Generic Template 或 Button Template 的時候，可以再加些文字引導使用者，讓使用者覺得不是只有可以點按鈕而已  
    3. 迷途引導  
        + 用提醒引導使用者回去使用正常的功能  
    4. 請求更多資訊  
        + 向使用者確認其目的  
    5. 不要停止引導  
        + 只要出現斷點，使用者就容易：  
            + 不知所措得離開  
            + 亂問不在範圍內的問題  
        + 引導方式  
            + 接續目前的互動  
            + 推薦相關的選項  
            + 探索其他功能  
+ 使用情境 Demo  
  
---  
  
## 如何用 Messenger Bot 提升 EC/O2O 成交轉換率  
講者：Lucas (AsiaYo Product Lead)  
  
+ 緣由  
    + 一年前團隊就在討論要不要用 Chatbot 取代真人客服  
    + 結論是被否決的，因為能解決的問題像是使用者的行李和 check-in 的問題很難用 chatbot 解決，並不會減少真人客服的負擔  
    + LINE 的 chatbot => 3 steps before interaction  
+ 那為什麼後來做了 Facebook Messenger Bot  
    + Facebook Messenger bot => 1 steps before interaction  
    + 直接接觸到使用者的成本低了很多  
        + OTA's users have longer decision funnel  
            + 會和朋友討論、可能還會在期間去其他民宿網比價、轉換流失率很高  
            + 對應機制  
                + Agoda: 不斷寄 email => 需要拿到使用者的個人資料（email 或電話）  
                + 透過 retargeting ad 讓使用者不管到哪裡都會看到 => 花費高  
    + 需要的 Designer 少很多  
+ Key Metrics  
    + 同意授權 > 第一次互動 > 轉換  
+ System Architecture  
    + Facebook checkbot plugin => Chatfuel (JSON API) => AsiaYo API => Chatfuel (JSON API) => Chatfuel Blocks (1st message)  
        + hmm... 沒想到 Chatfuel JSON API 可以拿來這樣做，這樣應該連自己的 webhook server 都不用架了？跟 Facebook server 溝通那邊就由 Chatfuel 幫忙處理掉，跟 Facebook 那邊溝通的確會是花最多時間的地方，畢竟 Facebook 沒有官方的 Messenger Bot Framework，第三方的也不盡理想。  
+ 第一次互動  
    + 要具有趣味性與互動性  
        + 對話設計成像遊戲  
        + 隨機彩蛋 + 優惠碼  
    + 實用性 & Cross Promotion  
+ Takeaways  
    + Context matters  
    + Createing Aha moments  
        + 讓使用者有眼睛一亮的感覺  
+ Future Works  
    + Cart abandoned  
    + Check order status  
