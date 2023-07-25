Title: Wrong % (matching parens searching) action in Vim  
Date: 2014-08-12 20:27  
Author: fkz  
Category: Note  
Tags: Vim  
Slug: wrong-matching-parens-searching-action-in-vim  
Modified: 2015-10-26 13:04  
  
`cpoptions` in Vim is so complicated...  
  
`{'{,''}’}` this pattern will cause a wrong `%` action (MATCHING PARENTHESES SEARCH) in Vim with default `cpoptions` flag.  
  
A real Example in JavaScript  
  
```javascript  
if (~item.indexOf('\n ')) {  
    space -= item.length;  
    item = !this.options.pedantic  
      ? item.replace(new RegExp('^ {1,' + space + '}', 'gm'), '')  
      : item.replace(/^ {1,4}/gm, '');  
}  
```  
  
  
And if we `:set cpoptions&vi` to change cpoptions let Vim act like VI, the result seems correct.  
  
But after read the doc in Vim, proved it was a coincidence because VI just treat this pattern a PLAINTEXT without considering parens in `“”` or `''`. So, if you remove one of the parens, the result get wrong again.  
  
What I am curious about is that the default syntax highlighting is correct but the % action is wrong in Vim with such pattern.  
  
I know install a plugin like matchit can probably resolve this problem. But is there any built-in method to deal with it?  
  
My friend found this problem while he was trying to fold his code and got an unpredictable result.  
  
  
### References  
+ [Vim finds incorrect matching bracket when using %](http://stackoverflow.com/questions/1903225/vim-finds-incorrect-matching-bracket-when-using)  
