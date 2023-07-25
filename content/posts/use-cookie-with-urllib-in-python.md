Title: Python 中讓 urllib 使用 cookie 的方法  
Slug: use-cookie-with-urllib-in-python  
Date: 2018-01-06 23:57:00  
Authors: fkz  
Category: Note  
Tags: Python, Python 2, Python 3, urllib, cookie, requests, 2018 iT 邦幫忙鐵人賽  
Summary: 紀錄一下在 urllib 使用 cookie 的方法。  
Modified: 2018-01-07 01:42:00  
  
  
## 前言  
  
其實一般來說只要用 [`requests`](https://github.com/requests/requests) 這個超強的 third-party library 就可以解了，`requests` 已經把 Cookie 的部份處理好了，那為什麼要紀錄這篇？其實這問題也是約莫一年前在前公司工作時遇到的問題，以下說明一下：  
  
Google App Engine Standard Environment 除了預設使用 Python 2 以外，加上因為是 PaaS 的關係，做了不少限制，直接拿 `requests` 來用的話會無法使用，必須再搭配 [`requests-toolbelt`](https://github.com/requests/toolbelt) 這個工具，讓 `requests` 在 GAE Standard 上使用的時候，底層會抽換成 GAE 提供的 `urlfetch`，這樣才能使用，而在 GAE Standard 上預設可以使用 `urlfetch` 和 `urllib2`。  
  
那為什麼不用 `requests` 就好了？因為 Legacy code 的緣故，無法很輕易使用 `requests`，所以採用 `urllib2`，但又遇到有需要使用 Cookie 的需求，而 `urllib2` 是沒有支援 Cookie 的，所以就必須再搭配 `cookielib` 來使用。  
  
就用這篇文章紀錄一下作法，順便連 Python 3 的寫法也順便紀錄一下，因為 Python 2 裡的 `urllib2` 和 `cookielib` 在 Python 3 裡頭都有做更動。順便也把最簡單的 `requests` 的寫法也一併附上。  
  
---  
  
## Python 2: `urllib2` + `cookielib`  
  
**Python 2 中的 `urllib2` 是 `urllib` 的加強版，在實際使用上比較常使用 `urllib2`，所以這裡直接講 `urllib2` 的寫法。**  
  
  
### 基本使用  
  
範例其實在官方網站的說明文件最底下的範例就有了：[20.21. cookielib — Cookie handling for HTTP clients — Python 2.7.14 documentation](https://docs.python.org/2/library/cookielib.html#examples)，其實也不會很複雜。  
  
```python2  
import cookielib, urllib2  
cj = cookielib.CookieJar()  
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))  
r = opener.open("http://example.com/")  
```  
  
  
### 不從檔案匯入，直接設定 Cookie  
  
但如果今天我們沒有一份先存好的 Cookie 設定檔，卻又想在發送 request 前預先設定一些 Cookie 的 value 怎麼辦？先講結論：「有辦法做到，但不推薦使用。」（如果是要改 "User-Agent" 的話，這個是 request header，而不是 cookie，所以是 `urllib` 要處理，而不是 `cookielib` 處理，請勿搞混。）  
  
`cookielib.CookieJar` 有個 `set_cookie()` 的函式，其預設接收的參數是 `cookielib.Cookie`，但 `cookielib.Cookie` 的文件中卻有著以下這段說明：  
  
> This class represents Netscape, RFC 2109 and RFC 2965 cookies. It is not expected that users of `cookielib` construct their own `Cookie` instances. Instead, if necessary, call `make_cookies()` on a `CookieJar` instance.  
  
也就是說，預設其實是不期望使用者自己設定 Cookie 的，但並不是不能做到，這個在 StackOverflow 上的回答有給出範例：[python - add cookie to cookiejar - Stack Overflow](https://stackoverflow.com/questions/4685337/python-add-cookie-to-cookiejar#12682437)，但我自己是覺得非常的不直觀，用這種開發方式應該很難維護，除非初始化 `cookielib.Cookie` 的時候把參數的 key 都加上去。順待一提，這篇文章的提問者誤把 `Cookie.SimpleCooke` 丟給 `cookielib.CookieJar.set_cookie()` 當參數餵入，但這個函式可以接受的參數必須是 `cookielib.Cookie`，而不是 `Cookie.SimpleCookie`，所以出了錯，而且這兩者並沒有任何關係，完全是繼承自不同的 class。  
  
  
### 從檔案匯入/匯出到檔案  
  
+ [`cookielib.FileCookieJar.save`](https://docs.python.org/2/library/cookielib.html#cookielib.FileCookieJar.save)  
	+ 將現有的 Cookie export 到檔案中。  
+ [`cookielib.FileCookieJar.load`](https://docs.python.org/2/library/cookielib.html#cookielib.FileCookieJar.load)  
	+ 從檔案中 import Cookie 的設定進來。  
  
這樣一來在實作爬蟲時，遇到會利用 Cookie 來判斷使用者是否登入的網站時就很方便。  
  
---  
  
## Python 3: `urllib.request` + `http.cookiejar`  
  
  
### 基本使用  
  
一樣在 Python 官方的說明文件底下就有範例可以參考了：[21.24. http.cookiejar — Cookie handling for HTTP clients — Python 3.6.4 documentation](https://docs.python.org/3/library/http.cookiejar.html?highlight=cookiejar#examples)  
  
```python3  
import http.cookiejar, urllib.request  
cj = http.cookiejar.CookieJar()  
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))  
r = opener.open("http://example.com/")  
```  
  
其實可以看到跟 Python 2 的寫法一模一樣，只是把 `cookielib` 換成 `http.cookiejar`，`urllib2` 換成 `urllib.request` 而已。  
  
  
### 不從檔案匯入，直接設定 Cookie。  
  
這部份跟 Python 2 一樣，可以做到，但不推薦，就不贅述。  
  
  
### 從檔案匯入/匯出到檔案  
  
+ [`http.cookiejar.FileCookieJar.save`](https://docs.python.org/3/library/http.cookiejar.html?highlight=cookiejar#http.cookiejar.FileCookieJar.save)  
	+ 將目前的 Cookie 匯出到檔案。  
+ [`http.cookiejar.FileCookieJar.load`](https://docs.python.org/3/library/http.cookiejar.html?highlight=cookiejar#http.cookiejar.FileCookieJar.load)  
  	+ 從現有的檔案中匯入 Cookie。  
  
  
---  
  
## requests  
  
官方文件的 Quickstart 就有一個關於 Cookies 的部份：[Quickstart — Requests 2.18.4 documentation](http://docs.python-requests.org/en/master/user/quickstart/#cookies)  
  
`requests` 本身就自帶 Cookie 的處理了，用法簡單了許多：  
  
### 基本使用  
  
> If a response contains some Cookies, you can quickly access them:  
  
```python  
>>> url = 'http://example.com/some/cookie/setting/url'  
>>> r = requests.get(url)  
  
>>> r.cookies['example_cookie_name']  
'example_cookie_value'  
```  
  
> To send your own cookies to the server, you can use the cookies parameter:  
  
```python  
>>> url = 'http://httpbin.org/cookies'  
>>> cookies = dict(cookies_are='working')  
  
>>> r = requests.get(url, cookies=cookies)  
>>> r.text  
'{"cookies": {"cookies_are": "working"}}'  
```  
  
### 不從檔案匯入，直接設定 Cookie。  
  
基本上這邊的作法就是上面 Python 2 那邊提到的作法，不過 `requests` 把剛剛說的加上參數 key  這件事情稍微處理了一下。  
  
> Cookies are returned in a `RequestsCookieJar`, which acts like a `dict` but also offers a more complete interface, suitable for use over multiple domains or paths. Cookie jars can also be passed in to requests:  
  
```python  
>>> jar = requests.cookies.RequestsCookieJar()  
>>> jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')  
>>> jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')  
>>> url = 'http://httpbin.org/cookies'  
>>> r = requests.get(url, cookies=jar)  
>>> r.text  
'{"cookies": {"tasty_cookie": "yum"}}'  
```  
  
### 從檔案匯入/匯出到檔案  
  
這部份在 `requests` 就比較麻煩一點，但也不難，需要額外用到 `requests.utils.dict_from_cookiejar()`，詳細可以參考這篇 StackOverflow 的解答：[How to save requests (python) cookies to a file? - Stack Overflow](https://stackoverflow.com/questions/13030095/how-to-save-requests-python-cookies-to-a-file/13031628#13031628)，它還有用到 `pickle` 這個函式庫。  
  
+ 無論是 `requests.Response.cookies` 或 `requests.Sessions.Session.cookies` 都是 `requests.cookies.cookiejar_from_dict()` 的輸出結果。  
+ 可以用 `requests.utils.dict_from_cookiejar()` 這個函式，將 `response.cookies` 或是 `session.cookies` 當作輸入，就可以得到該 Cookie 以 `dict` 方式呈現結果，當然也就可以匯出到檔案。  
+ 要匯入的話，可以使用 `requests.utils.cookiejar_from_dict()` 這個參數來把 `dict` 轉成 `RequestsCookieJar`。  
	+ `requests.utils.cookiejar_from_dict()` 是從 `requests.cookies` import 來的。  
+ 使用到 `pickle` 只是方便以 `pickle` 的形式儲存而已。  
  
---  
  
## 結論  
  
能用 `requests` 的話當然就直接用吧，如果遇到我提到的這種狀況才會需要特殊的解法。  
  
---  
  
## 參考來源  
  
+ [python - What are the differences between the urllib, urllib2, and requests module? - Stack Overflow](https://stackoverflow.com/questions/2018026/what-are-the-differences-between-the-urllib-urllib2-and-requests-module)  
+ [GitHub - requests/requests: Python HTTP Requests for Humans™ ✨🍰✨](https://github.com/requests/requests)  
+ [GitHub - requests/toolbelt: A toolbelt of useful classes and functions to be used with python-requests](https://github.com/requests/toolbelt)  
+ [20.5. urllib — Open arbitrary resources by URL — Python 2.7.14 documentation](https://docs.python.org/2.7/library/urllib.html?highlight=urllib)  
+ [20.6. urllib2 — extensible library for opening URLs — Python 2.7.14 documentation](https://docs.python.org/2.7/library/urllib2.html)  
+ [20.21. cookielib — Cookie handling for HTTP clients — Python 2.7.14 documentation](https://docs.python.org/2/library/cookielib.html)  
+ [21.5. urllib — URL handling modules — Python 3.6.4 documentation](https://docs.python.org/3/library/urllib.html?highlight=urllib)  
+ [21.24. http.cookiejar — Cookie handling for HTTP clients — Python 3.6.4 documentation](https://docs.python.org/3/library/http.cookiejar.html?highlight=cookiejar#module-http.cookiejar)  
+ [Quickstart — Requests 2.18.4 documentation](http://docs.python-requests.org/en/master/user/quickstart/#cookies)  
