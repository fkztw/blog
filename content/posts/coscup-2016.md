Title: COSCUP 2016  
Slug: coscup-2016  
Date: 2016-08-25 10:15:00  
Authors: fkz  
Category: Conf/Meetup  
Tags: COSCUP  
Summary: COSCUP 2016 筆記  
  
  
# INFO  
  
+ Official website: <http://coscup.org/2016>  
+ Note: <http://beta.hackfoldr.org/coscup2016>  
  
---  
  
# Day 1: 2016/08/20 Sat  
  
早上其實沒聽什麼議程，  
先隨便逛了一下攤位，  
在VLC 的攤位待了一下子，  
之前好像沒看過 VLC 來 COSCUP，  
跟兩個法國人聊天，  
還吃了法國來的糖果，  
拿了一張 VLC 的貼紙，  
對於沒有實體交通錐覺得有點小遺憾（？）  
![vlc](/files/coscup-2016/vlc.jpg)  
  
然後隔壁的 MOPCON 攤位很應 Pokemon GO 的景，  
讓大家有神奇寶貝可以收服 XD  
![mopcon-pokemon](/files/coscup-2016/mopcon-pokemon.jpg)  
  
後來一直待在天瓏攤位翻書，  
畢竟平常沒有跑天瓏實體書店的習慣，  
而且 Conf 擺攤的折扣又比會員卡還便宜，  
加上今年開始工作以後，  
買書終於可以不用像以前因為價錢而猶豫不決，  
所以今年 PyCon, HITCON 的時候都有到天瓏攤位買書，  
一次大概買三到四本左右，  
[結果這次又買就被老闆記住了 XD](https://twitter.com/M157q/status/766861133231759361)  
反正想說在 Conf 買比較便宜，  
而且最近每年大概也只固定跑 PyCon, HITCON, COSCUP 這三場 Conf，  
先買些書囤起來，  
之後再看應該不為過吧？  
只是每天花在閱讀實體書的時間要再增加了，（畢竟今年的目標可是多閱讀實體書啊）  
最近比較沒有撥時間出來閱讀。（一定都是 Pokemon GO 的錯）  
![tenlong](/files/coscup-2016/tenlong.jpg)  
  
---  
  
## 13:15~16:00 Docker 進階工作坊  
  
+ Slides: <https://docs.google.com/presentation/d/1yABG8gVJlzWMQnEAOJnMpFRoEXeDACnCHFR7HmFDWaA/pub?start=false&loop=false&delayms=3000&slide=id.p>  
+ Hands-on Lab: <https://github.com/philipz/docker_workshop>  
    1. [Docker 官方 Web 投票微服務範例](https://www.katacoda.com/docker/courses/docker2016/1)  
    2. [Docker Compose & CircleCI](https://www.katacoda.com/philipz/scenarios/7)  
    3. [Node.js 最精簡映像檔建置](https://www.katacoda.com/philipz/scenarios/2)  
        + [Dockerfile ONBUILD](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/#/onbuild)  
            + An ONBUILD command executes after the current Dockerfile build completes. ONBUILD executes in any child image derived FROM the current image. Think of the ONBUILD command as an instruction the parent Dockerfile gives to the child Dockerfile.  
    4. [Docker Compose 和 Service Discovery](http://www.katacoda.com/docker/courses/docker2016/2)  
        + 會眾反應：Docker Network 在 Docker 1.9 的時候，40G 的網路可以用到 30G，但到 Docker 1.12 的時候，只能用到 3G 多。  
    5. [Docker Compose for MySQL Cluster & WordPress](http://www.katacoda.com/docker/courses/docker2016/4)  
        + [Galera Cluster](http://galeracluster.com/products/)  
            + Galera Cluster for MySQL is  a true Multimaster Cluster based on synchronous replication. Galera Cluster is an easy-to-use, high-availability solution, which provides high system uptime, no data loss and scalability for future growth.  
        + Docker-compose 用 cluster 的時候要注意 depends-on 的順序  
        + Azure 西歐的機房在荷蘭  
        + DB 要設定 volumes 才能永久儲存資料，否則 container 一關掉，DB 的資料也會不見。  
    6. [Docker 1.12 Swarm 和 MySQL Cluster & WordPress](https://www.katacoda.com/philipz/courses/swarm/1)  
        + Docker Swarm  
            + Managers (Raft consensus group), Workers (Gossip Network), gRPC  
            + Mesh Network  
            + 會眾反應：之前有遇過用 Docker Swarm 然後出問題，用了 swarm left 然後把 node 砍掉，再把 Docker 相關的東西全部移除，之後重裝 Docker 和 Docker Swarm，發現設定檔仍舊是出問題的那個，並沒有被重裝，所以想請問 Managers 的設定檔到底是存在實體機器的哪裡？（A：不知道，可能要去看 Source code，也可以去 Docker 的 github 發個 issue 反應一下。）  
            + Manager 數量建議為三台以上，原因請見[拜占庭將軍問題](http://www.twword.com/wiki/%E6%8B%9C%E5%8D%A0%E5%BA%AD%E5%B0%87%E8%BB%8D%E5%95%8F%E9%A1%8C)，由 Leslie Lamport 所提出。  
  
    7. [Serverless 架構 & Docker (DockerCon 2016 Hackathon 作品)](https://www.katacoda.com/philipz/scenarios/8)  
  
+ `nvidia-docker run -it --rm -p 8888:8888 tensorflow/tensorflow:nightly-gpu`  
    + nvidia-docker 會幫你把 GPU 掛載到 docker 裏面。  
+ 有獎徵答  
    + Docker Network 在 Docker 1.9.0 以後出現  
    + Docker Swarm 的 Worker 是在 Docker 1.12 以後出現的  
  
這場 workshop 的內容個人覺得算蠻充實的，  
（好像滿多沒聽過 Docker 的新手跑來聽，結果跟不上就中途離席了 XD）  
我也差點跟不太上，畢竟跟 Docker 還沒有到很熟...  
  
講者的簡報內容都是公開的，  
覺得這種作法還挺不錯的，  
有興趣的人點選上面的連結自己閱讀就行了。  
  
因為講者是 O'REILLY 的 《Docker 錦囊妙計》的譯者，  
所以現場贈送五本，  
因為題目挺簡單的，  
所以就舉手拿了一本，  
本來打算在天瓏攤位買的，  
於是就賺到一本書了。  
![docker](/files/coscup-2016/docker.jpg)  
  
---  
  
## 《寫出高性能的服務與應用。那些你沒想過的事！》 by 小傑  
  
Docker workshop 結束後就跑來聽小傑學長的 talk，  
發現 IRC 上好多人都說根本是在複習大學的 OS，  
還有人說這是不是 Synology 的面試題目，  
覺得大家好毒呀，  
可能是我大學 OS 沒學好，  
我覺得複習一下也挺不錯的。  
但也可能是因為題目下的有點內容農場式，  
結果大家發現內容不如預期吧？  
果然標題還是下的腳踏實地一點比較好。  
  
---  
  
## Lightning talks  
  
> 發現好多認識的人都上去講了，  
> 但我好像還沒講過哪一場 Conf 的 Lightning talk，  
> 也沒在 R0 給過 talk，  
> 也許該找個機會解鎖成就一下。  
  
因為沒有現場筆記，  
所以就照記憶中的狀況紀錄一下吧，  
不一定會照順序。  
  
+ RS 的自幹 VR Pokemon GO  
+ tnlin 的 PokemonGo-TSP  
+ Denny 的瘋狂走路瘦身法  
+ Pellaeon 的臺灣程式路跑  
+ 蒼時的爸媽都認不得的 Ruby  
+ 中國來的會眾找人幫忙把 RMS 的 《Free Software, Free Society》中文化  
    + 想到我這本買了給 RMS 簽名，但只看一點點就沒看了，到現在還沒看完...  
+ 兩分鐘打臉 MTK  
    + 覺得這個最猛，只改兩行 code 就讓 MTK 的 LinkIt Smart 7688 同時支援 AP mode 跟 client mode，根本充份顯示了企業的程式碼應該要開源的重要性，不然使用者遇到問題根本沒有機會自己改。  
+ V字龍的臺灣社群非官方客製版 Ubuntu 作業系統  
    + 覺得這個還蠻棒的耶，不然臺灣自由軟體的中文化這塊真的幾乎快要沒人弄了，而且還自己先修了一些還沒被 upstream merge 的 bug，雖然我現在沒在用 Ubuntu 了，這個真的蠻值得支持的。  
+ pyclub - pycontw code sprint 的宣傳  
+ 交大丁戊組的工商服務  
  
---  
  
## BoF  
  
看到廠商攤位上有一張很神奇的履歷調查問卷，  
Slack 跟 Trello 算在專業技能裏面。  
![resume](/files/coscup-2016/resume.jpg)  
  
然後依照慣例就是披薩跟可樂吃到飽。  
![pizza](/files/coscup-2016/pizza.jpg)  
  
跑去 CTLUG x openSUSE x RailsFun，  
看到了有點久沒看到的 JC，  
還從他那邊拿到了很有趣的自製木牌避邪符，  
真的是目前遇過亂點技能樹最強的傢伙。  
![amulet](/files/coscup-2016/amulet.jpg)  
  
之後就和小趴還有喜德去各個 BoF 亂晃，  
然後臨時和雨蒼還有其他幾個人臨時組一個 Pokemon GO BoF，  
跑去外面抓呆呆獸（被它逃走了QQ）、電擊獸、迷你龍  
  
---  
  
# Day 2: 2016/08/21 Sun  
  
  
## 用 JS 自幹（鋼鐵人電影裡頭的）Jarvis by 李慕約  
  
+ <https://sheethub.github.io/smartcity2016/map/map2.5d.html>  
    + 應該是用 [GCP 的 Speech API](https://cloud.google.com/speech/)?  
+ Heilmeier Questions  
    + 是這個？ <http://www.design.caltech.edu/erik/Misc/Heilmeier_Questions.html>  
  
## Debater 辯論家：網路筆戰大亂鬥 by ETBlue  
  
+ <https://github.com/ETBlue/debater>  
+ Related links  
    + <https://github.com/ETBlue/gw2inventory>  
  
---  
  
## 開放公司文化之下的軟體開發 / 如何用開源軟體賺錢？ by 翟本喬  
  
+ 「要怎麼解決這個問題呢?」 政府：「辦一個比賽。」  
    + 笑著笑著就哭了  
+ 「還好我們沒有中華民國奧林匹克開源軟體協會。」  
+ LibreOffice  
+ ownCloud  
+ S3QL  
+ 和沛如何用開源軟體？  
    + 觀察客戶要什麼  
    + 加上重要功能  
    + 願意自己重寫  
    + 甚至徹底改變商業模式  
    + 建置世界級的大系統  
+ 找到使用者的痛，並解決它。  
  
> 真的覺得應該要一直強調一點：  
> 參與開源軟體真的不能只停留在使用者  
> 要讓每一位參與者都要有自己的貢獻是不可或缺的自覺  
> 不一定只侷限在寫程式  
> 不管是工作人員、翻譯或是其他跟 Open Source 有關的活動都是需要的  
> 真的不能只停留在一年參加一次 Conf 看人家演講  
> 每一個人都可以讓臺灣在 Open Source 界被其他國家看見  
  
---  
  
## Lightning talks  
  
+ othree: 用 git 線圖來畫臺北捷運路網  
    + <https://github.com/othree/taipei-mrt>  
    + 用完以後我更懂 git branch 跟 git log 了  
+ jackymaxj: HackMD  
    + <https://hackmd.io/p/HyTkWyJF#/>  
    + <https://hackmd.io/>  
+ 海豹：SITCON HK  
    + 今年十月  
+ 徵音梅林新歌發表 - YChao  
    + 三天三夜！  
+ 三分鐘送 first kernel patch - louielu  
+ 報到 App 的開發秘辛 - Denny Huang  
+ Chinese Character - DaeHyun Sung  
    + 韓國講者  
    + <https://telegram.me/cjkvBot>  
    + 感覺好猛啊，reference 裡頭竟然有 O'REILLY 的 CJKV 的書，我也是前陣子幫 Pellaeon 拿書才發現 O'REILLY 竟然有出關於字型編碼的書，而且超大一本，內容涵蓋中文(C)、日文(J)、韓文(K)、越南文(V)。  
  
---  
  
## Thoughts  
  
不知道是因為開始工作了以後心境轉變了還是其他原因，  
今年參加 Conf 沒有像以前聽那麼多議程了，  
也沒有開 IRC、沒開共筆。  
已經變成像以前社群長輩那樣，  
參加 Conf 比較像是為了見見一陣子沒看到的朋友，  
聊聊天、彼此交換一下資訊還有近況等等  
也不知道是不是個好現象就是。  
  
其實有想過，  
如果有真的想聽的議程沒聽到的話，  
還是可以會後自己去看錄影和簡報，  
（甚至拿來在工作的時候聽也 OK，  
畢竟現在工作的時候就會順便聽 Podcast 了。）  
大概只有 HITCON 有些不願意公開錄影和簡報的需要當場聽。  
  
然後現在都會儘量挑標題看起來比較不那麼浮誇和技術成份看起來比較多的 talk，  
往往內容比較紮實，  
而且人也比較少，  
不會沒地方坐。  
一開始來參加 Conf 的時候因為聽不太懂，  
所以都會挑比較有表演性質或嘴炮的 talk 聽，  
畢竟太難的就聽不懂了，  
我想這是比較明顯的差別吧。  
  
今年參加的時候不知道為何，  
一直有種 COSCUP 2015 恍若昨日的感覺，  
不知道是不是因為這一年過的不夠充實。  
其實開始工作以後，  
一直覺得工作比待在學校還輕鬆，  
不知道是自己鬆懈了，  
還是工作內容的問題，  
我想這是自己下半年要調整的方向吧。  
  
然後希望從今年開始，  
以後參加 COSCUP 都跟這次一樣要拿開源貢獻者的票，  
其實之前有想過，  
以後參加 Conf 要不要都給自己設下一定要投稿甚至當講者才能去的規則，  
我想就拿這個目標努力吧。  
