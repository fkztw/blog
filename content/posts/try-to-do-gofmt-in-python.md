Title: 嘗試在 Python 中做到 Golang fmt 的效果  
Slug: try-to-do-gofmt-in-python  
Date: 2018-01-03 23:54:54  
Authors: fkz  
Category: Note  
Tags: Python, formatter, Golang, gofmt, 2018 iT 邦幫忙鐵人賽  
Summary: 嘗試兜出一個在撰寫 Python 程式碼的時也能像 `gofmt` 這樣方便的 code formatter。  
Modified: 2018-01-18 03:11:54  
  
  
## 前言  
  
去年開始學 Golang，但早在這之前就已經聽過很多 Gopher 說過 `gofmt` 有多麼方便，當 Pythonista 還在靠 syntax checker 和自制力來遵守 [PEP8](https://www.python.org/dev/peps/pep-0008/) 的時候，Gopher 根本都不用管什麼 coding style，不管你是怎麼寫的，只要寫好之後用 `gofmt` 執行一下，就可以自動幫你把程式碼排版排好，還可以順便幫你檢查錯誤。  
  
故事起源於 2016 底，和平常不是寫 Python 的朋友一起弄了一個用 Python 寫的 side project，因為朋友平常不是寫 Python 的，然後那陣子他又剛好在寫 Golang，覺得要遵守 PEP8 很麻煩，所以問我 Python 有沒有類似 `go fmt` 的工具。  
  
當下想了一下好像還真的沒有，頂多就是像 `pep8`, `flake8`, `pyflakes` 這類的 syntax checker 而已，好像沒聽聞過什麼好用的 code formatter，也因為這樣，所以開始想辦法做到這件事。  
  
當然真的去查了之後發現還是有的，但使用起來不盡理想。於是找了些現成的程式兜一兜，再加上 git pre-commit hook 後，最後算是勉強做到了，當下有做個凌亂的紀錄，但一直沒有整理成一篇文章，利用最近離職後比較閒的時間，把它整理紀錄一下。  
  
---  
  
## 紀錄  
  
當時一開始是直接找到 GitHub 上的這個 repo: [GitHub - Psycojoker/pyfmt: automatic code formatter for python following pep8 using baron FST, like gofmt](https://github.com/Psycojoker/pyfmt)。  
  
看起來好像不錯，但實際上使用起來有滿多問題的，而且作者又用了另外一個自己寫的 Python Full Syntax Tree library: [GitHub - PyCQA/baron: IDE allow you to refactor code, Baron allows you to write refactoring code.](https://github.com/PyCQA/baron)，當時因為急著找現成的工具來用，所以就沒有多花時間研究。但後來才發現 PyCQA 裡頭的工具都滿不錯的: [Python Code Quality Authority · GitHub](https://github.com/PyCQA)，基本上都是用來提升 Python 程式碼品質的工具，滿推薦寫 Python 的人看一下的。  
  
---  
  
之後試了幾個工具以後，最後變成 `autoflake` + `isort` + `autopep8` + git pre-commit hook 來做到這件事，老實說真的有點繁瑣，但我找不到更好的方法，如果有人知道的話還請不吝告知。  
  
總之，接下來稍微介紹一下這幾個工具分別做了哪些事：  
  
+ `autoflake`  
    + [GitHub - myint/autoflake: Removes unused imports and unused variables as reported by pyflakes](https://github.com/myint/autoflake)  
    + 就如同其 GitHub 的敘述，可以把沒有用到的 `import` 和變數移除。  
+ `isort`  
    + [GitHub - timothycrosley/isort: A Python utility / library to sort imports.](https://github.com/timothycrosley/isort)  
    + 可以針對 Python 的 imports 做符合 PEP8 的字母序排序。  
+ `autopep8`  
    + [GitHub - hhatto/autopep8: A tool that automatically formats Python code to conform to the PEP 8 style guide.](https://github.com/hhatto/autopep8)  
    + 可以將 Python 程式碼自動以符合 PEP8 的方式排版。  
+ git pre-commit hook  
    + [Git - Git Hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)  
    + pre-commit hook 的觸發時間是在使用者下 `git commit` 後，編寫 commit message 之前。  
    + 這裡是用來確保使用者每次 commit 的 Python 程式碼會被以上這三種程式處理過。  
  
---  
  
後來發現 Google 也出了一個 Python formatter: [GitHub - google/yapf: A formatter for Python files](https://github.com/google/yapf)，用了以後覺得比 `autopep8` 好用，所以就把 `autopep8` 換成 `yapf` 了：[Use yapf instead of autopep8 as python code formatter. · pellaeon/fengyuan@abc9fc9 · GitHub](https://github.com/pellaeon/fengyuan/commit/abc9fc995a9c49fa208716954c2bc262fe6b783e)  
  
---  
  
## 結果  
  
最後的結果就是整合到一個 git pre-commit hook 裡頭，麻煩的是 clone 下來以後，得用這個指令初始化 git pre-commit hook：  
  
```  
ln -sf ../../pre-commit.sh .git/hooks/pre-commit  
```  
  
其實還是很麻煩，之後應該會再繼續尋找有沒有更方便的方法，不排除自己寫一個就是。  
  
最後的結果就是一個 git pre-commit hook：[fengyuan/pre-commit.sh at master · pellaeon/fengyuan · GitHub](https://github.com/pellaeon/fengyuan/blob/master/pre-commit.sh)  
  
以下直接複製貼上原程式碼留個紀錄，以防哪天 GitHub 掛了。  
  
```sh  
#!/bin/sh  
#  
# An example hook script to verify what is about to be committed.  
# Called by "git commit" with no arguments.  The hook should  
# exit with non-zero status after issuing an appropriate message if  
# it wants to stop the commit.  
#  
# To enable this hook, rename this file to "pre-commit".  
  
if git rev-parse --verify HEAD >/dev/null 2>&1  
then  
	against=HEAD  
else  
	# Initial commit: diff against an empty tree object  
	against=4b825dc642cb6eb9a060e54bf8d69288fbee4904  
fi  
  
# If you want to allow non-ASCII filenames set this variable to true.  
allownonascii=$(git config --bool hooks.allownonascii)  
  
# Redirect output to stderr.  
exec 1>&2  
  
# Cross platform projects tend to avoid non-ASCII filenames; prevent  
# them from being added to the repository. We exploit the fact that the  
# printable range starts at the space character and ends with tilde.  
if [ "$allownonascii" != "true" ] &&  
	# Note that the use of brackets around a tr range is ok here, (it's  
	# even required, for portability to Solaris 10's /usr/bin/tr), since  
	# the square bracket bytes happen to fall in the designated range.  
	test $(git diff --cached --name-only --diff-filter=A -z $against |  
	  LC_ALL=C tr -d '[ -~]\0' | wc -c) != 0  
then  
	cat <<\EOF  
Error: Attempt to add a non-ASCII file name.  
  
This can cause problems if you want to work with people on other platforms.  
  
To be portable it is advisable to rename the file.  
  
If you know what you are doing you can disable this check using:  
  
  git config hooks.allownonascii true  
EOF  
	exit 1  
fi  
  
# Run syntax checker and formatter for Python files.  
STAGED_PYTHON_FILES=$(git diff --cached --name-only HEAD "*.py")  
  
if [ "$STAGED_PYTHON_FILES" != "" ]  
then  
    autoflake -i --remove-all-unused-imports --remove-unused-variables $STAGED_PYTHON_FILES  
    isort -y $STAGED_PYTHON_FILES  
    yapf -i $STAGED_PYTHON_FILES  
    git add $STAGED_PYTHON_FILES  
fi  
```  
  
---  
  
## 參考來源  
  
+ [GitHub - Psycojoker/pyfmt: automatic code formatter for python following pep8 using baron FST, like gofmt](https://github.com/Psycojoker/pyfmt)  
+ [GitHub - PyCQA/baron: IDE allow you to refactor code, Baron allows you to write refactoring code.](https://github.com/PyCQA/baron)  
+ [GitHub - myint/autoflake: Removes unused imports and unused variables as reported by pyflakes](https://github.com/myint/autoflake)  
+ [GitHub - timothycrosley/isort: A Python utility / library to sort imports.](https://github.com/timothycrosley/isort)  
+ [GitHub - hhatto/autopep8: A tool that automatically formats Python code to conform to the PEP 8 style guide.](https://github.com/hhatto/autopep8)  
+ [Git - Git Hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)  
+ [GitHub - google/yapf: A formatter for Python files](https://github.com/google/yapf)  
+ [Use yapf instead of autopep8 as python code formatter. · pellaeon/fengyuan@abc9fc9 · GitHub](https://github.com/pellaeon/fengyuan/commit/abc9fc995a9c49fa208716954c2bc262fe6b783e)  
+ [Add git pre-commit hook for python files. · pellaeon/fengyuan@2de3e19 · GitHub](https://github.com/pellaeon/fengyuan/commit/2de3e199f2193ea25f4cd5bbb7f89673879862c6)  
+ [fengyuan/pre-commit.sh at master · pellaeon/fengyuan · GitHub](https://github.com/pellaeon/fengyuan/blob/master/pre-commit.sh)  
