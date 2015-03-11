try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Keep records of Saltybet matchs',
    'author': 'Eric Stinger',
    'url': 'URL to get it at',
    'download url': 'Where to download it at',
    'author_email': 'emstin1@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['CompuSalt'],
    'scripts': [],
    'name': 'Compusalt'
}

setup(**config)