Title: MC-SQLR 放大攻擊  
Date: 2015-01-22 15:20  
Author: fkz  
Category: Note  
Tags: DDoS, MC-SQLR, Amplification Attack, Security  
Slug: mc-sqlr-amplification-attack  
Modified: 2015-10-27 11:44  
  
  
在 Twitter 上看到  
  
[HD Moore on Twitter: "MS SQL Server Resolution Service enables reflected DDoS with 440x amplification http://t.co/wAy3szhseR < Still 200k+ vulnerable IPs on IPv4"](https://twitter.com/hdmoore/status/558041881138192386)  
  
---  
  
### 原文連結  
[Default Deny: MC-SQLR Amplification: MS SQL Server Resolution Service enables reflected DDoS with 440x amplification](http://kurtaubuchon.blogspot.tw/2015/01/mc-sqlr-amplification-ms-sql-server.html)  
  
---  
  
大致上是說在 2014 聖誕夜  
有個據信由 Bitcoin Baron 發起的  
針對 the City of Columbia, Missouri 的網站  
進行的 DDoS 攻擊中  
發現大量的 `1434/UDP` 封包  
此類封包的平均大小大約為 441 bytes (含 header)  
封包內容長得像這樣  
  
```  
ServerName;WIN3H1QPRPTOAS;InstanceName;MSSQLSERVER;  
IsClustered;No;Version;9.00.5000.00;tcp;1433;np;  
\\WIN3H1QPRPTOAS\pipe\sql\query;;  
```  
  
經由作者追查後發現  
是 MS SQL Server Resolution Service 所使用的  
稱為 MC-SQLR 的 Protocol  
存在於 MS SQL Server 2000 及其以後的版本中  
client 只要送 1 bytes 的 data 就會讓 Server 回傳此封包  
範例的 python3 sciprt 蠻簡單的  
  
```python  
import socket  
  
HOST_IP = "192.168.1.1"  
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
sock.connect((HOST_IP, 1434))  
qry = bytes.fromhex('02')  
sock.send(qry)  
ans = sock.recv(5120)  
print(ans)  
```  
  
將封包扣除 header 的大小後  
大約是 220 bytes 左右  
所以放大了 220 倍左右  
(此為作者後來修正，原先沒扣掉封包 Header 的平均大小約為 440 bytes)  
攻擊者透過 botnet 並將 source ip 偽造成 victim ip  
向網路上運行此服務的 Public MS SQL Server 發送此種封包  
導致這些 Server 成為 Amplifier  
間接對 victim 造成 DDoS 攻擊  
  
而將此 Resolution Service 關閉會影響一些正常的服務  
所以作者建議不要將有運行此 Service 的 MS SQL Server  
放在 Public Network  
>The behavior exploited in this reflection attack is a key component of the functioning of MS SQL Server 2000 and later.  
>Disabling this service is likely not to be an option.  
>It may be possible to limit the address space to which a server will respond to CLNT_BCAST_EX messages.  
>Most of all, though, owners of SQL Servers should question whether their servers should really be exposed to the internet in the first place.  
  
---  
  
有趣的是  
作者提到在 MC-SQLR protocol documentation 中  
有個關於安全的段落 [5.1 Security Considerations for Implementers](https://msdn.microsoft.com/en-us/library/cc219741.aspx)  
 寫著  
  
> "No security considerations are associated with the SQL Server Resolution Protocol"  
  
他建議 M$ 該修改這部分了XD  
  
  
