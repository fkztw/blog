Title: 如何在 Linux 上使用 Miracast  
Slug: miracast-on-linux  
Date: 2018-01-08 23:10:36  
Authors: fkz  
Category: Note  
Tags: Linux, Miracast, 2018 iT 邦幫忙鐵人賽  
Summary: 紀錄一下在 Linux 上使用 Miracast 無線投影的方法  
Modified: 2018-01-15 15:49:47  
  
  
## TL;DR  
  
先說結論，試了以下兩個專案：  
  
+ [GitHub - albfan/miraclecast: Connect external monitors to your system via Wifi-Display specification also known as Miracast](https://github.com/albfan/miraclecast)  
    + [GitHub - derekdai/miraclecast: Connect external monitors to your system via Wifi-Display specification also known as Miracast](https://github.com/derekdai/miraclecast) 這個 fork 出去修改的版本解決了比較多的問題，但最後嘗試了一番還是沒辦法順利使用。  
+ [GitHub - intel/wds: Wireless Display Software For Linux OS (WDS)](https://github.com/intel/wds)  
    + 嗯，沒錯，是那個 Intel。  
    + 這個算是試到後來可以動的，但結果不盡理想，畫面非常卡，聲音也沒有出來，猜測是還得去調整其他 `gstreamer` 的參數，這篇會以紀錄 `wds` 為主。  
  
---  
  
## 前言  
  
2017 年 5 月換租屋處後，客廳有台螢幕，雖然不大，但至少比筆電的螢幕還大。想說有時候筆電或手機可以把畫面投到上面用大螢幕看比較爽，然後又懶的接有線的 VGA 或 HDMI，就想說來買個無線投影裝置。  
  
於是就在 6 月初左右就上網買了便宜的無線投影裝置，該裝置對於 iOS 裝置的支援是使用 [DLNA](https://en.wikipedia.org/wiki/Digital_Living_Network_Alliance)，對於 Android 裝置的支援則是使用 [Miracast](https://en.wikipedia.org/wiki/Miracast)，當時是我第一次知道 Miracast。  
  
想說筆電是跑 Arch Linux，和 Android 一樣都是 based on Linux，所以應該也可以使用 Miracast 吧？才發現可以用的東西少的可憐，也不一定會動。在 GitHub 上找到了 2 看起來比較有希望的專案，花了好幾個小時，看程式碼、查閱相關文件，終於成功把筆電的畫面透過 Miracast 無線投影到螢幕上。  
  
後來因為室友買了個攜帶型投影機送了 Chromecast 之後就沒有使用 Miracast 了，所以這篇算是個半殘文，但還是想紀錄一下，畢竟花了不少時間研究。  
  
---  
  
## 關於 Miracast  
  
+ 可以把它想像成用 Wi-Fi 來傳輸 HDMI 訊號，所以可以不用接線就能把畫面投影到其他有支援 Miracast 的裝置上。  
+ 除了不用接線外，也不需要有其他的裝置或是要連接到某個 Wi-Fi Access Point。  
    + 這點真的很方便啊，不用買其他裝置就能支援無線投影。  
+ 2012 底，由 Wi-Fi Alliance 推出，也是 Android 4.2 的重要新功能之一，但在 2015 年推出的 Android 6.0 卻消失了。  
+ Miracast 不知道為啥一直沒有成為標準。  
+ Google 後來推出了 Chromecast，基本上這裝置的功能完全和 Miracast 衝突，而且我覺得沒有比較好，除了得額外多接一個 Chromecast 以外，Chromecast 還需要一個額外的 Wi-Fi Access Point，更別說 Chromecast 實際使用上的體驗真的是頗差的。  
+ 關於 Miracast 詳細介紹，可以參考這篇繁體中文的文章：[以鏡射與Wi-Fi技術為基礎　Miracast實現多螢影音串流 - 技術前瞻 - 新通訊元件雜誌](http://www.2cm.com.tw/technologyshow_content.asp?sn=1304260008)  
  
---  
  
##  紀錄  
  
因為 [MiracleCast](https://github.com/derekdai/miraclecast) 沒試成功，所以只會以紀錄 [WDS](https://github.com/intel/wds) 為主。  
其實還有找到一個 [openwfd](https://cgit.freedesktop.org/~dvdhrm/openwfd/)，不過因為看起來已經年久失修了，所以就沒去試了。  
  
---  
  
### WDS 的裝置分類  
  
首先，WDS 把使用 Miracast 的裝置區分為以下兩種：  
  
+ Sink: 要呈現畫面的裝置。  
+ Source: 要把畫面投影出去的裝置。  
  
---  
  
### 我使用 WDS 時遇到的問題  
  
然後把當時遇到的問題相關連結都先列出來一下：  
  
+ [\[wysiwidi-dev\] desktop_source and mirroring display](https://lists.01.org/pipermail/wysiwidi-dev/2015-April/000012.html)  
+ [Working with Linux as Source and Miracast Dongle · Issue #147 · intel/wds · GitHub](https://github.com/intel/wds/issues/147)  
+ [source video params should be tweaked for desktop mirroring use case · Issue #87 · intel/wds · GitHub](https://github.com/intel/wds/issues/87)  
+ [Black/frozen screen · Issue #133 · intel/wds · GitHub](https://github.com/intel/wds/issues/133)  
  
---  
  
### WDS 安裝與使用步驟  
  
WDS 會用到以下幾個程式，必須預先安裝：  
  
+ `wpa_supplicant`  
    + 2.4 以後的版本，且必須要在 build 的時候開啟 `CONFIG_P2P=y`, `CONFIG_WIFI_DISPLAY=y`, `CONFIG_CTRL_IFACE_DBUS_NEW=y` 這 3 個參數  
+ `connman`  
    + 必須是 1.28 以後的版本  
+ `gstreamer`  
  
接下來就可以照著以下步驟來嘗試：  
  
+ `git clone https://github.com/intel/wds.git`  
+ `cd wds`  
+ 修改程式碼  
    + 根據 [source video params should be tweaked for desktop mirroring use case · Issue #87 · intel/wds · GitHub](https://github.com/intel/wds/issues/87) 和 [Black/frozen screen · Issue #133 · intel/wds · GitHub](https://github.com/intel/wds/issues/133) 這兩個 issues 裡頭提到的解法，我們得修改程式碼裡頭用到 `gstreamer` 的參數，不然只會出現黑的畫面，這部份可能因人而異，我只就我遇到的部份描述，附上 git diff，這個參數還有調整的空間就是。  
  
```  
diff --git a/mirac_network/mirac-gst-test-source.cpp b/mirac_network/mirac-gst-test-source.cpp  
index 12c2623..821e38a 100644  
--- a/mirac_network/mirac-gst-test-source.cpp  
+++ b/mirac_network/mirac-gst-test-source.cpp  
@@ -42,7 +42,9 @@ MiracGstTestSource::MiracGstTestSource (wfd_test_stream_t wfd_stream_type, std::  
     } else if (wfd_stream_type == WFD_TEST_VIDEO) {  
         gst_pipeline = "videotestsrc ! videoconvert ! video/x-raw,format=I420 ! x264enc ! mpegtsmux ! rtpmp2tpay ! udpsink name=sink " + hostname_port;  
     } else if (wfd_stream_type == WFD_DESKTOP) {  
-        gst_pipeline = "ximagesrc ! videoconvert ! video/x-raw,format=I420 ! x264enc tune=zerolatency ! mpegtsmux ! rtpmp2tpay ! udpsink name=sink " + hostname_port;  
+        gst_pipeline = "ximagesrc use-damage=0 ! videoscale ! videoconvert ! video/x-raw,format=I420,width=1440,height=900,framerate=50/1 ! x264enc aud=false bitrate=2048 dct8x8=true vbv-buf-capacity=1000 tune=stillimage+zerolatency byte-stream=true ! video/x-h264,profile=high ! muxer. pulsesrc device=alsa_output.pci-0000_00_1b.0.analog-stereo.monitor ! audioconvert ! audio/x-raw,channels=2,rate=44100 ! faac ! audio/mpeg,mpegversion=4 ! muxer. mpegtsmux name=muxer alignment=0 ! rtpmp2tpay pt=33 ! udpsink name=sink sync=false " + hostname_port;  
```  
  
+ `cmake .`  
+ `make`  
+ `sudo wpa_supplicant -i wlp0s20u1 -ddt -u`  
    + `wlp0s20u1` 請換成你的無線網卡裝置名稱  
    + `-ddt`: 用來開啟比較詳細的 debug 訊息，且在訊息加上 timestamp  
    + `-u` : 用來開啟 DBus control interface  
        + 如果 `wpa_supplicant` 在編譯的時候沒有加入上面提到的 `CONFIG_CTRL_IFACE_DBUS_NEW=y` 的話，這個選項就不會有用。  
    + 執行這行指令的時候最好是先把原本有在用的 network manager 關掉，避免衝突。  
+ `sudo connmand -r -n -d -i wlp0s20u1`  
    + `wlp0s20u1` 請換成你的無線網卡裝置名稱  
    + `-r`: 不要開啟 DNS proxy  
        + 官方的 README 上沒有加這個選項，是我自己加上去的，我記得當時可以解掉一些問題，但現在忘了是什麼問題了。  
    + `-n`: 不要在背景執行，方便看到 debug 訊息  
    + `-d`: 開啟 debug 模式  
+ `sudo connmanctl`  
    + 開啟 connman 的互動式介面  
+ `connmanctl> enable wifi`  
+ `connmanctl> enable p2p`  
    + `connmanctl> scan p2p`  
    + `connmanctl> peers`  
    + 檢查 p2p 功能是否正常  
+ `connmanctl> agent on`  
  
如果以上都正常的話，應該就會像[官方在其 GitHub repo 的 wiki 所列出的截圖](https://github.com/intel/wds/wiki)一樣：  
  
+ Android 手機要無線投影到電腦 (Sink mode)  
    + 打開 Miracast 選單應該就可以看到電腦裝置  
    + 選擇投影到電腦上  
    + 許可連線  
    + 沒問題的話應該就可以在電腦上跳出一個視窗顯示手機的畫面了  
+ 電腦要無線投影到其他裝置 (Source mode)  
    + `connmanctl> scan` 可以重新掃描附近的裝置  
    + `connmanctl> peers` 列出可以連線的裝置  
    + `connmanctl> connect N` 連線到該裝置  
    + 許可連線  
    + 正常的話其他裝置應該就會顯示電腦上的畫面了  
  
---  
  
## 結論  
  
還沒到完全能動，畫面有點卡，而且沒有聲音，猜測是還得去調整 `gstreamer` 的參數。  
  
但就紀錄下來，也給可能有遇到這個問題想要解決的人參考，如果有幫助到你的話很歡迎留言跟我說一下，如果試出了更好的結果當然更棒就是。  
  
---  
  
## 參考來源  
  
+ [Digital Living Network Alliance - Wikipedia](https://en.wikipedia.org/wiki/Digital_Living_Network_Alliance)  
+ [Miracast - Wikipedia](https://en.wikipedia.org/wiki/Miracast)  
+ [Android nostalgia: 13 once-trumpeted features that quietly faded away | Computerworld](https://www.computerworld.com/article/3239864/android/android-nostalgia-old-features.html)  
+ [以鏡射與Wi-Fi技術為基礎　Miracast實現多螢影音串流 - 技術前瞻 - 新通訊元件雜誌](http://www.2cm.com.tw/technologyshow_content.asp?sn=1304260008)  
