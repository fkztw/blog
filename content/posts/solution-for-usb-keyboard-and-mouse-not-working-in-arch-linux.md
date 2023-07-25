Title: Arch Linux - USB鍵盤和USB滑鼠插上去卻無法使用的解法  
Date: 2013-02-17 01:19  
Author: fkz  
Category: Note  
Tags: Linux, Arch Linux, USB, mkinitcpio  
Slug: solution-for-usb-keyboard-and-mouse-not-working-in-arch-linux  
Modified: 2015-10-27 22:14  
  
  
前幾天剛灌好 `Arch Linux x86_64`  
接上 USB外接滑鼠和鍵盤 竟然沒辦法使用 (我想用我的青軸鍵盤啊Q_Q)  
光學滑鼠的紅色燈有亮 但不能動 鍵盤也沒反應  
查了論壇上幾篇文章 有和我狀況類似的 可是照著弄還是不會動  
大概都是問說有沒有在 `/etc/mkinitcpio.conf` 裏面的 HOOKS 加入 usbinput  
  
但參考了 [mkinitcpio - ArchWiki](https://wiki.archlinux.org/index.php/Mkinitcpio#HOOKS) 後  
  
裏面有著這行敘述  
  
![mkinitcpio](/files/solution-for-usb-keyboard-and-mouse-not-working-in-arch-linux/mkinitcpio.png)  
  
意思是 `usbinput` 在 `mkinitcpio 0.13.0` 已經被合併到 keyboard 裏面了  
所以只要在 `/etc/mkinitcpio.conf` 裏面的 `HOOKS` 加入 `keyboard`  
(HOOKS裏面應該已經有其他東西了)  
加入後，以我的 `mkinitcpio.conf` 為例，會長的像這樣  
  
`HOOKS="base udev autodetect modconf block filesystems keyboard fsck keymap"`  
  
修改完後 一定要記得下  
  
```sh  
$ sudo mkinitcpio -p linux  
```  
  
(我就是忘記下這行指令才卡很久都沒外接滑鼠和鍵盤可以用=  =")  
  
等他跑完 再把USB滑鼠和USB鍵盤插上去試試  
