Title: Cat System Workshop #11 Dynamically Hacking the Kernel with Containers  
Slug: cat-system-workshop-11-dynamically-hacking-the-kernel-with-containers  
Date: 2016-09-21 03:50:25  
Authors: fkz  
Category: Conf/Meetup  
Tags: Kernel, Containers, Cat System Workshop, Meetup  
Summary: Note for Cat System Workshop #11 (2016/09/20)  
  
  
## Info  
  
+ 活動網址：<http://www.accupass.com/go/cat0920>  
+ Spaker: 高魁良  
+ Slides:[Talk 160920 @ Cat System Workshop](http://www.slideshare.net/QueyLiangKao/talk-160920-cat-system-workshop-66199432)  
    + 講者在 ContainerCon Japan 2016 的投影片： [Dynamically Hacking the Kernel with Containers - ContainerCon Japan 2016 Tokyo - Quey-Liang Kao - National Tsing Hua University, Taiwan](http://events.linuxfoundation.org/sites/events/files/slides/talk_7.pdf)  
  
---  
  
# Note  
  
+ 稍微提到了一下 Live Kernel Patching  
+ Kernel Detouring  
    + 有點類似 Rootkit 的感覺  
+ Intel 也有在開發 Container，叫作 Clear Container，最近公佈了 2.0 版。  
    + <https://clearlinux.org/clear-containers>  
  
---  
  
+ 可以在 Linux 的機器上跑 FreeBSD 的 container，透過換掉 System call 的 table 來達成。  
+ Specific Challengs (FreeBSD)  
    + Corresponding system calls  
        + Flag numbers are not portable  
        + Different calling/exiting conventions  
    + Unique system calls  
        + Re-implementation  
+ General Challenges  
    + Insufficient isolation  
    + Limitation of development  
        + live patching should only be a temporary solution.  
+ Other Binary Compatibility Work  
    + Wine  
        + Special loader for PEs/DLLs  
    + FreeBSD, Windows 10  
        + Kernel built-in compatibility layer for Linux binary.  
            + FreeBSD i386  
            + Windows 10: Ubuntu on Windows 10 也是用類似的方法  
        + System call remapping/re-implementation  
  
---  
  
## How  
  
### Step 0: Setup  
  
+ Environment (x86\_64 maching)  
    + Linux 4.6.2  
    + FreeBSD 10.2  
+ Tools  
    + kpatch: A tool for kernel livepatch  
    + docker  
  
### Step 1: From LivePatching to Detouring  
  
```  
kernel/livepatch/core.c.orig:klp_ftrace_handler  
  
klp_arch_set_pc(regs, (unsigned long)func->new_func);  
```  
  
+ 目前 LivePatching 最成熟的還是在 x86 的 machine 上  
  
  
#### Ftrace in LivePatching  
  
在 kernel 的 config 中要 enable `ftrace` 和 `fentry`  
可以透過 ftrace 去抓到每個 function 被 call 的時間點。  
  
  
#### Ftrace in Detouring  
  
  
### Step 2: Detour-able Entry Point  
  
+ Assembly file is NOT detour-able  
    + 順便一提，也不支持 in-line function  
  
  
### Step 3: Detoured Entry Point  
  
+ maintain 一個 FreeBSD 的 system call table (不是一個 function pointer 的 table)  
+ 達到 remapping syscall 的效果  
+ 目前是用苦功寫死一個一個對應  
    + `cat maps | wc -l` 有 149 個可以互相對應的  
    + `cat syscall.h | wc -l` 468 FreeBSD 的 syscall  
    + `cat unistd_64.h | wc -l` 332 Linux 的 syscall  
  
---  
  
## The workflow  
  
1. Launch a normal container  
2. Run a init script  
    + which enables the specific detour modules  
3. A FreeBSD environment in the container  
4. On exit  
    + disable detour modules  
  
---  
  
## Demo  
  
+ [truss (Unix) - Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Truss_(Unix))  
+ Linux 跟 FreeBSD 的 `execve` 剛好是同個號碼  
  
---  
  
## 總結  
  
+ The kernel detouring demo attempts to indicate a possible movement of the development of OS containers  
    + as a proof-of-concept  
    + kpatch as a temporary solution  
+ Future direction  
    + Make more fun  
  
---  
  
## 一些討論  
  
+ 自己寫一個 ftrace handler 改掉 detour 的 destination 可能會是比較好的作法。  
+ 講者在日本的 ContainerCon 給 talk 的時候有人給了 `execution domain` 這個關鍵字。  
    + Linux 在 2015 前有個東西叫作，[execution domain](https://linux.die.net/man/2/personality)  
        + BSD 的部份是沒有實作的。(no effects.)  
+ 這邊只有針對 syscall 的 entry point 去改,沒有要 hook 到多深，也許會覺得用 ftrace 太 powerful，何不改寫 ptrace 就好。或是直接使用 user space Linux 等等。  
+ [Linux® emulation in FreeBSD](https://www.freebsd.org/doc/en_US.ISO8859-1/articles/linux-emulation/article.html)  
> 想當初修 SA 的時候 flash player 在 FreeBSD 上編不起來好像就是用這招。  
  
---  
  
## 幕後花絮  
  
+ How to implement the `is_freebsd_container()` function?  
+ How was the ContainerCon Japan?  
    + 跟當地的社群互動滿有趣的  
    + 會議室比較高級、沒有 host、會幫你準備好投影機、白板。  
    + 講者：「我覺得可以考慮不要去。」 （眾：XDDDD）  
        + 「裏面有一半以上的講者是日本人，腔調不是問題，主要是單位時間內的資訊密度，很多講者為了把發音腔調正確會講得很慢。」  
            + jserv: 「日本砸了很多錢在這上面，所以有一半以上的講者是日本人很正常的。」  
        + 「然後很多講者的問答時間都沒有人理。」  
            + jserv: 「他們可能都已經在公司聽過同事講過完整的日文版了，只是來這邊聽比較沒那麼完整的英文版。」  
        + 「日本人用 Twitter 用很兇，有位老老的日本人在我演講完後問了很多的問題，然後問我有沒有用 Twitter，把我加到了一個討論 Container 的 Group 裏面。我才發現他在聽我演講的時候發了很多推，然後這些推底下都有他的推友在討論，有提到 Execution domain，也有說我的某頁簡報毫無意義的評論，於是我用我沒那麼好的日文跟他們來來回回得回覆，但不知道是不是我的日文用字拿捏的不好，隔天我發現他們全都取消追蹤我而且還把我踢出那個討論 container 的 group。」  
            + xatier：「一定是沒跟他們喝酒的關係，日本人都是喝了酒馬上就熟了。」  
        + 「有位中國人看到我投影片的第一頁，就跑過來問我說：『你清華的啊？』『嗯，但我是臺灣的清華』然後他就當著我的面拿著他的東西走出去了。」  
            + jserv：「你下次遇到這種就要直接跟他講英文，他跟你用中文你還是一直跟他說英文，不然像你這樣整個就弱掉了。」  
+ 覺得 jserv 後來跟講者講的一些東西也頗值得紀錄一下的：  
    + 「你去了 Linux Foundation 辦的 Conference 一趟應該就知道當講者的不是超級大的公司就是超級小的公司，像你這種只有學生身份的是非常少的。」「對啊，有位和我討論的德國人也有聊到，他直接就說他覺得是主辦單位找不到足夠的講者才找我。」「也好啦，至少是一次出去看看的經驗。」  
    + 「看到滿多人說我的演講跟他們預期的有落差。」「你這次去就知道他們都是業界的工程師，你的摘要就輸人家了，人家 Twitter 是講幾萬台伺服器的佈署、Facebook 是講二十億使用者的資料分析」「對啊，我講的東西根本沒有 scale。」「他們很多人是公司出錢讓他們來的，最便宜的門票一張也要五百多鎂，你講的東西太空洞讓他們沒辦法寫報告的話，交不出報告就會被主管罵。」  
    + 「你的題目是還不錯，開始演講時的高度是在這，但你講完以後高度只有上升一點點。」「程式碼的部份放的太少算是我的失策。」「你的簡報太早做完了，你應該在聽完第一場 keynote 的時候就會知道日本這邊大概喜歡怎麼樣的簡報，你就要在這個時候開始修改你的簡報。」「哦對，日本人好像超級喜歡格言，看到有一個 keynote 講者，一開始的十張投影片全部都是格言然後搭配文青風格的照片背景，滿受大家歡迎的。」  
    + 「你這個演講就是缺乏應用的部份，因為參加的都是真的在業界的工程師，所以他們會希望看到你講的東西解決了什麼問題，如果沒有這部份的話，只會讓他們覺得『靠，又是一個窮學生來這邊講論文。』我覺得你這個可以考慮弄個 IDS，因為 syscall 都是抽換掉的，所以不用怕，甚至可以重現一堆 CVE，來分析攻擊者的行為。」「對耶，滿多人後來反應演講跟預期有落差的時候，我就有聽到我後面的人在用日語說『原來是學生而且還是做 High Performance Computing 又不是研究 Container 的，難怪』之類的。」「下次你就要問問看有沒有公司願意讓你掛名，你就可以放在投影片上，這樣就比較不會被這些業界的工程師看不起，你的英文表達能力基本上已經超過他們一半在場的日本工程師啦。」  
    + 「演講就是要安排暗樁啊，不然聽眾很容易聽到睡著的。像你的演講是第三天的上午，前面兩天就要儘量去認識人，然後跟他們稍微賣點關子，請他們來聽你的演講。」  
    + 「Linux Foundation 對於演講順序的安排是有根據的，不只是演講的內容，也會去查一下這個講者的影響力還有做了哪些事情，評價愈高的當然就是 keynote spearker。」  
