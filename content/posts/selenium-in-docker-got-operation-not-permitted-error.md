Title: Selenium in Docker got "Operation not permitted" error  
Slug: selenium-in-docker-got-operation-not-permitted-error  
Date: 2017-08-28 12:19:40  
Authors: fkz  
Category: Note  
Tags: Docker, Selenium  
Summary: The error message is "Failed to move to new namespace: PID namespaces supported. Network namespace supported, but failed: errno = Operation not permitted"  
Modified: 2017-09-19 12:51:40  
  
  
## Solutions  
  
Just choose one of the solutions below.  
  
---  
  
#### For Docker  
  
Add `--cap-add SYS_ADMIN` for `docker run` to gain the permission  
  
For example:  
  
```  
$ docker run -it \  
             --cap-add=SYS_ADMIN \  
             -e PYTHONPATH=$(container_work_dir)  
             -p $(site_port_mapping)  
             -p $(admin_port_mapping)  
             -p $(https_port_mapping)  
             -w $(container_work_dir)  
             --name $(project_name)`  
```  
  
---  
  
#### For Selenium  
  
Add `--no-sandbox` while launching Chrome driver  
  
For example:  
  
```  
from selenium import webdriver  
  
chrome_options = webdriver.ChromeOptions()  
chrome_options.add_argument('--no-sandbox')  
chrome = webdriver.Chrome(chrome_options=chrome_options)  
```  
  
---  
  
## References  
  
+ <https://github.com/jessfraz/dockerfiles/issues/65>  
+ <https://stackoverflow.com/questions/43665276/how-to-run-google-chrome-headless-in-docker>  
+ <https://github.com/jessfraz/dockerfiles/issues/17>  
+ <https://github.com/SeleniumHQ/docker-selenium/issues/383>  
+ <https://github.com/elgalu/docker-selenium/issues/58>  
+ <https://github.com/Chatie/wechaty/commit/e68483833f85cfc59879da0daf62f275a0ef9db8>  
