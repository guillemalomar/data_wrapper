import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="data_wrapper-guillemalomar",
    version="0.0.1",
    install_requires=requirements,
    author="Guillem Alomar",
    author_email="alomarguillem@hotmail.com",
    description="A library to make use of a database in a transparent and simple way",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guillemalomar/data_wrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
