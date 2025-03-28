# standard library
from pathlib import Path

# third party
import matplotlib.pyplot as plt
import numpy as np

# first party
from gypt_matplotlib import context_managers

# local
from .utils import assert_identical_images


def test_plot(img_plot: Path, out_png_path: Path, random_2d_array: np.ndarray):
    assert not out_png_path.exists(), "`out.png` already exists!"
    with context_managers.auto_save(out_png_path):
        plt.plot(*random_2d_array)
    assert_identical_images(out_png_path, img_plot)


def test_scatter(img_scatter: Path, out_png_path: Path, random_2d_array: np.ndarray):
    assert not out_png_path.exists(), "`out.png` already exists!"
    with context_managers.auto_save(out_png_path):
        plt.scatter(*random_2d_array)
    assert_identical_images(out_png_path, img_scatter)


def test_errorbar(img_errorbar: Path, out_png_path: Path, random_2d_array: np.ndarray):
    assert not out_png_path.exists(), "`out.png` already exists!"
    with context_managers.auto_save(out_png_path):
        plt.errorbar(*random_2d_array, *(0.1 * random_2d_array), fmt=". ")
    assert_identical_images(out_png_path, img_errorbar)


def test_hist2d(img_hist2d: Path, out_png_path: Path, random_2d_array: np.ndarray):
    assert not out_png_path.exists(), "`out.png` already exists!"
    with context_managers.auto_save(out_png_path):
        plt.hist2d(*random_2d_array)
    assert_identical_images(out_png_path, img_hist2d)
