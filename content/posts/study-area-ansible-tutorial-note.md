Title: 2015 12 月份 SA@Tainan 淺談 Ansible 自動化組態管理工具之筆記  
Slug: study-area-ansible-tutorial-note  
Date: 2015-12-26 21:54:18  
Authors: fkz  
Category: Conf/Meetup  
Tags: Python, Ansible, DevOps, automation, Meetup  
Summary: 簡單講解 Ansible  
Modified: 2016-07-16 15:17  
  
+ Speaker  
    + [黃俊宏 sakana / Max](https://github.com/sakanamax)  
+ Event URL  
    + [2015 12月份 SA@Tainan 淺談 Ansible 自動化組態管理工具 12/26(六)](http://phorum.study-area.org/index.php/topic,71531.msg343054.html#msg343054)  
+ Place  
    + 成功大學資訊新館 203 電腦教室  
+ [Slides](https://docs.google.com/presentation/d/136VKHI_H8wKyrLIm1eaTMLz82uoPgjV4zTiGb1_-_Ig/edit#slide=id.p)  
+ [Jupyter Notebook using in this tutorial](/files/study-area-ansible-tutorial-note/)  
  
---  
  
+ Configure Management 四大金釵:  
    + [Ansible](https://github.com/ansible/ansible) (Python)  
    + [Chef](https://github.com/chef/chef) (Ruby)  
    + [Puppet](https://github.com/puppetlabs/puppet) (Ruby)  
    + [Salt](https://github.com/saltstack/salt) (Python)  
+ Ansible 現在有 modules 可以控制 Windows  
  
---  
  
### About Ansible  
  
+ Ansible - configuration management tool 組態管理工具  
    + [Official Website](http://www.ansible.com/)  
    + [GitHub](https://github.com/ansible/ansible)  
+ Online resource 線上資源  
    + [Documentation 文件](http://docs.ansible.com/)  
    + [Ansible Galaxy](https://galaxy.ansible.com/)  
        + 社群共享 Role 集散地  
    + [Ansible Project Google Group 討論群組](https://groups.google.com/forum/#!forum/ansible-project)  
    + irc.freenode.net: #ansible  
        + Brian Coca 非常熱心，有問題問他就好(?)  
  
---  
  
### Why Ansible  
  
+ Infrastructure as Code  
+ 語法簡單 (playbook 以 YAML 語法撰寫)  
+ 不需要安裝 client (clientless)  
+ Push-based  
    + Pull-bsaed: Agent check to server by time. (Chef / Puppet by default)  
    + Push-based: Server push change by order  
        + 你可以決定何時進行設定  
+ Very thin layer of abstraction  
    + 以原有的習慣進行部署  
  
---  
  
### 預備知識  
  
+ ssh  
+ CLI  
+ 安裝套件  
+ sudo  
+ 管理檔案權限  
+ 管理 service  
  
---  
  
### How to install Ansible  
  
+ <https://docs.ansible.com/ansible/intro_installation.html>  
  
---  
  
### The role of Ansible  
  
+ Control Machine  
    + Control managed nodes  
    + Need Python 2.6 above  
+ Managed Node  
    + Remote server  
    + Need Python 2.5 above  
+ 預設一次五台主機佈署, 可以調整 forks 變數來改變預設值。  
  
---  
  
### Difference between shell script  
  
+ 不用登入遠端去抓 shell script 與執行 (中央集權)  
+ 會從佈署失敗的地方開始繼續，不會整個重跑。  
+ 針對所有主機同時進行，**按照順序**執行任務  
+ 有許多現成的 Module 可用,用法習慣跟原系統差不多  
+ 有別人寫好的 Role 可以參考與套用 (Ansible-galaxy)  
+ 語法簡單，容易上手(YAML)  
+ 可以利用 fact 與變數執行 loop 或是其他的做法  
+ 有別人寫好的 Role 可以參考與套用：[Ansible Galaxy](https://galaxy.ansible.com/)  
  
---  
  
### The first Ansible command for you  
  
`ansible 對象 -m ping`  
  
```  
Usage: ansible <host-pattern> [options]  
    -i INVENTORY, --inventory-file=INVENTORY specify inventory host file (default=/etc/ansible/hosts)  
    -m MODULE_NAME, --module-name=MODULE_NAME module name to execute (default=command)  
```  
  
---  
  
### Inventory File  
  
+ Ansible lists hosts in text files, called **inventory files**.  
+ 將遠端主機相關資訊以文字檔案的方式建立稱為 inventory file, 常見的檔案名稱為 hosts  
+ 語法 `servername  options`  
+ 可以設定群組 `[群組名稱]` 來組織對象  
+ 常用選項  
    + `ansible_ssh_host -- Remote Host IP`  
    + `ansible_ssh_user -- Remote SSH User Name`  
    + `ansible_ssh_private_key_file -- SSH Key`  
    + `ansible_ssh_port -- ssh port`  
    + `ansible_ssh_pass -- ssh password`  
+ 如果有定義到 `ansible.cfg` 的 `[defaults]` 就可以不列出  
  
---  
  
### ansible.cfg  
  
`ansible.cfg` looks for this order:  
  
1. File specified by the ANSIBLE_CONFIG (-i option)  
2. `./ansible.cfg`  
3. `~/.ansible.cfg`  
4. `/etc/ansible/ansible.cfg`  
  
可以設定一些預設行為，不需要逐一設定在 hosts  
  
example:  
```  
[defaults]  
# hostfile -- 主機 ip 對照  
hostfile = hosts  
  
# remote_user -- 遠端使用者名稱  
remote_user = root  
  
# private_key_file -- SSH privite key path  
# host_key_checking -- 不詢問加入 ssh 金鑰  
host_key_checking = False  
  
# 設定 retry files (*.retry) 存放路徑, 預設放家目錄  
# 我自己喜歡指定在目前目錄, 以免作完實驗家目錄一堆 .retry  
retry_files_save_path = ./ansible-retry  
  
# 平行處理數量, 預設是 5 個, 應該不一定會用到先記下來  
# forks = 20  
```  
  
---  
  
### Ansible Module  
  
Ansible 使用上, 會根據不同的功能呼叫不同的 Module  
  
+ Module 目錄： <http://docs.ansible.com/ansible/modules_by_category.html>  
+ [All Modules — Ansible Documentation](https://docs.ansible.com/ansible/list_of_all_modules.html)  
  
+ System module  
    + ping  
+ Notification Modules  
    + IRC  
    + Slack  
    + Jabber  
    + email  
  
---  
  
### Hands on Lab with Module  
  
`ansible 對象 -m 模組名稱 -a 要傳入的參數`  
  
#### 官方文件該怎麼看  
  
+ 官方 doc 的 Options 先看 required  
+ required 裏面先看 yes 的就好  
+ Example 沒差，因為有時候是騙你的XD  
  
---  
  
### Playbook  
  
> Playbook 包含很多 Play  
> Play 就是你要執行的工作  
> Play 裏面包含很多 hosts  
> Play 裏面有 tasks 定義要做哪些事  
> 而 tasks 做的事，可以透過 modules 達成  
  
+ 使用 YAML 語法  
+ **A script is called a playbook.** (類似一個 shell script)  
    + 包含要進行組態的主機  
    + 以及順序進行的工作  
    + 包含許多的 play (`*.yml`)  
+ Ansible 針對所有的主機同時 (平行) 執行tasks.  
    + Ansible 會等待所有主機 task 完成之後，才會進行下一個 task  
    + Ansible **按照順序執行** tasks  
    + 如果遇到錯誤的話就會立即停止，但在下次執行的時候，可以從上次錯誤跳出的地方繼續。  
+ Ansible playbooks 以 YAML 語法撰寫，簡單易讀。  
+ 使用 ansible-playbook 指令執行  
    + `ansible-playbook`  
    + `ansible-playbook  --verbose 顯示詳細資訊`  
    + `ansible-playbook  --check 不實際執行 dry run`  
  
#### YAML 語法  
  
+ Yet Another Markup Language  
    + <http://yaml.org/>  
    + <https://zh.wikipedia.org/wiki/YAML>  
+ Start of File  
    + 以 3 個 `---` 開始, 不加上去也可以  
+ Comment  
    + 以 `#` 來進行單行註解  
    + `#` 就是註解的開始（跟 shell script 一樣）  
+ Strings  
    + 不一定要加上引號  
    + 可是有的時候為了易讀性，可以使用單引號或是雙引號  
+ Booleans  
    + 使用 True 或是 Yes 都可以視為真  
    + 但是還是用 True 不會混亂  
+ Lists (delimited with hyphens)  
```  
- My Fair Lady  
- Oklahoma  
# inline 格式list  
[My Fair Lady, Oklahoma, The Pirates of Penzance]  
```  
+ Dictionaries  
```  
address: 742 Evergreen Terrace  
state: North Takoma  
# inline  格式  
{address: 742 Evergreen Terrace, city: Springfield, state: North Takoma}  
```  
  
---  
  
### Plays  
  
+ 每一個 play 包含  
    + A set of hosts to configure. （目標主機）  
    + A list of tasks to be executed on those hosts. （工作內容）  
+ 常用的設定  
    + `name` - 執行的 play 或是 task 名稱  
    + `sudo` - 要不要執行 sudo  
        +  已經改叫 `become` 了  
    + `vars` - 變數設定  
+ Tasks  
    + 要在遠端主機執行的工作  
        + Modules  
            + Modules are scripts that come packaged with Ansible.  
            + <http://docs.ansible.com/ansible/modules_by_category.html>  
  
register, debug 觀察錯誤的時候用  
通常會用到都不是什麼好事情XD  
  
---  
  
### Hands on Lab with Playbook  
  
+ [playbook using in this hands on](/file/study-area-ansible-tutorial-note/SA_playbook/shell_yum_when.yml)  
+ [Some playbook examples](https://github.com/sakanamax/LearnAnsible/tree/master/books/Oreilly-Up-And-Running-Ansible/playbooks)  
+ [The playbook for hands on environment for this tutorial](https://github.com/sakanamax/LearnAnsible/blob/master/books/Oreilly-Up-And-Running-Ansible/playbooks/SA_20151226_Tainan_Ansible.yml)  
+ [The docker file for hands on environment for this tutorial](https://hub.docker.com/r/sakana/jupyterhub/)  
  
---  
  
## References / Related Links  
  
+ [Ansible Up & Running](http://shop.oreilly.com/product/0636920035626.do)  
+ [sakananote](https://sakananote2.blogspot.tw/)  
+ <https://hub.docker.com/r/sakana/ansible2.x_ubuntu14043/>  
+ <https://hub.docker.com/r/sakana/jupyterhub/>  
+ [Ansible Mind Map](https://github.com/sakanamax/LearnAnsible/blob/master/Mindmap) (Use FreeMind to open it)  
+ [sakanamax/LearnAnsible · GitHub](https://github.com/sakanamax/LearnAnsible)  
+ [Google Cloud Platform Guide — Ansible Documentation](https://docs.ansible.com/ansible/guide_gce.html)  
  
---  
  
## Thoughts  
  
聽完後覺得 Anisble 真的蠻方便的，  
基本上就是把 shell script 包裝起來的概念，  
感覺可以直接取代 shell script 了。  
可以很簡單得用 YAML 撰寫 playbook 來針對不同作業系統做不同的事，  
在 playbook 中的每一個 play 都代表著一個步驟，  
每一個 play 在 Jupyter notebook 中也都會顯示執行結果，  
有種 unittest 的味道。有些人喜歡有些人不喜歡（誤）  
然後也不需要在 managed nodes 上裝任何 clients，  
只要 managed nodes 能夠用 ssh 登入進去，  
就可以直接都在 contorl machine 上操作。  
  
比較有趣的是講者有提到他們會直接使用 Jupyter notebook (IPython notebook)  
讓不懂 playbook 詳細細節的人也可以操作，  
因為 Jupyter notebook 可以在每個 play 加上說明，  
所以要交接的時候可以直接丟出這些 Jypyter notebooks 就無痛交接。  
  
會後跟凍仁拿到了之前一直想拿的 Vim 貼紙，  
還獲得了凍仁的 MOPCON 名片，  
然後和小飛機、小趴、CrBoy、雨蒼從 Ansible 聊到刑事訴訟法的灰色地帶XD  
（其實警察臨檢要搜身或者搜車的話，如果沒有搜索令其實是違法的之類的）  
  
之後去 Double Cheese 聚餐，  
在等待的時候又聊到了學校資訊系統的共同問題，  
Single Sign-On, 選課系統之類的...  
用餐的時候就坐在鳥哥(vbird)的對面！  
當初小高一的時候用 Ubuntu 就是看著鳥哥的網站學 Linux 指令的啊！  
今天本人竟然就在我對面！  
鳥哥的人好親切啊，竟然還幫我倒飲料>"<  
然後又聊到了威妥碼拼音、通用拼音、漢語拼音的故事。  
StudyArea 好像是我參與的社群裏面第一次可以這麼快聊起來的，  
真的很開心。  
  
+ 2015/12/26 寫於成功大學資訊舊館前  
    + (好多蚊子啊！)  
+ 2016/07/16 Study Area 2016 群英會  
    + 補充一些新的內容  
