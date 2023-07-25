Title: Mount Windows NTFS filesystem on Mac OSX  
Date: 2013-11-03 11:50  
Author: fkz  
Category: Note  
Tags: OS X, Mac, Windows, NTFS  
Slug: mount-windows-ntfs-filesystem-on-mac-osx  
  
Today, I tried to retrieve datas stored in my USB 2.0 external hard drive.  
After I plugged it into my MacBook Air 2013 USB port,  
I didn't see it show up in the sidebar of the finder.  
So I searching the web to find the solution.  
  
I find two existed softwares to help Mac user using the NTFS disk:  
  
1. [Paragon NTFS](http://www.paragon-software.com/home/ntfs-mac/)  
    After I installed it, it just can't read my NTFS external hard drive.  
    (The disk select list of Paragon NTFS is empty)  
  
2. [Tuxera NTFS](http://www.tuxera.com/products/tuxera-ntfs-for-mac/)  
    I didn't try it. After I saw it only have 15 days trial version, I just skipped it.  
  
Here are the tips to mount the Windows NTFS filesystem on Mac OSX using command line:  
  
<!--more-->  
  
  
#1. Install ntfs-3g  
I installed it by using homebrew. If you already installed homebrew as well,  
just type `brew install ntfs-3g`  
or you can get the source code of ntfs-3g [here](http://macntfs-3g.blogspot.tw/)  
  
---  
  
#2. Load the fuse4x kernel extension  
After installed ntfs-3g, you neet to load the fuse4x-kext or ntfs-3g will not work.  
follow the instructions given by `brew info fuse4x-kext`  
  
`sudo /bin/cp -rfX /usr/local/Cellar/fuse4x-kext/0.9.2/Library/Extensions/fuse4x.kext /Library/Extensions`  
  
`sudo chmod +s /Library/Extensions/fuse4x.kext/Support/load_fuse4x`  
  
---  
  
#3. Check & Mount NTFS  
`diskutil list` to see the identifier of your NTFS disk. **(for me, it's /dev/disk1s1 here.)**  
  
`diskutil unmount /dev/disk1s1` **(to make sure that the volume is unmounted)**  
  
`sudo mkdir /Volumes/NTFS` **(/Volumes/NTFS could be change to anywhere you want to mount your NTFS)**  
  
`sudo ntfs-3g /dev/disk1s1 /Volumes/NTFS`  
You can go to check the /Volumes/NTFS if the NTFS is mounted succefully or not.  
  
> Unsolved Problem:  
> All I could see in my NTFS filesystem are directories.  
> All the files in the directories can't be seen in the finder with gui mode.  
> So, I just use iTerm2 to cd into the directory, then  
> `open x.pdf` to open the file with default application.  
  
---  
  
###References  
[fuse4x installs properly but kext doesn't get loaded (10.8)](https://github.com/mxcl/homebrew/issues/13647)  
[Mount NTFS Drives on Mac](http://blog.taylormcgann.com/2012/07/19/mount-ntfs-drives-on-mac/)  
