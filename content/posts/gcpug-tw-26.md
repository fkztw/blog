Title: GCPUG.tw #26  
Slug: gcpug-tw-26  
Date: 2017-06-02 21:39:53  
Authors: fkz  
Category: Conf/Meetup  
Tags: Google Cloud Platform  
Summary: Note for GCPUG Taiwan Meetup 26  
  
  
Event link: <https://gcpugtw.kktix.cc/events/meetup201706>  
  
---  
  
### GCP Next 2017 recap  
  
#### Keynote  
  
+ Fe-Fe Li  
+ Vint Cerf  
    + TCP/IP  
+ Mac Andreessen  
    + Netscape  
+ Eric Schmidt  
    + Google has spent $30B in building Google Cloud in the past 3 years.  
+ Migrate 到 GCP 的知名企業  
    + Disney  
    + SAP  
    + 高露潔  
    + Verizon  
    + Home Depot  
    + HSBC  
        + 金融業算是對 Cloud 這部份最保守的行業  
    + eBay  
+ 其他重要公佈  
    + 2017 有 4 個新 Region  
    + 2018 有 5 個新 Region  
    + Cloud Spanner beta  
    + Committed-Used Discount  
    + Titan  
    + Dataprep  
    + Video Intelligence API  
        + 進階版的 Vision API  
    + Data Loss Prevention (in G Suite)  
    + CloudSQL w/ PostgreSQL  
  
#### 大會議程  
  
+ Kubernetes  
    + Fast Develop Productivity  
    + Efficient Scale Out  
    + Open Architecture  
    + Serverless / NoOps  
    + Security  
+ Tensorflow  
    + 利用 MINST 的手寫字體作為 demo  
    + Softmax classification  
    + Noisy  
    + Overfitting  
    + Learning Rate Decay  
    + Dropout  
    + <https://goo.gl/pHeXe7>  
    + <https://github.comn/martin-gorner/tensorflow-mnist-tutorial>  
+ Cloud Spanner  
    + Google DoubleClick / AdWords 內部自己在用的服務  
    + Scalabiltiy - 只要把 instance number 改掉  
    + 會自己學習你的 Query Pattern, 自動優化資料  
    + Interleave Table  
        + Table 之間的 Logical relation  
        + Pre-computed JOIN  
    + 也是需要 Warmup  
    + 有人直接拿來取代 MySQL 來用 (Quizlet)  
        + 500GB Data, 8 billions rows  
+ Cloud Storage and Optimization Tuning  
  
#### 教育訓練與認証  
  
+ Codelabs  
    + 各個 Google Cloud 主題的互動式免費教學  
+ GCP 認証  
    + Data Engineer  
        + 設計資料、資料模型  
        + 什麼資料要用什麼服務放  
            + BigTable, BigQuery, Datastore, GCS, ...  
    + Cloud Architect  
        + 架構設計、Solution 選擇  
        + 安全性設計  
        + 成本最佳化 (Cost-down)  
        + 現有服務整合  
        + 要花 200 鎂  
  
#### 技術展示  
  
+ Jupiter Switch  
    + Google 自製的 Data Center Switch  
    + 單櫃有 1300 Tbps 的 throughput  
    + Juniper 最大台的 MX2020 也只有 80 Tbps 的 throughput  
+ Pokemon Go  
    + CRE (Customer Reliability Engineer)  
        + 專案夠大的話，Google 會派工程師去協助該公司解決問題  
    + Datastore 無痛 auto-scaling 50 倍的預期流量  
+ Machine Learning + 農業  
    + 日本人用 Raspberry Pi + Tensorflow 替農夫用電腦來做小黃瓜等級篩選  
+ Evernote 搬家  
    + 在 70 天內搬了 3.5 PB  
    + 提升使用者存取速度  
    + 安全性提升  
    + 搬家的主要原因是為了做 Machine Learning  
+ LUSH  
    + 22 天就把全部環境包含軟體開發流程搬上 GCP  
    + 典型的先用 G Suite 再考慮 GCP 的客戶  
+ Cloud Spanner  
    + 主打 ACID、水平擴展、高可靠度  
    + ...  
+ G Suite  
    + Hangout 改版，主打多人會議功能  
    + 可以 25 個人同時視訊會議  
    + Data Loss Prevention  
    + Jamboard  
  
---  
  
### TensorFlow in the Wild  
  
+ Speaker: [Kaz Sato](https://github.com/kazunori279)  
    + Staff Developer Advocate Data & Analytics, Google Cloud  
  
+ Machine Learning? AI? Neural Network?  
    + Artificial Intelligence  
        + The science of making things smart  
    + Machine Learning  
        + Building machines that can learn  
    + Neural Network  
        + A type of algorithm in machine learning  
+ Neural Network  
    + is a function that can learn  
    + tons of multiply and add  
    + <http://playground.tensorflow.org>  
+ ML at Google  
    + Almost every products in Google use Maching Learning  
    + <https://deepmind.com/blog/wavenet-generative-model-raw-audio>  
        + Generate bit by bit with Neural Network  
    + Deteciton of Diabetic disease  
    + <https://keynote-video-demo.appspot.com/video/barcelona-webm> (Login Required)  
        + 可以分析影片中每一秒出現的物件是什麼，有點像是把每一個 frame 都丟去給 Vision API 後得到的結果  
  
#### Tensorflow  
  
+ Open Source  
+ Easy to use  
+ You can use it to train your own data  
+ Protable and Scalable  
    + Training on  
        + Mac / Windows  
        + GPU Server  
        + GPU cluster / cloud  
    + Prediction on  
        + Android and iOS  
        + RPi and TPU  
+ With great tools like [TensorBoard](https://www.tensorflow.org/get_started/summaries_and_tensorboard)  
+ TensorFlow 1.0 released in Feb 2017  
+ [Keras](https://keras.io/)  
+ [Classifying Manhattan with TensorFlow and BigQuery](https://github.com/kazunori279/TensorFlow-for-absolute-beginners/blob/master/2.%20Classify%20Manhattan%20with%20TensorFlow.ipynb)  
    + <https://github.com/kazunori279/TensorFlow-for-absolute-beginners>  
+ Community and Eco-System  
+ Demo of TensorFlow  
    + [TensorFlow powered Cucumber Sorter](https://cloud.google.com/blog/big-data/2016/08/how-a-japanese-cucumber-farmer-is-using-deep-learning-and-tensorflow)  
        + 電腦也碼ㄟ選小黃瓜  
    + [TensorFlow powered Fried Chicken Nugget Server](http://www.rt-net.jp/karaage1/)  
        + 人工智慧炸雞塊...  
    + [TV popstar face generator with DCGAN](http://memo.sugyan.com/entry/2016/10/12/084751)  
+ TensorFLow in enterprise  
    + The Challenge: Computing Power  
    + Cloud Maching Learning Engine (ML Engine)  
        + Fully manged distributed training and prediction  
        + Scales to tens of CPUs and GPUs  
        + Supports custom TensorFlow Graphs  
        + HyperTune  
    + [Real cases](http://www.techrepublic.com/article/7-companies-that-used-machine-learning-to-solve-real-business-problems/)  
        + Kewpie: Finding the bad potato cubes (by TensorFlow)  
            + A major food manufacturer in Japan  
        + AXA: Finding "large loss" car accidents  
            + TensorFlow gives 78% accuracy  
        + AUCNET IBS  
            + <https://konpeki.io/>  
            + > AUCNET IBS is a car auction service in Japan. The company relies on multiple photos for each vehicle, and they were previously sorted and categorized manually. AUCNET IBS built an image classifier that detects the model of the car and the parts featured in the photo with 95% accuracy.  
+ TensorFlow + BigQuery  
    + Define an UDF to calc similariry  
        + [UDF: User-defined Functions](https://cloud.google.com/bigquery/user-defined-functions)  
  
---  
  
### Google Genomics API 初探  
  
+ Resources  
    + <https://cloud.google.com/genomics/>  
    + <https://github.com/googlegenomics>  
  
#### 相關知識介紹  
  
+ Analogy between biology and computer science  
    + Biology vs Python  
        + Cell == Computer  
        + DNA == *.py source files  
        + Genome == All source files  
        + RNAs == binaries  
        + Proteins == Objects  
        + CRISPR == Sed (i.e. `s/'ATG'//g+`)  
+ Genetic Variation  
    + 每個人都是獨一無二的  
    + 雙胞胎之間仍然有差異  
    + 體質  
        + 吃不胖  
        + 容易得癌症  
    + 4 種核甘酸，20 種胺基酸，RNA encoding 每 3 個對應到 1 個胺基酸  
    + Mis-Sense Mutation  
    + Frame-shift mutation  
        + 有一個核甘酸突然不見了  
    + Genetic variant of ALDH2 makes us red face  
        + <https://en.wikipedia.org/wiki/Alcohol_flush_reaction>  
        + 乙醇無法順利代謝成乙醛  
    + Some drugs works for parts of people  
        + 有些人吃藥沒效  
        + 有些人吃藥會過敏  
            + [Stevens-Johnson syndrome](http://www.mayoclinic.org/diseases-conditions/stevens-johnson-syndrome/home/ovc-20317097)  
+ Precision Medicine  
    + <https://en.wikipedia.org/wiki/Precision_medicine>  
    + 歐巴馬政府提出  
    + 透過個人的基因定序，完全瞭解差異以後，針對個人的基因做的個人化醫療服務  
+ NGS  
    + 基因定序的成本在 2007 年左右突然驟降，自此有將其作為區分點，將之後的定序稱為次世代基因定序  
        + <https://www.genome.gov/sequencingcosts/>  
    + Next-Generation DNA Sequencing  
    + <https://www.ebi.ac.uk/training/online/course/ebi-next-generation-sequencing-practical-course/what-you-will-learn/what-next-generation-dna->  
    + 一人份的基因定序 raw data 平均在 200 GB 左右  
  
  
#### Google Cloud Platform & Google Genomics  
  
+ 實例  
    + MSSNG Project (AUTISM)  
        + <https://www.mss.ng/>  
        + 和自閉症患者相關的協會合作，收集了大量的自閉症患者的基因  
    + Million Veteran Project  
    + Cancer Investigation  
+ How Google Genomics Works  
    + <https://cloud.google.com/genomics/overview>  
    + Store: Google Cloud Storage  
    + Process: Google Genomics  
    + Explore: Google BigQuery  
+ How to use Google Genomics API?  
    + Requirement  
        + BigQuery  
        + Genomics API  
        + Cloud Storage  
    + Start  
        + <https://cloud.google.com/genomics/v1/load-variants>  
        + Create Dataset (To get  
            + `gcloud alpha genomics datasets create --name my-dataset`  
        + Create Variantsets  
        + Import Variants  
            + `gcloud alpha genomics variants import --variantest-id variantset-id`  
        + Check Operation Details  
            + 用 GCP 提供的工具看是不是完成了  
    + Pipelines  
        + <https://cloud.google.com/genomics/v1alpha2/pipelines>  
        + 看了 tutorial 之後，不一定就能套用到自己的 pipeline 上  
    + <https://googlegenomics.readthedocs.io/en/latest/>  
    + Workflow Languages  
        + CWL (Common Workflow Language)  
        + WDL (Workflow Description Language)  
            + <https://github.com/broadinstitute/wdl>  
            + <https://software.broadinstitute.org/wdl/>  
        + Others (Makefile, Snakemake, Nextflow, ...)  
    + Using Cloud ML  
        + <https://github.com/googlegenomics/cloudml-examples>  
+ 討論生物資訊的社群  
    + [Taipei Bioinformatics Omnibus (北-Bio)](https://www.facebook.com/groups/446434039038963/?ref=br_rs)  
