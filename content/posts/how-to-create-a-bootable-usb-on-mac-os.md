Title: How to Create a Bootable USB on Mac OS  
Date: 2013-10-14 11:28  
Author: fkz  
Category: Note  
Tags: OS X, Mac, USB, Bootable USB  
Slug: how-to-create-a-bootable-usb-on-mac-os  
  
  
Using Macbook Air 2013 with OSX 10.8.5  
  
`Applications -> Utilities -> Boot Camp Assistant -> continue`  
  
check the `"Create a Windows7 install disk"`  
  
you need to prepare a usb disk and a Windows7 iso file  
  
---  
  
> 2013/10/14 failed for making a Windows7 bootable usb disk using the method below  
  
* Convert a iso file into a img file:  
`hdiutil convert -format UDRW -o $[name].dmg $[name].iso`  
  
* List the disk storage information:  
`diskutil list`  
>You should see the usb disk is one of the /dev/disk?  
  
* Unmount the usb disk for writing the img file into the usb:  
`diskutil umountDisk /dev/disk?`  
  
* Use dd command to write the img file into the ubs disk:  
`sudo dd -if=$[name].dmg -of=/dev/disk? bs=1m`  
  
* If your dd command is GNU version, use:  
`sudo dd -if=$[name].dmg -of=/dev/disk? bs=1M`  
  
* After the dd command is completed, eject the usb disk:  
`diskutil eject /dev/disk?`  
  
---  
  
# Reference  
+ [http://sealmemory.blogspot.tw/2013/05/create-a-usb-stick-on-mac-osx.html][1]  
  
[1]: http://sealmemory.blogspot.tw/2013/05/create-a-usb-stick-on-mac-osx.html  
