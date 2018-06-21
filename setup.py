#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import inspect
import os
import sys

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand

__location__ = os.path.join(os.getcwd(), os.path.dirname(inspect.getfile(inspect.currentframe())))


def read_version(package):
    with open(os.path.join(package, '__init__.py'), 'r') as fd:
        for line in fd:
            if line.startswith('__version__ = '):
                return line.split()[-1].strip().strip("'")


version = read_version('swagger-ui-bundle')

install_requires = [
    'Jinja2>=2.0',
]


def readme():
    try:
        return open('README.rst', encoding='utf-8').read()
    except TypeError:
        return open('README.rst').read()

setup(
    name='swagger_ui_bundle',
    packages=find_packages(),
    version=version,
    description='swagger_ui_bundle - swagger-ui files in a pip package',
    long_description=readme(),
    author='Daniel Grossmann-Kavanagh',
    url='https://github.com/dtkav/swagger-ui-bundle',
    keywords='swagger-ui',
    license='Apache License Version 2.0',
    setup_requires=['flake8'],
    install_requires=install_requires,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    include_package_data=True,  # needed to include swagger-ui (see MANIFEST.in)
)
