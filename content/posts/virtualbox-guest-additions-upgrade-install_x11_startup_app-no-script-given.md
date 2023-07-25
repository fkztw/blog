Title: VirtualBox Guest additions upgrade: install_x11_startup_app: no script given  
Date: 2014-11-10 11:14  
Author: fkz  
Category: Note  
Tags: VirtualBox, Guest Additions, install_x11_startup_app, sysadmin  
Slug: virtualbox-guest-additions-upgrade-install_x11_startup_app-no-script-given  
Modified: 2015-10-28 14:41  
  
  
I encountered this problem while I was doing the upgrade for the guest additions of VirtualBox.  
  
### Guest OS: Ubuntu 14.04  
  
Remove the following symlinks before you install the new version of the Guest addtions  
  
`# rm /usr/lib/x86_64-linux-gnu/VBoxGuestAdditions`  
`# rm /usr/lib/VBoxGuestAdditions`  
`# rm /usr/share/VBoxGuestAdditions`  
  
---  
  
## Reference  
  
+ [A bozo's blog: VirtualBox Guest additions upgrade: install_x11_startup_app: no script given](http://gallinar.blogspot.tw/2012/07/virtualbox-guest-additions-upgrade.html)  
