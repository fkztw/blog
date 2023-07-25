Title: AWSUGTW Meetup 10th Note  
Slug: awsugtw-meetup-10th-note  
Date: 2016-04-19 19:40:08  
Authors: fkz  
Category: Conf/Meetup  
Tags: AWS, AWSUGTW, EC2, Serverless, Meetup  
Summary: Note for 2016/04/19 AWSUGTW Meetup 10th  
Modified: 2016-04-20 00:03  
  
  
<http://awsugtw.kktix.cc/events/10-tpe>  
  
---  
  
# Best practices for AWS ECS and Serverless  
## Speaker: Pahud  
  
### AWS EC2 Container Service (ECS)  
  
+ ECS Cluster  
    + ASG (Auto Scaling Group)  
        + on-demand  
        + spot instance (85% off compare to on demand ASG)  
    + CloudWatch  
+ Auto Scaling Policy Design  
    + `30%-60%`: scale out spot  
    + `>= 60%`: scale out on-demand  
    + `below 30%`: scale in spot  
    + Simple tip  
        + on-demand 打底，spot 伸縮。  
        + spot fleet if you need couples of instances (for RTB)  
+ [SQS (Job queue)](https://aws.amazon.com/sqs/)  
+ [internal / external ELB](https://aws.amazon.com/elasticloadbalancing/)  
+ [CloudWatch Logs Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/QuickStartEC2Instance.html)  
    + Chat Ops  
+ [ECR - EC2 Container Registry](https://aws.amazon.com/ecr/)  
  
  
### [Load Balancing on Random Ports](http://www.slideshare.net/JulienSIMON5/amazon-ecs-january-2016/12)  
  
+ Meteor Galaxy  
    + session-aware with random ports  
  
  
### Is there a way to move code in cloud native way?  
  
+ "No server is easier to manage than no server."  
+ Event-driven Cloud Computing  
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)  
+ [AWS API Gateway](https://aws.amazon.com/api-gateway/)  
+ [Amazon Kinesis](https://aws.amazon.com/kinesis/streams/)  
    + persistent  
+ [DynamoDB](https://aws.amazon.com/dynamodb/)  
    + 可以搭配 AWS Lambda 使用，幫忙 Archive  
+ [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)  
+ [AWS SNS](https://aws.amazon.com/sns/)  
  
  
### Mobile Integration  
  
手機安裝 SDK，可以直接使用 AWS Lambda  
支援 RequestResponse(Sync), Event(Async)  
可以直接丟 json payload  
  
如果不要直接跟 AWS Lambda 互動的話  
可以透過 API Gateway 使用 HTTPS RESTful API  
  
可以使用 Service Proxy Integration  
透過 IAM assume role 去達成  
  
  
### API Gateway Call Flow  
  
```  
User =>  
Internet =>  
Amazon CloudFront (保證最佳 routing) =>  
API Gateway => API Gateway Cache  
            => Amazon CloudWatch Monitoring  
            => Endpoints on Amazon EC2  
            => Any other accessible pubilc data.  
```  
  
  
### Pros and Cons  
  
+ Pros  
    + cloud native with you business code in AWS Lambda  
    + 不需要維護 infra  
    + leverage AWS PaaS infrastructure at scale  
    + custom or federated authorization  
        + 接到 request 後，可以先丟到某個 AWS Lambda 作 Authorization 當作 Authorization module  
        + 或是 AWS Lamdba 轉到預先寫好的或已經存在的認証系統請求 Authorization  
    + very minimal cost for small-medium teams  
        + AWS Lambda: 30M requests $11.53  
        + AWS API Gateway: 1M requests $4.23  
        + <http://www.slideshare.net/CaseyLee2/serverless-delivery>  
+ Cons - Lambda Limit  
    + Lambda soft limit concurrency is 100  
        + 調高的話必須要申請，預設是只有 100，為了防止你不小心寫錯程式導致帳單爆表 (?)  
        + 300 seconds max duration per invocation  
        + Lambda in VPC restriction  
            + Private IP addresses  
            + ENIC limit (default 20*5 == 100)  
                + 會用掉一張虛擬網卡  
+ Cons - API Gateway is Expensive  
    + 500-1000 QPS per AWS Account  
    + 5M requests/month == $18.79  
    + 100 QPS == $974.07/month == 31,350 NTD  
+ Cons - Performance  
    + push and pull invocation model of Lambda  
    + -> delegation with higher memory  
        + 用一個專門的 AWS Lambda，只從 stream 抓東西出來，丟給別的 AWS Lambda 做邏輯處理。  
    + No connection pooling  
        + Container 只有在第一次啟動的時候會 loading 最一開始初始化的部份  
        + 之後被 reuse 的時候會直接進 handler  
        + 所以不要把 conneciton 放在 code 一開始的部份，否則很可能會常常看到 conneciton 沒有正常 close，造成 TCP overhead.  
+ Cons - Development  
    + CloudWatch debugging is slow.  
    + Immature CI/CD toolchains  
    + lack of PHP, Ruby and Golang  
    + re-deploy the whole bundle could be a pain.  
        + 萬一 bundle 的大小超過 20~30 MB 的話有個解法  
            + 把 bundle 丟到 S3 裡面後，寫支 AWS Lamdba 幫你把這包 bundle 丟到另外一個 AWS Lambda 做處理  
  
  
### When should I use ECS and when for Serverless?  
  
+ When to use ECS  
    + Financial concern - When you have traffic more than 100+ QPS  
    + Operation concern - Long running process or API service  
    + Language concern - Golang, PHP, Ruby, etc.  
    + Performance concern  
    + Protocol concern  
+ When to use Serverless  
    + Small project, simple business logic  
    + focus on the code only  
    + no infra management  
    + stateless  
    + quick micro services implementation  
  
  
### Conclusions  
  
+ 儘可能把服務 container 化  
+ Build stateless application  
+ Immutable architecture  
    + every computing conponent can be replaced and scaled with no impact  
+ Focus on your business logic, instead of the infra, forget your infra  
+ Try not use any EC2, if necessary, avoid SSH into EC2 for manual operation.  
    + 不要想要救任何一台機器，應該要儘可能做到 stateless，只要壞掉就抽換掉。  
    + 抱著這樣的想法，比較能夠設計出夠彈性化的架構。  
+ Fully-managed and fully-automation is the way to go.  
  
---  
  
# Interview Quiz w/o Servers  
## Speaker: Cliff Lu  
  
### 用 AWS 架設低成本的面試系統  
  
+ Interview Automation  
+ [超過 90 秒的都要自動化！](http://www.bnext.com.tw/ext_rss/view/id/1099271)  
+ 考量  
    + 效能  
    + 管理  
    + 費用  
+ AWS API Gateway + Lambda + S3  
+ AWS Lambda  
    + Serverless computing service  
        + Support Python, Node.js, Java  
            + Python 在上面沒有 share memory 可用，所以 multiprocess library 無效，得用 os.fork。  
        + Managed, AWS 負責 HA and Scalability  
    + `/tmp` 有 512MB 可用  
    + 若 24/7 運行 (128MB)，費用與 t2.nano 差不多  
    + 觸發與權限設置詳見文件  
+ AWS API Gateway  
    + Managed HTTPS API Gateway  
    + 權限設計頗複雜，說明文件寫的蠻糟的，必須詳讀文件。  
  
---  
  
# 心得  
  
第一次參加 AWS 的聚會，也算是第一次認真接觸 AWS 啦。  
畢竟之前也就只有在參加 Conf 還有一些閒聊的時候聽到些名詞。  
只有懵懵懂懂的瞭解，印象最深的就是 AWS 有一堆自創的 service name，讓我不是很喜歡。  
雖然公司目前都在用 GCP ，但還是會想瞭解一下 AWS 的內容。  
希望之後對 GCP 和 AWS 都足夠瞭解之後，  
可以有辦法自己歸納瞭解 GCP 和 AWS 之間的優缺點，  
無論是在 Performance, Scalability, Pricing, Flexibility 等等。  
畢竟如果要朝 Architect 走的話我想這是不可少的。  
如果能力足夠的話可能還會再看看 Azure 吧。  
不過目前看來應該還是會以 GCP 為主  
希望之後研究夠深入的話可以有機會成為 GCP 相關 Library 的 contributor，  
只是當個 User 的話實在是有點無趣。  
  
話說 AWSUGTW 感覺蠻用心在經營的，  
挑的 CLBC 夠寬敞（跟我常去 Taipei.py 用的那個 CLBC 差好多 QQ），  
備有額外的茶點，而且免場地費。（真好奇錢從哪來的 XD)  
還會請參加者填寫問卷收集回饋意見。  
跟我最近參加過的 Taipei.py 跟 GCPUGTW 比起來算是比較會讓新加入者比較想繼續來的那種。  
（而且女生好多，Taipei.py 只有一點點，GCPUGTW 完全沒有 XDDD）  
不過沒啥人問問題，讓我不知道參加者到底是有沒有聽懂，  
不過會後感覺蠻多人私底下去找講者討論的，應該只是不想或不敢當面問吧？  
然後沒看到平常跑社群的熟面孔，  
果然不同的 User Group 就是不同的生態圈啊。  
