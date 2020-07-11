Title: No more requirements-test.txt for Flit or Poetry while using Tox running tests  
Slug: no-more-requirements-test-txt-for-flit-or-poetry-while-using-tox-running-tests  
Date: 2020-07-11 15:54:19  
Authors: m157q  
Category: Note  
Tags: Python, Poetry, Flit, Tox, setuptools  
Summary: 最近開始用 `pyproject.toml` 取代 `setup.py`, `requirements.txt`, ...，紀錄一下遇到的問題。  


# 前言

目前使用 `poetry` 和 `flit` 這兩套工具，皆可以讀取 `pyproject.toml`。  
但 `flit` 的開發較早，功能也比較陽春一些，如果是剛轉換的話，推薦直接使用 `poetry`。  
兩者最大的差別主要在於 `poetry` 有 lock dependencies 的機制，但 `flit` 沒有。

兩者都可以捨棄 requirements.txt files，與 tox 結合進行測試。

而 `tox.ini` 現在也可以寫在 `pyproject.toml` 裡頭了，請參考：[Basic usage — tox 3.16.2.dev1 documentation](https://tox.readthedocs.io/en/latest/example/basic.html#pyproject-toml-tox-legacy-ini)，所以以下的 `tox` 相關設定都是以這種方式寫在 `pyproject.toml` 裡頭。


# Poetry 解法

## Poetry 官方解法

- [FAQ | Documentation | Poetry - Python dependency management and packaging made easy.](https://python-poetry.org/docs/faq/#is-tox-supported)

```
[tox]
isolated_build = true
envlist = py27, py36

[testenv]
whitelist_externals = poetry
commands =
    poetry install -v
    poetry run pytest tests/
```

將 `tox.ini` 照著上面的方式修改即可。  
可以看到重點是在 `whitelist_externals = poetry` 這行。  
會讓 tox 建立的獨立 virtualenv 可以使用外部的指令。  
所以內部的獨立 virtualenv 便有了 `poetry` 可以用了。（當然前提是外部環境有裝 `poetry`）  

因為 `poetry install` 預設會自行偵測現在使用的 virtualenv，所以會正確將套件安裝到每個由 tox 建立出來的獨立 virtualenv 中。（`-v` 則是詳細顯示出安裝了哪些東西，方便確認是否真的有安裝需要的套件。）

最後就能直接用 `poetry run` 來跑測試了。


## Poetry 另類解法

**先註明：還是比較推薦上述的官方方法，這個另類解法只是提供另外一種紀錄方式，下面會提到其缺點。**

Poetry 有個 `export` 指令，可以將 lock file 轉為其他格式，目前僅支援 `requirements.txt` 的格式：[Commands | Documentation | Poetry - Python dependency management and packaging made easy.](https://python-poetry.org/docs/cli/#export)  
這個方法的邏輯很簡單。以前的 `requirements-test.txt` 是直接存在 repo 裡頭，但現在把它刪除掉，改成每次都透過 `poetry export --dev -f requirements.txt > requirements-test.txt` 產生 `requirements-test.txt`。 完全不用修改 `tox` 相關的設定，用完後再將 `requirements-test.txt` 刪除即可。  
但這個方法有個缺點，可能會安裝過多東西。因為 `poetry export` 的 `--dev` 是將開發相關的套件相依全部納入，並沒有生成只和測試相關套件的 `requirements-test.txt`


# Flit 解法

**這個其實才是我這次想解決的問題，因為某個 side project 在我一開始知道 `pyproject.toml` 後，而 `poetry` 還沒出來之前，就採用了 `flit` 進行套件管理。但 flit 的官方網站又沒有提到遇到跟 tox 的整合該如何處理，所以我參考了 `poetry` 的解法。但因為 `flit` 和 `poetry` 的運作機制不太一樣，所以需要做些調整，紀錄在下面。**

- 參考 Poetry 官方解法，在 `tox.ini` 裡頭使用 `whitelist_externals`
- 但 `flit install` 不會自動偵測目前所使用的 virtualenv，所以安裝的時候預設會裝在 `flit` 自帶的 lib 底下，必須安裝在 `tox` 使用的 virtualenv python lib 底下才有用。
- 還好 `flit install` 有 `--python` 這個選項，只要把 `tox` 使用的 virtualenv python 路徑給他就行了
- 然後發現 tox.ini 有內建變數 `{envpython}` 可以直接拿到 virtualenv python path，就解決了。
	- [tox configuration specification — tox 3.16.2.dev1 documentation](https://tox.readthedocs.io/en/latest/config.html#substitutions-for-virtualenv-related-sections)

以下是在 `pyproject.toml` 裡頭修改後的結果：

```
# Tox
[tool.tox]
legacy_tox_ini = """

[tox]
isolated_build = True
skipsdist = true
envlist = py34,py35,py36,py37,py38

[testenv]
whitelist_externals = flit
commands =
    flit install --extras test --python {envpython}
    pytest -vv --flake8 --cov hor2vec/ --cov-report html --cov-report term --junitxml=test-reports/junit.xml --flake8
"""
```

# 修改前後的對比

![Run tox with flit](/files/no-more-requirements-test-txt-for-flit-or-poetry-while-using-tox-running-tests/run-tox-with-flit.jpg)
