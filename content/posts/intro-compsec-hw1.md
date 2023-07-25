Title: Intro CompSec Hw1  
Date: 2014-12-18 16:51  
Author: fkz  
Category: Course  
Tags: Security  
Slug: intro-compsec-hw1  
  
  
### Introduction to Computer Security HW1  
  
1. Select a web site.  
    + Use “Wget” or “Teleport Pro” to mirror the site. Look for comments within comment tags. Give screen dumps and explain what you found.  
        + Screen Dumps & Explanations  
            + I've found some hidden targets that not be shown on the home page of <http://www.nctu.edu.tw>. These website probably still working but out of date or have already be deprecated that nobody maintain the website and may have some flaws. Below is the lists.  
            + <http://140.113.71.51>  
                + ![Screenshot 1](/files/intro-compsec-hw1/screenshot1.png)  
            + <http://president.nctu.edu.tw>  
                + ![Screenshot 2](/files/intro-compsec-hw1/screenshot2.png)  
            + <http://www.pac.nctu.edu.tw>  
                + ![Screenshot 3](/files/intro-compsec-hw1/screenshot3.png)  
            + <http://www.pac.nctu.edu.tw>  
                + ![Screenshot 4](/files/intro-compsec-hw1/screenshot4.png)  
            + <http://www.ccs.nctu.edu.tw>  
                + ![Screenshot 5](/files/intro-compsec-hw1/screenshot5.png)  
            + <http://www.itt.nctu.edu.tw>  
                + ![Screenshot 6](/files/intro-compsec-hw1/screenshot6.png)  
            + <http://www.ga.nctu.edu.tw>  
                + ![Screenshot 7](/files/intro-compsec-hw1/screenshot7.png)  
            + <http://campus.creativity.edu.tw>  
                + ![Screenshot 8](/files/intro-compsec-hw1/screenshot8.png)  
            + <http://apc.iim.nctu.edu.tw>  
                + ![Screenshot 9](/files/intro-compsec-hw1/screenshot9.png)  
            + <http://saofficion.adm.nctu.edu.tw>  
                + ![Screenshot 10](/files/intro-compsec-hw1/screenshot10.png)  
    + Use “DirBuster” with a proxy feature through “privoxy” to enumerate hidden files and directories. Screen dump and explain the hidden files and directories you found.  
        + Screen Dumps & Explanations  
            + ![Screenshot 11](/files/intro-compsec-hw1/screenshot11.png)  
            + ![Screenshot 12](/files/intro-compsec-hw1/screenshot12.png)  
                + Maybe there some something useful in these index.php files.  
2. Lookup “How I met your girlfriend” in the BlackHat 2010 demo to explain, in 0.5 page, how this was done.  
    + Explanations  
> The speaker first study on the session mechanism of the Facebook.  
> He reduced the complexity of breaking session steps by steps.  
> The Entropy had be redurced from the initial 160 bits to only 20 bits!! He kept tracing the source code and hacking it.  
> Then, he used a techical skill called "NAT pinning" to confuse the router at protocol level.  
> After that, he also used the IRC bot, Geoloction via XSS and HTML5 anti-WAF XSS.  
> Combined all these skills and analysized based on those results.  
> Finally, he used the triangle localization to find someone's girlfriend in reality.  
3. Select a person. Use on-line sites for phone book, social network, information, job, photo management, business directory, jigsaw.com, etc. to summarize, with screen dumps and explanations, what information you can get. If your target is not in US nor native English speaker, you might need to use on-line sites different from the textbook.  
    + Screen Dumps & Explanations  
        + Name: Johnny Depp (John Christopher Depp II)  
        + wikipedia: <http://en.wikipedia.org/wiki/Johnny_Depp>  
        + <http://www.peoplesearch.com>  
            + ![Screenshot 13](/files/intro-compsec-hw1/screenshot13.png)  
            + view more need to pay some money  
        + <https://www.facebook.com/JohnnyDepOfficial>  
            + ![Screenshot 14](/files/intro-compsec-hw1/screenshot14.png)  
        + <http://www.reunion.com/johnnydepp/>  
            + ![Screenshot 15](/files/intro-compsec-hw1/screenshot15.png)  
        + <http://www.mylife.com/mick563>  
            + ![Screenshot 16](/files/intro-compsec-hw1/screenshot16.png)  
        + <https://twitter.com/J0HNNYDepp>  
            + ![Screenshot 17](/files/intro-compsec-hw1/screenshot17.png)  
4. Google “XYZ resume firewall” and “XYZ resume intrusion detection” where “XYZ” is the name of your target company.  Screen dump “useful” results and explain what you got.  
    + Screen Dumps & Explanations  
        + ![Screenshot 18](/files/intro-compsec-hw1/screenshot18.png)  
        + ![Screenshot 19](/files/intro-compsec-hw1/screenshot19.png)  
            + A company called "Systems Technology International" is looking for who will use Linux iptables firewall.  
        + ![Screenshot 20](/files/intro-compsec-hw1/screenshot20.png)  
            + A company called "ICF International" is looking for who have experience with using Snort IDS.  
5. Lookup Archive.org and Google cached results, and select a target web site. Compare the differences between an archived and cached copy with its current on-line web site. Give screen dump and explain the differences.  
    + Screen Dumps & Explanations  
        + Archive.org  
            + ![Screenshot 21](/files/intro-compsec-hw1/screenshot21.png)  
            + 2014/02/09  
        + Google cached  
            + ![Screenshot 22](/files/intro-compsec-hw1/screenshot22.png)  
            + 2014/04/07 01:16:27 GMT  
        + current  
            + ![Screenshot 23](/files/intro-compsec-hw1/screenshot23.png)  
            + 2014/04/07 09:00:03 GMT  
        + Archive.org have older information. Google cached seems no different from the current website because the cached information just few hours ago.  
6. Find Google Hacking Database at hackersforcharity.org/ghdb/. Summarize what it has and select 3 strings to search. Screen dump and explain what you got.  
    + What GHDB has  
        + it store the google search sentences which can be used to search some specific websites vulnerabilities. There are many entries and each entry have many google search sentences for searching vulnerabilities. The information on the GHDB maybe too old. The newest record is almost eight years ago (2006), though it seems still working...  
    + Screen Dumps & Explanation  
        + Juicy information of the websites built by AppServ  
            + ![Screenshot 24](/files/intro-compsec-hw1/screenshot24.png)  
            + ![Screenshot 25](/files/intro-compsec-hw1/screenshot25.png)  
        + .xls files within user id and password  
            + ![Screenshot 26](/files/intro-compsec-hw1/screenshot26.png)  
            + ![Screenshot 27](/files/intro-compsec-hw1/screenshot27.png)  
        + backup directories of the server  
            + ![Screenshot 28](/files/intro-compsec-hw1/screenshot28.png)  
            + ![Screenshot 29](/files/intro-compsec-hw1/screenshot29.png)  
7. Select a web site. Start from whois.iana.org to find its registry, registrar, and registrant. Also select an IP address. Start from arin.net to find who owns the IP address. Show your screen dump and explain.  
    + Screen Dumps & Explanations  
        + whois.iana.org - www.nctu.edu.tw  
            + ![Screenshot 30](/files/intro-compsec-hw1/screenshot30.png)  
            + ![Screenshot 31](/files/intro-compsec-hw1/screenshot31.png)  
            + Registry: Taiwan Network Information Center (TWNIC)  
            + Registrar: rs.twnic.net.tw  
            + Registrant: Vice CEO  
        + arin.net - 8.8.8.8  
            + ![Screenshot 32](/files/intro-compsec-hw1/screenshot32.png)  
            + 8.8.8.8 is Google DNS Server  
8. Select a domain name. Use nslookup to dump its DNS records. Show your screen dump and explain.  
    + Screen Dumps & Explanations  
        + ![Screenshot 33](/files/intro-compsec-hw1/screenshot33.png)  
        + The <http://www.nctu.edu.tw> has three IP for load balancing.  
9. Select a domain name. Use traceroute or similar tools to find the access path to that domain. Show your screen dump and explain.  
    + Screen Dumps & Explanations  
        + ![Screenshot 34](/files/intro-compsec-hw1/screenshot34.png)  
        + The destination server seems close the ICMP, so traceroute didn't get the 5th hop ICMP "time exceeded" signal.  
10. Follow the case study right before chapter 1. Select one target and run through all tools (Tor, Vidalia, Privoxy, tor-resolve, proxychains, Nmap, socat, nc). Screen dump the process and explain what you got in your screen.  
    + Screen Dumps & Explanations  
        + turn on vidalia  
            + ![Screenshot 35](/files/intro-compsec-hw1/screenshot35.png)  
        + using tor  
            + ![Screenshot 36](/files/intro-compsec-hw1/screenshot36.png)  
        + finding target  
            + ![Screenshot 37](/files/intro-compsec-hw1/screenshot37.png)  
        + found target  
            + ![Screenshot 38](/files/intro-compsec-hw1/screenshot38.png)  
        + used tor-resolve to get target ip  
            + ![Screenshot 39](/files/intro-compsec-hw1/screenshot39.png)  
        + using proxychains and nmap  
            + ![Screenshot 40](/files/intro-compsec-hw1/screenshot40.png)  
            + ![Screenshot 41](/files/intro-compsec-hw1/screenshot41.png)  
        + using socat  
            + ![Screenshot 42](/files/intro-compsec-hw1/screenshot42.png)  
        + get target informations  
            + ![Screenshot 43](/files/intro-compsec-hw1/screenshot43.png)  
