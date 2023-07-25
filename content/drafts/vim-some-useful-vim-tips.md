Title: [Vim] Some useful Vim tips
Date: 2014-10-30 03:15
Author: fkz
Category: Vim
Tags: Vim, Tips
Slug: vim-some-useful-vim-tips
Status: draft

1. `:<visual>!<shell_command>`  
    + `:%!sort|uniq`  
        + If you are dealing with a list and you want to remove the duplicate name in this list, you can use `:%!sort|uniq` in the vim command mode, then the output of the command will show on the vim and replace the previous content.  
        + The effect just like `cat $previous_vim_content | sort | uniq > $afterward_vim_content` and open the `$afterward_vim_content` file in the Vim.  
        + If the content you are going to change is not whole file but a part of the file, you can use visual mode to select which part you want to apply the shell command then start with the `:` to type the command you wanna apply.  
2. `:w !sudo tee %`  
    + When you forgot to use `sudoedit` or `sudo -e`  
    + `:w !sudo tee > /dev/null` for ignoring the stdout from the `tee` command  
    + After type your sudo passwd, vim will tell you that the file has already been changed. You can press `L` to reload the file and check if your change is correct or not then `:q` to leave.  
    + If you think that `:w !sudo tee %` is too hard for you to remember, you can add `cmap w!! w !sudo tee %` to your `~/.vimrc`. After doing so, you can simply use `:w!!` to do the same thing.  
