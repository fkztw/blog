Title: Change from Travis CI Build Matrix to Build Stages  
Slug: change-from-travis-ci-build-matrix-to-build-stages  
Date: 2020-07-11 21:40:20  
Authors: m157q  
Category: Note  
Tags: CI, Travis CI  
Summary: How I changed from Travis CI Build Matrix to Build Stages for my side project.


**CAULTION: This post was written in April, 2018. Build Stages feature is beta at that time. Things may have changed, but I still want to write it down.**  


# Preface

- [Build Stages - Travis CI](https://docs.travis-ci.com/user/build-stages/)

Official documents about how to migrate from Build Matrix to Build Stages are awful.  
It took me lots of time and still don't know how to modify it until I met this: [Travis CI stage failed in matrix - Stack Overflow](https://stackoverflow.com/questions/49387696/travis-ci-stage-failed-in-matrix/49409551#49409551)

This beta feature is great, although I had already used CircleCI which already had build stages feature at that time.  
Maybe write this down can help you save your time.


# TL;DR

In the end, I found that the syntax of Build Stages is similar to Build Matrix.
I don't know how to explain it, so I'll just put the diff picture and url below:

- <https://github.com/zdict/zdict/compare/7567afa...2209204>
- ![Travis CI Build Matrix vs Build Stages](/files/change-from-travis-ci-build-matrix-to-build-stages/travis-ci-build-matrix-vs-build-stages.jpg)


# Final Result

- [.travis.yml which already used Build Stages](https://github.com/zdict/zdict/blob/2209204aa70e80720823f6c60d4be82d25a49232/.travis.yml)
- [Result on Travis CI](https://travis-ci.org/github/zdict/zdict/builds/364780102)
    - ![Result on Travis CI](/files/change-from-travis-ci-build-matrix-to-build-stages/result-on-travis-ci.jpg)
