Title: The ycmd server SHUT DOWN (restart with ':YcmRestartServer')  
Slug: youcompleteme-ycmd-server-shut-down-restart-with-ycmrestartserver  
Date: 2017-11-27 12:47:33  
Authors: fkz  
Category: Note  
Tags: Vim, YouCompleteMe  
Summary: Noticed YouCompleteMe not working in my Vim and got this message everytime in status bar when Vim starts, so noted the solution.  
  
  
## TL;DR  
  
+ <https://github.com/Valloric/YouCompleteMe/issues/1707#issuecomment-222056711>  
  
```sh  
cd ~/.vim/bundle/YouCompleteMe  
./install.py --clang-completer  
```  
  
---  
  
## Preface  
  
+ YouCompleteMe doesn't work anymore in my Vim.  
+ Got `The ycmd server SHUT DOWN (restart with ':YcmRestartServer')` in status bar everytime Vim starts.  
+ `:YcmRestartServer` always failed.  
+ `:YcmDebugInfo` shows the system path of YouCompleteMe stderr log.  
+ `$ less /tmp/ycmd_52159_stderr_m7n92px1.log`  
+ It shows `ModuleNotFoundError: No module named 'ycm_core'`  
  
---  
  
## Solution  
  
```sh  
cd ~/.vim/bundle/YouCompleteMe  
./install.py --clang-completer  
```  
  
Reinstall YouCompleteMe with Clang completer works.  
  
---  
  
## References  
  
+ <https://github.com/Valloric/YouCompleteMe/issues/914>  
+ <https://github.com/Valloric/YouCompleteMe/issues/1707#issuecomment-222056711>  
