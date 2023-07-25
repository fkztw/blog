Title: SNTT - week7  
Date: 2013-11-05 16:58  
Author: fkz  
Category: Course  
Tags: Facebook, Social Network  
Slug: sntt-week7  
  
  
SNTT == Socail Network Technology and Trend  
  
+ [facebook developer](https://developer.facebook.com)  
Facebook App setup  
+ [Facebook PHP SDK](https://github.com/facebook/facebook-php-sdk)  
  
---  
  
## Facebook PHP SDK  
  
 + Feed  
 + Graph API  
 + Checkin  
 + [Roadmap](https://developers.facebook.com/roadmap/)  
 	+ Release the information about the large change of the facebook API  
 + Access Token  
 	+ Token Type  
		+ long term  
		+ short term  
		+ for App  
		+ for Website  
		+ for fan page  
```PHP  
//Access Token  
$access_token = $facebook->getAccessToken();  
$facebook->setAccessToken($access_token);  
```  
  
---  
  
* Same Domain Policy  
* Channel File  
