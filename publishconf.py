#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://blog.fkz.tw'
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True

DISQUS_SITENAME = "fkz"
GOOGLE_ANALYTICS = "UA-45367183-2"
GOOGLE_ANALYTICS_DOMAIN = "auto"
