Title: Linux 設定桌面環境預設開啟程式  
Slug: set-default-application-in-desktop-environment-on-linux  
Date: 2018-01-05 23:56:26  
Authors: fkz  
Category: Note  
Tags: Linux, Desktop, XDG, 2018 iT 邦幫忙鐵人賽  
Summary: 可以利用 `xdg-settings` 這個指令來設定桌面環境中特定應用檔案預設的開啟程式。  
Modified: 2018-01-06 00:52:26  
  
  
## TL;DR  
  
`xdg-settings {get | check | set} {property} [subproperty] [value]`  
  
---  
  
## 前言  
  
其實主要是最近用了 qutebrowser 以後，要把預設瀏覽器從 Firefox 改成 qutebrowser，因為在 qutebrowser 的設定裡頭找不到，查了 qutebrowser 的說明也沒看到，後來發現一個指令就可以做掉了。  
  
---  
  
## 正文  
  
如果是 CLI 環境的話，可以透過 `EDITOR`, `BROWSER` 等環境變數來做設定。  
  
如果是桌面環境的話，我通常是在我使用的應用程式裏面找看看有沒有可以把該程式設定為預設開啟程式的選項，但因為這在 qutebrowser 上行不通，所以用下面這個方法。  
  
只要是走 [XDG 標準](https://specifications.freedesktop.org/mime-apps-spec/mime-apps-spec-1.0.html) 都可以用這個設定方式。（XDG 為 X Desktop Group 的縮寫）  
  
XDG 的設定檔有下面三種路徑：  
  
+ 個別使用者設定檔  
    + `~/.config/mimeapps.list`  
+ 所有使用者共用  
    + `/etc/xdg/mimeapps.list`  
+ 系統預設設定檔  
    + `/usr/local/share/applications/mimeapps.list`  
    + `/usr/share/applications/mimeapps.list`  
  
但我修改了以後發現沒用，所以就直接透過 `xdg-settings` 這個指令做設定，  
後來用下面這一行解決：  
  
`xdg-settings set default-web-browser qutebrowser.desktop`  
  
使用 `xdg-settings --list` 可以察看有哪些 XDG properties 可以設定。  
  
詳細內容可以參考這篇文章：[Default applications - ArchWiki](https://wiki.archlinux.org/index.php/Default_applications#xdg-utils)  
  
---  
  
## 參考來源  
  
+ [Default applications - ArchWiki](https://wiki.archlinux.org/index.php/Default_applications#xdg-utils)  
+ [freedesktop.org - Wikipedia](https://en.wikipedia.org/wiki/Freedesktop.org)  
