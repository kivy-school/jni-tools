from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.view.translation.TranslationSpec import TranslationSpec

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

class TranslationCapability:
    CREATOR: ClassVar[Creator]
    STATE_AVAILABLE_TO_DOWNLOAD: ClassVar[int]
    STATE_DOWNLOADING: ClassVar[int]
    STATE_NOT_AVAILABLE: ClassVar[int]
    STATE_ON_DEVICE: ClassVar[int]
    def getState(self) -> int: ...
    def getSourceSpec(self) -> TranslationSpec: ...
    def getTargetSpec(self) -> TranslationSpec: ...
    def isUiTranslationEnabled(self) -> bool: ...
    def getSupportedTranslationFlags(self) -> int: ...
    def toString(self) -> str: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def describeContents(self) -> int: ...
