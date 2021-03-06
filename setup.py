#!/usr/bin/env python
import sys
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

version = sys.version_info[:2]
if version < (3, 4):
    print('iamfast requires Python version 3.4 or later' +
          ' ({}.{} detected).'.format(*version))
    sys.exit(-1)

setup(name='iamfast',
      version='0.1.0',
      description='',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Ian Mckay',
      author_email='iamfast@ian.mn',
      url='https://github.com/iann0036/iamfast-python',
      license='MIT',
      packages=find_packages(exclude=['tests', 'tests.*']),
      zip_safe=True,
      install_requires=[],
      entry_points={'console_scripts': [
          'iamfast=iamfast.main:main'
      ]}
)