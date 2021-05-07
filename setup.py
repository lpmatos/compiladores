# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

from compyler import __version__, __app_name__

NAME = __app_name__

LONG_DESCRIPTION = """
A linguagem de programação SIMPLE, como o próprio nome indica, é uma linguagem simples,
mas ainda sim poderosa e de alto nível, semelhante às versões iniciais da conhecida linguagem BASIC.

Por meio de um CLI estaremos desenvolvendo um compilador feito em Python para essa linguagem que terá
as fazes de análise léxica, sintática and semântica.
""".strip()

SHORT_DESCRIPTION = """
IESB - [CCON7A-CCO076] - Projeto compiladores - Criação de um compilador para a linguagem SIMPLE.""".strip()

DEPENDENCIES = [
    "arrow==1.1.0",
    "asciimatics==1.12.0",
    "docopt==0.6.2",
    "rich==10.0.0",
]

URL = "https://github.com/lpmatos/compyler"
EMAIL = "luccapsm@protonmail.com"
AUTHOR = "Lucca Pessoa da Silva Matos"
REQUIRES_PYTHON = ">=3.6.0"
VERSION = __version__

setup(
    name=NAME,
    author=AUTHOR,
    author_email=EMAIL,
    version=VERSION,
    license="MIT license",
    url=URL,
    packages=find_packages(include=[NAME]),
    package_data={NAME: ["py.typed"]},
    include_package_data=True,
    zip_safe=False,
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    install_requires=DEPENDENCIES,
    python_requires=REQUIRES_PYTHON,

    entry_points=f"""
        [console_scripts]
        {NAME}={NAME}.main:main
    """,

    keywords=(
        "cli",
        "python"
    ),

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
        "Repository": f"{URL}",
    },
)
