Title: Use my old vimrc for NeoVim
Slug: use-my-old-vimrc-for-neovim
Date: 2018-07-23 05:02:21
Authors: fkz
Category: Note
Tags: Vim, NeoVim, Vundle
Summary: Just need some modifications and we are good to go for using old vimrc for NeoVim.


## Preface

Lately, I am trying to use NeoVim instead of Vim.
Yet, I am too lazy to write a new config for NeoVim, just want to use the `vimrc` I am using.
I've been using Vundle as my Vim plugin manager for a long time and I want to use it as my NeoVim plugin manager as well.

---

## Note

#### NeoVim use `~/.config/nvim/init.vim` as user config file.

Add soft link so we can make Vim and NeoVim share the same config file.

+ `mkdir -p ~/.config/nvim`
+ `ln -s ~/.vimrc ~/.config/nvim/init.vim`

#### Some modifications for `vimrc`

+ Add these lines at first of `vimrc` for Vundle to use different dir for Vim and NeoVim.

```vimrc
if has('nvim')
    let s:editor_root=expand("~/.config/nvim")
    set rtp+=~/.config/nvim/bundle/Vundle.vim
else
    let s:editor_root=expand("~/.vim")
    set rtp+=~/.vim/bundle/Vundle.vim
endif
```


+ Add this line before `call vundle#begin()` in `vimrc` to make Vundle use different dir for Vim and NeoVim.

```vimrc
call vundle#rc(s:editor_root . '/bundle')
```

That's it.

---

## References

+ [Switching to NeoVim (Part 1) | AruSahni.net](https://arusahni.net/blog/2015/03/switching-to-neovim-part-1.html)
+ [Switching to NeoVim (Part 2) | AruSahni.net](https://arusahni.net/blog/2015/04/switching-to-neovim-part-2.html)
