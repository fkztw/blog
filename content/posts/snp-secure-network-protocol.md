Title: SNP (Secure Network Protocol)  
Date: 2014-11-03 07:08  
Author: fkz  
Category: Note  
Tags: SNP, NCTU, DSNS  
Slug: snp-secure-network-protocol  
Modified: 2015-10-20 14:07  
  
  
交大 DSNS Lab 開發  
有申請專利  
看起來就是個有加密的 telnet (?)  
聽說後來沒人維護，就被 SSH 幹掉了  
又知道了奇怪的歷史  
以前的人都好強啊  
  
[SNP telnet for Windows 給你安全的 telnet 環境 - PChome 下載](http://toget.pchome.com.tw/category/network/11685.html)  
這邊還有相關軟體可以下載得到(?)  
  
Quote from [《網路與通訊》 淺談網路安全與防護](http://www.ascc.sinica.edu.tw/nl/88/1517/02.txt)  
> 3.SNP：  
> 由交通大學資訊工程學系分散系統與網路安全實驗室所研發出來的一套新式網路安全系統  
> （Security  Network Protocols， 簡稱SNP）。  
> 此套系統包含了多項安全的應用程式，  
> 如安全電子郵件（Certified  Secure E-mail System，簡稱CS-Mail）、  
> 身分認證中心（Certificate Authority）及  
> 網路監聽系統（Network Monitor Systems）等  
> 交大係冀望藉由此一系統的功能，達到整合式的安全通訊網路環境。  
  
Quote from <https://ir.nctu.edu.tw/bitstream/11536/6497/1/000272742700008.pdf>  
> Among these protocols, Secure Network Protocol (SNP)(Shieh et al., 1999)  
> is one of the few protocols that has real deployment for years.  
> SNP is a symmetric-key based protocol providing an efficient way for both intra- and inter- domain authentication.  
> Compared  to  Kerberos, fewer messages are required in SNP to authenticate client identity.  
> For intra-domain authentication,  
> SNP takes four messages to authenticate client identity and one more optional message for mutually authenticating the server.  
> For inter-domain authentication, it takes seven messages for initial authentication,  
> regardless of the number of hops between the visited and home domains.  
> Only two messages are required for subsequent authentication when requesting the same service.  
> To simplify the design, SNP replaces timestamps with nonces, reducing the need for time servers.  
> For faster authentication, a master key is shared by the authentication server (AS) and the service servers (S).  
> The unchanged master keys can make the system vulnerable to various attacks.  
  
Quote from [Prof. Shiuhpyng Shieh](https://comm.ntu.edu.tw/2010UKworkshop/NSP9.htm)  
> He was the designer of SNP (Secure Network Protocol), which was a very popular security software package.  
  
這篇疑似是 Secure Network Protocol 的論文  
<http://dsns.cs.nctu.edu.tw/ssp/paper/50.An%20Authentication%20and%20Key%20Distribution%20System%20for%20Open%20Network%20Systems.pdf>  
  
## References  
+ <http://dsns.cs.nctu.edu.tw/ssp/paper/50.An%20Authentication%20and%20Key%20Distribution%20System%20for%20Open%20Network%20Systems.pdf>  
+ <https://ir.nctu.edu.tw/bitstream/11536/6497/1/000272742700008.pdf>  
+ [Prof. Shiuhpyng Shieh](https://comm.ntu.edu.tw/2010UKworkshop/NSP9.htm)  
+ [netsec-intro-2nd](http://www.slidefinder.net/c/conventional_encryption/32524394)  
+ [BSD簡介 - SNP & ptelnet](http://content.edu.tw/senior/computer/ks_ks/pro/new8.htm)  
+ [SNP telnet for Windows 給你安全的 telnet 環境 - PChome 下載](http://toget.pchome.com.tw/category/network/11685.html)  
+ (dead) [FreeBSD SNP 1.裝設SNP](http://fanqiang.chinaunix.net/a1/b2/20020308/060200125_b.html)  
	+ (backup) [[備份] 安裝 SNP 通訊全程加密](https://www.evernote.com/shard/s351/sh/18196c4c-a29c-4b39-a114-78991a799f26/908d2e28eaaced87bc50f9bd05b6dfd3)  
+ (dead) [《網路與通訊》 淺談網路安全與防護](http://www.ascc.sinica.edu.tw/nl/88/1517/02.txt)  
    + (backup) [[備份] 《網路與通訊》淺談網路安全與防護](https://www.evernote.com/shard/s351/sh/889e26f1-362e-4785-b24a-1c5a71b9e2a3/a0a3c0e63b30a4c442d232fb34b37fca)  
