import setuptools

setuptools.setup(
    name="shared_objects",  # Replace with a unique name for PyPI
    version="0.1.1",
    description="ROS2 Utils",
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

