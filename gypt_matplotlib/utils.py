# standard library
from typing import Literal, overload

# third party
import matplotlib.pyplot as plt

# local
from .constants import AU, STYLE_PATH


__all__ = (
    "apply_gypt_style",
    "axes_label",
    "tex",
)


def apply_gypt_style() -> None:
    """Apply the GYPT-stylesheet."""
    plt.style.use(STYLE_PATH)


@overload
def axes_label(name: str, *, unit: str) -> str: ...
@overload
def axes_label(name: str, *, is_au: Literal[True]) -> str: ...


def axes_label(name: str, *, unit: str | None = None, is_au: bool = False) -> str:
    """
    Generate a label for an axes.

    Parameters
    ----------
    name : str
        The name of the variable/parameter.
    unit : str, optional
        The unit's name of the variable/parameter.
    is_au : bool
        Whether the unit of the variable/parameter is in arbitrary units.

    Returns
    -------
    str
        A formatted label containing the variable/parameter and unit for an axes.
    """
    if unit is None and is_au is False:
        raise ValueError("Either `unit` or `is_au` have to be set!")  # noqa: TRY003, EM101
    if isinstance(unit, str) and is_au is True:
        raise ValueError("Can't set `unit` and `is_au` at the same time!")  # noqa: TRY003, EM101

    if is_au:
        unit = AU
    return f"{tex(name)} in {tex(unit)}"


def tex(tex_string: str, /) -> str:
    r"""Wrap the given text to be rendered as \TeX."""
    return f"${tex_string}$"
