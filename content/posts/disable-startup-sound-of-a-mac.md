Title: Disable Startup Sound of a Mac  
Date: 2013-11-06 07:30  
Author: fkz  
Category: Note  
Tags: OS X, Mac, Startup Sound  
Slug: disable-startup-sound-of-a-mac  
  
  
The startup sound of Mac won't disappear if I mute the speaker.  
The startup sound just annoys me, so I wanna disable it.  
  
---  
  
## Disable startup sound  
  
`$ sudo nvram SystemAudioVolume=%80`  
  
It should work.  
  
---  
  
## Enable startup sound again  
  
To enable the startup sound  
  
`sudo nvram -d SystemAudioVolume`  
  
---  
  
Just still don't know why `%80` O_o?  
  
---  
  
## References  
[Silence Your Mac Boot Startup Sound Altogether [OS X Tips]](http://www.cultofmac.com/200772/silence-your-mac-boot-startup-sound-altogether-os-x-tips/)  
