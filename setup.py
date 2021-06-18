import re

import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

_version_regex = (
    r"^__version__ = ('|\")((?:[0-9]+\.)*[0-9]+(?:\.?([a-z]+)(?:\.?[0-9])?)?)\1$"
)

with open("typed_flags/__init__.py") as stream:
    match = re.search(_version_regex, stream.read(), re.MULTILINE)

version = match.group(2)

setuptools.setup(
    name="discord-typed-flags",
    version=version,
    author="Menudocs",
    author_email="contact@menudocs.org",
    description="A Typehint based flags system for discord.py",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MenuDocs/Typed-Flags",
    packages=setuptools.find_packages(),
    install_requires=["discord.py>=1"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
    ],
    python_requires=">=3.6",
)
