# standard library
from pathlib import Path

# third party
import matplotlib.pyplot as plt

# first party
from gypt_matplotlib import constants, context_managers, utils

# local
from .utils import assert_identical_images


def test_auto_safe(out_png_path: Path):
    assert not out_png_path.exists(), "`out.png` already exists!"
    with context_managers.auto_save(out_png_path):
        pass
    assert out_png_path.exists(), "`auto_save()` didn't save!"


def test_au_plot(img_au_plot: Path, out_png_path: Path):
    with context_managers.au_plot(), context_managers.auto_save(out_png_path):
        plt.title(f"plot with {utils.tex(constants.AU)}")
    assert img_au_plot != out_png_path, "Output and control are the same!"

    assert_identical_images(out_png_path, img_au_plot)
