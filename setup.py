__author__ = "Shane Drabing"
__license__ = "MIT"
__email__ = "shane.drabing@gmail.com"


# IMPORTS


import sys
import subprocess
import setuptools
from setuptools.command.install import install


# CONSTANTS


HERE = sys.path[0]
WINDOWS = str(sys.platform) in ("win32", "cygwin")


# CLASSES


class Install(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        if WINDOWS:
            subprocess.run(["call", ".\src\compile.bat"], cwd=HERE, shell=True)
        else:
            subprocess.run(["sh", "./src/compile.sh"], cwd=HERE)


# SCRIPT


setuptools.setup(
    name="seedling",
    version="0.0.1",
    author="Shane Drabing",
    author_email="shane.drabing@gmail.com",
    packages=setuptools.find_packages(),
    url="https://github.com/shanedrabing/seedling",
    description="Quick and easy molecular phylogenies.",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    data_files=[
        ("", ["LICENSE"])
    ],
    install_requires=[
        "requests"
    ],
    cmdclass={
        "install": Install,
    },
)
