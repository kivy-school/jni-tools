from typing import Any, ClassVar, overload
from android.os.Bundle import Bundle
from android.os.LocaleList import LocaleList
from android.os.Parcel import Parcel
from android.util.Printer import Printer
from android.view.autofill.AutofillId import AutofillId
from android.view.inputmethod.SurroundingText import SurroundingText

class EditorInfo:
    CREATOR: ClassVar[Any]
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
    TYPE_CLASS_DATETIME: ClassVar[int]
    TYPE_CLASS_NUMBER: ClassVar[int]
    TYPE_CLASS_PHONE: ClassVar[int]
    TYPE_CLASS_TEXT: ClassVar[int]
    TYPE_DATETIME_VARIATION_DATE: ClassVar[int]
    TYPE_DATETIME_VARIATION_NORMAL: ClassVar[int]
    TYPE_DATETIME_VARIATION_TIME: ClassVar[int]
    TYPE_MASK_CLASS: ClassVar[int]
    TYPE_MASK_FLAGS: ClassVar[int]
    TYPE_MASK_VARIATION: ClassVar[int]
    TYPE_NULL: ClassVar[int]
    TYPE_NUMBER_FLAG_DECIMAL: ClassVar[int]
    TYPE_NUMBER_FLAG_SIGNED: ClassVar[int]
    TYPE_NUMBER_VARIATION_NORMAL: ClassVar[int]
    TYPE_NUMBER_VARIATION_PASSWORD: ClassVar[int]
    TYPE_TEXT_FLAG_AUTO_COMPLETE: ClassVar[int]
    TYPE_TEXT_FLAG_AUTO_CORRECT: ClassVar[int]
    TYPE_TEXT_FLAG_CAP_CHARACTERS: ClassVar[int]
    TYPE_TEXT_FLAG_CAP_SENTENCES: ClassVar[int]
    TYPE_TEXT_FLAG_CAP_WORDS: ClassVar[int]
    TYPE_TEXT_FLAG_ENABLE_TEXT_CONVERSION_SUGGESTIONS: ClassVar[int]
    TYPE_TEXT_FLAG_IME_MULTI_LINE: ClassVar[int]
    TYPE_TEXT_FLAG_MULTI_LINE: ClassVar[int]
    TYPE_TEXT_FLAG_NO_SUGGESTIONS: ClassVar[int]
    TYPE_TEXT_VARIATION_EMAIL_ADDRESS: ClassVar[int]
    TYPE_TEXT_VARIATION_EMAIL_SUBJECT: ClassVar[int]
    TYPE_TEXT_VARIATION_FILTER: ClassVar[int]
    TYPE_TEXT_VARIATION_LONG_MESSAGE: ClassVar[int]
    TYPE_TEXT_VARIATION_NORMAL: ClassVar[int]
    TYPE_TEXT_VARIATION_PASSWORD: ClassVar[int]
    TYPE_TEXT_VARIATION_PERSON_NAME: ClassVar[int]
    TYPE_TEXT_VARIATION_PHONETIC: ClassVar[int]
    TYPE_TEXT_VARIATION_POSTAL_ADDRESS: ClassVar[int]
    TYPE_TEXT_VARIATION_SHORT_MESSAGE: ClassVar[int]
    TYPE_TEXT_VARIATION_URI: ClassVar[int]
    TYPE_TEXT_VARIATION_VISIBLE_PASSWORD: ClassVar[int]
    TYPE_TEXT_VARIATION_WEB_EDIT_TEXT: ClassVar[int]
    TYPE_TEXT_VARIATION_WEB_EMAIL_ADDRESS: ClassVar[int]
    TYPE_TEXT_VARIATION_WEB_PASSWORD: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    actionId: int
    actionLabel: str
    contentMimeTypes: Any
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
    def dump(self, p0: Printer, p1: str) -> None: ...
    def getAutofillId(self) -> AutofillId: ...
    def setAutofillId(self, p0: AutofillId) -> None: ...
    def getInitialToolType(self) -> int: ...
    def makeCompatible(self, p0: int) -> None: ...
    def getInitialSelectedText(self, p0: int) -> str: ...
    def getInitialSurroundingText(self, p0: int, p1: int, p2: int) -> SurroundingText: ...
    def getInitialTextAfterCursor(self, p0: int, p1: int) -> str: ...
    def getInitialTextBeforeCursor(self, p0: int, p1: int) -> str: ...
    def getSupportedHandwritingGesturePreviews(self) -> set: ...
    def getSupportedHandwritingGestures(self) -> list: ...
    def isStylusHandwritingEnabled(self) -> bool: ...
    def isWritingToolsEnabled(self) -> bool: ...
    def setInitialSurroundingSubText(self, p0: str, p1: int) -> None: ...
    def setInitialSurroundingText(self, p0: str) -> None: ...
    def setInitialToolType(self, p0: int) -> None: ...
    def setStylusHandwritingEnabled(self, p0: bool) -> None: ...
    def setSupportedHandwritingGesturePreviews(self, p0: set) -> None: ...
    def setSupportedHandwritingGestures(self, p0: list) -> None: ...
    def setWritingToolsEnabled(self, p0: bool) -> None: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...
