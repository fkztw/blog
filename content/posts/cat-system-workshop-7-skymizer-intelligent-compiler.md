Title: Cat System Workshop #7 Skymizer intelligent compiler  
Slug: cat-system-workshop-7-skymizer-intelligent-compiler  
Date: 2016-06-21 20:44:23  
Authors: fkz  
Category: Conf/Meetup  
Tags: Compiler  
Summary: Note for Cat System Workshop #7  
Modified: 2016-07-05 21:36  
  
  
Event link: <http://skymizer.kktix.cc/events/cat0621>  
  
> Q: iPhone 為什麼兩顆 core?  
> A: 人類寫出來的程式碼平行度平均約 1.8，所以兩顆就夠了。  
  
  
### CPU 效能  
  
+ 2004 年以前，每年改善 50%  
+ 2004 年之後，每年改善 21%  
+ 原因  
    + 電子漂移  
    + Power wall - faster computers get really hot  
    + Memory wall - memory bandwidth becomes one of the bottlenecks  
    + ILP wall - exploit performance from parallelism is diffifult  
        + 指令集的平行度已經遇到瓶頸  
+ 這 3 個問題都在 2004 年發生，所以突然驟降。  
+ 什麼時候會掉到 0 %?  
    + 半年前已經達到了。從半年前開始，CPU 效能已經沒有提升了。  
    + 大家都不敢講，怕產品銷售受影響。  
    + 現在只要有改善效能就贏其他人了  
  
---  
  
### 製程  
+ 明年 Q1 達到 10 nm, 7 nm  
  
---  
  
### The Best way to speed up Computer  
  
+ Manual  
+ Compiler  
+ (...)  
+ (...)  
  
---  
  
### Improvement  
  
+ 中國 H 社去年改善 150%，用飛的。  
  
---  
  
### Skymizer Cloud Compiler  
  
+ Cloud compiler is a kind of **iterative compiler**  
  
---  
  
### Challenges of Iterative Compilers  
  
+ Very long compilation time  
    + GCC has ~250 optimization flags  
        + ~200 machine independent flags  
        + ~50 machine-level optimization  
    + There are at least 10^60 combination of flags  
+ High cost of scripting  
    + A compilation unit needs at least four actions to keep the iteration smooth  
        + run.sh, kill.sh, clean.sh, build.sh  
        + Users need to tell iterative compiler at least how to run the program  
    + A system, take WebKit for example, may have ~25,000 compilation units  
    + Different systems have very different building systems  
+ Precise performance data  
    + An optimization phase has only ~3% impact to performance  
    + Application variance of performance are usually about 8%~20%  
    + Iterative compilers need precise performance data to ensure analyzed results  
    + 準確率很重要，如果收集了一大堆資料但準確率很差的話，只是 garbage in garbege out.  
+ Unstable optimization results  
    + Optimizing compilers don't guarantee performance imporvement  
+ Unstable compilers  
    + GCC  
        + GCC in average produces on incorrect results in 10,000 iterations  
        + GCC in average gets a segmentation fault every 100,000 compilation  
    + LLVM  
        + LLVM in average produces one incorrect results in 1000 iterations  
        + LLVM in average gets a segmentation fault every 3 compilation  
        + 所以 LLVM 在 iterative compiler 是不堪用的  
    + 重新 compile 也不會過的錯誤，Compiler 本身的 bug，極為難抓。  
  
---  
  
### Iterative compiler before ten years  
  
+ Since 1994. Most researches appear since 2001.  
+ 24 distinguished works. Only seven works have significant contribution.  
+ 很多論文都只是看到後你知道「喔，這個人畢業了。」的等級  
  
### 2001~2004 Expert System in iterative compilers  
  
+ Dr. Options and OSE represent this era.  
+ Expert system shortens compilation time.  
+ Dr.Options, expert system, TI and HP  
+ OSE, pruning by key insights and performance emulators, Princeton.  
  
### ACME - we have more exploration space than you can imagine  
  
+ Optimization phases can interchange their order.  
+ Sequence increases the exploration space from 10^60 to 250^250  
+ Although ACME success to eliminate exploraiton space, but we can not use it in practice.  
    + GCC re-call phases to simulate order change  
    + LLVM can not reorder any phases  
  
### Subtraction is more important then Exploration  
  
+ 如果一開始就不要嘗試這麼多 optimization，或許可以比較容易找到更有效的方式。  
+ PEAK - eliminate space by identifying harmful optimizations  
    + 先找壞的，把他們刪掉。  
    + Batch elimination  
    + Iterative elimination  
+ VISTA - eliminate space by pruning dormant phases  
    + 先找好的  
    + 把真正常用的、有效的挑出來，這些彼此之間衝突的做分群，然後再去嘗試  
  
### Social Network can help!  
  
+ cTuning  
+ 工人智慧  
+ [MILEPOST GCC](http://ctuning.org/wiki/index.php/CTools:MilepostGCC)  
    + <https://en.wikipedia.org/wiki/MILEPOST_GCC>  
+ Collective TUNING  
    + 每個人都用他的 compiler，他就會偷偷把你的 source code 送回去他的 server，然後再去用 AI 分析該 source code 可不可以做更好的 optimization，藉此收集很多的資料來作為優化的依據。  
    > xatier: 這不是跟微軟最近在 VS 的 profiler 塞了一個 entrypoint 是一樣的事情嗎？ XD  
+ 集眾人之力的群眾 Compile  
+ 在 4 年前就沒在動了  
  
### Skymizer Intelligent Compiler  
  
+ Sky Gold  
    + Testing Framework  
    + Result Repository  
        + Fast build (from hours to seconds)  
+ Sky Knight  
    + Distributed compilation  
    + 之後考慮改成用 p2p 的模式，下班電腦開著就可以加入 distributed compilation 的一部份。  
+ Sky Dragon  
    + Software Hypervisor Precise OS  
    + CPU 要跟客戶的一樣才有辦法  
+ Sky Wizard  
    + Fast exploration  
        + Guide optimization direction  
    + 只要拿到 characteristics，不會拿到客戶的 source code，所以客戶能夠接受。  
  
+ 把使用者 compiler 偷偷換掉  
+ 把使用者 compile 的過程都紀錄下來  
+ 找到最好的 object file (`*.o`) 之後，check-in 回去給 user，user 只會覺得之後愈用愈快>  
+ 優點  
    + user 實際上 99.9% 的 code 不會動，所以會一直穩定得嘗試 compile 出更快的 object file，再回傳給 user  
+ 目前遇到客戶反應的問題  
    + 回傳回去的 object file 沒有做版本控制，導致無法客戶拿某個時期的 object file 來做測試。  
  
---  
  
### Q&A  
  
+ 有支援 [Profile-guided optimization](https://en.wikipedia.org/wiki/Profile-guided_optimization) 嗎？  
    + 目前沒有支援  
+ 為什麼剛剛說 opentuner 是來亂的？  
    + [opentuner](http://opentuner.org/) 沒有解決任何問題，只是提供一個優雅的方式來把 run, kill, clean, build scirpts。  
+ 客戶使用你們的 compiler 不會造成 debug 很困難嗎？  
    + 會，這也是我們目前被罵的地方。  
+ 你們收費怎麼算？  
    + 很貴，因為我們的客戶幾乎都是大公司，但因為很貴，所以也很難談。  
