try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Number Formatter',
    'author': 'Frank Bardelli',
    'url': '',
    'download_url': '',
    'author_email': 'frank.bardelli@mediamath.com',
    'version': '0.1',
    'install_requires': [''],
    'packages': ['number_format'],
    'scripts': [],
    'name': 'number_format'
}

