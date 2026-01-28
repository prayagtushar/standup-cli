from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="standup-cli",
    version="0.1.0",
    description="Daily Standup Auto-Generator from git commits",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Prayag Tushar",
    author_email="prayagtushar2016@gmail.com",
    url="https://github.com/prayagtushar/standup-cli",
    py_modules=["main", "git_utils", "parser"],
    entry_points={
        "console_scripts": [
            "standup-cli=main:app",
        ],
    },
    install_requires=[
        "typer>=0.12.0",
        "rich>=13.7.0",
        "GitPython>=3.1.43",
        "pyperclip>=1.8.2",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Systems Administration",
    ],
    keywords="standup git cli commits automation",
)
