import os
import sys
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), "literals", "__version__.py")) as version_file:
    exec(version_file.read()) # pylint: disable=W0122

_INSTALL_REQUIRES = []

setup(name="literals",
      classifiers = [
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          ],
      description="Utility package for creating conditional/version dependent constants",
      license="BSD3",
      author="Infinidat Ltd.",
      author_email="info@infinidat.com",
      version=__version__, # pylint: disable=E0602
      packages=find_packages(exclude=["tests"]),

      url="https://github.com/infinidat/literals",

      install_requires=_INSTALL_REQUIRES,
      scripts=[],
      namespace_packages=[]
      )
