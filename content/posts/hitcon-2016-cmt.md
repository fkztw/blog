Title: HITCON 2016 CMT  
Slug: hitcon-2016-cmt  
Date: 2016-07-23 19:45:43  
Authors: fkz  
Category: Conf/Meetup  
Tags: HITCON  
Summary: Note for HITCON 2016 CMT  
  
  
# Day 1 (2016/07/22 Fri)  
  
## Keynote / 從人工搶旗到機器人攻防（From CTF to CGC) 談資安人才培育  
### Speaker: 交通大學資訊技術服務中心 黃世昆 Shih-Kun Huang  
  
+ CGC (Cyber Grand Challenge)  
    + CQE  
    + CFE  
+ ForAllSecure CRS  
    + Symbolic Fuzzer => 深、慢  
    + Random Fuzzer => 淺、快  
+ CRS Integration Attack  
    + Target-aware symbolic fuzzing  
    + 測、脅、隱、控  
        + Fuzzing, Exploit, Anti-mitigation, Post-exploitation  
+ CRS Integration Defense  
+ CRAX - World Second Auto Exploitation Generator (Simple Live Demo)  
    + Symbolic Execution  
    + Concolic Execution  
+ Hacker's Tool Chain  
    + Bug Fuzzzer  
    + Crash Detector / Failure Monitor  
    + Exploit Code Generator  
        + 目前缺少的一塊  
        + 目前分辨 Hacker 跟 Script Kiddie 的差別就在於會不會撰寫 Exploit，但要是之後 Exploit 能夠自動產生的話，Hacker 與 Script Kiddie 的分界就會消失，屆時 Hacker 又該以什麼為主要價值？  
    + Shell-code Forger  
  
  
---  
  
## 物聯網 BLE 認證機制設計的挑戰：以 Gogoro Smart Scooter 為例  
### Speaker:  GD  
  
+ Bluetooth 4.0 有三種  
    + High Speed  
    + Classic  
    + Low Energy (BLE)  
        + 類似 HTTP：session-less 有七種 method  
        + 很容易控制  
            + 可以在捷運上讓旁邊的小米手環一直振動。  
+ 很多物聯網裝置送的封包都沒加密  
    + Security Manager Protocol  
    + BLE 4.0 SMP 配對方式  
        + Just Works: 沒有保護，很容易被 MITM 攻擊  
        + Passkey Entry  
        + Out-Of-Band  
+ BLE 4.0 隱私保護  
    + 硬體識別元 讀取限制  
    + 硬體識別元 亂數化  
    + 無硬體識別元，增加驗證機制設計的困難  
+ Gogoro smart scooter  
    + Key Fob Unlock (BLE)  
        + Better than keeloq  
        + 類似 Challenge & Response 的過程  
    + Mobile App (Gateway)  
        + 交車設定 My Gogoro 帳號  
        + App 登入下載 Scooter 資訊  
    + Mobile App Pairing & Unlock  
        + 配對過程僅 ATT 讀寫資訊，沒有使用 BLE 原生的配對設定。  
        + 問題定義  
            + BLE 未配對，無硬體識別元，如何設計認証機制？ => App 和機車裏面要有同把 key，而這個 key 從 Server 來。（登入下載到 App 上）  
    + BLE Gogoro Service  
        + Service UDID 末 8 byte 為 Scooter MAC Address  
    + App Protocol 分析  
        + 發現有大概二十幾組 Command  
            + A 開頭為一般資訊查詢  
            + B 開頭為 Challenge 相關指令  
    + Unlock 流程  
        + Scooter 掃描附近 Peripheral 是否有 GATT Gogoro 服務。 UUID 351AAF0F-末 8 byte 同 Scooter MAC Address 才連上  
        + Mobile App 讀取 Scooter 目前狀態，啟用解鎖按鈕。按下按鈕後送出 ECU_Cmd(0xB4) Value 上鎖 0x00, 解鎖 0x01  
        + ...  
        + ...  
    + 車鑰匙 `Security_Key`  
        + `ECU_Response=SHA256(ECU_Challenge, Security_Key)`  
    + Insecure App Data Storage  
        + Token, Certificate 應該放在加密儲存區  
    + Unlock 模擬程式  
        + 根據上述分析結果，撰寫可 Unlock 已知 Security_Key 的 Scooter 的 Android App。（只要 Security_Key leak 的話就可能會被 Hacker 控制）  
        + 因此得知：  
            + 攻擊者只要取得 Security_Key 就能解鎖 Gogoro  
            + Security_Key 可被轉移到其他手機使用  
            + Scooter 無法驗證 Mobile 裝置識別元  
        + Security_Key 可能 Leak 的途徑  
            + 車主在 Gogoro 官網的帳號密碼被破解  
            + 車主手機的備份檔流出  
            + 車主手機使用不安全的連線導致 Security_Key 流出  
    + Gogoro 分析結果  
        + 裝置識別元隱私保護 => 提高驗證設計難度  
        + Insecure App Data Storage 弱點  
        + 其他可能威脅  
            + 取 Security_Key API 沒有 SSL Cert Pining 可能被 MITM  
            + Challenge-Response 可能被 Relay-Attack  
    + 大體來說 Gogoro 系統設計是安全的  
        + 藍牙傳輸雖然沒有配對與加密，但是傳輸的是一次性的 Challenge/Response  
        + 在手機端，金鑰基本上是綁手機，除非手機有自己做破解，而且被安裝後門程式，不然不容易直接從手機取得 Security_Key  
        + ...  
    + 威脅情境  
        + 車主手機被植入木馬  
        + ...  
    + 弱點通報廠商  
        + Gogoro 處理的態度非常積極  
+ IoT 裝置認証設計的挑戰  
    + 無法讀取裝置識別元  
        + IoT 裝置事先不認識手機  
        + IoT 裝置事先  認識金鑰  
        + 藉由 Server 把金鑰給手機  
    + 防止金鑰被複製  
        + BLE 4.2 Secure Connections  
        + 金鑰+手機裝置識別元  
        + 金鑰 Secure Element 儲存  
        + 金鑰+ Server SMS OTP  
            + 綁門號，不綁定手機。  
            + SMS 要錢，需要電信門號，IoT 裝置需跟 Server 同步。  
        + 金鑰+ Dual Counter 強化認証  
            + 綁定手機，可察覺金鑰盜用。  
            + 未必能阻擋金鑰盜用。  
    + 雙計數器強化認証  
        + 手機只存暫時性的 Key，如果被偷的話，可以 Revoke 掉。  
        + 真正的 Key 存在 Server  
        + 如果有其他裝置啟動自己的車子的話，計數器的數字會不 Match，可以察覺到有別人存取過自己的車子。  
        + 察覺到的話，可以把手機上的暫時性的 Key revoke 掉，換一把新的。  
+ 結論  
    + 介紹 Bluetooth Low Energy 安全性分析流程  
    + Smartphone 透過 BLE 控制 IoT 裝置，需要一套認証機制  
    + BLE 4.0 配對有許多限制，故廠商選擇另外設計自己的配對機制。  
    + 消費者隱私重視下，硬體識別元受限且亂數化。  
    + 提供一種更好的認証機制：雙計數器強化認証  
+ 未來展望  
    + 因為這台每天都要騎，所以不敢拆來研究 XDD  
    + Key Fob 晶片演算法研究  
    + Challenge nonce 亂數強度  
    + 是否可從 ECU 或其他管道取得 `Security_Key`  
+ Q&A  
    + 所以手機上那把 `Security_Key` 被幹走的話，目前是無法換新的 `Security_Key` 的？  
        + 對，目前是無法被更新的，至於要不要用新的機制，要問 Gogoro。  
    + HMAC 還是需要一把 Key，但那把存在手機上，還是不能避免外洩囉？  
        + 對，這邊只是用個 counter 來察覺外洩而已，並沒有要保護那把 Key，因為手機只要有 root 的話，就有外洩的風險。  
    + 在 `Security_Key` 不能更換的情況下，二手車是否有風險？  
        + 對，因為不能更換，等於原車主只要有心，還是可以保留 Security Key。  
+ Related Links  
    + [Le IoT  想想物聯網](https://thinkingiot.blogspot.tw/)  
    + [Bluetooth low energy - Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Bluetooth_low_energy)  
    + [KeeLoq - Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/KeeLoq)  
  
---  
  
## Introduction to CTF - BambooFox  
### Speaker: C.K Chen 陳仲寬  
  
+ Why attend CTF challenges?  
    + The other way for security training  
        + CTF as the training for offensive security  
        + Emulate real world problems  
    + Practice your hacking skill  
    + Compete with top hackers in the world.  
+ CTF  
    + The competition to steal data, a.k.a flag, from other computers  
        + EX. Stea admin password from a web server  
    + Most pobleams are related to real world  
    + Good practices for students even experts.  
+ History of CTF  
    + Starting from DEFCON 4 in 1996  
        + Format is a mystery  
        + Held every year since 1996  
+ Regions  
    + Japan  
        + SECCON, TMCTF, MMACTF  
        + 特別愛出 QR code 的題目  
    + South Korea  
        + CodeGate, SECUINSIDE  
    + China  
        + XCTF（聯賽）, BCTF(北京清華), 0CTF（上海交大）  
    + Russia  
        + RuCTF  
    + France  
        + Nuit du Hack CTF  
    + Malaysia  
        + HITB CTF  
    + Colombia  
        + Backdoor CTF  
+ CTFTime  
+ Famous CTF Teams  
    + PPP (US, CMU)  
    + HITCON (TW)  
    + 217 (TW, NTU)  
    + 0ops (China, Shanghai Jiao Tong University)  
    + Blue-Lotus (China, Tsinghua University)  
    + Dragon Sector (Poland)  
    + Gallopsled (Danmark)  
    + Shellphish (US, UCSB)  
    + DEFKOR (South Korea)  
+ CTF Types  
    + JeoPardy 解題型  
        + About 90% CTF are held in this type  
    + Attack & Defense  
        + Need good support of networking environment  
        + Skill needed  
            + Vul discovery and patching  
            + Network flow analysis  
            + System Administration  
            + Backdoor  
                + 把 process name 改成跟服務的名稱一樣，讓對方不知道要不要砍。  
                + 用提權的方式放入別人沒辦法砍掉的後門  
        + Online: iCTF, RuCTF  
        + Local: DEFCON Final , HITOCN Final, SECCON Final, XCTF Final, ...  
    + King of Hill  
        + Local: HoneyMe  
+ Which CTF to Play?  
    + For Beginners  
        + Backdoor, CSAW Qualificaiton, ASIS  
    + Advanced  
        + DEFCON  
        + PladiCTF (hold by PPP)  
        + CodeGate (South Korea)  
        + SECCON (Japan)  
        + PHD Quals  
+ Expreience Sharing  
    + Focus!  
        + When you start to CTF, it is best to focus on one type of problem.  
            E.g. Pwn, Reverse, Web  
        + 只要先讓自己專注於解某一類的題目，壓力比較小。  
    + Following New Techniques  
    + Customize Your CTF Toolset  
        + Prepare Your own environment  
        + E.g., pwntools  
    + Practice, Practice and Practice  
    + Enjoy the Game  
        + 不要有太大的壓力覺得自己一定要拿多少分數，應該要享受題目，讓自己儘可能從中學到東西。  
  
---  
  
## 神祕議程：黑客搶銀行  
### Speaker: cclien  
  
+ 20160716 上演 ATM Pwn2Own  （第一銀行提款機被搶 8000 萬新台幣）  
+ 2010 年的 Blackhat 就有 Live Demo 過 ATM 吐鈔票  
+ 國外有 ATM 被攻擊的案例嗎  
    + Backdoor.Tyupkin - 光碟片吐鈔  
    + Carbanak APT 內網策動吐鈔  
    + Wincor KDIAG32 維護程式吐鈔  
    + 俄羅斯和烏克蘭那邊很多提款機的維護人員會跳去作黑產賺外快 （？）  
    + [bankomatchik](http://bankomatchik.ru/)  
        + `CDM300.exe`  
        + `CSCWCING.EXE`  
        + 這個論壇是和 ATM 有關的工程師在討論的  
    + 安德魯這個名字在俄羅斯是菜市場名  
    + History  
        + 2013  
            + Skimer Trojan  
            + Plotus Trojan  
        + 2014  
            + Tyupkin Trojan (Russia)  
            + Anunak 1.0 犯罪集團  
            + Wincor Reg Trojan (Russia)  
        + 2015  
            + Carbanak 2.0 犯罪集團 (Global)  
            + GreenDispenser Trojan (Mexico)  
            + SUCEFUL Trojan (Russia)  
        + 2016  
            + GCMAN Trojan  
            + METEL Trojan  
            + Anunak 2.0 犯罪集團  
            + Wincor CNG Trojan (Taiwan)  
    + DMS 派送機制  
    + 網路架構圖中，Gateway 為什麼是網路卡？不是 Firewall？猜測是 CISCO 的設備，例如 PIX Firewall  
    + 吐鈔時間不是寫死的，是用電話與遠端的駭客聯絡，透過遠端協助 telnet 進去 ATM 讓它吐鈔  
    + Wincor 的硬體網路上都買得到  
+ 不同層面的 ATM 後門攻擊方式  
  
```  
                          應用軟體層  
                              ||  
                    WOSA/XFS, CEN/XFS 3.0  
                              ||  
OKI SP(硬體) NCR SP   Wincor SP   Hitachi SP   Diebold SP  
                    作業系統 Windows XP/7  
OKI ATM      NCR ATM  Wincor ATM  Hitachi ATM  Diebold ATM  
```  
  
+ ATM 吐鈔程式限定 2016 年 7 月  
    + 可能因為是集團長期佈署及規劃的活動。  
    + 可能是買斷的軟體，設定時間後出貨，所以可以賣給其他人，這只是其中一個買家。  
    + 從程式碼看來，英文用的很正確，程式應該不是俄羅斯人所撰寫。  
  
```  
{  
    v9 = v20;  
    *(_DWORD *)&SystemTime.wYear = 0;  
    *(_DWORD *)&SystemTime.wDayOfWeek = 0;  
    *(_DWORD *)&SystemTime.wHour = 0;  
    *(_DWORD *)&SystemTime.wSecond = 0;  
    GetSystemTime(&SystemTime);  
    if ( SystemTime.wYear != 2016 || SystemTime.wMonth != 7 || )  
```  
  
+ 新聞一直說內鬼，到底有沒有內鬼？  
    + 不太可能是內鬼所為。  
  
+ 這次破案的關鍵可能在哪？  
    + 台灣到處都有攝影機的畫面可以調閱。  
    + 台灣的外國人太少，會特別被注意。尤其到宜蘭吃飯還會被餐廳老闆娘要求合照。  
+ 台灣是鬼島，封鎖機場跟地下匯兌的話，人跟錢都出不去。  
+ 第一銀行決定把同機型(Wincor PC 1500)通通換掉，有沒有用？  
    + 典型的「頭痛醫頭，腳痛醫腳。」  
    + 每一型的 ATM 都有人在討論漏洞  
+ 在場的俄羅斯 Native Speaker 表示：「聽不太懂台灣那位幫安得魯翻譯俄文的女孩講的俄文」  
+ 最冤枉的就是 ATM，因為不是 ATM 本身的漏洞，是派送機制的管理跟網路管理上的漏洞。  
+ 真正幕後的 Hacker 並沒有被抓到，抓到的只是車手，只要換一批車手就可以繼續幹一樣的事情，如果能夠透過後續的調查，還原入侵的手法，藉此去防範，才能有效解決這個問題。  
  
---  
  
## Advanced Mobile Device Analysis using JTAG and Chip-Off  
### Speaker: Kelvin Wong  
  
  
#### JTAG  
  
+ What is JTAG  
    + Joint Test Action Group  
    + Test Access Ports (TAPs) to collect raw data from a memory chips  
+ Not chip-off and ISP  
    + Chip-Off: Remove the chip from the device  
    + In-Circular System Programming  
+ Extreme physical data acquisition  
+ Advanced technique  
+ Soldering and De-soldering （焊接）  
+ JTAG Box  
    + Riff BOX  
+ JTAG Finder  
+ Mounting Frame & Arms  
+ TAP  
    + TCK: test clock  
    + TMS: test mode state  
    + TDI: test data in  
    + TDO: test data out  
    + TRST: test reset  
    + NRST: normal reset  
    + RTCK: return clock  
    + GND: ground  
+ JTAG Molex and Jig  
+ Demonstration using Riff Box  
    + HTC EVO 3G  
    + Android OS  
+ Decoding the Lock Pattern  
    + gesture.key  
    + 20 bytes in length  
    + open source tools: Android Pattern Lock Cracker  
  
  
#### Chip-Off  
  
+ What is Chip-Off?  
    + eMMC cihp  
    + NAND Flash  
    + Disassemble & Re-balling  
+ eMMC programmer & Adapters  
+ eMMC Box  
+ EPR BOx & BGA 169e adaptor  
+ UFED Physical Analyzer  
  
---  
  
## Android Compiler Fingerprinting  
### Speaker: Caleb Fenton, Tim Strazzere  
  
+ Android Application Packaging  
    + apktool  
    + axmlprinter2  
    + jeb  
    + Reverse with  
        + smali / apktool  
        + IDA Pro  
        + jeb / jeb2  
        + androguard  
        + enjarify  
        + dex2jar + jad/jd  
        + jadx  
        + radare  
        + 010Editoer Templates  
+ AXML Files  
+ DEX Files  
    + Dex format is ... flexible  
    + Only a few different compilers  
+ Investigation  
    + Built logs of DEX files with different tools  
    + Compared files with 010Editor  
    + Found some differneces but wanted to know all of them  
+ Characteristics  
    + These may be abnormal  
        + Class interfaces  
        + Class paths  
        + Endian tag  
        + Header size  
        + Link section  
        + String sorting  
        + Map type order  
        + Section contiguity  
  
---  
  
# Day 2 (2016/07/23 Sat)  
  
## Bug Bounty 獎金獵人甘苦談 - 那些年我回報過的漏洞  
### Speaker: Orange Tsai, DEVCORE Consultant  
  
+ Slides: <http://blog.orange.tw/2016/07/hitcon-2016-slides-bug-bounty-hunter.html>  
  
+ What is Bug Bounty Program?  
    + 在官方所提供的規則及範圍下，讓獨立的研究人員可以自由尋找系統漏洞，並提供對等的獎勵。  
        + 小禮物  
        + 獎金  
        + 名譽 (Hall of Fame)  
+ Bug Bounty 的好處？  
    + 防止漏洞流入地下市場  
    + 企業架構大難顧及網路邊界時，Bug Bounty 可以邀請更多人來測試產品的漏洞  
    + 企業對外形象宣傳：告訴社會大眾重視資安，吸引資安高手  
    + 改善社會不良風氣：告訴駭客們有更簡單的方式可以做好事  
+ 哪些企業已經有 Bug Bounty?  
    + 1995: Netscape  
    + 2010: Google  
    + 2011: Facebook  
    + 2013: Microsoft, Yahoo  
    + 2014: Twitter  
    + 2015: Line  
    + 2016: Uber, Spotify, Uber, Pornhub (今年 5 月開始)  
+ The Internet Bug Bounty  
    + 為了維護網路世界的和平，獎勵那些找出可以影響整個網路世界弱點的英雄們  
+ Bug Bounty 成效  
    + Google  
        + 6 Million  
        + 750+ bugs in 2015  
        + 300+ hackrs in 2015  
    + Facebook  
        + 4.2 Million  
        + 526 bugs in 2015  
        + 210 hackers in 2015  
    + Yahoo  
        + 1.6 Million  
        + 2500+ bugs in 2015  
        + 3000+ hackers in 2015  
+ Bug Bounty 平台  
    + bugcrowd  
    + hackerone  
+ 參加 Bug Bounty 前的準備  
    + 為了什麼參加  
        + 獎金？  
        + 名譽？  
        + 練功？  
    + 對於尋找漏洞的心理準備  
        + 雖然今非昔比，但要告訴自己一定會有洞  
        + Bug Bounty 的藍海時期大約是 2013 ~ 2014 年  
        + 大公司的主機架構到了一定的規模，一定會有漏網之魚。  
    + 常見弱點的理解  
        + SQL Injection  
        + XSS  
        + CSRF  
        + XML External Entity  
        + Local File Inclusion  
        + CSV Macro Injection  
        + XSLT Injection  
        + SVG/XML XSS  
        + RPO Gadget  
        + Subdomain reaver  
    + 資訊的蒐集方法  
        + DNS 與 網路邊界  
            + 子域名？相鄰域名？內部域名？  
                + `uberinternal.com`  
                + `twtter.com`  
                + `etonreve.com`  
            + Whois? R-Whois?  
            + 併購服務  
                + Google 的 6 個月規則：併購服務 6 個月內出現的漏洞不給獎金  
        + Port Scanning  
            + Facebook Jenkins RCE by Dewhurst Security  
            + Pornhub Memcached Unauthenticated Access by @ZephrFish  
        + 小案例  
            + Yahoo! Yapache  
                + Yahoo 自己 Patch 的 Apache，在當時也算是個創舉  
                + `https://login.yahoo.com/bin/hostname`  
            + SSL 憑證不安全  
                + 可以去看憑證的內容有什麼  
+ 參加 Bug Bounty 注意事項  
    + 規則所允許範圍  
        + 範圍外就無法嘗試嗎？  
            + 多多少少還是會收一下，但不收的話廠商並沒有錯。  
            + 不要找錯目標，不然會浪費自己和廠商的時間。  
    + 規則所允許限度  
        + Instagram's Million Dollar Bug by Wesley  
            + 回報了漏洞之後，卻做了進一步的滲透測試，拿到 AWS key，進到 S3 bucket，拿到 Instagram 的 source code  
    + 不要丟不符合規定的漏洞  
        + 別踏入榮譽感的誤區  
        + 常見不符合規定的例子：  
            + SELF XSS  
            + Information Leakage  
            + Cookie without Secure Flage or HttpOnly  
            + Logout CSRF  
            + Content Injection  
            + More ...  
        + Facebook 去年有一萬多筆回報，但只有五百多筆是真正有效的漏洞回報  
        + 2014 Google VRP 回報狀況，很大的比例是沒有用的回報  
+ 撰寫報告的禮節  
    + 明確的標題及描述  
    + 附上驗證程式碼及截圖  
+ 尋找漏洞的思路  
    + 有做功課的 Bonus  
        + Facebook Onavo Dom-Based XSS  
            + 2014/03/16 Onavo Reflected XSS by Mazin Ahmed  
            + 2014/05/01 Facebook fixed it  
            + One day, Facebook revised it... Buggy again!  
        + eBay SQL Injection  
            + 列舉 eBay.com 時某台主機反查到 `eBayc3.com`  
            + 根據 WHOIS 確認為 eBay Inc. 所擁有無誤  
            + 列舉 eBayc3.com  
                + `images.ebayc3.com`  
            + 連貓都會的 SQL Injection  
                + 嘗試可否 RCE  
            + 嘗試讀檔  
                + `CREATE TABLE test (src TEXT);`  
                + `LOAD DATA LOCAL INFILE '/etc/passwd' INTO TABLE \`test\`;`  
    + 天下武功唯快不破  
        + 指紋辨識，收集整理  
            + Web Applicaion?  
            + Framework?  
        + 平時做好筆記，1-Day 出來搶首殺  
            + WordPress CVE-2016-4567  
        + 案例  
            + Uber Reflected XSS  
                + 馬上透過了 Google Hacking 找了一個 XSS 回報，但因為速度太慢被 Reject  
                + 中國網友跟我說：「所有服務到了中國，安全係數要乘以 0.8。」  
            + `developer.apple.com` 被駭案例  
                + 2013/07/18 Internet 最黑暗的一天，struts2 漏洞(s2-016)公佈。  
                + 當天有四組人馬進入，為什麼我知道？因為我是其中一個  
            + Yahoo Login Site RCE  
                + 依然是用 Google Hacking  
                    + `site:yahoo.com. ext:action`  
                    + `b.login.yahoo.com`  
                    + 看起來 s2-016 work 但看起來有 WAF  
                + 繞過 WAF  
    + 認命做苦工活  
        + 可以從一些小細節來判斷要不要對這個網站下手  
        + 用 Google Hacking 黑 Google => www.google.com XSS  
            + `site:www.google.com -adwords -finance...`  
            + `www.google.com/trends/correlate/js/correlate.js`  
            + 網站的 footer 停留在 2011，表示可能已經沒在維護  
            + JavaScript 有 Minify 但沒有做 Obfuscation  
            + 別忘了他在 JavaScript  
                + HTML Entity  
                + 八進位  
                + 十六進位  
            + 看起來是個 Dom-Based 的 SELF-XSS 需使用者互動  
                + 收的機率一半一半，需要找到更合理的情境說服 Google  
            + 繼續往下挖掘  
                + 跟 Click Hijacking 做組合技  
                + iframe 會跟著使用者的滑鼠移動，所以使用者點擊網站上任何地方都會觸發該漏洞  
            + 最後拿了 5000 美金  
        + Facebook Remote Code Execution  
            + 反向 facebook.com 的 Whois 結果  
            + 透過 SQL Injection 拿 Shell  
            + 拿 Root  
    + 平行權限與邏輯問題  
        + 平行權限：例如任意發文、任意改錢、權限問題  
        + 邏輯問題：想像自己是撰寫目標程式碼的工程師的話，自己會怎麼寫。  
            + 案例：Apple XSS  
                + `lookup-api.apple.com/wikipedia.org`  
    + 少見姿勢與神思路  
        + 針對架構的瞭解  
        + 非主流的漏洞，愈少人知道的東西愈有搞頭  
        + 思路的培養  
            + CTF  
            + 其他 Bug Bounty 的 write-up  
        + 案例：Apple RCE，第一次進入 Apple 內網  
            + Struts2 漏洞在 2012 年根本沒啥人知道  
            + Google Trend of Struts2  
                + 兩次高峰都是有 RCE 漏洞  
        + 發現的經典模式  
            + 「你尋找你知道的東西（比如到印度的新方法），結果發現了一個你不知道的東西（例如美洲）。」  
        + 某大廠商 XSS 0-Day 發現經過  
            + 掃 Tesla 範圍時發現一個 IP  
            + 進去發現是某大廠商的系統  
            + 思路  
                + Struts2 撰寫 action 都需繼承 ActionSupport  
                + 因此要判斷一個網站是不是 Struts2，只要在網址最後加上 `?actionErrors=1` 即可  
        + 如果被過濾的話怎麼辦  
            + AngularJS  
        + Uber SSTI RCE  
            + Template 相關攻擊手法是近幾年比較夯的東西，但較少人關注。  
            + Uber 在自身技術部落格有提到產品技術細節  
            + `riders.uber.com`  
                + 修改姓名等到寄信通知帳號變更  
            + Python Sandbox Bypass  
                + `{{ []._class__.__base__.__subclasses__() }}`  
+ 結語  
    + 一起成為獎金獵人吧！  
    + 勿驕矜自滿，勿忘初衷。  
    + 可以自己把 know-how 做成工具  
  
---  
  
## FèlDo: Function Event Listing and Dynamic Observing: for Detecting and Preventing Crypto Ransomware  
### Speaker: Tzung-Bi Shih  
  
Slides: <http://www.slideshare.net/penvirus/feldo-function-event-listing-and-dynamic-observing-for-detecting-and-preventing-crypto-ransomware>  
  
+ Ransomware 的本質  
    + DoS 受害者  
    + 限制軟體的使用，並以此向受害者要求付款。  
    + 最困難的是交易的部份，還必須把錢洗成白的。  
    + 沒有人能保證付了錢以後，勒索者就會把東西還給你。  
+ Ransomware 的誤解  
    + 我們會誤解成「利用加密手段而像你要求贖金」的軟體  
    + 但以下幾個也是 Ransomware  
        + misleading application  
            + 誤導你做出錯誤的舉動，然後再以幫你解決這問題為由跟你要贖金。  
        + police ransomware  
            + 假裝是當地的執法單位跟你要錢說可以規避一些法律上的問題。  
+ History of Ransomware on OS X  
    + July 2013, FBI ransomware  
        + 潛伏在 Safari 裏面，搜尋完後會跳出視窗，告訴你說你散佈著作權作品或散播兒童色情，必須要付贖金才可以解決。  
    + June 2014, FileCoder  
    + Sep 2015, Gopher  
    + Nov 2015, Mabouia  
    + Feb 2016, Ginx  
    + Mar 2016, KeRanger (今天這個 talk 的重點）  
+ OSX.KeRanger  
    + 研究這個 ransomware 的行為  
    + 然後嘗試去 rescue 被它 encrypt 的檔案  
    + 撰寫 kernel module 使用動態分析的方式去 detect 其行為  
+ Related Work  
    + Toward Generic (Crypto) Ransomware Detection  
+ Q&A  
    + 有沒有辦法做靜態分析？  
        + 有可能，但難度比較高，比如說用 Symbolic Execution 的方式，所以我認為還是用動態分析比較簡單。  
  
---  
  
## 台灣駭客協會年度規劃及專案報告 HITCON Annual Keynote  
  
+ <https://kb.hitcon.org>  
    + 資安技術文章分享平台  
+ <https://zeroday.hitcon.org>  
    + 漏洞通報平台  
  
---  
  
## HITCON 2016 奇葩獎  
  
+ 奇葩人氣獎  
    + 國安局招考駭客，單手握力竟要 30 公斤。  
        + 三立新聞 2015/10/15  
        + 少林科技武僧選拔  
    + 中勒索軟體是否會付款？民眾：「還是拿去報廢好了，因為現在電腦也才一萬多塊而已。」  
        + 刺激台灣 PC 業最佳模範  
    + 東森購物網抽獎被抓包！網友攤開程式碼，發現大獎根本抽不到」  
        + 不是你的，就不是你的。  
    + ERP Server 被勒索軟體加密，所以當機。  
        + 離職前夕送給同事的大禮  
    + 新政府將打造高階的臺灣資安神盾局  
        + 我是奇葩隊長，我終於找到工作了。  
    + 梁振英追蹤多位台灣美女，港特首辦：駭客入侵加的  
        + 自由時報 2015-12-30  
    + 網曝華碩主機板 BIOS 和 UEFI 更新機制隱患大，易被劫持。  
        + 因為交涉了一年多都沒有結果，只好把細節公佈出來。  
        + 交涉過程中各種理由推托：窗口離職、下班了、颱風假  
        + 「放假，對企業來說是十分嚴肅的。」  
    + 羅瑩雪：「他們又不方政府做， 他們是在政府的對面啊！」  
        + 在對面總比在下面好  
    + 民進黨網站遭駭，重要會議，手機全包塑膠袋。  
        + 如果有手汗的困擾，可以選購防水型手機。  
+ 奇葩特別獎  
    + MD5 惡意程式  
    + 四程式隔空盜領  
        + `ping 8.8.8.8 -t`  
+ 奇葩年度研究員（正經）  
    + Orange Tsai  
  
---  
  
## HITCON Workshop: [ZeroDay 漏洞通報平台](https://zeroday.hitcon.org)  
  
+ 通報漏洞的測試請點到為止就好，不要攻擊或是深入去拿不該拿的東西。  
+ 很多都沒有通報窗口  
    + whois  
        + 登記的人最好更正到正確的資訊，否則通報的內容會直接給 whois 上登記的人。  
    + 從網頁內容找  
    + 就是找不到  
+ 我們還會被反通報  
    + 被大學計中通報到 TACERT 說是詐騙信  
+ 滿分的單位  
    + 部份台灣的私立大學  
+ 最爛的單位  
    + 某國立大學、排名前五、在北部、有資安實驗室、還有 HITCON CTF 的成員。通報從頭到尾都沒修，還騙 TACERT 已經修了，脆後乾脆就不理他們了。（這間怎麼聽起來這麼明顯XDDD）  
+ 比較常見的嚴重狀況  
    + SQL Injection  
    + Struts2  
    + Jenkins RCE 漏洞  
  
---  
  
## 心得  
  
今年因為公司出門票而且不用請假就可以在星期五、六參加，  
所以拉了三位同事一起來，畢竟開發公司的程式還是要有些資安意識比較好，  
畢竟知道了 Hackers 到底可以做哪些事情後，寫程式應該也會比較注意一些。  
有兩位同事是第一次參加，所以大概跟他們稍微介紹了一下資安相關的常識。  
  
算一算，從 HITCON 2012 第一次參加開始，今年也算是第五年參加了，  
這次感覺不少非工作人員的熟面孔都沒出現，新面孔倒是多了不少，而且感覺有年輕化的趨勢。  
對我這種只把資安當興趣、打過兩次金盾決賽只拿到一次第五名、打 CTF 也沒有太大貢獻的傢伙來說，  
真的已經有種自己跟不上時代的感覺了。  
  
個人覺得今年講的比較好的場次是 GD 的 Gogoro 那場，  
還有第二天 Orange 有關 Bug Bounty 的 Keynote（聽完真的會讓我想嘗試看 Bug Bounty）。  
對我來說，現在參加 HITCON 已經有點變成是看這些能力很強的人怎麼努力，然後順便給自己充電的感覺，  
出社會工作以後真的覺得沒有個目標在的話，很容易迷失在庸庸碌碌中。  
  
個人覺得今年議程的種類算是蠻平均的，算是各個種類都有一些，  
Ransomware 因為最近一堆 Crypto Ransomware 很猖獗，所以有蠻多場次都與其相關，  
Android 的場次也不少，反觀 iOS 的好像就沒那麼多，然後 Web 好像又更少了。  
這兩年偏新手向的場次也比較多，  
想起第一次來參加 HITCON 的時候，  
我根本每個議程都聽不懂，  
現在的新會眾就比較幸福一些。  
  
然後 [KnowledgeBase](https://kb.hitcon.org) 跟 [ZeroDay](https://zeroday.hitcon.org)，  
也是這兩年左右才開始弄的東西，  
希望可以把台灣的資安發展帶往更好的方向。  
  
明年還會不會想參加我自己也不確定，  
出來工作以後其實也沒有說比學生還累，  
但不知道為啥就是已經沒那麼熱血了，  
去年還有玩一下 IoT Wargame 跟 RPi 和攤位的一些活動，  
今年不知為何慵懶到連玩都不太想玩，  
然後 BambooFox 打的一些 CTF 也沒啥心情想參加，  
也許明年還要不要參加就明年到時候再決定吧。  
