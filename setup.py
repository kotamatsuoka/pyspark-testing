#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import os

from setuptools import setup, find_packages

try:
    with open('README.rst') as f:
        readme = f.read()
except IOError:
    readme = ''


def _requires_from_file(filename):
    return open(filename).read().splitlines()


VERSION = '0.0.1'
email = os.environ['PYPI_EMAIL']

setup(
    name="pyspark-testing",
    version=VERSION,
    url='https://github.com/kotamatsuoka/pyspark-testing',
    project_urls={'Source Code': 'https://github.com/kotamatsuoka/pyspark-testing'},
    author='kmatsuoka',
    author_email=email,
    maintainer='kmatsuoka',
    maintainer_email=email,
    description='Testing Framework for PySpark',
    keywords='pyspark,test',
    long_description=readme,
    install_requires=_requires_from_file('requirements.txt'),
    license="MIT",
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
    ],
    packages=find_packages(exclude=('tests')),
    entry_points="",
    python_requires=">=3.6",
)
