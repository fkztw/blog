Title: Fifty Shades of Grey - Programmer Version  
Slug: fifty-shades-of-grey-programmer-version  
Date: 2015-02-18 22:36:42  
Authors: fkz  
Category: Note  
Tags: Fifty Shades of Grey, joke, geek, Code Golf  
Summary: When "Fifty shades of grey" comes to programmer. LOL  
  
# Reference  
  
[code golf - Fifty Shades of Grey - Programming Puzzles & Code Golf Stack Exchange](http://codegolf.stackexchange.com/questions/45736/fifty-shades-of-grey)  
  
---  
  
> Boys and girls are excited to see Fifty Shades of Grey on the silver screen, we just want to code without being bothered, so here's a challenge to pick our brain.  
  
然後要求如下：  
  
+ Print on the screen fifty squares filled each with a different shade of grey  
+ If your language of choice lacks image processing capabilities, you could output an image file  
+ Squares must be visible, at least 20 x 20 pixels  
+ You can not use random numbers unless you make sure each shade is unique.  
+ You can not connect to any service over any network  
+ You can not read any files in your program.  
+ You can not use any libraries out of the standard libraries of your language of choice.  
  
  
目前最多人按讚的是 Mathematica 寫的版本，只花 30 chars  
  
```Mathematica  
ArrayPlot[#+5#2&~Array~{5,10}]  
```  
```Mathematica  
ArrayPlot[5#+#2&~Array~{10,5}]  
```  
  
其他還有：  
  
+ CJam - 23 chars  
```CJam  
"P2"1e3K51_,1>K*$K*~]S*  
```  
  
+ Mathematica - 34 chars  
```Mathematica  
GrayLevel[#/50]~Style~50 &~Array~50  
```  
  
+ Sage - 29 chars  
```Sage  
matrix(5,10,range(50)).plot()  
```  
  
+ Java - 180 chars  
```Java  
import java.awt.*;void f(){new Frame(){public void paint(Graphics g){for(int i=1;i<51;g.setColor(new Color(328965*i)),g.fillRect(i%8*20,i++/8*20,20,20))setSize(600,600);}}.show();}  
```  
  
+ R - 35 chars  
```R  
symbols(x,,,x<-50:99,bg=gray(x/99))  
```  
  
+ ipython 2 - 54 chars  
```python2  
t=arange(50);c=t/50.;scatter(t%5,t,500,zip(c,c,c),'s')  
```  
  
+ ipython 2 - 61 chars  
```python2  
imshow(arange(50).reshape(5,10)*.02,'Greys',None,1,'nearest')  
```  
  
+ BBC BASIC - 57 chars  
```BASIC  
FORn=51TO2STEP-1VDU19;-1,n,n,n:RECTANGLEFILL0,0,n*20NEXT  
```  
  
+ C++ - 93 chars  
```C++  
#include <cstdio>  
int main(){for(int i=51;i--;)printf("\e[48;2;%i;%i;%im ",i,i,i);}  
```  
  
+ C - 58 chars  
```C  
main(i){for(i=51;i--;)printf("\e[48;2;%i;%i;%im ",i,i,i);}  
```  
  
+ JavaScript - 72 chars  
```JavaScript  
for(i=90;i>40;)document.write('<font color=#'+i+i+i--+' size=7>&#9632;')  
```  
  
+ JavaScript - 70 chars  
```JavaScript  
for(i=60;--i>9;)document.write('<font color='+i+i+i+' size=7>&#9632;')  
```  
  
一大堆... 剩下懶得看了XDD  
好多沒看過的語言啊...  
是說原來這種比誰寫的 code 短的比賽方式叫 Code Golf 呀  
