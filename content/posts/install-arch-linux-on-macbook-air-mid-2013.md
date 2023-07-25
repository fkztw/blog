Title: Install Arch Linux on MacBook Air Mid 2013  
Slug: install-arch-linux-on-macbook-air-mid-2013  
Date: 2015-09-10 05:21:04  
Authors: fkz  
Category: Note  
Tags: Arch Linux, MacBook Air, Linux, COSCUP  
Summary: 參加完 COSCUP 2015，聽完 jserv 的封麥演說以及一句「Linux 使用者有錢以後就會投入 Mac 的懷抱」覺得自己深深中槍，備感慚愧。於是決定來做一件很久以前其實就想做的事：跟 Linus Torvalds 一樣，把 MacBook Air 上的 OS X 砍了，直接灌 Linux 來用。當然，Arch Linux 是首選。以下紀錄一下過程，給有需要的人參考。  
Modified: 2017-12-08 12:47  
  
---  
  
> 使用上遇到問題，才有動力去解決、改善、貢獻並回饋程式碼到上游。  
  
`警告: 把 OS X 砍掉的話，之後要更新 firmware 必須使用有安裝 OS X 的外接硬碟上開機才能更新。`  
  
> 以下這段是一堆廢話，講了我為什麼決定要把 OS X 砍了然後灌 Linux 在 MacBook Air 上  
> 不想看的可以直接跳過  
  
改用 OS X 的這兩年，  
也不是說就完全沒用 Linux 了，  
舊的筆電退役成 Server 架在宿舍裡，  
一個不用桌面環境的 Linux ，  
使用起來基本上是不會遇到太多問題的。  
而 OS X 的確遇到使用上的問題減少了。  
用起來的確跟當初想的一樣，  
是個問題比較沒那麼多的 UNIX-like System  
但同時也在不知不覺中漸漸喪失了解決問題的能力，  
就好像一把兩年前就不再磨的刀劍，愈發鈍鏽。  
當初會買 MacBook Air 而不選擇 UltraBook 的原因  
主要是因為價錢、續航力、重量都是 MacBook Air 勝出，  
當然之後在使用上，我也對重量和續航力很滿意，  
但其實在使用 OS X 上也遇過許多無法接受的問題，有些妥協了，有些沒有  
例如：  
  
+ 原生的工具都非常老舊，舊版本代表著很多問題，無論是資安或是有無新功能。這對於一個從使用 Rolling Release 的 Arch Linux user 來說真的很不習慣。  
    + 骨灰級的 Bash 真的令我印象深刻，如果沒有 Homebrew 的話，我肯定無法用這麼久，感謝 `mxcl`  
+ 接網路線跟螢幕線得額外花錢買轉接頭  
    + 兩個加起來新台幣 1,600 左右。恩，我跟很多人一樣都買了。  
+ OS X 10.9 以前的視窗放大真的很雞肋和令人哭笑不得，放大後不會佔滿整個桌面，有時候甚至比按完放大前更小。  
    + 在 OS X 10.10 後，放大功能直接改成全螢幕了。恩，不意外，我在 10.9 以前早就都用全螢幕了。  
+ 雙螢幕在 OS X 10.10 仍然有一個我常常踩到的詭異Bug，如果有程式被丟到外接螢幕那邊，在不拔掉螢幕線的情況下，把螢幕闔上進入休眠，接著把螢幕線拔掉，然後喚醒 Mac，這時候就會發現被丟到外接螢幕的應用程式仍然被認為是在外接螢幕的範圍。但因為早就沒有外接螢幕了，所以即便程式仍然在執行，使用者也根本看不到畫面，重點是重新執行該程式也無法解決這問題，只能登出、重開機或是重新接上外接螢幕在電腦喚醒的情況下拔掉螢幕線，或是把該程式拉回原生螢幕，才有辦法解決。  
    + 我不確定 Reproduce 的機率是不是 100%，但就是偶爾會遇到，而寫這篇文章的時候已經把我手邊唯一的 OS X 砍了，所以也無從驗證。  
+ 系統介面內建中文字型不好看，要改也很難改。  
    + 還好 OS X 10.9 以前有 TCFail 能用，到了 OS X 10.10 只能去改系統檔案設定，而換成了我想用的字型以後，內建的中文輸入法就會掛掉，只好又改回原本的字型。  
+ 輸入法也是個問題  
    + 剛用 OS X 10.8 的時候就聽很多人說內建的中文輸入法不是很好用，所以很多人都裝開源的香草或是小麥注音，我本身也是注音輸入法的使用者，但我用了以後還是不太習慣(恩，當時明明用不習慣，卻沒有跳下去幫忙貢獻)。後來找到另一款開源的中州韻輸入法(RIME)，是對岸的中國人[佛振](https://github.com/lotem)開發的，在 Windows, Linux, Mac 上都能使用。裝來用以後發現還不錯用，自訂性蠻強大的，由於在用 gcin 時，我習慣把選字鍵從常人慣用的 1234567890 改成 asdfghjkl; 以減少手指移動的距離，這款輸入法也能做到，於是就用了。(至於後來關於 dvorak 跟拼音輸入法又是另一個故事了)  
    + 到了 OS X 10.10 之後，不知怎的，非官方的中文輸入法都變得超級慢，慢到無法接受，於是又換回不是很好用的官方中文輸入法。(恩，又是一個妥協，沒去追根究底找出為什麼變得這麼慢的原因)  
  
一不小心好像離題寫了太多關於 OS X 的部份。  
Anyway, 因為種種問題加上這次 COSCUP 的助力，  
還是想回歸到 Linux Desktop Environment 的懷抱，  
促使我把 Arch Linux 灌在我的 MacBook Air 2013 13' 上，  
以下是紀錄。  
  
---  
  
以下流程皆在 `MacBookAir6,2 (Macbook Air mid 2013)` 上進行  
不同 model 的 MacBook 會有不同的問題  
詳見 <https://wiki.archlinux.org/index.php/MacBook#Model-specific_information>  
由於我是採用把 OS X 洗掉直接裝 Arch Linux 的方式，並不是雙系統  
所以安裝方式與一般的 Arch Linux 安裝並無太大不同，  
故本篇文章會著重在裝好之後的一些調整  
  
如果有人想灌成 Ubuntu 的話，可以參考 <https://help.ubuntu.com/community/MacBookAir>  
(但上面最新的資料似乎只有到 2013 年的機種就是，當然也歡迎勇者測試之後貢獻)  
  
`  
警告：MacbookAir6,2 的網卡在 Linux 上"有可能"不被支援(需視網卡型號)，  
所以可能得另購 USB 無線網卡才有無線網路  
詳情請見底下關於 Wi-Fi 的部份  
`  
  
`  
If you want to mute the MacBook firmware boot sound,  
be sure you mute the volume of the MacBook before you eliminating OS X.  
`  
  
# Install Arch Linux Only (No OS X Dual Boot) on MacBook Air  
  
`  
WARNING: After erasing OS X,  
We can only update the MacBook Air firmware via the external drive which has already installed OS X.  
`  
  
1. Make Arch Linux bootable Live USB  
    + Go to <https://www.archlinux.org/download/> and download the newest Arch Linux iso.  
    + Plug in a USB drive  
    + use `diskutil list` to find the USB dirve `/dev/sdX`  
    + `dd if=$(path to arch linux iso) of=/dev/rsdX bs=1m`  
        + use raw disk (/dev/rsdX) make this quicker.  
2. Go to AppStore for updating OS X to the newest version  
    + After the first update, reboot, and check for newest update again  
    + Make sure it's newest update, espcially the firmware udpate  
3. Erase OS X  
    + Reboot MacBook Air  
    + Press Command + R to enter the Reinstall mode  
    + Choose DiskUtility and Erase the entire disk  
4. Entering Arch Linux Live USB installation  
    + Reboot MacBook Air  
    + Press alt/option key for entering EFI bootloader  
    + Choose EFI USB  
5. Install Arch Linux (Just like the normal installation with a little different)  
    + [Beginners' guide - ArchWiki](https://wiki.archlinux.org/index.php/Beginners'_guide)  
    + Important => [MacBook - ArchWiki](https://wiki.archlinux.org/index.php/MacBook#Arch_Only_Installation)  
    + Need to be aware about the EFI related options  
  
---  
  
> 底下其實有些調整不是那麼必要  
> 可能直接 `sudo pacman -S gnome-control-center` 就可以解掉許多問題  
> 只是個人覺得 gnome 太肥，想要用些 light weight 的 packages  
> 覺得麻煩的人可以直接裝個 gnome-control-center ，然後再視情況安裝需要的東西  
> 應該可以節省一些時間  
  
# Post-Install  
+ <https://wiki.archlinux.org/index.php/MacBook#Post-installation>  
+ <https://wiki.archlinux.org/index.php/General_recommendations>  
+ Install [yaourt](https://aur.archlinux.org/packages/yaourt/)  
    + `sudo mkdir /var/cache/yaourt`  
    + save tarball to `/var/cache/yaourt`  
```  
/etc/yaourtrc  
---  
EXPORT=1  
EXPORTDIR="/var/cache/yaourt"  
```  
  
  
## Configs  
### dotfiles  
Download my dotfiles on <https://github.com/M157q/dotfiles>  
```sh  
git clone https://github.com/M157q/dotfiles  
cd dotfiles  
make install  
```  
  
  
### Xorg  
+ `sudo pacman -S xcompmgr xorg-xrdb`  
    + [xcommpgr](https://wiki.archlinux.org/index.php/Xcompmgr)  
        + for simple effect, like transparency in `guake`  
    + [xorg-xrdb](https://wiki.archlinux.org/index.php/X_resources)  
        + for `.Xresources`, some config related to X Window  
  
  
### Wi-Fi  
不同型號的網卡會有不同的問題，這部份也需要多加注意。  
光是參考 <https://wiki.archlinux.org/index.php/MacBook#Wi-Fi> 可能不夠  
必須再自行找些相關資料，我在這部份卡了一陣子。  
  
先確認是哪張網卡  
`MacBookAir6,2` 沒意外的話應該都是 `BCM4360` 這張  
但還是有細節得注意  
  
```  
$ lspci -vnn |grep 0280  
03:00.0 Network controller [0280]: Broadcom Corporation BCM4360 802.11ac Wireless Network Adapter [14e4:43a0] (rev 03)  
```  
  
`Broadcom BCM4360` 這張網卡有兩種  
一種是 `14e4:43a0`, 另外一種是 `14e4:4360`  
根據 <https://wireless.wiki.kernel.org/en/users/Drivers/b43?highlight=%28b43%29#Supported_devices>  
`43a0` 這張是被 wl 驅動程式支援的，所以如果是這張的話可以用無線網路  
`4360` 這張則是不被支援的，所以可能需要另外購買無線網卡  
(我沒有親自測試過，如果有勇者或是有經驗的人歡迎回覆告知)  
  
`43a0` 的話照著底下的指令做應該就可以使用無線網路連網了 (kernel 為 Linux 4.1.5-1)  
  
+ `yaourt -S broadcom-wl-dkms`  
    + after installation, follow the postinstall instructions.  
+ `sudo pacman -S iw`  
+ `sudo pacman -S wicd-gtk`  
  
```  
==> You need to restart the dbus service after  
==> upgrading wicd.  
==> Disable networkmanager, dhcpcd or other networking  
==> utility and add 'wicd' to your systemd configuration.  
```  
  
記得 `systemctl stop dhcpcd`, `sytemctl disable dhcpcd`,  
`systemcl stop NetworkManager`, `systemctl disable NetworkManager`，  
然後 `systemctl enable wicd`，  
`dhcpcd` 或 `NetworkManager` 都會跟 `wicd` 衝突，  
開著 `dhcpcd` 或 `NetworkManager` 的時候使用 `wicd` 的話，  
會無法使用無線網路連線，  
錯誤訊息也看不出啥端倪，  
我就是卡在這很久 Orz  
  
#### 2017.10.31 更新  
  
```  
Warning: Running multiple network managers will cause problems, so it is important to disable all other network management daemons.  
  
First, stop all previously running network daemons (like netctl, netcfg, dhcpcd, NetworkManager).  
  
Disable any existing network management services, including netctl, netcfg, dhcpcd, and networkmanager. Refer to Systemd#Using units.  
Note: You might need to stop and disable the network daemon instead of netctl, which is a current replacement for network service. If unsure, try disabling both.  
```  
quote from [Wicd - ArchWiki](https://wiki.archlinux.org/index.php/wicd#Initial_setup)  
  
我猜不只 `wicd`，  
其他的 Network Daemon 應該也是同理，  
不要讓他們彼此起衝突。  
  
主要是因為我在這裡是使用 `wicd`  
所以如果沒有把 `dhcpcd` 或 `NetworkManager` 都關掉的話，  
在 `dmesg` 會看到以下相關的錯誤訊息：  
  
```  
[ 6677.574915] ERROR @wl_notify_scan_status :  
[ 6677.574919] wlp3s0 Scan_results error (-22)  
```  
  
```  
[ 6560.346608] ERROR @wl_cfg80211_scan :  
[ 6560.346611] WLC_SCAN error (-22)  
```  
  
```  
[ 6467.860408] ERROR @wl_notify_scan_status :  
[ 6467.860413] wlp3s0 Scan_results error (-22)  
```  
  
詳細請參考為這個問題而寫的新文章  
[用 broadcom-wl-dkms 讓 BCM4360 [14e4:43a0] (rev 03) 能順利在 Arch Linux 中使用](/posts/2017/10/31/make-bcm4360-14e4-43a0-rev-03-work-on-arch-linux-with-broadcom-wl-dkms/)  
  
---  
  
#### Improve DHCP connect init speed  
+ Add below into `/etc/dhcpcd.conf`  
  
```  
# Disable IP ARP checking  
noarp  
```  
  
  
#### Network Proxy Settings  
+ <https://wiki.archlinux.org/index.php/Proxy_settings>  
+ `wicd` has no proxy setting function, I can only set proxy configuration in `Firefox`.(This only works for web browsing)  
+ `networkmanager` can have proxy settings via install plugin `proxydriver`, check [NetworkManager - ArchWiki](https://wiki.archlinux.org/index.php/NetworkManager) for how to setup.  
+ I am kinda `wicd` lover and don't use proxy really often, so I think I'm just ok with it currently.  
+ (Considering write the proxy setting functionality for `wicd`...)  
  
  
### File Manager  
+ `sudo pacman -S pcmanfm`  
  
  
### Keyboard  
+ `sudo pacman -S xorg-xmodmap`  
    + for changing keymap like swap Ctrl and Caps Lock  
+ Check /etc/mkinitcpio.conf if `HOOKS` have `keyboard`, if not, add it then `sudo mkinitcpio -p linux`  
+ fix `~` problem  
    + if you press `~` on the keyboard, it will not print out `~` correctly.  
```  
/etc/modprobe.d/hid_apple.conf  
---  
options hid_apple iso_layout=0  
```  
  
#### Backlight  
+ <https://wiki.archlinux.org/index.php/MacBook#Keyboard_Backlight>  
+ `yaourt -S kbdlight`  
+ `sudo pacman -S xorg-xev`  
    + For chekcing the key value of keyboard  
  
  
### Synaptic (Touchpad)  
+ `sudo pacman -S xf86-input-synaptics`  
    + only basic functions  
or  
+ `yaourt -S xf86-input-mtrack-git`  
    + <https://github.com/BlueDragonX/xf86-input-mtrack>  
    + for OS X like touchpad and flexible configuration  
```  
/etc/X11/xorg.conf.d/10-mtrack.conf  
---  
Section "InputClass"  
    MatchIsTouchpad "on"  
    Identifier      "Touchpads"  
    Driver          "mtrack"  
  
    Option "Thumbsize"      "50"  
    Option "ScrollDistance" "150"  
    Option "Sensitivity"    "0.9"  
    Option "MaxTapTime"     "120"  
    Option "IgnoreThumb"    "true"  
    Option "IgnorePalm"     "true"  
    Option "TapDragEnable"  "false"  
  
    # Natural Scrolling  
    Option "ScrollUpButton"     "5"  
    Option "ScrollDownButton"   "4"  
    Option "ScrollLeftButton"   "7"  
    Option "ScrollRightButton"  "6"  
  
    # Disable tap-to-click  
    # Option "TapButton1" "0"  
    # Option "TapButton2" "0"  
    # Option "TapButton3" "0"  
EndSection  
```  
  
### Bluetooth (Headset)  
+ links  
    + <https://wiki.archlinux.org/index.php/Bluetooth>  
    + <https://wiki.archlinux.org/index.php/Blueman>  
    + <https://wiki.archlinux.org/index.php/Bluetooth_headset>  
+ `sudo pacman -S bluez bluez-utils bluez-libs bluez-firmware blueman pulseaudio-bluetooth pulseaudio-alsa pavucontrol`  
+ `sudo modprobe btusb`  
+ `sudo systemctl enable bluetooth`  
+ `sudo systemctl start bluetooth`  
+ `blueman-manager`  
    + scan, pair, connect  
+ `pavucontrol`  
    + Change sound channel to bluetooth headset  
+ Sometimes the bluetooth device may be blocked  
    + use `rfkill list` to check if it is blocked.  
    + use `sudo rfkill unblock bluetooth` to unblock.  
  
  
  
### Sound  
+ `sudo pacman -S xf86-video-intel alsa-utils`  
    + alsa-utils include alsamixer, amixer  
+ Add the content below to `/etc/asound.conf` //Important  
    + `/etc/asound.conf` should be created after installed `pulseaudio-alsa`  
```  
/etc/asound.conf  
---  
defaults.pcm.card 1  
defaults.pcm.device 0  
defaults.ctl.card 1  
```  
  
  
### awesomewm  
+ `sudo pacman -S awesome vicious`  
+ `cp -r /usr/share/awesome/themes ~/.config/awesome/`  
  
  
### Power Management  
+ <https://wiki.archlinux.org/index.php/Power_management>  
+ <https://wiki.archlinux.org/index.php/MacBookPro11,x#Powersave>  
  
#### ACPI  
+ `sudo pacman -S acpi`  
  
#### Powertop  
+ `sudo pacman -S powertop`  
+ Create `/etc/systemd/system/powertop.service`  
```  
[Unit]  
Description=Powertop Service  
[Service]  
Type=oneshot  
ExecStart=/usr/bin/powertop --auto-tune  
[Install]  
WantedBy=multi-user.target  
```  
+ `sudo systemctl enable powertop.service`  
+ `sudo systemctl start powertop.service`  
  
  
#### cpupower  
+ <https://github.com/torvalds/linux/tree/master/tools/power/cpupower>  
```  
sudo pacman -S cpupower  
sudo systemctl enable cpupower  
sudo systemctl start cpupower  
sudo cpupower frequency-set -g powersave  
```  
  
#### thermald  
+ [01org/thermal_daemon · GitHub](https://github.com/01org/thermal_daemon)  
+ Thermal daemon for Intel Architecture  
```  
yaourt -S thermald  
sudo systemctl enable thermald  
sudo systemctl start thermald  
```  
  
#### Fix the kworker CPU hug  
"kworker" triggers some ACPI interrupts.  
You can use `grep . -r /sys/firmware/acpi/interrupts/` to check.  
For me, `gpe4E` triggered lots of ACPI interruptions.  
So disable it via systemd.  
  
Create `/etc/systemd/system/suppress-gpe4E.service`  
and add the following lines.  
  
```  
[Unit]  
Description=Disables GPE 4E, an interrupt that is going crazy on Macs  
[Service]  
ExecStart=/usr/bin/bash -c 'echo "disable" > /sys/firmware/acpi/interrupts/gpe4E'  
[Install]  
WantedBy=multi-user.target  
```  
  
then enable and start it:  
`sudo systemctl enable suppress-gpe4E.service`  
`sudo systemctl start suppress-gpe4E.service`  
  
#### Enable power save mode on Intel Audio card  
Create new hook:  
`sudoedit /etc/modprobe.d/60-snd-hda-intel.conf`  
and add:  
```  
# Enable Power Saving on Intel HDA Audio  
options snd_hda_intel power_save=1  
```  
  
#### Enable powersaving options for Intel Processor  
Create new hook:  
`sudoedit /etc/modprobe.d/60-i915.conf`  
and add:  
```  
# Experimental options to improve power saving on Intel Graphics  
options i915 enable_rc6=1 enable_fbc=1 lvds_downclock=1  
```  
  
### Suspend problem  
#### Prevent shutdown directly when power button is pressed  
+ <https://wiki.archlinux.org/index.php/MacBookPro11,x#Repurpose_the_power_key>  
+ `/etc/systemd/logind.conf`  
    + `HandlePowerKey=suspend`  
  
#### Disable [Swappiness](https://en.wikipedia.org/wiki/Swappiness)  
  
To save SSD and avoid kswapd using lots of CPU resource on finding available swap when there's no more virtual memory can be used.  
  
+ [kswapd 100% CPU-usage · Issue #219 · igorpecovnik/lib · GitHub](https://github.com/igorpecovnik/lib/issues/219)  
+ <https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/tree/Documentation/sysctl/vm.txt>  
+ `sudo sysctl vm.swappiness=0`  
    + `The kernel will swap only to avoid an out of memory condition, when free memory will be below vm.min_free_kbytes limit. See the "VM Sysctl documentation"`  
    + `sudo sysctl vm.min_free_kbytes=0`  
+ `sudoedit /etc/sysctl.d/99-sysctl.conf`  
    + Add `vm.swappiness=0`  
    + Add `vm.min_free_kbytes=0`  
  
#### Fixing suspend mode  
Use `cat /proc/acpi/wakeup`.  
There's a line saying `XHC1  S3  *enabled  pci:0000:00:14.0`.  
We only want the `LID0  S4  *enabled   platform:PNP0C0D:00` to be enbaled.  
So `sudoedit /etc/udev/rules.d/90-xhc_sleep.rules` and add the follwing lines.  
  
```  
# Disable wake from S3 on XHC1  
SUBSYSTEM=="pci", KERNEL=="0000:00:14.0", ATTR{device}=="0x9c31" RUN+="/bin/sh -c '/bin/echo disabled > /sys$env{DEVPATH}/power/wakeup'"  
```  
  
#### Powersave  
+ [GitHub - Unia/powersave: Linux power save settings, compatible with systemd](https://github.com/Unia/powersave)  
  
```  
/etc/sysctl.d/99-powersave.conf  
---  
# Disable NMI watchdog  
kernel.nmi_watchdog = 0  
  
# laptop_mode is a knob that controls "laptop mode". All the things that are controlled by this  
# knob are discussed in https://www.kernel.org/doc/Documentation/laptops/laptop-mode.txt (Default  
# is 0).  
vm.laptop_mode = 5  
  
# Contains, as a percentage of total available memory that contains free pages and reclaimable  
# pages, the number of pages at which a process which is generating disk writes will itself start  
# writing out dirty data (Default is 20).  
#vm.dirty_ratio = 20  
  
# Contains, as a percentage of total available memory that contains free pages and reclaimable  
# pages, the number of pages at which the background kernel flusher threads will start writing out  
# dirty data (Default is 10).  
#vm.dirty_background_ratio = 10  
  
# This tunable is used to define when dirty data is old enough to be eligible for writeout by the  
# kernel flusher threads.  It is expressed in 100'ths of a second.  Data which has been dirty  
# in-memory for longer than this interval will be written out next time a flusher thread wakes up  
# (Default is 3000).  
#vm.dirty_expire_centisecs = 3000  
  
# The kernel flusher threads will periodically wake up and write `old' data out to disk.  This  
# tunable expresses the interval between those wakeups, in 100'ths of a second (Default is 500).  
vm.dirty_writeback_centisecs = 1500  
```  
  
```  
/etc/udev/rules.d/50-powersave-brightness.rules  
---  
# Display Power Management Signaling  
SUBSYSTEM=="power_supply", ENV{POWER_SUPPLY_ONLINE}=="0", ENV{DISPLAY}="DPY", ENV{XAUTHORITY}="/home/USER/.Xauthority", RUN+="/usr/bin/xset dpms 120 240 360"  
SUBSYSTEM=="power_supply", ENV{POWER_SUPPLY_ONLINE}=="1", ENV{DISPLAY}="DPY", ENV{XAUTHORITY}="/home/USER/.Xauthority", RUN+="/usr/bin/xset dpms 300 450 600"  
```  
  
```  
/etc/udev/rules.d/50-powersave-suspend.rules  
---  
# Suspend when battery is at 2%  
SUBSYSTEM=="power_supply", ATTR{status}=="Discharging", ATTR{capacity}=="2", RUN+="/usr/bin/systemctl suspend"  
```  
  
  
### Monitor  
#### Dual Display  
+ <https://wiki.archlinux.org/index.php/Multihead>  
+ `sudo pacman -S xorg-xrandr`  
    + <https://wiki.archlinux.org/index.php/Xrandr>  
    + xrandr should work.  
+ For more friendly GUI setting, `sudo pacman -S lxrandr`  
  
##### But my 1920x1080 external display only get 1024x768 support  
+ <https://wiki.archlinux.org/index.php/Xrandr#Adding_undetected_resolutions>  
  
```  
$ cvt 1920 1080  
# 1920x1080 59.96 Hz (CVT 2.07M9) hsync: 67.16 kHz; pclk: 173.00 MHz  
Modeline "1920x1080_60.00"  173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync  
  
$ xrandr --newmode "1920x1080_60.00"  173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync  
  
$ xrandr --addmode DP1 1920x1080_60.00  
  
$ xrandr --output eDP1 --auto --output DP1 --mode 1920x1080_60.00 --left-of eDP1  
```  
  
##### Hotplug problem - xrandr won't detect hotplug mini-display port to VGA adapter  
+ I'm pretty sure that `udev` indeed detect the hotplug event, but `xrandr` always shows that `DP1`(external VGA monitor) is disconnected.  
+ This can be solved by adding mode for `DP1` (check commands above).  
+ After adding modes, just type `xrandr --output eDP1 --auto --output DP1 --mode ${mode_name} --left-of eDP1` again, even if `xrandr` still shows that `DP1` is disconnected, it works.  
+ So, add all modes we need (1920x1080, 1280x720, 1024x768, ...) can be a workaroud for this problem.  
+ I think the problem is on `xrandr` cannot recongnize whether thunderbolt to VGA adapter is connected or not when hotplug.  
+ Add below to `.xinitrc`  
  
```  
xrandr --newmode "1920x1080_60.00"  173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync  
xrandr --addmode DP1 1920x1080_60.00  
  
xrandr --newmode "1280x720_60.00"   74.50  1280 1344 1472 1664  720 723 728 748 -hsync +vsync  
xrandr --addmode DP1 1280x720_60.00  
  
xrandr --newmode "1024x768_60.00"   63.50  1024 1072 1176 1328  768 771 775 798 -hsync +vsync  
xrandr --addmode DP1 1024x768_60.00  
  
xrandr --output eDP1 --auto --output DP1 --mode 1920x1080_60.00 --left-of eDP1  
```  
  
#### Birghtness  
+ `sudo pacman -S xorg-xbacklight`  
+ `yaourt -S mba6x_bl-dkms`  
    + (2016/12/02 update)  
        + `mba6x_bl-dkms` now depends on `mba6x_bl_dkms-git`  
        + `mba6x_bl-dkms-git-48.055d50d-1` doesn't work with `linux-4.8.11-1`  
        + Need to use `sudo rmmod mba6x_bl` to make `xbacklight` work.  
+ (optional) `yaourt -S lightum-git`  
    + For auto adjust keyboard and monitor birghtness by light sensor  
    + The AUR version has bug, use this fork version <https://github.com/esoleyman/lightum>  
  
### USB  
+ `yaourt -S pmount`  
  
### Fan  
+ <https://github.com/MikaelStrom/macfanctld>  
```  
$ yaourt -S macfanctld  
$ sudo systemctl enable macfanctld  
$ sudo systemctl start macfanctld  
```  
  
  
### IME  
+ `sudo pacman -S gcin`  
+ `sudo pacman -S libchewing`  
    + for chewing input method  
+ `sudo pacman -S anthy`  
    + for Japanese input method  
+ `sudo gtk-query-immodules-2.0 --update-cache`  
  
### Browser  
+ `sudo pacman -S firefox firefox-i18n-zh-tw`  
+ Flash  
    + `sudo pacman -S flashplugin`  
    + <https://addons.mozilla.org/en-US/firefox/addon/flashblock/>  
  
### Fonts  
+ `sudo pacman -S wqy-zenhei adobe-source-han-sans-tw-fonts`  
  
### Mobile  
#### USB-Tethering (Works out of box)  
+ <https://wiki.archlinux.org/index.php/Android_tethering#USB_tethering>  
    + Disconnect from other networks  
    + Connect phone to computer via USB cable  
    + Enable the tethering option from the phone  
    + Use `ip link` and search `usb?` or `enp?s??u?` interface  
    + `sudo dhcpcd ${interface}`  
    + Use `ip link` again to check if already got an ip on that interface  
#### Mount Android phone  
+ <https://wiki.archlinux.org/index.php/MTP>  
+ install `libmtp`, `android-file-transfer`  
  
```  
$ sudo pacman -S libmtp  
$ yaourt -S android-file-transfer  
  
(connect Android phone to Arch Linux via USB)  
  
$ aft-mtp-mount ~/mnt   // mount android to ~/mnt  
$ fusermount -u ~/mnt   // unmount  
```  
  
  
### Webcam  
  
> [UPDATED] see the info below  
>  
> The Facetime HD webcam (included on 2013 MBAs onwards) is no longer UVC device, and therefore, does not work out of the box.  
> It is actually a PCIE device.  
> While [a bcwc_pcie driver is being developed](https://github.com/patjak/bcwc_pcie), it will probably take some time before it is ready.  
> See also [Linux bug #71131](https://bugzilla.kernel.org/show_bug.cgi?id=71131) and [Ubuntu bug #1276711](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/1276811).  
  
+ <https://wiki.archlinux.org/index.php/MacBook#Webcam>  
+ (2017/12/08 update)  
    + [bcwc-pcie-git](https://aur.archlinux.org/packages/bcwc-pcie-git/) on AUR works.  
        + Use `yaourt -S bcwc-pcie-git` or download the tarball and use `makepkg -s` to install it.  
  
  
### Disable MacBook Firmware Boot Sound  
<https://wiki.archlinux.org/index.php/MacBook#Arch_Linux_only>  
  
> The only special consideration is the MacBook firmware boot sound.  
> To ensure that this sound is off: mute the volume in OS X before continuing further.  
  
I forgot to mute the volume before deleting the OS X.  
So, I have to get an OS X installed on USB drive.  
In order to mute the firmware boot sound and for the firmware updating in the furture.  
  
  
### Hotkey Settings  
+ use `xev` to check the keymap  
+ modify `rc.lua` instead using `sxhkd` if you are using awesomewm.  
+ <https://wiki.archlinux.org/index.php/PulseAudio#Keyboard_volume_control>  
+ Add below to the globalkeys in `rc.lua`  
  
```  
-- MacBook Air function keys  
awful.key({ }, "XF86MonBrightnessDown",  
    function ()  
        awful.util.spawn("xbacklight -dec 10")  
    end  
),  
awful.key({ }, "XF86MonBrightnessUp",  
    function ()  
        awful.util.spawn("xbacklight -inc 10")  
    end  
),  
awful.key({ }, "XF86LaunchA",  
    function ()  
        awful.util.spawn("xrandr --output eDP1 --auto --output DP1 --mode 1920x1080_60.00 --left-of eDP1")  
    end  
),  
awful.key({ }, "XF86LaunchB",  
    function ()  
        awful.util.spawn("xrandr --output eDP1 --auto --output DP1 --mode 1920x1080_60.00 --same-as eDP1")  
    end  
),  
awful.key({ }, "XF86KbdBrightnessDown",  
    function ()  
        awful.util.spawn("kbdlight down 10")  
    end  
),  
awful.key({ }, "XF86KbdBrightnessUp",  
    function ()  
        awful.util.spawn("kbdlight up 10")  
    end  
),  
awful.key({ }, "XF86AudioMute",  
    function ()  
        awful.util.spawn("pactl set-sink-mute 0 toggle")  
    end  
),  
awful.key({ }, "XF86AudioLowerVolume",  
    function ()  
        awful.util.spawn("pactl set-sink-mute 0 false")  
        awful.util.spawn("pactl set-sink-volume 0 -5%")  
    end  
),  
awful.key({ }, "XF86AudioRaiseVolume",  
    function ()  
        awful.util.spawn("pactl set-sink-mute 0 false")  
        awful.util.spawn("pactl set-sink-volume 0 +5%")  
    end  
)  
```  
  
  
### Kernel Upgrade  
  
After the kernel upgrade,  
there are no `wl` and `mba6x_bl` modules for the new kernel,  
(Becasue these two modules are in AUR and not supported by the Official.)  
so, we need to rebuild `broadcom-wl-dkms` and `mba6x_bl-dkms` again.  
Otherwise, the wireless interface won't be detected and backlight cannot be tuned while using the new kernel.  
Be sure to download the lastest version of these two packages before reboot to the new kernel.  
Follow the instructions below should work.  
  
```sh  
$ sudo pacman -S linux-headers linux  
  
(after kernel upgarde, download lastest version of these two packages)  
$ yaourt -S broadcom-wl-dkms mba6x_bl-dkms  
$ reboot  
  
(after reboot, rebuild these two kernel modules for the new kernel and load them)  
$ cd /var/cache/yaourt  
$ sudo pacman -U ${broadcom-wl-dkms_package} ${mba6x_bl-dkms_package}  
$ sudo modprobe wl mba6x_bl  
  
$ reboot  //optional  
(reboot again, and make sure that everything goes right.)  
```  
  
+ Upgrade all packages  
    + `yaourt -Syua`  
+ Upgrade all packages (with refetching and recompling all git packages  
    + `yaourt -Syua --devel`  
  
---  
  
## Misc  
  
Below are my personal needed. It's optional.  
<https://wiki.archlinux.org/index.php/List_of_applications>  
  
+ `sudo pacman -S virtualbox virtualbox-host-modules`  
+ `sudo pacman -S unrar`  
  
  
### Network  
+ `sudo pacman -S mosh mtr wget nmap`  
+ `sudo pacman -S dns-tools`  
    + for `dig`  
  
  
### Google Drive  
  
There are lots of 3rd party GNU/Linux clients for Google Drive:  
  
+ <https://github.com/google/skicka>  
+ <https://github.com/odeke-em/drive>  
+ <https://github.com/vitalif/grive2>  
+ <https://github.com/astrada/google-drive-ocamlfuse>  
  
  
#### [skicka](https://github.com/google/skicka)  
Here, I chose `skicka` because some of my friends had already tried it  
and they felt good about it, espcially for the `encrypt` funciton.  
  
To install `skicka` you need to install `go` and `mercurial` first.  
Then, install `skicka`, follow instructions below should work.  
  
```  
$ sudo pacman -S go mercurial  
$ mkdir ~/go  
$ export GOPATH=~/go  
$ export PATH=$PATH:~/go/bin  
$ go get github.com/google/skicka  
$ skicka init  
$ skicka -no-browser-auth ls    // set authentication for skicka  
```  
  
You can check out <https://github.com/google/skicka/blob/master/README.md> for further info.  
  
  
But, after I installed `skicka`, it didn't find all my directories on Google Drive.  
So, I just changed to `drive`  
  
#### [drive](https://github.com/odeke-em/drive)  
use `yaourt -S drive` to install it.  
then `drive init ${dir_for_google_drive}`  
copy and paste the token, then it should work.  
Check <https://github.com/odeke-em/drive/blob/master/README.md> for more info.  
(This command usage is a bit like `git`)  
  
  
### Python  
+ `sudo pacman -S python2 python-pip`  
+ `sudo pip install virtualenvwrapper`  
  
#### Pelican  
+ `pip2 install pelican markdown ghp-import`  
  
  
### GitHub  
+ Add SSH Key  
    + <https://help.github.com/articles/generating-ssh-keys/#platform-linux>  
  
  
### Screenshot  
+ `sudo pacman -S shutter`  
  
  
### Terminal  
+ `sudo pacman -S rxvt-unicode guake`  
  
  
### Monitoring  
+ `sudo pacman -S htop glances lm_sensors`  
    + `sudo sensors-detect`  
  
  
### Multi-Media  
+ `sudo pacman -S eog`  
+ `sudo pacman -S vlc`  
+ `yaourt -S wine-git`  
    + need to uncomment `multilib` in `/etc/pacman.conf` first  
+ `sudo pacman -S playonlinux`  
  
  
### Office  
+ `sudo pacman -S evince`  
    + for .pdf files  
+ `sudo pacman -S libreoffice`  
  
  
## App  
  
+ TweetDeck  
    + `yaourt -S nwjs-bin`  
    + <https://github.com/passcod/twd>  
        + `git clone https://github.com/passcod/twd.git`  
        + `cd twd`  
        + `nw .`  
        + Still buggy and need package on AUR  
+ Slack  
    + <https://github.com/raelgc/scudcloud>  
    + `yaourt -S scudcloud`  
+ Gitter  
    + `yaourt -S gitter`  
+ Facebook Messenger  
    + `yaourt -S messengerfordesktop`  
+ Popcorn-Time  
    + `yaourt -S popcorntime`  
  
---  
  
# References  
+ [MacBook - ArchWiki](https://wiki.archlinux.org/index.php/MacBook)  
    + Arch Linux Only, Dual Boot, Arch Linux + OS X + Windows  
+ [pandeiro/arch-on-air · GitHub](https://github.com/pandeiro/arch-on-air)  
    + Dual Boot  
+ [Mandriva: gcin 無法使用於 firefox, stardic](http://mandriva-usher.blogspot.tw/2014/02/gcin-firefox-stardic.html)  
+ [General recommendations - ArchWiki](https://wiki.archlinux.org/index.php/General_recommendations)  
+ [Beginners' guide - ArchWiki](https://wiki.archlinux.org/index.php/Beginners'_guide)  
+ [xf86-input-mtrack/README.md at master · BlueDragonX/xf86-input-mtrack · GitHub](https://github.com/BlueDragonX/xf86-input-mtrack/blob/master/README.md)  
+ [MacBook - ArchWiki](https://wiki.archlinux.org/index.php/MacBook#Mid_2013_13.22_-_Version_6.2C2)  
+ [List of applications - ArchWiki](https://wiki.archlinux.org/index.php/List_of_applications)  
+ [MacBookAir6-2/Trusty - Community Help Wiki](https://help.ubuntu.com/community/MacBookAir6-2/Trusty)  
+ [Apple Keyboard - ArchWiki](https://wiki.archlinux.org/index.php/Apple_Keyboard)  
+ [Sxhkd - ArchWiki](https://wiki.archlinux.org/index.php/Sxhkd)  
+ [Bluetooth - ArchWiki](https://wiki.archlinux.org/index.php/Bluetooth)  
+ [Bluetooth headset - ArchWiki](https://wiki.archlinux.org/index.php/Bluetooth_headset)  
+ [(=..=)/: skicka: Google drive command line tool](http://xatierlike.blogspot.tw/2015/05/skicka-google-drive-command-line-tool.html)  
+ [MTP - ArchWiki](https://wiki.archlinux.org/index.php/MTP)  
+ [PulseAudio - ArchWiki](https://wiki.archlinux.org/index.php/PulseAudio#Keyboard_volume_control)  
+ [Arch Linux running on my MacBook — Medium](https://medium.com/@PhilPlckthun/arch-linux-running-on-my-macbook-2ea525ebefe3)  
+ [Power management - ArchWiki](https://wiki.archlinux.org/index.php/Power_management)  
+ [MacBookPro11,x - ArchWiki](https://wiki.archlinux.org/index.php/MacBookPro11,x#Powersave)  
+ [GitHub - Unia/powersave: Linux power save settings, compatible with systemd](https://github.com/Unia/powersave)  
