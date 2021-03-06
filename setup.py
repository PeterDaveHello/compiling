#!/usr/bin/env python
from setuptools import setup, find_packages
import codecs
import os
import re
import compiling

here = os.path.abspath(os.path.dirname(__file__))


def path(*path):
    return os.path.join(here, *path)

with codecs.open(path('README.rst'), encoding='utf-8') as f:
    long_description = f.read()

with codecs.open(path('requirements.txt'), encoding='utf-8') as f:
    requirement = f.read()

setup(
    name='compiling',
    version=compiling.__version__,
    description='Compiling message generator',
    long_description=long_description,
    url='https://github.com/hacking-thursday/compiling',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    keywords='compile',
    packages=find_packages(exclude=['docs', 'test']),
    install_requires=requirement,
    package_data={
        'compiling': ['data/*.yml'],
    },
    data_files=[
    ],
    entry_points={
        'console_scripts': [
            'compiling = compiling.console:main',
        ],
    },
)
