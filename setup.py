from setuptools import setup, find_packages

setup(
    name="beanie_size_grader",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas>=2.0.0",
        "openpyxl>=3.0.0"
    ],
    entry_points={
        "console_scripts": [
            "beanie-grader=beanie_grader.beanie_grader:main",
        ],
    },
    description="Automates size grading for knit beanies/hats",
    author="YOUR NAME",
    url="https://github.com/Xhenzouu/beanie-size-grader",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
