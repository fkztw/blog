Title: Enable mCrypt in PHP5 on Ubuntu 13.10 for Apache  
Date: 2014-03-27 18:48  
Author: fkz  
Category: Note  
Tags: PHP, Ubuntu, Apache, mCrypt, sysadmin  
Slug: enable-mcrypt-in-php5-on-ubuntu-1310-for-apache  
Modified: 2015-10-26 14:59  
Summary: 幫室友解決網安作業的問題  
  
  
剛剛室友問網安作業  
  
弄了老半天 網頁都是一片空白  
  
後來乾脆直接寫在 .php 裏面  
  
然後用 command line php 執行  
  
結果問題出在  
  
`PHP Fatal Error: Undefined function mcrypt_encrypt()`  
  
看起來就是 mcrypt module 沒被 include 進來  
  
環境是 Ubuntu 13.10  
  
開 `/etc/php5/apache2/php.ini` 也沒看到 `mcrypt.so` 可以拿掉註解  
  
最後請教 Google 大神  
  
發現這篇 [mCrypt not present after Ubuntu upgrade to 13.10](http://stackoverflow.com/questions/19446679/mcrypt-not-present-after-ubuntu-upgrade-to-13-10)  
  
看起來是 Ubuntu 13.10 特有的問題 應該是位置改了之類的吧  
  
底下有回應提到解法  
  
簡記一下：  
  
---  
  
1. `$ sudo apt-get install php5-mcrypt` 確認有安裝 `php5-mcrypt`  
2. `$ sudo ln -s /etc/php5/conf.d/mcrypt.ini /etc/php5/mods-available`  
3. `$ sudo php5enmod mcrypt` 這個指令會自動幫你在 `/etc/php5/apache2/conf.d` 底下建一個 `mcrypt.ini` 指向 `/etc/php5/mods-available/mcrypt.ini`  
4. `$ sudo service apache2 restart` 重啟 Apache server  
  
應該就可以在網頁上順利使用 mcrypt 系列的 function 了  
  
---  
  
#### --珍惜生命，遠離 Ubuntu--  
  
---  
  
## Reference  
  
+ [mCrypt not present after Ubuntu upgrade to 13.10](http://stackoverflow.com/questions/19446679/mcrypt-not-present-after-ubuntu-upgrade-to-13-10)  
