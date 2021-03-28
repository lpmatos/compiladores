# -*- coding: utf-8 -*-

from typing import NoReturn

import arrow
from rich.table import Table
from rich.console import Console
from rich.markdown import Markdown

from compyler.const import DATA_FORMAT, TIMEZONE
from . import __version__


def show_version() -> NoReturn:
    console = Console()
    console.print(Markdown("# Version"))

    table = Table(show_header=True, header_style="bold blue")
    table.add_column(
        "NAME", style="dim", width=12, footer_style="bright_green"
    )
    table.add_column(
        "CLI VERSION", style="dim", width=12, footer_style="bright_green"
    )
    table.add_column(
        "SYSTEM DATE", style="dim", width=20, footer_style="bright_green"
    )
    table.add_row(
        "🤖 compyler",
        __version__,
        str(arrow.utcnow().to(TIMEZONE).format(DATA_FORMAT)),
    )
    console.print(table)
