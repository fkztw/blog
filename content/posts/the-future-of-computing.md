Title: 《代碼的未來》  
Date: 2014-03-10 21:37  
Author: fkz  
Category: Reading  
Tags: Review, NoSQL, Big Data, RDBMS  
Slug: the-future-of-computing  
Modified: 2015-10-26 12:08  
Summary: 《代碼的未來》讀後感與筆記  
  
  
### The Future of Computing by Matz  
  
本書作者為 Ruby 之父松本行弘(Matz)  
  
中譯本連結：[博客來-圖靈程序設計叢書：代碼的未來](http://www.books.com.tw/products/CN11004414)  
  
這本書裡面介紹了很多我都不知道的東西  
  
書的撰寫時間點是 2013 年 4 月左右  
  
有些書裡面描述的東西（我沒聽過的）在當時已經出現了一兩年  
  
而通常會寫成書的東西都已經舊了  
  
顯示我知道的東西實在還是太少  
  
因為快唸完了才覺得應該要筆記起來  
  
所以是從第五章開始（本書一共六章）  
  
推薦買來看看（雖然我是跟朋友借的）  
  
不過建議不喜歡 Ruby 的人不要買  
  
因為裡面很多例子都是用 Ruby 來舉例（畢竟作者是 Ruby 的發明人）  
  
不過其實如果真的很討厭 Ruby 的話  
  
把用 Ruby 舉例的部分跳過還是有很多東西值得看的  
  
<!--more-->  
  
Ch5. 支持 Big Data 的儲存技術  
===  
  
+ CAP 原理：在大規模的環境中，以下三種特性只能同時滿足其中兩個。  
    + Consistency（一致性）  
    + Availability（可用性）  
    + Partition Tolerance（分裂容忍性）  
    + 其中 Availability 是不能捨棄的，而在分散式計算的環境中，Partition Tolerance 其實也是不能捨棄的，所以唯一能捨棄的就只有 Consistency ，因此也造就了之後的 NoSQL 。  
+ Relational Database 的特性：ACID，比較重視保持嚴格的一致性。  
    + Atomicity：對於數據的操作只允許“全部完成”或“完全未作改變”  
    + Consistency：DB 的狀態必須永遠滿足給定的條件，當某操作無法滿足執行條件時就會被取消  
    + Isolation：不能被其他操作干涉以及避免對其它操作造成影響  
    + Durability：操作完成時，其結果會被保存且不會遺失  
+ NoSQL 的特性：BASE，比較重視可用性，沒那麼重視一致性，只要最終能夠達成目標即可。  
    + Basically Available：比較重視可用性  
    + Soft-state：不追求狀態的嚴密性  
    + Eventually consistent：最終達到一致性即可  
+ NoSQL  
    + Key-Value DB  
        + Example  
            + memcached  
            + memcachedb  
            + ROMA  
            + Flare  
            + kumofs (written in C++)  
            + Redis (written in C)  
            + TokyoTyrant  
    + [Document-Oriented DB](http://en.wikipedia.org/wiki/Document-oriented_database)  
        + Feature  
            + Value 儲存的部分不是單純的 String 或 Number，而是擁有結構的 Document  
            + 不需要 DB Schema  
        + Example  
            + XML(eXtended Markup Language)  
            + JSON(JavaScript Object Notation)  
            + CouchDB  
                + RESTful(REST: Representational State Transfer)  
                + Erlang  
                + JSON  
                + 無法實現 RDB 中的 Join  
            + MongoDB  
                + Combining the best features of document databases, key-value stores, and RDBMSes.  
                + 提供多語言的 API  
    + Object-Oriented DB  
        + Feature  
            + 將 OO 語言中的 Object 直接進行永久地保存，就算電腦關機後也不會消失，除存在硬碟中  
        + Example  
            + Db4o  
            + ZopeDB  
            + ObjectStore  
  
+ MongoDB  
    + born in 2009.  
    + mongod  
        + `$ sudo mongod --dbpath /var/db/mongo` use /var/db/mongo to store db files  
    + mongo command  
        + `$ mongo` for using mongo shell  
        + `$ rlwrap mongo` 為 mongo command 增加行編輯的功能  
        + `> use $db` swicth to $db (if not exists, mongo will create a new one)  
        + `> db.$collection_name.save($JSON)` insert  
        + `> db.$collection_name.find($JSON)` find in $JSON  
        + `> db.bench.ensureIndex({j:1}, {unique: ture})` create index for j  
    + 沒有固定的 DB Schema  
    + 儲存結構  
        + Database  
        + Collection  
        + Document  
    + Use JavaScript  
    + Support **Atomic operation & optimistic concurrency control**  
    + Support Distributed Environment  
    + Compare with SQL  
  
```MySQL  
SELECT * FROM bench WHERE x = 4  
```  
in MySQL  
  
and  
  
```JavaScript  
db.bench.find({x: 4})  
```  
in MongoDB  
  
are equal.  
  
+ Leaky abstraction  
    + 當 object 的調用越來越頻繁和複雜時，產生性能上的問題，導致 RDM 中的 Record 並沒有真的成為  object，在特殊的情況下，會暴露出抽象化的紕漏。  
+ OD Mapper (Object Document Mapper)  
  
+ SQL DB 的反擊  
    + Sharding 技術  
    + Spider  
        + 作者為 ST Global 公司的 Kentoku Shiba  
        + 為 MySQL 提供分割功能  
        + 和 InnoDB, MyISAM 一樣，為 MySQL 儲存引擎中的一種  
        + 邏輯和 DB 分離  
        + 可維護性高  
    + Michael Stonebraker - RDB 之父  
        + 最早的 RDB - Ingres 的開發者  
        + Ingres -> Postgres -> PostgreSQL  
        + Sybase 和 Microsoft SQL Server 都繼承了 Ingers 的 Code  
    + DB 性能的四大瓶頸  
        + Logging  
            + Log 需要對硬碟寫入，速度緩慢  
        + Buffer Management  
            + 需要管理內容是寫入硬碟或是 RAM  
        + Locking  
            + 在對 Record 進行操作前，必須加上 Lock ，防止其他 thread 對 Record 進行修改  
        + Latching  
            + 對共享的資料結構進行存取時必須使用的排他方式  
    + VoltDB  
        + 比傳統的 RDBMS 高出幾十倍的性能  
        + 線性可擴展性  
        + 以 SQL 作為 DBMS 接口  
        + ACID 特性  
        + 可 365/24 全天候工作的高可用性  
        + 在 2 ~ 12 個 Node 的環境下能夠發揮最大效率(少量的 node 就可實現高超的性能)  
        + 性能高超的原因  
            + 將資料儲存在 RAM 而非硬碟  
                + 排除 Logging 和 Buffer Management 瓶頸  
                + 透過將 RAM 中儲存的資料複製到其他電腦，避免意外關機遺失資料，以保持 Durability  
            + DB 分成多個 partitions 管理，每個 partition 都有獨立的 thread 進行管理，因為每個 partition 都只有一個 thread 對其進行操作，所以不用加上 Lock 和 Latch  
                + 解決 Locking 和 Latching 瓶頸  
        + 缺點  
            + 為了性能優化，把所有 Transaction 都事先儲存，無法從 Client 端進行 SQL Query（貌似實際上可以，但不推薦）  
            + 必須用 Java 撰寫對 VoltDB Query 的 client function  
            + 因為存在 RAM 中，所以儲存量大小受到 RAM 的限制，而且資料遺失的危險性也比將資料存在硬碟中的傳統 RDBMS 更危險。  
            + 靈活性沒有 NoSQL 來的高  
  
---  
  
Ch6. 多核時代的編程  
===  
  
#### 6.1 摩爾定律  
  
+ 摩爾(Gordon Moore)定律  
    + 「IC 中的 transistor 數量，大約每兩年增加一倍」  
    + 1965年的原始論文中寫的是每年增加一倍，1975年發表的論文中改成每兩年增加一倍  
    + David House：「LSI 的性能每 18 個月增加一倍」  
+ Dennard Scaling  
    + CPU 中的 MOS (Metal-Oxide Semiconductor) 在製程縮減到原來的 1/2 時，就可以實現 2 倍的開關速度和 1/4 的耗電量  
    + 由 IBM 的 Robert Dennard 發現（Dennard 於 1968 年發明了 DRAM）  
+ RISC 架構  
    + ex: MIPS, SPARC, ARM, PlayStation3 主機中的 Cell 晶片  
+ CISC 微指令轉換技術  
+ Hyper Threading / Simulation Multi-Threading  
    + 沒有相互依賴關係的多個指令同時進行  
    + 最多大概提升 30% 的 CPU 性能，只需要增加 5% 的 transistor 數量  
+ Multi-core  
    + Homogeneous multi-core  
    + Heterogeneous multi-core (CPU + GPU + ...)  
+ Many-core 正在研究中  
+ 摩爾定律的極限  
    + 導線寬度比感光光源的波長還小  
        + 必須在透鏡和晶圓中間加入純水，縮短光源的波長  
        + 波長更短的遠紫外線或X射線，很難用透鏡聚焦，可以使用反射鏡替代，但曝光機率和成本都會上升  
    + 開始進入量子物理的範圍，穿隧效應造成滲漏電流  
    + 熱密度的問題  
    + 需求的飽和  
        + 一般的大眾使用電腦所需要的性能不太需要主頻極高的 CPU  
        + 當然在 3D 圖形、視訊編碼和科學計算方面是永遠都不夠用的  
  
> 結論: 摩爾定律的終結，代表著硬體不再像以往進步的如此神速。  
> 軟體工程師在往後的日子，勢必得付出更多心力在優化方面，  
> 不能再像以前只依靠硬體的進步就能夠解決許多效能上的問題。  
> 作者將這現象稱為「免費午餐的終結」  
  
#### 6.2 UNIX pipeline  
  
+ JCL (Job Control Language)  
+ Shell  
+ Script  
+ Stream pipeline  
    + pipeline 在多核的環境下非常有用  
    + xargs  
        + -P : 要開的 Process 數量  
+ 很多時候瓶頸不是在 CPU 的性能，而是在其周邊裝置。在這樣的情況下，增加 CPU 的數量也不會改善效能。  
+ 阿姆達爾定律  
    + 估算透過多核 CPU 平行計算能夠獲得多少性能提升的經驗法則  
    + 「透過多核平行計算所獲得的系統效能提升效果，會隨著無法平行的部分而產生飽和。」  
    + 速度提升比例的公式  
        + 1 / [(1 - P) + P / N]  
        + P = 可平行化的比例  
        + N = CPU 的數量（並行度）  
+ ccache  
    + 將編譯的結果存入 cache 以達到大幅降低再次編譯時所花費的時間  
    + 用法: `$ CC='ccache gcc' make -j4`  
    + 將結果存在該資料夾底下的 .ccache/ 中  
+ distcc  
    + 利用多台電腦來改善編譯速度的工具  
    + 要在 ~/.distcc/hosts 中寫好要用哪些主機  
    + 被用到的主機必須要執行 distccd 或者可以透過 ssh 登入  
    + 透過 ssh 的安全性較高，但因為加密的關係，編譯效能會下降 25% 左右。  
    + 透過 distccd 的話，因為沒有認證機制，安全性較低，但編譯效能較快。  
    + 用法 `$ CC='distcc gcc' make -j4`  
  
#### Ch6.3 Non Blocking I/O  
  
+ Event Driven Model  
+ read(2), select, O_NONBLOCK  
+ Ruby: read_partial, read_nonblock  
+ POSIX: aio_read  
  
> POSIX (Portable Operating System Interface X), IEEE 103, 在各種 UNIX system 上 API 相互關聯的標準  
  
#### Ch6.4 node.js  
  
+ Introduction  
    + JavaScript  
    + Event Driven  
    + Non Blocking Framework  
    + Google Chrome v8 Engine  
    + Call Back Sytle  
+ 優點  
    + 可以很容易實做一個 Web Server  
    + 採用 epoll (Linux) 和 kqueue (FreeBSD), 可因應較多的 connection  
    + 採用 HTTP1.1 的 keep-alive 方式，同個 client 的 connection 是可以重複使用的，降低 TCP Socket connection 重複連接造成的成本。  
    + Event Driven 降低每個 connection 消耗的資源  
    + 同一個 client 對同一個 Server 進行頻繁的連接而且連接數非常大的時候，使用 node.js 非常適合(ex: 網路聊天程式)  
+ 其他 Event Driven Model  
    + Ruby: EventMachine, Rev  
    + Python: Twisted  
  
> [sid](http://www.debian.org/releases/sid/) - The unstable distribution of Debian  
  
#### Ch6.5 ZeroMQ  
  
+ Threads  
    + 在同一個 Process 中，所以只能在一台電腦上完成所有工作。  
        + 一台電腦的核心有限，遇到大規模的 concurrent 還是會有瓶頸。  
    + 共享 Memory  
        + 優點: data 不需要進行複製  
        + 缺點: thread 是獨立運作的，但因為資料共享，所以可能會更改到其他 thread 正在進行操作的資料，造成非常難以發現的 bug  
+ Processes  
    + 優點: 不必侷限在一台電腦上進行工作  
    + 缺點: 無法共享 Memory，必須進行資料複製以達到共享，對性能造成不利影響。  
    + 由於 Memory 無法共享，所以 process 之間必須進行溝通，還得考慮到排他性。  
    + Process Communication  
        + Pipe  
            + 只能在有 parent, sibling 或可共享 File Descriptor 的 process 之間使用  
            + 在所屬的 Process 結束後，會自動被銷毀  
        + SysV IPC (Unix System V Inter Process Communication)  
            + Message Queue  
                + 可以保存寫入訊息的長度  
            + Semaphore  
                + 可以設定某個 Resource 最大的同時訪問量  
            + Shared Memory  
            + 溝通完後必須進行顯示的銷毀，否則會在系統中留下 Garbage，造成 Memory Leak  
            + `$ man svipc`  
        + Socket  
            + 在 Process 結束後會由 OS 自動釋放，無需擔心 Memory Leak  
            + TCP Socket  
                + 基於 IP, 可在不同的電腦之間傳遞訊息  
                + Connection  
                + Realiable  
                + Datastream: 不會保存寫入訊息的長度  
            + UDP Socket  
                + 基於 IP, 可在不同的電腦之間傳遞訊息  
                + Connectionless  
                + Unrealiable  
                + Datagram: 會保存寫入訊息的長度  
            + UNIX Socket  
                + 非基於 IP, 只能在同一台電腦上傳遞訊息  
+ ZeroMQ (zmq)  
    + 為了解決 Process 溝通之間，使用 Socket 進行委派的易用性不夠理想而誕生  
    + 支援跨平台(Linux, Mac OS X, Windows)之間進行溝通  
    + 支援多種程式語言  
    + 提供了多種底層通信方法，可透過 API 使用  
        + tcp  
            + 使用 hostname 和 port 進行連接  
            + ZeroMQ 不存在身份認證的安全機制，所以不要在網路上公佈自己機器 ZeroMQ 的 port 號  
        + [ipc](http://en.wikipedia.org/wiki/Inter-process_communication)  
            + 同一台電腦上的 process 之間溝通  
        + inproc  
            + 同一個 process 之間的 thread 溝通  
        + multicast  
            + 一對多電腦的訊息傳遞  
            + 然而有些 router 是禁止 multicast 的  
    + 多種 connection model  
        + REQ/REP (Request/Reply)  
            + 雙向  
            + client 發 request, server 回 reply  
        + PUB/SUB (Publish/Subscribe)  
            + 單向  
            + Server publish 訊息給有 subscribe 過該 Sever 的 Client  
        + PUSH/PULL  
            + 單向  
        + PAIR  
            + 雙向, 一對一  
    + 其標準 API 是以 C 撰寫的  
    + 啓動順序自由：一般必須先啓動 Server 端，但在 ZeroMQ，先啓動 Client 端也是可以的。如果 Client 發現 Server 端未啓動的話，便會進入待機狀態，等待 Server 開啓服務。  
  
> 現在已是多核時代，撰寫程式的時候更應該考慮使用多核心來提高效能，而不是停留在以前單核心時代的撰寫方式。  
