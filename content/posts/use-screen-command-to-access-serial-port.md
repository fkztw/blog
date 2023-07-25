Title: Use screen Command to Access Serial Port  
Date: 2014-10-16 08:12  
Author: fkz  
Category: Note  
Tags: CLI, screen, serial port  
Slug: use-screen-command-to-access-serial-port  
  
  
```sh  
$ screen /dev/ttyS0 19200  
```  
> This command simply opens up a connection to serial port 0 (ttyS0) with a baud speed/rate of 19200  
  
## References  
  
+ [Is there an OS X terminal program that can access serial ports?](http://apple.stackexchange.com/questions/32834/is-there-an-os-x-terminal-program-that-can-access-serial-ports)  
+ [Hidden Features of `screen`](http://serverfault.com/questions/81544/hidden-features-of-screen/81548)  
