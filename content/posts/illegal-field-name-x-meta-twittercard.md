Title: Illegal field name 'X-Meta-Twitter:card'  
Date: 2013-05-08 07:44  
Author: fkz  
Category: Note  
Tags: Perl, CPAN, WWW::Mechanize, X-Meta-Twitter:card  
Slug: illegal-field-name-x-meta-twittercard  
Modified: 2015-10-28 15:07  
  
  
最近因為 NA 作業2 開始寫 Perl  
其中一個是寫 IRC bot  
作業 Demo 完後自己繼續開發新功能  
要做檢查到 URL 就回應該 URL Html source 的 title label 和 縮網址  
用了 CPAN 的 `WWW::Mechanize`  
結果 xatier 丟了 [gist:5538258 · GitHub](https://gist.github.com/xatier/5538258) 出來後  
IRC bot 就 die 了  
噴出了這行錯誤  
  
`Illegal field name 'X-Meta-Twitter:card' at .../HTML/HeadParser.pm line 207.`  
  
---  
  
Google 了一下 Error Message 發現不少人都有遇到  
  
根據這篇底下的 comment 找到了答案 (其實自己先 Trace code 之後也找到了同樣的地方  
  
[lwp-download fails with HTTP::Message 6.06 · Issue #3 · libwww-perl/http-message · GitHub](https://github.com/libwww-perl/http-message/issues/3#issuecomment-10118644)  
  
問題就出在 `perl5/lib/per5/HTTP/Headers.pm`  
  
`HTML::HeadParser` 有用到 `HTTP::Headers`  
  
裏面有個叫 `_header` 的 subroutine (不過在上面那篇的 comment 裏面好像是 header  
  
裏面有一行  
  
```perl  
Carp::croak("Illegal field name '$field'") if rindex($field, ':') > 1 || !length($field);  
```  
  
問題就出在  
  
```perl  
rindex($field, ':') > 1  
```  
  
只要 `:` 後面有東西的話就會回傳 `True`  
  
`Twiiter:card` 的 `:` 後面有 `card` 所以被判定成 `Illegal field name` 了  
  
要修正的話就照那個 comment 說的  
  
把該行改成  
  
```perl  
Carp::croak("Illegal field name '$field'") if $field !~ /^X-Meta/ && rindex($field, ':') > 1 || !length($field);  
```  
  
這樣就不會判斷 `X-Meta` 開頭的了  
  
只是這問題己經 6~7 個月了 開發者最近 commit 的時間也還是 2 個月前  
  
不懂為啥這問題遲遲不解決@@  
