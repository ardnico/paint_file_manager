import io
import re

library_name = "paint_file_manager"

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requires = [pkg.strip() for pkg in open('requirements.txt', 'r').readlines()]

version = ''
with open(f'{library_name}/__init__.py', 'r') as fd:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', fd.read(), re.MULTILINE).group(1)
if not version:
    raise RuntimeError('Cannot find version information')


setup(
    name=library_name,
    packages=[library_name],
    version=version,
    description='',
    long_description=io.open('README.md', mode='r', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    author='ardnico',
    author_email='leaf.sun2@gmail.com',
    install_requires=requires,
    url='https://github.com/ardnico/',
    download_url=f'https://github.com/ardnico/{library_name}/releases',
    keywords=[''],
        classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)