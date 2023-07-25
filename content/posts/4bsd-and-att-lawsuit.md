Title: 4BSD 與 AT&T 官司訴訟的影響
Slug: 4bsd-and-att-lawsuit
Date: 2015-06-16 18:15:23
Authors: fkz
Category: Note
Tags: BSD, AT&T, Open Source
Modified: 2018-10-31 06:09:00
Summary: 這學期修 Jserv 開的《自由開源軟體與專案協作》的期末分組報告，花了不少時間收集資料瞭解歷史，還和兩個組員製作了一部將近十分鐘的短片來介紹（雖然當時因為有點太忙，只參與了劇本編寫和上逐字稿），所以備份在自己的 Blog 紀錄一下。


原連結：<https://fossapc.hackpad.com/B0-1oYaaSKkruW>
新連結：<https://paper.dropbox.com/doc/B0--AQnQPFgBmERuzHLh7WXxOwwlAg-l8sO5FHj37BwLAO6XotW3>
（Hackpad 被 Dropbox 買下來了）

---

影片連結：[https://www.youtube.com/watch?v=LLtj41eyvcA](https://www.youtube.com/watch?v=LLtj41eyvcA)
影片下載：[https://drive.google.com/file/d/0B9cCeTKOkfWIaDJXOW9NUnBCYU0/view?usp=sharing](https://drive.google.com/file/d/0B9cCeTKOkfWIaDJXOW9NUnBCYU0/view?usp=sharing)
字幕檔下載：[https://drive.google.com/file/d/0B9cCeTKOkfWIeXNHUm9hZGFfckU/view?usp=sharing](https://drive.google.com/file/d/0B9cCeTKOkfWIeXNHUm9hZGFfckU/view?usp=sharing)

 **授權聲明**

《USL v. BSDi 官司》之影片與字幕檔由 Pellaeon Lin, Chiu Hsiang Hsu, Shun-Yi Jheng 共同製作，
以創用CC 姓名標示-非商業性-相同方式分享 3.0 台灣 授權條款
([http://creativecommons.org/licenses/by-nc-sa/3.0/tw/](http://creativecommons.org/licenses/by-nc-sa/3.0/tw/)) 釋出。
此作品衍生自 [https://www.youtube.com](https://www.youtube.com) 。



# 影片劇本

[https://www.youtube.com/watch?v=aurDHyL7bTA](https://www.youtube.com/watch?v=aurDHyL7bTA)
不知道能不能做一個類似的短片來介紹...(?

**背景、角色介紹**

- UNIX
- Berkeley
- AT&T
  - Introduction
  - subsidiary company
- USL


**過程**

- 整場訴訟的前情提要
- 為什麼要打官司
- 官司內容
- 最後結果


**影響**

- 對照 Linux 的崛起
- Net/1, Net/2, 386BSD
- BSD 的後續發展




**逐字稿**

【開場】
今天我們要來介紹 UNIX 家族中很有名的作業系統——BSD 歷史上知名的一場法律戰役，Unix System Laboratories 對上柏克萊大學。

【介紹】
首先來介紹一下 UNIX ，UNIX 是 AT&T Bell labs 於 1969 年開發的作業系統，
當時的電腦還很昂貴，最知名的系統是 DEC 公司的 PDP 系列，其中最流行的是 PDP-11 ，
他長這個樣子（show 圖片）。

60 年代晚期，美國 AT&T 公司底下的 Bell Labs 與 MIT 和 General Electric 公司，也就是奇異公司，合作開發一套名為 Multics 的作業系統，這套系統源自阿波羅登月計劃所使用的 CTSS 作業系統，
CTSS 在當時是個很先進的作業系統，全名為 Compatible Time-Sharing System，設計的目標是分時多工，也就是同一時間內，可以讓多個使用者同時執行多個程式，對之後電腦的設計造成重大的影響。

但是呢，AT&T Bell Labs 在 1969 年的時候，因為覺得 Multics 的開發進度實在是太慢了，所以退出了這個計畫。有兩位 Bell Labs 的工程師很不開心——Ken Thompson 和 Dennis Ritchie （畫），Ken Thompson 在 Multics 上面開發了一個太空遊戲 Space Travel ，雖然他再也不用繼續開發 Multics 了，但是這樣就沒有遊戲機可以玩了。Thompson 覺得不開心。「不過沒關係」，Ken Thompson 說，「反正 Space Travel 這遊戲在 Multics 這爛作業系統上面也跑的很慢」，「不如我們來開發一個新的作業系統吧！」。超熱血的 Ken Thompson 在辦公室裡面找到一台閒置的 PDP-7 舊電腦，找了一群人開始開發 UNIX 。

UNIX 一開始使用組合語言開發，運行於 PDP-7 上面，後來主管覺得 UNIX 真不錯，於是提供更多資源給團隊繼續開發，漸漸地， 公司其他部門也發現 UNIX 比起當時 PDP 系列預載的作業系統好用多了，對於 UNIX 的需求逐漸增加，這也使得 UNIX 有了跨平臺的需求。為了滿足跨平臺的需求，團隊發明了一種新的程式語言——C，並且逐漸將 UNIX 的各個部分使用 C 重寫。


後來團隊持續開發，這一系列的 UNIX 稱作 Research UNIX ，也就是早期研究中的 UNIX 。1973 年 11 月，釋出 Research UNIX 第四版，是第一個完整使用 C 語言實作的版本，1974 年 6 月，釋出第五版，這個版本被廣泛授權給教育機構使用——包含柏克萊大學。

背景就先講到這邊，接下來我們移動鏡頭，介紹一下 Berkeley 和 CSRG.

柏克萊大學 1973 年取得 AT&T 的 UNIX 授權之後，1974年成立了一個研究小組——Computer Systems Research Group ，來修改並改進 UNIX ，在 AT&T 與 Berkeley 的授權協議當中，AT&T 允許 Berkeley 修改原始碼，並且將修改後的原始碼發佈給其他 AT&T UNIX 的使用者，這一系列的發佈就稱作 BSD, Berkeley Software Distribution 。BSD 持續地演進，釋出了 1BSD、2BSD、3BSD、4BSD、4.1BSD 和 4.2 BSD，這些版本都包含 AT&T 原始碼，因此只能提供給 AT&T UNIX 的其他使用者。

1980 年的時候，CSRG 接了一個 DARPA 的計劃，DARPA 就是大名鼎鼎的美國國防部高等計劃研究署，當時 DARPA 正在發展 Internet 的前身 ARPANET，DARPA 希望 CSRG 在 UNIX 上面開發 ARPANET 所需的網路功能，包含 TCP/IP 協定，這些功能後來都釋出在 4.3BSD。

4.3BSD 當中的 TCP/IP 是當時最完整的實作，因此很多人都想要，在大家的要求下，柏克萊將 4.3BSD 當中 AT&T 的原始碼移除，將它釋出為 4.3BSD Networking Release 1 ，也就是俗稱的 Net/1 ，這是第一個可以公開流通的 BSD 版本。後來，BSD 團隊中的一位開發者提議，將 Net/1 當中 AT&T 的程式用自己的原始碼重新實作，如此一來公開流通的 BSD 就會更加地完整，經過了18個月的開發，BSD 團隊 1991 年6月釋出了 Networking Release 2 , Net/2 。Net2比起 Net/1 新增了很多功能，原本這些功能是 AT&T 所開發因此無法公開，在 Net/2 當中這些部分都由 CSRG 重新實作了。雖然如此， Net/2 仍然不是完整的作業系統，釋出之前 Net/2 的核心裡面仍然包含少數 AT&T 原始檔，團隊決定將這些檔案移除後釋出 Net/2 。Net/2 是 BSD 歷史上很重要的版本，因為後來許多衍生的 BSD 都是基於 Net/2 來開發的，像是 William 和 Lynne Jolitz 夫婦所開發的 386BSD ，即是將 Net/2 當中缺少的部分重新實作，並移植到 Intel 80386 處理器上面再公開釋出的版本。

1991 年 Net/2 釋出後，CSRG的核心成員出來開了一家公司——BSDI，Berkeley Software Design, Inc ，將 BSD 打包整合成為一個完整的作業系統，稱做 BSD/OS ，BSDI 販售 BSD/OS 的使用授權和支援服務。

這時候 AT&T 不高興了，因為 CSRG 拿 UNIX 的原始碼來修改成 4.3BSD Net/2 ，BSDI 又再拿 Net/2 包裝成 BSD/OS ，再拿去賣。當時的 BSD/OS 授權及原始碼，只要 995 美金，但是功能幾乎完全一樣的 AT&T UNIX/32V 要價超過 20000 美元，AT&T 的顧客都被搶走了。
雖然 Berkeley 認為他們已經將 AT&T 的原始碼都移除了，但是 AT&T 認為還是有侵權 ，於是1992年的時候透過他們的子公司 UNIX System Laboratories ，USL 對 BSDI 公司提出了告訴。

原告 USL 認為柏克萊大學釋出的 Net/2 當中部分檔案是 USL 的智慧財產，但是柏克萊認為他們已經移除所有 USL 的檔案。而雙方的爭議就在於，當時 AT&T 為了要推廣 UNIX ，默許部分的 UNIX 原始碼公開在教科書內，因此柏克萊認為這可以視為 AT&T 允許這些原始碼的公開流通，而 AT&T 不這麼認為。
並且，柏克萊認為他們釋出的部分原始碼屬於合理使用範圍，這些原始碼是 POSIX 規範的實作，幾乎只能有一種實作方法，因此他們使用這部分的原始碼不算侵權。這邊補充解釋一下 POSIX ，POSIX 是一套作業系統 API 的規範，宗旨在於希望各種不同的作業系統間至少能夠維持基本的相容性。
最後，柏克萊還說，USL 所聲稱的這些屬於他們的檔案，僅佔 Net/2 的極小部分，因此 Net/2 不能算是 UNIX/32V 的衍生作品。

訴訟進行了一年，後來 1993 年雙方在法庭外和解。和解的雙方同意不再針對此一案件進行後續法律行動。和解的條件有好幾項，但是最重要的是，柏克萊會將極少數的侵權檔案移除或修改，在 BSD 一萬八千個檔案中，柏克萊只需刪除其中3個，並且將其中70個加上 USL 的版權宣告，整個和解的結果大致是對 BSD 有利的。

訴訟之後，柏克萊1994 年釋出了下一版本的 BSD —— 4.4BSD ，4.4 BSD 又再分為兩個版本，4.4BSD-Lite 以及 4.4BSD-Encumbered ，其中 4.4BSD-Lite 是不包含任何 AT&T 原始碼的版本，允許公開流通；而 4.4BSD-Encumbered 則包含了 AT&T 原始碼，僅提供給 AT&T UNIX 合法授權的使用者使用。

1995 年的時候，柏克萊釋出了最後一版的 BSD—— 4.4BSD-Lite Release 2 ，釋出之後 CSRG 就解散了，柏克萊大學不再繼續開發BSD 。不過，解散的這群人，他們又各自發起了新的開發計劃，大部分都是基於 4.4BSD-Lite ，以及 Jolitz 夫婦所開發的 386BSD 。這些新計劃大多都延續到今日，有 FreeBSD 和 NetBSD ，後來 FreeBSD 又分支出 DragonflyBSD ，NetBSD 又分支出 OpenBSD 。

今天，FreeBSD 是 BSD 家族中最受歡迎的版本，而其他的 BSD 也都有在持續的開發並釋出新版本。

BSD 家族的故事就講到這邊了。


# 過程
- USL 1992 年提起訴訟，1994年和解，和解條件2004年公開
- USL 原訴：
  - Berkeley 釋出的 NET-2 違反了 USL 和 Berkeley 的軟體授權協議以及 USL 對 UNIX 的著作權
  - 等等，都是關於 NET-2
- [UNIX System Laboratories, Inc. v. Berkeley Software Design, Inc.](https://goo.gl/kA97T6)
  - ***USL v. BSDi*** was a [lawsuit](https://en.wikipedia.org/wiki/Lawsuit) brought in the United States in 1992 by [Unix System Laboratories](https://en.wikipedia.org/wiki/Unix_System_Laboratories) against [Berkeley Software Design](https://en.wikipedia.org/wiki/Berkeley_Software_Design), Inc and the [Regents of the University of California](https://en.wikipedia.org/wiki/Regents_of_the_University_of_California) over [intellectual property](https://en.wikipedia.org/wiki/Intellectual_property) related to [UNIX](https://en.wikipedia.org/wiki/Unix).  The case was settled out of court in 1993 after the judge expressed  doubt in the validity of USL's intellectual property, with Novell (who  by that time had bought USL) and BSDi agreeing not to litigate further  over the [Berkeley Software Distribution](https://en.wikipedia.org/wiki/Berkeley_Software_Distribution) (BSD), which would later develop into a [range of BSD](https://en.wikipedia.org/wiki/Comparison_of_BSD_operating_systems) distributions, each tuned to its own specific audience's strengths and markets.
- [Berkeley Software Distribution](https://en.wikipedia.org/wiki/Berkeley_Software_Distribution)
  - Historically, BSD has been considered a branch of Unix, **Berkeley Unix**, because it shared the initial codebase and design with the original [AT&T](https://en.wikipedia.org/wiki/AT%26T) Unix operating system.
  - 4.1BSD (June 1981) was a response to criticisms of BSD's performance relative to the dominant VAX operating system, [VMS](https://en.wikipedia.org/wiki/OpenVMS). The 4.1BSD kernel was systematically tuned up by [Bill Joy](https://en.wikipedia.org/wiki/Bill_Joy) until it could perform as well as VMS on several benchmarks. The release would have been called *5BSD*, but after objections from [AT&T](https://en.wikipedia.org/wiki/AT%26T) the name was changed; AT&T feared confusion with [AT&T](https://en.wikipedia.org/wiki/AT%26T)'s [UNIX System V](https://en.wikipedia.org/wiki/UNIX_System_V).
  - Net/1
    - Until then, all versions of BSD incorporated proprietary AT&T Unix  code and were, therefore, subject to an AT&T software license.  Source code licenses had become very expensive and several outside  parties had expressed interest in a separate release of the networking  code, which had been developed entirely outside AT&T and would not  be subject to the licensing requirement. This led to **Networking Release 1** (**Net/1**), which was made available to non-licensees of AT&T code and was [freely redistributable](https://en.wikipedia.org/wiki/Free_software) under the terms of the [BSD license](https://en.wikipedia.org/wiki/BSD_license). It was released in June 1989.
  - Net/2
    - After Net/1, BSD developer [Keith Bostic](https://en.wikipedia.org/wiki/Keith_Bostic)  proposed that more non-AT&T sections of the BSD system be released  under the same license as Net/1. To this end, he started a project to  reimplement most of the standard Unix utilities without using the  AT&T code. For example, [vi](https://en.wikipedia.org/wiki/Vi), which had been based on the original Unix version of [ed](https://en.wikipedia.org/wiki/Ed_%28Unix%29), was rewritten as [nvi](https://en.wikipedia.org/wiki/Nvi)  (new vi). Within eighteen months, all of the AT&T utilities had  been replaced, and it was determined that only a few AT&T files  remained in the kernel. These files were removed, and the result was the  June 1991 release of Networking Release 2 (Net/2), a nearly complete  operating system that was freely distributable.
    - Net/2 was the basis for two separate ports of BSD to the [Intel 80386](https://en.wikipedia.org/wiki/Intel_80386) architecture: the free [386BSD](https://en.wikipedia.org/wiki/386BSD) by [William Jolitz](https://en.wikipedia.org/wiki/William_Jolitz) and the [proprietary](https://en.wikipedia.org/wiki/Proprietary_software) [BSD/386](https://en.wikipedia.org/wiki/BSD/OS) (later renamed BSD/OS) by [Berkeley Software Design](https://en.wikipedia.org/wiki/Berkeley_Software_Design) (BSDi). 386BSD itself was short-lived, but became the initial code base of the [NetBSD](https://en.wikipedia.org/wiki/NetBSD) and [FreeBSD](https://en.wikipedia.org/wiki/FreeBSD) projects that were started shortly thereafter.
    - BSDi soon found itself in legal trouble with AT&T's [Unix System Laboratories](https://en.wikipedia.org/wiki/Unix_System_Laboratories) (USL) subsidiary, then the owners of the System V [copyright](https://en.wikipedia.org/wiki/Copyright) and the Unix trademark. The [*USL v. BSDi*](https://en.wikipedia.org/wiki/USL_v._BSDi) lawsuit was filed in 1992 and led to an [injunction](https://en.wikipedia.org/wiki/Injunction) on the distribution of Net/2 until the validity of USL's copyright claims on the source could be determined.


**和解條件**


- 釋出不包含爭議原始碼的發行版 4.4BSD-lite ，Berkeley 鼓勵使用者改換此版本
- Berkeley 停止散佈部分檔案
- USL 給爭議原始碼的使用者三個月的寬限期
- 部分 Berkeley 散佈的檔案必須包含 USL 授權告示
- 部分 USL 散佈的檔案必須包含 Berkeley 授權告示
- USL 允許自由散佈部分檔案
- University not to actively assist in legal attempts to challenge USL's rights to certain files.


Ref:

- [The 1994 USL-Regents of UCal Settlement Agreement  - PDF and text](http://www.groklaw.net/article.php?story=20041126130302760)



# 影響
- The lawsuit slowed development of the free-software descendants of BSD  for nearly two years while their legal status was in question, and as a  result systems based on the [Linux kernel](https://en.wikipedia.org/wiki/Linux_kernel), which did not have such legal ambiguity, gained greater support. Although not released until 1992, development of [386BSD](https://en.wikipedia.org/wiki/386BSD) predated that of Linux. [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds) has said that if 386BSD or the [GNU kernel](https://en.wikipedia.org/wiki/GNU_kernel) had been available at the time, he probably would not have created Linux.



# **BSD Family**



- [/share/misc/bsd-family-tree](https://github.com/freebsd/freebsd/blob/master/share/misc/bsd-family-tree)



- 386BSD
  - 由 Berkeley 校友  [Lynne Jolitz](http://en.wikipedia.org/wiki/Lynne_Jolitz) 和 [William Jolitz](http://en.wikipedia.org/wiki/William_Jolitz) 把 4.3BSD-Reno / 4.3BSD Net/2 移植到 Intel 80386 上 (80386 硬體在當時相對便宜很多)
  - 補上了 Net/2 缺乏的部份
  - 成為 FreeBSD 和 NetBSD 的基礎
  - 沒有被牽入訴訟之中
  - 台灣當時有 Newsgroup (tw.bbs.comp.386bsd) 在研究 BSD 相關技術
- 4.3BSD
  - Net/1 ：包含 berkeley 修改的 networking code
  - Net/2 ：berkeley 改寫了更多工具程式，以規避 at&t 的著作權
- 4.4BSD
  - 4.4BSD-Lite : 訴訟和解後 berkeley 釋出不含 AT&T 原始碼的版本，BSD License
  - **4.4BSD-Encumbered** : 包含 AT&T 原始碼，僅提供給 AT&T 授權者



# 補充
- [商業應用自由開源軟體的訴訟大事紀概述](https://www.dropbox.com/s/ih4eius66dyr1qi/20150422.pdf?dl=0)



# **角色介紹**
- **USL** (UNIX System Laboratories, Inc.)
  - 1989 創立，是 Bell labs 的子組織
  - 1990開始負責 UNIX 開發
  - 後來變成 AT&T 的 wholly owned subsidiary ，完全受到 AT&T 控制的子公司
  - Bell labs 又是 AT&T 的一個部門（或是子公司？）
  - 1993/Jun Novell 買下 USL ，所有財產、商標及專利，包含 UNIX 的財產權
- BSDI (Berkeley Software Design, Inc.)
  - 1991 由 Rick Adams 及 CSRG 的成員們所創立
  - 開發及販賣 BSD/OS （proprietary 版本的 BSD）的授權
  - 1999 試圖模仿 RedHat 的模式進行 IPO ，不幸的是這個策略後來失敗，總裁 Rob Kolstad 離開公司之後不久，公司面臨破產
  - 2000 BSDI 與 [Walnut Creek CDROM](https://en.wikipedia.org/wiki/Walnut_Creek_CDROM) 合併
  - 2001 年，在巨大的財務壓力下，BSDI 將軟體部門售出給[Wind River Systems](https://en.wikipedia.org/wiki/Wind_River_Systems)，公司的剩餘部門更名為 iXsystems ，專注在伺服器硬體的業務
- CSRG, **Computer Systems Research Group**
  - CSRG 是 Berkeley 的研究團隊，目的在 AT&T UNIX 的基礎上進行開發及增強，經費來源是 DARPA
  - 1974 柏克萊大學的 Bob Fabry 教授從 AT&T 取得 UNIX 的授權，Berkeley 開始修改 AT&T UNIX ，並將修改後的版本發佈為 Berkeley Software Distribution
  - 1980/Apr Professor Fabry 跟 DARPA 簽了合約，進一步開發 UNIX 以支援 ARPAnet 功能使用的需求
  - 1995 解散




# 問題
1. FreeBSD 是否有像 Linux 一樣類似 OIN 的組織？
  1. 似乎是沒有，請老師補充（補充：如果指的是「協助處理專利問題的相關組織」，沒有。）
  2. The FreeBSD Foundation 會協助處理專利問題，還有其他法律或是和廠商間的合約問題。
2. 這場戰爭後對於之後開源與商業間有什麼影響？（基本上就是稍阻開源軟體的商業應用，一段時間內商業公司迴避採用BSD-based的系統來進行產品製作，一直到GNU Linux的重新創作，才又再蓬勃發展。）
3. Difference between NET/1 and NET/2 ?h
  1. 衍生著作 (derivative work) 的基本原則 : A work based on the original work.
  2. 抄襲
    1. 抄 - 著作權
    2. 襲 - 改作權
  3. NET/1 先處理"抄"的問題
  4. NET/2 再處理"襲"的問題
4. 為什麼 Jollitz 沒有被告但是 BSDI 卻被告了？
  1. 歸責-因果關係



4. Difference between NET/1 and NET/2?
  1. 抄襲：抄─侵犯著作人的重製權 reproduction；襲─侵犯著作人的改作權，如翻譯哈利波特，即是改作的行為，因此須先取得作者的許可。
  2. 抄襲 in 程式碼：抄─直接抄程式碼；襲─根據別人的程式碼進行改寫。改寫又牽扯到 衍生著作 derivative work: a work based on the original work.
  3. 訴訟的目的不一定是要贏，有時候是為了阻斷對方的商業進展。以 AT&T 和 BSD 的訴訟而言，AT&T 確實是該告對方(阻止 BSDi 的商業發展)，就結果來說(和解且 BSDi 發展不下去) AT&T 是獲勝的，只是沒想到後有 Linux 的出現。
5. 386BSD: 由一對 Berkeley 校友從 NET/2 版本進行改寫，將此作業系統成功移植至 intel 80386 (當時比較便宜的電腦主機) 並將所有跟 AT&T 相關的程式碼拔除，以及補上其不足的功能。後來成為 FreeBSD、OpenBSD 的前身。



# 分工表
- 過程：鄭順一
- 影響：許邱翔
- 角色介紹：林育德




# Misc & Memo


**A Narrative History of BSD**

**Wikipedia**

- [https://en.wikipedia.org/wiki/Berkeley_Software_Distribution](https://en.wikipedia.org/wiki/Berkeley_Software_Distribution)

  ****
**FreeBSD.org**

- [https://www.freebsd.org/doc/en_US.ISO8859-1/articles/explaining-bsd/why-is-bsd-not-better-known.html](https://www.freebsd.org/doc/en_US.ISO8859-1/articles/explaining-bsd/why-is-bsd-not-better-known.html)


**參考**

- [**Unix Wars**](http://www.livinginternet.com/i/iw_unix_war.htm)
- [Twenty Years of Berkeley Unix - From AT&T-Owned to Freely Redistributable](http://www.oreilly.com/openbook/opensources/book/kirkmck.html)
- [The FreeBSD Diary -- Why is Linux Successful? - An Opinion.](http://www.freebsddiary.org/linux.php)
  - support of cheap hardware
  - visibility on Usenet (marketing)
  - the USL lawsuit against BSD
  - [Why](https://www.freebsd.org/doc/en_US.ISO8859-1/articles/explaining-bsd/why-is-bsd-not-better-known.html)
  - [is BSD not better known?](https://www.freebsd.org/doc/en_US.ISO8859-1/articles/explaining-bsd/why-is-bsd-not-better-known.html)
- [Interview with Andrew Tanenbaum](http://linuxfr.org/nodes/88229/comments/1291183)
  - The reason MINIX 3 didn't dominate the world has to do with one mistake I  made about 1992. At that time I thought BSD was going to take over the world. It was a mature and stable system. I didn't see any point in  competing with it, so I focused MINIX on education. Four of the BSD guys  had just formed a company to sell BSD commercially. They even had a  nice phone number: 1-800-ITS-UNIX. That phone number did them and me in.  AT&T sued them over the phone number and the lawsuit took 3 years  to settle. That was precisely the period Linux was launched and BSD was  frozen due to the lawsuit. By the time it was settled, Linux had taken  off. My mistake was not to realize the lawsuit would take so long and  cripple BSD. If AT&T had not brought suit (or better yet, bought  BSDI), Linux would never have become popular at all and BSD would  dominate the world.
  - [https://lwn.net/Articles/467852/](https://lwn.net/Articles/467852/)
- 1996 年的 WWDC 上，Apple 宣佈推出 [MkLinux](http://en.wikipedia.org/wiki/MkLinux)，這是建構於 Mach microkernel 的 Linux 系統，運作於 Macintosh  電腦硬體。雖然之後 MkLinux 停止發展，但至今 [Mac OS X 的原始程式碼](http://opensource.apple.com/)仍可見到 MkLinux 的蹤跡，像是在 libc。之後隨著 NeXTSTEP 的合併進 Apple，BSD 程式碼和 Mach microkernel 組成了 [XNU](http://en.wikipedia.org/wiki/XNU) 這個新的 hybrid。MkLinux 是首個由 Apple 支持的開放原始碼專案，開發經驗對日後以 Mach 3.0 為基礎的 Mac OS X 有很大的助益。
  - 1991 年末釋出的 Linux kernel，到 1995 年就促使 Open Software Foundation (和 open source 推廣無關，但部份成果的確以 open source license 釋出) 與 Apple 採納作為產品核心
  - 參考資料: [History of Linux for the PowerPC](https://gate.crashing.org/doc/ppc/doc003.htm)
  - MkLinux 許多原始程式碼的宣告是 Copyright 1991-1998 Open Software Foundation, Inc. (MIT 授權)，如 DR3/osfmk/src/mach_kernel/i386/i386_lock.s
- [AT&T lawsuit helps to launch Linux into mainstream](http://www.softpanorama.org/People/Torvalds/Finland_period/att_lawsuit_as_a_launcher_for_linux.shtml)
  - 時間點很重要
  - "In late 1991 there were 100 programmers on UseNet producing improvements for (BSD)," said Wes Peters, a BSD user from the beginning. "If not for the AT&T lawsuit at the worst moment.... Because of that, people said, 'I don't want to go with BSD now.' That was the time Linux was gaining functionality."
- Unix版权史
  - [http://www.ruanyifeng.com/blog/2010/03/unix_copyright_history.html](http://www.ruanyifeng.com/blog/2010/03/unix_copyright_history.html)
  - AT&T与BSD之间的诉讼，是当代版权制度最恶劣的应用之一。
  - 为什么这么说？
  - 首先，起诉者其实与Unix毫无关系。这是AT&T经理层的决定，而不是开发者的决定。事实上，包括Ken Thompson在内的技术人员一直希望，公司能够公开源码。他们完全有理由这么要求，因为Unix从来不是AT&T的业务重点，最初是个人项目，后来也没有占用公司太多资源。销售Unix的利润，在公司全部业务中，几乎可以忽略不计。为了一点点钱，去打击一个使许多人受益的产品，何必这样做呢。
  - 其次，AT&T根本不关心Unix的发展。它真正关心的是金钱和削弱对手。1994年，官司还没有结束，它就把Unix卖给了Novell公司，从此不再与Unix发生关系，官司也因此不了了之。既然你不想要这个产品，为什么要提起诉讼呢？真是不可理解。
  - 最后，所谓的侵权几乎是不存在的。因为Novell从AT&T买下Unix版权后，检查了BSD的源码，在18000个组成文件中删除了3个，并对其他文件做了一些小修改，然后BSD就重新获得了自由发布源码的许可。这意味着，至多只有千分之一的BSD代码有版权问题，但是就因为这千分之一的问题，导致百分之百的产品被迫中断，完全不符合比例原则。
  - 所以，这场版权官司就是一家利益至上的公司，以微不足道的理由，为了一个自己根本不在乎的产品，悍然发动一场损人不利己的战争。
- 更為自由的開放源碼作業系統
  - [https://www.openfoundry.org/tw/opensource-history/1891](https://www.openfoundry.org/tw/opensource-history/1891)
  - 由於 Unix 中包含原始碼，使得研究機構可以修改並擴充 Unix，加州大學柏克萊分校的研究生 Bill Joy 就以此方式於 1977 年延伸出 BSD（Berkeley Software Distribution），BSD 一開始僅是 Unix 的外掛，並非完整的作業系統，一直要到了1983 年的 2.9 BSD 才首次作為一個完整的作業系統釋出。1991 年，BSD Networking Release 2 釋出，除去多數 AT&T Unix 的原始碼，成為 386BSD 和 BSD/386 的前身，此一主張同時主張其使用者不需再取得 AT&T 授權。這使得 AT&T 所屬的 Unix System Laboratories 向 Berkeley Software Design, Inc. 提起訴訟，造成 Networking Release 2 直到爭議釐清前都無法散布。USL v. BSDi 一案於 1992 年提出，1994 年達成和解，這期間導致 BSD 開發趨緩，使得另一個開放源碼作業系統 Linux 後來居上。
- [Jserv's blog: 不再囉唆：NetBSD 簡化BSD 授權條款](http://blog.linux.org.tw/~jserv/archives/002042.html)
  - 隨著 BSD 的成熟，人們意識到摻雜 AT&T UNIX 的程式碼，意味著高價的授權 (AT&T License) 與使用上的限制，沒辦法透過當時開始發展的網路 (Ethernet) 作廣泛的散播，是此，在許多貢獻者的投入下，1989 年六月，Networking Release 1 (Net/1) 誕生了，不需 AT&T 授權也使用，當時一個劃時代的變革就是將上述四個條款的 BSD 授權聲明含入，只要在這個新的遊戲規則下，都可自由再發佈。而我們也可從這原始的四項被授權人的條件限制中，看出對於原始程式與二進位執行檔的散播形式 (需保有授權與免責聲明)、於程式本體提及 Net/1 研發背後的加州大學、禁止以貢獻者或加州大學之名，行衍生軟體之背書、推廣、促銷等行為，意思就是為這嶄新的系統，制定得以自由使用的規則。而到了 1991 年六月，Net/2 已幾近全新的作業系統，不含 AT&T 的程式碼，而 Net/2 在 Intel 80386 硬體架構的移植，由 William Jolitz 負責下進行，也被稱為 386BSD，後來，由握有 System V 版權、Unix 商標的 UNIX Systems Laboratories (USL，為 AT&T 附屬子公司) 對 Net/2 在 80386 硬體的封閉專屬 BSD/OS 背後研發的 Berkeley Software Design (BSDi) 公司，提出法律訴訟，延宕了多年，直到 1994 年一月份才落幕，並引來 BSD 原始程式碼重整的動作，顯然，對系出同門的 386BSD 來說，不免也受到影響，而無法在法律爭端休止前，作自由的開發與使用。
- UNIX的歷史沿革
  - [http://content.sp.npu.edu.tw/teacher/kkhuang/Shared%20Documents/Linux作業系統/UNIX的歷史沿革.pdf](http://content.sp.npu.edu.tw/teacher/kkhuang/Shared%20Documents/Linux作業系統/UNIX的歷史沿革.pdf)
- FreeBSD TCP/IP stack
- [2015] [A Repository with 44 Years of Unix Evolution](http://www.dmst.aueb.gr/dds/pubs/conf/2015-MSR-Unix-History/html/Spi15c.html)
  - [GitHub] [dspinellis/unix-history-repo](https://github.com/dspinellis/unix-history-repo)
![UNIX branches](http://www.dmst.aueb.gr/dds/pubs/conf/2015-MSR-Unix-History/html/branches.png)

- [2012] [Why Caldera Released Unix: A Brief History](http://www.linuxdevcenter.com/pub/a/linux/2002/02/28/caldera.html)
- [Wikipedia] [Ancient UNIX](http://en.wikipedia.org/wiki/Ancient_UNIX)
- Unix传奇
  - (上篇) [http://coolshell.cn/articles/2322.html](http://coolshell.cn/articles/2322.html)
  - (下篇) [http://coolshell.cn/articles/2324.html](http://coolshell.cn/articles/2324.html)
- [UNIX 相關歷史](https://embedded2015.hackpad.com/UNIX-History-o6ganUMGhbm)
  - 歡迎一起考古！ --jserv


旁徵博引

- [https://en.wikipedia.org/wiki/SCO%E2%80%93Linux_controversies](https://en.wikipedia.org/wiki/SCO%E2%80%93Linux_controversies) Linux 的官司





See Also:

- Linux Foundation, OIN


TODO:

- 將參考資料分類並分工研讀
- ~~填寫分工表~~
- ~~研讀誠夏老師提供的簡報(開源軟體法律訴訟案例)~~
- 訴訟、商業化、授權條款之間的關係
- 探討這場官司對於現在的影響
- BSDi 導火線


5/18 報告後 TODO:

- AT&T 公司介紹，後來為何被拆成好幾個子公司等補充介紹
- 整場訴訟的前情提要、為什麼要打官司、官司內容、最後結果與影響
