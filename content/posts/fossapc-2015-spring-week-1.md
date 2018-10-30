Title: FOSSAPC 2015 Spring Week #1
Slug: fossapc-2015-spring-week-1
Date: 2015-03-02 12:57:15
Authors: m157q
Category: Course
Tags: Course, FOSS, Open Source, Free Software
Summary: A note for 2015 FOSSAPC course in NCTU, Hsinchu, Taiwan
Modified: 2018-10-31 06:13:39

配合課程使用 Hackpad
後續更新請看：

- （舊連結）[2015 FOSS Week #1 Note - fossapc.hackpad.com](https://fossapc.hackpad.com/2015-FOSS-Week-1-Note-JHXVNsJzbeX)
- <https://paper.dropbox.com/doc/2015-FOSS-Week-1-Note--AQlVn_zO14tiQjN8l3w~MBYyAg-3KJYdxX1ubAjMpLZyt7Qa>
（Hackpad 已被 Dropbox 買下來）

---

+ Android Bionic
    + <https://github.com/android/platform_bionic>
    + <http://en.wikipedia.org/wiki/Bionic_(software)>

---

### How A Compiler Works

#### 課程連結：[20150302 - From Source to Binary: GNU Toolchain 是如何運作？ - 自由開源軟體與專案協作](https://sites.google.com/site/fossapc/list-of-lectures/fromsourcetobinarygnutoolchainshiruheyunzuo)
#### 投影片連結：[How A Compiler Works: GNU Toolchain](http://www.slideshare.net/jserv/how-a-compiler-works-gnu-toolchain)

+ 1985 - Richard Stallman - GNU FSF (GNU Free Software Foundation)
+ 屠龍書 - Syntax Directed Translator (SDT)
+ Embedded System - Toolchain 太新或太舊都不行
> 在嵌入式系統中，Toolchain 的版本匹配度影響到個別軟體元件的正確性，如 kernel, libc, graphics framework 等等，而且通常開發者會從個別套件的原始碼一路編譯並建立 system/firmware image，就會遇到各式編譯錯誤、來自個別工具產生的潛在錯誤，或者需要 workaround 的狀況。於是，開發過程就會限定某個版本的 toolchain
+ 第一版 gcc 是 RMS 寫的，之後的版本漸漸偏離 RMS 的初衷
+ Dead Code Elimination
+ Code Motion, Loop invariant, Pointer Aliasing
    + Pointer Aliasing 是 Compiler 最佳化瓶頸之一，如果不同的 Pointer 指向同個 address，會造成某些generic 的最佳化出錯
    + C99, Restrict Pointer Aliasing
        + [Pointer aliasing - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/Pointer_aliasing)
        + In C99, the restrict keyword was added, which specifies that a pointer argument does not alias any other pointer argument.
+ Static Single Assignment (SSA)
+ cc1: 真正的 GNU C Compiler
    + Source Code
    + Simplified AST
    + Gimple IR
    + Tree SSA Form
    + RTL IR (LISP Style)
    + Final SAM
+ Pipeline Scheduling
    + <http://en.wikipedia.org/wiki/Classic_RISC_pipeline>
    + Instruction Fetch, Decode, Execute, Memory Access, Write Back
    + [Hazard (computer architecture) - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/Hazard_%28computer_architecture%29)
+ LLVM
    + UIUC Vikram Adve, Chris Lattner in 2000
    + 高度模組化
    + LLVM bitcode (IR)
    + LLVM 一開始是用 GCC 的 Front-end (GPLv2) 結合自己的 Back-end 成為 llvm-gcc，但 RMS 對 LLVM 這種行為感到非常不滿，並在 gcc43 時將授權改為 GPLv3 來反對 LLVM 這種偷幹 Front-end 的方式，導致後來 Apple 發展自己的 Front-end Clang
> LLVM 的授權是 BSD License，沒有一定要 GPL 形式的強制釋出原始碼條款，但 llvm-gcc 實際上是一種「掏空」GPL 授權的 gcc 的方式，也就是讓 BSD 授權的部份在整個編譯器系統中越來越多，這是 Richard Stallman 不滿之處，他認為 GPL 在這樣的狀況下，不再保證 GPL 的效力。
    + Clang 採模組化設計 (Clang C API)
        + 可 export AST
        + 改善錯誤訊息
    + LLVM Bitcode 用來當傳遞格式還有很多問題
        + Binary Compatibility
    + 目前效能已經逼近 GCC 但還差一點

+ Objective-C
    + 1988
    + Steve Jobs
    + NeXT
    + GCC 2.7

在 Open Source 圈中，誠信是很重要的，千萬別幹抄襲這種事。

---

### Revolution OS

#### 課程連結：[20150302 - 《Revolution OS》影片背景知識補充 - 自由開源軟體與專案協作](https://sites.google.com/site/fossapc/list-of-lectures/revolutionosyingpianbeijingzhishibuchong)

+ [從 Revolution OS 看作業系統生態變化 - fossapc.hackpad.com](https://fossapc.hackpad.com/-Revolution-OS--RrJpYEByzmr)
+ [Revolution OS - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/Revolution_OS)
+ [Revolution OS - YouTube](https://www.youtube.com/watch?v=jw8K460vx1c)
+ 影片裡同時出現了 RMS 和 Linus，可能以後都不會再看到他們同時出現在同個地方了。
    + RMS 是非常純的自由教義派，可以為了 Open Source BIOS 去用[龍芯](http://zh.wikipedia.org/zh-tw/%E9%BE%99%E8%8A%AF)
    + Linus 則是實用主義派，可以為了實用而向沒有 Open Source 妥協，這是 RMS 完全沒辦法接受的。

+ GNU 早期最知名的軟體就是 Emacs
+ MicroSoft NBC 在 Linux 被大量採用的年代很多頭條都是跟 Linux 有關的，形成一股趣味的對比。ex: VA Linux
    + 當年 UNIX 紅到幾乎只要沾上邊就能賺錢，連賣大同電鍋的大同公司當年都搞了一套叫做 MITUX 的 UNIX 系統。
        + [SCO、IBM與Intel將合作開發IA-64架構的UNIX作業系統 | iThome](http://www.ithome.com.tw/node/5632)
        + [MITUX - MITUX系統漫談 # csj@pc2.hinet.net](http://bob.gddfpaper.com/COMPUTER/OS/UNIX/A18.htm)
+ microkernel 的 CMU Mach 影響了 MacOS X 10.0 (Darwin) 和 Windows NT，雖然因為 microkernel 效能太差而沒有採用，但還是取其 flexible 的優點併入 monolithic kernel 形成了結合兩者優點的 hybrid kernel
    + [Mach (kernel) - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/Mach_(kernel))
    + [Microkernel - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/Microkernel)
    + [Hybrid kernel - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/Hybrid_kernel)
    + [Monolithic kernel - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/Monolithic_kernel)
    + [Darwin (operating system) - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/Darwin_%28operating_system%29#Kernel)
        + Darwin is built around XNU, a hybrid kernel that combines the Mach 3 microkernel, ...
    + 關於 microkernel 的發展及介紹可以參考 jserv 的 slides [Microkernel Evolution](http://www.slideshare.net/jserv/microkernel-evolution)

---

### Misc.

+ [history - Why is the Unix linker called "ld" - Programmers Stack Exchange](http://programmers.stackexchange.com/questions/226573/why-is-the-unix-linker-called-ld)
    + Linkers in Linux were originally called loaders.

> Linking the Object code File
> ...Linux comes with its own linker, called ld. (The name is actually short for "load", and "loader" was what linkers were originally called, in the First Age of Unix, back in the 1970s.)
