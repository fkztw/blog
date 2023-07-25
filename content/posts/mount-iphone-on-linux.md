Title: Linux 上如何拿到 iPhone 裡的資料  
Slug: mount-iphone-on-linux  
Date: 2017-12-31 19:01:07  
Authors: fkz  
Category: Note  
Tags: Linux, iPhone, ifuse, 2018 iT 邦幫忙鐵人賽  
Summary: 透過 `ifuse` 可以很容易把 iPhone mount 到 Linux 上，變可以存取 iPhone 裡頭的資料。  
  
  
## 前言  
  
今年 4 月換新手機，因為不愛大尺寸的手機，五吋以下的手機只剩 iPhone SE 和 Sony Xperia X Compact。但查了一下以後發現 Sony Xperia XC 似乎有過熱的問題，加上剛好當時在公司的時候有位同事幾週前才買 iPhone SE，跟他借來操作一下覺得還不錯，上網查了一些評價也都沒啥問題，而且又是秉持當初 Steve Jobs 的 iPhone 設計造型，於是就買了。  
  
因為之前都是用 Android 手機，所以對 iPhone 的生態系不太熟，花了一點時間熟悉，其中一個就是現在紀錄的這篇。以前 Android 手機用 USB 線接到電腦後，基本上只要用 `adb` 就可以搞定一切了，但 iPhone 這邊我花了點時間熟悉一下，還好有 ArchWiki 上有一篇專門在講 iOS 的條目：[iOS - ArchWiki](https://wiki.archlinux.org/index.php/IOS)，省事了不少。  
  
---  
  
## 方法  
  
首先要安裝 `ifuse`，如果是 Arch Linux 的使用者，可以直接用以下指令來安裝：  
  
`sudo pacman -S ifuse`  
  
安裝好之後使用也很簡單，只要按照以下的步驟：  
  
1. 將你的 iPhone 接上電腦的 USB 埠  
2. 接上之後可以透過 `lsusb` 或 `dmesg` 來做確認  
3. `ifuse ${PATH_FOR_IPHONE_DATA}`  
    + 透過這個指令就可以 mount iPhone 的資料了  
    + 以我來說的話，我是特別開了一個 `/media/iPhone-SE` 的資料夾來使用，所以指令會是 `ifuse /media/iPhone-SE`  
    + 記得資料夾的權限要設定好  
4. `umount ${PATH_FOR_IPHONE_DATA}`  
    + 使用完了以後要 unmount 也很簡單，就直接透過上面這個指令就行了  
    + 如果出現 Permission Denied 的話就加上 `sudo` 吧  
  
---  
  
## 參考資料  
  
+ [iOS - ArchWiki](https://wiki.archlinux.org/index.php/IOS)  
