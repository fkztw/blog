Title: PyCon TW 2017  
Slug: pycon-tw-2017  
Date: 2017-06-09 17:51:37  
Authors: fkz  
Category: Conf/Meetup  
Tags: Python, PyCon, PyCon TW  
Summary: Note for PyCon TW 2017 (2017/06/09 ~ 2017/06/11)  
  
  
Website: <https://tw.pycon.org/2017/en-us/>  
Portal: <https://tw.pycon.org/2017/en-us/portal/>  
Chat: <https://gitter.im/pycontw/2017>  
Collaborative Notes: <https://hackfoldr.org/pycontw2017/>  
Quiz Bot: <https://pycontw2017-quizbot.herokuapp.com/>  
  
  
---  
  
# Day 1 (2017/06/09)  
  
## Keynote: Choices for Smarter AI  
  
Speaker: 林軒田  
  
有點像是在大學上第 1 堂 AI 概論的感覺，  
前面 30 分鐘基本上沒有啥重點 XD。  
  
後面 30 分鐘開始講開始接觸 AI 會面臨哪些 Choices  
  
+ Motivation vs Feasibility  
    + Motivation  
        + something publishable? (maybe just for academia)  
        + something profitable?  
    + Feasibility  
        + Modeling  
        + Timeline  
        + Budget  
+ Big AI problems comes from Big Data  
    + generate from motivation  
        + variety: dream more in big data age  
        + velocity: evolving data, evolving problem  
    + generate from feasibility  
        + volume: computational bottleneck  
        + veracity: modeling with non-textbook data  
            + 資料的 noise 會比教科書上多很多  
    + tip  
        + often needing "choose and learn" towards good problems  
+ Human vs Machine-er Route  
    + Human  
    + Machine  
        + objective criterion  
        + use computing power  
        + continuous improvement  
+ How to measure AI goal  
    + "Computers are useless, they can only give you answers."  
    + Spec for Program  
        + tip: always start with reasonable, measurable & priortized goals for AI.  
+ What Data to (or not to) Use?  
    + Bring Your Own Bottle  
    + Design Your ...  
    + Choice factors for Data  
        + Utility  
        + Necessity  
        + Quality  
        + Cost  
        + tip: garbages (data) in, garbages (AI) out. Choose your data.  
    + More Data Construction  
        + 不用一開始就要 AI 做事情，最好先用自己的腦袋先做一些 Data Analysis，再讓 AI 幫你完成這些事  
+ What Model to Start?  
    + myth: 即便有大量的資料也不該從最複雜的模型開始  
    + Linear (Simpler) Model First  
        + Keep It Simple and Stupid  
+ What Improvements to take  
    + Overfitting  
        + 控制模型的複雜度、做些資料的清理與選擇，讓你的模型可以維持在能夠運作的程度  
    + Misfitting  
        + 要 AI 做的好，要確定它在學習的東西是跟你最後的目標有關係  
    + Over-reusing  
        + "If you torture the data long enough, it will confess"  
        + 當你過度重複處理你的資料，到最後的結果可能是會被汙染的，所以要儘量避免掉這件事。  
+ How to Verify and Deploy?  
    + Code Deployment Workflow  
        + Development => Staging => Production  
    + AI Deployment Workflow  
        + Offline => Online => Production  
            + Offline  
                + 在這個階段常常會跟 Online 的部份有 Misfitting 的問題，所以通常只是做正確的驗證  
            + Online  
                + 這時候的 criterion 會跟你的目標比較接近  
                + 要謹慎選擇跟誰比較，跟太爛的比會太過樂觀，跟太好的比可能會過度調整而產生 Overfitting。  
                + Human trust 會比你原本的目標來的重要，因為一個能用的 AI 是需要取的人的信任的，就算你達到目標，如果結果跑出來讓人不滿意的話，一樣達不到效果。要讓人能夠接受這個結果，才能夠發揮這個 AI 的價值。  
    + 跟你的選擇一起學習，時時刻刻要把限制考慮進去，這樣才能夠做出比較好的決策。  
    + 在訓練 AI 的時候，就像訓練神奇寶貝一樣，會遇到非常多的選擇，而這些選擇也都真的會影響到你訓練出來的 AI 的好壞  
+ Q&A  
    + 剛剛演講的內容涉及到 Data Engineer 和 Data Scientist 的部份，想請問這兩者的區別？  
        + > 硬要區分的話，Data Scientist 比較偏向設計，而 Data Engineer 比較偏向實作與驗證。但我自己是傾向不去區分，因為最終會需要的能力是跨領域的，所以都要瞭解才是比較好的  
    + 剛剛提到訓練出來的 AI 要取得人的信任，但這個常常會牽涉到客戶的利益，這該怎麼處理？  
        + 要確認彼此的期待是合理的  
  
## Python 開源軟體考古 - 以 Viper 為例  
  
+ Speaker: [陳坤裕 KunYu Chen](https://github.com/18z)  
+ GitHub repo of this talk: <https://github.com/18z/viper-research>  
+ Viper: <https://github.com/viper-framework/viper>  
+ Collaborative Note: <https://hackmd.io/s/H1yP4MQye#1050-1120-talk-python-開源軟體考古-以-viper-為例>  
  
覺得這場講的東西挺不錯的，  
都算是講者自己整理出來的心得，  
介紹了一些可以使用的工具，  
也講了他是怎麼去 trace 以及觀察了哪些東西，  
不失為一個拿來 trace open source project 的方法，  
可能可以幫助自己更容易對於 open source contirbute 做貢獻。  
  
可以產生 dependency graph 的工具：<http://furius.ca/snakefood/>  
  
  
## TenslorFlow Wide & Deep Data Classification the Easy Way  
  
Speaker: Yufeng Guo @yufengG  
Slides: <https://www.slideshare.net/YufengGuo4/pycon-tw-tensorflow-wide-deep-data-classification-the-easy-way>  
Code: <https://github.com/amygdala/tensorflow-workshop/tree/master/workshop_sections/wide_n_deep>  
  
  
## Keynote: The State of Python for Education  
  
+ Speaker: Carol Willing  
+ Collaborative Note: <https://hackfoldr.org/pycontw2017/https%253A%252F%252Fhackmd.io%252Fs%252FHk-NVGXke>  
  
for Education => X  
for Learning => O  
<https://github.com/jakevdp/WhirlwindTourOfPython>  
  
+ Learning with Python  
    + [JupyterNotebook](https://github.com/jupyter/notebook)  
    + [JupyterLab](https://github.com/jupyterlab/jupyterlab)  
    + [pyvideo](http://pyvideo.org/)  
+ Creating opportunities  
+ Scaling Globally  
+ Call to Action  
    + Join PSF and Python in Education  
    + Participate in a sprint  
    + Give a talk or write a post  
    + Offer a workshop  
    + Contribute to a favorite project  
        + Open an issue  
        + Fix typo  
        + Send pull request  
    + Share your creations  
  
  
## Building Microservices in Python 個案分享  
  
+ Speaker: Jonas Cheng  
+ Slides: <https://www.slideshare.net/jonascheng3/building-microservices-in-python-pycon2017>  
+ Collaborative Note: <https://hackmd.io/OwQwDCBMYEaQtADgJwBYT1WSj7IIwDMh8ApgCYCskyklMyi5qQA=?both#1455-1540-talk-building-microservices-in-python-個案分享>  
  
Soocii 是趨勢科技為了弄手機群聊而獨立出來的子公司  
  
跨服務間的溝通最好是一個 transaction 就結束，  
如果要額外呼叫其他的服務的話，  
最好採用 async 的方式，  
避免因為時間太長而被 timeout、影響 UX。  
  
  
## Python Module in Rust  
  
+ Speaker: 許邱翔 (dv)  
+ Slides: <https://docs.google.com/presentation/d/1mTw-4buKDTqPNzJS03s2I0apBMal-SaeKk1dHDSE6fk/pub?start=false&loop=false&delayms=3000&slide=id.g22c75fc6c3_0_6>  
+ Rust 的生態系  
    + 特性  
        + Memory safety without GC  
        + Compiled language  
        + Strong, static type  
        + 效能與 C / C++ 接近  
    + Tools  
        + Crates (Like PyPI in Python)  
        + Cargo (Like pip + setuptools)  
            + <http://doc.crates.io/>  
        + rustup (like pyenv)  
            + <https://www.rustup.rs/>  
        + RFCs (like PEP)  
            + <https://github.com/rust-lang/rfcs>  
+ How can Python play with binary  
    + ctypes  
    + CFFI  
        + PyPy 團隊的實作  
    + CPython Extension  
        + CPython 官方實作  
+ How can Python play with Python  
    + <https://github.com/dgrunwald/rust-cpython>  
    + <https://github.com/PyO3/setuptools-rust>  
  
---  
  
# Day 2 (2017/06/10)  
  
## Stochastic Prediction Model, Case of the Dengue outbreak at Tainan, 2015  
  
使用 Jupyter Notebook 利用資料分析與視覺化的方式，  
來分析 2015 年台南登革熱爆發的狀況，  
並將這些處理完後的資料拿來建立模型，  
用於之後的預測。  
  
---  
  
## Submit your first CPython patch (and don't worry about C)  
  
+ Speaker: [Louie Lu](https://louie.lu)  
+ Slides: <https://goo.gl/4oC2Dg>  
  
+ Intro  
    + Status of CPython Branches  
    + History of CPython workflow  
        + ~2006: SourceForge (repo & issue tracker)  
        + 2006 ~ 2011: svn.python.org & bugs.python.org  
        + 2011 ~ 2016: hg.python.org  
        + July 2014: PEP-474 by Nick Coghlan (propose moving to Kallithea)  
        + Nov 2014: PEP-481  
        + Sep 2015: PEP-507  
+ Basic  
    + GitHub  
    + Git  
        + `git remote -v`  
    + CPython Coding Style  
        + PEP7  
        + PEP8 - CPython C Coding Style  
            + 比較特殊一點  
            + 4 spaces, 79 chars per line  
    + Sphinx document style  
        + reStructuredText  
            + Use 3 spaces, no tabs  
            + Hyperlinks  
                + `Link text <http://example.com/>`_  
            + Blocks  
                +  `.. note::`  
    +  Layout  
        + module, stdlib  
            + `Lib/<module>.py`  
        + extension-only module  
        + builtin types  
            + `Objects/<builtin>object.c`  
        + builtin functions  
            + `Python/bltinmodule.c`  
        + Exception!  
            + `int` is at `Objects/longobject.c`  
+ Contribute  
    + How  
        + Read, communicate, think  
            + devguide  
            + mailing lists  
                + Python-dev  
                + Python-ideas  
            + [bpo](https://bugs.python.org)  
            + IRC  
                + freenode #python-dev  
            + lwn.net  
                + <https://mail.python.org/pipermail/python-dev/2017-June>  
    + Where  
        + to find a bug?  
            + <http://bugs.python.org>  
            + source code  
                + `XXX`  
                + `TODO`  
            + mailing list  
            + stackoverflow  
            + bpo-mergerate:  
                + <https://bpo-mergerate.louie.lu>  
        + what can I do?  
            + Writing documentation  
            + Helping test patches  
                + 因為量很多通常核心貢獻者可能要幾個月後才有空測試，所以可以幫忙測試，然後給意見  
            + Review PR from others  
            + Increase test coverage  
            + Add comment to exists code  
                + 可以幫忙把程式碼加上註解，讓其他人比較容易瞭解  
        + Misc.  
            + IDLE  
            + devguide issues  
                + 有很多前人回報的問題，或者自己看到有問題也可以嘗試修改並 submit PR  
            + easy issues  
                + <http://bugs.python.org/issue?status=1&@sort=-activity&@columns=id,activity,title,creator,status&@dispname=Easy%20issues&@startwith=0&@group=priority&keywords=6&@action=search&@filter=&@pagesize=50>  
+ Live contribution  
    + `from ctypes import *`  
    + Bug 被人搶先修掉了，只好修文件 XD  
  
> 講者表示有興趣的人可以參加第三天的 Unconference，會再更詳細的教學怎麼 contribute code 到 CPython  
  
  
## Global Interpreter Lock: Episode III - cat < /dev/zero > GIL;  
  
- Slide: https://www.slideshare.net/penvirus/global-interpreter-lock-episode-iii-cat-lt-devzero-gil  
- Speaker: Tzung-Bi Shih  
  
+ 前情提要  
    + 一部曲：<https://www.slideshare.net/penvirus/global-interpreter-lock-episode-i-break-the-seal>  
    + 想瞭解 GIL 的人可以去看這個講者相關的 talk  
        + https://www.youtube.com/watch?v=MCs5OvhV9S4  
+ Introduction  
    + GIL prevents us (innocently) from utilizing full power of multiprocessors  
        + > 我比較常舉的例子是紅綠燈，一定要綠燈才可以走。如果今天有人不管號誌直接硬走，就有可能發生碰撞，GIL 就像是這樣的一個例子，但討厭的是他是 Global 的，所以很煩人。例如今天這個會場，我現在拿著麥克風在講話，現在後面的朋友想跟他旁邊的人講話，他得大費周章得跑來前面，拿我的麥克風才能講話，這樣大家不會覺得很沒效率嗎？  
  
  
NOTE: [深入 GIL: 如何寫出快速且 thread-safe 的 Python – Grok the GIL: How to write fast and thread-safe Python](https://blog.louie.lu/2017/05/19/深入-gil-如何寫出快速且-thread-safe-的-python-grok-the-gil-how-to-write-fast-and-thread-safe-python/ )  
  
一句話說清 GIL: 「當有一個執行緒在執行 Python，其他 N 個執行緒都在睡覺或是等待 I/O」  
  
  
+ Motivation  
    + > 大家是不是覺得我到底是多討厭 GIL 導致我要花三集來婊它？並不是的，是我在前公司和同事遇到的問題。  
    + High performance data processing platform  
    + > 大家可能會認為只有寫 Python 的人才要懂 GIL，但其實 Big Lock 是一個 fundamental 的問題。系統發展在初期的時候常常會使用這樣的 lock。所以研究 GIL 並不是只有 Python 特定而已，其實在研究作業系統的時候都會遇到類似的問題，因為最後大多會把這個大 lock 拆分成不同的小 lock  
+ Example  
    + [1a.c](https://github.com/penvirus/gil3/blob/master/1a.c)  
        + Get crashed if we don;t acquire the GIL before using the Python runtime.  
    + [1b.c](https://github.com/penvirus/gil3/blob/master/1b.c)  
        + Our multithreading program has been serialized into one "effective" thread  
        + > 在 Python 的 multithreading 基本上都一定要處理 GIL 的問題，不然只會是「你以為自己有用到但實際上並沒有」  
    + [1c.c](https://github.com/penvirus/gil3/blob/master/1c.c)  
        + warning: the example won't compile successfully.  
        + 嘗試修改，但兩個多小時之後沒成功就放棄了，改用其他方法  
        + Dynamic linker 可能有幫助，朝著讓兩個 task 使用不同的 Python interpreter 的方向去解決  
    + [2a.c](https://github.com/penvirus/gil3/blob/master/2a.c)  
    + [2b.c](https://github.com/penvirus/gil3/blob/master/2b.c), [2c.c](https://github.com/penvirus/gil3/blob/master/2c.c)  
        + 成功了，但結束後得把 .so 檔刪掉。  
        + > 這方法我給 87 分，因為太北七了，找到了 dlmopen 的文件，三天三夜跪在電腦前不能自我，醒來的時候已經是第四天早上  
    + [3a.c](https://github.com/penvirus/gil3/blob/master/3a.c), [3b.c](https://github.com/penvirus/gil3/blob/master/3b.c)  
        + 後續使用 dlmopen 把 global 變數拆成兩份，確實是可以做到。  
    + [4a.c](https://github.com/penvirus/gil3/blob/master/4a.c)  
        + 但把 dlmopen 和 Python 放在一起就是會出事，像是這個例子。  
+ More Complicated Example  
    + 6b.c  
        + configuration task  
+ Discussion  
    + some 3rd-party libraries may not work well  
        + they have been guaranteed to be the only active instance  
    + 64-bits address space is big enough; is put them altogether a good idea?  
        + Similar debates on monolithic and microkernel  
    + > 反正我今天就是來胡說八道的，我可以大膽預測，3~5年內一定會出現相關的第三方應用，可能會完全捨棄安全性而只著重在效能的方面  
  
About removing GIL, reference Larry Hastings The Gilectomy: https://www.youtube.com/watch?v=pLqv11ScGsQ  
  
  
## 土炮股票分析系統  
  
+ Spearker: Victor Gau  
+ Slides: <https://goo.gl/JVLhRh>  
+ GitHub Repo: <https://github.com/victorgau/PyConTW2017>  
  
講者使用 Jupyter Notebook 一步步教學，  
講解如何用 Python 去抓取和分析股票資訊，  
使用到 Pandas, Quandl, Numpy, ffn 等 modules，  
並透過 Jupyter Notebook 做簡單的視覺化。  
還加上了一些基本的投資教學，  
並在開頭的時候講了一些股票投資的小故事。  
  
+ 投資是藝術還是科學？  
    + 與生俱來或可被訓練？  
+ [華爾街傳奇：海龜投資法則](http://www.books.com.tw/products/0010384228)  
    + William Eckhardt vs Richard Dennis  
        + William 相信是與生俱來的  
        + Richard 則相信是可被訓練的  
            + 用好幾台 DOS 去跑分析  
+ 投資 3M's  
    + Mind: 投資心理  
    + Money: 資金管理  
        + Equal weight  
        + 停損、停利  
    + Method: 方法、系統  
        + 今天會談到的部份  
+ 架構圖  
  
```  
          +-------> 股價資料 -----------------+  
          |   |                               |  
抓資料 ---+---+---> 財報資料 ---> 選股策略 ---+---> 進出場策略 ---> 部位規模  
          |   |                      |        |          |             ^  
          +---+---> 公司資料         ˇ        |          ˇ             |  
                                  候選股票 ---+       投資標的 --------+  
                                     ^  
                                     |  
                                   自選股  
  
```  
+ 抓資料  
    + google 一下關鍵字  
        + e.g. "Nasdaq company list"  
    + 使用 Pandas  
    + 使用 [Quandl](https://www.quandl.com/)  
        + 讀歷史股價  
            + 用 Quandl 使用 "Yahoo/TW_${股票代號}"  
            + 要用調整過後的股價去算，不然會有問題。  
+ 選股策略  
    + 計算每天股價的變化  
    + 計算波動率  
        + Standard deviation  
+ 進出場策略  
    + 自己決定  
    + Sharpe Ratio  
        + 不希望大起大落  
    + Maximum Drawdown  
        + 不希望賺錢了之後結果兩個月都沒賺  
        + Maximum Drawdown 短一點就比較不會大起大落  
        + `f.fn()`  
+ DEMO  
    + <https://github.com/victorgau/PyConTW2017>  
  
---  
  
## Deep Learning Based Object Detection (Fast R-CNN) in the Microsoft Cognitive Toolkit  
  
+ Speaker: Herman Wu  
+ link: https://tw.pycon.org/2017/en-us/events/talk/348099433595928706/  
  
+ Cognitive 特性  
    + Python and C++ API  
        + 大部份用 C++ 實作  
        + Low level + high level Python API  
    + Extensibility  
        + User functions and learners in pure Python  
    + Readers  
        + Distributed highly...  
+ Deep Learning Revolutionized Image Recognition  
    + Largetst image datatset - ImageNET  
+ COCO Segmentation Challenge 2016  
    + MSRA won 1st place back-to-back  
+ Semantic Segmentation  
    + Recognizing pixels  
+ First CNTK Example  
    + CNTK Model  
    + MNIST Handwritten Digits (OCR)  
    + Multi-layer perceptron  
        + <https://github.com/Microsoft/CNTK/tree/master/Tutorials>  
        + RELU  
  
  
---  
  
  
# Day 3 (2017/06/11)  
  
  
## [Unconference](https://github.com/pycontw/unconference)  
  
### 用Python拯救地球： 如何找出危險的太陽系天體？  
  
+ JPL Horizon  
    + 可以看到小行星的軌跡  
+ 日本的「昴」望遠鏡  
    + 兩公尺高  
    + CCD 由一百多片 CCD 組成  
+ 真實看到的天文照片不是彩色的  
+ 要找出什麼？  
    + 近地小行星  
    + 小行星  
    + 古柏帶天體  
+ 主要應用工具  
    + Python  
    + scipy - KDTree, array  
    + sklearn - RandomForestClassifier (supervised and unsupervised)  
    + astropy, pyfits, pyephem, matplotlib, multiprocessing, sqlite3  
    + C, C++, MPI, mysql  
+ Super Big Data  
    + 一天將近 0.5 TB 的 raw data  
    + 包含許多恆星、星系、垃圾  
        + 一次曝光資料處理完約有數十萬至數百萬筆資料  
+ Machine Learning  
    + 利用資料庫裡的各種測量參數 (55個） 來判斷每一筆資料是否為真  
    + ML 的應用，比起傳統上的條件篩選有效的多，也被用來測量星系之間的距離（紅移）  
+ 現況  
    + 目前有 15,621 個近地小行星被找到 (大小 1 公尺 ~ 32 公里)，目前都沒有危險  
    + 理論模型推論有將近 100 萬個 > 140 公尺的近地小行星（所以我們才找到約 1%）  
    + 現在正在執行的計劃：LINEAR, NEAT, CSS, NEOWISE, Pan-STARRS, ALTAS  
    + 目前許多大型國際合作計劃都以 Python 為主要的程式語言，並結合 Cython 或 call 外部 script 以提升分析速度，例如：  
        + ALMA - CASA  
        + LSST  
        + > 微軟是主要出資者，所以開這個會議的時候不是微軟的電腦都要收起來，但天文分析基本上都是用 Unix-like 的系統，所以開完會又會拿出來 XDDD  
+ Q&A  
    + 為什麼用 Cython 不用 PyPy，有考慮換成 PyPy 嗎？  
        + 沒有，因為我只是使用者，這邊不是我負責的。  
    + 有可能發生像電影那樣，突然發現有個朝地球高速來襲的小行星嗎？  
        + 有可能，因為距離要到夠近才有辦法偵測到。  
    + 筆直衝過來的小行星只會有一個點，這有辦法偵測到嗎？  
        + 目前這個比較難處理  
    + 真的發現有會造成地球物種大規模毀滅的小行星朝地球衝過來怎麼辦？  
        + 基本上目前想到的方法都不太可行，例如：核彈爆破、派人上去鑽礦等等  
  
  
## CPython code sprint  
  
<https://docs.python.org/devguide/>  
  
  
## 一個軟體工程師在農村的見聞  
  
+ <http://ocf.tw/p/2017/openhackfarm/>  
+ Slides: https://hackmd.io/p/Hyzjn1FGb#/  
  
## 懶得答題？寫個 bot 來幫你刷榜  
+ Slides: https://github.com/aweimeow/PyConTW2017-UnConf-Slide  
+ Code: https://github.com/aweimeow/PyConTW2017-Quiz-Solver  
  
## 初めてのプログラミングならパイザで始めよう☆  
  
+ Online Judge Special Events  
    + https://paiza.jp/logic_summoner  
    + https://paiza.jp/cgc  
    + https://paiza.jp/poh/hatsukoi  
    + https://paiza.jp/poh/ando  
    + https://paiza.jp/moshijo  
  
預訂現場live解一題看看,破除never live demo迷思(?)  
  
hatsukoi 雙馬尾參考答案(Python3)  
```python=  
# coding: utf-8  
# 自分の得意な言語で  
# Let's チャレンジ！！  
s = int(input())  
t = int(input())  
print(''.join(('-', '+')[i+1==t] for i in range(s)))  
```  
