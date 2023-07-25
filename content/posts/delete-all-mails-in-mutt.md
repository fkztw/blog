Title: Delete all mails in Mutt  
Date: 2014-08-01 12:37  
Author: fkz  
Category: Note  
Tags: CLI, Mutt  
Slug: delete-all-mails-in-mutt  
Modified: 2015-10-26 14:51  
  
  
## How-to  
  
1. `D` - press **Shift-d** (delete pattern)  
2. `~s .*` then press **enter**. Mutt will flag all mail with a D.  
    + or just `.*`  
3. `q` to quit mutt  
    + confirm deletion before exit.  
  
another way  
  
1. `T` - tag pattern mode  
2. `~s .*` -  tag all mails  
3. `;d` - delete tagged mails  
4. $ (**Shift+4**) - to sync change to your mailbox or `q` to quit mutt  
  
---  
  
## Reference  
  
[Deleting all e-mail messages in your inbox with mutt](http://major.io/2009/06/19/deleting-all-e-mail-messages-in-your-inbox-with-mutt/)  
