__all__ = ("AxesLabelInvalidCallSignatureError", "GYPTError")


class GYPTError(Exception):
    """Base for all custom exceptions raised by this library."""

    may_be_issue_note: str = (
        "If you believe that this error is due to an internal issue, please open an issue at "
        "https://github.com/AlbertUnruh/gypt-matplotlib/issues."
    )

    def __init__(self, message: str, /, *, may_be_issue: bool):
        super().__init__(message)
        if may_be_issue:
            self.add_note(self.may_be_issue_note)


class AxesLabelInvalidCallSignatureError(GYPTError, TypeError):
    """Error for ``utils.axes_label``."""

    fname: str = "utils.axes_label"

    def __init__(self, *, unit: str | None, is_au: bool):
        super().__init__(
            f"{__package__}.{self.fname}() received an invalid combination of unit ({unit!r}) and is_au ({is_au!r})! "
            f"Valid signatures are {self.fname}(name, unit=...) or {self.fname}(name, is_au=True)!",
            may_be_issue=False,
        )
