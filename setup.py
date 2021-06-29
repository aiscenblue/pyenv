import setuptools

setuptools.setup(
    name="Python virtual environment manager",
    version="0.0.2",
    author="Jeffrey Marvin Forones",
    author_email="aiscenblue@gmail.com",
    description="Handles creation of virtual environment",
    url="https://github.com/aiscenblue/python-virtual-env-manager",
    project_urls={
        "Bug Tracker": "https://github.com/aiscenblue/python-virtual-env-manager/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)