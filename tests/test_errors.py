# standard library
import re

# third party
import pytest

# first party
from gypt_matplotlib import errors


@pytest.mark.parametrize(
    ("message", "may_be_issue", "pattern"),
    [
        ((_0 := "Hello World!"), False, _0),
        ((_0 := "Hello World!"), True, _0),
        ("Hello World!", False, "^[^/]+$"),  # no link
        ("Hello World!", True, ".*/.*"),  # with link
    ],
)
def test_gypt_error(message: str, may_be_issue: bool, pattern: str):
    with pytest.raises(errors.GYPTError, match=re.compile(pattern, re.IGNORECASE)):
        raise errors.GYPTError(message, may_be_issue=may_be_issue)


@pytest.mark.parametrize(
    "unit",
    [None, "Hello World!", True],
)
@pytest.mark.parametrize(
    "is_au",
    [None, True, False, "Hello World!"],
)
def test_axes_label_invalid_call_signature_error(unit: str, is_au: bool):
    part = f"({unit!r}|{is_au!r})"
    pattern = f"{part}.+{r"(?!\1)" if unit != is_au else ""}{part}"
    # pattern requires both unit and is_au being present (independent of order)
    with pytest.raises(errors.AxesLabelInvalidCallSignatureError, match=re.compile(pattern, re.IGNORECASE)):
        raise errors.AxesLabelInvalidCallSignatureError(unit=unit, is_au=is_au)


@pytest.mark.parametrize(
    "signature",
    [
        r"\w+\([^(]+,[^)]+\)",  # general signature
        r"\w+\(name, unit=\.\.\.\)",  # unit signature
        r"\w+\(name, is_au=True\)",  # is_au signature
    ],
)
def test_axes_label_invalid_call_signature_error_signature(signature: str):
    with pytest.raises(errors.AxesLabelInvalidCallSignatureError, match=re.compile(signature, re.IGNORECASE)):
        raise errors.AxesLabelInvalidCallSignatureError(unit=..., is_au=...)
