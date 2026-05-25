from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.text.TextPaint import TextPaint

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class FontMetricsInt:
    """Forward declaration for ``android.graphics.Paint.FontMetricsInt``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.graphics.Paint.FontMetricsInt')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/graphics/Paint/FontMetricsInt
    """
    ...

class LineHeightSpan:
    def chooseHeight(self, arg0: str, arg1: int, arg2: int, arg3: int, arg4: int, arg5: FontMetricsInt) -> None: ...

    class Standard:
        @overload
        def __init__(self, arg0: int) -> None: ...
        @overload
        def __init__(self, arg0: Parcel) -> None: ...
        def getHeight(self) -> int: ...
        def getSpanTypeId(self) -> int: ...
        def describeContents(self) -> int: ...
        def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
        def chooseHeight(self, arg0: str, arg1: int, arg2: int, arg3: int, arg4: int, arg5: FontMetricsInt) -> None: ...

    class WithDensity:
        def chooseHeight(self, arg0: str, arg1: int, arg2: int, arg3: int, arg4: int, arg5: FontMetricsInt, arg6: TextPaint) -> None: ...
