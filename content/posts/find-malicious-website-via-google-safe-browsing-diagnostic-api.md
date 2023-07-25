Title: Find Malicious Website via Google Safe Browsing Diagnostic API  
Date: 2015-01-14 14:23  
Author: fkz  
Category: Note  
Tags: Malicious Website, Safe Browsing, Security  
Slug: find-malicious-website-via-google-safe-browsing-diagnostic-api  
Modified: 2015-10-27 12:00  
  
  
One of my friends need to analyze the websites which are sentenced to be malicious website by the Google (Chrome safe browsing) for one of his security related course homeworks.  
He told me that it's very hard to find such links, so I found this kind of solution for him.  
  
![The site ahead contains malware](/files/find-malicious-website-via-google-safe-browsing-diagnostic-api/the_site_ahead_contains_malware.png)  
  
  
### Use the Google Safe Browsing Diagnostic API  
  
<https://www.google.com/safebrowsing/diagnostic?site=Google.com>  
  
+ Change the value of the `site` to some portal site such as Google, Yahoo, ...  
+ Check the result if it has `Malicious software is hosted on 276 domain(s), including ...` like the following pic  
+ Try those urls to see if Google Safe Browsing diagnose it as malicious urls  
  
![Safe Browsing](/files/find-malicious-website-via-google-safe-browsing-diagnostic-api/safe_browsing.png)  
  
### The result of <http://24corp-shop.com/>  
  
![24corp shop](/files/find-malicious-website-via-google-safe-browsing-diagnostic-api/24corp_shop.png)  
  
### NOTICE  
  
Sometimes you won't see the "Security Error" message because the result shows the record in last 90 days.  
When you access the website, the malicious software maybe already be removed from that site.  
