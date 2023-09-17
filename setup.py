import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="neuroinspired-vision",
    version="1.1.0",
    author="Aslan Satary Dizaji",
    author_email="asataryd@umich.edu",
    description="Neuro-Inspired Vision: Building Robust Vision Systems Inspired by Biological Brain",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aslansd/neuroinspired-vision",
    packages=setuptools.find_packages(),
    package_data={},
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)