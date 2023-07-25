Title: 如何及為什麼要使用 `git clone --shallow-submodules`  
Slug: what-does-git-clone-shallow-submodules-do-and-how-to-use-it  
Date: 2017-11-03 16:24:16  
Authors: fkz  
Category: Note  
Tags: Git  
Summary: 偶然因為同事的問題知道了 `git-clone` 有 `--shallow-submodules` 這個選項，紀錄一下。  
  
  
## TL;DR  
  
`git clone --shallow-submodules` must be used with `--recurse-submodules`.  
That is,  
  
`git clone --recurse-submodules --shallow-submodules <repository>`  
  
(git version 2.15.0)  
  
---  
  
## How to use `--shallow-submodules` for `git clone`?  
  
`man git-clone` 其實沒有寫得很清楚  
  
[Git - git-clone Documentation](https://git-scm.com/docs/git-clone#git-clone---no-shallow-submodules):  
> --[no-]shallow-submodules  
>            All submodules which are cloned will be shallow with a depth of 1.  
  
  
看完以後以為只要 `git clone --shallow-submodules`，  
就會自動幫你 `git submodule update --init --depth 1`，  
但並沒有。  
  
經過 [WanCW 的實際測試](https://twitter.com/WanCW/status/924993679156056064)後才知道，  
 `--shallow-submodules` 一定要搭配 `--recurse-submodules` 才有作用。  
  
如果只使用 `git clone --shallow-submodules`，  
會發現 submodule 的資料夾都還是空的，  
一樣得 `git submodulte update --init --depth 1` 才有用。  
  
---  
  
## Why use `--shallow-submodules` for `git clone`?  
  
減少整個 git clone 的傳輸量以及佔用硬碟的空間，  
submodules 都只會有最新一筆的 commit 及其 data 而已。  
（進入 submodule 後會看到 git log 只會有一筆資料）  
  
---  
  
## When to use `--shallow-submodules` for `git clone`?  
  
個人目前想到的適用情境：  
  
1. local 開發時不需要一併開發 submodule 的情況下  
    + 既然 submodule 只有需要被使用，不需要開發的話，只要抓最新的部份拿來用就好，可以減少 clone 的時間。  
    + submodule 愈肥大的話，clone 的時間應該省愈多。  
2. Deploy 的時候  
	+ 因為不需要修改 code 了，讓 CI clone source code 的時候可以減少傳輸量，加速 deploy 時的速度。  
  
其他有想到再補上。  
