Title: 買了一個叫作 fkz.tw 的域名  
Slug: i-bought-my-first-domain-name  
Date: 2016-09-06 18:25  
Authors: fkz  
Category: Life  
Tags: Domain name, CloudFlare, Gandi, GitHub Pages  
Summary: 約 3 個月前，心血來潮買了一個域名，用到了 [Gandi](https://www.gandi.net/) 和 [CloudFlare 免費版](https://www.cloudflare.com/)的服務，也順便紀錄一下。  
Modified: 2016-09-19 21:52  
  
  
## 前言  
  
今年 6/13 的時候一時心血來潮就買了，  
Domain Name 是 `fkz.tw`。  
從 [Gandi](https://www.gandi.net/) 那邊買的，  
因為之前還蠻常看到 Gandi 出現在 Conf 的攤位擺攤的，  
想說就用用看他們家的服務。  
  
`*.tw` 域名的價錢我覺得不貴，  
一年沒記錯的話好像新臺幣六七百塊而已。  
  
算一算用了也快 3 個月了，  
當時就想寫篇文章稍微紀錄一下，  
但身為一個拖延症患者，  
就一直拖到了現在。  
  
其實買了以後大概也只有 `blog.fkz.tw` 有在用，  
就是為了這個 blog 罷了，  
但想說之後有什麼東西要用的話，  
也可以 DNS record 設定一下就可以放在自己的 domain 底下，  
而且身為一個寫程式跟管 Server 的人，  
買個自己的 Domain Name 來用應該是件很合理的事？  
其實以前就想買了，  
只是窮學生沒什麼收入，  
現在有在工作有點收入後，  
就覺得不是啥太大的負擔了。  
  
因為用到 GitHub Pages, Gandi, CloudFlare 三個服務，  
所以以下稍微紀錄一下。  
  
---  
  
## GitHub 相關  
  
因為這個 blog 是透過 GitHub Pages 架設的 static site，  
要在 master branch 新增一個 `CNAME` 的檔案，  
內容則是這個 GitHub Pages 的 Custom Domain，  
[我的話當然就是放 `blog.fkz.tw`](https://github.com/M157q/fkz.github.io/blob/master/CNAME)，  
  
設定好的話，  
連到原本的 GitHub Pages 預設的 Domain Name，  
就會幫你 redirect 到 Custom Domain 去。  
例如：<https://fkz.github.io> 現在就會直接被導到 <https://blog.fkz.tw>。  
  
詳細的 GitHub 官方說明文件在此： [Using a custom domain with GitHub Pages - User Documentation](https://help.github.com/articles/using-a-custom-domain-with-github-pages/)  
  
---  
  
## Gandi 相關  
  
Gandi 的 web admin interface 我覺得沒有很好用，  
速度有點慢，  
而且帳號是 Gandi 把申請人姓名取兩個英文字母簡寫再加上四個數字的流水號，  
然後後面還要加上 `-GANDI`，  
所以我每次要登入的時候都忘記帳號，  
都要跑去信箱打開信件查閱。  
雖然他們家在社群攤位每次主打的都是 CLI 介面，  
但我沒用過，  
之後有機會可能會用用看。  
  
其實介面就還堪用，  
但有個很重要的功能我覺得需要提一下，  
就是把 Domain Name 申請人資料隱藏的選項。  
發現好多人買完好像都沒勾選這個選項，  
導致個人資訊只要一用 `whois` 就全部洩漏了。  
這個選項的位置在 Admin Interface 裡頭：  
  
`Account management` > `Update account information`  
裏面有一欄 `Private Domain Registration`  
請記得勾選 `Yes`  
然後儲存就行了。  
（其實好像在填寫申請資料的時候就可以勾選了）  
  
印象中要等一下子才會生效。  
之後用 `whois` 查詢自己的 domain name 的話，  
就只會出現本名，  
還有 Gandi assign 的 email，  
似乎會幫忙轉信到你真正的信箱。  
  
---  
  
## CloudFlare 相關  
  
CloudFlare 是因為公司裡頭的服務有用到而接觸，  
使用了以後覺得還滿好用的，  
我覺得後台的介面設計的蠻簡單易用的，  
而且說明也很好找，  
就在每個功能旁邊都有個 Help，  
不懂這個功能在幹嘛的話點下去就對了，  
而且說明我覺得滿詳細的。  
  
預設的免費版就有很多好用的功能，  
主要比較常用到的就是以下幾個功能：  
  
+ DNS  
    + 設定非常方便，我就是直接把 Gandi 的 DNS delegate 給 CloudFlare 這邊做管理。  
    + 透過後台可以馬上做設定，而且生效極快。  
+ CDN + Cache  
    + 非常強大，而且今年已經在臺北有 Node（與中華電信合作），所以存取速度大增。  
    + （2016/09/19 更新）目前因為中華電信的費用實在太貴，所以 CloudFlare 把 Free 跟 Pro User 的台灣流量都導到美西去了，[說是只有 Business User 才能使用台北的 Node](https://twitter.com/ihower/status/777723975300321280)。  
        + <https://blog.cloudflare.com/bandwidth-costs-around-the-world/>  
            + 之前看到這篇的時候沒有仔細看，以為只有單純婊中華電信和其他國家的五家電信很貴。(六家電信在 CloudFlare 總流量只有 6% 卻佔頻寬費用將近 50%)  
            > Today, however, there are six expensive networks (HiNet, Korea Telecom, Optus, Telecom Argentina, Telefonica, Telstra) that are more than an order of magnitude more expensive than other bandwidth providers around the globe and refuse to discuss local peering relationships. To give you a sense, these six networks represent less than 6% of the traffic but nearly 50% of our bandwidth costs.  
            + 沒想到裏面有提及，會把 CloudFlare 免費版使用者有用到這六家電信的流量導到其他費用比較合理的國家，直到這六家電信的費用有變便宜才會再做考慮。  
            > While we’ve tried to engage all these providers to reduce their extremely high costs and ensure that even our Free customers can be served across their networks, we’ve hit an impasse. To that end, unfortunately, we’ve made the decision that the only thing that will change these providers’ pricing is to make it clear how out of step they are with the rest of the world. To demonstrate this, we’ve moved our Free customers off these six transit providers. Free customers will still be accessible across our network and served from another regional cache with more reasonable bandwidth pricing.  
            + 剛剛用 [Claire](https://github.com/cloudflare/claire) 看了一下 blog，的確從原本台北的 node 變成 Los Angeles 的 node 了，所以 ping 的 latency 升到了 180 ms 左右。blog 好像還好，不過公司的 service 影響可能比較大就是了，雖然之前台北沒 node 的時候公司好像還是照用 CloudFlare 就是了。所以應該沒差吧（？  
+ 免費的 HTTPS  
    + 這部份本來使用 GitHub Pages 就有 HTTPS 了。  
    + 在 Crypto 的 SSL 設定要設定成 Full，設定成 Full(strict) 我記得是會有問題的。  
+ Analytics  
    + 簡單的流量分析，主要是讓你檢視 CloudFlare 幫你 Cache 了多少流量，還有其他圓餅圖。  
    + 免費版只能查看最近 24 小時、最近 1 個禮拜和最近 1 個月的資料，但我覺得已經夠用了。  
  
其他還有像是：  
  
+ Auto Minify JavaScript, CSS, HTML  
+ HTTP/2+SPDY  
+ 免費版可以設定 3 條 Page (Rewrite) Rules  
+ 也有 Firewall 可以設定，但因為我是用 static site，沒啥好擔心的，所以目前沒用到。  
+ 自動幫你擋掉一些惡意攻擊  
  
我的設定大致上跟 [CloudFlare 官方 Blog 這篇文章](https://blog.cloudflare.com/secure-and-fast-github-pages-with-cloudflare/)差不多，  
差別只在於文章裡面的 static site generator 是用 Jekyll，  
但我是用 Pelican。  
  
然後查了一下有人說掛上 CloudFlare 以後，  
使用 Disqus 和 Google Analytics 會有問題，  
主要是因為等同掛了 proxy，  
所以 Disqus 的留言者 IP 和 Google Analytics 的 IP 來源判斷會有問題，  
但我觀察了一下是沒有遇到這問題就是。  
  
---  
  
## 結論  
  
我覺得現在這樣還挺方便的，  
搭配之前設定的 [Travis CI 自動化發佈 blog](/posts/2016/05/08/use-travis-ci-to-publish-pelican-blog-on-github-pages-automatically/)，  
真的就不用登入後台，  
所以沒有網路也可以寫。  
（當然像 Hexo 那類 run local server 然後進去 local server 的 admin interface 也不用連網就是）  
但因為用 Markdown 習慣了，  
也不需要啥語法輔助或是所見即所得編輯器，  
然後用 Vim 也用習慣了，  
不太想空出一隻手去操控滑鼠，  
所以現在就可以開心用 Vim 寫 blog，  
還有用 Git 幫自己的 blog 做版本控制。  
  
也不用擔心哪個 blog 服務要關閉，  
就算 GitHub Pages 要關閉了，  
我也可以很容易的自己 serve 一個 static site，  
我覺得挺好的。  
  
---  
  
# References  
  
+ [Using a custom domain with GitHub Pages - User Documentation](https://help.github.com/articles/using-a-custom-domain-with-github-pages/)  
+ [Secure and fast GitHub Pages with CloudFlare](https://blog.cloudflare.com/secure-and-fast-github-pages-with-cloudflare/)  
