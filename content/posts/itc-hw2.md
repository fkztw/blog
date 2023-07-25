Title: ITC Hw2  
Date: 2013-11-11 12:34  
Author: fkz  
Category: Course  
Tags: Cryptography, InfoSec, Security  
Slug: itc-hw2  
  
  
# ITC == Introduction To Cryptography  
# Some notes about the Homework #2  
  
---  
  
# 1. Generator  
## (a) Generator  
  
## (b) Diffie-Hellman Key Exange Protocol  
* allows two parties to agree a secret key over an insecure channel without having met before.  
* Its security is based on the discrete logarithm problem in a finite abelian group G.  
![Diffie-Hellman 1](/files/itc-hw2/diffie-hellman-1.png)  
![Diffie-Hellman 2](/files/itc-hw2/diffie-hellman-2.png)  
  
## (c) Man-in-the-Middle attack  
![Man-in-the-Middle](/files/itc-hw2/man-in-the-middle.png)  
  
## (d) ElGamal cryptosystem  
![ElGamal 1](/files/itc-hw2/elgamal-1.png)  
![ElGamal 2](/files/itc-hw2/elgamal-2.png)  
![ElGamal 3](/files/itc-hw2/elgamal-3.png)  
![ElGamal 4](/files/itc-hw2/elgamal-4.png)  
![ElGamal 5](/files/itc-hw2/elgamal-5.png)  
  
#### [Modular multiplicative inverse](https://en.wikipedia.org/wiki/Modular_multiplicative_inverse)  
![Modular multiplicative inverse](/files/itc-hw2/modular-multiplicative-inverse.png)  
  
---  
# 2. Euler’s Theorem is the extension of Fermat’s Theorem.  
## (a) Euler’s totient function  
![Euler’s totient function 1](/files/itc-hw2/eulers-totient-function-1.png)  
![Euler’s totient function 2](/files/itc-hw2/eulers-totient-function-2.png)  
![Euler’s totient function 3](/files/itc-hw2/eulers-totient-function-3.png)  
  
## (b) Euler’s Theorem  
![Euler’s Theorem](/files/itc-hw2/eulers-theorem.png)  
  
## (c) the last 3 digits of 8^803  
![the last 3 digits of 8^803](/files/itc-hw2/the-last-3-digits.png)  
```mathjax  
8^{803}  \mod 1000 \equiv 8 \times 64^{400+1} \mod 1000 \equiv 8 \times 64 \equiv 512  
```  
  
---  
# 3.  
## multiplicative inverse  
![multiplicative inverse 1](/files/itc-hw2/multiplicative-inverse-1.png)  
![multiplicative inverse 2](/files/itc-hw2/multiplicative-inverse-2.png)  
![multiplicative inverse 3](/files/itc-hw2/multiplicative-inverse-3.png)  
  
## finite field  
![finite field 1](/files/itc-hw2/finite-field-1.png)  
![finite field 2](/files/itc-hw2/finite-field-2.png)  
![finite field 3](/files/itc-hw2/finite-field-3.png)  
![finite field 4](/files/itc-hw2/finite-field-4.png)  
![finite field 5](/files/itc-hw2/finite-field-5.png)  
  
---  
# 4. RSA  
  
## p, q, e, n, d  
use [Extended Euclidean algorithm](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm)  
  
---  
# 5. system of equations  
> Still don't get it...  
