# standard library
from contextlib import contextmanager
from pathlib import Path

# third party
import matplotlib.pyplot as plt

# local
from .constants import AU_STYLE


__all__ = (
    "au_plot",
    "auto_close",
    "auto_save",
    "auto_save_and_show",
    "auto_show",
)


@contextmanager
def au_plot():
    """Contextmanager for plots with a.u. (arbitrary units)."""
    with plt.style.context(AU_STYLE):
        yield


@contextmanager
def auto_close():
    """Contextmanager to automatically close plots."""
    yield
    plt.close()


@contextmanager
def auto_save(fname: Path | str, **kwargs: ...):
    """
    Contextmanager to automatically save and close plots.

    Parameters
    ----------
    fname : Path or str
        The filename or path to save the plot to.

    Other Parameters
    ----------------
    **kwargs
        Will be passed to `plt.savefig()`.

    Notes
    -----
    This contextmanager automatically applies `plt.tight_layout()` to the plot.

    Warnings
    --------
    This is incompatible with `auto_show`! Use `auto_save_and_show` instead!

    See Also
    --------
    plt.savefig()
    """
    with auto_close():
        yield
        plt.tight_layout()
        plt.savefig(fname, **kwargs)


@contextmanager
def auto_show():
    """
    Contextmanager to automatically show and close plots.

    Notes
    -----
    This contextmanager automatically applies `plt.tight_layout()` to the plot.

    Warnings
    --------
    This is incompatible with `auto_save`! Use `auto_save_and_show` instead!
    """
    with auto_close():  # pragma: no cover  # plt.show() won't be tested
        yield
        plt.tight_layout()
        plt.show()


@contextmanager
def auto_save_and_show(fname: Path | str, **kwargs: ...):
    """
    Contextmanager to automatically save, show and close plots.

    It combines the basic functionality of ``auto_save`` and ``auto_show``.

    Parameters
    ----------
    fname : Path or str
        The filename or path to save the plot to.

    Other Parameters
    ----------------
    **kwargs
        Will be passed to `plt.savefig()`.

    Notes
    -----
    This contextmanager automatically applies `plt.tight_layout()` to the plot.
    """
    with auto_close():  # pragma: no cover  # plt.show() won't be tested
        yield
        plt.tight_layout()
        plt.savefig(fname, **kwargs)
        plt.show()
