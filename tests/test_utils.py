# standard library
from pathlib import Path

# third party
import matplotlib.pyplot as plt
import pytest

# first party
from gypt_matplotlib import constants, context_managers, errors, utils

# local
from .utils import assert_identical_images


def test_axes_label(random_str: str):
    variable_name = random_str[::-1]

    unit_label = utils.axes_label(variable_name, unit=random_str)
    assert random_str in unit_label
    assert variable_name in unit_label

    au_label = utils.axes_label(variable_name, is_au=True)
    assert constants.AU in au_label
    assert variable_name in au_label


@pytest.mark.parametrize(
    "kwargs",
    [
        # ↓ function defaults ↓
        {},
        {"unit": None},
        {"is_au": False},
        {"unit": None, "is_au": False},
        # ↓ non function default ↓
        {"unit": "", "is_au": True},
    ],
)
def test_axes_label_fail(kwargs: dict[str, str | bool]):
    with pytest.raises(errors.AxesLabelInvalidCallSignatureError):
        utils.axes_label("", **kwargs)


def test_axes_label_plot(img_label_plot: Path, out_png_path: Path):
    with context_managers.auto_save(out_png_path):
        plt.xlabel(utils.axes_label("x", unit="m"))
        plt.ylabel(utils.axes_label("f(x)", is_au=True))

    assert img_label_plot != out_png_path, "Output and control are the same!"

    assert_identical_images(out_png_path, img_label_plot)


def test_tex(random_str: str):
    assert utils.tex(random_str) != random_str, "`utils.tex()` returns the input!"
    assert random_str in utils.tex(random_str), "`utils.tex()` manipulates the input itself!"
