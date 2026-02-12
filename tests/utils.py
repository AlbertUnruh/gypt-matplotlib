# standard library
from pathlib import Path

# third party
from PIL import Image, ImageChops

__all__ = ("assert_identical_images",)


def assert_identical_images(path_a: Path, path_b: Path, /):
    img_diff = ImageChops.difference(Image.open(path_a), Image.open(path_b))
    bytes_diff = img_diff.tobytes().replace(b"\x00", b"")
    assert len(bytes_diff) == 0, f"`{path_a}` and `{path_b}` are different!"
