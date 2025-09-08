# setup.py

from setuptools import setup, find_packages

setup(
    name="meg-compliance",
    version="0.1.0",
    author="MEG Initiative",
    author_email="contact@meg-initiative.org",
    description="A middleware for making AI systems compliant with the Minimal Ethical Governance (MEG) protocol.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/meg-initiative/meg-sdk",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires='>=3.8',
    install_requires=[
        # ...
    ],
)
