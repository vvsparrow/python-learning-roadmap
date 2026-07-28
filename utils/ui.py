from rich.console import Console

# \ufe0f — Variation Selector-16. Форсирует цветной Emoji Style в Alacritty
ICON_OK = "✅\ufe0f"
ICON_ERR = "❌\ufe0f"
ICON_WRN = "\u26a0\ufe0f"

_c = Console()


def ok(msg: str):
    _c.print(f"{ICON_OK} [bold green]{msg}[/bold green]")


def err(msg: str):
    _c.print(f"{ICON_ERR} [bold red]{msg}[/bold red]")


def wrn(msg: str):
    _c.print(f"{ICON_WRN} [bold yellow]{msg}[/bold yellow]")
