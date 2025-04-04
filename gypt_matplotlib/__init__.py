__version__ = "0.4.2"
__description__ = "A small addon for matplotlib that can be used for the GYPT."
__license__ = "MIT"
__authors__ = ["Keenan Noack <AlbertUnruh@pm.me>"]
__repository__ = "https://github.com/AlbertUnruh/gypt-matplotlib/"


# local
from . import constants, context_managers, errors, utils
from .context_managers import au_plot, auto_close, auto_save, auto_save_and_show, auto_show
from .utils import apply_gypt_style, axes_label, tex


__all__ = (
    "au_plot",
    "auto_close",
    "auto_save",
    "auto_save_and_show",
    "auto_show",
    "axes_label",
    "constants",
    "context_managers",
    "errors",
    "tex",
    "utils",
)


# automatically apply the GYPT style
apply_gypt_style()
