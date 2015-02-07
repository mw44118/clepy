import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

dependencies = [
        'decorator >= 3.0',
        'nose',
        'mock'
    ]

# If the python version is lower than 2.6, I need to add multiprocessing
# to the list of dependencies.

if sys.version_info < (2, 6, 0, '', 0):
    dependencies.append('multiprocessing')

setup(
    name="clepy",
    version="0.3.23",
    packages=["clepy"],
    install_requires=dependencies,
    url="http://code.google.com/p/clepy",
    license="MIT License",
    description="utilities from the Cleveland Python user group",
    maintainer="W. Matthew Wilson",
    maintainer_email="matt@216software.com",
    use_2to3=True,
)
