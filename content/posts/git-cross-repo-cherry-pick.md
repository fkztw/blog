Title: 使用 Git 時如何做出跨 repo 的 cherry-pick  
Slug: git-cross-repo-cherry-pick  
Date: 2017-12-30 23:59:05  
Authors: fkz  
Category: Note  
Tags: git, 2018 iT 邦幫忙鐵人賽  
Summary: 這篇文章簡單紀錄 3 個可以讓你把某個 git repo 的 commits 直接搬到另外一個 repo 的方法。  
Modified: 2017-12-31 01:52:05  
  
  
## 前言  
  
會有這個需求是因為在前公司的時候，有個舊的 repo 執行的服務被因為裡頭的程式碼有太多舊的東西，但仍然有目前要用的部份，所以複製到了一個新的 repo。同時舊的這邊的改動又有需要更新到新的 repo，所以必須做到跨 repo 的 cherry-pick。查了一下，StackOverflow 上也有不少人問，打聽了一下身邊工程師的朋友們，也有人有過同樣的需求。這篇把我知道的 3 個方法整理起來，並列出哪個比較好及為什麼比較好的原因。  
  
---  
  
## TL;DR  
  
`git format-patch -k --stdout ${commit_hash_1}..${commmit_hash_2} | git am -3 -k`  
  
---  
  
### "git remote add + git fetch + git cherry-pick"  
  
這個應該是最好懂的，只要有在 GitHub 上 fork 過別人的 repo，並按照 GitHub 的官方教學把對方的 repo 用 `git remote add` 設定成 upstream 的人，對這套流程應該不陌生，大概就是以下的步驟：  
  
1. `git remote add` 有你想要 `cherry-pick` 的 commit 的 repo  
2. `git fetch` 剛剛設定好的 remote  
3. fetch 下來後就可以 `git checkout` 到你要的 branch，然後用 `git log` 找尋你要的 commit，紀錄下來後就可以進行 `cherry-pick`  
  
如果這樣還是不太懂的話，底下有人回覆了這篇文章：[Git cherry-pick from another repository (Example)](https://coderwall.com/p/sgpksw/git-cherry-pick-from-another-repository)，把完整的步驟與指令都清楚的列出來了。  
  
這個方式很好懂，但很麻煩，因為步驟真的有點多。  
  
---  
  
### "git diff + git apply"  
  
比較進階一點的 Git user 會用這個方法，觀念上沒有很難懂，只是要瞭解 `git diff` 和 `git apply` 這兩個指令在幹嘛。其實從字面上看來大概就可以猜測到，`git diff` 生出一個 diff 檔，而 `git apply` 把這個 diff 檔 apply 到某個 branch 上。  
  
`git diff` 應該對大部分的 git user 來說不陌生，主要都是在修改檔案後要 `git add` 之前，用 `git diff ${FILE_PATH}` 來確認某個檔案修改的部份。但 `git diff` 也可以用來看從 A commit 到 B commit 之間修改了哪些東西，用法也不難，`git diff ${A_COMMIT_HASH} ${B_COMMIT_HASH}` 就行了。  
  
`git apply` 可能是一般 Git user 比較少用到的，但也沒有很難懂。`man git-apply` 顯示的簡介是 **git-apply - Apply a patch to files and/or to the index**，簡單來說就把一個 patch 檔 apply 到你現在的 branch。  
  
知道了這兩個指令在幹嘛以後，我們就可以透過以下步驟來達到我們想要的效果：  
  
1. `git diff ${A_COMMIT_HASH} ${B_COMMIT_HASH} > xxx.patch`  
	+ 在我們要抓 commmits 的 repo 下這行指令得到 patch 檔，以我的例子來說就是舊 repo。  
2. `git apply xxx.patch`  
	+ 在我們要加入這些 commits 的 repo 使用這行指令把 commits 新增進來，以我的例子來說就是新 repo。  
		+ 要記住 xxx.patch 的路徑要是對的，因為上個指令產生的 xxx.patch 應該是不會在新 repo 的目錄底下才對 XD  
  
	+ 如果在 `git apply` 的過程中遇到 trailing whitespace error 的話，可以參考這篇文章：[git - My diff contains trailing whitespace - how to get rid of it? - Stack Overflow](https://stackoverflow.com/questions/14509950/my-diff-contains-trailing-whitespace-how-to-get-rid-of-it)，透過加入 `--whitespace=warn` 或 `--whitespace=nowarn` 參數來解決。  
  
這樣是不是比上面那個步驟少多了？但這個方法有個缺點，就是使用 `git apply` 的話，committer 會是使用 `git apply` 的人，而不是原本的 committer，所以要介紹下面這個方法。  
  
---  
  
### "git format-patch + git am"  
  
這個是 3 個方法裏面最推薦的，最後會講一下 GitHub 有一個小方法可以直接拿到 patch，可以直接給 `git am` 使用。  
  
基本上這方法應該是最正統的如何把別人的 commit 拿來給自己用的方式了，GitHub 也只是把這個包裝起來而已。如果是已經習慣透過 email 或者論壇收發 patch 的 Open Source contributer 兼 git 使用者，應該對這個方法習以為常。  
  
一般的 GitHub user 應該都對這兩個指令不熟，因為 GitHub 已經把這塊都處理好了，所以使用者基本上不太需要自己操作。`man git-format-patch` 和 `man git-am` 就可以看到，這兩個指令基本上都是設計成在 email 的環境下使用：  
  
+ `man git-format-patch`: **git-format-patch - Prepare patches for e-mail submission**  
+ `man git-am`: **git-am - Apply a series of patches from a mailbox**  
  
有興趣的人可以自己去看個詳細，這邊就不多談，直接講使用方法：  
  
1. `git format-patch -k --stdout ${A_COMMIT_HASH}..${B_COMMIT_HASH} > xxx.patch`  
	+ 在我們要抓 commmits 的 repo 下這行指令，以我的例子來說就是舊 repo。  
	+ A commit 要比 B commit 早，不然 output 會是空的。  
	+ > `-k`, `--keep-subject`: Do not strip/add [PATCH] from the first line of the commit log message.  
		+ 加入 `-k` 這個參數的話， commit log 的第一行就不會加上 `[PATCH]`。  
2. `git am -k -3 < xxx.patch`  
	+ 在我們要加入這些 commits 的 repo 使用這行指令，以我的例子來說就是新 repo。  
		+ 要記住 xxx.patch 的路徑要是對的，因為上個指令產生的 xxx.patch 應該是不會在新 repo 的家目錄底下才對 XD  
	+ `-k` 是為了接收加了 `-k` 參數沒有加了 `[PATCH]` 字串的 patch 檔  
	+ `-3` 是使用 three-way merge  
  
其實跟 `git diff` + `git apply` 非常像。  
  
[在 StackOverflow 上的這個回答](https://stackoverflow.com/a/9507417) 直接教你怎麼把這兩個指令合在 1 行解決。  
  
  
#### GitHub 支援 `git format-patch` 的小功能  
  
GitHub 其實可以在 commit, pull request, compare 的網址後面加上 `.patch`，就會拿到 `git format-patch` 產生的檔案，不過這邊的 output 是沒有加 `-k` 參數的，所以會有 "[PATCH]" 字串，以下是範例：  
  
+ commit: <https://github.com/zdict/zdict/commit/b871cd6c8a6a71f595fe93132cc9d5c9a71eb82d.patch>  
+ pull request: <https://patch-diff.githubusercontent.com/raw/zdict/zdict/pull/149.patch>  
+ compare: <https://github.com/zdict/zdict/compare/issue-23.patch>  
  
---  
  
## 參考資料  
  
+ [Is it possible to cherry-pick a commit from another git repository? - Stack Overflow](https://stackoverflow.com/questions/5120038/is-it-possible-to-cherry-pick-a-commit-from-another-git-repository/9507417#9507417)  
    + 這邊有列出一些可以做到的方法  
+ [How do you take a git diff file, and apply it to a local branch that is a copy of the same repository? - Stack Overflow](https://stackoverflow.com/questions/12320863/how-do-you-take-a-git-diff-file-and-apply-it-to-a-local-branch-that-is-a-copy-o/12320940#12320940)  
    + 這篇解釋了為什麼 "`git format-patch` + `git am`" 比 "`git diff` + `git apply`" 好  
    + > A better way to exchange whole commits by file is the combination of the commands git format-patch on the sender and then git am on the receiver, because it also transfers the authorship info and the commit message.  
+ [Git cherry-pick from another repository (Example)](https://coderwall.com/p/sgpksw/git-cherry-pick-from-another-repository)  
+ [git - My diff contains trailing whitespace - how to get rid of it? - Stack Overflow](https://stackoverflow.com/questions/14509950/my-diff-contains-trailing-whitespace-how-to-get-rid-of-it)  
