[![GitHub License](https://img.shields.io/github/license/AlbertUnruh/gypt-matplotlib)](https://github.com/AlbertUnruh/gypt-matplotlib/blob/develop/LICENSE)
[![Python version](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2FAlbertUnruh%2Fgypt-matplotlib%2Frefs%2Fheads%2Fdevelop%2Fpyproject.toml&query=%24.project.requires-python&label=Python)](https://python.org)
[![PyPI - Version](https://img.shields.io/pypi/v/gypt_matplotlib?label=PyPi)](https://pypi.org/project/gypt_matplotlib/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
</br>
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/AlbertUnruh/gypt-matplotlib/develop.svg)](https://results.pre-commit.ci/latest/github/AlbertUnruh/gypt-matplotlib/develop)
[![Code QL](https://img.shields.io/github/actions/workflow/status/AlbertUnruh/gypt-matplotlib/.github%2Fworkflows%2Fcodeql.yml?branch=develop&logo=github&label=CodeQL)](https://github.com/AlbertUnruh/gypt-matplotlib/actions/workflows/codeql.yml)
[![pytest](https://img.shields.io/github/actions/workflow/status/AlbertUnruh/gypt-matplotlib/.github%2Fworkflows%2Fpytest.yml?branch=develop&logo=github&label=pytest)](https://github.com/AlbertUnruh/gypt-matplotlib/actions/workflows/pytest.yml)
</br>
[![GitHub Issues](https://img.shields.io/github/issues-raw/AlbertUnruh/gypt-matplotlib)](https://github.com/AlbertUnruh/gypt-matplotlib/issues)
[![GitHub PRs](https://img.shields.io/github/issues-pr-raw/AlbertUnruh/gypt-matplotlib)](https://github.com/AlbertUnruh/gypt-matplotlib/pulls)


# gypt-matplotlib
A small addon for matplotlib that can be used for the GYPT.


---

### GYPT?
GYPT stands for **G**erman **Y**oung **P**hysicists’ **T**ournament.

Further information can be found at [gypt.org][].


### Where did you get the stylesheet?
It's available over [here][stylesheet] at the [GYPT wiki][wiki].


[gypt.org]: https://gypt.org
[wiki]: https://wiki.gypt.org
[stylesheet]: https://wiki.gypt.org/index.php/Python/stylesheet


---

### How to use:

#### Applying GYPT-stylesheet
Just import the library. The stylesheet will be automatically applied.
```python
import gypt_matplotlib as gypt
```

#### Creating plots with ``a.u.`` (arbitrary units)
You can use the context manager ``gypt.au_plot()``
to create plots where the concept and not the actual numbers are important.
```python
import matplotlib.pyplot as plt
import gypt_matplotlib as gypt

with gypt.au_plot():
    plt.title("Demo of plot without numbers on X-/Y-Axis.")
    plt.show()

# or even more advanced:
with gypt.au_plot(), gypt.auto_save_and_show("path/to/file.png"):
    plt.title("Demo of plot without numbers on X-/Y-Axis.")
```

#### Using other diverse context managers
```python
import matplotlib.pyplot as plt
import gypt_matplotlib as gypt

with gypt.auto_close():
    # This context manager automatically calls ``plt.close()``.
    # Saving and displaying have to be done manually!
    ...

with gypt.auto_show():
    # This context manager automatically calls ``plt.show()`` and ``plt.close()``.
    # It's incompatible with ``gypt.auto_save()``! Use ``gypt.auto_save_and_show()`` instead!
    ...

with gypt.auto_save("path/to/file.png"):
    # This context manager automatically calls ``plt.savefig()`` and ``plt.close()``.
    # It's incompatible with ``gypt.auto_show()``! Use ``gypt.auto_save_and_show()`` instead!
    ...

with gypt.auto_save_and_show("path/to/file.png"):
    # This context manager automatically calls ``plt.savefig()``, ``plt.show()`` and ``plt.close()``.
    ...
```
