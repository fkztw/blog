Title: Compiler Design Week 3
Slug: compiler-design-week-3
Date: 2015-03-10 15:47:17
Authors: fkz
Category: Course
Tags: Cousre, Compiler
Summary: Note for Compiler Design Course in NTHU - Week 3
Modified: 2015-03-19 16:00:00

## 2015/03/10

### Left-Recursion Grammar & Right-Recursion Grammar
+ 兩者可以互轉
+ Left-Recursion => Left Associate, Right-Recursion => Right Associate.

#### Left-Recursion Conversion
```
S -> Sα | β

to

S  -> βS'
S' -> αS' | ɛ
```

### Parser for a Grammar
+ Top-down Parser / LL(1) Parser
+ Bottom-up Parser / LR(1) Parser

---

## Chapter 3 - Regular Expression

### Regular Expression
+ Regular Expresssion aka Regular Grammar, Regular Language, Regular, Regex  
+ \* - Kleene Closure
    + aka Kleene Operator, Kleene Star.
    + [Kleene star - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/Kleene_star)

### FSA - Finite State Automata
+ Regular Expression <=> Finite State Machine
+ 5-tuple (Q, Σ, δ, q。, F)
    + Q - a set of states
    + Σ - an input alphabet, symbol.
    + δ - a transition function
    + q。 - the initial state
    + F - a set of final states
+ DFA vs NFA
+ Finite => State 數量是有限的
+ 沒有 Memory, 無法記憶 alphabet 的數量

### Thompson Construction
+ [Thompson's construction algorithm - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/Thompson%27s_construction_algorithm)
+ Transforms a given regular expression into an equivalent nondeterministic finite automaton (NFA)
+ Establishing a conversion between two of many description formats for regular languages.

