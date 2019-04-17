import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pysicologo-herloncamargo",
    version="0.0.1.rc1",
    author="Herlon Camargo",
    author_email="herloncamargo@gmail.com",
    description="A simple multi-language sentiment analyzer.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/herloncamargo/pysicologo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
