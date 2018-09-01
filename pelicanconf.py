#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Basic settings
AUTHOR = u'm157q'
SITENAME = u'Just for noting'
TIMEZONE = 'Asia/Taipei'
DEFAULT_LANG = u'zh'
DEFAULT_PAGINATION = 10
THEME = 'themes/plumage'
USE_FOLDER_AS_CATEGORY = False
DISPLAY_CATEGORIES_ON_MENU = False
SUMMARY_MAX_LENGTH = 5

# Directories for Pelican processing
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['posts']
ARTICLE_EXCLUDES = ['drafts']

# URLs and Paths
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = TAG_URL + 'index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = CATEGORY_URL + 'index.html'

TAGS_SAVE_AS = 'tags/index.html'
CATEGORIES_SAVE_AS = 'categories/index.html'
ARCHIVES_SAVE_AS = 'archives/index.html'

STATIC_PATHS = [
    'files',
    'extra/favicon.ico',
    'extra/CNAME',
    'extra/robots.txt',
]

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'},
}

MENUITEMS = [
    # ('home', '/index'),
    ('Categories', '/categories'),
    ('Archives', '/archives'),
    ('Tags', '/tags'),
    # ('search', 'search'),
    # ('authors', 'authors'),
    # ('about', 'about'),
]

DIRECT_TEMPLATES = (
    'index',
    'tags',
    'categories',
    'archives',
    'search',
    # 'authors',
    # 'about',
)

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
)

# Social widget
GITHUB_USERNAME = 'M157q'
TWITTER_USERNAME = 'M157q'

SOCIAL = (
    ('GitHub', 'https://github.com/{}'.format(GITHUB_USERNAME)),
    ('Twitter', 'https://twitter.com/{}'.format(TWITTER_USERNAME)),
)

# Debug
CACHE_PATH = 'cache'
CACHE_CONTENT = True
LOAD_CONTENT_CACHE = True
GZIP_CACHE = True
RELATIVE_URLS = True

# Feed

# atom feed
FEED_ATOM = 'feeds/atom.xml'
CATEGORY_FEED_ATOM = 'feeds/category.%s.atom.xml'
AUTHOR_FEED_ATOM = 'feeds/author.%s.atom.xml'
TRANSLATION_FEED_ATOM = 'feeds/translation.%s.atom.xml'
TAG_FEED_ATOM = 'feeds/tag.%s.atom.xml'
FEED_ALL_ATOM = 'feeds/all.feed.atom.xml'

# rss feed
FEED_RSS = 'feeds/rss.xml'
CATEGORY_FEED_RSS = 'feeds/category.%s.rss.xml'
AUTHOR_FEED_RSS = 'feeds/author.%s.rss.xml'
TRANSLATION_FEED_RSS = 'feeds/translation.%s.rss.xml'
TAG_FEED_RSS = 'feeds/tag.%s.rss.xml'
FEED_ALL_RSS = 'feeds/all.feed.rss.xml'

# =============================================================================

# Donation section for article.html of my forked plumage theme
DONATIONS = {
    'btc': '3PpJHALguhGcA3An3GDyQb6x7yDwm9K38B',
    'eth': '0xf6414a9245f88484046448bb204111941b0d3fec',
    'ltc': 'LXrgT5JMW6vrua7BbkhHbeyip1HnXH6WKg',
    'paypalme': 'm157q',
    'opay-broadcaster-donate': '4E163AAE10E448A30DB244CF85527271',
}

# =============================================================================

# Plugins settings BEGIN

PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'neighbors',
    'pin_to_top',
    'related_posts',
    'render_math',
    'sitemap',
    'share_post',
    'tipue_search',
]

# related_posts
RELATED_POSTS_MAX = 5

# sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1.0,
        'indexes': 0.7,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'weekly',
        'pages': 'yearly'
    }
}

# render_math
MATH_JAX = {
    'color': 'blue',
    'linebreak_automatic': True,
    'responsive': True,
    'tex_extensions': ['color.js']
}

# tipue_search
TIPUE_SEARCH = True

# Plugins settings END
