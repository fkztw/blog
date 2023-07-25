Title: Setup Static Ip Wired Network in Arch Linux  
Date: 2013-02-25 02:05  
Author: fkz  
Category: Note  
Tags: Linux, Arch Linux, sysadmin, Network  
Slug: setup-static-ip-wired-network-in-arch-linux  
Modified: 2015-10-27 22:11  
  
  
因為之前安裝 Arch 的時候是用 wireless network 只要用就好  
  
```sh  
$ sudo wifi-menu  
```  
  
或者是  
  
```sh  
$ sudo wicd-gtk  
```  
  
> Arch 預設沒有裝 wicd,  
> 要使用的話請先用 `$ sudo pacman -S wicd-gtk` 安裝 wicd 後就可以解決  
> 在執行 wicd-gtk 之前 要先  `$ sudo wicd`  把 wicd run 起來  
> 不然會有錯誤訊息顯示  
  
以上是無線網路的部份 設定很簡單 有線網路的設定就比較麻煩一點  
  
---  
  
> 寒假在家裡上網用 ADSL  
> 照著上一篇的 [[Arch Linux] Set up wired network with pppoe-setup](/posts/2013/02/20/setup-pppoe-wired-network-in-arch-linux/) 就可以完成  
  
---  
  
開學後回到宿舍 得設定 static ip  
一開始想說用 `wicd-gtk` 新增一個 wired connection  
然後把該設定的 property 設定完應該就能用了  
結果就是連不上 然後發現  
  
[Beginners' guide - ArchWiki](https://wiki.archlinux.org/index.php/Beginners%27_guide#Wired) 其實有講  
不過我這裡的方法不太一樣就是 但基本上大同小異  
  
---  
  
以下是我的作法：  
  
在 `/etc/network.d/` 底下建立設定檔  
  
```sh  
$ vim /etc/network.d/ethernet-dorm  
```  
  
其內容如下 #為註解部分  
  
```  
CONNECTION='ethernet'  
DESCRIPTION='A basic static ethernet connection using iproute'  
INTERFACE='enp2s0'  
IP='static'  
ADDR='140.113.69.103'  
GATEWAY='140.113.69.254'  
DNS=('8.8.8.8', '8.8.4.4', '140.113.1.1', '140.113.6.2')  
  
## For IPv6 autoconfiguration  
#IP6=stateless  
  
## For IPv6 static address configuration  
#IP6='static'  
#ADDR6=('1234:5678:9abc:def::1/64' '1234:3456::123/96')  
#ROUTES6=('abcd::1234')  
#GATEWAY6='1234:0:123::abcd'  
```  
  
使用 `netcfg` 這個指令  
  
```sh  
$ sudo netcfg -u ethernet-dorm  
```  
  
這樣應該就可以啟動該網路連線了，如果設定都 OK 的話應該就會正常運作。  
