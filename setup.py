from setuptools import setup

with open("README.md", "r") as md:
    long_description = md.read()

setup(
    name="pyawx-client",
    packages=["pyawx", "pyawx.models", "pyawx.exceptions"],
    version="0.1.1",
    license="Apache 2.0",
    description="Python API to access Ansible AWX/Tower v2 API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Dennis Whitney",
    author_email="dennis@irunasroot.com",
    url="https://github.com/irunasroot/pyawx-client",
    download_url="https://github.com/irunasroot/pyawx-client/archive/v0.1.1.tar.gz",
    keywords=["ansible", "tower", "awx", "redhat", "ansible tower", "ansible awx", "playbook", "automation"],
    install_requires=[
        "requests"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6"
    ]
)
