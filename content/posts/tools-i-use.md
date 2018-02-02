Title: 我平常在電腦上用了哪些程式  
Slug: tools-i-use  
Date: 2018-01-09 22:09:55  
Authors: m157q  
Category: Note  
Tags: Tools, M157q, 2018 iT 邦幫忙鐵人賽  
Summary: 紀錄一下自己平常使用了哪些工具，給自己之後檢視用。  
Modified: 2018-02-02 18:17:55  
  
  
## 前言  
  
身為一個懶人，不喜歡做重複的事情，所以愛寫程式來把重複的事情解決掉，也因為這樣，所以很常用一些工具來幫助自己節省時間，以提高自己的生產力。  
  
想說利用待業這段比較有空的時間，拿這篇文章來詳細紀錄一下自己目前到底用了哪些工具，留個紀錄，之後也可以用來追蹤比較，看看自己之後換了工具的原因，以及是不是真的有比較好。也有可能會變成歷史文，見證什麼時代的眼淚之類的吧（？）  
  
身為一個寫程式的阿宅，平常都是用電腦居多，所以這篇只會以電腦用到的部份為主。格式分類參考自一年多前看到的這篇文章：[My Software Stack – Hungys.blog() – Medium](https://medium.com/hungys-blog/my-software-stack-2a406c1c57c1)  
  
---  
  
## OS & VM & VPS  
  
+ [Arch Linux](https://www.archlinux.org/)  
    + 從 2012 年用到現在，算一算也有個 5~6 年了，真的覺得是個很棒的作業系統。（在這之前是使用 Ubuntu。）  
    + 預設乾乾淨淨，想要裝什麼都自己決定，可以用 pre-compiled package 也可以自己編譯，自訂性挺高的。  
    + 最棒的還是 Rolling Update 的特性，遇到一些安全性的更新都可以馬上更新，雖然剛開始用的時候會遇到升上去就爛掉的問題，但這幾年已經很少遇到了。  
    + [2015 年 9 月後，直接把 Arch Linux 安裝在 MacBook Air Mid 2013 上使用。](https://blog.m157q.tw/posts/2015/09/10/install-arch-linux-on-macbook-air-mid-2013/)  
+ [Virtual Box](https://www.virtualbox.org/)  
    + 也是個用了很久的 Virtual Machine Manager，支援 Linux 使用，但近幾年開始使用 VPS 之後就沒那麼常用了。  
    + 以前在使用的時候有遇到些問題，分別寫了幾篇文章紀錄：  
        + [Boot LiveUSB in VirtualBox 4.3.18 | Just for noting](https://blog.m157q.tw/posts/2014/12/04/boot-liveusb-in-virtualbox-4-3-18/)  
        + [VirtualBox Guest additions upgrade: install_x11_startup_app: no script given | Just for noting](https://blog.m157q.tw/posts/2014/11/10/virtualbox-guest-additions-upgrade-install_x11_startup_app-no-script-given/)  
        + [Solution for the Failure to Attach USB Device in VirtualBox | Just for noting](https://blog.m157q.tw/posts/2014/10/16/solution-for-the-failure-to-attach-usb-device-in-virtualbox/)  
            + 這篇不知道為什麼流量莫名的高，可能很多人都有遇到這問題？  
+ [Kali Linux](https://www.kali.org/)  
    + 從它以前還叫作 [BackTrack Linux](https://backtrack-linux.org/) 的時候就有在用了。  
    + 大學有陣子在碰資安相關的東西，所以會拿來做一些資訊安全相關的測試，最近幾年也比較少用了。  
+ [Digital Ocean](https://www.digitalocean.com/)  
    + 大概 2015 年開始使用的，但真正開始使用是在工作後，因為在學校沒主機了，所以就租個 VPS 來用，每個月 10 美金，算滿夠用的。  
    + 雖然貌似比 Linode, Vultr 還貴，但使用上也沒啥太大的問題，所以也懶得換了就是。  
        + 結果才過沒幾天，2018/01/17 Digital Ocean 就推出了新方案，一個月 10 美金變成有 2 GB RAM, 1 vCPU, 50 GB SSD, 2TB Bandwidth，直接變得比 Linode 和 Vultr 還便宜了：[Kicking Off the New Year with New Droplet Plans](https://blog.digitalocean.com/new-droplet-plans/)  
    + 這間公司的文件都寫得滿用心的，因為有專門聘請寫手來寫，滿推薦的。  
    + 拿來放些自動化的程式，例如：  
        + [批踢踢每天定時登入](https://gist.github.com/M157q/ad375e227ec0f1ba450915df65433473)  
        + [一個每小時爬 RSS feed 然後發 Tweet 的 Twitter Bot](https://twitter.com/M157q_News_RSS)  
        + 之前寫[批踢踢網頁版爬蟲](https://github.com/M157q/ptt_statistics)時有放在上面跑  
        + 之前找租屋處的時候，寫了一個 [591 租屋網的爬蟲](https://github.com/M157q/5g1)也有放在上面跑。  
+ [Parsec](https://parsecgaming.com)  
    + 最近幾天才開始使用的 Cloud Gaming service，確定可以在上面直接用 Steam 玩遊戲，Linux 也可以使用。  
    + 可以讓你像 Steam In-Home 一樣設定自己的主機，也可以直接讓你租 AWS 或 Paperspace 的 GPU 主機來用，費用我覺得算 OK，依照分鐘收費。  
    + 租用雲端主機適合沒辦法或沒錢或沒地方或不想組 Windows 遊戲主機的人使用，但網路速度要夠快，不然 latency 可能會有點高。  
  
---  
  
## Editors  
  
+ [Vim](http://www.vim.org/)  
    + 大概從 2008 年開始用到現在，赫然發現也快 10 年了。  
    + 搭配 `Vundle` 來安裝 Plugin，詳細的設定可以參考這個設定：<https://github.com/M157q/dotfiles/blob/master/vimrc#L95-L179>  
+ [Atom](https://atom.io/)  
    + Open Source 的 Text editor，有時候會開來用。  
    + 有滿多的 plugin 可以裝的，但我沒有裝。之前最有名的應該是 [activate-power-mode 這個 plugin](https://atom.io/packages/activate-power-mode) 吧  
+ [Visual Studio Code](https://code.visualstudio.com/)  
    + <https://github.com/Microsoft/vscode>  
    + 微軟出的 Open Source edtior，有時候會開來用。  
    + 基本上我覺得是抄 atom 的就是，但有多出更多功能。  
    + 有一個我最喜歡的功能是可以在 editor 裡頭直接開 terminal 來用，我覺得很方便，然後[這個功能是一位台灣人去提的](https://github.com/Microsoft/vscode/issues/143)。  
  
---  
  
## Terminal  
  
+ [urxvt-unicode](https://www.gnu.org/software/bash/)  
    + 一款 terminal emulator，類似 macOS 上的 iTerm 或 iTerm2。  
    + 搭配這份設定檔：<https://github.com/M157q/dotfiles/blob/master/Xresources>  
+ [Zsh](https://www.zsh.org/)  
    + 以前是使用 bash，後來預設的 shell 改成 zsh，主要是補完功能以及支援非 ASCII 比較完整。  
    + 搭配 [oh-my-zsh](http://ohmyz.sh/) 針對不同的 OS 安裝不同的 plugins 來使用，設定檔在這：<https://github.com/M157q/dotfiles/blob/master/zshrc>  
+ [Bash](https://www.gnu.org/software/bash/)  
    + 基本上寫 shell script 還是會寫 bash 就是，管 server 的時候大多數 Linux server 也都是 bash。  
  
---  
  
## CLI Tools  
  
+ [screen](https://www.gnu.org/software/screen/) & [tmux](http://bxr.su/OpenBSD/usr.bin/tmux/)  
    + 這兩個指令基本上拿來做相同的事，可以在一個 terminal 裏面開多個分頁。  
    + 除了方便管理以外，在遇到某些程式要跑很久的時候也很好用，可以把該程式掛在某個分頁，然後再另外開一個分頁去做其他事，不用等到程式跑完。  
    + screen 和 tmux 各有擁護者，偶爾會見到兩派使用者開戰。  
    + 但我自己是開 screen 再在每個 screen 的分頁裏面開 tmux，這樣我覺得很好管理，比如說在不同的 project 開發的話，我就會一個 project 用一個 screen。因為如果在 screen 裏面再開 screen 或 tmux 裏面再開 tmux 的話，會沒辦法控制到裏面那層。  
+ [htop](https://hisham.hm/htop/)  
    + 可以拿來監控系統資源的工具  
    + 我通常都是開著掛在 `tmux` 的第一個分頁  
+ [speed-test](https://github.com/sindresorhus/speed-test)  
    + 直接在 CLI 測網路速度，不用開 SpeedTest 的網頁，挺方便的。  
+ [ag](https://geoff.greer.fm/ag/)  
    + 名字叫 The Silver Searcher  
    + 類似 `grep` 和 `ack` 的工具，但效能比較好，要下指令也很方便，只有 `ag` 兩個字。  
+ [virtualenv](https://virtualenv.pypa.io/en/stable/) + [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)  
    + 因為很常用 Python，然後裝東西的時候又不想影響到系統用的 Python，所以就會使用 virtualenv 來把環境隔開。  
    + 搭配 virtualenvwrapper 可以用更簡單的指令一次處理數個 virtualenv 的指令，挺方便的。  
    + 例如要新增一個新的 virtualenv 的話，只要 `mkvirtualenv py2 --python=python2` 這樣就行了。  
    + 我自己基本上都是切成 `py2`, `py3` 來使用，然後各個用 Python 的專案也都會有各自的 virutalenv。  
+ [wicd & wicd-curses](http://wicd.sourceforge.net/)  
    + wicd 的 CLI 介面，我都用這個來選擇無線網路。  
    + 如果是圖形化介面的話則有 wicd-gtk 可以使用。  
+ [NetworkManager](https://developer.gnome.org/NetworkManager/) & [nmcli](https://developer.gnome.org/NetworkManager/stable/nmcli.html) & [nmtui](https://developer.gnome.org/NetworkManager/stable/nmtui.html)  
    + wicd 遇到會重導向到 Login 頁面的 Public Wi-Fi 常常會連 IP 都拿不到，但 NetworkManager 往往對付這種 Public Wi-Fi 都可以順利拿到 IP，所以我會在這時候使用 `nmcli` 或 `nmtui` 去操控 NetworkManager。  
+ [alsamixer](http://www.alsa-project.org/main/index.php/Main_Page)  
    + 可以用來調整 ALSA 裝置的音量，操控挺容易的，也有基於文字的圖形化介面。  
+ [bluetoothctl](https://wiki.archlinux.org/index.php/Bluetooth)  
    + 可以用指令來管理藍牙裝置  
+ [youtube-dl](https://github.com/rg3/youtube-dl/)  
    + <http://rg3.github.io/youtube-dl/>  
    + 下載影片跟音樂的神器  
+ [pidof](https://blog.longwin.com.tw/2016/12/linux-pidof-get-sub-process-id-2016/)  
    + 因為這篇文章才知道的：[使用 pidof 找出此程式的所有 process id - Tsung's Blog](https://blog.longwin.com.tw/2016/12/linux-pidof-get-sub-process-id-2016/)  
    + 以前找 process 都要用 `ps aux | grep xxx` 來找，用這個指令的話只要用 `pidof xxx` 就行了  
    + Arch Linux User 的話可以用 `sudo pacman -S procps-ng` 來安裝。  
        + 但我發現 `pidof` 之前是被放在不同的 package 裡頭，所以之後有變的話，可以用 `pkgfile pidof` 來找 `pidof` 被包含在哪個 package 裡頭。  
        + 如果沒有 `pkgfile` 這個指令的話，可以透過 `sudo pacman -S pkgfile` 來安裝  
+ [ffmpeg](https://ffmpeg.org/)  
    + 影音轉檔神器，也可以做到裁切、截圖等等的後續處理。  
+ [mtr](https://github.com/traviscross/mtr)  
    + 用來查路由的神器，方便易用，比 `traceroute` 好用。  
+ [mediainfo](https://mediaarea.net/en/MediaInfo)  
    + 用來看圖片或影音檔的 metadata 很方便  
+ [jq](https://github.com/stedolan/jq)  
    + <https://stedolan.github.io/jq/>  
    + 很方便的 CLI JSON processor  
  
---  
  
## GUI Tools  
  
+ [wicd-gtk](http://wicd.sourceforge.net/)  
    + 因為 `wicd-curses` 有些 bug，例如遇到新的且需要輸入密碼的 SSID 時會無法設定密碼，所以偶爾會用到 `wicd-gtk`，顧名思義，就是 GTK 介面的 wicd。  
+ [PulseAudio Volume Control](https://freedesktop.org/software/pulseaudio/pavucontrol/)  
    + 指令為 `pavucontrol`  
    + `alsamixer` 的功能在普通使用下算夠用，但比較複雜的操作就會顯得麻煩了點，這時候 `pavucontrol` 就派上用場了。  
    + 可以把輸出和輸入合併為一個音源，大概就像 macOS 上的 SoundFlower 那樣。  
        + [Linux通过Pulse混合麦克风和音频输出 — Life in a Nutshell](https://wugh.github.io/posts/2015/01/linux-pulse-mix-mic-and-computer-audio/)  
+ [PCManFM](https://wiki.lxde.org/en/PCManFM)  
    + 由台灣人 PCMan 撰寫的開源檔案瀏覽器，嗯，就是那位撰寫瀏覽 BBS 程式 PCMan 的 PCMan （真繞口）  
+ [Chromium](https://www.chromium.org/)  
    + 算是去除了非開放原始碼部份的 Google Chrome，所以整個專案的程式碼都是公開的。  
    + 和 Google Chrome 比起來也比較輕量一些些。  
+ [Firefox Nightly](https://www.mozilla.org/zh-TW/firefox/channel/desktop/)  
    + 2017 年 10 月左右，為了先體驗 Firefox 57 的 Quantum engine 就先裝了，之後就一直使用到現在。  
    + 剛從 Firefox 55 切換過來的時候真的覺得快了不少，但後來因為使用上覺得還是有 Memory Leak 的問題，所以就比較少用了。  
    + 加上最近又出了這個問題：[Firefox is on a slippery slope | Drew DeVault’s Blog](https://sircmpwn.github.io/2017/12/16/Firefox-is-on-a-slippery-slope.html)，所以就換去使用 `qutebrowser` 了。  
+ [qutebrowser](https://qutebrowser.org/)  
    + 一個基於 QtWebEngine 並使用 Python 開發的開源瀏覽器。  
    + 所有的操作基本上都以 Vim 的使用習慣為主，有點類似 `dwb`，很適合我這種 Vim user，畢竟在 Chrome, Chromium, Firefox 上我都有裝 Vimium 這個瀏覽器套件，可以讓我不太需要移動右手去使用滑鼠。  
    + 輕量化瀏覽器，比 Chrome 或 Firefox 都省資源。  
  
---  
  
## Version Control & DevOps  
  
+ [Git](https://git-scm.com/)  
    + 應該不用多說了，算起來從 2012 年開始接觸，也快 6 年了。  
    +  雖然也用過 `svn` 和 `bzr`，但還是覺得比較習慣 `git`。  
    + 現在連寫 blog 都用 `git` 作版本控制了。  
+ [Docker](https://www.docker.com/)  
    + 目前最主流的 Container 格式。  
    + 開源的部份在 2017 年改名叫 Moby 了，但大家還是習慣叫 Docker 就是。  
    + Docker 現在專指這間公司，如果是企業版的話叫作 Docker EE，社群版的話叫作 Docker CE。  
    + 從 2016 年 4 月左右開始接觸，和 Microservices 息息相關。  
+ [Kubernetes](https://kubernetes.io/)  
    + <https://github.com/kubernetes/kubernetes>  
    + Google 出的 Container 管理工具，支援 Docker 和 Rocket，類似 Docker 官方出的 Docker Swarm。  
  
---  
  
## Online Services  
  
+ [Gmail](https://mail.google.com/mail/)  
    + 這應該不用多介紹了，雖然知道隱私會被侵犯得很嚴重，但目前還是離不開。  
    + 之後其中一個計劃應該就是換到自架的 Mail Server 吧。  
+ [Google Calendar](https://calendar.google.com)  
    + 這個應該也不用多做介紹，覺得真的不錯用，尤其以前辦社團活動的時候被成功提醒了不少次。  
    + 無論是個人、分享或團體的時間安排都挺方便的。  
    + 應該就只有比較不適合一次性使用吧。  
    + 雖然有用 iPhone，但還是沒用 Apple 的 Calendar。  
+ [Google Maps](https://maps.google.com)  
    + 這個應該也不用多說了，現在出門去很多人都是靠這個在導航的吧。  
+ [IFTTT](https://ifttt.com)  
    + IFTTT 的意思是："If it, then that."  
    + 和多家公司合作，可以很簡單設定一些跨服務的觸發條件，除了 API 提供的觸發條件以外，還可以在這之上自己撰寫 JavaScript 做一些彈性化的設定。  
    + 每個人也可以分享自己設定的腳本供他人使用，大多數都是用來做一些提醒或是自動備份的事。  
    + 我目前是拿來把我在 Twitter 分享或在 Pocket 儲存一些我覺得不錯的文章時，會幫我自動在：[Issues · M157q/m157q.github.io · GitHub](https://github.com/M157q/m157q.github.io/issues) 開個新的 Issue 紀錄，以方便我日後查詢，解決常常和人分享時想起看過某篇不錯的文章卻搜尋不到的問題。  
+ [Pocket](https://getpocket.com)  
    + 用來將文章暫存以供日後閱讀的服務。  
    + 目前我的使用方式比較像是用來儲存與分類看過的文章，再加上使用了 IFTTT  的關係，說穿了其實就只是不用自己接 API，透過 IFTTT 把我看過的文章存到 GitHub Issues 而已，連搜尋也不太會在 Pocket 作搜尋。  
    + 但因為使用 Pocket 的時間早於我把文章存到 GitHub Issues 的時間，所以一些比較舊的文章還是會來 Pocket 找就是。  
+ [Feedly](https://feedly.com)  
    + 一個不錯用的 RSS Reader，目前就拿來追蹤個人與企業的技術 blog。  
    + 現在免費版的上限好像只能到 100 個來源的樣子，但我自己好像因為比較早使用，所以即便是免費版卻沒有受到這個限制。  
+ [GitHub](https://github.com/)  
    + 基本上自己已經是每天都會使用 GitHub 了。  
    + 目前全球最大的程式碼管理平台，許多開放原始碼的專案都在上面，真的是有很多非常有趣的專案，也可以很輕易得和國外的開發者交流。  
    + 雖然大家私底下好像都戲稱成「全球最大同性交友平台」(ry  
    + 因為一掛掉就會導致很多工程師沒事幹，所以也有不少公司選擇使用 Bitbucket 或是使用 Gitlab 自己架設程式碼管理平台。  
+ [Trello](https://trello.com)  
    + 一套基於「看板」(KanBan) 設計的任務管理平台，可供個人或團體使用。  
    + 我自己是用來紀錄自己做過的事情、幫自己的要做的事排定時間以及快速整理一些新學到的東西，以便之後可能可以整理成一篇文章來紀錄。個人覺得免費版就很夠用了。  
    + 最近這幾天開始使用 KanbanFlow 這套類似的工具，好處應該就是多了個番茄鐘可以幫你紀錄時間，如果是番茄鐘的愛好者且還沒使用過 Trello 的話，可以直接試試看 KanbanFlow。我自己是因為 Trello 已經紀錄不少東西了，要搬挺麻煩了，所以目前是兩個搭配使用。  
+ [Travis CI](https://travis-ci.org)  
    + 一個僅和 GitHub 作整合的 Continuous Integration 平台，目前還是 GitHub 上市佔率最大的 CI 平台。可以參考這篇 2017 年 11 月的文章：[GitHub welcomes all CI tools · GitHub](https://github.com/blog/2463-github-welcomes-all-ci-tools)，列出了 GitHub 上使用的 CI 平台市佔率由多至少依序為：Travis CI, Circle Ci, Jenkins, AppVeyor, CodeShip, Drone, Semaphore CI, Buildkite, Wercker, TeamCity。  
    + 好處是所有 Public repo 都可以免費使用，而且搜尋一下就有很多設定檔可以參考。我目前是用來自動 build 並發佈我的個人部落格：[用 Travis CI 自動化發佈 Pelican blog 到 GitHub Pages 上 | Just for noting](https://blog.m157q.tw/posts/2016/05/08/use-travis-ci-to-publish-pelican-blog-on-github-pages-automatically/)  
+ [CloudFlare](https://www.cloudflare.com)  
    + 2016 年 6 月租了自己的 domain 之後，就拿來個人使用。在這之前是因為公司的服務有在使用，所以才接觸到，覺得設計的很簡單易用且功能又很強大。  
    + DNS 代管設定很方便，而且加上 proxy 之後就有免費的 CDN 和 HTTPS 可以使用。有很多其他的功能，可以設定 Cache、簡單的流量分析、免費的網站資安防護等等等。  
    + 詳細一點的介紹可以參考這篇文章：[買了一個叫作 m157q.tw 的域名 | Just for noting](https://blog.m157q.tw/posts/2016/09/06/i-bought-my-first-domain-name/)  
    + 不過 2017 年 2 月的時候也有出過 CloudBleed 這個大包就是：[Incident report on memory leak caused by Cloudflare parser bug](https://blog.cloudflare.com/incident-report-on-memory-leak-caused-by-cloudflare-parser-bug/)  
+ [Gandi](https://www.gandi.net)  
    + 因為很常出現在台灣的社群會議，所以就在上面租了域名。  
    + 但我覺得使用上沒有很方便，而且因為 DNS 的管理已經被我轉到 CloudFlare 了，所以基本上只有在續租域名的時候才會開啟。  
    + 其他類似的服務有 NameCheap, GoDaddy，GoDaddy 我覺得好用一些，但也沒有認真比較過就是。  
    + 如果要用 Gandi 的服務的話，記得要開啟 "Private Domain Registration" 就是，不然個資直接被人用 `whois` 看光光。  
+ [Slack](https://slack.com)  
    + 就是一個針對團隊協作而開發的平台，台灣不少新創公司與社群都有使用。  
    + 基本上就是功能更多元的 IRC 聊天室，可以整合許多 API，做到 CI, CD 的通知，甚至可以做到 ChatOps。  
    + 只是我沒有很喜歡一個 workspace 就要重新註冊一組帳號密碼的設計，但可以理解為什麼要這樣設計就是。  
+ [Discord](https://discordapp.com)  
    + 最近才開始使用的服務，主要是針對 Gamer 設計的即時語音通訊平台。  
    + 我個人是覺得像是 Slack + RaidCall，可以即時多人語音通訊（無上限），在 2017 年 11 月也開放了和好友視訊通話與螢幕畫面分享的功能（最多 10 人）。  
+ [Medium](https://medium.com)  
    + 一個算新的部落格平台，乾淨簡潔無廣告，採用付費訂閱制，國外已經滿多人使用了，最近台灣也愈來愈多人使用。  
    + 我自己其實沒在使用，因為已經厭倦使用部落格平台了，一旦平台一倒的話要搬文章又是件痛苦的事。追蹤文章也是用 Feedly 去追。  
    + 至於為什麼有辦 Medium 的帳號，主要是有時候想要留言回覆，加上可以使用其他服務登入不用註冊帳號也還算方便，附加功能應該是可以幫別人的文章拍拍手（？）  
+ Social Network Service  
    + Facebook, Twitter, Line, Telegram, LinkedIn, Google+ (?)  
    + 這邊用來紀錄時代的眼淚（？）  
  
---  
  
## Eating My Own Dog Food  
  
+ [zdict](https://github.com/zdict/zdict)  
    + 一個 CLI 的字典查詢工具，預設支援 Linux, FreeBSD 和 macOS，也可以透過 Docker 在 Windows 上面執行。  
    + 預設是使用 Yahoo 字典，也有萌典、Urban Dictionary 等等可以查詢。  
    + 當初是在看美劇的時候常常要查單字，覺得開網頁很麻煩，所以找到了 `ydict`，但不盡理想而且開發者也停止維護了，所以就 fork 出來大改，後來身邊也有幾個朋友加入開發，所以就弄了個 organization。  
    + 現在變成我每天會使用的工具了，之後應該會寫一篇介紹這個工具。  
+ [gettitle](https://github.com/M157q/gettitle)  
    + 寫文章的時候附上參考連結的時候常常不想要只附上網址，而是連網頁標題也一起附上，覺得要自己手動複製很麻煩，所以就寫了個小程式來做這件事。  
    + 使用 Selenium，所以支援使用 JavaScript 的網頁（例如：Dcard），不過也因為這樣所以速度有點慢，但目前是沒有什麼不能等的狀況，所以算是夠用。  
    +  基本上已經是我寫文章的時候必定會使用到的工具了。  
+ [M157q_News_RSS](https://twitter.com/M157q_News_RSS)  
    + 一個每小時發科技新聞 tweet 的機器人，主要來源是我有追蹤的科技新聞網站的 RSS feed。  
    + 之前是把科技新聞類的 RSS 放在 Feedly 裏面，但會造成未讀量暴增，常常幾天沒消未讀就會衝到 999+，後來覺得這樣不是辦法，而且很多其實不一定要看。  
    + 所以就想說能不能用個會發科技新聞的 Twitter bot，有看到的話就看，沒看到的話就算了。  
    + 是 fork 別人的程式碼來改的：[GitHub - M157q/py-feedr: A Python parser to tweet the latest updates from multiple RSS feeds.](https://github.com/M157q/py-feedr)  
    + 後來自己加上了訂閱事件的功能，當初是針對 Golang Taiwan Gathering 報名要搶票這件事，所以用來針對某些 KKTIX 的網頁新增事件時，會用 Twitter 的私訊通知我，讓我不會錯過報名的時間，甚至可以第一時間報名。  
  
---  
  
## 參考來源  
+ [My Software Stack – Hungys.blog() – Medium](https://medium.com/hungys-blog/my-software-stack-2a406c1c57c1)  
