from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.os.LocaleList import LocaleList
from android.os.Parcel import Parcel
from java.util.Locale import Locale

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

class LocaleConfig:
    CREATOR: ClassVar[Creator]
    STATUS_NOT_SPECIFIED: ClassVar[int]
    STATUS_PARSING_FAILED: ClassVar[int]
    STATUS_SUCCESS: ClassVar[int]
    TAG_LOCALE: ClassVar[str]
    TAG_LOCALE_CONFIG: ClassVar[str]
    @overload
    def __init__(self, arg0: Context) -> None: ...
    @overload
    def __init__(self, arg0: LocaleList) -> None: ...
    @staticmethod
    def fromContextIgnoringOverride(arg0: Context) -> "LocaleConfig": ...
    def getSupportedLocales(self) -> LocaleList: ...
    def getDefaultLocale(self) -> Locale: ...
    def getStatus(self) -> int: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
