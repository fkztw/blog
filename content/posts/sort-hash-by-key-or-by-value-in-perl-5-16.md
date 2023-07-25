Title: Sort hash by key or by value in Perl 5.16  
Date: 2013-05-10 16:38  
Author: fkz  
Category: Note  
Tags: Perl, sort  
Slug: sort-hash-by-key-or-by-value-in-perl-5-16  
Modified: 2015-10-28 15:12  
  
  
`%h = hash, $key = keys in %h`  
  
---  
  
## Sort by key  
  
```perl  
# if key is int  
    # ascending  
    for $key (sort keys %hash) {say "$key: $hash{$key}";}  
  
    # descending  
    for $key (reverse sort keys %hash) {say "$key: $hash{$key}";}  
  
# if key is str (represent number)  
    # ascending  
    for $key (sort {$a <=> $b;} keys %h) {say "$key: $h{$key}";}  
  
    # descending  
    for $key (sort {$b <=> $a;} keys %h) {say "$key: $h{$key}";}  
```  
  
---  
  
## Sort by value (int)  
  
```perl  
    # value of %h is int ($h{$key})  
    # ascending order  
    for $key (sort {$hash{$a} <=> $hash{$b};} keys %h) {say "$key: $h{$key}";}  
  
    # descending order  
    for $key (sort {$hash{$b} <=> $hash{$a};} keys %h) {say "$key: $h{$key}";}  
```  
