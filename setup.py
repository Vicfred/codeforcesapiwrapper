# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

_here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(_here, 'README.rst'), encoding='utf-8') as f:
    README = f.read()

with open(os.path.join(_here, 'LICENSE'), encoding='utf-8') as f:
    LICENSE = f.read()

version = {}
with open(os.path.join(_here, 'somepackage', 'version.py')) as f:
    exec(f.read(), version)

setup(
    name='codeforces',
    version='0.1.0',
    description='Simple wrapper for the codeforces API',
    long_description=README,
    author='Vicfred',
    author_email='me@vicfred.dev',
    url='vicfred.dev',
    license=LICENSE,
    packages=find_packages(exclude=('tests', 'docs'))
)
