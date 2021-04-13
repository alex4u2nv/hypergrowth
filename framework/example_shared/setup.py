from os import path

import setuptools

this_directory = path.abspath(path.dirname(__file__))

setuptools.setup(
    name="example_shared",
    version="1.6.4",
    author="Alexander Mahabir",
    author_email="alex.mahabir@gmail.com",
    description="A Skeleton Project with some handy libraries, helpers, and patterns to build on",
    url="https://github.com/alex4u2nv/hypergrowth",
    project_urls={
        "Bug Tracker": "https://github.com/alex4u2nv/hypergrowth/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(exclude=("tests",)),
    python_requires=">=3.8",
    install_requires=[
        'click'
    ]
)
