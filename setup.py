# -*- coding: utf-8 -*-

"""
United interface to different USBTMC (or "SCPI")
intstrument implementations in Python.

This package facilitates using USBTMC devices with Python
via quite some different ways of accessing them ("backends").
This allows you to write very platform independent code.

Go to https://github.com/pklaus/universal_usbtmc for more information.

Copyright (c) 2015, Philipp Klaus. All rights reserved.
"""

from setuptools import setup

desc  = __doc__.split('\n\n')[0]
ldesc = '\n\n'.join(__doc__.split('\n\n')[1:-1])

setup(name='universal_usbtmc',
      version = '0.3-dev',
      description = desc,
      long_description = ldesc,
      author = 'Philipp Klaus',
      author_email = 'philipp.l.klaus@web.de',
      url = 'https://github.com/pklaus/universal_usbtmc',
      license = 'GPL',
      packages = ['universal_usbtmc', 'universal_usbtmc.backends'],
      entry_points = {
        'console_scripts': [
            'usbtmc-shell = universal_usbtmc.usbtmc_shell:main',
        ],
      },
      zip_safe = True,
      platforms = 'any',
      keywords = 'USBTMC',
      classifiers = [
          'Development Status :: 4 - Beta',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: System :: Monitoring',
          'Topic :: System :: Logging',
      ]
)


