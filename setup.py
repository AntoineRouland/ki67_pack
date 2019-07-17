import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ki67segmentation",
    version="0.0.1",
    author="Rouland Antoine",
    author_email="antoine.rouland@grenoble-inp.org",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AntoineRouland/ki67_pack",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True
)

