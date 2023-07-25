Title: iThome #Chatbot Day  
Slug: ithome-chatbot-day  
Date: 2017-04-27 21:06:00  
Authors: fkz  
Category: Conf/Meetup  
Tags: ChatBot  
Summary: Note for iThome #Chatbot Day  
  
  
+ Event url: <http://chatbot.ithome.com.tw/>  
+ Collaborative note: <https://hackpad.com/20170427-CHATBOT-DAY-NOTE-zblg5e45w3g>  
  
---  
  
## 突破 Facebook Messenger Platform API 限制  
  
+ Speaker: Howard Chang  
    + Her/Him 開發者  
  
#### Facebook Messenger Platform API 在 Her/Him 上的應用實例  
  
+ Webview  
    + 讓 Messenger 的 UI 可以比較多樣與客製化  
    + Facebook Login Webhook  
    + 讓使用者自己填寫資料  
+ Template  
    + Generic Template  
        + 給使用者一些預設的聊天話題選項  
    + Button Template  
        + 玩猜拳  
+ 特殊的 Emoji 會觸發特效  
    + 目前已知：愛心、氣球、雪花  
+ 取得使用者的 FB ID 後，轉換成 Profile URL  
    + 正常來說應該做不到這件事  
  
#### Messenger Platform 的限制  
  
+ 24 小時內回覆的時間限制  
    + 超過 24 小時，只能再多發送一則訊息  
    + 有時候使用者一忙，可能超過 24 小時才回覆對方的訊息，如果不能突破這個限制，就無法讓使用者在超過 24 小時的回覆傳送到對方那邊  
+ 無法取得使用者的 FB permanent ID  
    + 不能取得的話，雙方就無法交換 Facebook 的網址  
+ 無法傳送貼圖  
    + 透過 Messenger Platform 傳送的貼圖會變成靜態的圖片  
+ 使用者刪除對話後，就無法傳送任何訊息給他。  
  
#### 如何突破限制  
  
+ 取得 Facebook permanent ID 的方法  
    + [Schmavery/facebook-chat-api](https://github.com/Schmavery/facebook-chat-api)  
        + npm module  
        + 透過模擬 Facebook 網頁運作，直接存取 private API  
        + 可以突破限制，在任何時間傳送任何訊息給任何人  
    + 可以拿到使用者的 Facebook permanent ID  
+ 突破 24 小時內回覆的限制與使用者刪除訊息後仍然可以傳送訊息  
    + 用 facebook-chat-api 傳送訊息給使用者  
+ 如何傳送貼圖  
    + 用 facebook-chat-api 傳送 `sticker_id` 給使用者  
  
今天覺得收穫最多的一場 talk，  
主要是因為最近公司專案的關係都在寫 Facebook Messenger Bot，  
然後這些的確都是在開發上會遇到的棘手問題。  
  
---  
  
## Chatbot 智能溝通策略流程規劃與實作  
  
+ AI  
    + luis.ai, IBM Waston 支援繁體中文  
    + > 據說 api.ai 也有支援繁體中文了，只是效果沒有那麼好。  
+ e-Commerce chatbot  
    + 手法  
        + Push notification  
            + 傳送貼圖、優惠活動、限時特價  
            + 太常傳送且沒有打到使用者的點的話就很容易被封鎖  
        + 產品使用後詢問、問卷回饋  
        + 使用者習性  
            + 預測使用者下次什麼時候會再購買一樣的日常用品  
        + 生日好禮  
    + 使用者流程  
        + 推薦商品、搜尋商品、熱門商品  
        + 查無商品、可能推薦商品  
        + 建議其他關鍵字  
        + 近期熱門活動、建議行動  
  
---  
  
## 用 Golang 打造 DevOps Bot  
  
+ Speaker: appleboy  
+ Projects  
    + `drone-line`  
        + <https://github.com/appleboy/drone-line>  
    + `drone-facebook`  
        + <https://github.com/appleboy/drone-facebook>  
  
+ CI/CD  
    + Gitlab  
    + Jenkins  
    + Drone  
+ 支援 CLI Flag 參數  
    + 內建支援 CLI Flag  
        + import "flag"  
    + 缺點  
        + 不支援系統環境變數  
+ 支援 API Webhook  
+ 支援 HTTPS for WebHook Tunnel  
    + ngrok  
    + localtunnel  
+ 支援自動更新 HTTPS 憑證  
    + Trafik  
        + Golang  
        + 支援自動更新憑證  
    + CADDY  
        + Golang  
        + 原生支援 HTTPS  
        + 自動更新 Let's Encrypt 憑證  
        + 會幫你自動把 HTTP protocol 轉到 HTTPS  
    + 用一行 Golang 支援 HTTPS  
        + `http.Serve(autocert.NewListener("ecample.com", handler))`  
            + <https://bit.ly/one-line-autotls>  
            + 自動幫你跟 Let's Encrypt 要憑證  
+ 支援監控 Webhook 的功能  
    + 監控服務健康狀態  
        + Memory usage, CPU usage  
    + 自訂監控數據，分析使用者訊息  
    + 統計報表  
        + prometheus 資料格式  
            + <https://prometheus.io>  
        + Grafana  
            + <https://grafana.com>  
+ 支援多種訊息格式  
+ 支援用 CLI 發送訊息  
+ Golang 跨平台  
    + Simple Go Cross Compilation  
        + `gox`  
        + <https://github.com/mitchellh/gox>  
        + Windows 的支援沒問題  
        + 可以加上 flag 指定特定檔案只在某些 plafform 才 build  
    + Support ARM Platform  
+ 支援透過 Docker 發送訊息  
    + 需支援系統環境變數  
        + <https://github.com/urfave/cli>  
            + lightweight  
        + <https://github.com/spf13/cobra>  
    + 自己的 Bug 自己解  
        + 只發送給原 Commit 作者，避免團隊成員收到太多無用的信件。  
+ 支援 Concurrent  
    + `go f("goroutine")`  
+ 用 App 控制家電  
    + Gorush - A push notification server written in golang  
        + <https://github.com/appleboy/gorush>  
+ 最後講講為什麼使用 Golang  
    + 出身名門：Google  
    + 學習曲線：類似 C 語言  
  
---  
  
## 透過 Golang 無痛建置機器學習聊天機器人  
  
+ projects  
    + [PetNeedMe](https://github.com/kkdai/PetNeedMe)  
    + Baby talk bot  
        + LUIS.ai  
        + [LUIS golang package](https://github.com/kkdai/luis)  
            + 沒有 LUIS.ai 沒有 golang SDK 所以自己寫  
            + 目前還在開發中  
    + ASKME animal  
        + TensorFlow  
        + 透過 TensorFlow 告訴你圖片中的動物名稱是什麼  
+ 透過這個 Template 可以在三分鐘內就在 Heroku 上架好一個 Line Bot  
    + <https://github.com/kkdai/LineBotTemplate>  
  
---  
  
## 孫子廣播電台：用 Linkit 7688 一鍵播放社交平台貼文  
  
<https://github.com/aaaddress1/grandsonRadio>  
  
為了不會用智慧型手機卻又想關心自己的奶奶而做的小專案  
  
+ Linkit 7688 + Python (gTTS) + 麵包板 + 一些電子元件 + 喇叭  
    + 大概新台幣一千元內有找  
+ 建立 Facebook Application  
+ 透過 Graph API 拿到貼文資訊：內容、發文時間、...等等  
    + 透過 Facebook 除錯工具來延長 otke  
  
雖然這好像比較算是 IoT 應用而不是 Chatbot，  
不過真的挺有趣的，  
尤其是最近 [gTTS (Google Text-to-Speech)](https://github.com/pndurette/gTTS) 因為狂新聞還有一堆實況主的 donate 音效很紅。（雖然我個人其實不太喜歡一直聽到 Google 小姐的聲音就是）  
透過判別中英文來切開斷句，  
因為 gTTS 產生的 mp3 每次只能限定某種語言。  
