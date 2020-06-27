# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="module_armando", # the name that you will install via pip
    version="1.0",
    author="Armando Sepulveda",
    author_email="sepulveda.armando97@gmail.com",
    description="Practice on creating modules and packages",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/ArmandoSep/Module-Packaging",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)