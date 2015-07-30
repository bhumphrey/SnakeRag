#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Installation instructions and package metadata."""

from setuptools import setup

setup(
    name='SnakeRag',
    version='1.0dev0',
    author='Chris Lasher',
    author_email='chris.lasher@gmail.com',
    # third-party packages
    install_requires=[],
    extras_require={
        'dev': ['pytest'],
        'test': ['pytest'],
    },
    packages=['snakerag'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
    ],
    description="A package for ragging out.",
    long_description=open('README.rst', encoding='utf-8').read()
)
