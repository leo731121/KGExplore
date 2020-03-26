import setuptools
import os

rootdir = os.path.abspath(os.path.dirname(__file__))
long_description = open(os.path.join(rootdir, 'README.md')).read()

setuptools.setup(
    name="xiushang",
    version="0.1.0",
    author="SmoothNLP Oraganization",
    author_email="contact@smoothnlp.com",
    description="Python Package for Xiushang",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/smoothnlp/SmoothNLP",
    packages=setuptools.find_packages(),
    install_requires=[
        'request',
      ],
    keywords=["Knowledge Graph","Business"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    test_suite = "smoothnlp.unittest.testall",
)
