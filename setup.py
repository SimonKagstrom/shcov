######################################################################
##
## Copyright (C) 2008,  Simon Kagstrom
##
## Filename:      setup.py
## Author:        Simon Kagstrom <simon.kagstrom@gmail.se>
## Description:   Installation script (from Dissy)
##
## $Id:$
##
######################################################################
import sys

sys.path.append(".")
from shcov import config

from distutils.core import setup

setup(name='%s' % (config.PROGRAM_NAME).lower(),
      version='%s' % (config.PROGRAM_VERSION),
      description="A gcov and lcov coverage test tool for bourne shell / bash scripts",
      author="Simon Kagstrom",
      url="%s" % (config.PROGRAM_URL),
      author_email="simon.kagstrom@gmail.se",

      packages = ['shcov'],
      scripts = ['scripts/shcov', 'scripts/shlcov'],

      data_files = [('share/%s/data' % (config.PROGRAM_NAME.lower()),
		     ['data/amber.png', 'data/gcov.css', 'data/ruby.png',
                      'data/emerald.png', 'data/glass.png', 'data/snow.png', ]),
		    ('share/doc/%s/' % (config.PROGRAM_NAME.lower()), ['README']),
		    ('share/doc/%s/' % (config.PROGRAM_NAME.lower()), ['COPYING']),
                    ('share/man/man1/', ['shcov.1', 'shlcov.1']),
                    ],
      )
