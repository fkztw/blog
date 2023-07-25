Title: Boot LiveUSB in VirtualBox 4.3.18  
Date: 2014-12-04 04:21  
Author: fkz  
Category: Note  
Tags: VirtualBox, LiveUSB, sysadmin  
Slug: boot-liveusb-in-virtualbox-4-3-18  
Modified: 2015-10-28 14:36  
  
  
## Steps  
  
### 1.  
  
```sh  
$ sudo chown fkz /dev/disk1  
```  
  
### 2.  
  
```sh  
$ VBoxManage internalcommands createrawvmdk -filename ~/VirtualBox\ VMs/win7_test.vmdk -rawdisk /dev/disk1  
```  
  
### 3.  
  
+ Create New Machine in VirtualBox and select the generated .vmdk file as the hard drive.  
	+ Use an existing virtual hard drive file while addding the Hard drive.  
  
### 4.  
  
+ Boot the virtual machine.  
  
---  
  
## References  
  
+ [VirtualBox 4.3.4使用USB隨身碟開機 @ 軟體使用教學 :: 隨意窩 Xuite日誌](http://blog.xuite.net/yh96301/blog/64131045-VirtualBox+4.3.4%E4%BD%BF%E7%94%A8USB%E9%9A%A8%E8%BA%AB%E7%A2%9F%E9%96%8B%E6%A9%9F)  
+ [VirtualBox設定由USB隨身碟開機 « 高登工作室](http://gordon168.tw/?p=324)  
+ [virtualbox.org • View topic - Using a raw hard disk on Mac OS X](https://forums.virtualbox.org/viewtopic.php?t=9223)  
+ [virtualbox.org • View topic - VERR_ACCESS_DENIED](https://forums.virtualbox.org/viewtopic.php?f=8&p=99406)  
