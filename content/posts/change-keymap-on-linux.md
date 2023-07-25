Title: Linux 上如何透過指令更改鍵盤鍵位  
Slug: change-keymap-on-linux  
Date: 2018-01-01 23:59:37  
Authors: fkz  
Category: Note  
Tags: Linux, Keymap, xmodmap, setxkbmap, X Window, 2018 iT 邦幫忙鐵人賽  
Summary: 之前都是用 `xmodmap` 來改鍵位，但在遇到不同鍵盤的時候就得使用不同的設定檔，覺得很麻煩，於是就花了點時間查詢有沒有其他更簡單的方法，利用這篇文章紀錄。  
Modified: 2018-01-02 22:17:41  
  
  
## TL;DR  
  
+ `setxkbmap -option ctrl:swapcaps -option altwin:swap_alt_win`  
    + [dotfiles/swap_win_keyboard_layout.sh at master · M157q/dotfiles · GitHub](https://github.com/M157q/dotfiles/blob/master/swap_win_keyboard_layout.sh)  
+ `setxkbmap -option ctrl:swapcaps`  
    + [dotfiles/swap_mac_keyboard_layout.sh at master · M157q/dotfiles · GitHub](https://github.com/M157q/dotfiles/blob/master/swap_mac_keyboard_layout.sh)  
  
---  
  
## 前言  
  
這邊提到的都會是在 X Window 環境下的設定方式為主，這是我目前正在使用也確定可行的方法。非 X Window 的環境下則是放在補充，但因為這部份我沒有親自試過，所以僅供參考。  
  
之前都是用 `xmodmap` 這個指令，搭配一份已經預先寫好的設定檔：[dotfiles/Xmodmap at master · M157q/dotfiles · GitHub](https://github.com/M157q/dotfiles/blob/master/Xmodmap)，讓 `xmodmap` 去執行這份設定檔，它會依照設定檔把鍵位更換掉。但因為我有時候是使用 Mac Book Air 的 Mac 鍵盤，有時候是外接 Filco 的鍵盤，差別最大的地方在於左下角。Mac 的鍵盤會多了一顆 Command 鍵，然後在桌面環境下，無論是我之前使用的 AwesomeWM 或是現在使用的 i3wm，在使用 Mac 鍵盤的時候會以 Command 鍵來當作 Mod4 鍵，但在非 Mac 鍵盤上，則會以 Win 鍵來當作 Mod4 鍵。  
  
問題就在於我已經習慣 Mac 鍵盤上的設定，覺得 Mod4 鍵在空白鍵的左邊比較順手，如果使用非 Mac 鍵盤的話，Mod4 鍵則會在空白鍵左邊的左邊，按起來比較抝手。所以針對不同的鍵盤我得有不同鍵位的改變設定，讓我的操作習慣一致。  
  
之前就覺得 `xmodmap` 的設定檔有點冗長，我只是要單純切換 CapsLock 和左邊的 Ctrl 鍵就要 6 行，等於是我要寫另外一份設定檔，加上我去看了設定檔的文件，覺得挺麻煩的，我也常常搞混。於是就花了點時間找尋看看有沒有比較方便的方式，後來找到 `setxkbmap` 這個指令，可以直接一行指令解決，利用這篇文章紀錄一下。  
  
不管是 Mac 鍵盤上的 Command 鍵，或是非 Mac 鍵盤上的 Win 鍵，在 X Window 的鍵位判定上都會被當作是 "Super" 鍵，即這兩個會被當成是一樣作用的按鈕，但是他們在鍵盤上排列的位置卻不相同：  
  
+ Mac 鍵盤，Command 鍵都是在空白鍵隔壁。  
+ 非 Mac 鍵盤，Win 鍵都是在空白鍵隔壁的隔壁，中間隔著一個 Alt 鍵。  
  
也就是只要我使用非 Mac 鍵盤的話，我就會需要把 Super 鍵和 Alt 鍵對調。  
  
---  
  
## 正文  
  
首先當然是得安裝 `setxkbmap` 這個程式，如果是使用 Arch Linux 的話，可以用以下指令安裝：  
`sudo pacman -S xorg-setxkbmap`  
  
安裝好了之後，使用方式也很簡單，就只要一行指令就行，然後每一個設定就使用 `-option` 參數來設定，有三個設定就會有三個 `-option`。切換的規則可以在 `/usr/share/X11/xkb/rules/base` 找到，我覺得名稱還算好懂，但裏面其實有滿多規則的，這篇文章裏面不會一一介紹，只會講到我有用到的。  
  
舉例來說，如果我要單純把 Ctrl 和 CapsLock 對調的話，就使用以下指令：  
`setxkbmap -option ctrl:swapcaps`  
  
如果要把 Ctrl 和 CapsLock 對調還要把 Alt 和 Win 鍵對調的話，就使用以下指令：  
`setxkbmap -option ctrl:swapcaps -option altwin:swap_alt_win`  
  
可以透過 `-device` 這個參數來做到只針對特定的鍵盤來更改鍵位，不會同時更 MacBook Air 本身的鍵盤和 USB 外接鍵盤。至於這個參數要接的 device id 則可以透過 `xinput` 這個指令來察看。而原先使用的 `xmodmap` 則貌似無法針對個別鍵盤來做設定。  
  
但每次要從已經更改後的鍵位，換到另外一個更改鍵位的時候，不能直接使用指令切換，而是得先用 `setxkbmap -option` 來重置鍵位，然後才能再下另外一個指令來切換到另外一種鍵位，因為 `setxkbmap` 預設是會繼續新增 `-option` 到目前的設定，這也是為什麼我上面自己整理的兩個 script 的第一行都要先用 `setxkbmap -option` 的原因。如果不這樣做的話，可能會出現很奇怪的狀況，這點是要注意的。在 `man setxkbmap` 裡頭關於 `-option` 的說明部份也有提到這點：  
  
![setxkbmap-option](/files/change-keymap-on-linux/setxkbmap-option.jpg)  
  
---  
  
## 補充：xkbcomp  
  
其實在 X Window 底下，除了使用 `xmodmap` 和 `setxkbmap` 兩個指令以外，還有一個 `xkbcomp` 指令可以使用，但因為我覺得這個指令還是沒有 `setxkbmap` 來得方便，所以後來沒有採用。`xkbcomp` 一樣可以透過 `-i` 來針對個別鍵盤做設定，而 device id 也是一樣透過 `xinput` 這個指令來察看。  
  
有關於 `xkbcomp` 的設定：  
  
+ 簡單的範例可以參考這篇文章：[Remap/change your secondary/usb keyboard keys – Linux, Apache, MySQL, PHP, Javascript](https://lampjs.wordpress.com/2015/06/26/remapchange-your-secondaryusb-keyboard-keys/)。  
+ 詳細一點的可以參考 ArchWiki：[X KeyBoard extension - ArchWiki](https://wiki.archlinux.org/index.php/X_KeyBoard_extension#Multiple_keyboards)  
  
---  
  
## 補充：在無 X Window 的 virtual console 環境下切換鍵位  
  
其實也有找到方法，在這篇文章有提到：[EmacsWiki: Moving The Ctrl Key](https://www.emacswiki.org/emacs/MovingTheCtrlKey#toc7)，可以使用 `dumpkeys` 和 `loadkeys` 這兩個指令來辦到，但目前沒有強烈需求，如果哪天真的有在非 X Window 的環境下做到這件事不可的動機的話，應該就會花點時間來設定，看起來其實也是以下這樣的步驟，只是是在非 X Window 的環境下使用：  
  
1. 用 `dumpkeys` 匯出鍵位設定檔  
2. 修改設定檔  
3. 再用 `loadkeys` 匯入鍵位設定檔  
  
  
---  
  
## 參考來源  
  
+ [How to remap keys under Linux for a specific keyboard only - Super User](https://superuser.com/questions/760602/how-to-remap-keys-under-linux-for-a-specific-keyboard-only)  
+ [A one line command to remap the CapsLock key to Ctrl : linux](https://www.reddit.com/r/linux/comments/1kyikn/a_one_line_command_to_remap_the_capslock_key_to/)  
+ [keyboard - How do I remap the Caps Lock and Ctrl keys? - Ask Ubuntu](https://askubuntu.com/questions/33774/how-do-i-remap-the-caps-lock-and-ctrl-keys)  
+ [CapsLock Remap Howto - Noah.org](http://www.noah.org/wiki/CapsLock_Remap_Howto)  
	+ 這篇也算是篇滿完整的文章，重點是它是個人用 Wiki 的頁面，覺得很厲害。  
+ [Remap/change your secondary/usb keyboard keys – Linux, Apache, MySQL, PHP, Javascript](https://lampjs.wordpress.com/2015/06/26/remapchange-your-secondaryusb-keyboard-keys/)。  
+ [X KeyBoard extension - ArchWiki](https://wiki.archlinux.org/index.php/X_KeyBoard_extension#Multiple_keyboards)  
+ [EmacsWiki: Moving The Ctrl Key](https://www.emacswiki.org/emacs/MovingTheCtrlKey#toc7)  
