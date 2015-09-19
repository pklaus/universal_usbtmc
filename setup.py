# -*- coding: utf-8 -*-

"""
Universal Python Interface For Different USBTMC Backends.

Github: https://github.com/pklaus/universal_usbtmc

Copyright (c) 2015, Philipp Klaus. All rights reserved.
"""

from setuptools import setup

desc  = __doc__.split('\n\n')[0]
ldesc = '\n\n'.join(__doc__.split('\n\n')[1:-1])
try:
    import pypandoc
    tmp_txt = open('README.md', 'r').read()
    ldesc += '\n\n' + pypandoc.convert(tmp_txt, 'rst', format='md')
except (ImportError, IOError, RuntimeError):
    pass

setup(name='universal_usbtmc',
      version = '0.3.3',
      description = desc,
      long_description = ldesc,
      author = 'Philipp Klaus',
      author_email = 'philipp.l.klaus@web.de',
      url = 'https://github.com/pklaus/universal_usbtmc',
      license = 'GPL',
      packages = ['universal_usbtmc', 'universal_usbtmc.backends'],
      entry_points = {
        'console_scripts': [
            'usbtmc-shell = universal_usbtmc.shell:main',
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


