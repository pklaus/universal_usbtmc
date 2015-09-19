# -*- coding: utf-8 -*-

"""
Copyright (c) 2015, Philipp Klaus. All rights reserved.

License: GPLv3
"""

from distutils.core import setup

setup(name='universal_usbtmc',
      version = '0.3.0',
      description = 'United interface to different USBTMC implementations in Python',
      long_description = '',
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
          'License :: OSI Approved :: GPL License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: System :: Monitoring',
          'Topic :: System :: Logging',
      ]
)


