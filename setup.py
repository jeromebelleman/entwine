#!/usr/bin/env python
# coding=utf-8

import os
from distutils.core import setup

delattr(os, 'link')

setup(
    name='{package}',
    version='{version}',
    author='Jerome Belleman',
    author_email='Jerome.Belleman@gmail.com',
    url='http://cern.ch/jbl',
    description={description},
    long_description={longdescription},
    scripts=['{package}'],
    py_modules = ['entwinelib'],
    data_files=[{manpage}],
)
