import setuptools

setuptools.setup(
    name="shared_objects",  # Replace with a unique name for PyPI
    version="0.1.0",
    description="A description of your package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Can Ozaydin",
    author_email="ozaydincan.app@gmail.com",
    url="https://github.com/ozaydincan/shared_objects.git",  # Update with your GitHub repo
    packages=["shared_objects"],
    package_dir={"shared_objects": "src/shared_objects"},
    python_requires=">=3.9",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Update with your license
        "Operating System :: OS Independent",
    ],
    license="MIT",
)

