# Reference: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

NAME = 'roatools'
DESCRIPTION = 'Tools for managing and using replays from Rivals of Aether'
AUTHOR = 'ContentsMayBeHot'
AUTHOR_EMAIL = None
URL = 'https://github.com/ContentsMayBeHot/roatools'
REQUIRES_PYTHON = '>=3.6.0'
REQUIRES_PACKAGES = [
    'keras'
]
VERSION = None
LICENSE = 'GPLv3'

setup(
    name=NAME,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL
    license=LICENSE
    python_requires=REQUIRES_PYTHON,
    url=URL,
    version=VERSION,
    packages=find_packages(exclude=('tests',)),
    install_requires = REQUIRES_PACKAGES
    include_package_data=True
)
