Title: 解決 Arch Linux 上 gcin 2.8.5-2 無法在 Qt 5.9.x 以後的應用程式中執行的問題  
Slug: solution-for-gcin-2-8-5-2-cannot-run-in-application-using-qt-after-5-9-x-on-arch-linux  
Date: 2018-01-04 23:10:00  
Authors: fkz  
Category: Note  
Tags: Arch Linux, Qt5, qutebrowser, gcin, 2018 iT 邦幫忙鐵人賽  
Summary: 用了 qutebrowser 以後， 發現 gcin 沒辦法在其中使用，查了一下解法後順利解決了，寫這篇文章紀錄一下。  
Modified: 2018-01-05 01:21:00  
  
  
## TL;DR  
  
[在基於較新版qt 5.9.1的軟體中無法輸入中文](https://hyperrate.com/thread.php?tid=33785)  
  
---  
  
## 前言  
  
[qutebrowser](https://github.com/qutebrowser/qutebrowser) 是一款以 Vim 操作流程為主、基於 PyQt5 上開發的的輕量化瀏覽器（有點類似 [dwb](https://bitbucket.org/portix/dwb)）。2017 年中的時候就知道這款瀏覽器了，但沒有特別強烈的需求，因為我在使用 Firefox 或 Chromium 的時候都有安裝 Vimium 這個套件，所以可以做到一樣的事。  
  
2017 年後半從 Firefox 55.0 開始，使用 Quantum 之後，我就從 Chromium 又跳回 Firefox 的懷抱，但接近 2017 年年底的時候，這篇文章：[Firefox is on a slippery slope | Drew DeVault’s Blog](https://sircmpwn.github.io/2017/12/16/Firefox-is-on-a-slippery-slope.html)，講到了 Firefox 和美國的 NBCUniversal "合作"，為該公司新一季的電視劇 "Mr.Robot" 作宣傳。其手法是當你在瀏覽網頁的時候，如果裏面文字有和該劇相關的關鍵字的話，就會被倒過來顯示，而且也會在你造訪某些特定網站的時候，在你的 HTTP request 加入特定的 Header。重點是這是在未經使用者同意就預設開啟的測試功能內，直接幫使用者安裝一個叫作 "Looking Glass" 的 plugin，而且如果你把它關掉的話，在下次更新 Firefox 的時候又會被自動開啟。  
  
再者是，討論這個功能的 ticket 是被鎖定的，只有 Mozilla 內部的人可以看到。這是非常不尊重使用者的行為，尤其 Firefox 又總是以不追蹤使用者、自由的開源軟體自居。雖然 Mozilla 在幾天後發了篇道歉文：[Update: Looking Glass Add-on | The Firefox Frontier](https://blog.mozilla.org/firefox/update-looking-glass-add/)，但這件事還是讓滿多人留下不好的印象的，畢竟這代表專案主導人不尊重使用者，難保之後不會又發生。  
  
剛好這篇文章的作者有提到他已經換到 qutebrowser 一陣子了，覺得還不錯用。剛好我也有在考慮要不要換過去使用，因為用了 Firefox 一陣子，雖然有比以前快，但還是常常會 crash，而且貌似也有 Memory Leak 的問題，常常用了一陣子記憶體就會愈用愈多，得重開才能解決。所以今天就下定決心拿 qutebrowser 來當預設的瀏覽器。  
  
有機會的話可能會寫篇關於 qutebrowser 的介紹文，因為預設的 qutebrowser 其實不太好用，我花了點時間調整了設定才覺得比較能用。但這篇文章是要紀錄我在 Arch Linux 上安裝了基於 Qt5 開發的 qutebrowser 後，無法在其中使用 gcin 輸入法打中文字的問題。  
  
---  
  
## 正文  
  
這篇應該只有在 Arch Linux 上的使用者可能會遇到，解法是在 gcin 論壇的這個討論串看到的：[在基於較新版qt 5.9.1的軟體中無法輸入中文](https://hyperrate.com/thread.php?tid=33785)。  
  
先附上發生 bug 的軟體版本：  
  
+ gcin 2.8.5-2  
+ Qt 5.10.0  
+ qutebrowser v1.0.4  
  
步驟：  
  
+ 先到 <https://git.archlinux.org/svntogit/packages.git/tree/trunk?h=packages/gcin> 把要 build `gcin` 需要的檔案都抓下來，開個資料夾放這些檔案。  
+ 進到該資料夾內，根據討論串裡提到的解法修改 `PKGBUILD`，加上這個 patch，[這裡附上 patch 的純文字檔連結](/files/solution-for-gcin-2-8-5-2-cannot-run-in-application-using-qt-after-5-9-x-on-arch-linux/qt-5.9.patch)：  
  
```  
diff --git a/gcin/trunk/PKGBUILD b/gcin/trunk/PKGBUILD  
index ca08fcb57f3..7048c13411d 100644  
--- a/gcin/trunk/PKGBUILD  
+++ b/gcin/trunk/PKGBUILD  
@@ -39,6 +39,12 @@ prepare() {  
         -e '/^MODVERSION=/a INCS+=-I/usr/include/qt/QtGui/$(MODVERSION) -I/usr/include/qt/QtCore/$(MODVERSION)' \  
         -i qt5-im/Makefile  
  
+    # Patch to make gcin work in qt >= 5.9.x  
+    # ref: <https://hyperrate.com/thread.php?tid=33785>  
+      sed \  
+          -e 's/org.qt-project.Qt.QPlatformInputContextFactoryInterface/&.5.1/' \  
+          -i qt5-im/gcin-qt5.h.in  
+  
     # FS#45732  
     patch -p1 -i ../qt-5.5.patch  
```  
  
+ 在該資料夾內下 `makepkg -s` 這個指令，就會開始 build gcin  
+ build 好之後應該會出現 `gcin-2.8.5-2-x86_64.pkg.tar.xz`  
+ 使用 `sudo pacman -U gcin-2.8.5-2-x86_64.pkg.tar.xz` 來安裝 patch 過後的 gcin  
+ 使用 `qtplugininfo /usr/lib/qt/plugins/platforminputcontexts/libgcinplatforminputcontextplugin.so` 來檢查  
    + 如果沒問題的話應該會得到下面這樣的輸出：  
  
```  
$ qtplugininfo /usr/lib/qt/plugins/platforminputcontexts/libgcinplatforminputcontextplugin.so  
IID "org.qt-project.Qt.QPlatformInputContextFactoryInterface.5.1" Qt 5.10.0 (debug)  
User Data: {  
    "Keys": [  
        "gcin"  
    ]  
}  
```  
  
+ 重新開啟 gcin  
+ 重開 qutebrowser  
  
這樣應該就沒問題了。  
  
---  
  
## 結論  
  
總之，我發了一個 bug report: [FS#56949 : \[gcin\] gcin 2.8.5-2 cannot run in qutebrowser v1.0.4](https://bugs.archlinux.org/task/56949)，希望這個 patch 會被加進去，這樣之後更新應該就沒問題了。  
  
好像有點久沒有自己 build package 了啊，原本打算用 `abs`，然後才想起來 `abs` 已經被 deprecated 了：[Arch Linux - News: Deprecation of ABS tool and rsync endpoint](https://www.archlinux.org/news/deprecation-of-abs/)  
  
---  
  
## 參考來源  
  
+ [GitHub - qutebrowser/qutebrowser: A keyboard-driven, vim-like browser based on PyQt5.](https://github.com/qutebrowser/qutebrowser)  
+ [portix / dwb — Bitbucket](https://bitbucket.org/portix/dwb)  
+ [Firefox is on a slippery slope | Drew DeVault’s Blog](https://sircmpwn.github.io/2017/12/16/Firefox-is-on-a-slippery-slope.html)  
+ [Update: Looking Glass Add-on | The Firefox Frontier](https://blog.mozilla.org/firefox/update-looking-glass-add/)  
+ [在基於較新版qt 5.9.1的軟體中無法輸入中文](https://hyperrate.com/thread.php?tid=33785)  
