from setuptools import setup

long_description = open('README.md').read()
VERSION = open('VERSION').read().strip()

setup(
    name = 'smugapi',
    version = VERSION,
    description = 'helpful api endpoints for smug',
    long_description = long_description,
    url = 'https://github.com/nod/smugapi',
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        ],
    entry_points = { 'console_scripts': [ 'smugapi=smugapi.cli.main:cli'] },
    packages=["smugapi"],
    package_dir={'': 'src'},
    python_requires='>=3.6',
    install_requires=[
        'click',
        'databag>=1.4',
        'humanize',
        'markdown2',
        'pngcanvas',
        'requests',
        'tornado',
        'tornroutes',
        'webpreview',
        ],
    )

