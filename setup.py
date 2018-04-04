from setuptools import setup, find_packages
import versioneer

setup(
    name='dahiti',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Download water level data from http://dahiti.dgfi.tum.de',
    author='Jonas Solvsteen',
    author_email='josl@dhigroup.com',
    url='https://www.dhigroup.com',
    packages=find_packages(),
    install_requires=['requests'])
