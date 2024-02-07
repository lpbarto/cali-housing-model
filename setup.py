from setuptools import find_packages, setup

setup(
    name='calimodelib',
    packages=find_packages(include=['calimodelib']),
    version='0.1.0',
    description='Cali housing model library',
    author='Me',
    install_requires=['torch==2.2.0'],
)