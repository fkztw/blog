Title: Taipei.py 20160331 Meetup Note  
Slug: taipei-py-20160331-meetup-note  
Date: 2016-04-01 09:54:54  
Authors: fkz  
Category: Conf/Meetup  
Tags: Python, Taipei.py, skyfield, astronomy, concurrency, Meetup  
Summary: "Skyfield" & "Uncomplicated Concurrency in Python"  
  
  
<https://www.meetup.com/Taipei-py/events/229246749>  
  
+ Topic 1: Skyfield  
+ Topic 2: Uncomplicated Concurrency in Python  
  
---  
  
# Tutorial about skyfield  
## David Mikolas (david.mikolas@gmail.com)  
<https://tw.pycon.org/2015apac/en/program/72>  
<http://davidmikolas.blogspot.tw/>  
  
+ astropy - clothes  
+ AstroPython  
+ AstroBetter  
    + [Blender](https://www.blender.org/)  
+ <https://www.youtube.com/watch?v=vW93wkDqz54>  
+ [Alfonsine tables](https://en.wikipedia.org/wiki/Alfonsine_tables)  
+ [星歷表](https://en.wikipedia.org/wiki/Ephemeris)  
    + <http://ssd.jpl.nasa.gov/?ephemerides>  
+ [Julian Date](https://en.wikipedia.org/wiki/Julian_day)  
  
---  
  
# Uncomplicated Concurrency in Python  
## Mosky Liu  
  
> It will introduce how to implement the CSP (Communicating Sequential Processes) in Python with common libraries.  
  
> CSP（communicating sequential processes）是一個著名的並行系統（concurrent systems）數學理論 [1]，並獲得 Go lang 採用作為其並行設計的基礎 [2]。其優點是相較於傳統的多執行緒設計來說較為簡單 [3]，依此理論可以設計出更好維護的並行程式。  
  
> 雖然 Python 並沒有特別將 CSP 設計成語言的一部份，但我們仍可以利用常見函數庫內的工具實現 CSP，寫出更好維護的並行程式。講者將介紹各種利用 Python 常見函數庫，包含 event-driven、multithreading、multiprocessing 層級，實現 CSP 的方法。  
  
  
Ctrl-C => SIGINT  
Ctrl-C in Python => KeyboardInterrupt  
  
+ Channel-based Multithreading  
+ With the channel  
    + Channel 讓 Multi-Threading in Python 變得比較好寫  
        + 讓程式裏面只會有 Queue, 不需要費心去處理 join, lock 的問題，只要小心一下 Ctrl-C  
    + Producer-Consumer Pattern  
    + SOA (Service-oriented Architecture)  
+ CSP actually is  
    + a formal language  
        + describing patterns of interaction in concurrent systems  
    + mathematical theories  
    + [process calculi](https://en.wikipedia.org/wiki/Process_calculus)  
  
---  
  
# Lightning Talk  
## Vectorizing String Operation  
  
<http://www.pha8.com/demo.html>  
