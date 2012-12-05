#!/usr/bin/env python

from os.path import exists
try:
    # Use setup() from setuptools(/distribute) if available
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='pyper',
      version='0.0.1',
      author='James Sofra',
      author_email='james.sofra@gmail.com',
      packages=['pyper'],
      scripts=[],
      url='https://github.com/jsofra/pyper',
      license='',
      description='Immutable Persistent data structures for Python',
      long_description=open('README.md').read() if exists("README.md") else "",
      install_requires=['clojure-py'],
)
