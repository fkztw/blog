Title: 為 G Suite 新增 SPF, DKIM 和 DMARC 設定以避免有心人士的釣魚攻擊  
Slug: setup-spf-dkim-dmarc-for-g-suite  
Date: 2018-07-04 02:09:19  
Authors: m157q  
Category: Note  
Tags: G suite, Google, Mail, SPF, DKIM, DMARC, Security  
Summary: 公司最近收到了漏洞回報，結果是因為 DNS 沒有設定 SPF record，導致有心人士可以偽裝成客服的電子郵件信箱寄信給任何人。  
  
  
## TL;DR 懶人包  
  
如果你正在使用 Google 的 G Suite 而且有在使用其 Gmail 功能的話，  
請記得花點時間設定 Gmail 的 SPF, DKIM 和 DMARC，  
以防止有心人士偽裝成你的公司寄電子郵件給別人。  
  
直接按照 G suite 的官方教學一步步進行設定就行了，  
以下直接附上連結：  
  
+ [使用 SPF 對寄件者授權 - G Suite 管理員說明](https://support.google.com/a/answer/33786?hl=zh-Hant)  
+ [產生網域金鑰 - G Suite 管理員說明](https://support.google.com/a/answer/174126?hl=zh-Hant)  
+ [關於 DMARC - G Suite 管理員說明](https://support.google.com/a/answer/2466580?hl=zh-Hant)  
  
設定好之後可以使用 Google 的網站來檢測：  
[Check MX: Check MX and SPF Records.](https://toolbox.googleapps.com/apps/checkmx/)  
或者這個網站也可以  
[SPF Query Tool](https://www.kitterman.com/spf/validate.html)  
但我比較推薦前者就是。  
  
---  
  
##  前言  
  
最近公司的 contact 電子郵件帳號收到了漏洞回報，  
告知 SPF record 沒設定好，  
任何人都可以假冒公司的電子郵件地址寄信給別人進行釣魚攻擊。  
  
和同事都以為都用了 G suite 了，  
Google 應該會幫你自動設定好這些東西，  
但其實沒有。  
  
應該是因為是在 DNS 進行設定，  
而 G suite 其實沒包含 DNS，  
也沒權限動你的 DNS。  
  
所以真的要記得設定啊。  
  
---  
  
## 紀錄  
  
### SPF  
  
設定了一下 SPF，其實不花多少時間，也不需要 G suite 管理員權限的帳號。  
只要有可以改 DNS 的帳號即可，就加上一行 TXT record:  
  
```txt  
host: @  
value: v=spf1 include:_spf.google.com ~all  
ttl: 3600  
```  
  
DigitalOcean 也有一篇關於 SPF 的文章：[How To use an SPF Record to Prevent Spoofing &amp; Improve E-mail Reliability | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-use-an-spf-record-to-prevent-spoofing-improve-e-mail-reliability)  
說明了 SPF (Sender Policy Framework) 的作用、語法和設定方式。  
簡單來說就是讓人家知道收到你的網域的電子郵件時，  
只有其 IP 來自於 SPF 中有寫到的 IP 才是認可的來源這樣。  
其他都會被認定為 Spoofing。  
  
CloudFlare 也有一篇教學教你怎麼設定 SPF：[How do I add a SPF record? – Cloudflare Support](https://support.cloudflare.com/hc/en-us/articles/200168626-How-do-I-add-a-SPF-record-)  
其實就是一筆特殊格式的 DNS TXT 紀錄。  
  
想詳細知道 SPF 語法的人可以參考這個網站：[SPF: SPF Record Syntax](http://www.openspf.org/SPF_Record_Syntax)  
  
可以使用 `dig` 指令來查詢是否設定好了：  
  
```sh  
dig TXT [domain]  
```  
  
如果有出現 `v=spf1` 的 TXT 紀錄就是設定好了。  
  
  
### DKIM  
  
DKIM 則是用來簽署由此網域發出去的電子郵件，  
設定步驟直接參考 G suite 官方教學：[產生網域金鑰 - G Suite 管理員說明](https://support.google.com/a/answer/174126?hl=zh-Hant)  
這個部份要在 G suite 管理介面做些設定，  
所以會需要有 G suite 管理員權限的帳號。  
  
要先在 G suite 產生 DKIM 的金鑰後，  
再把 DKIM 的公鑰設定在 DNS 的 TXT 紀錄中，  
完成後即可開啟驗證，  
供人日後做驗證使用。  
  
DNS TXT record 會長得像這樣：  
  
```txt  
host: google._domainkey  
value: v=DKIM1; k=rsa; p=<encoded public key>  
```  
  
CloudFlare 也有篇文章教你怎麼設定 DKIM:[How do I add DKIM records? – Cloudflare Support](https://support.cloudflare.com/hc/en-us/articles/200168696-How-do-I-add-DKIM-records-)  
  
可以使用 `dig` 指令來查詢是否設定好了：  
  
```sh  
dig TXT google._domainkey.[domain]  
```  
  
  
### DMARC  
  
需先設定好 SPF 和 DKIM，DMARC 才有用。  
簡單來說就是讓網域擁有者可以決定該如何處理從自己的網域寄出但未經驗證的郵件，  
可以設定三種動作：不採取動作、隔離、拒絕，  
並可設定要檢查的比例，預設是 100% 都要檢查。  
然後可以設定要把這些未經過驗證的信件寄信到管理員的電子郵件，  
讓網域管理員瞭解自己的網域有多少未經驗證的電子郵件發出。  
  
關於 DMARC 的介紹和格式可以參考以下網站：  
  
+ [關於 DMARC - G Suite 管理員說明](https://support.google.com/a/answer/2466580?hl=zh-Hant)  
+ [Overview – dmarc.org](https://dmarc.org/overview/)  
+ [DMARC.org: Domain-based Message Authentication, Reporting and Conformance (DMARC)](https://dmarc.org//draft-dmarc-base-00-01.html#iana_dmarc_tags)  
  
設定的步驟一樣按照 G suite 的官方教學即可：  
[新增 DMARC 記錄 - G Suite 管理員說明](https://support.google.com/a/answer/2466563?hl=zh-Hant)  
  
設定好的話大概會長這樣：  
  
```txt  
host: _dmarc.[domain]  
value: v=DMARC1; p=reject; rua=mailto:admin@[domain]  
```  
  
`p` 可以是 `none`, `quarantine`, `reject`  
`none` 是不採取任何動作，仍會進到收件人的信箱。  
`quarantine` 是隔離，未經驗證的信件會被標為垃圾信，仍會進到收件人的信箱。  
`reject` 是拒絕，會直接擋掉，不會進到收件人的信箱。  
  
如果要設定檢查的比例的話，  
可以再加上 `pct` 這個參數，  
`pct=5` 代表只檢查 5%，  
不做設定的話，  
預設是 `pct=100`。  
  
可以使用 `dig` 指令來查詢是否設定好了：  
  
```sh  
dig TXT _dmarc.[domain]  
```  
  
---  
  
## 後記  
  
突然想起遙遠的 Network Administration 課程好像有講過這件事，  
不過那時的作業是教你怎麼寄信到人家的 Gmail 信箱裏面啊，  
有講這幾個 protocol 可以用來防禦，  
但真的是到今天才想起來啊。  
  
不過印象中當時只有聽過 SPF 和 DKIM，  
DMARC 應該是後來才出現的。  
  
總之是又學了一課啊。  
