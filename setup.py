#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
from sys import version

SETUPTOOLS = False

try:
    from setuptools import setup
    SETUPTOOLS = False
except ImportError:
    from distutils.core import setup

# Backwards compatibility with distutils prior to 2.2.3:
if version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None

# Utility function to read the README.md file from main directory, used for 
# the long_description.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='pyrsync',
      version='0.1.0',
      description='''A Python module which implements rsync with SHA256 hash.''',
      long_description=read('README.md'),
      author='Eric Pruitt, Isis Lovecruft',
      author_email='isis@patternsinthevoid.net',
      url='https://github.com/isislovecruft/pyrsync',
      py_modules=['pyrsync'],
      license=['MIT'],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Security :: Cryptography',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Archiving',
        'Topic :: System :: Archiving :: Backup',
        'Topic :: System :: Archiving :: Compression', ],
      packages=['pyrsync'],
      package_dir={'pyrsync': ''},
      package_data={'': ['README.md']},
      )
