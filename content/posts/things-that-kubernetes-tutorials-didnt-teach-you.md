Title: Things that Kubernetes tutorials didn't teach you  
Slug: things-that-kubernetes-tutorials-didnt-teach-you
Date: 2020-07-11 16:24:41  
Authors: fkz  
Category: Note  
Tags: Kubernetes, K8s 
Summary: Sum-up for my experience about using Kubernetes in production.


**NOTE: This was written in July, 2018, maybe something has changed.**

+ Code as Infrastructure? Code decides Infrastructure.
    + Writing bad code could crash your pod.
    + Code with good performance could save your money.
+ HPA default sync period is 30 secs
    + Too long for some bursts which cause high loading peak.
    + If you are using GKE, you cannot change this.
+ Bad liveness probe settings could destory high availability
    + If your condition is way too scrict, your pod will keep restarting.
+ `minReadySecs` and `initialDelaySecs` are important.
    + Without these two settings, your users might get 502 Bad Gateway Error while rolling update.
+ `maxSurge` and `maxUnavailable`
    + Rolling update speed and availability
+ `targetCPUUtilizationPercentage`
    + Is the CPU utilization percentage of the node that pods are running on.
+ `terminationGracePeriodSeconds`
    + <https://pracucci.com/graceful-shutdown-of-kubernetes-pods.html>
+ Resources
    + CPU and Memory threshold is very important.
    + Pods will be killed if you set the threshold too low.
    + It's a waste if you set the threshold too high.
+ Tools
    + `kubectx`, `kubens`
        + <https://github.com/ahmetb/kubectx>
        + Faster way to switch between clusters and namespaces in kubectl
        + Really useful when you have more than 2 namespaces.
