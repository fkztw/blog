Title: Compiler Design Week 7
Slug: compiler-design-week-7
Date: 2015-04-07 15:40:11
Authors: fkz
Category: Course
Tags: Course, Compiler
Summary: Note for Compiler Design Course in NTHU - Week 7

### LL(1) - Top-Down parsing
+ No ambiguous or left recursive grammar can be LL(1).
    + ambiguous grammar 要先轉成 unambiguous grammar 才有辦法轉 LL(1)

### Recursive decent parsing (Top-Down)
+ Left-most derivation for an input string
    + LL
    + LR
        + 現成的工具比較多

---

# Grammar substitution to revise non-LL(1) into LL(1) grammar
+ Useless and un-reachable grammar handlings
+ Eliminating Ambiguity
+ Eliminating left-recursion
+ Corner substitution
+ Singleton substitution

---

## Useless and un-reachable grammar handlings

### Un-reachable
+ 從 grammar rule 就可得知某個 id 不會被用到，也就是不會被用到
+ Method
    + Step 1: Start from root
    + Step 2: Add reachable Rules
    + Step 3: Until no more
> 師：有點類似 java 裡面的 garbage collection。(mark-N-sweep)  
> 謎：java 有 GC ?!  

### Useless
```
S -> a | b B
B -> b B
```
+ 會被使用到，但是不會出現新東西，不會出現 leaf node，會一直 recursive 下去。
> 師：看起來好像很有用，但其實是 useless  

### Applying sequence
+ Remove Un-reachable => Remove useless => Remove un-reachable => OK
+ Remove Useless => Remove un-reachable => OK
> 師：如果忘記順序，不管順序，多做幾次，做到不會再變了，就是最佳化了。  
> 問：why?  

---

## Eliminating Ambiguity: Ambiguous Grammar
```
E -> E + E
  -> E * E
  -> ID
  -> number
  -> (E)
```
> 師： 考試時看到 ambiguous grammar 就絕對不是 LL(1)  

### Un-Ambiguos Grammar
```
E -> E + term
  -> term
```

### Left Associativity

---

## Eliminating left-recursion
> 師：top-down parsing 不喜歡 left recursion，一定要去除掉。  

### Left-Recursion Conversion
> 師：會造成 infinite loop  
```
S -> Sα|β
```
to  
```
S  -> βS'
S' -> αS'|ε
```
> 師：兩個的 selection set 會一樣  
> //selection set??

### More General Cases
```
S -> Sα_{1} | Sα_{2} | ... | Sα_{n} | β_{1} | β_{2} | ... | β_{n}
```
to   
```
S  -> β_{1}S' | β_{2}S' | ... | β_{n}S'
S' -> α_{1}S' | α_{2}S' | ... | α_{n}S'
```

### Left-Recursion Conversion
```
list -> operand | list operator operand
```
to   
```
list' -> 
```
> //待補  

### Left-Recursion Grammar to Right-Recursion Grammar
```
E -> E + T | T
T -> T * F | F
F -> id | (E)
```
to  
```
E  -> TE'
E' -> +TE' | ε
T  -> FT'
T' -> *FT' | ε
F  -> id | (E)
```
