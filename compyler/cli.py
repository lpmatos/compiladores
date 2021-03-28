# -*- coding: utf-8 -*-

import sys
from typing import Dict, NoReturn

from compyler.cli_version import show_version


def cli(information: Dict) -> NoReturn:
    if information["-v"] or information["--version"]:
        show_version()
        sys.exit(1)

    print("Hello!")
