import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="seedling",
    version="0.0.1",
    author="Shane Drabing",
    author_email="shane.drabing@gmail.com",
    packages=setuptools.find_packages(),
    url="https://github.com/shanedrabing/seedling",
    description="Quick and easy molecular phylogenies.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    data_files=[
        ("", ["LICENSE"])
    ],
    install_requires=[
        "requests"
    ]
)
