Title: 在 Arch Linux 上將 Docker 的 Storage Driver 從 devicemapper 改為 overlay2 以釋放硬碟空間  
Slug: change-docker-storage-driver-from-devicemapper-to-overlay2-to-free-your-disk-space-on-arch-linux  
Date: 2018-01-16 23:19:02  
Authors: fkz  
Category: Note  
Tags: Docker, devicemapper, overlayFS, Arch Linux, 2018 iT 邦幫忙鐵人賽  
Summary: 拋棄 `devicemapper`，釋放你的硬碟空間。  
Modified: 2018-01-17 05:05:02  
  
  
## TL;DR  
  
<https://wiki.archlinux.org/index.php/Docker#Storage_driver>  
  
---  
  
## 前言  
  
因為硬碟空間只剩 1.8 GB，在清硬碟空間的時候發現 `/var/lib/docker/devicemapper` 佔了 35 GB，以前同事在 Mac 上遇過，但一直找不到啥好解法，這次自己遇到了，於是就花了點時間查了一下。  
  
先是用了 `docker system prune -a` 把所有東西都清掉，結果發現 `/var/lib/docker/devicemappe` 的大小只有減少 1 GB，但明明用 `docker info` 檢查， Data used 就只剩 KB 而已，於是跑去找 Arch Wiki。  
  
得到 Storage Driver 最好不要用 `devicemapper` 的答案，新安裝的預設應該都會是 `overlay2` 了，發現自己的 docker 仍舊是使用 `devicemapper`，所以乾脆動手修改一下。  
  
---  
  
## 步驟  
  
+ `systemctl stop docker` 把 dockerd 關了  
+ 因為我已經用 `docker system prune -a` 把東西全砍了，所以就沒備份必要，直接 `sudo rm -rf /var/lib/docker` 了  
    + 這個時候硬碟就多出了 35 GB 啦！  
+ `systemctl edit docker` 編輯設定檔  
    + 如果 root 使用的 editor 非平常慣用的話，可以先 `export EDITOR=vim` 再使用 `sudo -E bash -c "systemctl edit docker"` 來編輯  
    + 應該會開啟 `/etc/systemd/system/docker.service.d/override.conf` 或其暫存檔  
    + 新增以下內容，將 Storage Driver 指定成 `overlay2` 後存檔離開：  
  
```  
[Service]  
ExecStart=  
ExecStart=/usr/bin/dockerd -H fd:// -s overlay2  
```  
  
+ `systemctl start docker` 重新開啟 dockerd  
+ `docker info | head` 裡頭應該要有一行 "Storage Driver: overlay2" 這樣就成功了  
  
---  
  
## 補充  
  
+ [Select a storage driver | Docker Documentation](https://docs.docker.com/engine/userguide/storagedriver/selectadriver/)  
    + 這篇官方文件講述有哪些 Storage Driver 可供選擇以及各 Storage Driver 支援的 File System 格式  
    + 包含：`aufs`, `devicemapper`, `overlay`, `overlay2`, `btrfs`, `zfs`  
    + 我自己是沒有詳細研究所有 Storage Driver 的優劣就是  
+ [Use the OverlayFS storage driver | Docker Documentation](https://docs.docker.com/engine/userguide/storagedriver/overlayfs-driver/)  
    + 這篇官方文件則講述怎麼把 Storage Driver 設定成 `overlay` 和 `overlay2`  
    + 建議是能用 `overlay2` 就別用 `overlay`  
    + 也講了 `overlay` 和 `overlay2` 的運作原理，還有效能和限制方面的部份  
  
---  
  
## 參考來源  
  
+ [Docker - ArchWiki](https://wiki.archlinux.org/index.php/Docker#Storage_driver)  
+ [Use the OverlayFS storage driver | Docker Documentation](https://docs.docker.com/engine/userguide/storagedriver/overlayfs-driver/)  
+ [Select a storage driver | Docker Documentation](https://docs.docker.com/engine/userguide/storagedriver/selectadriver/)  
