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
                return line.split()[-1].strip().strip("'").strip('"')


version = read_version('swagger_ui_bundle')

install_requires = [
    'Jinja2>=2.0',
]


def readme():
    try:
        return open('README.rst', encoding='utf-8').read()
    except TypeError:
        return open('README.rst').read()


class PyTest(TestCommand):

    """Command to run unit tests after in-place build."""

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = [
            '-sv',
            '--pep8',
            '--flake8',
        ]
        self.test_suite = True

    def run_tests(self):
        # Importing here, `cause outside the eggs aren't loaded.
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='swagger_ui_bundle',
    packages=find_packages(),
    version=version,
    description='swagger_ui_bundle - swagger-ui files in a pip package',
    long_description=readme(),
    author='Daniel Grossmann-Kavanagh, Bartolomé Sánchez Salado',
    url='https://github.com/bartsanchez/swagger_ui_bundle',
    keywords='swagger-ui',
    license='Apache License Version 2.0',
    setup_requires=['pytest-runner', 'flake8'],
    install_requires=install_requires,
    tests_require=[
        "pytest",
        "pytest-pep8",
        "pytest-flake8",
        "tox",
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    include_package_data=True,  # needed to include swagger-ui (see MANIFEST.in)
)
