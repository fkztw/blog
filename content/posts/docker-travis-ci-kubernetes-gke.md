Title: Docker + Travis CI + Kubernetes + GKE  
Slug: docker-travis-ci-kubernetes-gke  
Date: 2018-01-10 22:15:19  
Authors: fkz  
Category: Note  
Tags: Docker, Kubernetes, Travis CI, 2018 iT 邦幫忙鐵人賽  
Summary: 紀錄一下透過 Travis CI  build Docker image 之後，再 Deploy 到 GKE 上的方法。  
Modified: 2018-01-11 17:01:19  
  
  
## 前言  
  
這篇是 2016 年 6 月時的紀錄，當時剛接觸 Docker 和 Kubernetes 4 個月左右，在把舊的服務根據性質拆分成 3 個不同的 mircro serverices，想要做到讓 Travis CI 在跑完測試後，自動 build Docker image，再把 image 丟到 Google Cloud Platform 上，讓 GKE 使用。  
  
當時還沒有 Google Cloud Builder 可以使用，所以在找尋解法的時候看到果然有人已經這麼做了。以下就來紀錄一下方法。  
  
---  
  
## 概要  
  
學 Kubernetes 的時候找到了這簡短的文章：[Orchestrating Docker with Kubernetes](https://chengl.com/orchestrating-docker-with-kubernetes/)，覺得可以讓剛上手的人快速瞭解。  
  
至於透過 Travis CI 自動 build image  的部份，照著這篇文章做的確有成功：[Docker Workflow](https://chengl.com/docker-workflow/)（其實看這篇文章的 `.travis.yml` 就可以瞭解整個梗概了），但發現效果不盡理想，儘管已經拆分成 base image 和 production image，在每次 build image 的時候節省掉 build base image 的時間了，但花的時間還是太久。  
  
當時因為被抓去做其他事，這部份就只弄到這裡，我覺得滿可惜的，後來大家都還是在 local build image 然後再透過 Makefile 把指令包裝起來，在 local 這邊透過 kubectl 把 image push 到 GCP。  
  
---  
  
## 後續  
  
當時過了幾個月後，在 2016 年 9 月看到這篇文章：[在 Travis 實現 Docker Cache | 小惡魔 - 電腦技術 - 工作筆記 - AppleBOY](https://blog.wu-boy.com/2016/09/docker-cache-on-travis/)，才發現原來有這樣的解法可以用。  
  
後來發現也有很多人遇到一樣的問題，後來也大多是用 `docker save`, `docker load` 解決:  
  
+ [Docker cache on Travis and Docker 1.12 // Read at G's // A personal blog from Giorgos Logiotatidis.](https://giorgos.sealabs.net/docker-cache-on-travis-and-docker-112.html)  
+ [Caching Docker Images on Build · Issue #5358 · travis-ci/travis-ci · GitHub](https://github.com/travis-ci/travis-ci/issues/5358)  
+ [Faster Travis CI tests with Docker cache](http://atodorov.org/blog/2017/08/07/faster-travis-ci-tests-with-docker-cache/)  
+ [performance - Cache docker images on Travis CI - Stack Overflow](https://stackoverflow.com/questions/35305492/cache-docker-images-on-travis-ci)  
  
---  
  
## 參考來源  
  
+ [Orchestrating Docker with Kubernetes](https://chengl.com/orchestrating-docker-with-kubernetes/)  
+ [Docker Workflow](https://chengl.com/docker-workflow/)  
+ [在 Travis 實現 Docker Cache | 小惡魔 - 電腦技術 - 工作筆記 - AppleBOY](https://blog.wu-boy.com/2016/09/docker-cache-on-travis/)  
