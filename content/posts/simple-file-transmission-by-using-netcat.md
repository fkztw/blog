Title: Simple File Transmission by using Netcat  
Date: 2014-10-22 06:02  
Author: fkz  
Category: Note  
Tags: CLI, NetCat, nc  
Slug: simple-file-transmission-by-using-netcat  
Modified: 2015-10-28 13:57  
  
  
## Scenario  
  
把檔案從 Server A (傳送方) 傳到 Server B (接收方)  
B(接收方)先用 `nc` 把 port 打開  
下面的 `$TARGETSERVER` 指的就是 B 的 ip  
A(傳送方)再丟檔案過去  
  
---  
  
### 不用打包的話 （單一檔案）  
  
B : `nc -l $PORT > $FILENAME`  
A : `cat $FILENAME | nc $TARGETSERVER $PORT`  
  
---  
  
### 如果需要打包的話 （資料夾）  
  
以 .tar 為例  
  
B : `nc -l $PORT | tar xvf -`  
> 從 `stdin` 收到後直接解開成資料夾  
  
A : `tar cvf - $DIRNAME | nc $TARGETSERVER $PORT`  
  
---  
  
#### 如果傳到B後不想直接解開  
  
ex: 想放在 `/usr/ports/distfiles` 裏面  
  
B : `nc -l $PORT > $DIRNAME.tar`  
> 收到後直接變成 `.tar` 檔  
