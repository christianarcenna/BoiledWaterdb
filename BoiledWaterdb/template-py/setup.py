try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

config = {
    'description': 'boiledwaterdb',
    'author': 'Joshua Pineda',
    'author_email': 'joshua.pineda1@uoit.net',
    'version': '0.0.1',
    'packages': find_packages(),
    'name': 'boiledwaterdb'
}

setup(**config)
