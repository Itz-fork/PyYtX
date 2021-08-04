# Copyright (c) 2021 Itz-fork
# Part of PyYtX Project

import os
from setuptools import setup, find_packages

# Allow Exec. from any path (Credits: mega.py)
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# Getting the requirements
with open('requirements.txt') as req:
    reques = req.read().splitlines()


setup(name='PyYtX',
version='0.3',
description='A Simple Python Program to Get Best Possible Thumbnail Urls From a Youtube Video Link',
url='https://github.com/Itz-fork/PyYtX',
author='Itz-fork',
author_email='itz-fork@users.noreply.github.com',
license='MIT',
packages=find_packages(),
download_url="https://github.com/Itz-fork/PyYtX/archive/refs/tags/v0.3.tar.gz",
keywords=['python', 'youtube', 'PyYtX'],
install_requires=reques,
classifiers=[
    'Development Status :: 4 - Beta',
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
