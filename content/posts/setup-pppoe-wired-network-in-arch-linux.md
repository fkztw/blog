Title: Setup PPPoE Wired Network in Arch Linux  
Date: 2013-02-20 00:28  
Author: fkz  
Category: Note  
Tags: Linux, Arch Linux, Network, rp-pppoe, PPPoE  
Slug: setup-pppoe-wired-network-in-arch-linux  
Modified: 2015-10-27 22:03  
  
  
照著 [Direct modem connection - ArchWiki](https://wiki.archlinux.org/index.php/Direct_modem_connection) 這部份設定  
  
下 `# pppoe-setup` 的時候 跟我說 `command not found`  
  
查了一下才知道要先裝上 `rp-pppoe`  
  
所以要設定之前記得先下  
  
`$ sudo pacman -S rp-pppoe`  
  
安裝完後再照著上面 ArchWiki 的步驟設定應該就行了  
  
之前不知道要安裝 `rp-pppoe`  
  
結果跑去 ArchWiki 搜尋 `pppoe`  
  
跑出 [pppd - ArchWiki](https://wiki.archlinux.org/index.php/pppd) 給我  
  
照著做還是弄不起來 後來才知道要安裝 `rp-pppoe`  
  
所以就是先 `$ sudo pacman -S rp-pppoe` 後  
  
再 `$ sudo pppoe-setup` 就行了  
