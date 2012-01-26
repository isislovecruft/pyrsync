#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys

if sys.version_info < (2, 2):
    raise RuntimeError('You need python 2.2 for this module.')

__author__ = "Isis Lovecruft <isis@patternsinthevoid.net>"
__date__ = "24 Jan 2012"
__version__ = (0, 1, 0)
__license__ = "MIT"

import collections
import hashlib

__all__ = [ 'collections',
            'hashlib', ]
