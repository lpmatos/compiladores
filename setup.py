# -*- coding: utf-8 -*-

from setuptools import find_packages, setup
from compyler import __version__

NAME = "compyler"

LONG_DESCRIPTION = """
Projeto compiladores - CCON7A-CCO076 [2020]
""".strip()

SHORT_DESCRIPTION = """
Projeto compiladores - CCON7A-CCO076 [2020].""".strip()

DEPENDENCIES = [
    "asciimatics==1.12.0",
    "docopt==0.6.2",
]

URL = "https://github.com/lpmatos/compyler"
EMAIL = "luccapsm@gmail.com"
AUTHOR = "Lucca Pessoa da Silva Matos"
REQUIRES_PYTHON = ">=3.8.0"
VERSION = __version__

setup(
    name=NAME,
    author=AUTHOR,
    author_email=EMAIL,
    version=VERSION,
    license="MIT license",
    url=URL,
    packages=find_packages(include=[NAME], exclude=[
                           "tests", "*.tests", "*.tests.*", "tests.*"]),
    package_data={NAME: ["py.typed"]},
    zip_safe=False,
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    install_requires=DEPENDENCIES,
    python_requires=REQUIRES_PYTHON,
    entry_points=f"""
        [console_scripts]
        {NAME}={NAME}.main:main
    """,
    keywords=[
        "cli",
        "python"
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Helm",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    project_urls={
        "Repository": "https://github.com/lpmatos/compyler",
    },
)
