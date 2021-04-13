from os import path

import setuptools

setuptools.setup(
    name="example",
    version="1.7.0",
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
    package_dir={'example': 'example'},
    package_data={
        'example': ['example/resources/*'],
    },
    include_package_data=True,
    packages=setuptools.find_packages(exclude=("tests",)),
    python_requires=">=3.8",
    entry_points='''
        [console_scripts]
        hgex=example.entrypoint:cli
    ''',
    install_requires=[
        'click',
        'awslambdaric',
        'hypergrowth'
    ]
)
