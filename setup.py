# -*- coding: utf-8 -*-

"""
Copyright (c) 2015, Philipp Klaus. All rights reserved.

License: GPLv3
"""

from distutils.core import setup

setup(name='universal_usbtmc',
      version = '0.2.0',
      description = 'United interface to different USBTMC implementations in Python',
      long_description = '',
      author = 'Philipp Klaus',
      author_email = 'philipp.l.klaus@web.de',
      url = '',
      license = 'GPL',
      packages = ['universal_usbtmc', 'universal_usbtmc.backends'],
      scripts = ['scripts/usbtmc-shell',],
      zip_safe = True,
      platforms = 'any',
      keywords = 'USBTMC',
      classifiers = [
          'Development Status :: 4 - Beta',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: GPL License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Topic :: System :: Monitoring',
          'Topic :: System :: Logging',
      ]
)


