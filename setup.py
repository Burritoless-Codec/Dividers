from setuptools import setup, find_packages
import os

VERSION = '1'
DESCRIPTION = 'Creating dividers (divs) for CLI or output files'

# Setting up
setup(
    name="Dividers",
    version=VERSION,
    author="Burritoless Codec",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'dividers', 'cli', 'output'],
    classifiers=[
        "Development Status :: 1 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
