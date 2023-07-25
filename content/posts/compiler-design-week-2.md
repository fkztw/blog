Title: Compiler Design week 2
Slug: compiler-design-week-2
Date: 2015-03-03 15:46:36
Authors: fkz
Category: Course 
Tags: Course, Compiler 
Summary: Note for Compiler Design Course in NTHU - week 2
Modified: 2015/03/05 15:38:00

## 2015/03/03

### Evolution of Programming Languages

+ [List of programming languages by type - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/List_of_programming_languages_by_type)
+ Categorize by feature
    + Imperative
    + Delcarative
    + Von Neumann
    + Object-Oriented
    + Functional
    + Assignment-Oriented
    + Scripting
        + Python, JavaScript, AWK
+ Categorize by Generation
    + 1st Gen - Machine
    + 2nd Gen - Assembly
    + 3rd Gen - Structural Programming (C, Pascal)
    + 4th Gen - SQL
    + 5th Gen - Prolog (logic inference)

---

### Memory Hierarchies

+ Memory Hierarchies
    + Registers
    + Scratch Memory
    + Local Memory
    + Cache
    + Remote Memory
    + Disk
+ 對商用 Compiler 來說，記憶體的架構很重要，會對 Performance 造成頗重大的影響。
+ [Out-of-core Algorithm](http://en.wikipedia.org/wiki/Out-of-core_algorithm)
    + Designed to process data that is too large to fit into a computer's main memory at one time.
    + Must be optimized to efficiently fetch and access data stored in slow bulk memory such as hard drives or tape drives.

---

### Binary Translation

+ 操作位置較接近 Machine code, 而不是 Assembly code
+ Input: Machine Code, Output: Another Machine Code or Assembly Code
    + ARM Machine Code => (Binary Translation) => X86 / MIPS / Andes

---

### Scope

+ 分類
    + Static Binding (Lexical Binding)
        + Scheme, C++, C, Java
        + 直接看 program 的 scope，以最接近的那個上層為主。
    + Dynamic Binding
        + Lisp
        + 從 runtime 的順序反推回去找
    + Fluid Binding (Dynamic Assignments)
        + `var := expr during stmt-body`
        + 當成可以指定特殊條件的 Static Binding
+ 指如何處理 free variable，對於 bound variable 沒有啥問題，無需處理。

---

### Parameter Passing Schemes

+ call by value / call by in
+ call by result / call by out
+ call by value result / call by in Out
+ call by address (本質上為 call by value or call by value of pointer)
+ call by reference
    + 沒有產生額外的 storage
    + 任何修改都會直接反應到 argument
+ call by reference 的變形。三者都使用 Late Binding
    + call by name
        + binding per use
        + caller environment
    + call by text
        + binding per use
        + callee environment
    + call by need (lazy evaluation)
        + [Lazy evaluation - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/Lazy_evaluation)
        + binding at first time use
        + caller environment
    
---

## Chapter 2

### Chomsky Hierarchy

+ Non-R.E.
+ R.E.（RecursivelyEnumerable）
+ Context-Sensitive Grammar
+ Context-Free Grammar (CFG)
+ Regular Expression (regex) 

### Halting Problem

+ [Halting problem - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/Halting_problem)

### Context-Free Grammar

+ [Backus–Naur Form - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/Backus%E2%80%93Naur_Form)
+ BNF (Backus-Naur Form / Backus Normal Form)
    + one of the two main notation techniques for context-free grammars.
+ G = (V, T, P, S)
    + V - A set of non-terminals
    + T - A set of Terminals
    + P - A set of Production Rules
    + S - Starting Symbol

---

## 2015/03/05

### Terminology
+ Alphabet
+ String
+ Language
    + L, L(G)
+ Grammar
    + G

### Derivation Tree
+ [Parse tree - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/Parse_tree)
+ **Not to be confused with Abstract syntax tree.**
+ 分類
    + 直
    + 橫
+ write grammar for balanced expression with '{' and '}'
    + balanced: 左右括號數目要相同
+ write grammr for Palindrome (迴文) 

### Ambiguous Grammar
+ [Ambiguous grammar - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/Ambiguous_grammar)

### Un-Ambiguous Grammar
+ add **Precedence** into Ambiguous Grammar
    + Precedence 低的在外部
    + Precedence 高的在內部

