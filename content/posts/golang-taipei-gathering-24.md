Title: Golang Taipei Gathering #24  
Slug: golang-taipei-gathering-24  
Date: 2017-05-23 21:46:45  
Authors: fkz  
Category: Conf/Meetup  
Tags: Golang  
Summary: Note for Golang Taipei Gathering #24  
  
  
+ Links  
    + KKTIX: <https://golang.kktix.cc/events/gtg24>  
    + GitHub: <https://github.com/golangtw/GolangTaiwanGathering/tree/master/meetup/gtg24>  
  
---  
  
### 鮑承佑: go-swagger 踩雷分享  
  
+ Slides  
    + <https://github.com/golangtw/GolangTaiwanGathering/blob/master/meetup/gtg24/gogland_and_go-swagger.pdf>  
+ <https://github.com/go-swagger/go-swagger>  
+ [Gogland](https://www.jetbrains.com/go/)  
  
寫 `swagger.yaml` 可以 generate golang code for web server  
  
---  
  
### Genji Lu: Golang GC 演算法  
  
+ Slides  
    + <https://www.slideshare.net/GenchiLu/gc-in-golang-76250675>  
+ [Tri-color GC](https://en.wikipedia.org/wiki/Tracing_garbage_collection#Tri-color_marking)  
    + mark phase & sweep phase  
+ Write Barrier  
+ [Go GC: Prioritizing low latency and simplicity - The Go Blog](https://blog.golang.org/go15gc)  
    + Golang 1.5 時的文章，以降低 latency 為主。  
    + Golang 1.5 公佈了這個 low latency 為主的 Garbage Collector  
+ tradeoff  
    + Tricolor GC 能達到極短暫的 pause time，但相對的付出代價  
        + heap size 不可預期性  
        + 頻繁產生新物件時，throughput 會較低，CPU 時間花在 GC 上的比例較高  
        + 潛在風險：記憶體破碎  
+ 實測 GC example code  
    + `GODEBUG=gctrace=1`  
        + `$ GODEBUG=gctrace=1 go run main.go`  
+ [runtime/pprof](https://golang.org/pkg/runtime/pprof/)  
+ net/pprof  
    + http://127.0.0.1:7777/debug/pprof  
+ Golang 對 GC 的優化  
    + 1.6: 在 rescan stack 階段會檢查自從上次 STW (stop-the-world) 之後該 goroutine 是否有執行過，否則不 scan 該 stack。  
    + 1.7: 用一個 list 紀錄所有自從上次 STW 以後有執行過的 goroutine，在 rescane 階段不用 scan 所有 stack。  
    + 1.8: 修改 write barrier 消除 stack re-scan 的必要性。  
+ Related materials  
    + [GODEBUG | Dave Cheney](https://dave.cheney.net/tag/godebug)  
    + [\[译\]GC专家系列1：理解Java垃圾回收 - 牧曦之晨 - SegmentFault](https://segmentfault.com/a/1190000004233812)  
        + > STW:「回到垃圾回收上，在開始學習GC之前你應該知道一個詞：stop-the-world。不管選擇哪種GC算法，stop-the-world都是不可避免的。Stop-the-world意味著從應用中停下來並進入到GC執行過程中去。一旦Stop-the-world發生，除了GC所需的線程外，其他線程都將停止工作，中斷了的線程直到GC任務結束才繼續它們的任務。GC調優通常就是為了改善stop-the-world的時間。」  
  
---  
  
### Linzy: 介紹 Testify 的 mock 功能  
  
+ Slides  
    + <https://github.com/golangtw/GolangTaiwanGathering/blob/master/meetup/gtg24/testify_gtg24.zip>  
+ <https://github.com/stretchr/testify>  
    + A sacred extension to the standard go testing package  
+ <https://github.com/stretchr/testify#mock-package>  
+ `mock.AnythingOfType("string")`  
+ Chain your expectations  
+ Verify your expectations  
    + `mock.AssertCalled(t, "foo", "bar")`  
  
---  
  
### Stan Lo: Rooby: A new object oriented language written in Go aim at developing microservice efficiently  
  
是這篇[寫自己的程式語言（For Rubyist） – Stan Lo – Medium](https://medium.com/@st0012/%E5%AF%AB%E8%87%AA%E5%B7%B1%E7%9A%84%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80-for-rubyist-3f055c4573da) 的作者本人耶  
  
+ Slides  
    + <https://www.slideshare.net/LoStan/goby-76176699>  
+ [GitHub - goby-lang/goby: Goby (Rooby) is a new object oriented language written in Go aim at developing microservice efficiently.](https://github.com/goby-lang/goby)  
    + 從 Rooby 改名叫 Goby 了，因為被罵翻了，一堆人寫信或開 issue 建議改名 XDDD  
+ <https://goby-lang.github.io/goby/>  
    + 目的是想用 Ruby 的語法來做到像 Golang 一樣的 High Performance 的 Language  
    + Goby is not  
        + A new implementation of Ruby  
        + Syntax sugar for Golang.  
    + Why Golang?  
        + 已經對 Golang 有興趣一陣子  
        + 效能不錯  
        + GC 和底層的事可以交給 Golang，自己則專心在 VM 上面的開發  
    + 上禮拜五辭職來全職開發這個語言，希望大家可以[捐助一點錢](https://gratipay.com/goby/) XD  
    + 目前開發完成度大概是 first release 的 70%  
    + 歡迎大家送 PR，就算是改個錯字也可以。  
