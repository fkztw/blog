Title: Travis CI stdout write error and resource temporarily unavailable workaround  
Slug: travis-ci-stdout-write-error-and-resource-temporarily-unavailable-workaround  
Date: 2018-03-30 10:59:48  
Authors: m157q  
Category: Note  
Tags: Travis CI, non-blocking  
Summary: A workaround for Travis CI stdout "write error" or "Resource temporarily unavailable"  
  
  
## TL;DR  
  
`python3 -c 'import os,sys; os.set_blocking(sys.stdout.fileno(), True)'`  
  
Add the line above at `before_install` section of your `.travis.yml` file.  
Specifically, add this line before the line in your `.travis.yml` which causes the error.  
  
This problem won't happen in debug build.  
  
---  
  
## Preface  
  
One of my Travis CI build got `tar: write error` while installing the gcloud SDK.  
I was trying to find the reason in debug build, but got nothing.  
  
---  
  
## Reason  
  
`EAGAIN` (errno 11) in Linux while dealing with non-blocking operations.  
  
Lots of CLI tools expect `stdout` is in blocking mode,  
but it looks like Travis CI set `stdout` to non-blocking mode in default.  
These CLI tools (tar, make, ...) didn't handle `EAGAIN` error well. (Should retry when got this error)  
  
---  
  
## Solution  
  
Add the line below before the line in your `.travis.yml` which causes error.  
You can also add it at `before_install` section of your `.travis.yml`.  
  
`python2 -c 'import os,sys,fcntl; flags = fcntl.fcntl(sys.stdout, fcntl.F_GETFL); fcntl.fcntl(sys.stdout, fcntl.F_SETFL, flags&~os.O_NONBLOCK);'`  
  
For Python 3.5+:  
  
`python3 -c 'import os,sys; os.set_blocking(sys.stdout.fileno(), True)'`  
  
This will turn off the non-blocking mode for stdout.  
  
---  
  
## References  
  
+ [Large writes to stdout sometimes fail with "Resource temporarily unavailable". · Issue #4704 · travis-ci/travis-ci · GitHub](https://github.com/travis-ci/travis-ci/issues/4704#issuecomment-348435959)  
+ [Linux中的EAGAIN含义 - 桂皮猪 - 博客园](http://www.cnblogs.com/pigerhan/archive/2013/02/27/2935403.html)  
+ [linux非阻塞的socket EAGAIN的错误处理 - CSDN博客](https://blog.csdn.net/tianmohust/article/details/8691644)  
