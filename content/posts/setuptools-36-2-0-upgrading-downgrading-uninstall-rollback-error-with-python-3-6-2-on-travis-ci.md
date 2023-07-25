Title: setuptools 36.2.0 upgrading/downgrading uninstall rollback error with Python 3.6.2 on Travis CI  
Slug: setuptools-36-2-0-upgrading-downgrading-uninstall-rollback-error-with-python-3-6-2-on-travis-ci  
Date: 2017-08-27 18:12:22  
Authors: fkz  
Category: Note  
Tags: Travis CI, Python, setuptools  
Summary: Note for situation and solution and more  
  
  
> TL;DR: Just `pip install -U setuptools` before the package which depends on `setuptools` upgrade it.  
  
---  
  
## Preface  
  
A build on Travis CI of one of my side projects got error `AttributeError: 'Distribution' object has no attribute 'install_requires'` while upgrading setuptools from 36.2.0 to 36.7.0 with Python 3.6.2 build job. This build also has Python 3.4 and Python 3.5 build jobs which have no erorr because they didn't need to upgrade `setuptools`.  
  
---  
  
## What's the problem  
  
Travis CI image with `os: linux` and `python: 3.6` labels default installed `Python 3.6.2`, `pip 9.0.1` and `setuptools 36.2.0` in this time. The problem occured while `pip install -U pytest` was running because the default `--upgrade-strategy` of `-U / --upgrade` option of `pip` is `"eager"` which will upgrade all dependent packages to newest version.  
  
> See part of `pip install -h` for detail:  
> ```  
>  -U, --upgrade               Upgrade all specified packages to the newest available version.  
>                               The handling of dependencies depends on the upgrade-strategy  
>                               used.  
>   --upgrade-strategy <upgrade_strategy>  
>                               Determines how dependency upgrading should be handled. "eager"  
>                               - dependencies are upgraded regardless of whether the currently  
>                               installed version satisfies the requirements of the upgraded  
>                               package(s). "only-if-needed" -  are upgraded only when they do  
>                               not satisfy the requirements of the upgraded package(s).  
> ```  
  
  
This made `pip install -U pytest` upgrade `setuptools` from 36.2.0 to 36.7.0 while installing `pytest-3.2.1` and got the error below:  
  
```  
Found existing installation: setuptools 36.2.0  
    Uninstalling setuptools-36.2.0:  
      Successfully uninstalled setuptools-36.2.0  
  Rolling back uninstall of setuptools  
Exception:  
Traceback (most recent call last):  
  File "/home/travis/virtualenv/python3.6.2/lib/python3.6/site-packages/pip/basecommand.py", line 215, in main  
    status = self.run(options, args)  
  File "/home/travis/virtualenv/python3.6.2/lib/python3.6/site-packages/pip/commands/install.py", line 342, in run  
    prefix=options.prefix_path,  
  File "/home/travis/virtualenv/python3.6.2/lib/python3.6/site-packages/pip/req/req_set.py", line 784, in install  
    **kwargs  
  File "/home/travis/virtualenv/python3.6.2/lib/python3.6/site-packages/pip/req/req_install.py", line 851, in install  
    self.move_wheel_files(self.source_dir, root=root, prefix=prefix)  
  File "/home/travis/virtualenv/python3.6.2/lib/python3.6/site-packages/pip/req/req_install.py", line 1064, in move_wheel_files  
    isolated=self.isolated,  
  File "/home/travis/virtualenv/python3.6.2/lib/python3.6/site-packages/pip/wheel.py", line 247, in move_wheel_files  
    prefix=prefix,  
  File "/home/travis/virtualenv/python3.6.2/lib/python3.6/site-packages/pip/locations.py", line 140, in distutils_scheme  
    d = Distribution(dist_args)  
  File "/home/travis/virtualenv/python3.6.2/lib/python3.6/site-packages/setuptools/dist.py", line 365, in __init__  
    self._finalize_requires()  
  File "/home/travis/virtualenv/python3.6.2/lib/python3.6/site-packages/setuptools/dist.py", line 372, in _finalize_requires  
    if not self.install_requires:  
AttributeError: 'Distribution' object has no attribute 'install_requires'  
```  
  
---  
  
## How to fix it  
  
Although there are many comments on [pypa/setuptools #1086](https://github.com/pypa/setuptools/issues/1086) and [pypa/setuptools #1101](https://github.com/pypa/setuptools/issues/1101), I didn't know the exact reason after I read them. But after a little digging on the GitHub, I finally got some clues.  
  
This problem had already been fixed in [pypa/setuptools #1089](https://github.com/pypa/setuptools/pull/1089), but why I still got this problem? Because this fix is [in setuptools-36.2.1](https://github.com/pypa/setuptools/blob/ac7a33c84d74afd3b7453bd880943be9cb4c5787/setuptools/dist.py) not in [setuptools-36.2.0](https://github.com/pypa/setuptools/blob/1eec02038d28506a42bc45d14ef2d54b136cc8bc/setuptools/dist.py), if you use `setuptools-36.2.0` you will still encounter this problem.  
  
Here's [a workarond for this problem](https://github.com/labgrid-project/labgrid/pull/119/files) which is same as the TL;DR, just `pip install --upgrade setuptools` to upgrade it.  
  
---  
  
## Further Discussion  
  
But why? why `pip install --upgrade setuptools` works? why `pip install -U pytest` doesn't? Aren't these two methods just remove `setuptools-36.2.0` and install a newer `setuptools`? According to the result, it's not.  
  
I guess I might have to spend some time on figuring the workflow of `pip`?  
  
---  
  
## References  
  
+ <https://stackoverflow.com/questions/45307110/pip-is-rolling-back-uninstall-of-setuptools>  
+ <https://github.com/pypa/setuptools/issues/1086>  
+ <https://github.com/pypa/setuptools/issues/1101>  
+ <https://github.com/pypa/setuptools/pull/1089>  
