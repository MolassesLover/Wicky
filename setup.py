#!/usr/bin/python3

#region Modules

from Cython.Build import cythonize
from pathlib import Path
from setuptools import setup, Extension

#endregion

#region Variables

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

#endregion

setup(
    name = "Wicky",
    version = '0.1.1',
    description = "A libre tool for Wicked Engine development",
    author = "Maeve Garside",
    author_email = "60114762+MolassesLover@users.noreply.github.com",
    url = 'https://github.com/MolassesLover/Wicky',
    license = 'MIT',
    packages = ['wicky'],
    ext_modules=[Extension('Source/Wicky.py', ['Wicky.c'])],
    Install_requires=[
        'colorama',
        'pyyaml'
    ]
)