#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

# Testing dependencies
testing_extras = []

setup(
    name='wagtailstreamfieldforms',
    version='0.1.0',
    description=
    'A module for Wagtail that provides functionality of polls and surveys.',
    author='Hannes Lohmander',
    author_email='hannes@aldowntown.com',
    url='https://github.com/aldowntown/wagtailstreamfieldforms',
    packages=find_packages(),
    include_package_data=True,
    license='BSD',
    long_description=
    'See https://github.com/torchbox/wagtailsurveys for details',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
    install_requires=[
        'Django>=1.8.1',
        'wagtail>=1.13',
        'Unidecode>=0.04.14',
    ],
    extras_require={
        'testing': testing_extras,
    },
    zip_safe=False, )
