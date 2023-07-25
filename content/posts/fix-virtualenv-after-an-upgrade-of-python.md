Title: Fix virtualenv after an upgrade of Python  
Slug: fix-virtualenv-after-an-upgrade-of-python  
Date: 2015-10-07 15:39:41  
Authors: fkz  
Category: Note  
Tags: Python, virtualenv  
Summary: Always forget how to do it after upgrading Python, so just write it down.  
Modified: 2017-01-16 22:29:41  
  
  
## Manual  
  
```terminal  
$ cd ~/.virtualenvs  
$ find ${envname}/ -type l -delete  
$ virtualenv ${envname}  
```  
  
---  
  
## Script for one virtualenv  
  
Here's a tiny script from [Fix python virtualenv after python update · GitHub](https://gist.github.com/tevino/1a557a0c200d61d4e4fb) for doing this.  
  
```sh  
fix_virtualenv.sh  
---  
#!/usr/bin/env bash  
ENV_PATH="$(dirname "$(dirname "$(which pip)")")"  
SYSTEM_VIRTUALENV="$(which -a virtualenv|tail -1)"  
  
echo "Ensure the root of current virtualenv:"  
echo "    $ENV_PATH"  
read -p "‼️  Say no if you are not sure (y/N) " -n 1 -r  
echo  
if [[ $REPLY =~ ^[Yy]$ ]]; then  
    echo "♻️  Removing old symbolic links......"  
    find "$ENV_PATH" -type l -delete -print  
    echo "💫  Creating new symbolic links......"  
    $SYSTEM_VIRTUALENV "$ENV_PATH"  
    echo "🎉  Done!"  
fi  
```  
  
### Steps  
  
```terminal  
$ source ~/.virtualenvs/${envname}/bin/activate.sh  
$ chmod u+x ./fix_virtualenv.sh  
$ ./fix_virtualenv.sh  
```  
  
---  
  
## Script for all virtualenvs under `~/.virtualenvs`  
  
Based on the above script which for only one virtualenv,  
I modified it to [a slighty powerful script](https://gist.github.com/M157q/e1bf93a4a8170fabac24db9aee686caf) to fix all virtualenvs (include reinstall all modules in a virtualenv).  
  
### One liner (Network needed)  
  
+ `curl`  
    + `sh <(curl -sL https://gist.githubusercontent.com/M157q/e1bf93a4a8170fabac24db9aee686caf/raw)`  
+ `wget`  
    + `sh <(wget -qO- https://gist.githubusercontent.com/M157q/e1bf93a4a8170fabac24db9aee686caf/raw)`  
  
### Plaintext  
  
```bash  
fix_virtualenvs.sh  
---  
#!/usr/bin/env bash  
  
VIRTUALENVS_ROOT_DIR="${HOME}/.virtualenvs"  
ACTIVE_SH_PATH="/bin/activate"  
  
for dir in `find ${VIRTUALENVS_ROOT_DIR} -type d -maxdepth 1`  
do  
    if [[ ${dir} == ${VIRTUALENVS_ROOT_DIR} ]]; then  
        continue  
    fi  
  
    source ${dir}${ACTIVE_SH_PATH}  
  
    ENV_PATH="$(dirname "$(dirname "$(which pip)")")"  
    SYSTEM_VIRTUALENV="$(which -a virtualenv|tail -1)"  
  
    echo  
    echo "Ensure the root of current virtualenv:"  
    echo "    $ENV_PATH"  
    read -p "Say no if you are not sure (y/N) " -n 1 -r  
    echo  
    if [[ $REPLY =~ ^[Yy]$ ]]; then  
  
        read -p "Reinstall all packages of this virtualenv after upgraded? (y/N) " -n 1 -r  
  
  
        if [[ $REPLY =~ "^[Yy]$" ]]; then  
            echo "Dump pip freeze for current virtualenv into requirements.temp"  
            pip freeze > requirements.temp  
        fi  
  
        VIRTUALENV_PYTHON_VERSION=`python --version`  
        echo "Removing old symbolic links......"  
        find "$ENV_PATH" -type l -delete -print  
  
        echo "Creating new symbolic links......"  
        echo ${VIRTUALENV_PYTHON_VERSION}  
        if [[ $VIRTUALENV_PYTHON_VERSION =~ "Python 2" ]]; then  
            echo "Use Python 2 environment for this virtualenv"  
            $SYSTEM_VIRTUALENV "$ENV_PATH" --python=python2  
        elif [[ $VIRTUALENV_PYTHON_VERSION =~ "Python 3" ]]; then  
            echo "Use Python 3 environment for this virtualenv"  
            $SYSTEM_VIRTUALENV "$ENV_PATH" --python=python3  
        else  
            echo "Unknown Python version of this virtualenv"  
        fi  
  
        if [[ $REPLY =~ "^[Yy]$" ]]; then  
            echo "Reinstall modules from previous dumped pip freeze result."  
            pip install -r requirements.temp  
  
            echo "Remove requirements.temp"  
            rm requirements.temp  
        fi  
    fi  
  
    deactivate  
done  
  
echo "Done!"  
```  
  
---  
  
## References  
  
+ [Stéphane Wirtel - Read-Eval-Print Loop](http://wirtel.be/posts/en/2014/07/29/fix_virtualenv_python_brew/) (Dead link)  
+ [Fix python virtualenv after python update · GitHub](https://gist.github.com/tevino/1a557a0c200d61d4e4fb)  
