#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
setup.py

Created by Stephan Hügel on 2011-03-04
"""

from setuptools import setup, find_packages

setup(
    name='Circles',
    version='0.1',
    description='Draw correctly-projected circles on a Basemap plot',
    author='Stephan Hügel',
    author_email='urschrei@gmail.com',
    license='MIT',
    url='https://github.com/urschrei/circles',
    download_url='https://github.com/urschrei/circles/tarball/v0.1',
    keywords=['basemap'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=find_packages(),
    install_requires=['numpy'],
    long_description="""\
A convenience method for calculating circular coordinates for a given centre and radius. 
These can be plotted on a Basemap instance, and will conform to its selected projection 
"""
)
