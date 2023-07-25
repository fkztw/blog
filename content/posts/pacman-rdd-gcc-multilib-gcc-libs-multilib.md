Title: pacman -Rdd gcc-multilib gcc-libs-multilib  
Slug: pacman-rdd-gcc-multilib-gcc-libs-multilib  
Date: 2017-09-17 17:50:32  
Authors: fkz  
Category: Note  
Tags: Arch Linux, pacman, gcc, gcc-libs  
Summary: A solution to save your ass if you broke pacman after force removed `gcc-multilib` and `gcc-libs-multilib` on your Arch Linux  
Modified: 2018-07-24 22:04:32  
  
  
### Preface  
  
If you've installed `gcc-libs-multilib` and `gcc-multilib` in your Arch Linux,  
you might cannot `$ sudo pacman -Syu` because sometimes they will conflict with `gcc-libs` and `gcc` in `[core]` repository.  
  
You have two choices:  
  
1. Don't install `gcc` and `gcc-libs` to avoid the conflict, and wait until `gcc-multilib` and `gcc-libs-multilib` have new version.  
    + Remove them from the list of packaged to install of this packages upgrade.  
2. Force remove `gcc-multilib` and `gcc-libs-multilib` with `$ sudo pacman -Rdd gcc-multilib gcc-libs-multilib`.  
  
If you do the latter, and break your `pacman`, then this blog post may be your salvation.  
I just encountered this situation and that's why I wrote down this blog post.  
  
---  
  
### Error Message  
  
> pacman: error while loading shared libraries: libstdc++.so.6: cannot open shared object file: No such file or directory  
  
---  
  
```  
$ ldd $(which pacman)  
  
...  
  
libstdc++.so.6 => not found  
libgcc_s.so.1 => not found  
```  
  
These two share objects are gone which make `pacman` broken.  
  
---  
  
### Solution  
  
Copy `libstdc++.so.6` and `libgcc_s.so.1` from other Arch Linux computer with same architecture.  
  
If you have nothing to copy from, I've backed up these two shared objects with x86_64  architecutre below.  
  
(If somehow you cannot download these two files or these doesn't work for you,  
you can try the following link in the reference part.  
Someone also backed up these two files and uploaded them in the reply of the forum thread.)  
  
  
1. Download these 2 share objects:  
    + [libstdc++.so.6](/files/pacman-rdd-gcc-multilib-gcc-libs-multilib/libstdc++.so.6)  
        + sha256sum: 30c1b6ae5936f5f4afdba39f44465efc84422e957db13580e1891f081b615d0e  
    + [libgcc\_s.so.1](/files/pacman-rdd-gcc-multilib-gcc-libs-multilib/libgcc_s.so.1)  
        + sha256sum: 95298eef28aca7cef5b28d8388ef0ea3721add9e7c19df74054d7b1c41bcca2e  
2. `$ sudo mv libstdc++.so.6 libgcc_s.so.1 /usr/lib`  
3. `$ sudo pacman -S --force gcc gcc-libs`  
    + Make sure you use `--force` option, or pacman will complain about these two files are conflict.  
  
---  
  
### Reference  
  
+ [pacman error: libstdc++.so.6 : archlinux](https://www.reddit.com/r/archlinux/comments/6e2no7/pacman_error_libstdcso6/)  
