Title: 關於 Django REST framework 的一些筆記  
Slug: django-rest-framework-note  
Date: 2018-01-07 23:59:00  
Authors: fkz  
Category: Note  
Tags: Python, Django, RESTful API, 2018 iT 邦幫忙鐵人賽  
Summary: 一年多前接觸 Django REST framework 時做的一些紀錄，整理一下，其中包含了 Django REST framework Docs (DRF Docs) 的部份。  
Modified: 2018-01-16 15:04:00  
  
  
## 前言  
  
2016 年 9 月的時候被老闆告知公司報名了交通大學的梅竹黑客松，要我回母校當評審，然後在一個月內生出一個 API 且附帶文件的網站給參賽者使用。  
  
 當時公司並沒有這些資料的 API，只有資料而已，所以等於是從零開始設計，想說藉由這次機會，除了提供給參賽者 API 以外，未來也可以提供給公司自己使用。  
  
在這之前就有聽過 [Django REST frmaework](https://github.com/encode/django-rest-framework)，也看過滿多人用的，查了一下發現也有 [DRF Docs (django-rest-framework-docs)](https://github.com/manosim/django-rest-framework-docs) 這個 plugin 可以用來生出 API 的文件，看了一下範例感覺還不錯，於是就放棄用 Flask 自己刻，直接採用 Django + Django REST framework + DRF Docs + Google Cloud SDK + Google App Engine Flexible Environment，建立一個可以從 BigQuery dataset 撈資料出來且帶有文件說明的 API。  
  
以下會就當時使用 Django REST framework 和 DRF Docs 遇到的問題做些紀錄，當時為了馬上解決一些問題，也 fork 了 DRF Docs 的 repo 來改。  
  
---  
  
## Django REST framework  
  
**以下為了撰寫方便，直接把 Django REST framework 簡稱為　DRF。**  
  
整個 DRF 我覺得設計得滿完整，甚至也有 plugin 的生態系，如果找不到合適的，也可以自己撰寫 DRF 的 plugin。剛開始上手的話有份官方的 Tutorial 可看：[Quickstart - Django REST framework](http://www.django-rest-framework.org/tutorial/quickstart/)，建議把整份 tutorial 都唸完會比較瞭解整個 framework 元件之間的關係，畢竟篇幅也不多，加上 Quickstart 也就 8 個頁面而已。剩下的等實際撰寫程式碼時遇到不太懂的時候，再去查詢官網上詳細一點的文件就行了，有時候真的文件說的不夠清楚的話可能還是得去看一下程式碼。  
  
---  
  
這邊紀錄一下幾個我自己在閱讀文件的時候花比較多時間理解的部份：  
  
+ [1 - Serialization - Django REST framework](http://www.django-rest-framework.org/tutorial/1-serialization/)  
    + 基本上就是在 Django 的 Model 上再多做一層包裝，可以對 API 做一些客製化設定，比如要顯示哪些欄位、限定哪些權限...等等。  
+ [Filtering - Django REST framework](http://www.django-rest-framework.org/api-guide/filtering/)  
    + 如果要針對不同的使用者得到不同的結果的話，就會需要用到 filtering 的部份。  
    + 可以針對使用者、網址、可使用參數做限制。  
    + 有多種不同的 filter 可以用，搜尋、排序、權限，也可以自己繼承下來撰寫客製化的 filter。  
+ [Routers - Django REST framework](http://www.django-rest-framework.org/api-guide/routers/)  
    + 基本上跟 Django 的 dispatcher 寫法差不多，但多了一些可以針對 HTTP method 的設定ˇ等等。  
+ [django-rest-framework/viewsets.py at master · encode/django-rest-framework · GitHub](https://github.com/encode/django-rest-framework/blob/master/rest_framework/viewsets.py)  
    + 當時是因為對 `ViewSet` 可以使用的參數不太清楚，看文件又看不出個所以然，所以就跑去看程式碼了。  
  
---  
  
花了一點時間熟悉之後，我在後續使用上遇到最大的問題是在效能，因為我要去查詢的資料總量滿大的，所以查詢常常都會等很久。還有 DRF 預設的 pagination 部份也沒有處理得很好，查了一下發現也有很多人遇到，所以有滿多文章在講這件事的，這裡列出我自己覺得比較有用的：  
  
+ [Ditching Django REST Framework Serializers for Serpy · BetterWorks Engineering Blog](https://engineering.betterworks.com/2015/09/04/ditching-django-rest-framework-serializers-for-serpy/)  
    + 這篇是作者因為 DRF 的 Serializer 實在是太慢，所以自己寫了另外一個作 serialization 的 library: [serpy](https://github.com/clarkduvall/serpy)  
+ [Optimizing slow Django REST Framework performance](http://ses4j.github.io/2015/11/23/optimizing-slow-django-rest-framework-performance/)  
    + 這篇是在講怎麼透過調整 DRF 的 Serializer 來處理 query 時過慢的問題。  
    + 要用上 `queryset.prefech_realted` 等等。  
+ [Web API performance: profiling Django REST framework](https://www.dabapps.com/blog/api-performance-profiling-django-rest-framework/)  
    + 這篇是作者使用了 DRF 並測試其效能以後自己歸納出的一些結論，基本上是推薦使用 DRF，算是我看過最完整對 DRF 做效能測試的文章了。  
    + 一些迷思：  
        + 自己寫個框架：即便只有用到 DRF 的 `APIView` 其他都沒用到，還是推薦使用 DRF，比起你自己用 Django 撰寫的 API 還是好上許多。  
        + 想用輕量化的框架：DRF 雖然包含了很多功能，但核心的 view 部份是很簡單的。  
        + DRF 會被 Django 的 model 綁住：view 和 serializer 都是可選的，沒有強制綁定。  
        + Django/Python/DRF 太慢：這篇文章會大量討論效能的部份，基本上都可以透過適當的資料庫查詢結果暫存、設計良好的 HTTP 暫存以及 shared server-side cache 來解決。  
    + 接下來就是非常詳細的 profiling 步驟與紀錄  
    + 結論  
        + > Get your ORM lookups right.  
        + > Your database lookups will be the bottleneck.  
        + > Work on performance improvements selectively.  
        + > You don't always need to use serializers.  
  
但這幾篇文章其實都有點舊了，大部份都是 2015 年的，所以可能不一定符合現在的狀況，不確定 DRF 在效能方面改進了多少就是。  
  
---  
  
另外，DRF 也有設計一些可以拿來做測試的函式，列在官方的這篇文章裡頭：[Testing - Django REST framework](http://www.django-rest-framework.org/api-guide/testing/)  
  
---  
  
## DRF Docs  
  
DRF Docs 主要功能就是可以根據你在 Django REST framework 所使用的 View function 直接生出 API 文件，有要額外補充的也可以寫在 View function 的 docstring 裡頭，DRF Docs 會幫你呈現出來，這樣就不需要為了 API 額外撰寫文件，只要 docstring 寫得夠清楚就行，可以節省開發上的時間，也可以讓程式碼更容易被理解。  
  
當時會 fork [GitHub - manosim/django-rest-framework-docs: Document Web APIs made with Django Rest Framework](https://github.com/manosim/django-rest-framework-docs) 出來改的主要原因是要改首頁的標題。  
  
但實際使用過發現有個需求，就是我想在 docstring 直接寫 markdown，覺得應該也有人有這樣的需求，所以找了一下。發現有個 PR 就是在做這件事，不過還沒被 merge：[Added markdown support for endpoint docstrings by mikeengland · Pull Request #117 · manosim/django-rest-framework-docs · GitHub](https://github.com/manosim/django-rest-framework-docs/pull/117)，於是就把這個 PR merge 進來使用，基本上沒啥太大的問題。  
  
撰寫這篇文章的時候去追了一下進度，發現已經有另外一個支援 markdown 的 PR 被 merge 了：[Add optional markdown for docstrings by rainyday · Pull Request #127 · manosim/django-rest-framework-docs · GitHub](https://github.com/manosim/django-rest-framework-docs/pull/127)，所以現在的 DRF Docs 應該是有正式支援在 docstring 可以寫 markdown 這件事，但這個部份我自己沒使用過就是。  
  
---  
  
## 結論  
  
如果熟 Django 的人真的可以很快用 DRF + DRF Docs 弄出一個可以做帳號權限管理的 REST API 網站，而且因為用上了 DRF Docs，所以不會出現程式碼和文件不一致的狀況。當時撰寫完整個網站我也不過花了 `53 commits  1,806 ++  761 --`，為期大概一個月，學到了沒碰過的新東西，成功嘗試了 Google App Engine Flexible Environment，期間當然也有做其他事。  
  
但如果不考慮快速完成而是考慮效能的話，我大概就不太推薦 DRF，雖然不確定目前效能改善到什麼地步，如果還是要使用的話可能就要在 Database 或架構方面多下點功夫。  
  
因為開發完這網站之後我就沒再碰 DRF 了，所以這篇文章可能會顯得有點過時些，但可以當個參考，畢竟這篇主要目的是紀錄給我自己知道到底我把時間花在哪裡了。  
  
技術文這種東西真的不太能囤積在草稿啊，能發就要趕快發，不然真的很容易過時。如果是一些跟人比較有關係的文章則大概很難過時，看看技術的長青書基本上都是在講人的態度或是做事的方法與原則。其實也在思考以後寫的一些技術文能否能朝這個方向去多紀錄一些。  
  
---  
  
## 參考來源  
  
+ [GitHub - encode/django-rest-framework: Web APIs for Django.](https://github.com/encode/django-rest-framework)  
+ [GitHub - manosim/django-rest-framework-docs: Document Web APIs made with Django Rest Framework](https://github.com/manosim/django-rest-framework-docs)  
