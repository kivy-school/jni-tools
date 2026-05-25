from typing import Any, ClassVar, overload
from android.os.Bundle import Bundle
from android.os.LocaleList import LocaleList
from android.os.Parcel import Parcel
from android.util.Printer import Printer
from android.view.inputmethod.SurroundingText import SurroundingText

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

class EditorInfo:
    CREATOR: ClassVar[Creator]
    IME_ACTION_DONE: ClassVar[int]
    IME_ACTION_GO: ClassVar[int]
    IME_ACTION_NEXT: ClassVar[int]
    IME_ACTION_NONE: ClassVar[int]
    IME_ACTION_PREVIOUS: ClassVar[int]
    IME_ACTION_SEARCH: ClassVar[int]
    IME_ACTION_SEND: ClassVar[int]
    IME_ACTION_UNSPECIFIED: ClassVar[int]
    IME_FLAG_FORCE_ASCII: ClassVar[int]
    IME_FLAG_NAVIGATE_NEXT: ClassVar[int]
    IME_FLAG_NAVIGATE_PREVIOUS: ClassVar[int]
    IME_FLAG_NO_ACCESSORY_ACTION: ClassVar[int]
    IME_FLAG_NO_ENTER_ACTION: ClassVar[int]
    IME_FLAG_NO_EXTRACT_UI: ClassVar[int]
    IME_FLAG_NO_FULLSCREEN: ClassVar[int]
    IME_FLAG_NO_PERSONALIZED_LEARNING: ClassVar[int]
    IME_MASK_ACTION: ClassVar[int]
    IME_NULL: ClassVar[int]
    actionId: int
    actionLabel: str
    contentMimeTypes: list[str]
    extras: Bundle
    fieldId: int
    fieldName: str
    hintLocales: LocaleList
    hintText: str
    imeOptions: int
    initialCapsMode: int
    initialSelEnd: int
    initialSelStart: int
    inputType: int
    label: str
    packageName: str
    privateImeOptions: str
    def __init__(self) -> None: ...
    def setSupportedHandwritingGestures(self, arg0: list) -> None: ...
    def getSupportedHandwritingGestures(self) -> list: ...
    def setSupportedHandwritingGesturePreviews(self, arg0: set) -> None: ...
    def getSupportedHandwritingGesturePreviews(self) -> set: ...
    def setStylusHandwritingEnabled(self, arg0: bool) -> None: ...
    def isStylusHandwritingEnabled(self) -> bool: ...
    def setInitialSurroundingText(self, arg0: str) -> None: ...
    def setInitialSurroundingSubText(self, arg0: str, arg1: int) -> None: ...
    def getInitialTextBeforeCursor(self, arg0: int, arg1: int) -> str: ...
    def getInitialSelectedText(self, arg0: int) -> str: ...
    def getInitialTextAfterCursor(self, arg0: int, arg1: int) -> str: ...
    def getInitialSurroundingText(self, arg0: int, arg1: int, arg2: int) -> SurroundingText: ...
    def makeCompatible(self, arg0: int) -> None: ...
    def getInitialToolType(self) -> int: ...
    def setInitialToolType(self, arg0: int) -> None: ...
    def dump(self, arg0: Printer, arg1: str) -> None: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def describeContents(self) -> int: ...
