Title: Upgrade MongoDB from 3.2 to 3.4 on Debian 9  
Slug: upgrade-mongodb-from-3-2-to-3-4-on-debian-9  
Date: 2018-07-24 21:51:32  
Authors: m157q  
Category: Note  
Tags: MongoDB, Debian, Debian 9  
Summary: How to install (upgrade to) MongoDB 3.4 on Debian Strech (Debian 9)  
  
  
## TL;DR  
  
```bash  
sudo apt-get remove mongodb  
  
sudo apt-get autoremove  
  
sudo apt-get autoclean  
  
sudo tee -a /etc/apt/sources.list.d/mongodb-org-3.4.list << EOF  
deb http://repo.mongodb.org/apt/debian jessie/mongodb-org/3.4 main  
EOF  
  
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com --recv 0C49F3730359A14518585931BC711F9BA15703C6  
  
sudo apt-get update  
  
sudo apt-get --assume-yes install mongodb-org=3.4.16  
  
sudo systemctl start mongod  
  
sudo systemctl enable mongod  
```  
  
---  
  
## Preface  
  
Official MongoDB package for Debian Stretch (Debian 9) only update to 3.2.  
Community MongoDB package for Debian Stretch (Debian 9) already update to 3.6.  
And we cannot just upgrade MongoDB from 3.2 to 3.6. (Will encounter error)  
So, that's why I wrote this note.  
  
---  
  
## Steps  
  
+ Must stop `mongodb` (MongoDB 3.2 still use `mongodb` not `mongod`)  
  
```bash  
sudo systemctl stop mongodb  
```  
  
  
+ Must remove current old mongodb package and related tools  
  
```bash  
sudo apt-get remove mongodb  
sudo apt-get autoremove  
sudo apt-get autoclean  
```  
  
  
If you don't do the steps above, you will encounter error while installing MongoDB 3.4.  
Some dependencies may conflict.  
  
  
+ Add MongoDB 3.4 package source for `apt-get`  
  
```bash  
sudo tee -a /etc/apt/sources.list.d/mongodb-org-3.4.list << EOF  
deb http://repo.mongodb.org/apt/debian jessie/mongodb-org/3.4 main  
EOF  
```  
  
  
+ Add public key for MongoDB 3.4 package source  
  
```bash  
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com --recv 0C49F3730359A14518585931BC711F9BA15703C6  
```  
  
  
+ Update to newest package index  
  
```bash  
sudo apt-get update  
```  
  
+ Install MongoDB 3.4.16 (You can change to any 3.4.x)  
  
```bash  
sudo apt-get --assume-yes install mongodb-org=3.4.16  
```  
  
Now, your MongoDB 3.4 should be running well.  
If it doesn't, you should use the steps below.  
  
```bash  
sudo systemctl start mongod  
sudo systemctl enable mongod  
```  
  
---  
  
## Last but not lease  
  
+ Global config file changed from `/etc/mongodb.conf` to `/etc/mongod.conf`  
+ If you want to enable backwards-incompatible features in MongoDB 3.4.  
	+ Execute this command in MongoDB shell: `db.adminCommand( { setFeatureCompatibilityVersion: "3.4" } )`  
  
---  
  
## References  
  
+ [Repository](https://docs.pritunl.com/docs/repository)  
+ [Upgrade a Standalone to 3.4 — MongoDB Manual](https://docs.mongodb.com/manual/release-notes/3.4-upgrade-standalone/)  
