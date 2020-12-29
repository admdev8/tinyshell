from setuptools import find_packages
from setuptools import setup

setup(
    name="tinyshell",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "docopt==0.6.2",
        "requests==2.20.0",
    ],
)
