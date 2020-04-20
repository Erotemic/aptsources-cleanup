#!/usr/bin/env python3
"""Returns the paths of the files behind the given modules."""
# -*- coding: utf-8
from __future__ import absolute_import, print_function
import sys
import operator
import importlib

try:
    from future_builtins import *  # NOQA
except ImportError:
    pass


print(
    *map(operator.attrgetter('__file__'),
         map(importlib.import_module, sys.argv[1:])),
    sep='\n')
