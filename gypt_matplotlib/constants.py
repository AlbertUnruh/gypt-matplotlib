# standard library
from pathlib import Path


__all__ = ("AU", "AU_STYLE", "PKG_PATH", "STYLE_PATH")


PKG_PATH: Path = Path(__file__).parent  # package path
STYLE_PATH: Path = PKG_PATH / "gypt.mplstyle"

AU_STYLE: dict[str, bool] = {  # Style for plots with a.u. (arbitrary units)
    "xtick.top": False,
    "xtick.bottom": False,
    "xtick.labelbottom": False,
    "ytick.left": False,
    "ytick.right": False,
    "ytick.labelleft": False,
}
AU: str = r"\text{a.u.}"
