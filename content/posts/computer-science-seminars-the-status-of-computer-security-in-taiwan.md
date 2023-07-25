Title: 資訊工程研討 - 台灣資安防護及技術發展現況  
Date: 2013-12-17 06:59  
Author: fkz  
Category: Course  
Tags: Information Security, Hacking, Network Attack, InfoSec, Security  
Slug: computer-science-seminars-the-status-of-computer-security-in-taiwan  
  
  
## Title: 台灣資安防護及技術發展現況  
## Spearker: [黃彥男 博士/ 行政院科技會報辦公室副執行秘書](http://www.bost.ey.gov.tw/cp.aspx?n=34034779A580C772)  
  
---  
  
+ [賽門鐵克：台北市成為全球最多殭屍網路城市](http://www.ithome.com.tw/itadm/article.php?c=60894)  
+ 2012 與 2013 相較起來，十六種攻擊手法裡面，只有 Spam 下降，其他都上升。  
+ 一些常見的攻擊手法  
    + Drive-by-exploits  
        + 先觀察攻擊目標習慣瀏覽哪些網站，再去入侵那些網站並植入惡意程式  
    + Drive-by-update  
        + 透過正常軟體的更新管道派送惡意程式，成為散播惡意程式之主要管道  
    + Rogueware/Scareware  
        + 勒索軟體肆虐  
    + Target Attacks  
        + 針對式攻擊，效率持續提升  
        + 大多鎖定中小企業  
  
---  
### Evolution of DDoS  
  
+ DNS Amplification Attack  
    + Compromised DNS servers -> Domains reputation doesn't work anymore.  
+ DDoS Attack using Layer7  
    + Very difficult to block (requires L7 analysis)  
    + Can be implemented with relatively smaller number of zombies  
    + Advanced features (cookie learning etc) are implemented  
    + Jam the Web server  
        + 攻擊前還會先送 request 檢查哪個 server 最容易被攻陷  
    + Jam the application  
    + DDoS 已經商業化 ex: [ddos-service](http://www.ddos-service.ws/)  
  
---  
### 資訊安全的著手點  
  
+ 技術、人、管理  
+ 美國全面性國家網際安全倡議 (CNCI)  
    + CNCI-5  
+ 共通運作圖像 (Common Operation Picture)  
    + 狀況認知 (Situation Awareness)  
+ Cyber Kill Chain  
    + 情蒐攻擊對象 -> 入侵工具研製 -> 傳遞入侵工具 -> 執行弱點攻擊 -> 安裝後門程式 -> 指揮與管制 -> 資料竊取運送  
    + 對網路攻擊者攻擊的地點進行預測來進行防治  
+ 台灣資安策略聯盟合作模式  
    + 遭受攻擊後通報  
    + 如何整合所有的單位，達到在受到攻擊的時候可以做出相對的處理，而不是只有通報。  
+ 政府持續推動資通安全  
    + 行政院國家資通安全會報  
        + 行政院國家資通安全會報技術服務中心  
            + G-SOC 二線監控  
                + 資料蒐集、整合、分析  
                + 利用 Big Data 進行分析  
    + SPMO 規劃  
  
---  
### 資安技術的研發及挑戰  
  
+ New Challenges  
    + Social networks  
    + Cloud computing  
    + Internal threats  
    + Mobile communication  
    + Smarter and more organized hackers  
    + Data explosion  
+ [Taiwan Information Security Center (TWISC)](http://www.twisc.org/)  
+ Cyber Security Intelligent Center (CSIC)  
    + Security: 5 Phases  
        + Prevention  
        + Protection/monitoring  
        + Detection (abnormaly)  
        + Analysis & Prediction  
        + Recovery  
    + 事後資料的分析  
+ 找出 Low-Hanghing Fruit，並進行防護  
+ How do we know the emerging attack  
    + Run server honeypots  
    + Run client honeypots  
    + Run the Crawler  
    + Manual work  
+ Free DNS are bad  
+ 蒐集資料、建關係圖、找出  
