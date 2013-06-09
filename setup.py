#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='python-wordpress-api',
      version='0.1',
      description='WordPress JSON/XML-RPC API Integration Library',
      author='Max Cutler',
      author_email='max@maxcutler.com',
      url='https://github.com/maxcutler/python-wordpress-api/',
      packages=['python-wordpress-api'],
      license='BSD',
      test_suite='nose.collector',
      classifiers=[
          'Programming Language :: Python',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Environment :: Console',
          'Environment :: Web Environment',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Internet :: WWW/HTTP :: Site Management',
          'Topic :: Utilities',
          'Natural Language :: English',
      ],
      include_package_data=True,
      long_description=open('README.rst').read(),
)
