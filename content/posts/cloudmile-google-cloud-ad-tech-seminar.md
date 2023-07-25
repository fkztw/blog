Title: CloudMile Google Cloud Ad Tech Seminar  
Slug: cloudmile-google-cloud-ad-tech-seminar  
Date: 2017-09-22 15:27:22  
Authors: fkz  
Category: Conf/Meetup  
Tags: GCP, Ad Tech  
Summary: Note for <https://www.mile.cloud/Google-Cloud-AD-Tech-Seminar/>  
  
  
## GCP 簡介及 AD Tech 應用趨勢  
  
Speaker: Harry Lin, Google Cloud Customer Engineer Lead  
  
  
+ Challenges  
    + Data lives in silos  
        + 資料是各自獨立的  
    + For marketers - especially difficult to get a single view  
        + Web Analytics, SEM, Ad Server, DSP, ...  
    + Understading your customer?  
        + 資料完全分散，無法連結的話就無法得到有價值的資訊，也就無法瞭解使用者。  
+ How can Google Cloud help you?  
    + Google Analytics  
        + Features  
            + Acquisition & Behaviour Report  
            + Enhanced e-commerce  
        + Scenarios  
            + 有多種不同的資料來源  
                + 有 GA 的資料  
                + 有自己收集的資料  
                + 有跟其他合作伙伴拿到的資料  
        + Insight 1-2-3  
            1. Collect the data  
                + BigQuery Data Transfer Service: Adwords, Double Click, Youtube  
                + Direct Connectivity: Google Analytics 360 Suite, Firebase  
                + Connectivity via Partners: informatica, Segment, talend, ...  
                + 三種途徑將所有的資料都匯入 BigQuery  
            2. Cleanse the data  
                + BigQuery (Raw Data) => Cloud Dataprep (Data Analysts), Cloud Dataflow (Data Engineers) => BigQuery (Clean Data)  
            3. Analyze & Visualize  
                + Analyze: BigQuery, Microsoft Excel, Google Sheets, JDBC/ODBS connectors  
                + Visualize: Google Data Studio, tableau, looker, BI/Analytics  
+ Attribution Modeling: Which of my Channels Drive the Most Success?  
    + Multi-channel  
        + 透過結合不同的 Custom ID，將資料一起灌到 BigQuery 分析，把使用者的行為連接起來。  
            + Youtube, DoubleClick, Adwords, CRM  
        + Cookie based or Session based mapping 得透過 CRM 的 Custom ID 連接  
    + Data lifecycle on Google  
        + Capture  
        + Process  
        + Store  
        + Analyze  
        + Use  
    + Segment high value customers by behaviour  
        + Fantasy Bingers  
        + Action Weekly Tune-ins  
        + Nightly Updates  
        + Touch-and-Go Nature Clippers  
    + Ingest Data into BigQuery  
        + 有乾淨整理好的資料才能訓練出有用的模型，否則只是 garbage in, garbage out.  
        + Indigest Data  
        + Transform Data with Dataflow pipeline  
        + Customer-Segmentation using ML/Clustering  
            + Google Cloud Datalab  
+ Snapchat  
    + QPS second only to Gmail  
    + Bandwidth second only to Youtube  
    + Monetization - Ads and Geofilters  
        + In-App Image Search  
        + 3V - Vertical Video Views  
        + Custom Geofilters  
        + Early Adopters  
  
  
---  
  
## AD Tech 在 GCP 上的應用技術簡介及國外案例  
  
+ Impact of Maching Learning  
    + [資料分析運用四大階段](https://www.hbrtaiwan.com/article_content_AR0007025.html)  
        + 描述型分析：發生了什麼  
        + 診斷型分析：為什麼發生  
        + 預測型分析：未來會不會發生  
        + 指示型分析：如何讓它發生  
    + 汽車業  
        + 物件偵測  
        + 自動駕駛  
    + 醫療業  
        + 醫療影像辨識  
        + 個人化投藥  
    + 金融業  
        + 金融趨勢分析  
        + 異常偵測  
            + 盜刷  
            + 是否被詐騙  
    + 電商  
        + 分析使用者行為  
+ Impact of Ad Tech  
    + 精準投放  
    + Programmatic Buying  
    + Media Planning Flow  
        + What?  
        + Who?  
        + Where?  
        + When?  
        + How much?  
    + Recommendation Engine  
        + 相似廣告推薦  
        + 相似廣告受眾推薦  
        + 即時性推薦  
            + 根據使用者當下的時間點、地點、溫度、溼度做推薦  
    + Personalization  
        + 抓出受眾的各個特徵  
            + 比較不容易得到的是偏向心理層面的特徵，可能得透過平常的行為去進行分析。  
        + 86% 的消費者證實個人化行銷會影響他們的購買決策  
    + Audience Classification  
        + Predict Click  
            + 將有點擊廣告和沒點擊廣告的歷史資訊拿來訓練出模型，之後就可以拿來預測是否會點擊廣告。  
            + 更複雜一點的就可以再加入更多的條件去做分類  
    + Clustering  
        + Lookalike audience  
            + 可以達到不需要浪費過多的資源就達成有效的廣告頭放  
    + Smart Bidding: Right time, Right user, Right bid  
        + Google Adwords: 將行銷列表、時間、瀏覽器、作業系統等等作為競價條件  
        + Real Time Budget Allocation  
            + 不同的時間點設定不同的競價條件，達到即時動態調整預算，節省開銷且提升精準度  
    + Cases  
        + MainAd  
            + 捨棄描述型的分析，採用了預測型的分析  
                + 描述型分析：先競價、再驗收、後預測  
                + 預測型分析：先預測、再競價、後驗收  
        + Jivox  
            + Creative Optimizer  
            + Ad Content Recommendation Engine  
            + Dynamic Audience Scoring  
            + 作法  
                + Know => Personalize => Engage  
+ 總結  
    + 只要有最佳化、預測的需求，就有機會利用 ML 達到最好的成果。  
  
  
---  
  
## Google Cloud Platform 客戶實例分享  
  
+ 禾多  
    + 推播  
    + Firebase  
    + 一天約上百萬到上千萬則推播  
    + Datalab  
        + sklearn, TensorFlow  
+ Koodata  
    + 從 AWS 轉換過來  
    + 機房在台灣，速度比較快  
    + AI 相關應用  
    + 因為有使用 Google Adwords  
+ GMobi  
    + IoT，最近新增了手機廣告平台  
    + 需求：Realtime, Scalibility, Pricing, Reliability  
+ UrAd  
    + Data Source 較多元，得經過非常多的處理。  
    + Data business 相關的架構轉移到 GCP  
        + Pub/Sub  
        + 分析：Dataflow, Dataproc, Dataprep  
        + 儲存：BigQuery, Cloud Storage  
