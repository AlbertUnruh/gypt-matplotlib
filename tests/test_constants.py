# first party
from gypt_matplotlib import constants


def test_okg_path():
    assert constants.PKG_PATH.exists()
    assert constants.PKG_PATH.name == "gypt_matplotlib"
