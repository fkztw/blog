Title: A Free Certificate Authority to Encrypt the Entire Web  
Slug: a-free-certificate-authority-to-encrypt-the-entire-web  
Date: 2015-11-27 22:05:53  
Authors: fkz  
Category: Conf/Meetup  
Tags: Let's Encrypt, EFF, Speech  
Summary: 資訊與人權的交會: Seth Schoen 訪台系列活動之 11/27 專家講座  
Modified: 2015-11-29 09:33  
  
  
KKTIX URL: [專家講座：資訊與人權的交會](http://ocftw.kktix.cc/events/imhp)  
  
---  
  
# Let's Encrypt: A Free Certificate Authority to Encrypt the Entire Web  
  
+ Seth Schoen - Senior staff at Electronic Frontier Foundation  
  
  
## Acronyms  
  
SSL, TLS, HTTPS, X.509, PKI, CA  
  
+ SSL (Secure Sockets Layer)  
    + The old name for the main security layer for TCP  
+ TLS (Transport Layer Security)  
    + The modern name of SSL  
  
  
## Importance of TLS  
  
+ Still occasionally dealing with the idea that it's only needed for finalncial data.  
+ ... more often these days, the idea that it's only needed for logins.  
+ We need to articulate a stronger vision that networks are untrustworthy and commmunications need to be protected.  
+ Networks are routinely attacking us and plain HTTP offers no defense.  
  
We need security for everything on the Internet?  
  
  
## Just a few examples  
  
+ Sidejacking and location tracking  
+ Integrity of software downloads  
+ Reader privacy (although size of documents is still an enormous problem)  
    + ex: Medical info site with searchiin function but no HTTPS connection.  
+ Content-based censorship prevention  
    + Ad, Cookies  
+ Protection against ad injection, tracking-header-injection and even malware injection at ISP  
  
  
## Barriers to adoption  
  
+ Perception that TLS is slow (especially for session establishment) or is very computationally intensive  
+ Difficulty integrating into some server and data center designs (like load balancing)  
+ Cost and effort of obtaining and managing PKI certificates  
+ Even a skilled person who understands PKI conceptually may take ~1 hour to get and deploy a cert... and then it may expire, or omit some vhosts.  
    + People say it's waste of my time and not worth it.  
  
  
## Let's Encrypt  
  
+ Initially, a collaboration among EFF, University of Michigan, and Mozilla  
    + to create a fully automated CA to issus certificates to any site for any purpose, quickly and at no charge  
+ Aiming to be cheaper, easier, and more secure than existing CAs  
+ Thanks to partners including Akamai, Cisco, and IdenTrust, we have publicly  
  
  
## Cross-signing  
  
+ Root CAs can and do delegate their authority to intermediate CAs - currently hundreds of named entities  
+ Browsers then automatically trust these intermediates; end-entity certs are almost always signed by intermediates, not roots  
+ Our CA is now cross-signed by IdenTrust; *mainstream browsers trust us today*;  
  
  
## Let's Encrypt concept  
  
+ Clien (User's Web Server), Sever (Let's Encrypt CA)  
+ Lowest level of validation for PKIX certificates is DV (Domain Validation) - verification by the CA that the applicant controls the domain name (or a server that the domain name is pointed at)  
+ Explicitly doesn't confirm the real-world identity of the applicant  
+ Software on web server, and the server connect to the Let's Encrypt CA.  
+ ACME (Automated Certificate Management Environment) to handle conversations about cert issuance  
+ Client claims to control a particular name or names, and asks for a cert for them  
+ Server issues one or more challenges to ask the client to prove its control (and/or possibly prove control of other cryptographic keys)  
+ Client satisfies these challenges and server verifies this automatically then issues cert and sends it over  
  
Normal users: Certificates just make browsers complain the wrong domain name or expired to users while browsing the Internet. (LOL)  
  
  
## ACME  
  
+ A JSON-based protocol  
  
  
## Let's Encrypt status  
  
+ Internet Security Resarch Group (ISRG)  
    + We don't want people to know about what we are doing, so we think this name is good.  
  
  
## DVFNI  
  
+ Crypto  
  
  
## Convenience  
  
We anticipate people who administer their own web servers will run something like  
  
```  
$ sudo apt-get install letsencrypt  
$ sudo letsencrypt  
```  
  
and the client will not only obtain, but also deploy, the new cert in less than a minute.  
  
We're working on a client that will parse and write Apache and Nginx configs, and autorenew expiring certs.  
  
Apache sever's config file is really hard to parse, so we made a lot of effort on it.  
  
  
## Safety  
  
+ We care a lot about avoiding misissuance and plan to adopt technologies to stop it  
+ We are publishing all certs in Google's Certificate Transparency system  
+ We're planning to prevent issuance for a domain that already has a valid cert unless the applicant can prove control of its subject key  
+ We can also have mechanisms for domains to ask us never to issue for them  
  
We can have records about all certificates we've issued, and people can also check the list. If we got hacked, we can easily see the compromised records.  
  
  
## Wider integration  
  
+ We'd like to be integrated on every server OS or web server and every hosting and application platform  
+ The ACME protocol is in a standardization process at IETF and will be an open standard  
+ You can use the protocol to request certs from us without using our client software.  
    + You can even write you own client.  
+ Contractual relationship isn't required, though we welcome new sponsors.  
  
  
## Help!  
  
+ Please join the beta test program  
    + Fill out a form with your domin names + e-mail address, then wait for e-mail confirmation  
+ Try out our service and report client or service bugs, and optionally send us pathces.  
+ Beta certs are fully "real" and mainstream browsers accept them now  
+ Integrating our client in your favorite OS or with your favorite web server  
    + Or other server (ESMTP, IMAP, XMPP, ...)  
+ Packaging our client  
+ Integrating our client with your favorite hosting environment  
+ Auditing our client or server  
+ Writing more tests  
+ Documenting our client (man pages, FAQ, introduction, explaining PKI, what key/cert/chain are)  
  
Client written in Python, Server written in Go.  
  
---  
  
# Real-world cryptography: What could possibly go wrong?  
  
+ 鄭振牟 （台大電機系副教授）  
  
## EasyCard 2.0  
  
## CDC (自然人憑證) - Citizen Digital Certificate  
  
政府：「新的自然人憑證應該安全了」 「你信嗎？」 「反正我是信了。」  
  
---  
  
## Thought  
  
後半段鄭教授講有關悠遊卡跟自然人憑證的部份我沒有聽的很仔細，  
大致上是在講之前悠遊卡出包後，教授的研究團隊有投入補救，然後推出悠遊卡 2.0。  
然後自然人憑證的部份有講到超大質數在以 Hexadecimal 顯示時會有過度規律的問題等等。  
然後提供了許多論文，給想瞭解的人去參考。  
我也沒有記下來，畢竟這次來主要是想瞭解 EFF 的資訊。  
  
簡單來說 Let's Encrypt 在做的事情就是讓取得憑證這件事情變得愈簡單愈好，  
方便架站者可以很快、很方便的取得並儘量自動化設定憑證，之後便能直接使用，  
讓架站者可以迅速地提供使用者 HTTPS 加密連線，不要使用 plaintext 的 HTTP。  
以往因為憑證的設定需要一連串繁瑣的步驟及有些複雜的指令，讓許多架站者覺得時間成本過高，  
而且大多數的憑證是需要購買的，Let's Encrypt 則提供免費的憑證，且只需透過簡單的指令就可以迅速設定完成。  
總之就是希望使用者在網路上的連線資料都是加密的，而不是使用 HTTP 在網路上裸奔，容易讓有心人士取得資料。  
  
Let's Encrypt 的官方網站： [Let's Encrypt](https://letsencrypt.org/)  
有興趣的人可以點進去瞧瞧，目前只有英文，也歡迎有興趣的人貢獻繁體中文的翻譯。  
如果你覺得他們致力於網路安全的努力值得支持的話，也可以到官方網站的 donate 連結，小額贊助一些錢給他們。  
  
從 2015/9/12 到目前都是 limited beta 測試中，採填表申請並等待的制度。  
但從下禮拜 (12/3 Thu) 開始，進入 public beta 測試階段，  
屆時系統會開放給任何想申請的人，無需等待回信。  
詳細公告在此 [Public Beta: December 3, 2015](https://letsencrypt.org/2015/11/12/public-beta-timing.html)  
有興趣的人歡迎到時候申請來使用看看，遇到任何問題或 bug 都歡迎回報給他們。  
  
順便附上他們的 Twitter： [EFF (@EFF) | Twitter](https://twitter.com/EFF)  
可以比較快的知道一些新資訊  
  
最後覆蓋海報一張結束這篇文章  
  
![Poster](/files/a-free-certificate-authority-to-encrypt-the-entire-web/poster.jpg)  
