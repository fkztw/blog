Title: GHC 7.8.2 造成 Arch Linux 無法升級的解法  
Date: 2014-05-21 14:50  
Author: fkz  
Category: Note  
Tags: Linux, Haskell, Arch Linux, GHC, sysadmin  
Slug: the-solution-for-system-upgrade-failure-caused-by-ghc-7-8-2  
Modified: 2015-10-27 13:10  
  
  
官方公告 [Managing Haskell packages with GHC 7.8.2](https://www.archlinux.org/news/managing-haskell-packages-with-ghc-782/)  
  
裡面寫了  
  
> Moving every package that is not ghc or cabal-install to [community]. This will allow better support of the core common haskell libraries since I do not actually use these packages due to cabal-install.  
  
其實我根本看不懂該怎麼做= ="  
反正我一定不是唯一一個看不懂的(?)  
所以就查到了這篇 [\[SOLVED\] Problems upgrading some haskell packages](https://bbs.archlinux.org/viewtopic.php?pid=1412908)  
遇到的情形似乎跟我一樣  
下了 `sudo pacman -Syu` 後噴了  
  
```txt  
:: haskell-transformers: requires ghc=7.6.3-1  
```  
  
然後  `pacman -Qs ghc` 後也一樣已經安裝了  
然後底下有人提供了解法  
  
```sh  
sudo pacman -Rcs haskell-transformers  
```  
  
把跟 `haskell-transformers` 有關的套件都移除掉以後  
再重新下一次 `sudo pacman -Syu` 就可以了  
  
底下的回覆有人的解釋是  
  
> haskell-transformers was recently removed from extra.  
> It depends on a specific version of ghc.  
> There is a newer version of ghc in the repos.  
> Since haskell-transformers was removed there's no upgrade path to resolve the issue.  
> You'll have to do it manually.  
> Edit: Removed from the repos entirely.  
> Not moved from extra to community like the other haskell packages.  
  
恩 應該就是這樣吧  
