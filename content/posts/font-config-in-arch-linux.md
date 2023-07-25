Title: Font Config in Arch Linux  
Date: 2013-02-16 12:29  
Author: fkz  
Category: Note  
Tags: Linux, Arch Linux, awesomewm, font  
Slug: font-config-in-arch-linux  
Modified: 2015-10-28 15:27  
  
  
漂亮的字型對一個好的使用環境來講真的非常重要  
  
+ 中文字型我慣用 `LiHei Pro`  
+ 英數字型我慣用 `Monaco`  
  
這幾天剛用 awesome window manager  
一直在想辦法讓預設的字型變好看  
  
---  
  
+ 在 `~/.config/awesome/rc.lua` 中，加入 `awesome.font = "LiHei Pro 12"`  
+ 在 `~/.config/awesome/themes/default/theme.lua` 中，加入 `theme.font = "LiHei Pro 10"`  
  
除了這兩個之外 其他以 gtk 開啟的程式預設字型真的很醜= ="  
找了好多篇文章 最後發現應該加上 `~/.fonts.conf` 就行了  
參考了以下這三篇 Archwiki 的 section 之後  
  
1. [Fonts - ArchWiki](https://wiki.archlinux.org/index.php/Fonts#Fallback_font_order_with_X11)  
2. [Font configuration/Examples - ArchWiki](https://wiki.archlinux.org/index.php/Font_configuration/Examples)  
3. [Chromium - ArchWiki](https://wiki.archlinux.org/index.php/Chromium#Font_Rendering)  
  
我的 `~/.fonts.conf` 目前長這樣  
  
```xml  
<?xml version="1.0"?>  
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">  
  
<fontconfig>  
<!-- set font -->  
<alias>  
<family>serif</family>  
<prefer>  
<family>Monaco</family>  
<family>LiHei Pro</family>  
</prefer>  
</alias>  
  
<alias>  
<family>Sans-serif</family>  
<prefer>  
<family>Monaco</family>  
<family>LiHei Pro</family>  
</prefer>  
</alias>  
  
<alias>  
<family>monospace</family>  
<prefer>  
<family>Monaco</family>  
</prefer>  
</alias>  
  
<!-- Chromium fonts rendering from archwiki-chromium -->  
<match target="font">  
<edit name="autohint" mode="assign">  
<bool>true</bool>  
</edit>  
<edit name="hinting" mode="assign">  
<bool>true</bool>  
</edit>  
<edit mode="assign" name="hintstyle">  
<const>hintslight</const>  
</edit>  
</match>  
  
<!-- make the font looks perfect from  
tps://wiki.archlinux.org/index.php/Font_Configuration/fontconfig_Examples -->  
<match target="font" >  
<edit mode="assign" name="autohint">  <bool>true</bool></edit>  
<edit mode="assign" name="hinting">   <bool>false</bool></edit>  
<edit mode="assign" name="lcdfilter"> <const>lcddefault</const></edit>  
<edit mode="assign" name="hintstyle"> <const>hintslight</const></edit>  
<edit mode="assign" name="antialias"> <bool>true</bool></edit>  
<edit mode="assign" name="rgba">      <const>rgb</const></edit>  
</match>  
  
<match target="font">  
<test name="pixelsize" qual="any" compare="more"><double>15</double></test>  
<edit mode="assign" name="lcdfilter"><const>lcdlight</const></edit>  
<edit mode="assign" name="hintstyle"><const>hintnone</const></edit>  
</match>  
  
<match target="font">  
<test name="weight" compare="more"><const>medium</const></test>  
<edit mode="assign" name="hintstyle"><const>hintnone</const></edit>  
<edit mode="assign" name="lcdfilter"><const>lcdlight</const></edit>  
</match>  
  
<match target="font">  
<test name="slant" compare="not_eq"><double>0</double></test>  
<edit mode="assign" name="hintstyle"><const>hintnone</const></edit>  
<edit mode="assign" name="lcdfilter"><const>lcdlight</const></edit>  
</match>  
</fontconfig>  
```  
  
結果這些都弄完了以後 發現有些地方還是沒改到...  
  
![Error](/files/font-config-in-arch-linux/error.png)  
  
這我真的不知道要怎麼改了Orz  
  
---  
  
## References  
  
+ [Fonts - ArchWiki](https://wiki.archlinux.org/index.php/Fonts#Fallback_font_order_with_X11)  
+ [Font configuration/Examples - ArchWiki](https://wiki.archlinux.org/index.php/Font_configuration/Examples)  
+ [Chromium - ArchWiki](https://wiki.archlinux.org/index.php/Chromium#Font_Rendering)  
