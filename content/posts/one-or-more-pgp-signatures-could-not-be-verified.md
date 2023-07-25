Title: ERROR: One or more PGP signatures could not be verified  
Slug: one-or-more-pgp-signatures-could-not-be-verified  
Date: 2017-11-27 14:56:38  
Authors: fkz  
Category: Note  
Tags: Arch Linux, makepkg, yaourt, AUR, PGP  
Summary: Solution for this error while installing packages from AUR.  
  
  
## TL;DR  
  
`gpg --keyserver keys.gnupg.net --recv-keys ${PGP_PUBLIC_KEY}`  
  
---  
  
## Preface  
  
Encountered this error while installing `firefox-nightly` from AUR  
  
```  
==> Verifying source file signatures with gpg...  
    20171127-firefox-59.0a1.en-US.linux-x86_64.tar.bz2 ... FAILED (unknown public key BBBEBDBB24C6F355)  
==> ERROR: One or more PGP signatures could not be verified!  
==> ERROR: Makepkg was unable to build firefox-nightly.  
```  
  
---  
  
## Solution  
  
`gpg --keyserver keys.gnupg.net --recv-keys BBBEBDBB24C6F355`  
  
---  
  
## References  
  
+ [One or more PGP signatures could not be verified! / AUR Issues, Discussion & PKGBUILD Requests / Arch Linux Forums](https://bbs.archlinux.org/viewtopic.php?id=191954)  
+ [Two PGP Keyrings for Package Management in Arch Linux | Allan McRae](http://allanmcrae.com/2015/01/two-pgp-keyrings-for-package-management-in-arch-linux/)  
