import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='awxapis',
    version='0.4',
    author="Nirabhra Tapaswi",
    author_email="nirabhratapaswi@gmail.com",
    description="Helper module for utilizing Ansible Tower/AWX Apis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nirabhratapaswi/awx-apis",
    packages=["awxapis"],
    install_requires=[
        "requests",
        "beautifulsoup4"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
 )