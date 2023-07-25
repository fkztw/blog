Title: 關於 Django 的 F() expressions, Q object, Aggregation 的一些筆記  
Slug: about-django-f-expression-q-object-and-aggregation  
Date: 2017-12-28 23:15:00  
Authors: fkz  
Category: Note  
Tags: Python, Django, 2018 iT 邦幫忙鐵人賽  
Summary: 以前維護離職同事留下來的程式碼時做的一些筆記，當時沒有發文，時隔一年才整理成這篇文章。  
  
  
## 前言  
  
這篇算是在清草稿，約莫一年前紀錄在自己使用的 Trello board 的其中一張 card 裏面。  
  
當時接手維護已離職的前同事的專案，是當時將員工內部使用的後台前後分離出來的網頁後端伺服器。他透過使用 Django 的 F() expressions, Q object, Aggregation 創造了一個 base view class（命名為 `ModelView`），讓所有繼承這個 base class 的 view 都可以有類似 GraphQL 的效果，可以接收帶有符合 Django Query 參數的 json request 後，直接透過 model 去拿資料，再把資料包成 json response 吐回去。  
  
這讓新增新的 API 變得很簡單，只要以下幾個步驟：  
  
+ 定義好新的 model  
+ 寫一個新的 View 繼承自 `ModelView`  
    + 第一行宣告繼承，第二行寫說對應到哪個 model 就行了  
    + 只要兩行，所有的 CRUD 以及 response 都會自動處理好  
+ 在 `urls.py` 裡頭新增對應到該 View 的網址  
  
真的是用了滿多黑魔法的，我們在開發的時候都開玩笑得說：「這算是『魔改 Django』了吧？」但因為程式碼是放在 private repo，所以以下就只紀錄當時我去 trace source code 時紀錄的一些筆記。  
  
最讓我覺得厲害的地方是，前同事 Jay 寫出這個東西之前根本沒碰過 Django，雖然其中也有問我一些問題，但他大概只花 3 個月就寫出這東西，後來我去看他寫的程式碼發現許多地方我看不懂，讓我挺佩服的。有點可惜這裡不能拿程式碼來一一講解就是。  
  
---  
  
## [`F()` expressions](https://docs.djangoproject.com/en/1.10/ref/models/expressions/#f-expressions)  
  
+ > An `F()` object represents the value of a model field or annotated column. It makes it possible to refer to model field values and perform database operations using them without actually having to pull them out of the database into Python memory.  
+ 不會真的從 db 拿出值，可以減少 db query，讓效能好一點。  
+ 使用 `F()` 以後，要真的更新值的話，必須要使用 `refresh_from_db()`，`save()` 只會先紀錄而已，並不會真的寫入。  
+ 可以避免 race condition 的問題，因為每個人不用拿到現在的值以後才去做更改，只要每個動作都有 `save()` 的話，最後再一次 `refresh_from_db()` 就好。  
+ > `F()` assignments persist after `Model.save()`  
    + 如果 `save()` 兩次的話，就會作用兩次。  
  
---  
  
## [Q object](https://docs.djangoproject.com/en/1.10/topics/db/queries/#complex-lookups-with-q)  
+ Django `QuerySet` 的 `filter()` 基本上只能處理 AND 的 Query，如果想要使用 OR 或者更複雜一點的 Query 的話，就必須要使用 `Q()`。  
  
---  
  
## [Aggregation](https://docs.djangoproject.com/en/1.10/topics/db/aggregation/)  
  
+ `QuerySet.annotate()`  
    + 回傳一個 `QuerySet`，可以給 `admin.ModelAdmin` 使用。  
    + 基本上等同於 SQL 語句的 `AS`。  
    + 可搭配 `values()`, `order_by()` 做到 SQL 語句的 `GROUP BY`。  
    + `values()` 和 `annotate()` 的前後順序生出來的 Query 語句是有差別的。  
+ `QuerySet.aggregate()`  
    + 回傳一個 dictionary，基本上就是拿來統計數字用而已。  
+ 使用 `print(QuerySet.query)` 來察看 QuerySet 生成的 SQL query statement.  
  
---  
  
## 後記  
  
讓我有點不勝唏噓的是，筆記內容的連結依然是 Django 1.10，一年半前是最新的版本，但現在點進去已經顯示 **"This document is for an insecure version of Django that is no longer supported. Please upgrade to a newer release!"** 了。  
