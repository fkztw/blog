Title: TYPO3 CMS  
Date: 2014-03-03 12:32  
Author: fkz  
Category: Note  
Tags: PHP, Open Source, CMS, TYPO3  
Slug: typo3-cms  
Modified: 2015-10-26 15:10  
  
Introduction to [TYPO3](https://typo3.org/) by [Rüdiger Marwein](https://twitter.com/keinerweiss)  
  
---  
  
+ Why name [TYPO3](https://typo3.org/)?  
    + Because the author deleted the project unintentionally **TWICE**, so it called **TYPO3** .  
    + Developed by PHP.  
+ TYPO3 Association  
    + Enables developers to contribute  
    + Ensures stable release cycle  
    + Provides certification program  
    + Organizes community events  
        + TYPO3 conference  
        + T3BOARD  
        + Developer Day  
+ Open Source Community  
    + Strongest participation concentrated in Germany, Switzerland, Austria  
    + Global approach  
        + software available in 50+ languages  
+ Content Management System (CMS) of TYPO3  
    + To separate content from layout  
    + 6000+ extensions in the repo  
+ Skill-levels for TYPO3 CMS  
    + Integrator  
        + Setup, configuration management  
    + Extension Developer  
        + Create extensions by using the framework  
    + Editor  
        + Create and edit content  
+ TypoScript  
    + Users Can change configuration without write any PHP code.  
+ Enterprise CMS  
    + Unlimited users & groups  
    + Multiple clients in one system  
    + Multiple domains manageable  
    + Flexible configuration, even for core features.(by TypoScript)  
    + Extensibility  
    + Inexpensive upgrade & migration  
        + use symbolic link  
    + Release schedule  
    + Security-team & -workflow for core + extensions  
        + If you find a security hole, you can email the Security team, the team will deal with it.  
        + A big issue will be solved in 24 hours as soon as possible and release an update.  
+ Core Features  
    + Enable / Disable pages or content  
    + Time based hide / show  
    + Global & local content  
        + Referencing content  
    + Many content element types  
        + Text / image combinations  
        + Menus & link lists  
        + Multi-column content  
    + Media management  
    + Versioning  
    + HMAC-based security  
    + Extension concept  
    + Drag & Drop  
    + Access / feature restrictions  
    + Protected areas via frontend login  
    + High-traffic - intensive caching  
        + File system, Database, memory, NoSQL  
    + Output fully configurable  
        + Website, PDF, Image, XML Interface, ...  
        + Single source publishing  
    + DB-record relations  
        + 1:1, 1:n, n:m  
    + Valid HTML5 output  
+ Features via extensions  
    + Press / News releases  
    + Newsletter  
    + Search engine optimization  
    + Image galleries  
    + Readable URLs  
    + Address database  
    + Forum  
    + Frontend user registration  
    + Mail forms  
    + FAQ  
    + Online-Shop  
    + Google Maps  
    + Search  
    + Web Analytics  
    + Developer support  
        + Extension Builder  
            + You can use UML diagram to generate Extensions  
        + Protocols  
        + Libraries  
        + PHP unit integration  
+ Current Work  
    + Code cleanup with version 4.7 (4.2012)  
        + Many extensions known to not work without rework.  
    + Rebased for version 6.0 (11.2012)  
        + Partly breaks backward compatibility  
    + Why?  
        + For code refactoring  
        + Removed tons of legacy code  
        + Cleanup outdated file structure, class and function naming  
        + [PSR-0](http://www.sitepoint.com/autoloading-and-the-psr-0-standard/) conformity  
        + Replace prototype with jQuery  
        + Use new "Extbase" framework in backend as well  
        + Final goal: merge in Flow framework -> product interoperability  
        + Backend layout / usability enhancements  
  
---  
  
## Appendix  
  
+ [gource - software version control visualization](https://code.google.com/p/gource/)  
  
  
