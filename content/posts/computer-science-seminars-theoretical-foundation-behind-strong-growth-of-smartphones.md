Title: 資訊工程研討 - Theoretical Foundation Behind Strong Growth of Smartphones  
Date: 2013-11-12 07:14  
Author: fkz  
Category: Course  
Tags: Video, Audio, Security, Network  
Slug: computer-science-seminars-theoretical-foundation-behind-strong-growth-of-smartphones  
  
  
## Title: Theoretical Foundation Behind Strong Growth of Smartphones  
## Speaker: [黃正能 / 華盛頓大學電機系教授](http://www.ee.washington.edu/faculty/hwang/)  
  
---  
  
* Qualcomm's Awareness  
* AT&T's Digital Home/Life  
* Wearable Computing and Bendable Display  
    * Google glass - 華大教授三、四年前被 google 挖角過去做的東西  
    * Samsung bendable display  
* [Apple TV AirPlay](https://www.apple.com/airplay/) and [Google Chromecast](http://www.google.com/intl/en/chrome/devices/chromecast/#netflix)  
    * display device 不需要永遠都在 mobile device 上  
    * google chromecast USD$35.00  
* Transparent Smart Windows  
  
---  
## What are Theoretical Foundations behind these technology?  
  
### Energy Efficient + CPU, GPU  
#### SoC Based Powerful Engine  
Qualcomm SnapDragon 600  
  
#### CPU + GPU  
根據不同狀況使用 CPU 或 GPU  
  
#### Power Efficient Design  
+ 省電  
+ Thermal Design Power  
+ Leakage 的耗電越來越大  
  
#### Run-Time System-Level Energy Self-Optimization  
+ Optimization - 控管 Device 內的各個 chip  
  
### Standarlize  
### Audio  
#### Human Psychoacoustics  
+ Hearing Sensitivity - 只聽得到對 20~20000 Hz 的頻率  
+ Frequency Masking - 某個頻率的聲音特別明顯的時候，會聽不到這段時間其他頻率的聲音  
    + Saving More Bits with Frequency Masking  
+ Temporal Masking - 某段時間音量特別大的話，會聽不到在這段時間前後的其他聲音  
  
利用上述這三點作為音頻壓縮技術的基礎  
  
#### Audio Coding Standards  
+ MP3 (128Kbps)  
+ AC3  
+ AAC (64Kbps)  
+ HE-AAC (48 or 24 Kbps)  
  
### Video  
#### Digital Video Coding  
+ Digitize  
+ Infra-frame compression (Simlliar to JPEG)  
    +  A DCT Based Intra-Frame Encoding  
        + img -> DCT -> Quantize -> Zig-zag -> ...  
    + Coding Block  
    + Motion Vector Search - 拿 difference 去作 DCD 再作壓縮，省略掉重複的部份  
+ Symbol Entropy coding - 機率因素  
+ Rate Control  
  
#### Video Coding Evolution  
+ MPEG-2 - 1994  
+ AVC/H.264 - 2003  
+ AVC Scalable Extension  
+ HEVC/H.265 - 2013  
H.265 用 50% 的 bitrate 壓縮出來的效果跟 H.264 100% bitrate 差不多  
  
#### Multi- and Free-View of Video Scenes  
+ Users can dynamic select and viewpoint they want to use  
+ Virtual Viewpoint Not Captured by the real camera - 可以透過多個 Camera 模擬出實際上不是由真的 Camera 拍攝出來的視角  
  
---  
## What will be 5G?  
  
1991 - Voice - SMS - 2G  
2001 - App - SNS - 3G  
2009 - Big Data - Cloud - 4G  
2020 - ??? - ??? - 5G #沒記到- -"  
  
### Earlier Generations of Mobile Technologies  
+ 2G  
+ CDMA  
+ Hive technology  
  
### Toward ALL-IP 4G Wireless  
+ LTE (Long Term Evolution) of 3GPP  
+ WiMAX  
+ 4G  
  
### OFDM & OFDMA  
### Channel Quality Dependent Scheduling  
### MIMO (Multiple Input Multiple Output)  
簡單來說，就是多支天線彼此之間的合作，讓收訊更好。  
#### SD(Spatial Diversity) & SM(Spatial Multiplexing)  
#### Coordinated MIMO  
甚至使用不同的基地台讓收訊更好  
#### Adaptive Modulation & Coding (AMC)  
加入調變或 error correction code 讓收訊的效果更好  
#### QoS(Quality of Service) and QoE(Quality of Experience)  
+ Packet lost  
  
### Scheduling and Resource Allocation  
透過安排，讓收訊品質更好  
### Heterogeneous Wireless Networks  
透過一些小裝置合作，達到更好的無線收訊品質  
  
---  
## Secured and Right Protected Usage  
### Digital Right Management (DRM)  
+ DRM License Server - 認證  
  
### What is Encryption  
+ Symmetric encryption (secret key cryptography)  
+ Asymmetric encryption (public key cryptography) - 為了要傳送 secret key  
  
#### Secret Key  
+ DES - IBM  
+ AES - NIST  
+ Fast and efficient  
+ to use public key cryptography only to a private secret key  
  
#### Public Key  
+ RSA (明天要考密碼學期中考 還只能用手算 現在看到這個真的超親切的啊)  
  
---  
## Conclusion  
+ Smartphones will evolve to all kinds of wearable devices, sensors, attached to our bodies (wireless chargeable), and displays are avaailable anywhere surrounding us.  
+ HCIs(speech, gesture, facial, etc) will replace keypads  
+ Internet of things(IoTs) will be all ubiquitous in our living environment  
+ Information are collectd, indexed, and available in/from clouds  
  
作 low power 技術的教授都被 Google 挖走了XDD  
  
---  
# Academic Research: It is Easier Than You Think  
## Important Features (M2I4) You should have  
如果你想唸研究所的話，希望你有以下的特質  
+ Motivation: really enjoy digging deeper into the scientific truth  
+ Maturity: never afraid of being failed or left alone  
+ Innovation: always think of what is (or can be) new and different?  
+ Intelligence: filter useful information to become usable knowledge  
+ Independence: a step-by-step problem formulation and module solving  
+ Integrity: always be honest in reporting and research  
  
## Getting Ready for Research  
+ Research topics selection and switching  
    + Extend from senior graduate students' topics  
    + Existing research projects in the Lab  
    + Something your advisor is willing to learn closely with you  
+ Depth knowledge  
    + A good series of class taking, or self study related tutorial background  
    + Most updated Conference/Journal papers ([IEEE Xplore](http://ieeexplore.ieee.org/Xplore/home.jsp))  
    + Joint project discussions and group collaborations, or new class offering  
+ Breadth Knowledge  
    + Attend technical presentation and active questioning (key messages?)  
    + Magazine and Hi-Tech News  
    + 到最後很多領域會殊途同歸，都會彼此相關，所以有機會的話可以瞭解一下其他領域在做什麼，尤其是一些 Conference。  
    + 透過瞭解其他領域的新聞及期刊，可以瞭解到整個市場的趨勢。  
    + 研究生有人去面試的時候，被問到的問題剛好是他在聽同學的 group meeting 時聽到的。  
  
## Jumping into Research  
+ Extensive literature **survey** and problem formulation  
+ Summarize others' paper in their **block diagrams** (flow charts) - look for weak links or not convincing blocks  
    + 看完別人的 paper 以後，要有辦法自己畫出剛剛那篇 paper 的 block diagram ，如果畫不出來的話，代表你還不夠瞭解那篇論文在幹嘛。  
+ Conclusion meet the original problem formulation?  
+ Methodologies: integration -> evolution -> revolution  
+ Always use the data and compare the results with the most recent or best reported results  
+ Clear and detailed interpretation of simulation results  
    + 做完 simulation 以後，要把結果好好想清楚，再跟自己的 leader 討論，而不是把整個 simulation 的結果原封不動的丟出來。  
+ Confidence and leadership building (organized speech in group or individual meetings)  
    + 出去就業後不該是只幫別人寫程式碼，而是應該當個 leader ，因為研究給你訓練就是如此。得到一個新的題目、開始 survey、嘗試、失敗，這是你已經學到的東西，所以你應該已經瞭解如何處理，所以你應該當個 leader。  
  
## Persistence in Research  
+ Never expect a smooth path, refine the research scopes all the time (backoff slightly to find brighter road ahead)  
+ Learn from any failure  
+ Never hide from your professor  
  
## Research Publications and Technical Reports  
+ Practice Engilish writing of thesis and papers: **practice by mimicking**  
+ Always seek publication opportunities: from conferences to periodical journals  
    + 自己主動去找有什麼地方可以投稿。  
+ Learn the standard **writing style and outline** of manuscript (a good outline, 70% done!)  
    + 能夠把自己大綱全部列出來，並且瞭解大綱在做什麼，這樣大概就完成百分之七十了。  
+ Learn from the grammatical errors corrected by your advisor or technical editing persons.  
    + 寫論文的文法很重要，設法知道老師幫你改了哪些部分，並從中學習。  
+ Discuss clearly the flow charts and simulation results in your papers, never leave the weak links  
+ **Never be afraid/frustrated of major/minor revision of paper submission - reviewers are never your enemies**  
    + 別人有什麼意見的話要用心傾聽，如果有好的意見的話就記得要更改。  
