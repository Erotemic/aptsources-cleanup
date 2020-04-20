#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup
from os.path import dirname, join, exists


def parse_description():
    """
    Parse the description in the README file
    """
    readme_fpath = join(dirname(__file__), 'README.md')
    # This breaks on pip install, so check that it exists.
    if exists(readme_fpath):
        with open(readme_fpath, 'r') as f:
            text = f.read()
        return text
    return ''


def parse_version(fpath):
    """
    Statically parse the version number from a python file
    """
    import ast
    if not exists(fpath):
        raise ValueError('fpath={!r} does not exist'.format(fpath))
    with open(fpath, 'r') as file_:
        sourcecode = file_.read()
    pt = ast.parse(sourcecode)
    class VersionVisitor(ast.NodeVisitor):
        def visit_Assign(self, node):
            for target in node.targets:
                if getattr(target, 'id', None) == '__version__':
                    self.version = node.value.s
    visitor = VersionVisitor()
    visitor.visit(pt)
    return visitor.version


NAME = 'aptsources-cleanup'
VERSION = parse_version('aptsources_cleanup/__init__.py')


if __name__ == '__main__':
    setup(
        name=NAME,
        version=VERSION,
        author='David Foerster',
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
            # the console_scripts entry point creates the aptsources-cleanup executable
            'console_scripts': [
                'aptsources-cleanup = aptsources_cleanup.__main__:main'
            ]
        },
        classifiers=[
            # List of classifiers available at:
            # https://pypi.python.org/pypi?%3Aaction=list_classifiers
        ],
    )
