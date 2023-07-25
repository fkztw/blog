Title: Arch Linux Quick Installation with GPT in BIOS  
Date: 2013-12-30 16:36  
Author: fkz  
Category: Note  
Tags: Linux, Arch Linux, Guide, GPT, BIOS  
Slug: arch-linux-quick-installation-with-gpt-in-bios  
Modified: 2015-10-27 19:08  
  
  
## Preface  
  
A quick installation based on [Arch wiki - Beginners' Guide](https://wiki.archlinux.org/index.php/Beginners'_Guide)  
  
> WITHOUT NETWORK CONFIGURATION  
> (INSTALL IN VIRTUAL MACHINE USING DHCP).  
> YOU NEED TO SETUP THE NETWORK OF THE MACHINE FIRST.  
  
---  
  
## Network  
  
[Network configuration - ArchWiki](https://wiki.archlinux.org/index.php/Network_configuration)  
  
---  
  
## Partition  
  
* `# lsblk`  
    * Check you are partitioning on the right disk.  
    * (assume `/dev/sda` here)  
* `# cgdisk /dev/sda`  
    * Partition Table  
        * GPT - `ef02` (BIOS boot partition) => `/dev/sda1`  
            * 1M  
            * MUST be the first partition of the disk.  
            * `IMPORTANT!! Set to BIOS Boot partition for grub2`.  
        * / - 8300 (Linux filesystem) => `/dev/sda2`  
        * swap - 8200 (Linux swap) => `/dev/sda3`  
        * home - 8302 (Linux /home) => `/dev/sda4`  
    * Write -> yes  
    * QUIT  
* `# lsblk`  
    * Check if the partition scheme of the disk is right.  
  
---  
  
## Create Filesystem  
  
* `# mkfs.ext4 /dev/sda2`  
    * `ext4` for `/`  
* `# mkfs.ext4 /dev/sda4`  
    * `ext4` for `home`  
* `# mkswap /dev/sda3 && swapon /dev/sda3`  
    * `swap` for `swap`  
  
## Mount partitionis  
  
* `# mount /dev/sda2 /mnt`  
* `# mkdir /mnt/home && mount /dev/sda4 /mnt/home`  
  
## Select a mirror  
  
* `# vi /etc/pacman.d/mirrorlist`  
    * Choose a mirror site that is the nearest from your machine  
    * Copy it to the top of this mirrorlist.  
  
## Install the base system  
  
* `# pacstrap /mnt base base-devel`  
  
###Generate fstab  
  
* `# genfstab -p /mnt > /mnt/etc/fstab`  
* `# vi /mnt/etc/fstab`  
    * Check if the fstab is right.  
  
---  
  
## Chroot and configure the base system  
  
* `# arch-chroot /mnt /bin/bash`  
    * After chroot, use bash.  
  
### Locale & Keymap  
  
* `# vi /etc/locale.gen`  
    * Select needed encoding and uncomment them.  
    * en_US.UTF-8 UTF-8  
    * zh_TW.UTF-8 UTF-8  
* `# locale-gen`  
* `# echo "LANG=en_US.UTF-8" > /etc/locale.conf`  
* `# echo "KEYMAP=us" > /etc/vconsole.conf`  
  
### Timezone & Hardclock & Hostname  
  
* `# ln -s /usr/share/zoneinfo/Asia/Taipei /etc/localtime`  
* `# hwclock --systohc --utc`  
* `# echo "$myhostname" > /etc/hostname`  
  
### Configure the network (DHCP)  
  
* `# systemctl enable dhcpcd.service`  
    * I use DHCP for the virtual machine.  
* For static IP  and wireless, Check the Official Guide  
    * [Network configuration - ArchWiki](https://wiki.archlinux.org/index.php/Network_configuration)  
  
### Create an initial ramdisk environment  
  
* If you won't modify `/etc/mkinitcpio.conf`, you can just skip this step.  
* `# mkinitcpio -p linux` after modified `/etc/mkinitcpio.conf`  
  
### Set User  
  
* `# passwd`  
    * set root password.  
* `# useradd -m $user`  
    * add a user with home directory.  
* `# passwd $user`  
    * set the password for the user.  
  
---  
  
## Install and configure a bootloader  
  
* `# pacman -S grub`  
* `# vi /etc/default/grub`  
    * [For a bug of grub I've met](https://bugs.archlinux.org/task/38041?project=1&cat%5B0%5D=31&string=grub).  
    * Add `GRUB_DISABLE_SUBMENU=y` at the end of `/etc/default/grub`  
* `# grub-mkconfig -o /boot/grub/grub.cfg`  
    * Generate the configuration file of grub  
> If you didn't add the `GRUB_DISABLE_SUBMENU=y` mentioned above  
> you would get error message and fail here.  
  
* `# grub-install --target=i386-pc --recheck /dev/sda`  
> If you didn't mark the GPT partition (1007KiB)  
> as a `BIOS Boot Partition`  
> you would get error message and fail here.  
> the solution is in [GRUB - ArchWiki](https://wiki.archlinux.org/index.php/GRUB#Intel_BIOS_not_booting_GPT)  
  
---  
  
## After installation  
  
* `# exit`  
* `# umount -R /mnt`  
    * unmount the partitions  
* `# reboot`  
  
---  
  
## References  
  
* [Arch wiki - Beginner's Guide](https://wiki.archlinux.org/index.php/Beginners'_Guide)  
* [Arch wiki - GRUB - Intel BIOS not booting GPT](https://wiki.archlinux.org/index.php/GRUB#Intel_BIOS_not_booting_GPT)  
* [[solved] Grub Update gives Syntax error](https://bbs.archlinux.org/viewtopic.php?id=173921)  
* [FS#38041 - grub 1:2.00.1282.g5ae5c54-1 will not generate grub.cfg file syntax errors](https://bugs.archlinux.org/task/38041?project=1&cat%5B0%5D=31&string=grub)  
* [Archlinux installation - xatierlike](http://xatierlike.blogspot.tw/2012/10/archlinux-installation.html)  
