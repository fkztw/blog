Title: 我愛開源，因為會遇到路人幫我寫測試。  
Slug: i-love-open-source-because-someone-will-write-testings-for-me  
Date: 2017-12-24 23:23:12  
Authors: fkz  
Category: Note  
Tags: Open Source, 2018 iT 邦幫忙鐵人賽  
Summary: 無聊寫個小程式，結果被不認識的路人發了幫忙寫測試的 PR，而且 commit messages 還超級詳細，讓我學到了不少，這就是 Open Source 的魅力啊。  
Modified: 2017-12-26 12:05:12  
  
  
## 先講結論  
  
感恩開源！讚嘆開源！（啥）【詳見附 1】  
  
  
## 故事內文  
  
故事緣起於 9 月底的某個星期六晚上  
因為太邊緣了沒人約  
加上一時興起  
於是花了幾個小時  
用 Python 寫了個把文字從橫書轉成直書的小程式  
詳情請見：<https://github.com/M157q/hor2vec>  
  
之後有收到些回饋  
有人說想寫個 JavaScript 版  
也有說人說想寫個 Rust 版  
  
也有收到網友的訊息說  
在隔幾天的十月初  
日本知名的 GitHub 使用者 mattn  
（在 GitHub 上有 3.6k followers，有用 Vim 和寫 Golang 的人應該對他的 id 不陌生）  
也用 Golang 寫了一個用途一樣的程式  
<https://github.com/mattn/tate>  
裏面有些我沒有實作的功能可以參考看看  
  
看了一下才知道  
原來日文的平假名和片假名也有分全形和半形  
然後連標點符號也可以從橫的轉成直的  
  
於是我就開了幾個 issue 紀錄要新增的功能  
然後因為我是測試苦手不太會寫測試  
所以一開始就沒寫測試  
於是就[開了一個 issue 提醒我自己要寫測試](https://github.com/M157q/hor2vec/issues/5)  
  
沒！想！到！  
竟然收到一個路人的 pull request 幫我加上了測試  
<https://github.com/M157q/hor2vec/pull/6>  
花了 27 個 commits  
更動了 400 多行程式碼  
太神奇啦！  
這種路過幫人寫測試的神奇小精靈哪裡找啊？  
  
最神奇的還不只這個  
重點是他的 27 個 commits 裡頭的內容之詳細  
比他更改的程式碼還多行  
實在是太令人賞心悅目  
<https://github.com/M157q/hor2vec/pull/6/commits/0f67f0fe8be0312b08195b8157fac5f0be6c9830>  
於是我就忍不住在底下詢問他  
到底是怎麼寫 commit message 的  
  
他也很認真得[給了一個很詳細的回覆](https://github.com/M157q/hor2vec/pull/6#issuecomment-343633972)  
真的讓我很佩服  
推薦對如何把 commit message 寫好有興趣的人點進去看一下  
  
開源大法太神奇啦  
竟然可以吸引到幫人寫測試的小精靈  
感恩開源！讚嘆開源！  
你在等什麼？  
還不趕快加入開源的行列嗎？  
搞不好你也可以找到你的開源小精靈並向對方學習喔！  
  
（我好像該去 Review 他的 PR 了...）  
  
---  
  
## 附錄  
  
[1] 開源  
全稱「開放源始碼」或「開放原始碼」  
英文 "Open Source"，常被戲稱為「歐噴壽司」  
（例句：「我今天放了一顆歐噴壽司，釣到一個路過的小精靈幫我寫測試，潮爽 der」）  
為一種將程式原始程式碼公開讓人檢視、修改、散佈、使用的行為。  
在台灣隸屬宗教為「開源大法教」（這是玩笑  
教眾口號為「感恩開源！讚嘆開源！」（這也是玩笑  
年度最大教眾聚會為「開源人年會」  
英文全名為 Conference for Open Source Coders, Users and Promoters  
簡稱「COSCUP」，常被戲稱為「餘弦杯」及常被誤認為台灣年度最大型 Cosplay 比賽  
官方網址：<https://coscup.org>  
