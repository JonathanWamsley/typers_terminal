import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="typers_terminal",
    version="0.0.1",
    author="Jonny Wamsley",
    author_email="Jonnywamsly@gmail.com",
    description="A productivity app for speed reading and typing in a terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JonathanWamsley/typers_terminal",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)