Title: [Python] [Django] Notes for the Official Django Tutorial (1)
Date: 2013-10-03 06:48
Author: fkz
Category: Python
Tags: Python, django
Slug: python-django-notes-for-the-official-django-tutorial-1
Status: draft

ref: [https://docs.djangoproject.com/en/1.5/intro/tutorial01/][1]    
    
* 檢查 Django 是否已經安裝    
  ``python -c "import django; print(django.get_version())"``  
    
  安裝成功的話會顯示 Django 的版本號，    
  沒有安裝成功的話會顯示 ImportError: No module named Django    
  請回到下方連結重新檢視安裝流程    
  [https://docs.djangoproject.com/en/1.5/intro/install/][2]    
    
    
* 建立一個名為 $projectname 的 Project 資料夾    
  `django-admin.py startproject $projectname`    
    
* 定義 Model 回傳物件的內容  
  
```python  
def __unicode__(self):    
	return self.question  
```  
  
* admin.py 讓管理員界面顯示 Poll 相關應用，新增 admin.py 以後必須重啓 Web Server  
  
```python  
from django.contrib import admin    
from polls.models import Poll  
   
admin.site.register(Poll)   
```  
  
  
[1]: https://docs.djangoproject.com/en/1.5/intro/tutorial01/  
[2]: https://docs.djangoproject.com/en/1.5/intro/install/  
