from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import sys

import codewatch

here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.md', 'CHANGES.txt')

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='codewatch',
    version=codewatch.__version__,
    url='http://github.com/peachjean/codewatch/',
    license='Apache Software License',
    author='Jared Bunting',
    tests_require=['pytest'],
    install_requires=['GitPython==0.1.7',
                      'requests==2.4.3',
                      ],
    cmdclass={'test': PyTest},
    author_email='jared.bunting@peachjean.com',
    description='A utility for tracking code analysis metrics directly in the git repository.',
    long_description=long_description,
    packages=['codewatch'],
    include_package_data=True,
    platforms='any',
    test_suite='test.test_codewatch',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    extras_require={
        'testing': ['pytest'],
        }
)
