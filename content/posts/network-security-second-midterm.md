Title: Network Security Second Midterm  
Date: 2014-12-08 09:56  
Author: fkz  
Category: Course  
Tags: NetSec, Security  
Slug: network-security-second-midterm  
  
  
Find the answers for the questions I am not sure about.  
  
### Q: Is it correct that a certificate contains both the public key and private key of a user? Who should sign a certificate? why?  
### A: No, only the public key. The trusted Third Party (usually CA) should sign a certificate in order to let anyone needing this user’s public key can obtain the certificate and verify that it is valid by way of the attached trusted signature.  
![1.png](/files/network-security-second-midterm/1.png)  
  
---  
  
### Q: What is 802.11i?  
### A: 802.11i is a standard for wireless local area networks (WLANs) that provides improved encryption for networks that use the popular 802.11a and 802.11b (which includes Wi-Fi standards).  
+ [IEEE 802.11i-2004 - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/IEEE_802.11i-2004)  
+ [What is 802.11i? - Definition from WhatIs.com](http://searchmobilecomputing.techtarget.com/definition/80211i)  
  
![2.png](/files/network-security-second-midterm/2.png)  
![3.png](/files/netowrk-security-second-midterm/3.png)  
  
---  
  
## IPsec  
Check links below for the detail.  
+ [RFC 4301 - Security Architecture for the Internet Protocol](https://tools.ietf.org/html/rfc4301)  
+ [IPsec - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/IPsec)  
  
---  
  
### Q: In IPsec, explain security association (SA) and who may keep it?  
### A: An SA is a simplex "connection" that affords security services to the traffic carried by it. (RFC-4301 4.1)  
### Both client & server will keep it.  
  
+ [Security association - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/Security_association)  
	+ A Security Association (SA) is the establishment of shared security attributes between two network entities to support secure communication.  
  + An SA is a simplex (one-way channel) and logical connection which endorses and provides a secure data connection between the network devices.  
  + An SA is a logical group of security parameters that enable the sharing of information to another entity.  
  
### Q: In IPsec, explain security association database (SAD) and who may keep it?  
### A: In each IPsec implementation, there is a nominal Security Association Database (SAD), in which each entry defines the parameters associated with one SA.  Each SA has an entry in the SAD. (RFC-4301 4.4.2)  
### Both client & server will keep it.  
  
![4.png](/files/network-security-second-midterm/4.png)  
  
---  
  
### Q: In IPsec, if ESP and AH support authentication? confidentiality?  
### A: AH support authentication; ESP support authentication and cofidentiality;  
![5.png](/files/network-security-second-midterm/5.png)  
  
---  
  
### Q: IPsec Modes detail  
### A: Transport mode and Tunnel Mode  
![6.png](/files/network-security-second-midterm/6.png)  
![7.png](/files/network-security-second-midterm/7.png)  
![8.png](/files/network-security-second-midterm/8.png)  
  
---  
  
### Q: IPsec Header  
### ESP Encryption and Authentication  
![9.png](/files/network-security-second-midterm/9.png)  
### ESP Transport mode & Tunnel mode  
![10.png](/files/network-security-second-midterm/10.png)  
