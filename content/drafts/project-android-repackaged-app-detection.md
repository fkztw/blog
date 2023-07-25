Title: [Project] Android Repackaged App Detection
Date: 2014-05-21 18:11
Author: fkz
Category: Project
Tags: Python, android, Repackaged, Detection, Matplotlib, NetworkX
Slug: project-android-repackaged-app-detection
Status: draft

---  
  
## [NetworkX](https://networkx.github.io/)  
### [matplotlib](http://matplotlib.org/)  
+ `import matplotlib.pyplot as plt`  
  
#### Error: No module named matplotlib.pyplot  
+ [Installation](http://matplotlib.org/faq/installing_faq.html)  
+ `$ sudo apt-get install python-matplotlib` in Ubuntu  
  
#### Error: no display name and no $DISPLAY environment variable  
+ [generating a PNG with matplotlib when DISPLAY is undefined](http://stackoverflow.com/questions/2801882/generating-a-png-with-matplotlib-when-display-is-undefined)  
+ [How to save a figure remotely with pylab?](http://stackoverflow.com/questions/4706451/how-to-save-a-figure-remotely-with-pylab/4706614#4706614)  
+   
```python  
import matplotlib  
matplotlib.use('Agg')  
import matplotlib.pyplot as plt  
```  
#### Error: ImportError: ('requires pygraphviz ', 'http://networkx.lanl.gov/pygraphviz ', '(not available for Python3)')  
+ `$ sudo apt-get install python-pygraphviz`  
  
---  
  
