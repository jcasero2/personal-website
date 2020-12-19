"""
Insta485 python package configuration.

Andrew DeOrio <awdeorio@umich.edu>
"""

from setuptools import setup

setup(
    name='personalwebsite',
    version='0.1.0',
    packages=['personalwebsite'],
    include_package_data=True,
    install_requires=[
        'arrow',
        'bs4',
        'Flask',
        'html5validator',
        'nodeenv',
        'pycodestyle',
        'pydocstyle',
        'pylint',
        'pytest',
        'requests',
        'selenium',
        'psycopg2-binary',
    ],
    python_requires='>=3.6',
)
