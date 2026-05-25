from typing import Any, ClassVar, overload
from android.os.LocaleList import LocaleList
from android.os.Parcel import Parcel
from android.view.textclassifier.ConversationActions import ConversationActions
from android.view.textclassifier.SelectionEvent import SelectionEvent
from android.view.textclassifier.TextClassification import TextClassification
from android.view.textclassifier.TextClassifierEvent import TextClassifierEvent
from android.view.textclassifier.TextLanguage import TextLanguage
from android.view.textclassifier.TextLinks import TextLinks
from android.view.textclassifier.TextSelection import TextSelection

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Request:
    """Forward declaration for ``android.view.textclassifier.TextSelection.Request``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.view.textclassifier.TextSelection.Request')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/view/textclassifier/TextSelection/Request
    """
    ...
class Creator:
    """Forward declaration for ``android.os.Parcelable.Creator``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.os.Parcelable.Creator')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/os/Parcelable/Creator
    """
    ...

class TextClassifier:
    EXTRA_FROM_TEXT_CLASSIFIER: ClassVar[str]
    HINT_TEXT_IS_EDITABLE: ClassVar[str]
    HINT_TEXT_IS_NOT_EDITABLE: ClassVar[str]
    NO_OP: ClassVar["TextClassifier"]
    TYPE_ADDRESS: ClassVar[str]
    TYPE_DATE: ClassVar[str]
    TYPE_DATE_TIME: ClassVar[str]
    TYPE_EMAIL: ClassVar[str]
    TYPE_FLIGHT_NUMBER: ClassVar[str]
    TYPE_OTHER: ClassVar[str]
    TYPE_PHONE: ClassVar[str]
    TYPE_UNKNOWN: ClassVar[str]
    TYPE_URL: ClassVar[str]
    WIDGET_TYPE_CLIPBOARD: ClassVar[str]
    WIDGET_TYPE_CUSTOM_EDITTEXT: ClassVar[str]
    WIDGET_TYPE_CUSTOM_TEXTVIEW: ClassVar[str]
    WIDGET_TYPE_CUSTOM_UNSELECTABLE_TEXTVIEW: ClassVar[str]
    WIDGET_TYPE_EDITTEXT: ClassVar[str]
    WIDGET_TYPE_EDIT_WEBVIEW: ClassVar[str]
    WIDGET_TYPE_NOTIFICATION: ClassVar[str]
    WIDGET_TYPE_TEXTVIEW: ClassVar[str]
    WIDGET_TYPE_UNKNOWN: ClassVar[str]
    WIDGET_TYPE_UNSELECTABLE_TEXTVIEW: ClassVar[str]
    WIDGET_TYPE_WEBVIEW: ClassVar[str]
    @overload
    def suggestSelection(self, arg0: Request) -> TextSelection: ...
    @overload
    def suggestSelection(self, arg0: str, arg1: int, arg2: int, arg3: LocaleList) -> TextSelection: ...
    @overload
    def classifyText(self, arg0: Request) -> TextClassification: ...
    @overload
    def classifyText(self, arg0: str, arg1: int, arg2: int, arg3: LocaleList) -> TextClassification: ...
    def generateLinks(self, arg0: Request) -> TextLinks: ...
    def getMaxGenerateLinksTextLength(self) -> int: ...
    def detectLanguage(self, arg0: Request) -> TextLanguage: ...
    def suggestConversationActions(self, arg0: Request) -> ConversationActions: ...
    def onSelectionEvent(self, arg0: SelectionEvent) -> None: ...
    def onTextClassifierEvent(self, arg0: TextClassifierEvent) -> None: ...
    def destroy(self) -> None: ...
    def isDestroyed(self) -> bool: ...

    class EntityConfig:
        CREATOR: ClassVar[Creator]
        def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
        @staticmethod
        def createWithHints(arg0: list) -> "EntityConfig": ...
        @staticmethod
        def create(arg0: list, arg1: list, arg2: list) -> "EntityConfig": ...
        @staticmethod
        def createWithExplicitEntityList(arg0: list) -> "EntityConfig": ...
        def resolveEntityListModifications(self, arg0: list) -> list: ...
        def getHints(self) -> list: ...
        def shouldIncludeTypesFromTextClassifier(self) -> bool: ...
        def describeContents(self) -> int: ...

        class Builder:
            def __init__(self) -> None: ...
            def setIncludedTypes(self, arg0: list) -> "Builder": ...
            def setExcludedTypes(self, arg0: list) -> "Builder": ...
            def includeTypesFromTextClassifier(self, arg0: bool) -> "Builder": ...
            def setHints(self, arg0: list) -> "Builder": ...
            def build(self) -> "EntityConfig": ...
