Title: 用 Python 寫個程式抓出我在 Twitter 上存了哪些 tweet  
Slug: write-a-python-script-to-retrieve-twitter-direct-messsages  
Date: 2017-12-22 23:57:08  
Authors: fkz  
Category: Note  
Tags: Python, Twitter, 2018 iT 邦幫忙鐵人賽  
Summary: 用 Python 簡單寫個小程式，抓出我存在 Twitter 私訊裡的 tweet。  
Modified: 2017-12-24 22:58:08  
  
  
## 前言  
  
身為一個邊緣人，  
沒有 Instagram 帳號，  
卻有台灣沒什麼人用的 Twitter 帳號也是很合理的。  
  
其實 Twitter 上很容易得到國外第一手即時資訊，  
常常看到好幾天之後才在 Facebook 或台灣的媒體看到消息，  
很適合我這種資訊焦慮症的人（？  
  
Twitter 也很容易跟一些很有名的人直接交流，  
像上一篇翻譯文章的授權，  
我就是直接在 Twitter 上問作者，  
大概五分鐘之內，沒錯，就是短短幾分鐘之內，就收到作者同意的回覆。  
  
總之，  
我平常在用 Twitter 的時候有個習慣，  
就是把我看到覺得值得保留下來的 tweet 分成兩類，  
一類是比較不嚴肅的，把該 tweet 私訊給自己。  
另一類是比較嚴肅的，把該 tweet 私訊給另外一個 RSS bot 帳號。  
（這個 RSS bot 有機會的話會發篇文章講一下）  
  
這裡要來用 Python 寫個程式，  
把今年存下來的這兩大類 tweet 抓出來，  
其實我不確定是不是一定會成功，  
大概只有 87% 的把握，  
總之接下來就一步步講一下要怎麼做。  
  
（謎之音：最愛寫這種無用的小程式了。）  
  
---  
  
## 步驟  
  
### 看有哪個 API 可以拿來用  
  
+ [GET direct_messages/events/list — Twitter Developers](https://developer.twitter.com/en/docs/direct-messages/sending-and-receiving/api-reference/list-events)  
    + 最多只能抓取最近的 200 則私訊（不限 30 天內。）  
    + 如果超過 200 則的話，只能抓取最近 30 天內的私訊。  
  
  
### 取得 Access Token  
  
+ 到 <https://apps.twitter.com/> 建立一個新的 App。  
+ 記下 Consumer Key (API Key) 和 Consumer Secret (API Secret)  
+ 點選 Permissions  
    + 選取 Read, Write and Access direct messages。（原本只有 Read, Write）  
    + 選好之後按底下的 Update Settings  
+ 點進去剛建立的 App，移到底下，點選建立 Access Token。  
+ 記下 Access Token 和 Access Token Secret  
  
  
### 安裝要使用的 Python 套件  
  
+ <https://github.com/bear/python-twitter>  
+ `pip install python-twitter`  
  
  
### 撰寫程式  
  
因為兩個的作法類似，  
這邊就以抓出比較嚴肅一點的 tweet 作為範例，  
幾行就可以寫完了。  
  
```python  
#!/usr/bin/env python3  
  
import urllib  
  
import twitter  
  
  
# Fill these contants by yourself.  
CONSUMER_KEY = ""  
CONSUMER_SECRET = ""  
ACCESS_TOKEN_KEY = ""  
ACCESS_TOKEN_SECRET = ""  
MY_TWITTER_ID = 0  
MY_BOT_TWITTER_ID = 0  
  
  
api = twitter.Api(  
    consumer_key=CONSUMER_KEY,  
    consumer_secret=CONSUMER_SECRET,  
    access_token_key=ACCESS_TOKEN_KEY,  
    access_token_secret=ACCESS_TOKEN_SECRET,  
)  
  
# Twitter API limitation:  
# "Last 30 days DMs" or "Up to 200 DMs which created before 30 days"  
sent_direct_messages = api.GetSentDirectMessages(count=200)  
for dm in sent_direct_messages:  
    if dm.recipient_id == MY_BOT_TWITTER_ID:  
        try:  
            # Got t.co url in DM, use urllib to get its real Twitter Status URL.  
            with urllib.request.urlopen(dm.text) as response:  
                real_url = response.geturl()  
        except Exception:  
            raise  
        else:  
            print("+ <{}>".format(real_url))  
```  
  
開一個 gist 放個程式碼：<https://gist.github.com/M157q/a90f5d2948442dc482e35d671b074c6f>  
  
---  
  
## 結果  
  
直接以網址呈現：  
（其實應該可以直接 embed tweet 啦，但我有點懶得弄。）  
  
+ <https://twitter.com/yoyo0329/status/944230050399793152>  
+ <https://twitter.com/rewoIf/status/943852230796484610>  
+ <https://twitter.com/zaticwu/status/943834445886267392>  
+ <https://twitter.com/zhusee2/status/943728354057887744>  
+ <https://twitter.com/TinyDenny/status/943332441699299328>  
+ <https://twitter.com/CHl1XIB8ymdrKbC/status/943482302822150144>  
+ <https://twitter.com/jserv/status/942265803868487680>  
+ <https://twitter.com/rochacbruno/status/942419952300167169>  
+ <https://twitter.com/daiwanhanji/status/942046653619478535>  
+ <https://twitter.com/thecat/status/942193282968305664>  
+ <https://twitter.com/riddle_ling/status/942271085495459840>  
+ <https://twitter.com/c9s/status/942224140273987584>  
+ <https://twitter.com/sandokaishy/status/942057552577052672>  
+ <https://twitter.com/johnroyer/status/941478195362119682>  
+ <https://twitter.com/ferrari_tw/status/941137503423119360>  
+ <https://twitter.com/lovecankill/status/940781592947048448>  
+ <https://twitter.com/linuxtoy/status/940780140081975298>  
+ <https://twitter.com/Ignissfate/status/940453739718066177>  
+ <https://twitter.com/schrockn/status/940037656494317568>  
+ <https://twitter.com/M157q/status/939785465992953857>  
+ <https://twitter.com/welkineins/status/939541907612377089>  
+ <https://twitter.com/WanCW/status/938624903724404736>  
+ <https://twitter.com/jaceju/status/937497004690751488>  
+ <https://twitter.com/ronnywang/status/937511877092847616>  
+ <https://twitter.com/hynek/status/937316249431928832>  
+ <https://twitter.com/Schnappiggg/status/936591006169890816>  
+ <https://twitter.com/tebeka/status/934013246226526210>  
+ <https://twitter.com/riddle_ling/status/932499976193585152>  
+ <https://twitter.com/PeterZaitsev/status/931485736855134213>  
+ <https://twitter.com/TinyDenny/status/932093891368460288>  
+ <https://twitter.com/ruanyf/status/931709967966412800>  
+ <https://twitter.com/dlackty/status/931328546664050689>  
+ <https://twitter.com/joelgrus/status/931202032978948096>  
+ <https://twitter.com/x0rz/status/930016909231362048>  
+ <https://twitter.com/TinyDenny/status/929187796752855040>  
+ <https://twitter.com/dbader_org/status/927899530942668801>  
+ <https://twitter.com/M157q_News_RSS/status/925543091339010048>  
+ <https://twitter.com/WanCW/status/924993679156056064>  
+ <https://twitter.com/jaceju/status/924455583587037184>  
+ <https://twitter.com/LoveHyperApp/status/923523498743439360>  
+ <https://twitter.com/suitingtseng/status/923917098233073664>  
  
---  
  
## 題外話  
  
在寫這篇的時候發現，  
最近 Twitter 好像針對這需求有了一個[新的 Bookmark 功能](https://techcrunch.com/2017/11/23/twitter-is-testing-bookmarks-a-feature-to-privately-flag-tweets-for-later/)，  
看了一下，好像還不能分類就是，  
所以我應該還是會繼續用這樣的方式當作 bookmark。  
  
然後也發現好像多了個 [Account Activity API](https://developer.twitter.com/en/docs/accounts-and-users/subscribe-account-activity/overview)，  
可以設定 webhook 即時接收帳號的事件，  
可能可以做到類似聊天機器人這樣事件觸發式的對話。  
  
如果是這裡的用途的話，  
可以在我每次發送私訊的時候，  
就直接透過 webhook 把該 tweet 的內容存在資料庫裡，  
這樣就不會受 Twitter API 的限制了，  
有空的話再來弄吧。  
