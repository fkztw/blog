Title: Solution for reconnecting bluetooth after disconnected while using TLP on Linux  
Slug: solution-for-reconnecting-bluetooth-after-disconnected-while-using-tlp-on-linux  
Date: 2020-07-11 20:04:52  
Authors: fkz  
Category: Note
Tags: Linux, TLP, Bluetooth  
Summary: One day, I found I cannot re-enable my bluetooth connection and this solved my problem.


# TL;DR

Set `USB_BLACKLIST_BTUSB=1` in `/etc/default/tlp`  

This will make TLP exclude Bluetooth devices from USB auto suspend.  


# Reason

The default is `USB_BLACKLIST_BTUSB=0` which will auto suspend Bluetooth devices.  
This could make your bluetooth devices cannot be connected with your computer.
