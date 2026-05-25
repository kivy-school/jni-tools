from typing import Any, ClassVar, overload

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Named:
    """Forward declaration for ``android.graphics.ColorSpace.Named``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.graphics.ColorSpace.Named')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/graphics/ColorSpace/Named
    """
    ...

class ColorSpaceProfiles:
    UNSPECIFIED: ClassVar[int]
    def __init__(self, arg0: list[int]) -> None: ...
    def getSupportedColorSpaces(self, arg0: int) -> set: ...
    def getSupportedImageFormatsForColorSpace(self, arg0: Named) -> set: ...
    def getSupportedDynamicRangeProfiles(self, arg0: Named, arg1: int) -> set: ...
    def getSupportedColorSpacesForDynamicRange(self, arg0: int, arg1: int) -> set: ...
