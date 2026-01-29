# standard library
import secrets
from pathlib import Path

# third party
import pytest


IMG_DIR: Path = Path(__file__).parent / "img/"
assert IMG_DIR.exists(), "No image directory present!"
assert IMG_DIR.is_dir(), "Image directory not a directory!"


@pytest.fixture
def out_png_path(tmp_path: Path) -> Path:
    return tmp_path / "out.png"


@pytest.fixture
def img_au_plot() -> Path:
    name = "au_plot.png"
    path = IMG_DIR / name
    assert path.is_file(), f"`{name}` not present!"
    return path


@pytest.fixture
def img_label_plot() -> Path:
    name = "label_plot.png"
    path = IMG_DIR / name
    assert path.is_file(), f"`{name}` not present!"
    return path


@pytest.fixture
def random_str() -> str:
    return secrets.token_urlsafe()
