Title: wttr.in - 一個讓你用網頁或終端機看天氣或月亮圓缺的有趣網站  
Slug: wttr-in  
Date: 2017-10-20 21:09:15  
Authors: fkz  
Category: Note  
Tags: CLI, Weather  
Summary: 關於 [wttr.in](http://wttr.in) 的一點小介紹  
Modified: 2017-10-20 23:35:15  
  
  
## 前言  
  
最近不知道為啥身邊一堆人在傳 [wttr.in](http://wttr.in)，  
才發現好像有很多人不知道。  
自己是有陣子之前就開始用了，  
當時有花一點時間亂看過[這個專案的程式碼](https://github.com/chubin/wttr.in)，  
依稀記得 wttr.in 有一些比較少人知道的小功能，  
回朋友的某個跟 wttr.in 相關的 Facebook 動態時又去找了一下。  
查著查著突然心血來潮，  
乾脆寫這篇廢文筆記一下。  
  
反正邊緣人的週五晚上沒事做。（嗚嗚  
  
## TL;DR  
  
+ `curl wttr.in` && `curl wttr.in/:help`  
+ <http://wttr.in> && <http://wttr.in/:help>  
+ 專案的原始碼在這：<https://github.com/chubin/wttr.in>  
  
---  
  
## 介紹  
  
最簡單的用法就是 `curl wttr.in`  
或用網頁瀏覽器直接連到 <http://wttr.in>  
就會得到像這樣精美的 ASCII Art 天氣預報圖。  
  
![wttr-web](/files/wttr-in/wttr-web.jpg)  
![wttr-cli](/files/wttr-in/wttr-cli.jpg)  
  
但基本上要用等寬字型才會比較正確的顯示，  
否則排版會亂掉。  
  
---  
  
## 比較少人知道的功能  
  
### 支援 UTF-8  
  
所以其實可以直接用中文  
  
`curl wttr.in/台北` 或 <http://wttr.in/台北>  
  
---  
  
### 可以用不同的形式指定想查的城市天氣  
  
> Supported location types:  
>  
>     /paris                  # city name  
>     /~Eiffel+tower          # any location  
>     /Москва                 # Unicode name of any location in any language  
>     /muc                    # airport code (3 letters)  
>     /@stackoverflow.com     # domain name  
>     /94107                  # area codes  
>     /-78.46,106.79          # GPS coordinates  
  
+ 城市名稱（含 UTF-8，不一定要用英文）  
+ ~地標  
+ 機場代號  
+ @域名 （透過 DNS 去搜尋該域名所註冊的城市）  
+ IP 位址  
+ 美國郵遞區號  
+ 經緯度  
  
---  
  
### 支援不同語言顯示  
  
> Localization:  
>  
>     $ curl fr.wttr.in/Paris  
>     $ curl wttr.in/paris?lang=fr  
>     $ curl -H "Accept-Language: fr" wttr.in/paris  
  
可以用中文顯示，  
用法是這樣  
  
+ <http://zh.wttr.in/taipei>  
+ <http://wttr.in/taipei?lang=zh>  
+ `curl -H "Accept-Language: zh" wttr.in/taipei`  
  
不過這部份還在持續開發中，  
目前是神奇的簡繁混雜的狀況。  
  
![wttr-cli-zh](/files/wttr-in/wttr-cli-zh.jpg)  
  
中文翻譯的 Issue [在此](https://github.com/chubin/wttr.in/issues/83)  
追了一下，  
應該是中間的討論產生了一些誤解，  
原本有人給簡中翻譯，  
結果後來有人以為是繁中，  
所以就變這樣哩，  
是個可以發 PR 的機會。  
  
---  
  
### 可以直接產生 PNG 圖片  
  
> PNG options:  
>  
>     /paris.png              # generate a PNG file  
>     ?p                      # add frame arond the output  
>     ?t                      # transparency 150  
>     transparency=...        # transparency from 0 to 255 (255 = not transparent)  
  
<http://wttr.in/taipei.png>  
  
支援加邊框和調整透明度的參數  
PS：圖片這邊也支援使用下面會提到的參數  
  
---  
  
### 可以接受參數  
  
> Units:  
>  
>     ?m     # metric (SI) (used by default everywhere except US)  
>     ?u     # USCS (used by default in US)  
>     ?M     # show wind speed in m/s  
>  
> View options:  
>  
>     ?0     # only current weather  
>     ?1     # current weather + 1 day  
>     ?2     # current weather + 2 days  
>     ?n     # narrow version (only day and night)  
>     ?q     # quiet version (no "Weather report" text)  
>     ?Q     # superquiet version (no "Weather report", no city name)  
>     ?T     # switch terminal sequences off (no colors)  
  
其實[這程式有吃不少參數](https://github.com/chubin/wttr.in/blob/ac939032fd593b14584ce5c38a86a68026a0190a/share/help.txt)，  
也可以用 `curl wttr.in/:help` 直接查看。  
傳參數給它的方法是接在問號後面，  
像 `curl "wttr.in/taipei?0"`  
大家可以自己試試看，  
這邊就不一一介紹了。  
  
我自己慣用的參數就以下這兩個：  
  
+ `0`: 只顯示現在天氣，不顯示未來幾天的預報  
+ `q`: 讓輸出不會顯示 "Weather Report" 的字串  
  
加上這兩個參數以後輸出就會變得非常簡潔乾淨，  
很適合拿來放在 motd  
`curl "wttr.in/taipei?0q"`  
![wttr-cli-0q](/files/wttr-in/wttr-cli-0q.jpg)  
  
---  
  
### 可以接多個參數  
  
> Options can be combined:  
>  
>     /Paris?0pq  
>     /Paris?0pq&lang=fr  
>     /Paris_0pq.png          # in PNG the file mode are specified after _  
>     /Rome_0pq_lang=it.png   # long options are separated with underscore  
  
多個參數就直接接上去就好了，  
`&` 可加可不加，  
除非遇到像有等號的 `lang=zh` 才得加 `&`  
也就是說  
  
+ `/taipei?0q` 等同於 `/taipei?0&q`  
+ `taipei?0&q&lang=zh` 等同於 `/taipei?0q&lang=zh`  
  
如果是要 png 圖片的話要變這樣  
  
+ `/taipei_0g.png` 等同於 `/taipei_0&q.png`  
+ `/taipei_0&q&lang=zh.png` 等同於 `/taipei_0q&lang=zh.png`  
  
---  
  
### 可以包成一個簡單的 shell function  
  
官方有[推薦怎麼加一個簡單使用 wttr.in 的 bash function](https://github.com/chubin/wttr.in/blob/ac939032fd593b14584ce5c38a86a68026a0190a/share/bash-function.txt)  
也可以用 `curl "wttr.in/:bash.function"` 來察看  
  
> ```  
> wttr()  
> {  
>     # change Paris to your default location  
>     curl -H "Accept-Language: ${LANG%_*}" wttr.in/"${1:-Paris}"  
> }  
> ```  
  
很適合放在 shell 的 alias 裏面  
  
我自己是改成自訂性再高一點，  
可以自己決定要帶什麼參數。  
  
```  
# Weather in terminal  
function weather ()  
{  
    curl -H "Accept-Language: ${LANG%_*}" wttr.in/"${1:-Taipei}?${2:-0q}"  
}  
```  
  
---  
  
### 可以拿來看月亮圓缺  
  
> Special locations:  
>  
>     /moon                   # Moon phase (add ,+US or ,+France for these cities)  
>     /moon@2016-10-25        # Moon phase for the date (@2016-10-25)  
  
  
最後這個是跟天氣比較不太相關的功能  
  
`curl wttr.in/moon`  
  
可以接受日期作為參數，  
觀看不同時間的月相。  
  
`curl wttr.in/moon@2017-10-20`  
  
關於這功能的實作在這 <https://github.com/chubin/pyphoon>，  
是用 Python 撰寫的。  
  
---  
  
## 補充  
  
程式的輸出其實來自另外一支用 Golang 寫的 CLI 程式，  
<https://github.com/schachmat/wego>  
wttr.in 主要只是把 `wego` 和 `pyphoon` 的輸出以 web server 的方式呈現。  
  
然後它其實有點不太穩，  
例如在寫這篇文章的時候，  
大概寫了兩個半小時左右，  
不知道為啥寫到最後 wttr.in 就掛了。`Q_Q`  
有興趣的人其實可以 fork 下來自己架（？  
專案原始碼在這 <https://github.com/chubin/wttr.in>。  
用 Python 寫的，  
Web server 用 Flask + gevent，  
天氣的部份則是接 [WorldWeatherOnline API](https://developer.worldweatheronline.com/api/) 來用。  
