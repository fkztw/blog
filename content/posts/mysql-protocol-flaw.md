Title: MySQL client 預設允許 MySQL Server 讀取本地端的檔案  
Slug: mysql-protocol-flaw  
Date: 2019-01-22 03:17:54  
Authors: m157q  
Category: Note  
Tags: MySQL, Security  
Summary: MySQL 的協定在設計上有瑕疵，導致了一些安全性問題。  
  
  
這篇算是個翻譯兼摘要文，  
今天看到原文覺得有趣就追了一下，  
原文在此：<https://gwillem.gitlab.io/2019/01/20/sites-hacked-via-mysql-protocal-flaw/>  
  
---  
  
## TL;DR  
  
MySQL 協定上的瑕疵  
預設讓 Server 可以讀取 Client 上有讀取權限的所有資料  
導致有心人士可以寫一個加了點料的 MySQL server  
當你連上它的時候你的東西就被它看光光了  
  
- 原因：mysql-client 的 `LOAD DATA LOCAL` 預設是 Enable  
- 解法：記得改成 Disable  
- 官方文件：<https://dev.mysql.com/doc/refman/8.0/en/load-data-local.html>  
  
[目前據報 mysql-client 8.0 預設沒這問題，因為 `LOAD DATA LOCAL` 預設是 Disable 的。但 5.5, 5.6, 5.7 預設都是 Enable 的。](https://twitter.com/ColeWippern/status/1086974610246193152)  
  
有些 ORM framework 預設是有幫忙 Disable `LOAD DATA LOCAL` 的，但不是每個都有，開發者要注意一下。  
  
---  
  
## 玩法  
  
1.  攻擊執行了 Adminer 的網站  
	- 黑帽架一個 Evil MySQL Server  
		- 這裡有個 5 年多前就出現的範例程式：<https://github.com/Gifts/Rogue-MySql-Server/blob/master/rogue_mysql_server.py>  
	- 找到某個網站公開的 `adminer.php`  
	- 讓 Adminer 去連接黑帽架設的 Evil MySQL Server  
		- Adminer 預設沒 Disable `LOAD DATA LOCAL`  
		- Adminer 其中一個功能就是讓你可以連接外部的 MySQL Server  
	- 黑帽就可以開心的讀取到你伺服器上的各種資料了  
	- 原作者的另一篇文章有詳細講 Adminer 被攻擊的步驟  
		- <https://gwillem.gitlab.io/2019/01/17/adminer-4.6.2-file-disclosure-vulnerability/>  
	- Adminer 升級到 4.7.0 可以避免掉這個問題  
  
2. Honeypot  
	- 架個公開的 Evil MySQL Server  
	- 嘗試讀取上鉤的攻擊者的檔案  
		- 如果他用來連線的 mysql-client 也沒把 `LOAD DATA LOCAL` 關掉就會中招。  
  
---  
  
## 相關討論  
  
可能會有後續發展可以追  
  
- <https://mobile.twitter.com/gwillem/status/1086275952915533828>  
- [MySQL client allows MySQL server to request any local file by default : programming](https://www.reddit.com/r/programming/comments/ahspfv/mysql_client_allows_mysql_server_to_request_any/)  
  
---  
  
## References  
  
- [MySQL client allows MySQL server to request any local file](https://gwillem.gitlab.io/2019/01/20/sites-hacked-via-mysql-protocal-flaw/)  
