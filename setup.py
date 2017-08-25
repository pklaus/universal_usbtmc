# -*- coding: utf-8 -*-

"""
Copyright (c) 2015-2017, Philipp Klaus. All rights reserved.
"""

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

try:
    import pypandoc
    # for PyPI: Removing images with relative paths and their descriptions:
    import re
    LDESC = open('README.md', 'r').read()
    matches = re.findall(r'\n\n(.*(\n.+)*:\n\n!\[.*\]\((.*\))(\n\n)?)', LDESC)
    for match in matches:
        text, _, link, _ = match
        if text.startswith('http://'): continue
        LDESC = LDESC.replace(text, '')
    # Converting to rst
    LDESC = pypandoc.convert(LDESC, 'rst', format='md')
except (ImportError, IOError, RuntimeError) as e:
    print("Could not create long description:")
    print(str(e))
    LDESC = ''

setup(name='universal_usbtmc',
      version = '0.3-dev',
      description = "Universal Python Interface For Different USBTMC Backends",
      long_description = LDESC,
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
      include_package_data = True,
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


