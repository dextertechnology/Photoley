import os.path
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

setup(
    name="photoley",
    version="1.0.0",
    description="Using unsplash, fetch random wallpaper with specific size and category",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/dextertechnology/Photoley",
    author="Dexter",
    author_email="dipipandey1@gmail.com",
    license="LGPL-3.0",
    classifiers=[
        "License :: OSI Approved :: GNU LGPL 3.0",
        "Programming Language :: Python :: 3.8.0"
    ],
    packages=["photoley"],
    include_package_data=True,
    # install_requires=[""],,
    data_files=[('photoley/config.ini')],
    entry_points={
        "console_scripts": [
            "photoley=photoley.__main__:main",
        ]
    },
)
