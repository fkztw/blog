Title: Study-Area 2016 群英會  
Slug: study-area-summit-2016  
Date: 2016-07-16 16:28:58  
Authors: fkz  
Category: Conf/Meetup  
Tags: SDN, DevOps, DC/OS, ePUB, Git, Ansible  
Summary: 2016/07/16 在交大 EC122 教室舉辦的 Study-Area 2016 群英會的筆記。  
  
  
Event Link: <http://studyarea.kktix.cc/events/c6457aff>  
> 好多人報了名沒出現啊 ww  
  
---  
  
# ONOS 及實際 SDN Switch 整合使用經驗分享 by 小飛機  
  
+ 投影片連結：[ONOS 及實際 SDN Switch 使用經驗分享 - Google 簡報](https://docs.google.com/presentation/d/18tDnGkjTQ1yEcZnNkVz94a0FbusDd9lXb3MAcTnZDzE/edit#slide=id.p)  
+ ONC (Open Network Conference), SDN 相關領域年度最大聚會  
+ 因為在 ONC 發表成果，而被 Bell Labs 位於比利時的歐洲總部邀請面試。  
    + 多參與 Open Source 專案，讓自己在國際級的 Conf 被看見，是很有用的  
  
## SDN 新手如何開始？  
  
### 簡單起頭  
  
+ 只做 L2 Switching  
    + 用 `ping` 驗證網路狀況  
    + 用 `iperf` 驗證網路速度  
+ 決定 Topology  
    + 3-Tier Topology  
    + Mesh Topology  
    + Leaf-Spine Topology  
    + [STP](https://en.wikipedia.org/wiki/Spanning_Tree_Protocol#Rapid_Spanning_Tree_Protocol) (Spannig Tree Protocol)  
        + Loop-free Topology  
+ 養成有實驗組與對照組的習慣  
+ 基本的 Networking 經驗要有  
+ 美國有高中生就在當 intern 學習這個部份，所以不要覺得門檻太高，真的有興趣的話就跳下來研究吧  
  
### 常見實際拓墣  
  
```  
Internet -- DHCP/NAT Server -- Legacy L2 Switch  -- OpenFlow Controller (放在內網，不然很容易被打）  
                                       |  
                            OpenFlow-Enabled Switch (建議用 Out-of-band)  
                                   /        \  
                             Host A         Host B  
```  
  
可以觀察到封包都是好事  
  
  
### OpenFlow-Enabled Switch 選擇  
  
價格從高排到低依序為：  
  
1. 採買實體 OpenFlow-Enabled Switch 及 Network OS  
    + 從各家 Network OS 廠商中的 Hardware Compatibility List 裡挑選硬體  
2. Linux Server + 4-Port NIC + OpenvSwitch  
    + 可以直接在 Local 用 Wireshark 觀察封包  
3. 支援 OpenWrt AP + OpenvSwitch  
  
Protocol 請以 1.3 為主，1.0 為次。  
  
OpenvSwitch 和 Docker (Socket Plan), Xen Server 有關  
  
  
### OpenFlow Controller 選擇  
  
選擇 Controller Application 有實作 L2 Forwarding 或者是 Switching 功能  
  
1. [Ryu](https://osrg.github.io/ryu/)  
    + 學習曲線低  
    + Keyword: `Simple_Switch_13` (or `Simple_Switch_10`)  
2. [ONOS](http://onosproject.org/)  
    + 學習曲線偏高  
    + Keyword: `org.onosproject.fwd`  
+ Tip: 觀測不同家的 Controller 建立行為基準  
  
  
### 直接接上 SDN Controller 進行測試？  
  
+ 如果你經驗非常豐富的話，可以。  
+ 要先確保 OpenFlow-Enabled Switch, Host A, Host B 都可以 ping 到 OpenFlow Controller  
    + 八成的人有問題都是出在這部份，基本上就是網路設定沒設定好  
  
  
### OpenFlow Connection Setup  
  
+ <http://sdnhub.org/tutorials/openflow-1-3/>  
+ 要記得看 Spec，去對照現在做的行為對不對  
+ 確認連線正常後，再開啟 OpenFlow Controller。（SDN 的功能）  
+ 到目前為止是基本的設定步驟，可以嘗試用全自動化的方式做掉這部份，例如用 Ansible。  
  
  
### 在啟動 SDN 的狀況下，連線不正常？  
  
+ 觀測 Flow Count 是否有增加 => 可確定 Flow Entry 有沒有被 Match  
    + `ovs-ofctl dump-flows`  
+ Tips: 先從 Switch 開始懷疑起  
  
  
### 真的找不出業障在哪裡的話  
  
+ 撈封包回來用 Wireshark 檢查  
+ 根據 IANA 的規定，OpenFlow 使用 6653 port，但早期有些是 6633 port，記得現在都用 6653 就好。  
+ 業障關鍵字： `OFPT_ERROR`  
    + 對照 [OpenFlow 1.3 Spec Error Message](https://www.opennetworking.org/images/stories/downloads/sdn-resources/onf-specifications/openflow/openflow-spec-v1.3.0.pdf) (A.4.4) 確定錯誤碼的意思  
  
  
### 複雜一點的實際使用案例  
  
+ ONOS SDN-IP  
    + <https://wiki.onosproject.org/display/ONOS/SDN-IP+Tutorial>  
+ [OpenCORD](http://opencord.org/)  
    + AT&T 提出的 Project  
    + Re-architecting the Central Office  
        + <http://opencord.org/wp-content/uploads/2016/04/ONS-2016-Plenary.pdf>  
    + 今年 4 月在美國有進行 field try 了  
    + Domains (三者都建立在 CORD Controller）  
        + Residential  
        + Mobile  
        + Enterprise  
+ ONF Atrium - SDN Project Stack  
    + <https://www.opennetworking.org/?p=1757&option=com_wordpress&Itemid=316>  
    + <https://github.com/onfsdn/atrium-docs>  
  
對這些專案或者和 SDN 相關議題有興趣的話，歡迎加入 [SDNDS-TW 社群](http://sdnds.tw/)  
  
  
## Related Links  
  
+ [GitHub - opennetworkinglab/onos: Open Network Operating System](https://github.com/opennetworkinglab/onos)  
  
---  
  
# 淺談 DC/OS by Daniel  
  
+ 相關關鍵字  
    + [DC/OS](https://dcos.io/)  
    + [Mesos](https://mesos.apache.org/)  
    + [Kubernets](http://kubernetes.io/)  
    + [CoreOS](https://coreos.com/)  
  
  
## What's DC/OS  
  
### Mesos Master Quorum  
  
+ 預設一台 Mesos Master，兩台 Mesos Standby，預設用 ZooKeeper 管理。  
+ Framework 和 Scheduler 做資源的分配與調度，丟到 Mesos Slave (Framework + Executor) 執行  
  
+ [Architecture - Mesosphere DC/OS Documentation](https://docs.mesosphere.com/1.7/overview/architecture/)  
    + DCOS Master  
        + Mesos DNS  
            + Service Discovery  
    + DCOS Private Agent  
        + 給內部使用，外網連不到  
    + DCOS Public Agent  
  
  
## Why DC/OS  
  
+ 生態圈豐富  
    + 許多大廠都有在使用  
+ 漂亮的 GUI  
+ 有 HA 機制 (ZooKeeper) 及 Service Discovery (Mesos DNS)  
+ 100% Open Source  
  
  
## How to use DC/OS  
  
+ <https://dcos.io/docs/1.7/>  
+ Use DC/OS on AWS  
    + <https://mesosphere.com/amazon/>  
+ Login 方式目前只支援三種  
    + Google Gmail  
    + Azure Hotmail  
    + GitHub  
    + LDAP 是不行的  
  
  
## [dploy](https://github.com/mhausenblas/dploy)  
  
+ DC/OS 的 build file 是 JSON 格式，和 Dockerfile 的 yaml 格式不同。  
+ Usage  
    + `dploy init`  
    + `dploy dryrun`  
    + `dploy destory`  
        + 刪除 container  
    + `dploy ls`  
        + 列出所有 containers  
    + `dploy [-all] ps`  
        + 列出 container 在執行的 process  
    + `dploy -pid=<PID> [-instances=NUM] scale`  
        + 幫你做 auto-scaling  
+ Docs  
    + <http://dploy.sh>  
    + [GitHub - mhausenblas/s4d: A sandbox for dploy (s4d)](https://github.com/mhausenblas/s4d)  
        + 透過 GitHub 的 Webhook 去 trigger DC/OS  
  
  
## [Marathon](https://docs.mesosphere.com/1.7/usage/service-guides/marathon/)  
  
+ DC/OS GUI 介面  
+ 有基本的 healthcheck  
  
  
## Related Links  
  
+ [GitHub - dcos/dcos: DC/OS Build and Release tools](https://github.com/dcos/dcos)  
+ [Mesosphere DCOS on Google Cloud Platform - Mesosphere](https://mesosphere.com/google/)  
+ [Mesosphere Comes To Google's Cloud Platform](https://techcrunch.com/2014/08/18/mesosphere-comes-to-the-google-cloud-platform-integrates-googles-kubernetes-project/)  
+ [Setting up a Mesos and Marathon Cluster · Mesosphere](https://open.mesosphere.com/getting-started/install/)  
+ [GitHub - google/cadvisor: Analyzes resource usage and performance characteristics of running containers.](https://github.com/google/cadvisor)  
  
---  
  
# ePUB 電子書現場包 by 雨蒼  
  
## 為什麼要用 ePUB  
  
+ Reflow  
    + 中文直排  
    + 避頭尾點  
    + 嵌入字體  
+ 支援字體特效  
+ Fixed Layout  
    + 一頁一圖  
        + 日本蠻多拿來做漫畫的  
    + 有聲朗讀  
+ 提供 DRM 版權保護  
  
  
## ePUB 的結構  
  
+ mimetype  
+ META-INF/container.xml  
    + 設定路徑  
+ OEBPS/content.opf  
    + 整個 ePUB 最核心的地方  
    + metadata  
    + manifest  
        + 可放字體、圖片、CSS、XML，基本上就是個網頁  
    + spine  
        + 整個 ePUB 的骨幹。（目錄、書本內容）  
    + guide  
        + 導讀頁  
  
## 打包流程  
  
製作 Markdown => [電電轉換器](http://conv.denshochan.com/tw) => 解壓縮、修改、打包  
  
+ [電電轉換器有自己的特殊 Markdown format](http://conv.denshochan.com/tw/markdown)  
+ 表格  
    + [csv to html converter](http://www.convertcsv.com/csv-to-html.htm)  
    + 再貼上到 Markdown 裏面  
+ [電電設定檔](http://conv.denshochan.com/tw/config)  
    + 使用 YAML 格式  
    + ddconv.yml  
+ 上傳打包  
+ 修改檔案  
    + 使用 ePUB Packer 解壓縮  
    + 使用 ePUB Checker 檢查語法是否有錯  
+ 修改 CSS  
    + 新增靠右對齊  
    + blockquote 從變成斜體修改成變成標楷體  
  
  
## 實際打包  
  
+ 從 gitbook 到 ePUB  
    + toc.ncx 很不好改，而且在 ePUB 不是必要的，所以可以直接砍掉  
  
  
## 目前遇的問題  
  
+ ePUB 的表格呈現不是很理想  
  
  
## Q&A  
  
Q: 自己做電子書要如何申請 ISBN?  
A: 我都交給別人申請，有需要的話可以找我，我幫你轉介給知道的人幫忙。  
  
電電轉換器是日本人開發的，  
目前還有些不足的地方，  
有時候會突然當掉。  
  
Q: 臺灣有沒有類似 <https://www.bookscan.co.jp> 這種讓你寄實體書過去然後轉成電子書給你的服務？  
A: 臺灣目前好像沒有。  
  
Q: GitBook vs ePUB  
A: 一開始也是用 GitBook，但後來用電電轉換器這套以後，覺得這套方法比較好，因為這套方法產生出來的 ePUB 才能上架到 Google 等其他平台。但我通常還是會兩個都做，先弄 GitBook 的版本，然後再把 GitBook 產生的 markdown 全部合到一個 markdown 裡頭再用這套方法產生 ePUB。  
  
  
## Related Links  
  
+ [如何製作一本epub3電子書 - g0v.hackpad.com](https://g0v.hackpad.com/epub3-9zQsGYYU1TG)  
+ [小市民權益保護99招  - GitBook](https://www.gitbook.com/book/jrf-tw/citizen_defend_rights_99_steps/details)  
    + [Introduction · 小市民權益保護99招](https://jrf-tw.gitbooks.io/citizen_defend_rights_99_steps/content/)  
+ [EPUB - Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/EPUB)  
  
---  
  
# Git 導入中小企業經驗分享 by Haway  
  
  
## 真實遇到的問題  
  
+ Clone 錯專案  
+ Add 錯檔案，不能 commit  
+ Merge 失敗  
+ Branch 是三小  
+ 不會打版號  
+ SVN 的高手搗亂  
  
  
## 版本號如何決定  
  
就 [Semantic Versioning 2.0.0](http://semver.org/)  
  
  
## Git 專案開始  
  
+ 與開發人員討論工作習慣  
+ 瞭解開發環境與測試方式  
+ 專案賣給 A 客戶後，也要賣給 B 客戶，但要微調需求，這時候要開新 branch 還是 clone 成新 project 來改？  
    + clone 成新 project 來改，因為開新的 branch 的話，永遠不會 merge，開一個不會 merge 的 branch 幹嘛？  
    > 其實我沒有很認同這個，萬一要是要更改什麼功能或是修改 bug 呢？每個 repo 都要重覆改？跨 repo 的 cherry-pick？要是今天有 N 間公司呢？  
+ 在一個 git repo 底下，什麼時候該用 `git init`？什麼時候該用 `git submodule`？  
    + 可以自己獨立運作的就 `git init`  
    + 必須 depend 在現在這個 git repo 底下的就 `git submodule`  
    > 我也沒有很認同這個答案，基本上 submodule 對我來說就是有用到 git 的 dependency packages 就可以用。  
  
> 大部分都是喇賽性質，  
> 覺得這個 Talk 應該叫做 「大家一起來嘲笑 git 新手會做的那些蠢事」，  
> 本來是預期這個 talk 應該會講遇到的困難，  
> 然後怎麼設計出一個使用模式或者解法，  
> 讓不太會使用 git 的人也能夠開發。  
> 或者是怎樣的教學可以讓這些新手比較快瞭解 git 的概念，  
> 而不是只是提到遇到的問題然後一直抱怨，  
> 這個在 Twitter 上嘴炮就好了啊，  
> 沒必要開個 talk 吧 XD  
  
---  
  
# 淺談 Ansible 組態管理工具 by Sakana  
  
這個應該跟我半年前聽的那場內容是一樣的，  
[2015 12 月份 SA@Tainan 淺談 Ansible 自動化組態管理工具之筆記](/posts/2015/12/26/study-area-ansible-tutorial-note/)  
這次有補充的內容我會集中整理在這份裡頭，不會記這在篇。  
  
---  
  
# 現代 IT 人一定要知道的 Ansible 自動化組態技巧 by 凍仁翔  
  
## Roles 是什麼？  
  
"Scalinig Up Your Playbooks" - Ansbile: Up and Running  
  
## 怎麼使用 Roles  
  
+ <https://galaxy.ansible.com>  
+ 安裝 Roles  
    + `$ ansible-galaxy install {ansible-roles}`  
+ 初始化  
    + `$ ansible-galaxy init {ansible-roles}`  
    + <https://galaxy.ansible.com/intro>  
  
## Windows Support 是什麼？  
  
+ <https://docs.ansible.com/ansible/intro_windows.html>  
+ Ansible 2.0 對 Windows Managed node 的支援度大幅提升  
    + 換句話說，就是 2.0 以前的支援度蠻雷的 XD  
+ 透過 inventory 定義 Managed node 透過 WinRM, SSH, PowerShell 來佈署  
  
## 怎麼用 Ansible 管 Windows Server？  
  
+ 怎麼佈署 Control Node?  
    + 安裝 Ansible 和 pywinrm  
+ 怎麼佈署 Managed Node?  
    + 開啟 WinRM: <https://github.com/ansible/ansible/blob/devel/examples/scripts/ConfigureRemotingForAnsible.ps1>  
        + 若網路有問題，改成私人網路(Private Network)  
    + 安裝 PowerShell  
    + 關閉 UAC  
        + 沒關的話，可能會造成部份 tasks 被中斷。(Optional，視情況而定，可能會遇到，也可能不會遇到）  
+ 怎麼設定 Ansible？  
+ Inventory 是什麼？  
    + 主要用來定義 Managed Node 的 IP 與 Group，也可以用來設定 WinRM 連線資訊。  
    + 在控管 Windows Managed node 前，還需要設定一些 inventory 變數。  
        + `ansible_connection: winrm`  
        + `ansible_port: 5968`  
+ 怎麼用 Ad-Hoc command 管 Windows？  
    + `ansible <主機名稱> -m <模組> -a <參數1> <參數2>`  
    + `ansible all -m win_ping`  
+ 怎麼用 Playbooks 和 Roles 管 Windows？  
  
```YAML  
setup.yaml  
===  
hosts: all  
roles:  
  - chusiang.win_vim  
  
tasks:  
  - name: copy check vim version file  
    win_template:  
      src: 'templates/check_vim_version.bat.2'  
  
...  
```  
  
### Demo  
  
<https://youtu.be/wZLT1B_uh9Q>  
  
  
## 怎麼避開 Windows Playbooks 路徑地雷？  
  
1. 使用 `key:value` 寫法會比 `key=value` 少採點雷  
    + 後者會不時遇到路徑無法辨識的問題  
2. 避免在行尾使用 `\`  
3. 遇到 `\` 可以是用 `\\` 來代替，因為 Windows 原先就會這樣解析路徑。  
4. 特殊符號解析有誤？  
    + 先寫好批次檔  
5. 在 Playbooks 裡，`/` 作為路徑的分隔符號是有效的。  
  
  
## Ansible 常用的 Windows 有哪些？  
  
1. `raw`: Executes a low-down andy dirty SSH command.  
2. `win_copy`  
3. `win_file`  
4. `win_get_url`  
5. `win_lineinfile`  
6. `win_msi`  
7. `win_ping`  
8. ...  
9. ...  
10. ...  
  
  
## References  
  
+ [GitHub - chusiang/studyarea1607-ansible-demo: Ansible Playbook Roles Demo on StudyArea Summit 2016.](https://github.com/chusiang/studyarea1607-ansible-demo)  
+ [Ansible Up and Running eBook Preview | Ansible.com](https://www.ansible.com/ansible-book)  
  
  
## Q&A  
  
Q: Playbooks 怎麼管理比較好？  
A: 可以參考 [Best Practices — Ansible Documentation](https://docs.ansible.com/ansible/playbooks_best_practices.html)  
  
Q: 是不是一定要透過 MSI? 有沒有遇過 AD server 上的問題？  
A: AD server 的雷有遇到，然後因為我其實比較常用 Linux 和 Mac，所以大部份都是從 [Windows Modules — Ansible Documentation](https://docs.ansible.com/ansible/list_of_windows_modules.html) 拿一些現成的來用。  
  
---  
  
# Nokia Bell Labs 面試經驗 by 小飛機  
  
## 心得  
  
+ 英文超級無敵重要  
+ 平時要多參與 Open Source 專案累積經驗  
> 個人覺得還要注意的重點是深度，而且專案最好都要彼此有相關。  
+ 面試一定要準備  
+ 做的專案要能夠適當的行銷  
    + 雖然當時的重點是放在怎麼 promote Taiwan  
+ 正常歐洲處理速度超慢  
    + 從第一天寄信到面試過了一個月  
    + 歐洲還會放暑假  
    + 下班就下班了，沒在看 mail 的，所以約的時間常常很慢才看到就錯過。  
+ 當然還需要點運氣  
