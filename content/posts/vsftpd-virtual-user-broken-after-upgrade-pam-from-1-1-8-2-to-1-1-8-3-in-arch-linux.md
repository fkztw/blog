Title: vsftpd virtual user broken after upgrade pam from 1.1.8-2 to 1.1.8-3 in Arch Linux  
Date: 2014-02-21 01:53  
Author: fkz  
Category: Note  
Tags: Linux, Arch Linux, vsftpd, pam, sysadmin  
Slug: vsftpd-virtual-user-broken-after-upgrade-pam-from-1-1-8-2-to-1-1-8-3-in-arch-linux  
Modified: 2015-10-27 13:14  
  
  
pam 升到 1.1.8-3 後，vsftpd 的 virtual user 功能就爛掉了  
  
檢查了 `auth.log` 以後，發現噴了  
  
```txt  
Feb 20 00:35:49 localhost vsftpd:  
PAM unable to dlopen(/usr/lib/security/pam_userdb.so):  
/usr/lib/security/pam_userdb.so: cannot open shared object file:  
No such file or directory  
```  
  
進 `/usr/lib/security` 裡查看，發現 `pam_userdb.so` 消失了  
  
推測問題出在這，到 Google 丟了 `/usr/lib/security/pam_userdb.so` 進行搜尋  
  
查到這兩篇文章  
  
+ [pam_userdb.so gone after upgrading pam-1.1.8-2 -> pam-1.1.8-3](https://bbs.archlinux.org/viewtopic.php?pid=1382541)  
+ [FS#38848 - [pam] /usr/lib/security/pam_userdb.so missing](https://bugs.archlinux.org/task/38848)  
  
原來是被移除掉了  
  
從底下的回應看起來好像只看到 vsftpd 的 virtual user 功能受到影響  
  
兩篇的回應都有人提到 `pam_pwdfile` 這個套件，  
不過是在 AUR 上而非官方套件，而且用的人好像有點少，所以不考慮。  
  
目前的解法還是用  
  
```sh  
$ sudo pacman -U /var/cache/pacman/pkg/pam-1.1.8-2-x86_64.pkg.tar.xz  
```  
  
將 pam 先降級回 `pam 1.1.8-2`  
