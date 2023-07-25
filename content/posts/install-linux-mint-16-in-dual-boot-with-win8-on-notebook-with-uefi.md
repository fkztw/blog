Title: Install Linux Mint 16 in Dual Boot with Win8 on Notebook with UEFI  
Date: 2014-02-21 03:00  
Author: fkz  
Category: Note  
Tags: Linux, Linux Mint, Win8, UEFI, Dual Boot  
Slug: install-linux-mint-16-in-dual-boot-with-win8-on-notebook-with-uefi  
Modified: 2015-10-26 13:53  
  
  
有人不會裝，又剛好自己沒有在 UEFI 系統的 Win8 筆電上灌 Linux 的經驗，就想說來試試看。  
(之前嘗試要幫人把 UEFI 系統的 Win8 灌成 Win7 失敗後，就覺得 UEFI + Win8 很難搞)  
  
這次灌完後仍然覺得很討厭，所以紀錄一下方法。  
  
前面一直到 LiveUSB 成功開啟的部份應該其他 Linux Distribution 的安裝也適用吧？  
  
因為沒試過，所以只是猜測。  
  
以下簡要紀錄過程  
  
---  
  
1. 到 [Mint 官方網站](http://www.linuxmint.com/) 下載 Image 檔  
    + [Download Linux Mint Latest Version](http://www.linuxmint.com/download.php)  
        + 自行選擇 Window Manager 和符合的位元版本  
    + 將 .iso 檔製作成 LiveUSB  
2. 清出一個 Unallocated 的磁區給 Mint 安裝用  
3. 插入 Mint16 的 LiveUSB，要讓 Win8 讀到，待會要進 UEFI 調整開機順序  
4. 把 Windows 的 Fast Boot 關掉  
    + Fast Boot 預設載入 Windows Kernel，如果沒關掉的話，用 LiveUSB 開機，進到 GRUB 選擇 Mint 開機後就會進入黑屏。  
    + 步驟  
        1. 點選 Win8 桌面側欄的「設定」  
        2. 點選最下方的「變更電腦設定」  
        3. 點選左方側欄的「一般」  
        4. 右方側欄拉到最下方，點選進階啟動中的「立即重新啟動」  
        5. 出現畫面後，選擇「疑難排解」  
        6. 點選「進階選項」  
        7. 點選「UEFI韌體設定」  
        8. 點選「重新啟動」，之後電腦會重開機進入 UEFI 設定介面  
        9. Boot 中的 Fast Boot 用空白鍵更改為 Disabled  
        10. 將底下的 Boot Options Priorites 調整為 LiveUSB 為第一個  
        11. 按 F10 Save & Exit -> Yes  
5. 重開機後，應該就會進入 LiveUSB 中  
6. 其他就參考 References 部分的第一篇文章，照著 Mint 的安裝流程安裝  
    + 切 /, /swap, /home  
  
---  
  
## Refereneces  
  
+ [Guide To Install Linux Mint 16 In Dual Boot With Windows](http://itsfoss.com/guide-install-linux-mint-16-dual-boot-windows/)  
+ [Black screen when boot from liveUSB to install Linux Mint 16](http://forums.linuxmint.com/viewtopic.php?f=46&t=155164)  
+ (dead) [Booting Linux Mint 16 from Live USB fails in initramfs](http://forums.linuxmint.com/viewtopic.php?f=46&t=159972)  
+ [《SOLVED》Black screen before installation, Mint 16](http://forums.linuxmint.com/viewtopic.php?f=46&t=153074)  
