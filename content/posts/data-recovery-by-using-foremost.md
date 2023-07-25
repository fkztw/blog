Title: Data recovery by using foremost  
Slug: data-recovery-by-using-foremost  
Date: 2015-08-25 19:02:31  
Authors: fkz  
Category: Note  
Tags: Data Recovery, foremost, Life  
Summary: 今天早上一個不小心手殘，把外接硬碟裡從 2009 年到 2013 年結尾為 .JPG 的檔案都清掉了，哀傷懊悔了大概半小時左右(恩，沒辦法，我的很多美好回憶都在那些年)，開始找尋有沒有可以救援的辦法，踏上一條短暫的資料救援之路(?)  
Modified: 2015-08-26 15:58:58  
  
  
### 溫馨小提醒  
要把所有 \*\.JPG 轉成 \*\.jpg 的情況下  
如果有 `rename` 的話，可以這樣用 `rename "s/JPG/jpg/" *.JPG`  
如果沒有的話，我是這樣用 `find | grep .JPG | xargs -I {}.JPG mv {}.JPG {}.jpg`  
然後就悲劇了，因為如果以 .JPG 結尾的檔案有空白或啥其他特殊的符號的話，就會出現恐怖的意外  
所以改成 `find | grep .JPG | xargs -I {}.JPG mv "{}.JPG" "{}.jpg"` 才能避免悲劇發生  
(應該吧?有錯請指正)  
  
> 其實可以省略 grep  
  
`find -type f -name "*.JPG" | xargs -I {}.JPG mv "{}.JPG" "{}.jpg"`  
  
  
### 資料救援之路 with foremost  
搜尋了一下相關資料  
找到了 [File recovery - ArchWiki](https://wiki.archlinux.org/index.php/File_recovery) 和 [DataRecovery - Community Help Wiki](https://help.ubuntu.com/community/DataRecovery)  
一開始是裝了 [extundelete](http://extundelete.sourceforge.net/)  
裝完以後才想到這顆外接硬碟是 NTFS 不是 ext4  
所以看到底下的 [Foremost](http://foremost.sourceforge.net/)  
在 [DataRecovery - Community Help Wiki](https://help.ubuntu.com/community/DataRecovery) 裡頭寫著支援 fat, ext3 和 NTFS  
所以才想裝來試試看  
  
Arch Linux Official Package 裡頭有  
所以直接 `sudo pacman -S foremost` 就能安裝了  
使用方法也沒有很難  
  
```  
foremost version 1.5.7 by Jesse Kornblum, Kris Kendall, and Nick Mikus.  
$ foremost [-v|-V|-h|-T|-Q|-q|-a|-w-d] [-t <type>] [-s <blocks>] [-k <size>]  
    [-b <size>] [-c <file>] [-o <dir>] [-i <file]  
  
-V  - display copyright information and exit  
-t  - specify file type.  (-t jpeg,pdf ...)  
-d  - turn on indirect block detection (for UNIX file-systems)  
-i  - specify input file (default is stdin)  
-a  - Write all headers, perform no error detection (corrupted files)  
-w  - Only write the audit file, do not write any detected files to the disk  
-o  - set output directory (defaults to output)  
-c  - set configuration file to use (defaults to foremost.conf)  
-q  - enables quick mode. Search are performed on 512 byte boundaries.  
-Q  - enables quiet mode. Suppress output messages.  
-v  - verbose mode. Logs all messages to screen  
```  
  
使用前先把外接硬碟 `umount` 後  
再 `foremost -t jpg -i /dev/sdb1 -o /recovery`  
這是我這次的使用情況: 把 sdb1 中的 .jpg 檔案還原到 /recovery 這個資料夾中  
比較詳細一點的範例可以參考 <https://help.ubuntu.com/community/DataRecovery#Foremost>  
  
另外在 <https://wiki.archlinux.org/index.php/File_recovery#Foremost> 也有寫到  
`foremost` 會根據檔案的 headers, footers 以及內部的資料結構來進行檔案的回復  
可以裝在 Live USB 上使用當作救援USB，也可以直接安裝來使用  
並且可以透過 config file (`/etc/foremost.conf`)來決定要回復哪些類型的檔案  
內建也有提供檔案類型可供選擇：  
jpg, gif, png, bmp, avi, exe, mpg, wav, riff, wmv, mov, pdf, ole, doc, zip, rar, htm, cpp  
  
+ 如果沒有用 -t 指定檔案類型的話，預設就是回復所有檔案  
+ -i 則是接要救援的東西(預設是 stdin，可以是單檔、磁區或是映像檔)  
+ -o 就接要把復原的檔案放到哪裡  
+ -v 的話可以把 log print 到 stdout  
  
總之用法大概就是這樣  
對了 要注意一下 -o 參數接的目標位置的容量夠不夠大，不夠大的話可能會悲劇(?)  
  
  
### 結果  
  
程式大概執行了兩個半小時左右  
總共回復了 24,481 個 jpg 檔  
大小約 11G 左右  
只有稍微看一下，但的確都是消失的檔案沒錯  
之後應該就是慢慢將檔案重新分類就是  
  
  
### 結論  
  
第一次自己搞檔案救援，還好沒把外接硬碟弄掛，不然我一定會哭死  
畢竟這台外接硬碟也有點年紀了，大概也用了6年左右，很怕他哪天突然壞軌掛掉  
然後 `extundelete` 我還沒試過，只是剛好看到順便提一下  
至於 `foremost`，在 <https://github.com/korczis/foremost> 有原始碼，  
稍微瞄過了一下，覺得程式碼寫的蠻乾淨的，有空的時候想去理解一下裏面程式碼怎麼寫的  
然後 README 裏面寫到  
```  
Foremost was written by Special Agent Kris Kendall and Special Agent Jesse  
Kornblum of the United States Air Force Office of Special Investigations  
starting in March 2001.  
```  
恩 沒錯 是美國空軍特別調查辦公室(AFOSI)的兩位特務(Special Agent)寫的  
不愧是美國政府出品 真的蠻猛的 而且還是距今十幾年的 project  
(真不知道我自己現在寫的這些程式 十多年後還能不能正常運作)  
老實說我本來真的對回復這些檔案不抱任何期待  
畢竟有點 UNIX-like system 使用經驗的人大概都知道 rm 跟 mv 不要亂下  
下了就別抱太大的期待能救回來了，畢竟這不是丟到垃圾桶而已  
但 foremost 真的幫我把圖片救回來了...  
所以寫個文章紀錄一下這個好東西  
(只是不知道 24,881 個圖片我要手動分類多久Orz)  
  
  
### References  
+ <https://github.com/korczis/foremost>  
+ <https://help.ubuntu.com/community/DataRecovery>  
+ <https://wiki.archlinux.org/index.php/File_recovery>  
+ <https://wiki.archlinux.org/index.php/Foremost>  
+ <http://foremost.sourceforge.net/>  
