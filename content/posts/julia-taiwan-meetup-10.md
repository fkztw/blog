Title: Julia Taiwan Meetup #10  
Slug: julia-taiwan-meetup-10  
Date: 2017-11-17 21:30:48  
Authors: fkz  
Category: Conf/Meetup  
Tags: julialang  
Summary: Note for Julia Taiwan Meetup #10  
  
  
+ 網址：<https://juliataiwan.kktix.cc/events/6e617417>  
  
---  
  
## 開場  
  
+ <https://github.com/JuliaGPU/>  
+ <https://github.com/SimonDanisch/MakiE.jl>  
+ Julia 用來增進效能的方法是直接使用 LLVM IR  
  
---  
  
## OOP and design patterns in Julia - 杜岳華  
  
+ 對 Julia OOP system 和 multiple dispatch 的理解程度  
    + <https://en.wikipedia.org/wiki/Multiple_dispatch>  
+ Composite over inheritance  
+ Decouple the behavior and state  
    + 先不管 behavior，而是先管 datatype  
    + Method 不屬於某個 datatype  
    + Julia 的 OOP 比較著重在 behavior (function) 的部份  
        + 例如以往我們可能得針對信用卡和悠遊卡分別撰寫其儲值這個動作的 function，然後要使用的時候便以 `悠遊卡.儲值()` 或 `信用卡.儲值()` 的方式使用，這種方式又被稱為 single dispatch。  
        + 但 Julia 則是以撰寫儲值這個 behavior 為主，使用時會變成，`儲值.悠遊卡()` 和 `儲值.信用卡()` 的方式使用，這種方式不同於以往習慣的 single dispatch，而是 multiple dispatch。  
+ 如何用 multiple dispatch 寫猜拳遊戲？  
    + The beauty of multiple dispatch  
        + <https://giordano.github.io/blog/2017-11-03-rock-paper-scissors/>  
  
```  
abstract type Shape end  
  
struct Rock <: Shane end  
struct Paper <: Shane end  
struct Scissors <: Shane end  
  
play(::Type{Paper}, ::Type{Rock}) = 1  
play(::Type{Scissors}, ::Type{Papper}) = 1  
play(::Type{Rock}, ::Type{Scissors}) = 1  
  
play(::Type{T}, ::Type{T}) where {T <: Shape} = 0  
  
play(a:Type{<:Shape}, b::Type{<:Shape}) = - play(b, a)  
```  
  
+ 可以把更抽象的代數運算放到 Julia 裡頭去做，但不用像以前一樣寫一大堆 if else。  
+ Design Patterns  
    + Composite pattern  
        + 希望結構上呈現「部份-整體」的概念  
            + 比如說你想畫一張圖  
                + 可能會包含：線、圖片、文字，而圖片裏面可能又會有不同的形狀，所以可以抽象成一個樹狀的結構。  
        + Recursive composition  
            + 可能會有遞迴式的組合  
        + Composite lets clients treat individual objects and compositions of objects uniformly.  
        + Example code  
            + <https://github.com/yuehhua/patterns.jl/blob/master/src/composite.jl>  
            + <https://github.com/yuehhua/patterns.jl/blob/master/test/composite.jl>  
    + Decorator pattern  
        + 例如：可以幫一把槍加上不同的配件，而且同樣的配件還還可以不只加一次。  
        + Example code  
            + <https://github.com/yuehhua/patterns.jl/blob/master/src/decorator.jl>  
            + <https://github.com/yuehhua/patterns.jl/blob/master/test/decorator.jl>  
    + Observer pattern  
        + Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.  
        + Example code  
            + <https://github.com/yuehhua/patterns.jl/blob/master/src/observer.jl>  
            + <https://github.com/yuehhua/patterns.jl/blob/master/test/observer.jl>  
    + Chain of responsibility pattern  
        + Launch-and-leave requests with a single processing pipeline that contains many possible handlers.  
        + 把東西送到某個人手上，如果他能處理就處理，如果不能處理的話，就丟給下一個人處理。  
        + 如果到最後都沒有人處理的話，那就是另外一回事了。  
        + Example code  
            + <https://github.com/yuehhua/patterns.jl/blob/master/src/chain_of_responsibility.jl>  
            + <https://github.com/yuehhua/patterns.jl/blob/master/test/chain_of_responsibility.jl>  
  
---  
  
## 補充  
  
+ <https://github.com/FluxML/Flux.jl>  
+ Julia 的 naming convention 對於 function 的部份，如果 function name 是以 `!` 做結尾的話，代表這個 function 有 side effect。  
+ [Algebraic data type](https://en.wikipedia.org/wiki/Algebraic_data_type)  
+ [GitHub - JuliaComputing/FemtoCleaner.jl: The code behind femtocleaner](https://github.com/JuliaComputing/FemtoCleaner.jl)  
    + [femtocleaner - Cleans your julia projects by upgrading deprecated syntax, removing version compatibility workarounds and anything else that has a unique upgrade path.](https://github.com/apps/femtocleaner)  
+ [GitHub - JuliaStats/TimeSeries.jl: Time series toolkit for Julia](https://github.com/JuliaStats/TimeSeries.jl)  
+ [GitHub - JuliaCI/Nanosoldier.jl: A package for running JuliaCI services on MIT's Nanosoldier cluster](https://github.com/JuliaCI/Nanosoldier.jl)  
    + 可以幫你在 CI 的過程中測 Julia 程式碼的 Performance。  
