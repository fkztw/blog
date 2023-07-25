Title: CP100A: Google Cloud Platform Fundamentals  
Slug: cp100a-google-cloud-platform-fundamentals  
Date: 2016-05-25 20:50:47  
Authors: fkz  
Category: Conf/Meetup  
Tags: Google Cloud Platform  
Summary: [CP100A](https://events.withgoogle.com/cp100a-420770/) 筆記  
Modified: 2016-05-25 22:47  
  
  
# 課程資訊  
  
+ <http://myclass.gcptrain.org/>  
    + OXZnOGVkCg==  
    + <https://sites.google.com/a/google.com/cloud-platform-training/cloud-platform-training/>  
    + <https://sites.google.com/a/google.com/cloud-platform-training/cloud-platform-training/cp100-v2>  
    + [slides.tar.gz](https://drive.google.com/file/d/0B9cCeTKOkfWIaXNqWnNDT0VmaG8/view?usp=sharing)  
  
---  
  
# Course Overview  
  
![CP100 V2: Google Cloud Platform Fundamentals](/files/cp100a-google-cloud-platform-fundamentals/course-overview.png)  
  
---  
  
# Module 1: Introducing Google Cloud Platform  
  
## Why Choose Google Cloud Platform?  
  
+ 你可以在 GCP 看到所有不同 Region 的機器，不用像 AWS 一樣必須切換 Region  
+ 可以直接享用 Google 遍布全球的網路設施  
  
  
## Google's Infrastructure  
  
+ [GCP Next](https://cloudplatformonline.com/next2016-schedule.html)  
    + GCP 的年度會議  
    > 目前似乎辦了兩屆。  
    > 2015 年第一屆辦在日本東京  
    > 2016 年第二屆辦在荷蘭阿姆斯特丹。  
+ 最近在日本新增了 Data Center  
+ Google 的高速 Backbone Network  
+ Points of Presence  
    + 幾乎全球都有節點  
+ Edge Caching  
  
  
## Cloud Regions and Zones  
  
+ Central US  
+ Eastern US  
+ East Asia  
    + Data Center 在彰化  
    + 和 CloudFlare 有合作，最近 CloudFlare 和中華電信合作，在台北有機房。  
    + 所以在臺灣的 latency 蠻低的  
+ Western Europe  
+ <https://cloud.google.com/compute/docs/regions-zones/regions-zones>  
  
  
## Innovative, Customer-Friendly Pricing  
  
+ Sub-hour billing  
    + 以分計費  
    + 不像 AWS 以小時計費，不滿一小時仍然以一小時計費  
+ Sustained-use discounts  
    + 機器開超過一定的時間就會有折扣，採累進的折扣。  
+ Compute Engine custom machine types  
+ 價錢比較便宜，但有夠難算 XDDD  
  
  
## Commitment to Open APIs and Open Source  
  
+ TensorFlow  
+ Android  
+ Go  
+ [Kubernetes](http://kubernetes.io/) (k8s)  
  
  
## The Future of Cloud Computing  
  
+ 1st wave: Colocation  
+ 2nd wave: Virtualized Data Centers  
+ 3rd wave: A global, elastic cloud  
  
  
## IaaS and PaaS  
  
+ IaaS: Compute Engine  
    + Towards managed infrastructure (DevOps)  
+ PaaS: App Engine  
    + Towards managed services (NoOps)  
  
## Google Cloud Platform  
  
![Google Cloud Platform](/files/cp100a-google-cloud-platform-fundamentals/gcp.png)  
  
+ Storage  
    + BigTable  
        + Fully Compatible with HBase  
        + Google 版本的 HBase  
    + Cloud SQL  
        + 最近出了 2.0 (2nd Generation)  
+ Big Data  
    + Pub/Sub  
        + Distributed Message Queue like Kafka  
    + [Dataflow](https://cloud.google.com/dataflow/)  
        + a unified programming model and a managed service for developing and executing a wide range of data processing patterns including ETL, batch computation, and continuous computation.  
    + [Dataproc](https://cloud.google.com/dataproc/)  
        + Spark Cluster  
        + an Apache Hadoop, Apache Spark, Apache Pig, and Apache Hive service, to easily process big datasets at low cost.  
    + Datalab  
        + 基本上就是 Google Cloud 版本的 Jupyter Notebook (IPython Notebook)  
  
### Google Cloud Launcher  
  
+ 和 Bitnami 合作提供的服務  
+ 可以直接在上面直接 Create 設定好的 GCE instance  
  
  
## Lab 1  
  
+ [Sign Up for the Free Trial and Create a Project](https://codelabs.developers.google.com/codelabs/cp100-free-trial/#0)  
    + [Stackdriver](https://cloud.google.com/stackdriver/)  
        + monitoring, logging, & diagnostics  
        + 可以整合 GCP 和 AWS  
    + [Cloud Launcher](https://console.cloud.google.com/launcher)  
        + <https://cloud.google.com/launcher/docs/#deploying_a_software_package>  
        + 點下去可以直接幫你 create 安裝好該服務的 GCE instance，簡單來說就是已經預先做好 Image 然後直接幫你塞進去。  
            + 我原本以為是可以複選，然後一次幫你安裝剛剛選的那些服務到一台 GCE instance 上，但看來是比較提倡分散式就是了，當然這樣在 Production 上會比較好，不然一台 instance 炸了就所有服務都炸了 XD  
  
  
## 補充  
  
+ Project 的管理  
    + Members 的 account 可以採用 gmail.com, apps for work 的 account, Google Groups 的 account, service account  
    + 一個帳號可以管理多個 project  
    + 管錢的和管 Project 的帳號可以分開設定  
    + 可以考慮多開不同的 Project，一來是 Quota 的限制比較不會那麼吃緊，二來是 Permission 的設定可以比較不需要那麼費心，如果全部的 Team 都擠在同個 Project 的話，Permission 的設定可能得多費心調整。  
+ Billing  
    + Sustain Pricing 在遇到 billing account change 的時候會重算，所以  
    + 可以設定 budget，超過的時候會通知，每個服務也都可以設限。  
  
  
---  
  
# Module 2: Getting Started with Google Cloud Platform  
  
## Cloud Computing  
  
```  
Compute Engine --- Container Engine --- App Engine --- Cloud Endpoints  
IaaS ------------- Clusters -------- Managed VMs (beta) -------- PaaS  
Configurability DevOps <-----------------------------> Agility NoOps  
```  
  
+ IaaS  
    + Compute Engine == AWS EC2 == Virtual Machine  
        + Raw compute granular control  
        + 可以使用預先提供好的 Image，也可以自己建好 Image 再上傳來用  
+ PaaS  
    + App Engine  
        + 最早出來的時候是只有 Python  
        + 有漲價過，當時一堆人離開  
        + 後來又有一些人回來用，支援 Java, Go, PHP, Python  
        + 最近 Beta 開始支援 Ruby  
    + Cloud Endpoints  
        + Preset run-times  
        + Focus app logic  
+ SaaS  
+ [Google APIs Explorer](https://developers.google.com/apis-explorer/#p/)  
    + 只要是 Google 的服務基本上都會有 API  
  
  
## Lab 2  
  
+ [Getting Started with Google Cloud Platform](https://codelabs.developers.google.com/codelabs/cp100-cloud-launcher/#0)  
  
---  
  
# Module 3: Google App Engine and Google Cloud Datastore  
  
## Google App Engine  
  
### What is Google App Engine  
  
+ Managed runtimes for specific versions of Java, Python, PHP and Go. (Standard Runtime)  
+ Autoscale workloads to meet demand  
    + 可以透過 app.yaml 去做 autoscale 的設定  
    + 也可以透過 app.yaml 對 instance class 做設定，預設是用最低階的 F1，可以參考 [app.yaml Reference|Python|Google Cloud Platform](https://cloud.google.com/appengine/docs/python/config/appref#scaling_elements)  
+ Free daily quota, usage based pricing  
+ Local SDK for development, testing and deployment  
+ Need to conform to sandbox constraints  
    + No writing to the local filesystem  
    + Request timeouts at 60 seconds  
+ 補充  
    + 可以透過 version 來控管每個 service (原本叫 module，最近改叫 service 了）  
    + 可以透過 split traffic 做 A/B testing  
    + 有類似 rolling update 的機制  
        + Deploy 新的 version 後，GAE 會自動幫你把舊版本的 instance 關掉，然後開新的版本的 instance  
    + 可以讓開發者專注在發開程式，不用費心在建置環境的部份  
    + 實例：  
        + Snapchat  
            + 用 App Engine  
            + 只花流量的費用，不存圖片，超省成本。  
  
  
### App Engine Standard Environment  
  
+ Managed runtimes for specific versions of Java, Python, PHP, Go.  
    + 目前只支援 Python 2  
+ Autoscale  
+ Free daily quota, usage based pricing.  
+ 原本 support 一天發 2000 封 email，但現在收回來了，現在要在 GCP 上寄信的話，統一都要使用 [SendGrid](https://sendgrid.com/)，會有比較嚴格的審核，避免大量的垃圾信件。  
    + AWS 也採用 SendGrid，蠻多 Cloud Platform 都把寄信的部份交給它。  
+ 跟 Google 的很多服務都有滿完整的整合。  
+ GAE 的設計理念是服務要愈 light weight 愈好  
+ GAE 的內建服務  
    + Memcache  
        + 免費的會有 crash 的風險，不會幫你把 data 復原。  
        + 付費的會在 crash 的時候幫你把 data 復原。  
    + Taskqueues  
        + 用來設計保證該 task 一定會被完成的架構  
    + Scheduled tasks  
        + cron.yaml  
    + Blobstore  
    + Search  
    + Logging  
  
  
### App Engine Flexible Environment (GAE Managed VM)  
  
+ 用 container 來處理  
+ 沒有 sandbox 的限制  
+ 可以做到支援 Python 3  
+ During beta pricing based on GCE  
+ Local Development relies on Docker  
  
  
### GAE Standard vs Flexible Environment 比較表  
  
![GAE Environments](/files/cp100a-google-cloud-platform-fundamentals/gae-environments.png)  
  
  
# Google Cloud Endpoints  
  
+ Build your own API running on App Engine Standard  
+ Expose your API using a RESTful interface  
+ Includes support for OAuth 2.0 authorization  
+ Generate client libraries  
+ Supports Java and Python server-side code  
+ Includes App Engine features  
    + Scaling  
    + Denial of service protection  
    + High availability  
+ Supports iOS, Android, and JavaScript  
+ 補充  
    + 可以自動 generate client library  
    + 目前 support Java 跟 Python  
    + 直接 apply GAE 的一些 feature  
    + HA  
    + Support iOS, Android and JavaScript clients  
    + 但因為是在 GAE 上在堆疊一層，所以當量很大的時候，效能可能要注意一下  
  
  
## Google Cloud Datastore  
  
+ Daily free quota  
+ Database designed for application backends  
+ NoSQL store for billions of rows  
+ Schemaless access, no need to think about underlying data structure  
+ Local development tools  
+ Automatic scaling and fully managed  
+ Built-in redundancy  
+ Supports ACID transactions  
+ RESTful API  
+ Includes a free daily quota  
+ Access from anywhere through a RESTful interface  
+ 補充  
    + 有 autoscale 的能力，會對應 GAE 的數量來去調整  
  
## Lab 3  
  
+ [Deploying Applications Using App Engine and Cloud Datastore](https://codelabs.developers.google.com/codelabs/cp100-app-engine/)  
    + <https://github.com/GoogleCloudPlatformTraining/cp100-bookshelf>  
  
---  
  
# Module 4: Google Cloud Platform Storage Options  
  
## Google Cloud Storage  
  
+ Not a file system (but can be accessed as one via 3rd party tools such as GCS Fuse)  
    + <https://github.com/GoogleCloudPlatform/gcsfuse>  
    + IO 不快  
+ Simple administration and does not require capacity management  
+ All storage options accessed through the same APIs and include client libraries  
    + JSON API  
    + XML API  
        + 可能是因為 AWS S3 是用 XML API，所以也要跟著提供一下。  
+ 補充  
    + 硬碟上的資料是有做 encryption 的  
    + 容器是以 bucket 為單位  
  
  
### Cloud Storage Classes  
  
![Cloud Storage Classes](/files/cp100a-google-cloud-platform-fundamentals/cloud-storage-classes.png)  
  
+ Standard  
+ DRA  
    + 可以限制資料的區域  
+ Nearline  
    + 經常變動的資料不適合存在這裡，cost 會增加。  
    + 比較適合拿來做 backup, archive, 長久性不太會變動的資料。  
+ 這 3 個 classes 存取的 API 是相同的  
  
  
### Cloud Storage Features  
  
![Cloud Storage Features](/files/cp100a-google-cloud-platform-fundamentals/cloud-storage-features.png)  
  
### Cloud Storage Integration  
  
+ BigQuery  
    + Import and export tables  
+ Compute Engine  
    + Startup scripts, images and general object storage  
+ App Engine  
    + Object storage, logs, Datastore backup  
    + App Engine 本身不能存資料，但可以存在 Cloud Storage 和 Datastore  
+ Cloud SQL  
    + Import and export tables  
+ 可以拿來直接 serve static websites.  
  
  
## Google Cloud Bigtable  
  
+ NoSQL database service for large-workload applications (Terabytes to Petabytes)  
    + 不便宜  
        + 貴在 Node 執行時間的收費，目前是 $1.95 USD/hour per node  
        + 最少必須開 3 個 node  
    + 是儲存在 SSD 上  
        + 最近開始可以選擇儲存在普通硬碟上了，Storage 的費用會降低大概十倍。  
+ Protected  
    + Replicated storage  
    + Data encryption in-flight and at rest  
    + Role-based ACLs  
+ Proven  
    + Gmail and Google Analytics  
+ 補充  
    + 高 IO, 可在最短的時間內查到最多的資料  
    + Gmail 和 Google Analytics 的背後也是用 Bigtable  
    + 很多做股票交易的也是用 Bigtable  
    + 很貴但反應快  
    + 主要是為了取代 HBase  
  
  
### Google Cloud SQL  
  
+ Google-managed MySQL  
+ Pay-per-use model  
+ REST API for management  
+ Affordability and performance  
    + 有 class 可以選擇，視需求可以調整  
+ Google security  
+ Vertical scaling (read and write)  
+ Horizontal scaling (read)  
+ Seamless integratin with GAE and GCE  
+ 補充  
    + 第一代的 performance 不是那麼好  
    + 第二代則是選擇 run 在 container 上  
    + 所有要連線來的 IP 都需要經過 white list  
        + 有個例外是 App Engine，可以直接連線，不會被白名單限制。  
        + 可以設定讓 Cloud SQL 綁定 GAE，讓它開在跟 GAE 同個 region，用來降低 Latency  
    + 七天一個 cycle 的 backup  
  
  
### Cloud SQL Features  
  
+ Familiar with MySQL  
+ Flexible pricing  
+ Google Security  
    + [AES-128 encryption](https://cloud.google.com/sql/faq#encryption_manage)  
+ Managed backups  
+ Automatic replication  
    + master-slave  
    + 自動化 replication  
    + 一個 instance 掛掉的話，會有 downtime 但會再開另外一個 instance 去接替，有基本的 HA 功能。  
+ 支援 SSL 的 connection  
  
  
### Cloud SQL Second Generation  
  
+ Same features as first generation with higher performance, storage capacity at lower cost.  
    + Up to 7X throughput and 20X sotrage capacity of first generation instances  
    + Less expensive than first generation for most use cases.  
+ 補充  
    + 如果想要開比較小的 DB 的話可以考慮用 2nd generation，性價比會比較高。  
    + 如果是要用很大的 DB 的話，建議用 1st generation 讓 Google 幫忙管理會比較好。  
  
### Comparing Storage Options  
  
![Comparing Storage Options](/files/cp100a-google-cloud-platform-fundamentals/comparing-storage-options.png)  
  
  
## Lab 4  
  
+ [Integrating Applications with Google Cloud Storage](https://codelabs.developers.google.com/codelabs/cp100-cloud-storage/)  
  
---  
  
# Module 5: Google Container Engine (GKE)  
  
## What is a Container  
  
+ Virtualization at the operating system layer  
+ Separates operating system from application code and dependencies  
+ Isolates individual processes  
+ Popular implementations include Docker and [rkt](https://coreos.com/rkt/docs/latest/)  
    + k8s 目前支援這兩種格式的 Container  
+ OS => Shared Libraries => Contianer  
    + 安全性問題  
        + 會不會影響到別的 Container  
        + 把 kernel 弄爛了的話，別的 Container 也會一起爛掉。  
  
## Why Use Container?  
  
+ Support consistency across development, testing, and production environments  
+ Loose coupling between application and operating system layers  
+ Much simpler to migrate workloads between on premises and cloud environments  
+ Support agile development and operations  
  
## [Kubernetes (k8s)](http://kubernetes.io/)  
  
+ Open Source  
    + <https://github.com/kubernetes/kubernetes>  
+ Google 的服務是跑在 [Borg](http://blog.kubernetes.io/2015/04/borg-predecessor-to-kubernetes.html) 上面，Borg 是 k8s 的前身。  
+ 另外一個 Container 是 [dcos](https://dcos.io/)  
    + <https://github.com/dcos/dcos>  
  
### Features of k8s  
  
+ Workload portability  
    + Run in many environments, across cloud providers  
    + Implementation is open and modular  
+ Rolling updates  
    + Upgrade application with zero downtime  
+ Autoscaling  
    + Automatically adapt to changes in workload  
+ Persistent storage  
    + Abstracts details of how storage is provided from how it is consumed  
    + 有支援 MySQL Cluster  
+ Multi-zone clusters  
    + Run a single cluster in multiple zones  
    + Alpha on Google Cloud Platform  
+ Load balancing  
    + External IP address routes traffic to correct port  
    + Google 會幫你偵測機器的狀態，在機器死掉的時候幫你做 Migration  
  
### Google Cloud Container Engine (GKE)  
  
+ Based on open source Kubernetes(k8s) orchestration system  
+ Orchestrate and schedule Docker containers  
+ Consumes Compute Engine instances and resources  
+ Uses a declarative syntax to manage applications  
    + JSON, YAML  
+ Decouple operational and development concerns  
+ Manages and maintains  
    + Logging  
    + Health management  
    + Monitoring  
    + Scaling  
+ 補充  
    + 不只在 GCP 可以用，AWS 或是自己架都可以，因為是 Based on Open Source 的 k8s  
    + 可以執行很多 Container，彼此可以透過 k8s 達到 HA  
    + 目前的費用是算在 Compute Engine 上，因為實際還是開 GCE 然後在上面 run containers  
    + 目前以 GCE 的收費方式計價  
    + Google Cloud Container Builder  
        + Create Docker container images from app code in Google Cloud Storage  
    + Google Container Registry  
        + Secure, private Docker image storage  
        > 沒記錯的話 images 是存在 Cloud Storage 上  
    + <https://cloud.docker.com/>  
  
  
## Lab 5  
  
+ [Deploying Applications Using Google Container Engine](https://codelabs.developers.google.com/codelabs/cp100-container-engine/#0)  
  
---  
  
# Module 6: Google Compute Engine and Networking  
  
## Google Compute Engine  
  
+ Run large-csale workloads on virtual machines hosted on Google's infrastructure  
+ Robust networking features  
    + 可以拿來做 MySQL cluster load balancer  
+ Instance metadata and startup scripts  
    + 每個 instance 會有 global 的 metadata 和各自的 metadata  
    + startup script 也是放在 metadata 去做描述  
+ Persistent disk snapshots  
+ High CPU, high memory, standard and shared-core machine types  
+ HTTP and network load balancing  
    + 可以針對 Load Balancer 做個別的設定，會比 AWS 簡單。  
+ Advanced APIs for auto-scaling and group management  
+ Innovative pricing  
    + per *minute* billing, sustained use discounts  
    + Preemptible instances  
    + High throughput to storage at no extra cost  
    + Custom machine types - Only pay for the hardware you need  
+ 補充  
    + Google 用 KVM 來實作這部份  
    + 可以在兩分多鐘內就開啟 1000 台機器  
        + 壓力測試跑了大概一個多小時，最後收到帳單大概是 500 美金左右。  
    + 硬碟必須至少要 200 GB 才會有一般的 performance, < 200 GB 的話會比較慢。  
    + 目前看到比較多的是拿來當 Load Balancer  
    + 目前 Load Balancer 使用 BSD 是會有問題的，因為缺少某些 Linux 才有的 Libraries。  
  
  
## Google Cloud Networking  
  
### Google Cloud Interconnect  
  
+ Carrier Interconnect  
+ Direct Peering  
    + 需要有第 2 類電信執照才能申請  
    + Connect your business directly to Google  
    + 所有流量的費用打對折，速度會更快，適合擁有 Data Center 的公司申請。  
  
  
### Google Cloud VPN  
  
+ Secure connection over the Internet  
+ Securely connect your network to Google Cloud Platform using IPsec VPN connection  
+ Encrypts traffic over the Internet  
+ Google Cloud Router supports dynamic routing between Google Cloud Platform and your network  
  
  
### Google Cloud DNS  
  
+ Highly available and scalable DNS  
+ Translates domain names into IP addresses  
+ Create managed zones, then add, edit, delete DNS records  
+ Programmatically manage zones and records using RESTful API or command- line interface  
  
  
### Google Cloud Load Balancing  
  
+ HTTP(s) load balancing  
+ Balance HTTP-based traffic across multiple Compute Engine regions  
+ Global, external IP address routes traffic  
+ Scalable, requires no pre-warming and provides resilience, fault tolerance  
+ TCP/SSL and UDP (network) load balancing  
    + Spread TCP/SSL and UDP traffic over pool of instances within a Compute Engine region  
    + Ensures only healthy instances handle traffic  
    + Scalable, requires no pre-warming  
+ 補充  
    + Global  
        + 可以在不同的 region 建 load balancer  
    + HTTP(S) load balancing  
    + Network load balancing  
        + 支援 Auto scaling  
        + 可以設定 protocol 跟 port  
    + 可以選擇 client IP + Protocol 的規則，看要導到哪台 Load Balancer  
    + 有隱藏 CDN 的功能，可以把 CDN 的功能打開。  
  
  
## Operations and Tools  
  
### Google Stackdriver  
  
+ Integrated monitoring, logging, diagnostics  
+ Works across Google Cloud Platform, Amazon Web Services  
+ Open source agents, integration  
+ Powerful data, analytics tools  
+ Collaborations with PagerDuty, BMC, Splunk, others  
+ 補充  
    + 可以針對條件去設定 alert  
  
#### Cloud Monitoring  
  
+ 可以監控各種項目  
+ 可以自訂要監控哪些部份  
+ 可以和第三方應用程式銜接  
  
#### Cloud Logging  
  
+ 可以幫你很輕鬆的檢視不同機器的 log  
+ Log 線上保留三十天  
+ 支援 Export，讓你可以自己處理 Log  
  
  
### Google Cloud Deployment Manager  
  
+ Infrastructure management service  
+ Create a .yaml template describing your environment and use Deployment Manager to create resources  
+ Provides repeatable deployments  
+ 補充  
    + 有點類似 Ansible 和 Chef  
  
  
### Google Cloud Source Repositories  
  
+ Fully-featured Git repositories hosted on Google Cloud Platform  
+ Supports collaborative development of cloud apps  
+ Includes:  
    + Source code editor  
    + Integration with Stackdriver debugger  
  
  
### Google Cloud Functions  
  
+ Create single-purpose functions that respond to events without a server or runtime  
    + Event examples: New instance created, file added to Cloud Storage  
+ Written in Javascript, execute in managed Node.js environment on Google Cloud Platform  
  
  
## Lab 6  
  
+ [Deploying Applications Using Google Compute Engine](https://codelabs.developers.google.com/codelabs/cp100-compute-engine/#0)  
  
---  
  
# Module 7: Big Data and Machine Learning  
  
![Big Data Services](/files/cp100a-google-cloud-platform-fundamentals/big-data-services.png)  
  
+ Fully managed, No-Ops Services  
+ BigQuery  
    + 一個 column 就儲存一個 object，不是存 row。(column based)  
        + 不要下 `select *`，會很慢，而且很貴，因為會對 process 的資料量收費。  
    + 每次 query 就透過 mapreduce 去做 macthing  
    + 可以透過 SQL-like 的語法(GQL)去查詢 big data  
    + [Apache drill](https://drill.apache.org/)  
+ Pub/Sub  
    + 建立一個 big data 用的 queue  
    + 比較常用的案例是 IoT  
    + 可搭配 dataflow 作 big data 的運算  
+ Dataflow  
    + 幫你整理資料  
+ Dataproc  
  
  
## Big Data  
  
### Google BigQuery  
  
+ Fully-managed analytics data warehouse  
    + provides a service for near real-time interactive analysis of massive datasets (hundreds of TBs)  
+ Query using a SQL-like syntax (GQL)  
+ Only pay for storage, processing used  
+ Zero administration for performance and scale  
+ Supports open standads  
+ 補充  
    + 當作 storage 和 analyze 的工具  
    + 類似 [Cassandra](https://cassandra.apache.org/)  
    + Column-based  
    + 1 TB 的資料大概花 6 秒就可以 scan 完  
    + 一次會幫你開很多機器去做運算，最後吐回一個結果給你  
    + 切忌用 `select *`  
    + 有 dry run 可以先告訴你這個 Query 下下去會花多少錢  
  
  
### Google Cloud Pub/Sub  
  
+ Scalable and reliable messaging for Google Cloud Platform and beyond  
+ Supports many-to-many asynchronous messaging  
+ Includes support for offline consumers  
+ Based on proven Google technologies  
+ Integrates with Cloud Dataflow for data processing pipelines  
+ Uses push/pull subscriptions to topics  
+ Use cases:  
    + Building block for data ingestion in Dataflow, Internet of Things (IoT), Marketing Analytics  
    + Foundation for Dataflow streaming  
    + Push notifications for cloud-based applications  
    + Connect applications across Google Cloud Platform (push/pull between Compute Engine and App Engine)  
  
  
### Google Cloud Dataflow  
  
+ Managed service for executing scalable and reliable data pipelines  
+ Write code once and get batch and streaming  
    + Transform-based programming model  
+ Clusters are sized for you  
+ Processes data using Compute Engine instances  
+ Integrates with GCP services like Cloud  Storage, Cloud Pub/Sub, BigQuery, Bigtable  
+ Open source Java and Python SDKs  
+ Use cases:  
    + ETL (extract/transform/load) pipelines to move, filter, enrich, shape data  
    + Data analysis - batch computation or continuous computation using streaming  
    + Orchestration - create pipelines that coordinate services, including external services  
        + 可以很容易的和其他服務整合  
  
### Google Cloud Dataproc  
  
+ Fast, easy, managed way to run Hadoop and Spark/Hive/Pig on Google Cloud Platform  
+ Benefit from cloud integration  
    + Cloud Storage  
    + Stackdriver  
+ Customize and configure clusters using initialization actions  
+ Create clusters in 90 sec or less  
+ Dataproc clusters billed minute-by-minute  
    + Save money using preemptible instances for batch processing  
+ Scale clusters up and down even when jobs are running  
+ Developer tools  
    + RESTful API  
    + Integration with Google Cloud SDK  
+ Use cases:  
    + Easily migrate on-premises Hadoop jobs to the cloud  
    + Quickly analyze data (like log data) stored in Cloud Storage - create a cluster in less than 2 minutes then delete it immediately  
    + Use Spark/Spark SQL to quickly to perform data mining and analysis  
        + Spark SQL 可以讓你比較好操控資料  
    + Use Spark Machine Learning Libraries (MLlib) to run classification algorithms  
        + Spark 最強的部份就是 MLlib，但之後可能會被 Google 推出的 TensorFlow API 取代掉也不一定  
+ 補充  
    + Cluster  
    + HDFS work node  
    + 完整的 Hadoop 類型服務  
    + 可以在 WebUI 上面選擇 node 數目  
    + 要自己寫 mapreduce  
    + 支援直接撈 Cloud Storage 的資料，甚至可以把資料送到 BigQuery  
    + create cluster 後要 submit job，只要寫好 mapreduce 和 jar 檔，就可以直接幫你處理資料  
  
  
### [Google Cloud Datalab](https://datalab.cloud.google.com/)  
  
+ Interactive tool for large-scale data exploration, transformation, analysis, visualization  
+ Analyze data in BigQuery, Compute Engine, and Cloud Storage using Python, SQL, and JavaScript  
+ Easily deploy transformation, analysis models to BigQuery  
+ Integrated, open source  
    + Runs on Google App Engine  
    + Built on Jupyter (formerly IPython)  
    + Use Google Charts or matplotlib for easy visualizations  
+ Code, documentation, results, visualizations in intuitive notebook format  
+ 補充  
    + 可以透過 Google 去銜接很多 Datasource，可以做整合，例如匯出報表。  
    + 有支援 BigQuery, Cloud Dataflow，可以利用他們去做分析  
    + 用法跟 Jupyter Notebook 差不多  
    + 是使用 Managed VM 來用 Datalab，該 VM 會裝一些套件，然後透過 GAE 去操作。  
        + 安裝好後會變成 GAE 裡頭的其中一個 service  
  
  
## Machine Learning (Google Cloud ML)  
  
+ [Vision API](https://cloud.google.com/vision/)  
+ [Speech API](https://cloud.google.com/speech/)  
+ [Translate API](https://cloud.google.com/translate/docs/)  
+ [Prediction API](https://cloud.google.com/prediction/)  
+ Google Cloud Machine Learning Use Cases  
    + Structured Data  
        + Classification / Regression  
            + Customer churn analysis  
            + Product diagnostics  
            + Forecasting  
        + Recommendation  
            + Content personalization  
            + Product X-sells/up-sells  
        + Anomaly Detection  
            + Fraud detection  
            + Asset sensor diagnostics  
            + Log metric anomalies  
    + Unstructured Data  
        + Image Analytics  
            + Identify damaged shipments  
            + Explicit content classification  
            + Identify “styles” in images  
        + Text Analytics  
            + Call center log analysis  
            + Language identification  
            + Topic classification  
        + Sentiment analysis  
  
## Lab 7  
  
+ [Getting Started with BigQuery](https://codelabs.developers.google.com/codelabs/cp100-big-query/#0)  
  
---  
  
# Questions  
  
+ 一個帳號可以管理的 Project 上限是多少？  
+ GAE serving static 不用開 instance?  
+ Project migration 的建議  
+ Bigtable 和 BigQuery 的主要差異  
+ GKE 的 MySQL cluster  
+ GAE 的 Front-end instances 跟 Back-end instances 的差別  
  
> 其實還有很多問題啦，只是沒有太多時間可以問，  
> 而且要在網路上發問又必須描述的很詳細，  
> 然後 Facebook 又是個黑洞，很難找之前的發文內容，  
> 實在不太喜歡拿 Facebook 來問問題。  
> 所以可能就自己 Google 、親自實驗或之後有機會再在 GCPUG.tw 當面問吧  
  
---  
  
# 相關連結  
  
+ <https://www.facebook.com/groups/GCPUG.TW/>  
    + 臺灣的 Google Cloud Platform User Group，有問題歡迎在上面發問討論。  
+ [Google Cloud Platform Pricing Calculator | Google Cloud Platform](https://cloud.google.com/products/calculator/)  
    + GCP Pricing 試算  
+ <https://github.com/GoogleCloudPlatformTraining>  
    + GCP 教材的 Lab code  
  
---  
  
> 有種吃了 GCP 大還丹的感覺，需要時間消化。  
> 能夠在上班時間來 Google Taipei 上課實在太棒了！  
> 謝謝同事 Finley 一直被我煩被我問問題 XD  
> 感謝老闆 Teddy，也感謝辛苦的講師 Simon。  
