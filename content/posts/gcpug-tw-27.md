Title: GCPUG.tw #27  
Slug: gcpug-tw-27  
Date: 2017-07-05 21:46:56  
Authors: fkz  
Category: Conf/Meetup  
Tags: Google Cloud Platform  
Summary: Note for GCPUG Taiwan meetup #27  
  
  
Event link: <https://gcpugtw.kktix.cc/events/meetup201707>  
  
---  
  
## Using Kubernetes to deploy Django in GCP  
  
Speaker: Walter Liu  
Slides: <https://www.slideshare.net/walterliu7/using-kubernetes-to-deploy-django-in-gcp>  
  
+ [Statefulset](https://kubernetes.io/docs/tutorials/stateful-application/basic-stateful-set/)  
    + Beta feature since k8s 1.7  
    + Sharding Service  
    + 還是得設定 service 給他，不然 DNS lookup 會找不到  
    + Like deployment with static POD name  
    + Usage: Sharded service  
        + redis  
        + memcached  
    + Other usage: static volume  
+ Secret / ConfigMap  
+ Service  
+ Ingress  
    + Global Load Balancer  
    + No firewall ability  
+ k8s has no crontab (currently)  
    + Use Celery  
    + Use crontab in Google App Engine  
+ k8s + GCP Load Balancer  
+ Cluster creation steps  
    + `kubectl create -f web_secretes.yaml`  
    + `kubectl apply -f cache_stateful_set.yaml`  
    + `./titan_control deploy prod`  
        + Like => `kubectl apply -f prod_web_deploy.yaml`  
    + `kubectl apply -f service.yaml`  
    + `kubectl apply -f ingress.yaml`  
    + `gsutil mb -l asia gs://static.example.com`  
    + 要記得檢查該開啟來的 service 有沒有開起來  
+ 遇到的問題  
    + Templating  
        + Use Python Jinja to do k8s templating  
        + Someone had suggested me to use [HELM](https://github.com/kubernetes/helm)  
        + Show templating example  
  
---  
  
## 深入 Kubernetes Network，Calico Overlet Network 介紹  
  
Speaker: 光光  
Slides: <https://www.slideshare.net/IsaacTseng/20170705-kubernetes-with-calico>  
  
+ k8s cluster network  
    + inside a pod  
        + App & DB connection with local network  
            + 因為在同個 Pod 走內網，所以不會有 performance 的問題  
    + pod-to-service  
        + Conneciton via Service  
            + 不會有啥太大的問題  
    + external-to-service  
        + Conneciton via Service  
            + 不會有啥太大的問題  
    + pod-to-pod  
        + Pod & Pod may in different hosts  
        + How to connect two Pods?  
        + 這會是今天主要探討的部份  
+ Overlay network  
    + Flannel  
        + CoreOS 使用 [Flannel](https://github.com/coreos/flannel)  
        + All pockets go through Flannel  
+ Performance  
    + Overlay vs Underlay  
+ User story  
    + IPsec Tunneling  
        + 在內部網路仍然使用 IPsec Tunneling 導致 throughput Performance 下降了約 80%  
        + 為了想要解決這個問題，所以用上了 Calico  
    + [RancherOS](http://rancher.com/rancher-os/)  
        + <https://github.com/rancher/os>  
+ [Calico](https://github.com/projectcalico/calico)  
    + <https://www.projectcalico.org//>  
    + Features  
        + Use etcd  
        + BGP Routing  
        + Pod get routings to other Pod  
        + Packets not over Calico  
    + How to use  
        + Kubelet settings: `--network-plugin=cni`  
    + CoreOS 的相容性不太高，要做網路層的實體 binding 的話會比較複雜，可能需要多注意一點。  
    + [Daemon Set](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/)  
    + `kubectl apply -f calico.yaml`  
    + `kubectl get pod --namespace=kube-system`  
    + 為什麼選 Calico 不選 Flannel?  
        + 因為 Flannel 是 Overlay Network，而且不在 CoreOS 裏面用的話會很麻煩  
    + 為什麼 GCP 比 Calico 更好？  
        + GKE 是執行在 GCE 裏面，然後 Network 是直接跟 GCE 作 bridge，所以 Pod 之間的溝通會很方便。  
        + 但會有個問題，如果要做一些安全性的限制的話會比較麻煩，因為大家的網路都是 bridge 在一起，所以比較難針對這點去做限制。  
        + 如果有這方面的考量的話，建議不要直接用 GKE，但可以試著在 GCE 上安裝 Calico 來使用。  
    + Calico node 會去處理他擁有的 IP，寫在 etcd 裡頭。BGP peering 之後，IP 就可以共享。  
+ BGP Peering  
    + 可以透過 BGP Peering 的方式，把 Pod 之間相連起來。  
+ 有興趣的人也可以去玩一下 GCP 上的 [Container-Optimized OS](https://cloud.google.com/container-optimized-os/docs/)  
  
---  
  
## 從 AWS 轉移到 GCP，一個新創團隊搬家的故事: TABLEAPP Architecture Story  
  
Speaker: 陳彥文  
Slides: <https://www.slideshare.net/wenchen3/from-aws-to-gcp-tableapp-architecture-story>  
  
幫一家新創公司解決 Server 維護上的問題  
  
+ 找出問題  
    + 展開完整架構  
    + 列出操遇到的狀況  
    + 儘可能開啟所有 log  
    + 分析狀況來源  
+ 選定改善目標及檢驗標準  
    + 降低成本  
    + 資源使用效率  
    + 減緩月支出成長速度  
+ Other Benefits of Docker  
    + Version Control  
        + push code and build  
        + every commit has its own images  
    + Lightweight  
    + Isolation  
    + Portable  
+ How about K8S on EC2?  
    + Deploy kubernets on EC2  
        + Maintain Kubernetes yourself  
            + Install  
            + Testing  
            + Updating  
            + and ...  
            + Kubernetes updates really fast  
        + Handle auto-scaling manually  
            + Remove pods before remove ec2  
        + Using CI to deploy image  
        + Set up logging and monitoring policy  
        + Integrate AWS resource and Kubernetes manually  
            + It must be scalabel  
    + It sucks...  
+ Kubernetes on GCP is awesome  
    + GKE  
        + Easy  
        + Full managed  
            + even update kubernetes  
        + Logging and Monitoring support (stackdrive)  
        + Automatic and configurable cluster scaling  
        + Google Cloud Platform resource integration  
    + Architecture  
        + [GCP](https://www.slideshare.net/wenchen3/from-aws-to-gcp-tableapp-architecture-story/17)  
        + [Inside k8s](https://www.slideshare.net/wenchen3/from-aws-to-gcp-tableapp-architecture-story/18)  
        + [Deployment](https://www.slideshare.net/wenchen3/from-aws-to-gcp-tableapp-architecture-story/19)  
        + [Log Collection](https://www.slideshare.net/wenchen3/from-aws-to-gcp-tableapp-architecture-story/20)  
        + > 這架構挺棒的，雖然不大，但把可以用的都用上了，可以學習一下。  
+ Cost and Usage  
    + Hybrid 時期的 cost 有比較高  
    + 後來做完 migration 到 GCP 之後，cost 比在 AWS 上降一半，然後 handle 的 request 量多 5 倍。  
+ Conclusion  
    + CloudCDN is really fast  
        + very low latency  
    + Lower price  
        + based on new arch, we save 40% cost  
    + 平台終究只是工具，人才是最大的關鍵。  
