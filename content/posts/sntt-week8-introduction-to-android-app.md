Title: SNTT week8 - Android App 入門  
Date: 2013-11-12 13:01  
Author: fkz  
Category: Course  
Tags: Java, Android  
Slug: sntt-week8-introduction-to-android-app  
  
  
# SNTT == Social Network Technology and Trend  
# Android App 入門  
  
## How to work on a Framework  
+ 通常其基礎功能以預先完成且可執行  
+ 有許多 Hook 讓我們能夠增加其行為 (寫好的 library 可以取用 function)  
+ 使傳統的 flow driven 轉變成 event driven  
  
---  
## Java  
+ 物件導向  
+ 靜態、強型別、強分型  
  
### 基礎 Object Orientation  
+ Object  
    + Attribute  
    + Method  
  
---  
## Android Development  
  
+ Java Development Kit (JDK)  
+ Android SDK  
+ Eclipse  
  
### Install  
### Setup Simulator  
> Android Simulator 的速度看起來非常悲劇  
  
### Create An App  
+ Application Name  
+ Project Name  
+ Package Name (Unique, 不可跟別人衝突)  
  
### App 如何執行?  
+ 一個 App 會產生一個獨立的 VM, run 在一個 process 裡面  
+ 利用 JNI 和其他 App 溝通  
+ 必須設定權限  
  
### *.apk 的內容物  
+ Android SDK app  
    + Android manifest  
    + Dalvik class  
    + Resources  
+ Android NDK app  
		+ Android manifest  
    + Dalvik class  
    + Resources  
    + Libraries & JNI  
  
### Application Components  
+ Activities  
    + 包含螢幕 UI 的呈現  
    + 一個 App 會有很多 Activity  
    + 可以想像成一個 UI 畫面就是一個 Activity  
+ Services  
    + 能在背景持續執行  
    + 不能寫太 heavy load 的東西，不然會太耗電  
    + 通常用在需要持續連接網路的程式  
+ Content providers  
    + 資料中心  
    + 會提供一些系統裡面的資料  
+ Broadcast receivers  
    + 訊號接收器  
    + 分成兩種： 有特定接收者 vs 無特定接收者  
  
### Single Activity - 修改 UI  
+ Callback  
    + 將動作寫成 callback 等待 listener 呼叫  
+ Listener  
    + 負責等待事件的發生，並呼叫相應的 callback  
    + OnClick()  
  
### Internet  
+ NetworkOnMainThreadException: (After Android 4.0)  
    + Any potentially long task that may hang your application should not be handled in the main thread.  
    + Android 4.0 之後不允許可能會花長時間的應用程式在 main thread，下載東西就是其中一種。  
    + 解決辦法: 使用其他的 thread 來進行資料傳輸  
  
#### [URLConnection](https://developer.android.com/reference/java/net/URLConnection.html)  
example:  
```java  
//建立新的網址物件  
URL url = new URL("http://example.com/a.txt");  
  
//建立網址連線的物件  
URLConnection conn = url.openConnection();  
  
//連接該網址  
conn.connect();  
  
//建立一個字串物件，將檔案內容接上這個 string 物件  
StringBuilder text = new StringBuilder("");  
int c = -1;  
do {  
    c = input.read();  
    if (c != -1) text.append(c);  
    else break;  
} while (c != -1)  
```  
  
### Multiple Threads  
+ Thread & ThreadHandler  
    + Thread: 專門負責實際上的運作，無法更改UI  
    + ThreadHandler: 負責 Thread 和 UI 之間的溝通  
  
mThread, mThreadHandler, removeCallbacks  
  
### View  
+ ScrollView  
+ TextView  
+ RelativeView  
  
## Objects  
+ Button  
+ Timer  
  
> 寫 App 必須非常重視 UX (User Experience)  
