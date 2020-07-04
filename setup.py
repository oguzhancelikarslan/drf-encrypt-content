from setuptools import setup

from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    description=(
        'The package helps you encrypt your serialized data.'
    ),
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'cryptography>=2.9.2',
    ],
)
