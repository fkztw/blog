Title: Cat System Workshop #17 Full-Stack IoT Development 探索之旅  
Slug: cat-system-workshop-17-full-stack-iot-development-探索之旅  
Date: 2017-03-14 22:31:17  
Authors: fkz  
Category: Conf/Meetup  
Tags: IoT, Node.js  
Summary: Note for <http://skymizer.kktix.cc/events/cat170314>  
  
  
Speaker: [Simen](https://github.com/simenkid)@[sivann](http://www.sivann.com.tw/)  
> 前半段是 IoT Development 相關  
> 後半段則是 JavaScript Web development 和 Node.js 開發大全  
  
---  
  
### Google Weave  
  
+ <https://developers.google.com/weave/>  
  
---  
  
### Android Things (Brillo)  
  
<https://developer.android.com/things/hardware/index.html>  
  
+ 專為 IoT 設計的 OS  
+ 35 MB RAM  
  
---  
  
### Apple HomeKit  
  
+ 體系相對封閉  
+ 語音助手 (Siri)  
+ 認証: MFi  
  
iOS (SDK)  
HomeKit API  
HomeKit Accessory Protocol (HAP)  
  
---  
  
### Eclipse IoT Working Group  
  
+ Open Source and Open Standards for IoT  
    + New and Existing Devices  
    + IoT Gateways  
    + Network Carriers  
    + Backend Systems  
+ IoT Suite  
    + oneM2M: REST interface  
    + OMA LWM2M Server - Leshan  
    + Gateway stack - Kura  
    + CoAP - Californium (Java)  
    + MQTT - Mosquitto/Paho  
        + Paho 提供了不同語言實作的 MQTT client  
            + 有 C++, Java, JavaScript ...  
    + MQTTSN (Eclipse 自己設計的)  
  
#### Kura - IoT Gateway Stack/ App Framework  
  
+ Edge Nodes (clients, 連網的裝置)  
    + Local Automation  
+ M2M Integration Platform  
+ Enterprise Interfaces  
    + Business Applications (Mobile Apps, Web Apps, ...)  
  
---  
  
### Web Of Things  
  
#### Google Physical Web  
  
+  Eddystone  
    + <https://en.wikipedia.org/wiki/Eddystone_(Google)>  
    + <https://github.com/google/eddystone>  
    + <https://developers.google.com/beacons/>  
+ MT7697  
  
---  
  
IoT Platform  
  
+ [Ayla](https://www.aylanetworks.com/)  
+ [ubiworx](https://ubiworx.com/)  
+ [SAMSUNG SmartThings](https://www.smartthings.com/)  
  
---  
  
### Front-end and Back-end  
  
+ Web Front-end  
    + Web 1.0  
        + F5 刷新  
    + Web 2.0+  
        + HTML RSP  
        + AJAX  
        + HTML5  
        + [WS (WebSocket)](https://tools.ietf.org/html/rfc6455)  
        + [SSE (Server-Sent Events)](https://www.w3.org/TR/2011/WD-eventsource-20110208/)  
    + MVP (Web 2.0+)  
        + 代表性的案例：jQuery  
    + MVVM (Framework)  
        + V (user), VM (framework), M <---client-side-----------server-side---> M  
        + server 一有資料更新就會 push 過來或是背後會一直去跟 server 要資料，所以使用者端會覺得資料是即時的  
    + React.js  
        + 使用 JavaScript (JSX) 撰寫 View (React)  
        + Virtual DOM  
        + Controller View = View + State Machine + Controller  
        + 單向數據流架構化 (Flux)  
        + 單一數據源、狀態大總管 (Redux)  
+ Web Back-end (JavaScript related)  
    + Package Manager  
    + Task Runner  
        + grunt, gulp, npm, webpack  
    + Pre-compiler Transpiler  
    + Linter  
    + Utils  
    + Bundler  
        + webpack, RequireJS (AMD), Browserify (CommonJS)  
    + Dev Server  
        + uglify, watchify  
  
---  
  
### Node.js  
  
+ Server-side, JS runtime  
+ Async I/O - libuv  
+ Concurrenty - Event Loop  
    + timers  
    + I/O callbacks  
    + idle, prepare  
    + poll  
    + check  
    + close callbacks  
+ <https://simeneer.blogspot.tw/2016/09/nodejs-eventemitter.html>  
+ 除錯工具  
    + 原生除錯工具  
        + `break;`  
        + `$ node debug app.js  # c, n, s, o`  
    + 第三方工具  
        + node-inspector  
            + `$ node-debug app.js`  
        + iron-node  
            + `$ iron-node app.js`  
        + devtool  
            + `$ devtool app.js`  
    + IDE 內建的除錯模組  
+ 除錯訊息與日誌 (Logging)  
    + stdout / stderr [+ pipe][+ redirect]  
        + `console.log();`  
        + `console.error();`  
    + 第三方模組  
        + `$ npm install debug --save`, `$ DEBUG=namespace node app.js`  
        + `$ npm install winston --save`, `$ node app.js`  
        + `$ npm install bunyan --save`, `$ node app.js | bunyan [opts]`  
        + `$ npm install pino --save`, `$ node app.js | pino-<xxx>`  
            + 號稱 Node.js 的 logging module 裡頭速度最快的  
        + intel, log4js, loggly, bole  
+ 測試框架/工具  
    + Hosted CI Services  
        + Travis CI, Circle CI, GitLab Ci, wercker, codeship  
    + Test Framework  
        + mocha, jasmie-node, tape, tap  
    + Assertions  
        + assert, should, expect, chai  
    + Test Double  
        + sinon.js  
    + Code Coverage  
        + istanbul, JSCover, blanket.js  
  
---  
  
### 物聯網大亂鬥  
  
+ Network Topology  
    + p2p  
    + star  
        + 目前的藍芽  
    + star-of-star  
    + Mesh  
        + 有自我修復的功能  
        + ZigBee  
            + <https://en.wikipedia.org/wiki/ZigBee>  
+ 依區域範疇劃分  
    + Near Field  
        + < 10 cm  
        + NFC Forum  
    + PAN  
        + 1m ~ 50m  
        + Bluetooth, ZigBee, Thread, IEEE 802.15.4  
    + LAN  
        + 50m ~ 1km  
        + Wi-Fi, Ethernet  
    + (LP)WAN  
        + 1km ~ 50km  
        + [SigFox](https://en.wikipedia.org/wiki/Sigfox), [LoRa](http://www.semtech.com/wireless-rf/internet-of-things/what-is-lora/), 5G, 4G, 3G, Internet  
+ 常見 PAN/WAN 之特性  
    + EnOcean  
    + ZigBee  
    + Thread  
    + BLE  
    + WiFi  
