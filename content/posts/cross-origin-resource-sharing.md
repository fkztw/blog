Title: 紀錄一下和 CORS (Cross-Origin Resource Sharing) 有關的問題  
Slug: cross-origin-resource-sharing  
Date: 2016-09-07 23:22:28  
Authors: fkz  
Category: Note  
Tags: W3C, HTTP, CORS, Cross-Origin HTTP Request, Google App Engine  
Summary: 前陣子在弄公司系統新架構的 CDN 部份時遇到和 Cross-Origin HTTP Request 有關的問題，紀錄一下。  
  
  
## Situation  
  
錯誤訊息長的像下面這樣  
  
```  
Font from origin 'http://cdn.xxx.xxx'  
has been blocked from loading by Cross-Origin Resource Sharing policy:  
No 'Access-Control-Allow-Origin' header is present on the requested resource.  
Origin 'http://ooo.xxx.xxx' is therefore not allowed access.  
```  
  
這是以前沒遇過的問題，  
所以尋找了一下答案，  
紀錄起來，  
給自己備忘。  
  
---  
  
## What is CORS?  
  
### CORS is the abbreviation of "Cross-Origin Resource Sharing".  
  
#### 1. [HTTP access control (CORS) - HTTP | MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS#Access-Control-Allow-Origin)  
  
1.  
> For security reasons, browsers restrict cross-origin HTTP requests initiated from within scripts. For example, XMLHttpRequest follows the same-origin policy. So, a web application using XMLHttpRequest could only make HTTP requests to its own domain. To improve web applications, developers asked browser vendors to allow XMLHttpRequest to make cross-domain requests.  
  
2.  
> The W3C Web Applications Working Group recommends the new Cross-Origin Resource Sharing (CORS) mechanism. CORS gives web servers cross-domain access controls, which enable secure cross-domain data transfers. Modern browsers use CORS in an API container - such as XMLHttpRequest - to mitigate risks of cross-origin HTTP requests.  
  
簡單來說就是 XMLHttpRequest 因為安全性的考量只允許相同域名的請求，  
如果要請求跨域名的物件的話，  
就必須請目標域名的管理者把自己加到該目標域名網站的 `Access-Control-Allow-Origin` 的 HTTP Header 中，  
而 CORS 就是為了解決這件事而出現。  
  
#### 2. [Cross-Origin Resource Sharing (CORS) | Cloud Storage | Google Cloud Platform](https://cloud.google.com/storage/docs/cross-origin#client_side_support)  
  
1.  
> The same-origin policy is a security policy enforced on client-side web apps (e.g., web browsers) to prevent interactions between resources from different origins. While useful for preventing malicious behavior, this security measure also prevents useful and legitimate interactions between known origins. For example, a script on a page hosted from Google App Engine at example.appspot.com might want to use static resources stored in a Cloud Storage bucket at example.storage.googleapis.com. However, because these are two different origins from the perspective of the browser, the browser won't allow a script from example.appspot.com to fetch resources from example.storage.googleapis.com using XMLHttpRequest because the resource being fetched is from a different origin.  
  
2.  
> The Cross Origin Resource Sharing (CORS) spec was developed by the World Wide Web Consortium (W3C) to get around this limitation.  
  
大意其實跟上面那段差不多。  
  
  
#### 3. [Cross-Origin Resource Sharing](https://www.w3.org/TR/cors/)  
  
1.  
> This document defines a mechanism to enable client-side cross-origin requests. Specifications that enable an API to make cross-origin requests to resources can use the algorithms defined by this specification. If such an API is used on http://example.org resources, a resource on http://hello-world.example can opt in using the mechanism described by this specification (e.g., specifying Access-Control-Allow-Origin: http://example.org as response header), which would allow that resource to be fetched cross-origin from http://example.org.  
  
2.  
> 5.1 Access-Control-Allow-Origin Response Header  
> The Access-Control-Allow-Origin header indicates whether a resource can be shared based by returning the value of the Origin request header, "\*", or "null" in the response. ABNF:  
> `Access-Control-Allow-Origin = "Access-Control-Allow-Origin" ":" origin-list-or-null | "\*"`  
> Note: In practice the origin-list-or-null production is more constrained. Rather than allowing a space-separated list of origins, it is either a single origin or the string "null".  
  
所以直接從文件看來，  
W3C 當初設計上其實是允許多個 domain 的，  
只要以空白分隔就行。  
但 Note 的部份就提到了一個重點，  
實作上通常只允許單一 domain 或是 `"*"` 而已，  
不允許用空白分隔多個 domain 形成的 origin-list，  
這個原因我也不懂，  
但造成我不小的問題就是。  
  
---  
  
## Solution of Google App Engine for CORS  
  
### [app.yaml Reference | App Engine standard environment for Python | Google Cloud Platform](https://cloud.google.com/appengine/docs/python/config/appref)  
> CORS Support  
>  
> One important use of this feature is to support cross-origin resource sharing (CORS), such as accessing files hosted by another App Engine app.  
>  
> For example, you could have a game app mygame.appspot.com that accesses assets hosted by myassets.appspot.com. However, if mygame attempts to make a JavaScript XMLHttpRequest to myassets, it will not succeed unless the handler for myassets returns an Access-Control-Allow-Origin: response header containing the value http://mygame.appspot.com.  
>  
> Here is how you would make your static file handler return that required response header value:  
>  
> ```  
> handlers:  
> - url: /images  
>   static_dir: static/images  
>   http_headers:  
>     Access-Control-Allow-Origin: http://mygame.appspot.com  
> ```  
> Note: if you wanted to allow everyone to access your assets, you could use the wildcard '\*', instead of http://mygame.appspot.com.  
  
這邊並沒有提到能不能使用空白分隔的 origin-list，  
但我記得我試過，  
結果是不行的，  
所以後來我採用下面的解法，  
仍然是只能設定成 `"*"`  
  
在 `app.yaml` 中，  
針對 static files 的 handler 加上 `http_headers`，  
並在其中加入 `Access-Control-Allow-Origin: "*"`，  
讓所有其他 domain 的 script 都可以 request 這些 static files (assets)。  
  
改完之後的 `app.yaml` 其中部份會長得像是這樣：  
  
```yaml  
 - url: /(.*)$  
   static_files: static/\1  
   upload: static/.*$  
   http_headers:  
      Access-Control-Allow-Origin: "*"  
```  
  
---  
  
## Questions  
  
顯然把 allow domain 設定成 `"*"` 允許所有其他 domain 不是件好事，  
理想上當然是只允許 subdomain 就好，  
但我在找尋相關解法的時候沒有找到這樣的用法。  
看到的解答都是 `Access-Control-Allow-Origin` 只能允許使用一個寫死的 domain 或是 `"*"`。  
  
Apache 和 Nginx 都可以針對這個部份做設定，  
例如這兩篇都有提到作法：  
  
+ [CORS with Wildcard Subdomains Using Nginx — Rustyrazorblade](http://rustyrazorblade.com/2013/10/cors-with-wildcard-subdomains-using-nginx/)  
+ [Apache Configure CORS Headers for Whitelist Domains](http://blog.blakesimpson.co.uk/read/64-apache-configure-cors-headers-for-whitelist-domains)  
  
似乎是回一個寫死 domain 的 `Access-Control-Allow-Origin` 的 HTTP Header，  
但是可以在設定檔裏面做設定，  
如果 request 是來自允許的 domain 的話，  
就把 `Access-Control-Allow-Origin` 的值設定成該 domain，  
如果不在白名單裡面的話當然就擋掉。  
  
Google App Engine 這邊也只能幫忙加上 header，  
如果 Google App Engine 的使用者想針對這部份做進一步的設定的話，  
我目前的想法是只能用 Flexiable Environment，  
前面架個 Apache 或 Nginx 來解掉這問題，  
但我還沒試過就是，  
因為後來又有其他事情得做，  
所以這個 CDN 就暫時開發到這邊而已。  
  
---  
  
## Postscript  
  
弄這個 CDN 大約是6月底的事，  
所以算來也差不多兩個月了，  
直到最近又遇到了一次 CORS 的問題。  
  
主要是公司有些功能想要實作，  
會需要在客戶的網站上呼叫我們自家公司的 API，  
同事嘗試了以後就遇到 CORS 的問題然後跑來問我。  
因為 API 也是跑在 Google App Engine，  
所以我第一時間就想到在該 API 的 url handler 加上 http_headers。  
但加上去以後用 `appcfg.py` 要 deploy 的時候遇到了下面這個錯誤，  
  
```  
appcfg.py: error: Error parsing ./app.yaml: Unexpected attribute "http_headers" for mapping type script.  
  in "./app.yaml", line 70, column 1.  
```  
  
看來 Google App Engine 不允許對非 static files 的 handler 加上 HTTP Headers，  
於是只好另尋出路。  
  
想了一下，  
依稀記得之前在處理這個問題的時候好像有看到 JSONP 可以跳過一些跨域名請求的限制，  
於是找到了這篇 [javascript - Google Place API - No 'Access-Control-Allow-Origin' header is present on the requested resource. Origin 'null' is therefore not allowed access - Stack Overflow](https://stackoverflow.com/questions/28359730/google-place-api-no-access-control-allow-origin-header-is-present-on-the-req)  
底下有一個回應給出了解答，  
可以透過 jQuery 的 `$.ajax()` 跳過 CORS 的限制，  
直接拿到 Cross-Domain 的 JSON API 的結果。  
  
作法如下：  
  
```javascript  
$.ajax({  
    url: $url_of_api,  
    type: "GET",  
    dataType: 'jsonp',  
    cache: false,  
    success: function(response){  
        console.log(response);  
    }  
});  
```  
  
其中把 `$url_of_api` 換成會回傳 JSON 結果的 Cross-Domain API 的網址就行了，  
我把這個事件叫作「JSONP 拯救 Cross-Domain JSON API Request」。(啥  
  
---  
  
## Related Links  
  
+ [HTTP access control (CORS) - HTTP | MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS#Access-Control-Allow-Origin)  
+ [Cross-Origin Resource Sharing (CORS) | Cloud Storage | Google Cloud Platform](https://cloud.google.com/storage/docs/cross-origin#client_side_support)  
+ [python - Access-Control-Allow-Origin header on Google App Engine - Stack Overflow](https://stackoverflow.com/questions/17555269/access-control-allow-origin-header-on-google-app-engine)  
+ [Cross-Origin Resource Sharing](https://www.w3.org/TR/cors/)  
+ [CORS with Wildcard Subdomains Using Nginx — Rustyrazorblade](http://rustyrazorblade.com/2013/10/cors-with-wildcard-subdomains-using-nginx/)  
+ [Apache Configure CORS Headers for Whitelist Domains](http://blog.blakesimpson.co.uk/read/64-apache-configure-cors-headers-for-whitelist-domains)  
+ [app.yaml Reference | App Engine standard environment for Python | Google Cloud Platform](https://cloud.google.com/appengine/docs/python/config/appref)  
+ [javascript - Google Place API - No 'Access-Control-Allow-Origin' header is present on the requested resource. Origin 'null' is therefore not allowed access - Stack Overflow](https://stackoverflow.com/questions/28359730/google-place-api-no-access-control-allow-origin-header-is-present-on-the-req)  
