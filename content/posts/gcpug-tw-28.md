Title: GCPUG.tw #28  
Slug: gcpug-tw-28  
Date: 2017-08-04 21:37:05  
Authors: fkz  
Category: Conf/Meetup  
Tags: Google Cloud Platform  
Summary: Note for GCPUG.tw #28  
  
  
+ Links  
    + <https://gcpugtw.kktix.cc/events/meetup201708>  
  
---  
  
# Running Workloads in Kubernetes - Janet Kuo  
  
今年 2/28 時，[Amazon S3 的 outage](https://techcrunch.com/2017/02/28/amazon-aws-s3-outage-is-breaking-things-for-a-lot-of-websites-and-apps/) 讓很多公司的網站都掛了，  
但有間叫 [Spire 的公司沒受到影響](https://twitter.com/robertjscott/status/836743514423713793)，  
原因是因為用了 Kubernetes。  
  
+ Demo code  
    + <https://github.com/janetkuo/k8s-demos>  
    + <https://github.com/kubernetes/contrib/tree/master/micro-demos>  
+ Architecture of Kubernetes  
    + Master node  
        + Controller  
            + 管理 Worker nodes 上面的 Pod  
    + Worker node  
        + Running Pods  
        + Pull image  
        + 把 Network, Volume 連接起來  
+ Four General Patterns  
    + Stateless  
        + Web frontends  
        + Web servers  
            + NGINX  
    + Stateful  
        + Databases  
            + MongoDB  
        + Message queues  
    + Daemon  
        + Cluster storage  
        + Logs collections  
        + Node monitoring  
        + example  
            + linkerd  
            + fluentd  
    + Batch  
        + Emails to send  
        + Files to zip  
+ Deployment (For stateless pattern)  
    + No persistent states  
        + Scale is easy  
    + Availability > Consistency  
        + Create multiple replicas of the smae pod  
        + Pods are disposable  
    + Rolling update  
        + Update at a controlled rate  
        + Block updates on failure  
        + History and rollback  
    + 用 `kubectl` 下指令，會對 Master node 下一個 async 的指令，Master Node 再透過 controller 去控制 Worker node  
    + Service  
        + 去跟後面的 Pods 溝通  
        + 當有 Pod 掛掉的話，Service 的 load balancer 就不會把 request 導到壞掉的 Pod  
    + Demo code  
        + <https://github.com/janetkuo/k8s-demos/tree/master/dep>  
+ StatefulSet (For stateful pattern, 另外一個專門針對 Stateful 使用的 controller)  
    + 可能的使用情境  
        + ZooKeeper  
    + Store persistent data  
        + Need stable, unique and sticky identity and storage  
    + Consistency > Availability  
        + Create similar pods, each has its own identity and storage  
        + Pods are not disposable  
    + Deploy, scale, terminate  
        + In order or in parallel  
        + 可以設定依序 deploy，因為有些服務不能全部一起開，而是必須照順序開。但如果沒有這個需求的話，還是可以用 Parallel。  
        + StatefulSet 的 Parallel Deployment 是在 k8s 1.7 加入的功能  
    + Rolling update  
        + StatefulSet 的 parallel rolling update 是在 k8s 1.7 加入的功能  
        + 會有 graceful 的 termination，預設的 timeout 時間是 30 秒，如果超過的話，termination 就會被取消。  
    + Demo  
        + <https://github.com/janetkuo/k8s-demos/tree/master/stateful>  
+ DaemonSet (For Daemon Pattern)  
    + One Daemon per node  
        + Background process  
    + Daemons created and removed with nodes  
    + Node labels  
        + Control which nodes daemons should run on  
        + 可以用來控制讓 daemon 只執行在特定的 node 上  
    + Rolling update  
        + 在 k8s 1.6 新增的功能  
    + Demo  
        + <https://github.com/janetkuo/k8s-demos/tree/master/ds>  
+ Jobs (For Batch Pattern)  
    + Run in Parallel  
        + How many pods can be created and running at a time  
    + Run to Completion  
        + How many pods need to complete (exit successfully)  
    + Parallel processing of independent but related work items  
        + Emails to send or frames to render  
    + Job create 出來的 pod 是會結束的，因為事情做完了就會關掉。與前面 3 個 pattern 的 controller 建立的 Pod 不同，如果壞掉了不會幫你重開。  
    + Demo code  
        + <https://github.com/janetkuo/k8s-demos/tree/master/jobs>  
        + parallelism: 一次最多開幾個 pod  
        + completions: 需要幾個成功的 pods 才能停止  
+ 4 Controllers for 4 Patterns  
    + Deployment  
        + Availability  
        + Scale & recover easily  
        + Disposable cpoies of the same pod  
    + StatefulSet  
        + Consistency  
        + Unique, sticky identity and storage  
        + Deploy, scale and terminate in order or in parallel  
    + DaemonSet  
        + One pod per node by default  
        + Daemon pods added and removed with nodes  
        + Use node labels to control  
    + Jobs  
        + Run multiple pods in parallel  
        + Run pods to completion  
            + 只有指定數量的 pods 都成功結束的話，這個 job 才算成功  
+ Where Do I start?  
    + Get a Kubernetes Cluster  
        + GCE  
        + GKE  
        + [minikube](https://github.com/kubernetes/minikube)  
        + [Kubernetes Charts](https://github.com/kubernetes/charts)  
            + Curated applications for Kubernetes  
        + [Kubernetes Helm](https://github.com/kubernetes/helm)  
            + The Kubernetes Package Manager  
+ How Do I Customize?  
    + Kubernetes is extensible  
        + You can write your own controller or use controllers wrote by other people.  
        + Examples  
            + <https://github.com/upmc-enterprises/elasticsearch-operator>  
            + <https://github.com/coreos/etcd-operator>  
+ Kubernetes is Open  
    + <https://github.com/kubernetes/kubernetes>  
    + <https://kubernetes.io>  
    + <https://slack.k8s.io>  
    + <https://twitter.com/kubernetesio>  
+ Q&A  
    + StatefulSet 的 Storage 不會被砍掉，那 DaemonSet 可以有一樣的效果嗎？因為有時候一些 Daemon 會需要這方式。  
        + 可以，但只能讀，不能寫，因為 DaemonSet 的設計上的關係，如果大家都可以寫的話會很亂。  
    + Rolling Update 如果希望新舊版都同時存在的話該怎麼做  
        + StatefulSet 可以透過 Partition 做到  
        + Deployment 的話，可以建立一個新的和一個舊的 Deployment，再透過 Service 的 Load Balancer 去導流量。  
    + Rolling Update 如果不希望新舊版都同時存在的話該怎麼做  
        + StatefulSet 沒辦法做到  
        + 但 Deployment 可以把 strategy 設定成 Recreate，這樣就會先起好新的 pod，然後把舊的砍掉。  
