Title: 用 broadcom-wl-dkms 讓 BCM4360 [14e4:43a0] (rev 03) 能順利在 Arch Linux 中使用  
Slug: make-bcm4360-14e4-43a0-rev-03-work-on-arch-linux-with-broadcom-wl-dkms  
Date: 2017-10-31 17:10:43  
Authors: fkz  
Category: Note  
Tags: Arch Linux, Broadcom, Wireless, MacBook Air  
Summary: 紀錄一下在使用 BCM4360 14e4:43a0 (rev 03) 的 MacBook Air 2013 上裝 Arch Linux，用 wicd 使用無線網路會遇到問題的解法。  
  
  
## TL;DR  
  
`sudo pacman -S broadcom-wl-dkms` should be good.  
  
If you are using `wicd` like me,  
remember to [close other network management daemon](https://wiki.archlinux.org/index.php/wicd#Initial_setup) like:  
  
`systemctl stop dhcpcd`  
`systemctl disable dhcpcd`  
`systemctl stop NetworkManager`  
`systemctl disable NetworkManager`  
  
---  
  
## 正文  
  
之前好一陣子都是一直用 `broadcom-wl-dkms-248-6.30.223.248-1-x86_64` 撐著，  
簡單來說就是之前從 AUR 上 download 這版的 `broadcom-wl-dkms` 下來後，  
之後每次更新用新版的都有問題，  
就得一直 down grade 下來  
所以我就一直留著舊版的以備不時之需，  
救了我好幾次。  
  
而且因為 dkms 每次在 kernel upgrade 之後，  
都會幫你重新 build 一次，  
基本上不用理他，  
所以我後來也把原本有從 AUR 上裝的 `broadcom-wl-dkms` 刪掉了，  
之後自動更新就不會需要一直 down grade。  
  
直到昨天升上 `Linux 4.13.9-1-ARCH`，  
dkms 無法成功 build `broadcom-wl-dkms-248-6.30.223.248-1-x86_64`，  
我在升級 kernel 的時候又沒去注意 kernel upgrade 的訊息，  
於是我的無線網卡在重開機之後就消失在 `ip`, `iwconfig` 的 output 了。  
  
以前就遇過好幾次這狀況了，  
所以並沒有特別的驚慌。  
想說來試裝看看新版的 `broadcom-wl-dkms`，  
才發現[已經從 AUR 被移到 community repository 了](https://www.archlinux.org/packages/community/x86_64/broadcom-wl-dkms/)，  
用 `sudo pacman -S broadcom-wl-dkms` 安裝後，  
看了一下訊息，  
看起來有成功 build 並安裝。  
  
重開機之後，  
無線網卡出現了，  
也搜尋得到 SSID，  
但就是連不上。  
卡了很久，  
想說回來看看以前自己寫的[這篇文章](/posts/2015/09/10/install-arch-linux-on-macbook-air-mid-2013/)會不會有什麼端倪，  
結果就看到了  
「記得 disable dhcpcd，錯誤訊息也看不出啥端倪，就是在這卡了很久。」  
頓時覺得似曾相似。  
  
`systemctl status dhcpcd` 是 inactive 的，  
又想到了 `NetworkManager` 也會影響到，  
`systemctl status NetworkManager` 是 running...  
靠，怎麼又被誰打開了，  
`systemctl stop NetworkManager` 之後果然就正常了。  
因為之前沒有紀錄錯誤訊息導致我這次找超久，  
所以這次就來紀錄一下這些在 `dmesg` 會看到的錯誤訊息吧。  
（同樣的錯誤訊息也有新增在之前的文章了。）  
  
```  
[ 6677.574915] ERROR @wl_notify_scan_status :  
[ 6677.574919] wlp3s0 Scan_results error (-22)  
```  
  
```  
[ 6560.346608] ERROR @wl_cfg80211_scan :  
[ 6560.346611] WLC_SCAN error (-22)  
```  
  
```  
[ 6467.860408] ERROR @wl_notify_scan_status :  
[ 6467.860413] wlp3s0 Scan_results error (-22)  
```  
  
也因為這次的遭遇而誕生了這篇新文章，  
畢竟網路上跟 Arch Linux 相關的資源實在有點少，  
拿這些錯誤訊息去 Google 看到跟 Arch Linux 相關的，  
大多是 DELL 筆電 (XPS 13, Vostro 3560) 的問題，  
[解法是要用 Fn+PrtScrn 把 Wireless 開啟](https://bbs.archlinux.org/viewtopic.php?pid=1216302#p1216302)。  
第二多的就是跟 Ubuntu 相關的，  
[有篇超級詳細的回答已經紀錄在這了](https://askubuntu.com/a/60395)  
  
---  
  
## 小確幸  
  
不得不說一下，  
這種幾年前自己寫的筆記，  
救了現在的自己的感覺，  
真的是會讓人有  
  
「啊，還好當初有花時間紀錄下來。」  
  
的那種欣慰又安全的感覺啊。  
  
---  
  
## 題外話: DKMS  
  
也是這次查解法的過程看到[這篇文章](https://bbs.archlinux.org/viewtopic.php?pid=1370568#p1370568)才知道，  
其實 Arch Linux 現在每次 kernel upgrade 幫你做的事大致上就是  
  
```  
dkms remove ${KERNEL_MODULE_NAME} -v ${KERNEL_MODULE_VERSION} -k ${CURRENT_KERNEL_VERSION}  
dkms install ${KERNEL_MODULE_NAME} -v ${KERNEL_MODULE_VERSION} -k ${NEW_KERNEL_VERSION}  
```  
  
實際大概長的像這樣  
  
```  
dkms remove broadcom-wl -v 6.30.223.271-15 -k 4.13.8-1-ARCH  
dkms install broadcom-wl -v 6.30.223.271-15 -k 4.13.9-1-ARCH  
```  
  
至於 `dkms install` == `dkms build` + `dkms add`  
這個可以 `man dkms` 就可以看到了  
  
```  
install [module/module-version] [-k kernel/arch] [/path/to/driver.rpm]  
  
    Installs  a  built module/version combo onto the kernel it was built for.  
    If the kernel option is not specified it assumes the currently running kernel.  
    If the module has not been built, dkms will try to build it.  
    If the module has  not been added, dkms will try to add it.  
    In both cases, the install command can then take the same arguments as the build or add commands.  
    If you pass a .rpm file, dkms will try to install that file with rpm -Uvh ,  
    and it will perform an autoinstall action to mesure that everything is built for your kernel if the RPM installed sucess‐  
    fully.  
```  
  
這只是個人粗淺的理解，  
如果理解有誤的話還請不吝指教。  
