import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

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
    # install_requires=[""],
    entry_points={
        "console_scripts": [
            "photoley=photoley.__main__:main",
        ]
    },
)