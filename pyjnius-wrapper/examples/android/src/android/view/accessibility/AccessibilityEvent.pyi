from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.view.accessibility.AccessibilityRecord import AccessibilityRecord

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

class AccessibilityEvent:
    CONTENT_CHANGE_TYPE_CONTENT_DESCRIPTION: ClassVar[int]
    CONTENT_CHANGE_TYPE_CONTENT_INVALID: ClassVar[int]
    CONTENT_CHANGE_TYPE_DRAG_CANCELLED: ClassVar[int]
    CONTENT_CHANGE_TYPE_DRAG_DROPPED: ClassVar[int]
    CONTENT_CHANGE_TYPE_DRAG_STARTED: ClassVar[int]
    CONTENT_CHANGE_TYPE_ENABLED: ClassVar[int]
    CONTENT_CHANGE_TYPE_ERROR: ClassVar[int]
    CONTENT_CHANGE_TYPE_PANE_APPEARED: ClassVar[int]
    CONTENT_CHANGE_TYPE_PANE_DISAPPEARED: ClassVar[int]
    CONTENT_CHANGE_TYPE_PANE_TITLE: ClassVar[int]
    CONTENT_CHANGE_TYPE_STATE_DESCRIPTION: ClassVar[int]
    CONTENT_CHANGE_TYPE_SUBTREE: ClassVar[int]
    CONTENT_CHANGE_TYPE_TEXT: ClassVar[int]
    CONTENT_CHANGE_TYPE_UNDEFINED: ClassVar[int]
    CREATOR: ClassVar[Creator]
    INVALID_POSITION: ClassVar[int]
    MAX_TEXT_LENGTH: ClassVar[int]
    SPEECH_STATE_LISTENING_END: ClassVar[int]
    SPEECH_STATE_LISTENING_START: ClassVar[int]
    SPEECH_STATE_SPEAKING_END: ClassVar[int]
    SPEECH_STATE_SPEAKING_START: ClassVar[int]
    TYPES_ALL_MASK: ClassVar[int]
    TYPE_ANNOUNCEMENT: ClassVar[int]
    TYPE_ASSIST_READING_CONTEXT: ClassVar[int]
    TYPE_GESTURE_DETECTION_END: ClassVar[int]
    TYPE_GESTURE_DETECTION_START: ClassVar[int]
    TYPE_NOTIFICATION_STATE_CHANGED: ClassVar[int]
    TYPE_SPEECH_STATE_CHANGE: ClassVar[int]
    TYPE_TOUCH_EXPLORATION_GESTURE_END: ClassVar[int]
    TYPE_TOUCH_EXPLORATION_GESTURE_START: ClassVar[int]
    TYPE_TOUCH_INTERACTION_END: ClassVar[int]
    TYPE_TOUCH_INTERACTION_START: ClassVar[int]
    TYPE_VIEW_ACCESSIBILITY_FOCUSED: ClassVar[int]
    TYPE_VIEW_ACCESSIBILITY_FOCUS_CLEARED: ClassVar[int]
    TYPE_VIEW_CLICKED: ClassVar[int]
    TYPE_VIEW_CONTEXT_CLICKED: ClassVar[int]
    TYPE_VIEW_FOCUSED: ClassVar[int]
    TYPE_VIEW_HOVER_ENTER: ClassVar[int]
    TYPE_VIEW_HOVER_EXIT: ClassVar[int]
    TYPE_VIEW_LONG_CLICKED: ClassVar[int]
    TYPE_VIEW_SCROLLED: ClassVar[int]
    TYPE_VIEW_SELECTED: ClassVar[int]
    TYPE_VIEW_TARGETED_BY_SCROLL: ClassVar[int]
    TYPE_VIEW_TEXT_CHANGED: ClassVar[int]
    TYPE_VIEW_TEXT_SELECTION_CHANGED: ClassVar[int]
    TYPE_VIEW_TEXT_TRAVERSED_AT_MOVEMENT_GRANULARITY: ClassVar[int]
    TYPE_WINDOWS_CHANGED: ClassVar[int]
    TYPE_WINDOW_CONTENT_CHANGED: ClassVar[int]
    TYPE_WINDOW_STATE_CHANGED: ClassVar[int]
    WINDOWS_CHANGE_ACCESSIBILITY_FOCUSED: ClassVar[int]
    WINDOWS_CHANGE_ACTIVE: ClassVar[int]
    WINDOWS_CHANGE_ADDED: ClassVar[int]
    WINDOWS_CHANGE_BOUNDS: ClassVar[int]
    WINDOWS_CHANGE_CHILDREN: ClassVar[int]
    WINDOWS_CHANGE_FOCUSED: ClassVar[int]
    WINDOWS_CHANGE_LAYER: ClassVar[int]
    WINDOWS_CHANGE_PARENT: ClassVar[int]
    WINDOWS_CHANGE_PIP: ClassVar[int]
    WINDOWS_CHANGE_REMOVED: ClassVar[int]
    WINDOWS_CHANGE_TITLE: ClassVar[int]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, arg0: int) -> None: ...
    @overload
    def __init__(self, arg0: "AccessibilityEvent") -> None: ...
    def getRecordCount(self) -> int: ...
    def appendRecord(self, arg0: AccessibilityRecord) -> None: ...
    def getRecord(self, arg0: int) -> AccessibilityRecord: ...
    def getEventType(self) -> int: ...
    def getContentChangeTypes(self) -> int: ...
    def setContentChangeTypes(self, arg0: int) -> None: ...
    def isAccessibilityDataSensitive(self) -> bool: ...
    def setAccessibilityDataSensitive(self, arg0: bool) -> None: ...
    def getSpeechStateChangeTypes(self) -> int: ...
    def setSpeechStateChangeTypes(self, arg0: int) -> None: ...
    def getWindowChanges(self) -> int: ...
    def setEventType(self, arg0: int) -> None: ...
    def getEventTime(self) -> int: ...
    def setEventTime(self, arg0: int) -> None: ...
    def getPackageName(self) -> str: ...
    def setPackageName(self, arg0: str) -> None: ...
    def setMovementGranularity(self, arg0: int) -> None: ...
    def getMovementGranularity(self) -> int: ...
    def setAction(self, arg0: int) -> None: ...
    def getAction(self) -> int: ...
    @overload
    @staticmethod
    def obtain(arg0: int) -> "AccessibilityEvent": ...
    @overload
    @staticmethod
    def obtain(arg0: "AccessibilityEvent") -> "AccessibilityEvent": ...
    @overload
    @staticmethod
    def obtain() -> "AccessibilityEvent": ...
    def recycle(self) -> None: ...
    def initFromParcel(self, arg0: Parcel) -> None: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def describeContents(self) -> int: ...
    def toString(self) -> str: ...
    @staticmethod
    def eventTypeToString(arg0: int) -> str: ...
