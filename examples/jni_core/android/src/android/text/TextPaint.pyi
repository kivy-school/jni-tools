from typing import Any, ClassVar, overload
from android.graphics.Paint import Paint

class TextPaint:
    ANTI_ALIAS_FLAG: ClassVar[int]
    CURSOR_AFTER: ClassVar[int]
    CURSOR_AT: ClassVar[int]
    CURSOR_AT_OR_AFTER: ClassVar[int]
    CURSOR_AT_OR_BEFORE: ClassVar[int]
    CURSOR_BEFORE: ClassVar[int]
    DEV_KERN_TEXT_FLAG: ClassVar[int]
    DITHER_FLAG: ClassVar[int]
    EMBEDDED_BITMAP_TEXT_FLAG: ClassVar[int]
    END_HYPHEN_EDIT_INSERT_ARMENIAN_HYPHEN: ClassVar[int]
    END_HYPHEN_EDIT_INSERT_HYPHEN: ClassVar[int]
    END_HYPHEN_EDIT_INSERT_MAQAF: ClassVar[int]
    END_HYPHEN_EDIT_INSERT_UCAS_HYPHEN: ClassVar[int]
    END_HYPHEN_EDIT_INSERT_ZWJ_AND_HYPHEN: ClassVar[int]
    END_HYPHEN_EDIT_NO_EDIT: ClassVar[int]
    END_HYPHEN_EDIT_REPLACE_WITH_HYPHEN: ClassVar[int]
    FAKE_BOLD_TEXT_FLAG: ClassVar[int]
    FILTER_BITMAP_FLAG: ClassVar[int]
    HINTING_OFF: ClassVar[int]
    HINTING_ON: ClassVar[int]
    LINEAR_TEXT_FLAG: ClassVar[int]
    START_HYPHEN_EDIT_INSERT_HYPHEN: ClassVar[int]
    START_HYPHEN_EDIT_INSERT_ZWJ: ClassVar[int]
    START_HYPHEN_EDIT_NO_EDIT: ClassVar[int]
    STRIKE_THRU_TEXT_FLAG: ClassVar[int]
    SUBPIXEL_TEXT_FLAG: ClassVar[int]
    TEXT_RUN_FLAG_LEFT_EDGE: ClassVar[int]
    TEXT_RUN_FLAG_RIGHT_EDGE: ClassVar[int]
    UNDERLINE_TEXT_FLAG: ClassVar[int]
    VERTICAL_TEXT_FLAG: ClassVar[int]
    baselineShift: int
    bgColor: int
    density: float
    drawableState: Any
    linkColor: int
    underlineColor: int
    underlineThickness: float
    @overload
    def __init__(self, p0: int) -> None: ...
    @overload
    def __init__(self, p0: Paint) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def set(self, p0: "TextPaint") -> None: ...
    def getUnderlineThickness(self) -> float: ...
