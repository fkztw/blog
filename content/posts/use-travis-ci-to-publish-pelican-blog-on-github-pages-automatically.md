Title: 用 Travis CI 自動化發佈 Pelican blog 到 GitHub Pages 上  
Slug: use-travis-ci-to-publish-pelican-blog-on-github-pages-automatically  
Date: 2016-05-08 13:00:07  
Authors: fkz  
Category: Note  
Tags: Python, Pelican, Travis CI, GitHub Pages, Blog  
Summary: 因為總文章數已經累積到約 150 篇，所以每次 build Pelican 的時候都差不多要十秒，覺得每次都要等這十秒實在是很浪費時間，所以幾個月前想到可以用 Travis CI 來自動幫我完成這件事，但直到前幾天才花一個晚上的時間成功設定完，紀錄一下。  
  
  
# 前言  
  
主要的設定都是參考這篇：[Publish your Pelican blog on Github pages via Travis-CI](http://blog.mathieu-leplatre.info/publish-your-pelican-blog-on-github-pages-via-travis-ci.html)  
不過因為這篇寫於 2014 年的 1 月，  
有些內容已經有點過時了，跟我實際操作起來上有些差異，  
我有在底下留言給作者了，我自己這邊也順便紀錄一下作法。  
  
先把最終的設定檔放上來好了  
  
+ [.travis.yml](https://github.com/M157q/fkz.github.io/blob/source/.travis.yml)  
+ [requirements.txt](https://github.com/M157q/fkz.github.io/blob/source/requirements.txt)  
+ [Makefile](https://github.com/M157q/fkz.github.io/blob/source/Makefile)  
  
---  
  
# 作法  
  
先到 `https://travis-ci.org/profile/${your_github_username}` switch on 該 repo  
  
## 設定 `.travis.yml`  
  
```yaml  
language: python  
python:  
- '2.7'  # Pelican 已支援 Python 3，只是我用到一些 Plugins 仍然只能用 Python 2  
  
branches:  
  only:  
  - source  # 我是把 Pelican 的原始文字檔放在 source 這個 branch  
            # 如果是一般的 project 應該就是用 master branch  
install:  
- pip install -r requirements.txt  # 這邊其實可以直接寫死 pip install ${package}  
                                   # 使用 requirements.txt 純粹是我個人喜好  
script:  
- make travis  # 需要在 Makefile 新增 travis 的 label  
```  
  
扣掉空行也不過就 10 行  
  
  
## 設定 `requirements.txt`  
  
```txt  
pelican==3.6.3  
markdown==2.6.6       # 因為我用 Markdown 而不是 reStructuredText 寫 blog  
ghp-import==0.4.1     # 讓你 git add 某個資料夾的內容並將其 commit 到另外一個 branch  
beautifulsoup4==4.4.1 # 我用到的 plugin 需要  
```  
  
  
## 設定 `Makefile`  
  
```Makefile  
OUTPUTDIR=$(BASEDIR)/output  
GITHUB_REPO_SLUG=M157q/fkz.github.io  
GITHUB_REMOTE_NAME=origin  
GITHUB_PAGES_BRANCH=master  
# 以上參數請根據需求自行替換  
GITHUB_COMMIT_MSG=$(shell git --no-pager log --format=%s -n 1)  
  
travis: publish  
    # 為 Travis CI 設定 git 的 user.name 和 user.email  
    # 沒設定 email 的話，GitHub 上面看到的 Author 會是 Unknown  
    git config --global user.name "M157q - Travis"  
    git config --global user.email M157q.tw@gmail.com  
  
    # 將 Pelican output dir 的內容 commit 到 GitHub Pages 用的 branch，準備 push 上去  
    # 因為我用的是 user site，所以 branch 是 master。如果是 project site 的話，branch 會是 gh-pages  
    ghp-import -n -r $(GITHUB_REMOTE_NAME) -b $(GITHUB_PAGES_BRANCH) -m "$(GITHUB_COMMIT_MSG)" $(OUTPUTDIR)  
  
    # 將剛剛的 commit force push 到 GitHub 上相同的 branch  
    # 不用 -f (force push) 的話一定會因為 conflict 而失敗  
    # 因為每次 Travis CI build 只會有一個 commit  
    # 而且該 branch 只會存一堆靜態檔案，每次變動都很大，沒有啥需要保存 commit log 的必要性。  
    @git push -fq https://${GH_TOKEN}@github.com/$(GITHUB_REPO_SLUG).git $(GITHUB_PAGES_BRANCH):$(GITHUB_PAGES_BRANCH) > /dev/null  
    # 用 @ 可以讓 Travis CI 不要顯示這行在 log 上，這樣別人就不會看到你的 GitHub Personal Access Token 了，也就是這裡用的 ${GH_TOKEN}  
```  
  
  
## 設定 `GH_TOKEN`  
  
先到 <https://github.com/settings/tokens> 點選右上方的 `Generate new token`  
GitHub 可能會要求輸入密碼，確定現在是本人使用，然後進入 sudo mode。  
填寫 Token description 描述一下這是 Travis CI 要拿來 build Pelican blog 用的，  
主要是給自己看的，怕之後忘記。  
然後 select scopes 就點選 repo 就夠了  
直接移到底下點選 Generate token  
之後就會有一組 GitHub Personal Access Token 可以複製了  
然後我們要將這個 Token 的權限綁到 Travis CI 上，  
讓 Travis CI 有權限將 commit push 到 repo  
這邊有兩種作法，  
一種是直接在 Travis CI 的 Web 介面上設定環境變數（比較簡單），  
另一種是寫在 `.travis.yml` 裡頭，但有先透過 travis 將 token 進行加密，  
所以不會在 `.travis.yml` 就洩漏 GitHub Personal Access Token（但要輸入一些指令，比較麻煩一點）  
兩種擇一即可，我原本是用 CLI 設定，後來改用 Web Interface 設定。  
  
### 透過 Travis CI Web Interface 設定  
  
+ 到 `https://travis-ci.org/${user_name}/${repo_name}`  
+ 移到右手邊的 more options 並點選 settings  
+ 底下有個 Environment Variables，有 Name 和 Value 兩個欄位  
    + 在 Name 欄位填上 `GH_TOKEN`  
    + 在 Value 欄位貼上剛剛複製的 Token  
+ 然後點選 Add 即可  
  
### 透過 Travis CI CLI 設定  
  
+ 首先必須確認有安裝 `travis` 的 CLI tool  
+ 之後在 terminal 輸入 `travis encrypt GH_TOKEN=${your_token} --add`  
+ 就會看到 `.travis.yml` 裡頭多了一個 block 顯示類似下面的內容  
  
```  
env:  
  global:  
    secure: xxxxxxxxxx  
```  
  
+ 這樣就行了，之後每次 Travis CI 在跑的時候都會把這串值拿去 decode 並解密成原本的 token。  
  
  
## 讓 Travis CI 不要在有 PR 的時候重新產生 blog  
  
到 `https://travis-ci.org/${user_name}/${repo_name}/settings`，  
把 `Build pull requests` 那個 switch 切換成 off  
  
  
## 測試有沒有成功  
  
都設定完的話，  
之後只要把新的 commit push 到 GitHub 上，  
Travis CI 就會自動 build blog 啦~  
  
---  
  
# Reference  
  
+ [Publish your Pelican blog on Github pages via Travis-CI](http://blog.mathieu-leplatre.info/publish-your-pelican-blog-on-github-pages-via-travis-ci.html)  
