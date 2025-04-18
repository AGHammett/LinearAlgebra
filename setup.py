from setuptools import setup, find_packages

setup(
    name="alexhlinalg",  
    version="0.1",         
    packages=find_packages(),  
    install_requires=[ 
        "numpy",
        "scipy",
        "matplotlib.pyplot"
    ],
    author="Alex Hammett",
    author_email="aghammett00@gmail.com",
    description="Some linalg function I found helpful",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AGHammett/linearalgebra",
)
