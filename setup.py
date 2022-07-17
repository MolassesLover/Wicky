from setuptools import setup
from Cython.Build import cythonize

setup(
    name = "Wicky",
    version = '0.1',
    description = "A libre tool for Wicked Engine development",
    author = "Maeve Garside",
    author_email = "60114762+MolassesLover@users.noreply.github.com",
    url = 'https://github.com/MolassesLover/Wicky',
    license = 'MIT',
    packages = ['wicky'],
    ext_modules = cythonize("Source/Wicky.py"),
    Install_requires=[
        'colorama'
    ]
)