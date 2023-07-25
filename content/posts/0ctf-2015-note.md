Title: 0CTF 2015 Note  
Slug: 0ctf-2015-note  
Date: 2015-03-30 18:15:23  
Authors: fkz  
Category: Contest  
Tags: CTF, Write-up, 0CTF  
Summary: A note for 0CTF 2015  
  
  
# web / mislead  
  
Padding Oralcle Attack in Cookie  
  
+ <https://en.wikipedia.org/wiki/Padding_oracle_attack>  
+ <https://github.com/mwielgoszewski/python-paddingoracle>  
  
  
  
# web / golden mac 1  
  
Download .DS\_Store file from http://202.112.26.102/g0ldenM4c/.DS\_Store.  
It tells the flag is in http://202.112.26.102/g0ldenM4c/u\_can\_not\_guess\_this\_haha.  
Then, upload a .docx files which contains XXE to read the flag.  
  
```  
php://filter/convert.base64-encode/resource=u_can_not_guess_this_haha.php  
```  
  
+ <https://www.owasp.org/index.php/XML_External_Entity_%28XXE%29_Processing>  
+ <http://resources.infosecinstitute.com/xxe-attacks/>  
  
  
# web /forward  
  
forward the MySQL connection to your MySQL Server and look at the network traffic.  
u will see the flag leaked.  
  
```  
mysql_native_password  
forward  
SELECT flag FROM forward.flag  
def.forward.flag.flag.flag.flag....  
0ctf{w3ll_d0ne_guY}  
```  
  
---  
  
# crypto / GREBeginner  
  
+ <https://gist.github.com/5lipper/d6363e436f08f12f0bbb>  
    + [GREBeginner](/files/0ctf-2015-note/GREBeginner.cpp)  
  
  
# crypto / RSA Quine  
  
+ <https://gist.github.com/mheistermann/0dee124d7eed2ec26fcd>  
  
---  
  
# mobile / dataraidar  
  
+ <http://www.forensicswiki.org/wiki/How_To_Decrypt_Android_Full_Disk_Encryption>  
+ <http://blog.scrt.ch/2015/03/27/insomnihack-finals-insomnidroid-level-1-writeup/>  
  
  
# mobile / simpleapk  
  
+ <http://androidcracking.blogspot.tw/2010/12/getting-apk-signature-outside-of.html>  
  
```  
08:39 < KT_SaH> wytshadow: simpleapk: reversed the lib and saw some xoring, so I xored the flag.txt => win  
08:39 < riatre> wytshadow: simpleapk: reverse the elf  
08:39 < niklasb> yeah and maybe realize that they used adi  
08:39 < niklasb> *adbi  
08:40 < Zzzzzzzzzz> wytshadow: simpleapk: inject logger in smali, recompile, dump variable with flag ;]  
08:44 < niklasb> the XOR key had 0 bytes at the first 5 and the last position  
08:45 < KT_SaH> 0ctf{Too_Simple_Sometimes_Naive!!!} -> 0ctf{It's_More_Than_Meets_The_Eye!}  
```  
  
  
  
# mobile / VEZEL  
  
```  
08:39 < niklasb> wytshadow: tl;dr for vezel you could just compute the values from another app  
08:39 < KT_SaH> vezel: IDA + adb + print flag value :D  
08:39 < KT_SaH> + bluestacks  
```  
  
---  
  
# Pwn Challenges  
  
+ <https://rzhou.org/~ricky/0ctf2015/>  
    + [0ops App](/files/0ctf-2015-note/0ops_app.py)  
    + [Flag Generator](/files/0ctf-2015-note/flaggenerator.py)  
    + [freenote](/files/0ctf-2015-note/freenote.py)  
    + [login](/files/0ctf-2015-note/login.py)  
+ <https://gist.github.com/seanwupi/49c7d68ee13f29ddb435>  
    + [flagen](https://gist.github.com/seanwupi/37ffc34032c0ada9a9d8)  
    + [freenode](https://gist.github.com/seanwupi/929df6655f2acdbab3ff)  
    + [login](https://gist.github.com/seanwupi/e4b1f039e9f949a7b972)  
    + [0opsapp](https://gist.github.com/seanwupi/713023672c42aa62ca9e)  
    + [vbs](https://gist.github.com/seanwupi/286c823afe64617c652d)  
+ VBS  
    + [CVE-2014-6332](http://www.cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6332)  
  
---  
  
# Misc  
  
+ LFI - Local File Inclusion  
    + <https://en.wikipedia.org/wiki/File_inclusion_vulnerability>  
    + <https://www.owasp.org/index.php/Testing_for_Local_File_Inclusion>  
    + <http://hakipedia.com/index.php/Local_File_Inclusion>  
+ SSRF - Server Side Request Forgery  
    + <https://www.acunetix.com/blog/articles/server-side-request-forgery-vulnerability/>  
    + <http://www.slideshare.net/d0znpp/ssrf-attacks-and-sockets-smorgasbord-of-vulnerabilities>  
