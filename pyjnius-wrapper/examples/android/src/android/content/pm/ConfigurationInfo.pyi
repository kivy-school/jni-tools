from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Creator:
    """Forward declaration for ``android.os.Parcelable.Creator``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.os.Parcelable.Creator')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/os/Parcelable/Creator
    """
    ...

class ConfigurationInfo:
    CREATOR: ClassVar[Creator]
    GL_ES_VERSION_UNDEFINED: ClassVar[int]
    INPUT_FEATURE_FIVE_WAY_NAV: ClassVar[int]
    INPUT_FEATURE_HARD_KEYBOARD: ClassVar[int]
    reqGlEsVersion: int
    reqInputFeatures: int
    reqKeyboardType: int
    reqNavigation: int
    reqTouchScreen: int
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: "ConfigurationInfo") -> None: ...
    def toString(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def getGlEsVersion(self) -> str: ...
