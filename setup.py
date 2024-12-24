from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name='AutoExpireDB',
    version='1.0.0',
    author="Siddhanth",
    author_email="thebiryanimonsterr@gmail.com",
    description='A library for automatically expiring database users and password entries.',    
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(include=["src"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "psycopg2-binary",
        "celery"
    ],
    license="MIT",
    url="https://github.com/mafiaguy/AutoExpireDB",
)
