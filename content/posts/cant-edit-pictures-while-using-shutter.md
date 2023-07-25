Title: Can't edit pictures while using Shutter  
Date: 2013-06-08 12:42  
Author: fkz  
Category: Note  
Tags: shutter, perl  
Slug: cant-edit-pictures-while-using-shutter  
Modified: 2017-09-15 17:55:00  
  
  
After upgraded my Arch Linux, I just can't edit photos with Shutter while the function of taking screenshots is ok.  
  
So, I googled for "shutter can't edit archlinux" and found [this article](http://shutter-project.org/downloads/dependencies/).  
The function of editing pics depends on libgoo-canvas-perl  
  
In Arch Linux, we just need to type this in terminal  
  
`$ yaourt -S libgoo-canvas-perl`  
  
to install the package from AUR.  
  
Then the function of editing pics works fine.  
  
---  
  
### Reference  
  
+ [Dependencies | Shutter - Feature-rich Screenshot Tool](http://shutter-project.org/downloads/dependencies/)  
