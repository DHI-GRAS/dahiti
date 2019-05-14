from setuptools import setup, find_packages
import versioneer

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='dahiti',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Download water level data from http://dahiti.dgfi.tum.de',
    author='Jonas Solvsteen',
    author_email='josl@dhigroup.com',
    url='https://github.com/DHI-GRAS/dahiti',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    install_requires=[
        'requests'
    ]
)
