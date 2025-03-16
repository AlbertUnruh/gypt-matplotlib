# standard library
from pathlib import Path


__all__ = ("AU_STYLE", "PKG_PATH")


PKG_PATH: Path = Path(__file__).parent  # package path

AU_STYLE: dict[str, bool] = {  # Style for plots with a.u. (arbitrary units)
    "xtick.top": False,
    "xtick.bottom": False,
    "xtick.labelbottom": False,
    "ytick.left": False,
    "ytick.right": False,
    "ytick.labelleft": False,
}
