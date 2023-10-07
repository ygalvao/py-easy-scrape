#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='py-easy-scrape',
    version='0.1.5',
    url='https://github.com/ygalvao/py-easy-scrape',
    author='Yuri Henrique Galvao',
    author_email='yuri@galvao.ca',
    description='A useful package for web scraping with Selenium',
    packages=find_packages(),
    install_requires=[
        'selenium',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
