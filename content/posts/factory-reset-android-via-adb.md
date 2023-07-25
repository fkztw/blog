Title: Factory Reset Android via ADB  
Slug: factory-reset-android-via-adb  
Date: 2017-05-05 01:33:34  
Authors: fkz  
Category: Note  
Tags: android, adb, factory reset  
Summary: Simple note for factory reset Android via ADB.  
  
  
## Preface  
  
Factory Reset from the GUI settings of my ASUS ZenFone 2 (ZE551ML) with CynagenMod 14 installed didn't work.  
  
---  
  
## Steps  
  
Before doing this:  
  
+ Make sure your computer had already installed `adb`.  
    + For Arch Linux users: `$ sudo pacman -S android-tools`  
+ Make sure your Android phone had already enable the `Developer Options` and enable the USB Debugging via ADB.  
  
  
Let's go:  
  
1. Connect your Android phone to your computer.  
2. `$ adb devices` make sure your phone is listed.  
2. `$ adb reboot bootloader` to reboot the Android to bootloader.  
3. Wait until it reboot to bootloader.  
4. `$ sudo fastboot erase userdata` to wipe all user data.  
5. `$ sudo fastboot erase cache` to wipe all cache.  
6. `$ sudo fastboot reboot` to reboot your phone.  
  
And that's it, it works for me.  
  
```  
$ adb --version  
Android Debug Bridge version 1.0.36  
Revision 7.1.2_r6  
```  
