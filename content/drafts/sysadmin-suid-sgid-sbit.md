Title: [SysAdmin] SUID, SGID, SBIT
Date: 2013-06-05 18:55
Author: fkz
Category: Sysadmin
Tags: 
Slug: sysadmin-suid-sgid-sbit
Status: draft
  
SUID (Set UID) (chmod 4xxx)    
      
    On binary executing file: (ex: ping, passwd)    
        give the person who run the file temporary permission same as the file owner. (Can't be used on script!)    
      
    On directory: Useless    
    
    
    
SGID (Set GID) (chmod 2xxx)    
    
    On binary executing file:    
        The person who run the file temporarily becomes a member of the file's Group Owner. (Can't be used on script!)    
    
    On directory:    
        All the files and directories which are created under this directory will have the same Group Owner as this directory.    
    
    
    
SBIT (Sticky Bit) (chmod 1xxx)    
      
    On directory: (ex: /tmp)    
            If a user has write and execute permission in this directory. Then all the files and directories created by him/her could only be deleted by himself/herself or by root. It usually be used to create a shared directory. ex: directories on FTP server.    
    
    On file:     
        Setting the sticky bit on a file is pretty much useless, and it doesn’t   
do anything. On some of the older *nix flavors, a sticky bit enabled executable   
file will be loaded to the swap memory after 1st execution, which speeds up   
all subsequent execution. This is not true anymore.[2] (For more details also   
see [4])    
      
    
    
Refs:    
[1] [http://clayssite.com/2009/09/08/suid-guid-and-the-sticky-bit/][1]    
    
[2] [http://www.thegeekstuff.com/2011/02/sticky-bit-on-directory-file/][2]    
    
[3] [http://linux.vbird.org/linux_basic/0220filemanager/0220filemanager-fc4.php#suid_sgid_sbit][3]    
    
[4] [http://en.wikipedia.org/wiki/Sticky_bit][4]  
  
  
  
[1]: http://clayssite.com/2009/09/08/suid-guid-and-the-sticky-bit/  
[2]: http://www.thegeekstuff.com/2011/02/sticky-bit-on-directory-file/  
[3]: http://linux.vbird.org/linux_basic/0220filemanager/0220filemanager-fc4.php#suid_sgid_sbit  
[4]: http://en.wikipedia.org/wiki/Sticky_bit  
