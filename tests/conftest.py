# standard library
import secrets
from pathlib import Path

# third party
import pytest

# first party
from gypt_matplotlib.constants import PKG_PATH


IMG_DIR: Path = Path(__file__).parent / "img/"
assert IMG_DIR.exists(), "No image directory present!"
assert IMG_DIR.is_dir(), "Image directory not a directory!"


def _stylesheet_published() -> bool:
    """
    Check whether the GYPT stylesheet is published or not.

    The stylesheet is ready (locally), but I'm waiting for approval to publish it.
    This function is only used to determine the correct control-file, as they differ due to the different styles.

    Once the stylesheet is published, I'll remove this function as it's no longer necessary.
    It's only in place to prevent failing CI due to me already having the stylesheet integrated locally.
    """
    return (PKG_PATH / "gypt.mplstyle").read_text("utf-8") != "# COMING SOON\n"


@pytest.fixture
def out_png_path(tmp_path: Path) -> Path:
    return tmp_path / "out.png"


@pytest.fixture
def img_au_plot() -> Path:
    name = "au_plot.png" if _stylesheet_published() else "_au_plot.png"
    path = IMG_DIR / name
    assert path.is_file(), f"`{name}` not present!"
    return path


@pytest.fixture
def img_label_plot() -> Path:
    name = "label_plot.png" if _stylesheet_published() else "_label_plot.png"
    path = IMG_DIR / name
    assert path.is_file(), f"`{name}` not present!"
    return path


@pytest.fixture
def random_str() -> str:
    return secrets.token_urlsafe()
