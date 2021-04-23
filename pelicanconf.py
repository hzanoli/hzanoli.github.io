#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Henrique J C Zanoli'
SITENAME = 'hzanoli.dev'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = 'en'

# Short about
AUTHOR_HEADLINE = 'Python, C++, physics, data science  <div class="bg-primary text-accent">& more</div>'
AUTHOR_SUMMARY = "I am an analytical-driven person that likes to understand reality and its patterns. " \
                 "What it is - a solid mathematical formulation, a clean piece of " \
                 "code, a modern graphic design or a picture of how nature behaves - depends on the day."

FOOTER = '<span class="text-muted">Proudly </span>🏳‍🌈<span class="text-muted">made with ' \
         '<a class="text-muted" href="https://docs.getpelican.com">Pelican</a></span> and ' \
         '<a class="text-muted" href="https://getbootstrap.com">Bootstrap</a>. Check it on ' \
         '<a class="text-muted" href="https://github.com/hzanoli/hzanoli.github.io">Github</a>!'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('ALICE Collaboration', 'https://alice-collaboration.web.cern.ch/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/')
         )
# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

THEME = 'themes/quadrado'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
