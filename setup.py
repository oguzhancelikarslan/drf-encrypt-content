from setuptools import setup

with open('README.md', encoding="utf8") as f:
    long_description = f.read()

setup(
    description=(
        'The package helps you encrypt your serialized data.'
    ),
    long_description=long_description,
    long_description_content_type="test/markdown",
    install_requires=[
        'cryptography>=2.9.2',
    ],
)
