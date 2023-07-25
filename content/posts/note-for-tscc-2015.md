Title: Note for TSCC 2015  
Slug: note-for-tscc-2015  
Date: 2015-05-02 16:27:52  
Authors: fkz  
Category: Note  
Tags: TSCC, HPC, Competition  
Summary: A note for the TSCC 2015 Final  
Modified: 2015-08-27 16:39:17  
  
  
## System Preparation  
  
---  
  
## [HPL](http://www.netlib.org/benchmark/hpl/)  
  
---  
  
### [LAMMPS](http://lammps.sandia.gov/)  
  
---  
  
### [Einstein toolkit](http://einsteintoolkit.org/)  
  
#### References  
+ <https://sites.google.com/site/lincytw/cactus>  
+ <https://docs.einsteintoolkit.org/et-docs/Tutorial_for_New_Users>  
+ <http://collapse2013.fudan.edu.cn/collapse/Talks/Loeffler.pdf>  
+ <http://www.linuxjournal.com/content/numeric-relativity-einstein-toolkit>  
  
#### Installation  
##### Get Herschel tarballs (released on Nov 19th, 2014)  
```  
$ curl -kLO https://raw.githubusercontent.com/gridaphobe/CRL/ET_2014_11/GetComponents  
  
$ chmod a+x GetComponents  
  
$ ./GetComponents --parallel https://bitbucket.org/einsteintoolkit/manifest/raw/ET_2014_11/einsteintoolkit.th  
```  
May need to wait about 5 minutes (depend on the network speed)  
After this, you should have a directory called "Cactus" contains tons of files.  
  
##### Compile  
Configuration files can be found at `Cactus/simfactory/mdb/optionlists/*.cfg`  
The thornlist determine what to compile, can be found at `Cactus/thornlists/*.th`.  
Default will on ly have `einsteintoolkit.th`  
Find the proper config file and thornlist then copy them to the Cactus/  
  
```  
$ cd Cactus  
$ make <NAME>-config THORNLIST=BSSN_Hydro.th options=c3.cfg  
## Then config. You need say "yes" if asked.  
$ make <NAME>  
```  
  
<NAME\> is the name of the setting user-defined variable.  
You can have different settings with different names.  
Here I use tscc.  
  
##### Debug  
  
1. Add `#include <math.h>` into `arrangements/EinsteinAnalysis/AHFinderDirect/src/jtutil/cpm_map.cc`  
  
---  
  
### 多核心高效能程式調教  
  
#### keywords  
OpenMP, MPI, CUDA, OpenCL  
  
+ CUDA  
    + [Nice Series of CUDA Tutorials on ptt.cc | Just for noting](https://fkz.github.io/posts/2015/08/15/nice-series-of-cuda-tutorials-on-ptt-cc/)  
