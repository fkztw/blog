Title: Error: contextify@0.1.15 install: `node-gyp rebuild`  
Slug: error-contextify-0-1-15-install-node-gyp-rebuild  
Date: 2017-09-01 16:25:08  
Authors: fkz  
Category: Note  
Tags: Node.js, node-gyp  
Summary: Note for solution of "Error: contextify@0.1.15 install: `node-gyp rebuild`"  
  
  
## Preface  
  
Encountered this error of one build on Travis CI of some project.  
  
---  
  
## Solution  
  
Downgrade node to 6.11 which is LTS version can solve this problem.  
  
```  
- nvm install v6.11.2  
- nvm use v6.11.2  
```  
  
Add these two lines into `install` part of `.travis.yml`.  
  
---  
  
## Reference  
  
+ <https://github.com/blackjk3/react-form-builder/issues/11#issuecomment-319307464>  
