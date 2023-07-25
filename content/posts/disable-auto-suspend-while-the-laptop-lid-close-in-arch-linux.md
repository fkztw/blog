Title: Disable auto suspend while the laptop lid close in Arch Linux  
Date: 2013-10-15 05:59  
Author: fkz  
Category: Note  
Tags: Linux, Arch Linux, Laptop, systemd  
Slug: disable-auto-suspend-while-the-laptop-lid-close-in-arch-linux  
Modified: 2015-10-27 21:24  
  
  
1. Use editor to modify the configuration file of the systemd-logind  
`# vim /etc/systemd/logind.conf`  
  
2. Find  
`#HandleLidSwitch=suspend`  
  
3. Uncommnet it and then change it to  
`HandleLidSwitch=ignore`  
  
4. After saving the modification, we need to restart the systemd-logind  
`# systemctl restart systemd-logind`  
  
Now the change should be effective now.  
  
---  
  
## Reference  
  
+ [How to disable auto suspend when I close laptop lid?](http://unix.stackexchange.com/questions/52643/how-to-disable-auto-suspend-when-i-close-laptop-lid)  
