Title: Golang Taipei Gathering #22  
Slug: golang-taipei-gathering-22  
Date: 2017-03-28 22:39:59  
Authors: fkz  
Category: Conf/Meetup  
Tags: Golang  
Summary: Note for Golang Taipei Gathering #22  
  
  
+ Links  
    + <http://golang.kktix.cc/events/gtg22>  
    + <https://www.facebook.com/groups/269001993248363/permalink/817469818401575/>  
  
---  
  
## 19:30~20:10: 陳敬翔 (Sean) - Go 的技能與安裝入門  
  
+ Slides  
    + <http://go-talks.appspot.com/github.com/Starfine/02.-Go-Present/GTG22.slide#1>  
+ 用 Go 開發手機 App  
    + `gomobile`  
        + `gomobile install golang.org/x/mobile/example/flappy`  
    + 用 Chrome 開啟 Android 畫面的瀏覽器套件  
        + <https://chrome.google.com/webstore/detail/vysor/gidgenkbbabolejbgbpnhbimgjbffefm>  
+ 用 Go 開發 Arduino  
    + [GoBot](https://gobot.io)  
+ 學習資源  
    + Google 搜尋時，用 `golang` 當關鍵字，不要用 `go`  
    + <https://github.com/golang/go/wiki/FromXToGo>  
    + 常用網站  
        + [GoDoc](https://godoc.org/)  
        + [GoWalker](https://gowalker.org/)  
        + [AwesomeGo](https://awesome-go.com/)  
            + <https://github.com/avelino/awesome-go>  
        + [GoLangLibs](https://golanglibs.com/)  
  
  
---  
  
## 20:20~21:00: VMFive - TA-CHING CHEN - Introduction to Fission  
  
+ Slides  
    + <https://tachingchen.com/tw/blog/Fission-Introduction/>  
    + <https://www.slideshare.net/TaChingChen/fission-introduction>  
+ [Fission: Fast Serverless Functions for Kubernetes](https://github.com/fission/fission)  
+ Function as a Service (FaaS)  
    + Exmaple  
        + [AWS Lambda](https://aws.amazon.com/lambda/)  
        + [Google Cloud Functions](https://cloud.google.com/functions/)  
    + Pros  
        + developer focus on code snippets  
        + short cold-start  
        + horizontal scaling  
        + pay as you go (!= cheap)  
    + Cons  
        + vendor lock-in  
        + hard to test  
        + environmental limitation  
        + limited execution time per request  
+ Fission  
    + 支援 Go, Node.js, PHP7, Python3, .NET  
        + Go 的部份是以 Go 1.8 plugin 的方式插入，如果要使用 Go 開發的話，記得要把版本升到 1.8  
    + Live demo example  
        + `fission fn create --name GTG22 --env nodejs --code hello.js`  
        + `fission route create --method GET --url /hello --function GTG22`  
        + `fission fn edit --name GTG22`  
        + 看 log (講者貢獻的 [PR](https://github.com/fission/fission/pull/131)，不到一個星期前才剛 merge 進 master branch)  
            + `fission fn logs --name GTG22`  
            + `fission fn logs --name GTG22 -f`  
            + `fission fn logs --name GTG22 -f -d` # 看更詳細的 log (Debug mode)  
    + Architecture  
        + <https://github.com/fission/fission/blob/master/Documentation/Architecture.md>  
        + 會先開好一堆 generic pods listen，當接到佈署 fuction 的需求時，可以在幾毫秒內就佈署完成，並轉換成 Specific Function Pod.  
+ How to contribute  
    + <https://github.com/fission/fission/blob/master/CONTRIBUTING.md>  
    + 是個去年才開始的專案，所以有很多地方可以貢獻。文件寫的不錯，懂 Go 的話基本上可以很快做出一些貢獻。  
    + Repo owner 是位印度人，但英文很好，也很積極的回應，做出貢獻還有可能得到神祕小禮物，例如一件來自美國的 T-shirt 之類的  
    + 還不是個成熟的專案，還不建議用在 Production。  
+ Conclusion  
    + Short cold-start overhead (~100 ms)  
    + Suitable for developers want to set up their own FaaS  
    + Cutsomized environment image  
    + Adjustable execution time  
    + Cheaper than FaaS under heavy usage  
  
---  
  
## Lighting Talks  
  
+ 陳小熊 - Go 新手村冒險筆記  
    + Slides: <https://drive.google.com/file/d/0B158iGrlsSveNFVoUUF4ZTlsbVE/view>  
    + 生動活潑得介紹了 Golang 有哪些學習資源，包括線上課程、推薦書籍、Gopher Con 等等，為入門者提供了一個方向。  
    + 還 Live Demo 了一個用 Golang 實作出來的線上讀書會平台  
        + > 想想我也是上次 GTG 才決定開始學 Golang 的，結果過了一個月了根本沒啥進展，感到慚愧 QQ  
