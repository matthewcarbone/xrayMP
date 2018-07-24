#!/usr/bin/env python3

DESCRIPTION = "Pull and process XANES spectra from the Materials Project"
LONG_DESCRIPTION = """See description."""

VERSION = '0.0.1'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

to_install = []

try:
    import numpy
except ImportError:
    to_install.append('numpy')


if __name__ == '__main__':

    setup(name='xrayMP',
          author='Matthew Carbone',
          author_email='x94carbone@gmail.com',
          maintainer='Matthew Carbone',
          maintainer_email='x94carbone@gmail.com',
          description=DESCRIPTION,
          long_description=LONG_DESCRIPTION,
          license='BSD-3-Clause',
          version=VERSION,
          download_url='https://github.com/x94carbone/xray-mp/',
          install_requires=to_install,
          packages=['xrayMP'],
          )
