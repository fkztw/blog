Title: 修改 Mac 的截圖儲存位置及格式  
Date: 2014-02-27 14:08  
Author: fkz  
Category: Note  
Tags: Mac, Screenshot  
Slug: change-the-default-screenshot-saving-folder-and-format-on-mac  
  
  
+ 修改內建截圖的儲存位置  
  
`$ defaults write com.apple.screencapture location ${directory}`  
  
`$ killall SystemUIServer`  
  
---  
  
+ 修改內建截圖的儲存格式  
  
`$ defaults write com.apple.screencapture type $type`  
  
type 有 4 種可選:  
  
1. png  
2. jpg  
3. gif  
4. pdf  
  
---  
  
#### Reference  
+ [【Mac技巧】修改Mac系统电脑快捷键截图默认保存路径及修改图片类型](http://my.eoe.cn/sisuer/archive/4711.html)  
