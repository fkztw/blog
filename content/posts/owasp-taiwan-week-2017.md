Title: OWASP Taiwan Week 2017  
Slug: owasp-taiwan-week-2017  
Date: 2017-11-20 18:01:33  
Authors: fkz  
Category: Conf/Meetup  
Tags: OWASP, Security  
Summary: Note for OWASP Taiwan Week Day 1  
  
  
+ event links  
    + <https://csa.kktix.cc/events/owasp2017>  
    + <http://2017.owasp.org.tw/agenda_2.html>  
+ [OWASP 2017 Top 10 Golden Master (EN) 備份](/files/owasp-taiwan-week-2017/OWASP Top 10 2017 GM (en).pdf)  
  
---  
  
## 開場  
  
+ [OWASP 2017 Top 10](https://www.owasp.org/index.php/Top_10_2017-Top_10) 已經釋出，上一次正式發佈是 2013 年。  
    + 2017 分別有 RC1 和 RC2，中間有些差異，大家吵了很久。XD  
    + 原來 [OWASP Top 10 有 GitHub Repo](https://github.com/OWASP/Top10) 啊。  
    + [OWASP Top 10 2017 Golden Master](https://github.com/OWASP/Top10/blob/master/2017/OWASP%20Top%2010%202017%20GM%20(en).pdf)  
  
---  
  
## OWASP 發展趨勢 - 蔡一郎  
  
+ 簡介  
    + <https://owasp.org>  
    + OWASP Taiwan 創立約莫 7~8 年，但之前都是被認定為不活躍的社群。  
    + [OWASP CTF](https://www.owasp.org/index.php/Category:OWASP_CTF_Project)  
    + [OWASP Top 10](https://github.com/OWASP/Top10) 都有告訴你要如何檢測網站是否有該漏洞。  
    + 志工性質、無給薪，好處是志工可以優先參加活動。  
    + Research and Development  
        + [Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)  
        + [Zed Attack Proxy (ZAP)](https://www.owasp.org/index.php/OWASP_Zed_Attack_Proxy_Project)  
        + [WebGoat](https://www.owasp.org/index.php/Category:OWASP_WebGoat_Project)  
    + OWASP Taiwan Week 今年是第一次辦。  
    + 每年 7 月會有個較大型的會議。(OWASP Taiwan Day)  
+ OWASP 旗艦計劃 (OWASP Flagship Projects)  
    + Tools  
        + [OWASP Zed Attack Proxy (ZAP)](https://www.owasp.org/index.php/OWASP_Zed_Attack_Proxy_Project)  
        + [OWASP Web Testing Environment Project](https://www.owasp.org/index.php/OWASP_Web_Testing_Environment_Project)  
        + [OWASP OWTF](https://www.owasp.org/index.php/OWASP_OWTF)  
        + [OWASP Dependency Check](https://www.owasp.org/index.php/OWASP_Dependency_Check)  
    + Code  
        + [OWASP ModSecurity Core Rule Set Project](https://www.owasp.org/index.php/Category:OWASP_ModSecurity_Core_Rule_Set_Project)  
        + [OWASP CSRFGuard Project](https://www.owasp.org/index.php/Category:OWASP_CSRFGuard_Project)  
        + [OWASP AppSensor Project Reference](https://github.com/jtmelton/appsensor)  
    + Documentation  
        + [OWASP Application Security Verification Standard Project](https://www.owasp.org/index.php/Category:OWASP_Application_Security_Verification_Standard_Project)  
        + [OWASP Software Assurance Maturity Model (SAMM)](https://www.owasp.org/index.php/OWASP_SAMM_Project)  
            + <https://github.com/OWASP/samm>  
        + [OWASP AppSensor Project Guide](https://www.owasp.org/index.php/File:Owasp-appsensor-guide-v2.pdf)  
        + [OWASP Top 10 Project](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project)  
        + [OWASP Testing Guide Project](https://www.owasp.org/index.php/OWASP_Testing_Guide_v4_Table_of_Contents)  
+ 建議先從 Flagship Projects 開始看，因為這是很多人吵架的結果。XD  
  
---  
  
## OWASP Top 10 2017 - Henry Hu  
  
+ General introduction to OWASP Top 10  
    + first released in 2003  
    + flagship project  
    + 2004, 2007, 2010, 2013, 2017  
    + a list of the 10 most critical web application security risks  
+ 2017 Timeline  
    + 07/31: Call for Data Open  
    + 10/09: RC2  
    + 11/20: Released  
+ How is OWASP Top 10 generated?  
    + Data proven  
+ Web App by Language in survey  
    + Java: 54%  
    + .NET: 32%  
    + JavaScript 快速成長  
+ Vunlnerability Assessments - HAT vs TAH  
    + Human-Augmented Tools (HAT)  
        + 人去調整工具之後用工具去做掃描  
        + 很多現有的工具都是 foucs 在 XSS，所以掃出來的結果以 XSS 居多。  
    + Tool-Augmented Humans (TAH)  
        + 以人為主去使用工具來做掃描  
        + 發現的漏洞就比較多樣化。  
+ [2017 RC1 Changed](https://www.owasp.org/index.php/Top_10_2017-Release_Notes)  
    + merged 2013-A4: Insecure Direct Object References and 2013-A7: Missing Function Level Access Control back into 2017-A4: Broken Access Control.  
    + added 2017-A7: Insufficient Attack Protection  
    + added 2017-A10: Underprotected APIs  
    + dropped: 2013-A10: Unvalidated Redirects and Forwards  
+ [2017 Golden Master Changed](https://github.com/OWASP/Top10/blob/master/2017/OWASP%20Top%2010%202017%20GM%20(en).pdf)  
    + ADDED  
        + A4:2017-XML External Entities (XXE) is a new category primarily supported by source code analysis security testing tools (SAST: Static Application Security Testing tools) data sets.  
        + A8:2017-Insecure Deserialization, which permits remote code execution or sensitive object manipulation on affected platforms.  
            + Responsible for one of the worst breaches of all time.  
        + A10:2017-Insufficient Logging and Monitoring, the lack of which can prevent or significantly delay malicious activity and breach detection, incident response, and digital forensics.  
    + MERGED  
        + A4-Insecure Direct Object References and A7-Missing Function Level Access Control merged into A5:2017-Broken Access Control.  
    + RETIRED  
        + A8-Cross-Site Request Forgery (CSRF), Frameworks commonly include CSRF defenses, with < 5% of all apps, now #13.  
        + A10-Unvalidated Redirects and Forwards, less than 1% of the data set supports this issue today, now #25.  
+ The Significant of Top 10 2017  
    + Web front-end  
        + Single page application (SPA) wriiten in JS allows the creation of highly modular front end UI/UX  
    + Web back-end  
        + Microservices written in node.js is now the primary interface for legacy application through API and RESTful web services.  
    + [A4:2017-XML External Entities (XXE)](https://github.com/OWASP/Top10/blob/master/2017/en/0xa4-xxe.md) explained  
        + 尤其微軟的 IIS server 的 XML Processor 的設定最有可能有問題  
        + [Billion laughs attack](https://en.wikipedia.org/wiki/Billion_laughs_attack)  
    + [A8:2017 Insecure Deserialization](https://github.com/OWASP/Top10/blob/master/2017/en/0xa8-insecure-deserialization.md) explained  
        + 這次制定的過程中其中一個吵架吵的滿兇的一個  
    + [A10:2017 Insufficient Logging and Monitoring](https://github.com/OWASP/Top10/blob/master/2017/en/0xaa-logging-detection-response.md) explained  
        + 不是只有 web server 而已，應該要把所有的 server log 都納入管轄範圍。  
        + 大部份的 breach 被發現時潛伏期已經拉長到 200 天前的事了，目前很少人會去看到 200 天前的 log，所以這是新的需要去注意的事。  
+ Moving on...  
    + 除了 Top 10 以外，其實有列出總共 50 個 issues，但事實上當然有更多的安全漏洞。  
    + 請不要只看 OWASP Top 10，它不是一切，也不是聖經，在開發網站的時候還要注意更多的安全問題。  
    + 希望各位可以多多參與 OWASP 的社群，因為很缺人。  
  
---  
  
## Client Side Security and Testing Tools - David Cervigni  
  
+ JS Security, topics:  
    + Evolution of client technologies  
    + Why is always more important  
    + Why is always more difficult  
+ Client security is vast  
    + <https://www.owasp.org/index.php/Client_Side_Testing>  
+ XSS  
    + XSS is always dangerous  
        + consequences  
            + XSRF protection bypass  
            + Cookies / session stealing  
            + Defacement  
            + Password / credential stealing  
            + Enumeration  
    + Anti XSS approaches  
        + Classic  
            + Validation  
            + Filtering  
            + HTML Encoding  
            + Encoding lib + Contextual encoding  
        + Requires  
            + Secure coding standards (enforced!)  
            + Knowledge  
            + Design (use the right libs)  
    + Anti XSS evolution  
        + Contextual encoding templates  
            + Very strict  
                + Hard to encode in nested contexts. (double encoding)  
        + Mitigations  
            + CPC: Content Security Policy  
            + ECMAScript security features (e.g. strict mode)  
            + Sandboxing JS (Google CAJA, sanitizer libraries)  
            + Anti XSS browser features WAF  
            + Requires  
                + Secure Application Design  
                + Third parties JS libraries compatibility  
                + Legacy systems?  
+ Code Flow and Taint analysis  
    + Sources  
    + Filters  
    + Sinks  
    + 投影片的字有點小，可能可以直接看[這份文件](https://www.owasp.org/index.php/Static_Code_Analysis)  
+ Tools for JS Code analysis  
    + SCA, static code analysis  
        + Heavy  
        + Difficult  
        + Lower accuracy (false positive)  
        + Adaptability (false negatives... needs custom rules)  
        + Broad language support  
    + Dynamic code analysis  
        + Requires instrumentation  
        + More accurate  
        + Fuzzing capabilities  
    + Integrated them into SDLC (systems development life cycle) and Automation (CI)  
  
---  
  
## 當萬物相遇電信網路：一探邊緣運算的資安議題與解決方案 - 王騰嶽  
  
這個 talk 介紹挺有意思的，  
講了滿多跟電信網路相關的東西，  
平常真的比較少接觸到。  
  
+ [LPWAN (Low Power WAN)](https://en.wikipedia.org/wiki/LPWAN) 與其他 Wireless 技術  
    + [NB-IoT](https://en.wikipedia.org/wiki/NarrowBand_IOT) 是 3GPP 標準的窄帶蜂窩物聯網技術，也是 5G 時代一項重要的實體連結技術。  
        + NB-IoT 只是 3GPP 技術中的一環。  
        + 使用專屬的頻譜，必須要花費。但未來不會有爭奪 NB-IoT 頻譜的問題，因為可以直接使用在電信公司現有的電信網路上。  
    + LPWAN: NB-IoT, LoRa, sigfox, LTE-M, genu, eightless, waviot  
        + 使用開放頻譜，不需要購買，所以品質也就無法保證，但價格會較便宜。  
    + Bluetooth 的限制是不夠遠。  
    + 功耗比 ZigBee 還要低，Range 比 3G/4G/5G 還要遠。  
+ NB-IoT 與電信網路架構  
    + UE, LTE-Uu (NB-IoT 只有在這段）, eNB, GTP-U (S1-U), S-GW, P-GW, Internet  
    + Physical Interface (Last Mile), Backhual, EPC（核心網路）  
    + GTP 的世界：GPRS Tunnel 包覆 IP 封包  
    + 所以使用 NB-IoT 只會在 UE （手機） 和 eNB （基地台） 這段而已  
+ Mobile Edge Computing (MEC)  
    + Mobile Edge  
        + 電信行動網的邊緣（核心網路與基地台之間）  
    + IoT 為何需要搭配 MEC  
        + 如果 device 不太需要上 Facebook / LINE / YouTube  
    + MEC Case  
        + 車聯網  
        + Cache  
            + Content cache 有困難，因為加密太多。  
            + 但 DNS 是可以做的。  
+ IoT 與 MEC 合體之後的資安疑慮  
    + 前情提要  
        + 核心網路內是沒有 IPS 或 Firewall 的  
        + 客戶的手機有被攻擊過嗎？  
            + 沒聽過  
        + 我們手機客戶會攻擊人？  
            + 那不關我的事...  
    + IoT 服務的資安疑慮  
        + 如果電信商真的要提供這樣的服務的話，應該要更正視這樣的問題。  
        + Device 於實體世界被駭，透過 MEC 作為中繼繼續傳播。  
        + Device 運算力弱者，不太可能端點防禦，也不太可能裝防毒軟體。  
        + 在 MEC 與基地台中間安裝 Firewall 或 IPS 就收工了？  
            + 錯，因為有 Tunnel 存在，一定得請電信公司處理。  
    + 建立 MEC 的資安機制  
        + MEC 的平台要提供 IoT 服務進駐  
        + MEC 內各個 IoT 服務（VM 型態）要隔離  
        + MEC 可以直接進行黑名單 IP 過濾  
        + MEC 要轉換 GTP <-> IP 和 GTP termination，於是 IT 產業找到了電信的突破口。  
        + 進入 IP 世界之後：NFV (Network Functions Virtualization) + SDN  
            + VM 監控管理平台  
            + 網路安全設備  
+ Security Framework in MEC Platform  
    + NFV Inftrastructure Security  
    + Network Security  
    + Application Authorization  
+ 講者認為 IoT + MEC + 資安尚未解決的問題對於軟體從業人員是個在未來有許多發展空間的舞台。  
  
---  
  
## Container 與 Web 安全 - 鄭學輝  
  
前半段有點分不清楚是在介紹 Docker 還是在講 container security...  
個人感覺整個投影片比較偏向 Sales Kit...  
  
+ 新興應用安全技術  
    + RUNTIME  
        + Runtime Application Self Protection (RASP)  
    + INTERACTIVE  
    + SOFTWARE  
  
---  
  
## Python as Hacking Tool - Galoget Latorre  
  
原本以為是要現場教學，  
但整場的狀況比較像是，  
前半段推坑 Python，  
後半段 Live Demo 用 Python 寫的 script 的攻擊實況，  
然後提供一些工具供聽眾參考，  
還是沒講要怎麼寫 XD。  
（是說現場直接拿別人的真實個資來 Demo 真的沒問題嗎 www）  
  
+ Python 簡介  
+ 基本 Google Hacking  
+ Some tools  
    + [GitHub - dloss/python-pentest-tools: Python tools for penetration testers](https://github.com/dloss/python-pentest-tools)  
    + [GitHub - andresriancho/w3af: w3af: web application attack and audit framework, the open source web vulnerability scanner.](https://github.com/andresriancho/w3af)  
    + [GitHub - chinoogawa/fbht: Facebook Hacking Tool](https://github.com/chinoogawa/fbht)  
    + [GitHub - IFGHou/wapiti: A web-application vulnerability scanner](https://github.com/IFGHou/wapiti)  
    + [GitHub - OWASP/QRLJacking: QRLJacking or Quick Response Code Login Jacking is a simple-but-nasty attack vector affecting all the applications that relays on “Login with QR code” feature as a secure way to login into accounts which aims for hijacking users session by attackers.](https://github.com/OWASP/QRLJacking)  
  
---  
  
## web swc case study and cyber simulation - 何宜霖  
  
（這場講的條理滿清楚的，但會場座位沒得充電，我的 Mac Book Air 2013 已經沒電了 Orz）  
  
+ 講了釣魚攻擊和水坑攻擊的發生情境  
+ 腳本駭客的常見攻擊手法  
    + [GitHub - beefproject/beef: The Browser Exploitation Framework Project](https://github.com/beefproject/beef)  
+ 一些很基本的卻常常忽略的問題  
    + 裝置預設密碼沒改  
    + 放在 DMZ 東西是否會被外網輕易存取  
    + 網站測試頁面和測試帳號是否有清除  
        + 上傳檔案的測試頁面記得關掉，否則就很有可能會被人上傳後門。  
        + 網路上都有很多現成的後門可以取得了，像是 [GitHub - tennc/webshell: This is a webshell open source project](https://github.com/tennc/webshell)  
+ 物聯網裝置的資安模擬環境會是未來重要的一環  
    + 電腦跟手機可能不是 24x7 連網，但物聯網裝置基本上都是 24x7 連網而且有的還要求網路的 latency 要很低，一被入侵很有可能成為非常大型的 Bot Net。（沒提到前陣子鬧很大的 Mira 病毒）  
+ 然後講者講了一句很有趣的話  
    + > 「社交工程一直都可以成功的原因是什麼？因為人腦的愚蠢是不能進行安全性更新的。」  
  
---  
  
## 結論  
  
今天聽下來真的覺得滿棒的，  
也對 OWASP 更加瞭解了，  
一直以來都只知道 Top 10 而已，  
今天才發現原來還有很多很好用的 Project 和文件，  
才知道原來以前用的 DirBuster 也是 OWASP 的 project 之一。  
打聽一下才發現原來今年 7 月就有個 OWASP Taiwan Day 了，  
但我當時沒有見到任何宣傳消息。  
現在自己的狀況真的就比較像拿資安當興趣而已，  
要當飯吃的話覺得自己的技術力和學習能力都跟不上這個產業啊。  
