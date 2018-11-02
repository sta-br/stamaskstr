import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stamaskstr",
    version="0.0.2",
    author="Marco Ostaska",
    author_email="marcoan@ymail.com",
    description="string masking",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sta-br/stamaskstr",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)