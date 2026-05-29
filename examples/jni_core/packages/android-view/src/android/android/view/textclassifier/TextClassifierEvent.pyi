from typing import Any, ClassVar, overload
from android.icu.util.ULocale import ULocale
from android.os.Bundle import Bundle
from android.os.Parcel import Parcel
from android.view.textclassifier.TextClassificationContext import TextClassificationContext

class TextClassifierEvent:
    CATEGORY_CONVERSATION_ACTIONS: ClassVar[int]
    CATEGORY_LANGUAGE_DETECTION: ClassVar[int]
    CATEGORY_LINKIFY: ClassVar[int]
    CATEGORY_SELECTION: ClassVar[int]
    CREATOR: ClassVar[Any]
    TYPE_ACTIONS_GENERATED: ClassVar[int]
    TYPE_ACTIONS_SHOWN: ClassVar[int]
    TYPE_AUTO_SELECTION: ClassVar[int]
    TYPE_COPY_ACTION: ClassVar[int]
    TYPE_CUT_ACTION: ClassVar[int]
    TYPE_LINKS_GENERATED: ClassVar[int]
    TYPE_LINK_CLICKED: ClassVar[int]
    TYPE_MANUAL_REPLY: ClassVar[int]
    TYPE_OTHER_ACTION: ClassVar[int]
    TYPE_OVERTYPE: ClassVar[int]
    TYPE_PASTE_ACTION: ClassVar[int]
    TYPE_SELECTION_DESTROYED: ClassVar[int]
    TYPE_SELECTION_DRAG: ClassVar[int]
    TYPE_SELECTION_MODIFIED: ClassVar[int]
    TYPE_SELECTION_RESET: ClassVar[int]
    TYPE_SELECTION_STARTED: ClassVar[int]
    TYPE_SELECT_ALL: ClassVar[int]
    TYPE_SHARE_ACTION: ClassVar[int]
    TYPE_SMART_ACTION: ClassVar[int]
    TYPE_SMART_SELECTION_MULTI: ClassVar[int]
    TYPE_SMART_SELECTION_SINGLE: ClassVar[int]
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getResultId(self) -> str: ...
    def getEventIndex(self) -> int: ...
    def getEntityTypes(self) -> Any: ...
    def getEventCategory(self) -> int: ...
    def getEventContext(self) -> TextClassificationContext: ...
    def getScores(self) -> Any: ...
    def getModelName(self) -> str: ...
    def getActionIndices(self) -> Any: ...
    def toString(self) -> str: ...
    def getExtras(self) -> Bundle: ...
    def getLocale(self) -> ULocale: ...
    def describeContents(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def getEventType(self) -> int: ...

    class TextSelectionEvent:
        CREATOR: ClassVar[Any]
        CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
        PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
        CATEGORY_CONVERSATION_ACTIONS: ClassVar[int]
        CATEGORY_LANGUAGE_DETECTION: ClassVar[int]
        CATEGORY_LINKIFY: ClassVar[int]
        CATEGORY_SELECTION: ClassVar[int]
        CREATOR: ClassVar[Any]
        TYPE_ACTIONS_GENERATED: ClassVar[int]
        TYPE_ACTIONS_SHOWN: ClassVar[int]
        TYPE_AUTO_SELECTION: ClassVar[int]
        TYPE_COPY_ACTION: ClassVar[int]
        TYPE_CUT_ACTION: ClassVar[int]
        TYPE_LINKS_GENERATED: ClassVar[int]
        TYPE_LINK_CLICKED: ClassVar[int]
        TYPE_MANUAL_REPLY: ClassVar[int]
        TYPE_OTHER_ACTION: ClassVar[int]
        TYPE_OVERTYPE: ClassVar[int]
        TYPE_PASTE_ACTION: ClassVar[int]
        TYPE_SELECTION_DESTROYED: ClassVar[int]
        TYPE_SELECTION_DRAG: ClassVar[int]
        TYPE_SELECTION_MODIFIED: ClassVar[int]
        TYPE_SELECTION_RESET: ClassVar[int]
        TYPE_SELECTION_STARTED: ClassVar[int]
        TYPE_SELECT_ALL: ClassVar[int]
        TYPE_SHARE_ACTION: ClassVar[int]
        TYPE_SMART_ACTION: ClassVar[int]
        TYPE_SMART_SELECTION_MULTI: ClassVar[int]
        TYPE_SMART_SELECTION_SINGLE: ClassVar[int]
        def getRelativeSuggestedWordEndIndex(self) -> int: ...
        def getRelativeSuggestedWordStartIndex(self) -> int: ...
        def getRelativeWordEndIndex(self) -> int: ...
        def getRelativeWordStartIndex(self) -> int: ...
        def writeToParcel(self, p0: Parcel, p1: int) -> None: ...

        class Builder:
            def __init__(self, p0: int) -> None: ...
            def setRelativeWordStartIndex(self, p0: int) -> Any: ...
            def setRelativeWordEndIndex(self, p0: int) -> Any: ...
            def setRelativeSuggestedWordStartIndex(self, p0: int) -> Any: ...
            def setRelativeSuggestedWordEndIndex(self, p0: int) -> Any: ...
            def build(self) -> Any: ...

    class TextLinkifyEvent:
        CREATOR: ClassVar[Any]
        CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
        PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
        CATEGORY_CONVERSATION_ACTIONS: ClassVar[int]
        CATEGORY_LANGUAGE_DETECTION: ClassVar[int]
        CATEGORY_LINKIFY: ClassVar[int]
        CATEGORY_SELECTION: ClassVar[int]
        CREATOR: ClassVar[Any]
        TYPE_ACTIONS_GENERATED: ClassVar[int]
        TYPE_ACTIONS_SHOWN: ClassVar[int]
        TYPE_AUTO_SELECTION: ClassVar[int]
        TYPE_COPY_ACTION: ClassVar[int]
        TYPE_CUT_ACTION: ClassVar[int]
        TYPE_LINKS_GENERATED: ClassVar[int]
        TYPE_LINK_CLICKED: ClassVar[int]
        TYPE_MANUAL_REPLY: ClassVar[int]
        TYPE_OTHER_ACTION: ClassVar[int]
        TYPE_OVERTYPE: ClassVar[int]
        TYPE_PASTE_ACTION: ClassVar[int]
        TYPE_SELECTION_DESTROYED: ClassVar[int]
        TYPE_SELECTION_DRAG: ClassVar[int]
        TYPE_SELECTION_MODIFIED: ClassVar[int]
        TYPE_SELECTION_RESET: ClassVar[int]
        TYPE_SELECTION_STARTED: ClassVar[int]
        TYPE_SELECT_ALL: ClassVar[int]
        TYPE_SHARE_ACTION: ClassVar[int]
        TYPE_SMART_ACTION: ClassVar[int]
        TYPE_SMART_SELECTION_MULTI: ClassVar[int]
        TYPE_SMART_SELECTION_SINGLE: ClassVar[int]

        class Builder:
            def __init__(self, p0: int) -> None: ...
            def build(self) -> Any: ...

    class LanguageDetectionEvent:
        CREATOR: ClassVar[Any]
        CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
        PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
        CATEGORY_CONVERSATION_ACTIONS: ClassVar[int]
        CATEGORY_LANGUAGE_DETECTION: ClassVar[int]
        CATEGORY_LINKIFY: ClassVar[int]
        CATEGORY_SELECTION: ClassVar[int]
        CREATOR: ClassVar[Any]
        TYPE_ACTIONS_GENERATED: ClassVar[int]
        TYPE_ACTIONS_SHOWN: ClassVar[int]
        TYPE_AUTO_SELECTION: ClassVar[int]
        TYPE_COPY_ACTION: ClassVar[int]
        TYPE_CUT_ACTION: ClassVar[int]
        TYPE_LINKS_GENERATED: ClassVar[int]
        TYPE_LINK_CLICKED: ClassVar[int]
        TYPE_MANUAL_REPLY: ClassVar[int]
        TYPE_OTHER_ACTION: ClassVar[int]
        TYPE_OVERTYPE: ClassVar[int]
        TYPE_PASTE_ACTION: ClassVar[int]
        TYPE_SELECTION_DESTROYED: ClassVar[int]
        TYPE_SELECTION_DRAG: ClassVar[int]
        TYPE_SELECTION_MODIFIED: ClassVar[int]
        TYPE_SELECTION_RESET: ClassVar[int]
        TYPE_SELECTION_STARTED: ClassVar[int]
        TYPE_SELECT_ALL: ClassVar[int]
        TYPE_SHARE_ACTION: ClassVar[int]
        TYPE_SMART_ACTION: ClassVar[int]
        TYPE_SMART_SELECTION_MULTI: ClassVar[int]
        TYPE_SMART_SELECTION_SINGLE: ClassVar[int]

        class Builder:
            def __init__(self, p0: int) -> None: ...
            def build(self) -> Any: ...

    class ConversationActionsEvent:
        CREATOR: ClassVar[Any]
        CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
        PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
        CATEGORY_CONVERSATION_ACTIONS: ClassVar[int]
        CATEGORY_LANGUAGE_DETECTION: ClassVar[int]
        CATEGORY_LINKIFY: ClassVar[int]
        CATEGORY_SELECTION: ClassVar[int]
        CREATOR: ClassVar[Any]
        TYPE_ACTIONS_GENERATED: ClassVar[int]
        TYPE_ACTIONS_SHOWN: ClassVar[int]
        TYPE_AUTO_SELECTION: ClassVar[int]
        TYPE_COPY_ACTION: ClassVar[int]
        TYPE_CUT_ACTION: ClassVar[int]
        TYPE_LINKS_GENERATED: ClassVar[int]
        TYPE_LINK_CLICKED: ClassVar[int]
        TYPE_MANUAL_REPLY: ClassVar[int]
        TYPE_OTHER_ACTION: ClassVar[int]
        TYPE_OVERTYPE: ClassVar[int]
        TYPE_PASTE_ACTION: ClassVar[int]
        TYPE_SELECTION_DESTROYED: ClassVar[int]
        TYPE_SELECTION_DRAG: ClassVar[int]
        TYPE_SELECTION_MODIFIED: ClassVar[int]
        TYPE_SELECTION_RESET: ClassVar[int]
        TYPE_SELECTION_STARTED: ClassVar[int]
        TYPE_SELECT_ALL: ClassVar[int]
        TYPE_SHARE_ACTION: ClassVar[int]
        TYPE_SMART_ACTION: ClassVar[int]
        TYPE_SMART_SELECTION_MULTI: ClassVar[int]
        TYPE_SMART_SELECTION_SINGLE: ClassVar[int]

        class Builder:
            def __init__(self, p0: int) -> None: ...
            def build(self) -> Any: ...

    class Builder:
        def setEntityTypes(self, p0: Any) -> Any: ...
        def setEventContext(self, p0: TextClassificationContext) -> Any: ...
        def setResultId(self, p0: str) -> Any: ...
        def setEventIndex(self, p0: int) -> Any: ...
        def setScores(self, p0: Any) -> Any: ...
        def setModelName(self, p0: str) -> Any: ...
        def setActionIndices(self, p0: Any) -> Any: ...
        def setExtras(self, p0: Bundle) -> Any: ...
        def setLocale(self, p0: ULocale) -> Any: ...
