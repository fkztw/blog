Title: ITC week8 - LFSR-based Stream Cipher  
Date: 2013-11-20 04:00  
Author: fkz  
Category: Course  
Tags: Cryptography, InfoSec, Security  
Slug: itc-week8-lfsr-based-stream-cipher  
  
  
#  NCTUCS 2013-Fall Introduction to Cryptography by Professor Rong-Jaye Chen.  
#  LFSR == Linear Feedback Shift Register  
  
## FSR  
Feedback shift register  
![FSR](/files/itc-week8-lfsr-based-stream-cipher/fsr.jpg)  
**connection polynomial:**  
```mathjax  
C(x) = 1 + C_{1}x + C_{2}x^{2} + \cdots + C_{L}x^{L}  
```  
  
## LFSR  
> If the feedback function is linear, the FSR is called LFSR  
  
i.e.  
```mathjax  
S_{L} = C_{1}S_{L-1} + C_{2}S_{L-2} + \cdots + C_{L}S_0{}  
```  
is linear.  
  
---  
  
```mathjax  
\begin{align}  
  
& \text{If } C(x) \text{ is primitive and the initial state } \\  
& (S_{0}, S_{1}, \cdots , S_{L-1}) \text{ is not zero, } \text{the period is } 2^{L} - 1  
  
\end{align}  
```  
  
> A stream cipher constructed by a LFSR alone is not secure.  
  
---  
## Nonlinear combination generators  
  
+ Geff Generator (1973)  
  
## Nonlinear filter generators  
  
## Clcok-controlled generators  
  
+ Stop-and-Go Generators (1987)  
+ The Shrinking Generator (1993)  
+ A5 (the GSM standard)  
+ E0 (Bluetooth's standard encryption)  
  
---  
## GSM A5/1  
[wikipedia - A5/1](https://en.wikipedia.org/wiki/A5/1)  
[Animation of A5/1 cipher](https://www.youtube.com/watch?v=LgZAI3DdUA4)  
