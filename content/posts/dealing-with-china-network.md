Title: 中國網路相關筆記  
Slug: dealing-with-china-network  
Date: 2018-01-11 16:00:26  
Authors: fkz  
Category: Note  
Tags: China, Network, 2018 iT 邦幫忙鐵人賽  
Summary: 紀錄一下 2016 年 10 月左右處理跟中國網路相關問題時的一些筆記。  
Modified: 2018-02-01 00:22:26  
  
  
## 前言  
  
2016 年 8 月緊急接到要支援客戶在中國的服務，但我們現有的 infrastructure 都是在台灣，又不可能在短時間內全部搬到中國的雲服務商那，所以就用上了各種 workaround，最後算是得到了一個還可以接受的結果，雖然不盡理想就是。  
  
當時實在是忙到沒啥時間紀錄，最近比較有空了，用這篇文章留個紀錄一下。  
  
---  
  
## 一些可以用來輔助的網站  
  
+ <https://en.greatfire.org/analyzer>  
    + TEST URL 可以讓你檢查某個網址在中國是不是被禁止的  
+ <https://www.17ce.com/>  
    + 可以用來檢查中國大部份地區以及少數國外地區連到某個網站的狀況  
    + 我後來有寫個爬蟲專門爬這網站的結果，每個小時去檢查連到某個網址的狀況。  
+ <http://ping.chinaz.com/>  
    + 可以用來檢查中國大部份地區以及少數國外地區連到某個網站的狀況  
    + 我後來有寫個爬蟲專門爬這網站的結果，每個小時去檢查連到某個網址的狀況。  
+ <http://www.speedtest.cn/>  
    + 中國的 SpeedTest  
+ <http://www.webkaka.com/>  
    + 一樣是中國大部份地區連到某個網址的狀況，但伺服器的站點數量沒有很多，有些省分沒有。  
+ <http://tools.cloudxns.net/>  
    + 有一系列的工具可以使用，主要都是跟 DNS 比較相關。  
    + 當時是用來查合作伙伴的伺服器到底有沒有指到中國內的伺服器用的。  
+ <https://www.hidemyass.com/proxy>  
    + 免費的 web proxy，當時用來檢測中國國內某個地方是否可以成功存取我們的資源。  
+ <https://chrome.google.com/webstore/detail/proxy-switchysharp/dpplabbmogkhghncfbfdeeokoefdjegm>  
    + 免費的 chrome plugin，當時用來檢測中國國內某個地方是否可以成功存取我們的資源。  
+ <https://www.gdaily.org/8170/free-proxy-google-china-japan-usa>  
    + 整理了一些免費的 proxy 資源，主要是 proxy 到牆內用。  
+ <http://proxy.moo.jp/zh/?c=CN&pt=&pr=&a%5B%5D=0&a%5B%5D=1&a%5B%5D=2&u=0>  
    + 列出了有哪些免費的 proxy 位址可供使用。  
    + 但很常變動，常常要換就是。  
+ <http://ipcn.chacuo.net/>  
    + 列出中國 IP 對應到哪個電信商及省分的列表  
  
當然使用免費的 proxy 就要記得不要在網站上輸入啥私密資料了，畢竟很有可能會被錄封包。  
  
---  
  
## 狀況  
  
因為現有的服務使用 Google Cloud Platform，伺服器在美國，客戶在中國的網站直接嵌入我們原本提供的 JavaScript 會被中國的防火長城擋掉，導致客戶的網站上看到錯誤，或是要等很久才能載入，等於現有的服務無法提供使用。除了短時間內無法搬到中國的雲服務商上面以外，老闆也不太希望這麼做，一方面是時間上的壓力，一方面是費用的問題，所以還是希望能夠儘量用現有的服務，如果不能全部搬過去也沒差，只要有辦法得到的一個能接受的結果就好。  
  
---  
  
## 歷程  
  
+ 因為連不到放在美國伺服器上的 JavaScript，所以得把目前在用的 JavaScript 放一份到中國雲服務商上，最好還要有 CDN。  
    + 原本有想說要比較中國各服務商例如：青雲、阿里雲、騰訊雲等等，哪些比較好用。但後來因為公司以前有陣子有用阿里雲的服務，所以有帳號，加上時間很趕，所以就直接使用阿里雲了。  
    + 把公司自己的 JavaScript 複製到阿里雲上之後，可以成功連到了。  
+ 但使用的 Google Tag Manager 要載入的 gtm.js 在有些狀況仍然連不到，但有時候卻連得到。  
    + 這部份除非不用 Google Tag Manager，不然基本上沒有什麼太好的解法。  
    + 遇到的時候有去找中國有沒有類似 Google Tag Manager 的服務，但找不太到。  
    + 加上公司使用 Google Tag Manager 有弄出自己的一套架構，所以要搬也沒那麼好搬。  
+ 就想說能不能幫 gtm.js 弄個 proxy。  
    + 有找到這個：[Ajax Cross Origin - jQuery plugin](http://www.ajax-cross-origin.com/)，實際也有架起來。  
    + 但後來才想到這樣根本行不通，因為 gtm.js 會紀錄使用者的行為，架了一個 proxy 的話就會被擋住。  
  
到此已經放棄讓所有使用者都載入 gtm.js 了，轉而變成「讓可以載入的使用者載入，無法載入的就不要載入，而且不能顯示有錯誤。」因為客戶要求不能在連到他們的網站時在瀏覽器的 console 中看到任何錯誤。  
  
+ 於是轉而想說能不能做到「如果嘗試載入 JavaScript 一段時間後不成功的話就停止載入。」  
    + 有找到 StackOverflow 上的這篇： [browser - Load a Javascript file, but cancel if it takes too long? - Stack Overflow](https://stackoverflow.com/questions/5642270/load-a-javascript-file-but-cancel-if-it-takes-too-long)  
    + 試了一下發現無法成功。  
+ 最後自己想出了一個折衷的辦法，但非常的土炮。  
    + 我在阿里雲上開了台虛擬機，用 Django 架了個伺服器。  
    + 寫了個 crawler 每小時固定去爬上面提到的 <https://www.17ce.com/> 和 <http://ping.chinaz.com/> ，把他們有沒有辦法載入 gtm.js 的結果紀錄起來。  
        +  其結果會包含省分、電信商及其能不能載入。  
    + 另外一個 crawler 則是去爬 <http://ipcn.chacuo.net/>，把所有 IP 對應到的省分和電信商紀錄下來，每天會更新一次。  
    + 最後在使用者瀏覽客戶的網站要嘗試載入 gtm.js 之前，會先去問我用 Django 架起來的伺服器，會把使用者的 IP 當參數送過來。  
    + 伺服器收到使用者的 IP 後，先去拿到其所屬的省分和電信商，再去檢查最近一個小時的結果是否能夠載入，如果可以載入的話，API 就會回傳 true 回去，不行的話就回傳 false，當然都是包成 JSON 回傳回去。  
    + 伺服器同時也會把來詢問的結果紀錄到資料庫裡頭，以供日後查詢統計用。最後發現平均能夠載入載入的比例大概是四成左右而已，雖然少的可憐，但至少是可以接受的結果。  
    + 是說這個 Django 專案也算是我第一個完全自己獨力完成的，也學到了不少東西。  
  
---  
  
## 結論  
  
最後整件事情弄完的結論就是：如果原本沒有做中國的服務然後哪天要做中國的服務的話，絕對不要堅持用現有的服務來用，除非確定完全可以動。不然就會出現各種奇怪的狀況，需要各種不同的 workaround 來解，真的會很累。  
  
---  
  
## 參考來源  
  
+ [Ajax Cross Origin - jQuery plugin](http://www.ajax-cross-origin.com/install.html)  
+ [Google Tag Manager blocked in China..? - Webmasters Stack Exchange](https://webmasters.stackexchange.com/questions/81878/google-tag-manager-blocked-in-china)  
+ [browser - Load a Javascript file, but cancel if it takes too long? - Stack Overflow](https://stackoverflow.com/questions/5642270/load-a-javascript-file-but-cancel-if-it-takes-too-long)  
