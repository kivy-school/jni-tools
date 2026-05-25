from typing import Any, ClassVar, overload
from android.content.IntentSender import IntentSender
from android.os.Parcel import Parcel
from android.service.autofill.CustomDescription import CustomDescription
from android.service.autofill.Sanitizer import Sanitizer
from android.service.autofill.Validator import Validator
from android.view.autofill.AutofillId import AutofillId

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

class SaveInfo:
    CREATOR: ClassVar[Creator]
    FLAG_DELAY_SAVE: ClassVar[int]
    FLAG_DONT_SAVE_ON_FINISH: ClassVar[int]
    FLAG_SAVE_ON_ALL_VIEWS_INVISIBLE: ClassVar[int]
    NEGATIVE_BUTTON_STYLE_CANCEL: ClassVar[int]
    NEGATIVE_BUTTON_STYLE_NEVER: ClassVar[int]
    NEGATIVE_BUTTON_STYLE_REJECT: ClassVar[int]
    POSITIVE_BUTTON_STYLE_CONTINUE: ClassVar[int]
    POSITIVE_BUTTON_STYLE_SAVE: ClassVar[int]
    SAVE_DATA_TYPE_ADDRESS: ClassVar[int]
    SAVE_DATA_TYPE_CREDIT_CARD: ClassVar[int]
    SAVE_DATA_TYPE_DEBIT_CARD: ClassVar[int]
    SAVE_DATA_TYPE_EMAIL_ADDRESS: ClassVar[int]
    SAVE_DATA_TYPE_GENERIC: ClassVar[int]
    SAVE_DATA_TYPE_GENERIC_CARD: ClassVar[int]
    SAVE_DATA_TYPE_PASSWORD: ClassVar[int]
    SAVE_DATA_TYPE_PAYMENT_CARD: ClassVar[int]
    SAVE_DATA_TYPE_USERNAME: ClassVar[int]
    def toString(self) -> str: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...

    class Builder:
        @overload
        def __init__(self, arg0: int, arg1: list[AutofillId]) -> None: ...
        @overload
        def __init__(self, arg0: int) -> None: ...
        def setFlags(self, arg0: int) -> "Builder": ...
        def setOptionalIds(self, arg0: list[AutofillId]) -> "Builder": ...
        def setDescription(self, arg0: str) -> "Builder": ...
        def setCustomDescription(self, arg0: CustomDescription) -> "Builder": ...
        def setNegativeAction(self, arg0: int, arg1: IntentSender) -> "Builder": ...
        def setPositiveAction(self, arg0: int) -> "Builder": ...
        def setValidator(self, arg0: Validator) -> "Builder": ...
        def addSanitizer(self, arg0: Sanitizer, *arg1: AutofillId) -> "Builder": ...
        def setTriggerId(self, arg0: AutofillId) -> "Builder": ...
        def build(self) -> "SaveInfo": ...
