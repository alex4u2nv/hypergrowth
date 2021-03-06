import setuptools

with open("Readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hypergrowth",
    version="1.1.0",
    author="Alexander Mahabir",
    author_email="alex.mahabir@gmail.com",
    description="A Skeleton Project with some handy libraries, helpers, and patterns to build on",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alex4u2nv/hypergrowth",
    project_urls={
        "Bug Tracker": "https://github.com/alex4u2nv/hypergrowth/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={'hypergrowth': 'hypergrowth', 'example': 'example'},
    package_data={
        'example': ['example/resources/*'],
    },
    include_package_data=True,
    packages=setuptools.find_packages(exclude=("tests",)),
    python_requires=">=3.8",
    py_modules=['example_shared.interface'],
    entry_points='''
        [console_scripts]
        hgex=example.entrypoint:cli
    ''',
    install_requires=[
        'click'
    ]
)
