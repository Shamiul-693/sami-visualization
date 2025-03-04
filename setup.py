from setuptools import setup, find_packages

setup(
    name="sami",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "matplotlib",
        "seaborn",
    ],
    author="Sami",
    description="A simple visualization package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
