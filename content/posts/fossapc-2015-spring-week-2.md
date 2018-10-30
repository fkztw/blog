Title: FOSSAPC 2015 Spring Week #2
Slug: fossapc-2015-spring-week-2
Date: 2015-03-09 23:40:43
Authors: m157q
Category: Course
Tags: Course, FOSS
Summary: A note for 2015 FOSS course in NCTU, Hsinchu, Taiwan
Modified: 2018-10-31 06:15:43

因為配合課程的需求
就直接看 Hackpad 吧

- （舊連結）[2015 FOSS Week #2 Note - fossapc.hackpad.com](https://fossapc.hackpad.com/2015-FOSS-Week-2-Note#2015-FOSS-Week-2-Note)
- 新連結：<https://paper.dropbox.com/doc/2015-FOSS-Week-2-Note--AQnq5MGikUiPlfXj5EBF4xCUAg-6hu43RXcaTrewq2ouWOO3>
（Hackpad 已被 Dropbox Paper 買下）

之後應該就不另外再寫 markdown 記錄了
雖然還是不太喜歡直接用 hackpad
太多人的時候還是會噴 502
以及同時多人中文輸入還是會有打架的問題
也許可以考慮之後都用英文來記錄
好像也是個不錯的選擇

---

## 2018.10.31 後記

因為當時上課主要都是我在打字，花了不少時間。
當時懶得再把內容記錄到自己的 blog 上，想說看 Hackpad 就好，
結果後來 Hackpad 被 Dropbox 買下變成 Dropbox Paper 後，
共筆變成都要登入後才看得到，
所以還是想說記錄到這裡來，
至少想看的時候可以看得到，
誰知道 Dropbox 哪天會不會消失呢？

以下直接 export markdown 格式然後貼上：

---


# 2015 FOSS Week #2 Note


# **複習 Week #1: Revolution OS**

共筆:

- Week #1 NOTE
- 從 Revolution OS 看作業系統生態變化

說明 [Homework #1](https://sites.google.com/site/fossapc/class-news/homework12015spring) 進行方式

- 影片觀賞：
[ ] 《[Revolution OS](https://www.youtube.com/watch?v=jw8K460vx1c)》
  - [esr - The Cathedral and the Bazaar](http://www.catb.org/esr/writings/cathedral-bazaar/cathedral-bazaar/)
  - 1971, RMS 加入 MIT 的 AI Lab (現已改名為 [CSAI Lab](https://www.csail.mit.edu/)) 裡頭全是當時非常活躍的 Hackers
  - [4:51] [光筆](http://www.baike.com/wiki/%E5%85%89%E7%AC%94)與航空指揮中心
  - 登月計劃的多人多工作業系統: CTSS (Compatible Time-Sharing System)
  - password 的出現
  - 自製電腦俱樂部 [Homebrew Computer Club](http://en.wikipedia.org/wiki/Homebrew_Computer_Club)
    - 1976, [An Open Letter to Hobbyists](http://en.wikipedia.org/wiki/Open_Letter_to_Hobbyists) (by Bill Gates)
      - [原檔截圖](http://en.wikipedia.org/wiki/Open_Letter_to_Hobbyists#mediaviewer/File:Bill_Gates_Letter_to_Hobbyists.jpg)
    - 當時有著作權，但是對於軟體的保護並未完善，主要是因為多數人認為軟體只是附屬品。
    - 時薪兩美元：Bill Gates & [Paul Allen](http://zh.wikipedia.org/wiki/%E4%BF%9D%E7%BD%97%C2%B7%E8%89%BE%E4%BC%A6) 在高中時就開始撰寫 BASIC 程式、為公司開發微處理器專用的 BASIC 編譯器，2 美元是他們高中時期的薪資。
    - [Altair BASIC](http://en.wikipedia.org/wiki/Open_Letter_to_Hobbyists)：針對 MITS *Altair* 小型電腦推出的 BASIC 系統
    - Bill Gates 說：軟體沒有付費就是偷來的
    - [MITS](http://en.wikipedia.org/wiki/Micro_Instrumentation_and_Telemetry_Systems) : 70 年代微型電腦公司
  - 在北歐，可以合法的對軟體做逆向工程。但在美國軟體商業化的觀念下，對軟體進行反組譯或是逆向工程是違法的。
    - EULA (End-User License Agreement) 制定的精神也不同
  - 在當時，作業系統幾乎都是需要授權才能使用，而價格不盡相同。並且必須簽署協議，保證不將軟體分享給其他人
    - AT&T 的 Unix 需要高額授權金： 999 美元
    - DOS的授權金： 15 美元
  - [Book] [Open Sources: Voices from the Open Source Revolution](http://www.oreilly.com/openbook/opensources/book/)
  - RMS 為了反制這種軟體私有化的文化，創造了一個可以自由分享的 OS 來作為 Unix 的替代品，並將名字取為 [GNU: GNU's Not Unix](https://www.gnu.org/) 用來諷刺 UNIX
  - 電話號碼： ITS-UNIX （從商標到電話，都視為資產來保護）
    - 導致和 AT&T 的官司訴訟: [http://redhat.ecenter.idv.tw/bbs/showthread.php?postid=221810](http://redhat.ecenter.idv.tw/bbs/showthread.php?postid=221810)
    - 有一家公司 Berkeley Software Design, Inc.(BSDI)從事 4.4BSD 商業化。該公司產品名為 BSD/386，並宣稱 BSD/386 經過了Berkeley 的改寫,已經沒有 AT&T 的原始碼了，不過 AT&T 還是對Berkeley和BSDI提出告訴。導火線是 BSDI 的電話: 1-800-ITS-UNIX.此一訴訟延後了4.4BSD 的發表
    - 終於 1994 年 2 月 4 日，雙方達成和解，撤銷告訴， BSDI 發表了不含 AT&T 宣稱的原始碼的4.4BSD 原始碼，稱為 4.4BSD-Lite.
  - Unix-like 與 POSIX 的出現
    - [POSIX](http://en.wikipedia.org/wiki/POSIX)
      - P for Portable
      - O for Operating
      - S for System
      - I for Interface
      - X for Unix
    - POSIX 的規格是有分版本的，目前是由 [Open Group](http://www.opengroup.org/) 制定
  - [BSD](http://en.wikipedia.org/wiki/Berkeley_Software_Distribution): 全名為 Berkeley Software Distribution，為 Berkeley 開發的 Unix Operating System，因為 AT&T 授權問題，較晚被使用者接受。
  - Richard Stallman / FSF 當時收入來源：販售 Emacs 磁帶、接受捐贈、為公司進行教育訓練，算是實踐 GNU Manifesto  的「服務」性質收益，但一直到了 Cygnus Solutions 出現，才開始企業化經營 Free software 商業化
  - 1991 年
    - GNU U許多程式替換完成
    - 當時已有 gcc, gdb, yacc, emacs, TeX ... 等工具程式
    - 這也是 Linux 釋出第一年
  - 本片最帥型男 [Michael Tiemann](http://en.wikipedia.org/wiki/Michael_Tiemann)
    - [http://people.redhat.com/tiemann/](http://people.redhat.com/tiemann/)
    - 早期與 RMS 合作開發 gcc 編譯器 (在他22歲的時候)
    - 他和 RMS 現在都不寫 code 了
    - 創立第一家以自由軟體形式獲利公司  [Cygnus Solutions](http://en.wikipedia.org/wiki/Cygnus_Solutions), 現為 [Red Hat](http://en.wikipedia.org/wiki/Red_Hat)
    - [Michael Tiemann：GNU C编译器发布20周年纪念](http://blog.csdn.net/jackjoy/article/details/2062414)
    - [MIPS](http://zh.wikipedia.org/wiki/%E6%AF%8F%E7%A7%92%E6%8C%87%E4%BB%A4) (Million Instructions per second**)**
      - e.g. 2009, AMD Phenom II X4 940 Black Edition
      - 42,820 MIPS at 3.0 GHz ( 14.273 MIPS/MHz )
    - GCJ (GNU Compiler for Java) - 把 Java 對應到 C++ 的物件上，稱為 CNI: [https://gcc.gnu.org/onlinedocs/gcc-4.9.0/gcj/About-CNI.html](https://gcc.gnu.org/onlinedocs/gcc-4.9.0/gcj/About-CNI.html)
    - GNU gold: 一個 Linker 實做，由 Google 工程師  Ian Lance Taylor 主導開發。Google 裡頭有些工程師來自 Cygnus / Red Hat，特別在編譯器小組
  - Cygnus solution: gcc 輸出的符號中，以 cyg_ 開頭的函式，就是來自 Cygnus 公司的貢獻
    - gcc 的 -finstrument-functions 參數
    - [eCos](http://ecos.sourceware.org/) 嵌入式作業系統是 Cygnus 開發，其 kernel API 也是以 cyg_ 開頭
[ ] 《[Code Rush](https://www.youtube.com/watch?v=VoLUvE-ny1k)》(Netscape/Mozilla 的紀錄片)
[ ] 《[The Unix System: Making Computers Easier to Use](https://www.youtube.com/watch?v=XvDZLjaCJuw) 》
[ ] 《[A Narrative History of BSD](https://www.youtube.com/watch?v=ds77e3aO9nA)》
[ ] 《[Pirates of Silicon Valley](https://www.youtube.com/watch?v=iX7nSQDFbnQ)》- 講述 Bill Gates 與 Steve Jobs 的故事
  - [http://en.wikipedia.org/wiki/Pirates_of_Silicon_Valley](http://en.wikipedia.org/wiki/Pirates_of_Silicon_Valley)
  - [http://www.imdb.com/title/tt0168122/](http://www.imdb.com/title/tt0168122/)



# **Open Source Ecosystem & Business**

課程網站：[20150309 - Open Source Ecosystem & Business - 自由開源軟體與專案協作](https://sites.google.com/site/fossapc/list-of-lectures/20150309-opensourceecosystembusiness)
對 P. McCoy Smith 和 Wayne R. Chang 論文 [The Evolution of Business Models Using Open Source Software](https://wiki.oulu.fi/download/attachments/58197330/ossd_2015_luu_li_dong_samodelkin.pdf?version=1&modificationDate=1448956483000&api=v2) (2011 年) 進行導讀，探討以下企業的獲利模式:

- Cygnus (現為 Red Hat)
- Novell/SUSE
- IBM
- Sun Microsystems (現為 Oracle)
- HP
- Mozilla Foundation
- MySQL
- Google 的 Android

投影片:

- [Open Sourcefrom Legend, Business, to Ecosystem](http://www.slideshare.net/jserv/opensource-ecosystem)
  - 淘寶年營收從 2003 年的 400 萬元台幣至 2010 年超過 40 億人民幣 (之前沒上市，只能看報導推敲)，成長速度之高，已經到了沒有現成的商業軟體可完美解決該公司面對的技術問題，只好重頭改善開放原始碼的技術，以符合自身需求
    - OaaS (Open-source As A Strategy)
    - 舊有商業方案: IOE
      - I: IBM (server)
      - O: Oracle (database)
      - E: EMC (storage)
  - Microsoft 一開始 (2001) 否認 Open Source，認為它是一個軟體產業的「Cancer」，後來自己也推行一套 Open Source 的授權（2007）。
  - 要去思考我們需要解決什麼樣的問題，如果沒有解決任何問題，則不會有商機。
  - Open Source 提供一個高度可見的協作框架,吸引大公司的關注
  - Open Source 作為公共財的形式,刺激了基礎軟體設施
  - [Symbian](http://en.wikipedia.org/wiki/Symbian)
    - 華冠電子：一間使用 Symbian 來代工功能手機的台灣公司。Symbian 作業系統的授權金行情價是台幣一億元，顯示在當時非開源的手機系統的開發成本極高無比
    - 但是，Android 完全顛覆這樣的模式，把價值上億元的手機系統原始碼，當作廣告來免費放送
  - 高通的專利傘
    - 規定高通的客戶彼此之間不能互相提起法律訴訟
    - 但這規則在去年消失了
    - 這專利傘造成的封閉市場存在了十幾年
    - [小米還有更壞的事？　恐失「高通傘」保護 | 即時新聞 | 20141216 | 蘋果日報](http://www.appledaily.com.tw/realtimenews/article/new/20141216/524954/)
  - [OpenStack](http://en.wikipedia.org/wiki/OpenStack) - [https://www.openstack.org/](https://www.openstack.org/)
  - Nokia 各種手機軟體從頭到腳都是自己開發，Android 這個 Open Source Project 的出現造成整個手機生態的改變。
  - [Open Source Software Business Models](http://events.linuxfoundation.org/sites/events/files/slides/lfcs15_hall.pdf)



# **GNU Autotools + Git**

課程連結: [20150309 - GNU Autotools - 自由開源軟體與專案協作](https://sites.google.com/site/fossapc/list-of-lectures/20150309-gnuautotools)
簡報:

- [GNU Autotools Are What Your Users Need](http://sed.bordeaux.inria.fr/seminars/autotools_20140715.pdf)
  - auxiliary => aux.c, 但 Windows 不允許這個字，aux, AUX 在 Windows 都是保留字
  - Is C really portable? (以下在 gdb 實驗，Linux/x86_64)
    print 0 - 0 => 0
    print 0 - 1 => -1
    print 0U - 1 => 4264697295
    print 0 - 1U => 4294967295
  - the result depends on the architecture of CPU



- 探討案例: [pcmanx](https://code.google.com/p/pcmanx-gtk2/)
  - [https://code.google.com/p/pcmanx-gtk2/](https://code.google.com/p/pcmanx-gtk2/)
  - [https://github.com/pcman-bbs/pcmanx](https://github.com/pcman-bbs/pcmanx)
- 如何安裝 pcmanx
    git clone https://github.com/pcman-bbs/pcmanx.git
    cd pcmanx
- 請先詳細閱讀目錄中的 README 檔案，依據建議安裝必要的套件，否則後續無法進行
- 透過 GNU Autotools 來生成必要的編譯工具
    ./autogen.sh
    ./configure
    make
- 測試 pcmanx
    ./src/pcmanx
- 安裝 pcmanx 到系統目錄
    sudo make install
- 當然也可以解除安裝
    sudo make uninstall
- 倘若想清除所有由編譯器產生的檔案、中間過程的輸出 (包含由 configure 所產生的 Makefile)，可執行以下：
    make distclean
- 小提示
  - 在 configure 階段可以指定不同的 prefix
    ./configure --prefix=/tmp/myhome (make install 安裝的目的地)
  - make 時，可以使用 4 核心來編譯
    make -j4


Git version system

- [30 天精通 Git 版本控管](https://github.com/doggy8088/Learn-Git-in-30-days)
- [Git / GitHub 教學](http://dylandy.github.io/Easy-Git-Tutorial/)
- [Learn Git Branching](http://pcottle.github.io/learnGitBranching/) (精美動畫，必看)



# **課堂問答**

Q1: [Revolution OS 4:51] 這個螢幕叫什麼？
Jserv: 這個設備叫做[光筆](http://terms.naer.edu.tw/detail/1281172/)，跟一般觸控螢幕的原理不太一樣，有些是用磁感應的，有些是有接線的。（2002年 Jserv 當兵時用的設備）
Q2: 你覺得有那些系統需要授權？
[同學]: SunOS, BSD
Jserv: 最早的 BSD 是在 UNIX 的基礎上，而 UNIX 需要去花錢買的，當年需要花 999 美元給 AT&T，後來 AT&T 就拆開了。
*Q3: 你覺得 80 年代 DOS 需要多少錢？*
[同學1]2000?
[同學2]500
[同學3]300
A3: Jserv：答案是 15 美元 (ODM 版本)，且 MS 睜一支眼閉一支眼，他們並沒有刻意去抓盜版的人，讓DOS更快速去擴散，不過他們把額外的功能放在別的地方（另外販售？）。

- 1980 以前
  - Apple
  - Atair
  - Digital Research
  - [CP/M](http://en.wikipedia.org/wiki/CP/M) (Control Program for Microcomputers)
  - [Seattle Computer Products](http://en.wikipedia.org/wiki/Seattle_Computer_Products) (SCP) 開發的 QDOS (Quick and Dirty Operating System)
- 1980 以後
  - MS-DOS 1.0 （單工）
  - DR-DOS （有多工的版本）

Q4: 在《[20年前的今天](http://blog.sina.com.cn/s/blog_4dfa80d301008gfm.html)》中，什麼是RSI？
Q5: Macbook Air 有多少 MIPS ?
A5: 我用的是 MacBook AIr 2013 13-inch 的版本 => **52620 MIPS**

- [http://www.digitaltrends.com/laptop-reviews/apple-macbook-air-13-inch-2013-review/](http://www.digitaltrends.com/laptop-reviews/apple-macbook-air-13-inch-2013-review/)
  - MacBook Air 13-inch boasts a Core i5-4250U processor
- [http://www.notebookcheck.net/Intel-Core-i5-4250U-Notebook-Processor.93564.0.html](http://www.notebookcheck.net/Intel-Core-i5-4250U-Notebook-Processor.93564.0.html)
![](https://hackpad-attachments.imgix.net/hackpad.com_2015-FOSS-Week-2-Note_p.338452_1425881139753_Screen%20Shot%202015-03-09%20at%201.56.50%20PM.png?fit=max&w=882)


Q6: 有沒有聽過 Nortel ?
A6: 沒聽過
Jserv: Nortel 是加拿大的一間電信公司 (2009 年申請破產)，中文名叫做北電，一度是世界上最大的通訊製造商，對 free software 做了頗多貢獻
[http://www.nortel.com](http://www.nortel.com)
Q7: 如何以C program寫字串"C:\windows\temp" ?
A7: 跳脫字元, "C:\\windows\\temp"
