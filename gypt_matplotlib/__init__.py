__version__ = "0.2.0"
__description__ = "A small addon for matplotlib that can be used for the GYPT."
__license__ = "MIT"
__authors__ = ["Keenan Noack <AlbertUnruh@pm.me>"]
__repository__ = "https://github.com/AlbertUnruh/gypt-matplotlib/"


# local
from .context_managers import au_plot, auto_close, auto_save, auto_save_and_show, auto_show
from .utils import apply_gypt_style, axes_label, tex


__all__ = (
    "au_plot",
    "auto_close",
    "auto_save",
    "auto_save_and_show",
    "auto_show",
    "axes_label",
    "tex",
)


# automatically apply the GYPT style
apply_gypt_style()
