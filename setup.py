# Copyright (c) 2021 Itz-fork
# Part of PyYtX Project

import os
from setuptools import setup, find_packages

# Allow Exec. from any path (Credits: mega.py)
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# Getting the requirements
if os.path.isfile('requirements.txt'):
  with open('requirements.txt') as req:
    reques = req.read().splitlines()
else:
  reques = [
    'wget'
  ]

# Getting the long description
if os.path.isfile('README.md'):
  with open(('README.md'), encoding='utf-8') as readmeh:
    big_description = readmeh.read()
else:
  big_description = "PyYtX - A Simple Python Library to Get Details About a Youtube Video."


setup(name='PyYtX',
version='0.6.5',
description='A Simple Python Program to Get Best Possible Thumbnail Urls From a Youtube Video Link',
url='https://github.com/Itz-fork/PyYtX',
author='Itz-fork',
author_email='itz-fork@users.noreply.github.com',
license='MIT',
packages=find_packages(),
download_url="https://github.com/Itz-fork/PyYtX/archive/refs/tags/v0.6.5.tar.gz",
keywords=['python', 'youtube', 'PyYtX'],
long_description=big_description,
long_description_content_type='text/markdown',
install_requires=reques,
classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.9',
  ],
)
