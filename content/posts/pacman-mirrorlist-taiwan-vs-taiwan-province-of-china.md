Title: pacman mirrorlist - Taiwan vs. Taiwan (Province of China)  
Date: 2014-10-29 20:53  
Author: fkz  
Category: Note  
Tags: Linux, Taiwan, Arch Linux, pacman, mirrorlist  
Slug: pacman-mirrorlist-taiwan-vs-taiwan-province-of-china  
Modified: 2015-10-27 12:55  
  
  
這是個有點久以前的故事了  
  
+ [2012/06/26 的 pacman mirrorlist commit](https://projects.archlinux.org/svntogit/packages.git/commit/trunk?h=packages/pacman-mirrorlist&id=4ebeb6161b4f178b9f3105d47a2c408bc1dd9547)  
  
把 Taiwan 改成了 Taiwan (Province of China)  
  
然後就有台灣人在 Arch Bugs Report 發起一則 Bug Report  
  
+ [FS#30444 - Download Page uses Taiwan's name as “Taiwan, Province of China”](https://bugs.archlinux.org/task/30444)  
  
要求把名字改回 Taiwan  
  
陸陸續續也有人去發 Bug Report 要求正名  
  
+ [FS#35586 - Please change "Taiwan, province of china" to "Taiwan in pacman-mirrorlist](https://bugs.archlinux.org/task/35586)  
+ [FS#35757 - Listing for Taiwan](https://bugs.archlinux.org/task/35757)  
+ [FS#37973 - Taiwan is not a province of China...](https://bugs.archlinux.org/task/37973)  
  
然後之後就被 Admin 拿 [ISO 3166](http://en.wikipedia.org/wiki/ISO_3166) 打槍  
  
![ISO 3166](/files/pacman-mirrorlist-taiwan-vs-taiwan-province-of-china/iso_3166.png)  
  
把相關所有 Report 都 close 掉  
  
直到剛剛  
下個 `sudo pacman -Syu` 更新 Arch，再用 `sudo pacdiff` 更新設定檔的時候  
發現從 Taiwan (Province of China) 改回 Taiwan 了  
  
![Change Back to Taiwan](/files/pacman-mirrorlist-taiwan-vs-taiwan-province-of-china/change_back_to_taiwan.png)  
  
覺得有點訝異和好奇  
查了下官網也沒啥相關公告  
然後去翻了一下[最新的 commit log](https://projects.archlinux.org/svntogit/packages.git/commit/?h=packages/pacman-mirrorlist&id=6438bca958924f781d166c2a473abecd3db54670)  
和舊的比較一下  
發現是同一個 committer  
  
![Same Committer](/files/pacman-mirrorlist-taiwan-vs-taiwan-province-of-china/same_committer.png)  
再去看了一下 [Arch Linux 官網的 Download Page](https://www.archlinux.org/download/)  
台灣的部分還真的改回來變成 Taiwan 了  
  
![Taiwan](/files/pacman-mirrorlist-taiwan-vs-taiwan-province-of-china/taiwan.png)  
  
於是又去找了一下 [Google Cache](http://webcache.googleusercontent.com/search?q=cache:nsRN9P-SvTgJ:https://www.archlinux.org/download/+&cd=1&hl=en&ct=clnk&gl=tw) 確認一下是不是最近發生的事  
發現還是舊的 Taiwan (Province of China)  
  
![Province of China](/files/pacman-mirrorlist-taiwan-vs-taiwan-province-of-china/province_of_china.png)  
  
所以就確定是最近發生的事了  
  
不過我不太清楚改回來的原因是啥  
（其實我也不知道當初被從 Taiwan 改成 Taiwan (Province of China) 的原因）  
發個[噗浪狀態](http://www.plurk.com/p/ki0evh)後就有人跑去要求 [re-open](https://bugs.archlinux.org/task/30444#actionbuttons) 了 囧  
  
> 2014-10-29: A request to re-open the task has been made. Reason for request: ISO claimed that the country name is not part of the ISO 3166 standard, thus it's still a WONTFIX for the upstream, ArchLinux is responsible for the issue for regarding something not-in-fact-in-a-standard as standard, thus request re-open. Falling back to the complex procedure of finding country names *least* irritating for everyone is both sane and required.  
  
![Re-open](/files/pacman-mirrorlist-taiwan-vs-taiwan-province-of-china/re_open.png)  
  
且看這次會如何回應吧?  
  
---  
  
# Reference  
  
+ <http://planykao.blogspot.tw/2012/07/taiwan-is-not-province-of-china.html>  
