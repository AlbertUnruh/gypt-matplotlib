# standard library
from pathlib import Path

# third party
import matplotlib.pyplot as plt
from PIL import Image, ImageChops

# first party
from gypt_matplotlib import context_managers


def test_auto_safe(out_png_path: Path):
    assert not out_png_path.exists(), "`out.png` already exists!"
    with context_managers.auto_save(out_png_path):
        pass
    assert out_png_path.exists(), "`auto_save()` didn't save!"


def test_au_plot(img_au_plot: Path, out_png_path: Path):
    with context_managers.au_plot(), context_managers.auto_save(out_png_path):
        plt.title(r"plot with $\text{a.u.}$")
    assert img_au_plot != out_png_path, "Output and control are the same!"

    img_diff = ImageChops.difference(Image.open(out_png_path), Image.open(img_au_plot))
    bytes_diff = img_diff.tobytes().replace(b"\x00", b"")
    assert len(bytes_diff) == 0, f"`{img_au_plot}` and `{out_png_path}` are different!"
