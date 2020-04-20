#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Installation:
    pip install git+https://github.com/Erotemic/ubelt.git

Developing:
    git clone https://github.com/Erotemic/ubelt.git
    pip install -e ubelt
"""
from setuptools import find_packages
from setuptools import setup


def parse_description():
    """
    Parse the description in the README file
    """
    from os.path import dirname, join, exists
    readme_fpath = join(dirname(__file__), 'README.md')
    # This breaks on pip install, so check that it exists.
    if exists(readme_fpath):
        with open(readme_fpath, 'r') as f:
            text = f.read()
        return text
    return ''


NAME = 'aptsources-cleanup'
# VERSION = parse_version('aptsources_cleanup/__init__.py')


if __name__ == '__main__':
    setup(
        name=NAME,
        # version=VERSION,
        long_description=parse_description(),
        long_description_content_type='text/markdown',
        install_requires=[
            'regex',
        ],
        extras_require={
            'dev': [
                'gitpython',
            ],
        },
        packages=find_packages('.'),
        entry_points={
            # the console_scripts entry point creates the xdoctest executable
            'console_scripts': [
                'aptsources-cleanup = aptsources_cleanup.__main__:main'
            ]
        },
        classifiers=[
            # List of classifiers available at:
            # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        ],
    )
