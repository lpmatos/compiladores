# -*- coding: utf-8 -*-

"""
Description: Projeto compiladores - linguagem Estrela.

Usage:
  compyler [options]
  compyler -h | --help
  compyler -v | --version

Options:
  -h --help                         show this help message and exit
  --version                         show version and exit
"""

from typing import NoReturn
from docopt import docopt

from compyler.cli import cli


def main() -> NoReturn:
    arguments = dict(docopt(__doc__))
    cli(arguments)


if __name__ == "__main__":
    main()
