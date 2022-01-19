import setuptools
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="teamapt-monnify", # Replace with your own username
    version="1.1.1",
    author="Samson Ilemobayo",
    author_email="ilemobayosamson@gmail.com",
    description="TeamApt Monnify Python Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/samkayz/teamapt-monnify.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    
    ],
    python_requires='>=3.x',
    install_requires=[
        "requests",
    ],
)