Title: ITSE Ch11 - Review Techniques  
Date: 2013-11-25 01:56  
Author: fkz  
Category: Course  
Tags: Software Engineering  
Slug: itse-ch11-review-techniques  
  
  
# NCTUCS 2013-Fall Introduction to Software Engineering by Professor Feng-Jian Wang  
# Ch11 - Review Techniques  
  
## 課前閒聊  
SOA  
CMMI  
  
---  
## Defect Amplification  
+ 每個階段都要有 Review  
+ 有經過 Review 的 Code 可以明顯有效的減少 Code 中的 Bug，避免掉很多產品釋出後的瑕疵  
  
---  
## Metrics  
![Metrics 1](/files/itse-ch11-review-techniques/metrics1.jpg)  
![Metrics 2](/files/itse-ch11-review-techniques/metrics2.jpg)  
  
+ Major Model Error: 會影響到 Database 中的資料、會影響到 Global 的變數、影響到程式邏輯的進行  
+ Minor Model Error: User 覺得怪怪的，但不會影響到程式主要的進行。  
  
---  
## An Example  
+ 因為邏輯上彼此 Ambiguous 的關係，所以在 Review 的過程中，能找出的 Error 有限，通常能夠找出 30% 的 Error 已經算是很不錯的了  
+ Minor Error 出現的次數通常會是 Major Error 的六倍左右  
+ 花在 Testing 的時間通常比 Review 多非常非常多  
  
---  
## Informal Reviews  
+ a simple desk check  
+ a casual meeting  
+ the review-oriented aspects of pair programming  
+ pair programming encourages continuous review as a work product (design or code) is created.  
  
---  
## FTR (Formal Technical Reviews)  
+ Walkthroughs：從頭到尾執行一遍  
+ Inspections：檢查規格是否符合  
  
---  
## Review Options Matrix  
各種 Review 方法的比較表，直接看投影片 p.20 的圖表吧。  
  
---  
## SDRs (Sample-Driven Reviews)  
**SDRs attempt to quantify those work products that are primary targets for full FTRs.**  
  
---  
## Metrics Derived from Reviews  
總之就是各種衡量 Review 效果好不好的指標  
直接看投影片裡面那九個吧  
  
---  
## 課後結語  
+ Review 的時間是有限的  
+ 透過 Metric 來衡量 Review 的效果，透過 Metric 的結果檢視並改善 Review 的方法  
