Title: 用 Python 抓出我在前公司貢獻了多少 GitHub commits  
Slug: fetch-my-github-commits-in-one-organization-with-python-script  
Date: 2017-12-27 21:29:13  
Authors: fkz  
Category: Note  
Tags: GitHub, Python, Python 3, 2018 iT 邦幫忙鐵人賽  
Summary: 如果你想計算你在某個 GitHub organization 的總 commits 數的話，可以參考一下這篇文章。  
Modified: 2018-01-13 20:45:13  
  
  
## 前言  
  
主要是因為[上一篇文章撰寫了離職心得](/posts/2017/12/26/i-left-my-first-full-time-job/)，在寫的過程中想到，好像可以用 GitHub API 抓一下我在前公司這將近兩年的日子到底送了多少 commits。  
  
---  
  
## 正文  
  
廢話不多說，直接進程式碼。  
  
+ 使用 Python 3  
+ 要用到 [github3.py](https://github.com/sigmavirus24/github3.py) 這個 package  
    + 請使用 `pip install --pre github3.py` 來安裝  
    + 使用的版本為 `github3.py (1.0.0a4)`  
+ 雖然可以直接用帳號密碼登入，但因為我有用 2FA，所以直接產生一組 Access Token 比較方便，也比較安全。  
    + 可以到 <https://github.com/settings/tokens> 產生一組，只需要勾選最基本的 repo 權限就行了，詳細可以參考 [GitHub 的官方教學](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/)  
+ 這個 script 可以拿來算你在某個 organization 的總 commits 數，總共 35 行就搞定了。  
  
```python  
#!/usr/bin/env python3  
  
from pprint import pprint  
  
# Make sure you've installed github3.py via `pip install --pre github3.py`  
from github3 import login  
  
  
MY_GITHUB_USERNAME = ""  
# Visit https://github.com/settings/tokens to create a token if you don't have.  
# Check "repo" permission  
MY_GITHUB_TOKEN = ""  
TARGET_ORGNIZATION_NAME = ""  
  
user = login(token=MY_GITHUB_TOKEN)  
org = user.organization(TARGET_ORGNIZATION_NAME)  
my_stats = []  
  
for repo in org.repositories():  
    for contribution in repo.contributor_statistics():  
        if MY_GITHUB_USERNAME in repr(contribution.author):  
            print(repo.name, contribution.total)  
            my_stats.append((repo.name, contribution.total))  
  
print("")  
print('=' * 80)  
print("")  
print("GitHub username: {}".format(MY_GITHUB_USERNAME))  
print("Target GitHub organization: {}".format(TARGET_ORGNIZATION_NAME))  
print("Total contributed repos: {}".format(len(my_stats)))  
print("Total commits: {}".format(sum(commits for repo, commits in my_stats)))  
  
my_stats_desc_sorted = sorted(my_stats, key=lambda x: x[1], reverse=True)  
print("Repo and commits:")  
pprint(my_stats_desc_sorted)  
```  
  
一樣把程式碼開一個 gist 存：<https://gist.github.com/M157q/94be5759d2f13bfdcdd485feff2be3e6>  
  
---  
  
## 結果  
  
```  
GitHub username: M157q  
Target GitHub organization: Tagtoo  
Total contributed repos: 36  
Total commits: 1521  
```  
  
總共在 36 個 repos 貢獻了 1521 個 commits，由於大多是 private repo，所以就不一一秀出了。  
這邊只有算在 master branch 上的 commits 而已，不包含 issue 跟 PR。  
  
---  
  
## 參考資料  
  
+ [hvelarde: How to get statistics about your contributions on a GitHub organization](http://hvelarde.blogspot.tw/2014/01/how-to-get-statistics-about-your.html)  
