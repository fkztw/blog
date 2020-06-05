Title: 新增幾項設定來防範 Clickjacking Frame Attack
Slug: clickjacking-frame-attack-defense
Date: 2018-07-23 05:34:59
Authors: m157q
Category: Note
Tags: Security, Clickjacking, owasp, Content Security Policy, CSP, X-Frame-Options, Frame Breaking Script
Summary: 公司的 Bug Bounty Program 收到了 Clickjacking Frame Attack 的回報，以前學資安都偏攻擊面較多，最近比較有機會接觸到防禦的部分，想說紀錄一下。
Modified: 2020-06-05 15:18:59

## TL;DR

Clickjacking 主要是在釣魚網站上嵌入正版網站（攻擊對象）的內容，並將一些物件隱藏在正版內容之上，讓受害者以為自己操作了正版網頁，但實際上卻是執行了隱藏物件上的動作。

可以透過以下幾種設定和方法來防禦：

+ [Content Security Policy (CSP)](https://www.owasp.org/index.php/Clickjacking_Defense_Cheat_Sheet#Defending_with_Content_Security_Policy_.28CSP.29_frame-ancestors_directive)
+ [`X-Frame-Options` Header](https://www.owasp.org/index.php/Clickjacking_Defense_Cheat_Sheet#Defending_with_X-Frame-Options_Response_Headers)
+ [Frame Breaking Script](https://www.owasp.org/index.php/Clickjacking_Defense_Cheat_Sheet#Best-for-now_Legacy_Browser_Frame_Breaking_Script)

其他還有 `window.confirm()` protection 和一些注意事項在 OWASP 的網頁都有說明：
[Clickjacking Defense Cheat Sheet - OWASP](https://www.owasp.org/index.php/Clickjacking_Defense_Cheat_Sheet)

---

## `Firebase.json`

關於 `Content-Security-Policy` 和 `X-Frame-Options` 的設定，在 Firebase 裡頭可以簡單作這樣的設定：

```json
{
  "hosting": {
    "public": "dist",
    "cleanUrls": true,
    "headers": [
        {
            "source": "**",
            "headers": [
                {"key": "Content-Security-Policy", "value": "frame-ancestors 'none'"},
                {"key": "X-Frame-Options", "value": "DENY"}
            ]
        }
    ]
  }
}
```

`Headers` 詳細的設定方式可以參考 Firebase 的官方網頁：[Customize Hosting Behavior  |  Firebase](https://firebase.google.com/docs/hosting/url-redirects-rewrites#section-headers)

---

## Content Security Policy (CSP)

- 功用：限制是否要讓其他網頁可以使用 `<frame>` 或 `<iframe>` 嵌入本頁面
- 限制：有些瀏覽器並不支援此 Header
- 我很懶惰，所以直接設定
    - `Content-Security-Policy: frame-ancestors 'none';`
    - 禁止網站所有頁面被嵌入在任何網站

---

## `X-Frame-Options` Header

- 功用：限制是否要讓其他網頁可以使用 `<frame>` 或 `<iframe>` 嵌入本頁面
- 限制：有些瀏覽器並不支援此 Header
- 我很懶惰，所以直接設定
    - `X-Frame-Options: DENY;`
    - 禁止網站所有頁面被嵌入在任何網站

---

## Frame Breaking Script

- 功用：限制是否要讓其他網頁可以使用 `<frame>` 或 `<iframe>` 嵌入本頁面且在舊的瀏覽器上也適用，因為是直接使用 JavaScript 處理，而不是透過瀏覽器去解析 HTTP Header。
- 限制：必須要手動修改網頁上執行的 JavaScript 才能作用，當然遇到不支援 JavaScript 的瀏覽器就無效了？

節錄自 [Clickjacking Defense Cheat Sheet - OWASP](https://www.owasp.org/index.php/Clickjacking_Defense_Cheat_Sheet#Best-for-now_Legacy_Browser_Frame_Breaking_Script):

> In the document HEAD element, add the following:

> First apply an ID to the style element itself:

```html
<style id="antiClickjack">body{display:none !important;}</style>
```

> And then delete that style by its ID immediately after in the script:

```html
<script type="text/javascript">
   if (self === top) {
       var antiClickjack = document.getElementById("antiClickjack");
       antiClickjack.parentNode.removeChild(antiClickjack);
   } else {
       top.location = self.location;
   }
</script>
```

> This way, everything can be in the document HEAD and you only need one method/taglib in your API.

---

## References

+ [Clickjacking Defense Cheat Sheet - OWASP](https://www.owasp.org/index.php/Clickjacking_Defense_Cheat_Sheet)
+ [Clickjacking Defense](https://www.codemagi.com/blog/post/194)
