Title: 利用 ngrok 直接在本機開發 chatbot  
Slug: ngrok-https-proxy-to-write-chatbot-in-localhost  
Date: 2017-12-29 23:58:20  
Authors: fkz  
Category: Note  
Tags: ngrok, chatbot, 2018 iT 邦幫忙鐵人賽  
Summary: 利用 ngrok 拿到一個免費的 https proxy，將這個網址綁到 chatbot 的 webhook 網址，便可以很輕鬆得在本機開發 chatbot。  
Modified: 2017-12-31 15:54:20  
  
  
## 前言  
  
去年第 4 季部份時間，加上今年上半年大部份時間，幾乎都在做 chatbot 相關的開發。剛開始的時候真的是感到相關開發的工具是很不齊全（當然經過了一年多的發展，現在有更多更方便開發 chatbot 的工具了。），尤其是臺灣最多人用的 Facebook 和 Line 真的是對開發者挺不友善的。主要都是 API 的限制比較多，但 Line 至少還有個官方的 SDK，Facebook Messenger Bot 則連個官方的 SDK 都沒有，基本上都是第三方的，絕大多數都是開發者自己包的。  
  
好像有點離題了，總之，一開始開發 Facebook Messenger Bot 的時候，都是在 Webhook 網址填入 Google App Engine service 給的預設網址，每次有改動就要 deploy 上去 GAE，等新版本的 service 正常運作之後，還要再等 Facebook 一段時間才會真的切換到新版本，時間不太一定。一開始還可以接受，但後來就覺得這樣實在是太麻煩了，所以就開始尋找有沒有比較方便的解法。  
  
一開始是往「有沒有辦法在本機架一個模擬 Messenger Bot 介面的網頁前端出來」去找，還真的有人寫：<https://github.com/spchuang/fb-local-chat-bot>，但因為是獨立開發，而且 Messenger Bot 的介面或 API 其實很常改動，所以我後來沒有採用這個方法。  
  
後來詢問了一些人後，才往 web proxy 的方向找，有人推薦我使用免費的 [ngrok](https://ngrok.com/)：可以拿到一個支援 https 的 web proxy，在 Facebook Messenger Bot 使用的 Webhook 網址填入 ngrok 的 https 網址，之後 Facebook 送到該網址的 request 都會由 ngrok 轉送到本機的某一個 port 上，只要你有在 localhost 把 Messenger Bot 的 Webhook server 執行起來的話，就可以很方便得用自己的手機開啟 chatbot 來邊操作邊即時修改程式碼。  
  
作法其實滿簡單的，用了以後開發速度真的加快不少，也可以很即時跟跟 PM 那邊去做確認，確認沒問題了以後再 deploy。而且無論任何語言寫的 chatbot 都可以使用這方法，以下做個介紹。  
  
---  
  
## 介紹  
  
官方網站：<https://ngrok.com/> 有安裝方式，安裝好後也只要一行指令就可以使用了，我自己是這樣用：  
  
`ngrok http 8080`  
  
這樣就會拿到一個接到 local host 8080 port 的 HTTP/HTTPS proxy，至於要用哪個 port 可以自己選擇，不一定要用 8080。  
  
執行後，Termianl 就會拿到像下面這樣的畫面：  
  
![ngrok cli](/files/ngrok-https-proxy-to-write-chatbot-in-localhost/ngrok-cli.jpg)  
  
也會在 local 開一個 web interface，連入以後的畫面像是這樣：  
  
![ngrok web admin 1](/files/ngrok-https-proxy-to-write-chatbot-in-localhost/ngrok-web-admin-1.jpg)  
![ngrok web admin 2](/files/ngrok-https-proxy-to-write-chatbot-in-localhost/ngrok-web-admin-2.jpg)  
  
接下來只要把拿到的 https proxy 的 url 填入 chatbot 的 webhook url，然後在 local 把自己開發的 chatbot webhook server 開在接入的 port 就行了。  
  
如果是 Google App Engine 的 dev_appserver.py 的話，預設就會開在 8080 port。  
  
---  
  
## 參考來源  
  
+ [ngrok - secure introspectable tunnels to localhost](https://ngrok.com/)  
+ [GitHub - inconshreveable/ngrok: Introspected tunnels to localhost](https://github.com/inconshreveable/ngrok)  
