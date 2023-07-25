Title: 讓 gpg-agent 在 git commit gpg-sign 時使用 pinentry-curses  
Slug: make-gpg-agent-use-pinentry-curses-while-git-commit-gpg-sign  
Date: 2017-01-20 13:21:09  
Authors: fkz  
Category: Note  
Tags: cli, gpg, pinentry, git  
Summary: 最近用 Arch Linux 升上 4.8.13 後，X window 跑一跑會突然 crash，重開之後會抓不到 X window 的 output 變數，導致平常 git commit 在 gpg-sign 時，gpg-agent 預設使用的 pinentry-gtk2 會開不起來，讓 git commit 無法順利使用 gpg-sign，所以找一個不用開 gtk 視窗起來的方法。  
  
  
## 前言  
  
git 使用 gpg sign 預設的 gpg-agent 會是 pinentry-gtk2  
最近把 Arch Linux 筆電升上 Linux 4.8.13 後  
X server 好像有 Buffer Overflow 還是 Garbage collection 沒做好的問題  
跑一陣子就會跳掉  
重新 `startx` 還是可以動  
但會抓不到 x window 的 output 變數  
導致 git commit 在作 gpg sign 時  
叫不出 `pinentry-gtk2` 所以無法輸入 passpharse  
直接噴  
  
```  
error: gpg failed to sign the data  
fatal: failed to write commit object  
```  
  
所以就想說找找看有沒有可以在 terminal 裏面就解決  
不用開 gtk 的方法  
嗯 果然是有的  
  
---  
  
## 解法  
  
### 設定檔  
  
在 `~/.gnupg/gpg-agent.conf`  
（沒有這個 conf 的話就建一個，記得要 chmod 一下）  
  
加入一行  
`pinentry-program /usr/bin/pinentry-curses`  
（記得確認 `pinentry-curses` 已經安裝且路徑正確，否則請安裝並自行修改到正確路徑）  
  
### 重新載入  
  
之後讓 gpg-agent 重新載入，使用新的 pinentry-program  
`gpg-connect-agent reloadagent /bye`  
  
### 設定變數  
  
然後因為 `pinentry-curses` 會需要用到 `$GPG_TTY` 這個變數  
所以請在自己使用的 .shellrc 裡頭加入  
  
```  
# Set GPG_TTY for pinentry-curses  
export GPG_TTY=$(tty)  
```  
  
### 打完收工  
  
沒意外的話這樣就行了  
在原本的 shell 重新 source 一次修改好的 rc 檔  
或是直接開啟一個新的 shell  
確認有 `GPG_TTY` 這個參數  
之後用 git commit 在做 gpg sign 的時候  
就可以直接在 terminal 裏面打 passphrase 了  
不需要用到 GTK 和 X window 啦  
  
---  
  
## Reference  
  
+ [GnuPG - ArchWiki](https://wiki.archlinux.org/index.php/GnuPG#Configuration_2)  
