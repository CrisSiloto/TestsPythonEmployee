import setuptools
import glob
import os
import shutil

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("VERSION", "r") as fh:
    VERSION = fh.read().strip('\r\n ')

setuptools.setup(
    name="datamodel",
    version=VERSION,
    author="Cristiane",
    author_email="csiloto@sorint.it",
    description="Creates a list of employees for each department",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://gitlab.dev.bancaimi.com/hdb/bbg_dl_retriever",
    packages=setuptools.find_packages(),
    package_data={'datamodel': ['template/*.txt', 'conf/conf.properties']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",

    ]
)