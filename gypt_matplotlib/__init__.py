__version__ = "0.1.0"
__description__ = "A small addon for matplotlib that can be used for the GYPT."
__license__ = "MIT"
__authors__ = ["Keenan Noack <AlbertUnruh@pm.me>"]
__repository__ = "https://github.com/AlbertUnruh/gypt-matplotlib/"


# third party
import matplotlib.pyplot as plt

# local
from .constants import PKG_PATH
from .context_managers import au_plot, auto_close, auto_save, auto_save_and_show, auto_show


__all__ = (
    "au_plot",
    "auto_close",
    "auto_save",
    "auto_save_and_show",
    "auto_show",
)


# automatically apply the GYPT style
plt.style.use(PKG_PATH / "gypt.mplstyle")
