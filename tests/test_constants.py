# first party
from gypt_matplotlib import constants


def test_pkg_path():
    assert constants.PKG_PATH.is_dir()
    assert constants.PKG_PATH.name == "gypt_matplotlib"


def test_style_path():
    assert constants.STYLE_PATH.is_file()
    assert constants.STYLE_PATH.suffix == ".mplstyle"
