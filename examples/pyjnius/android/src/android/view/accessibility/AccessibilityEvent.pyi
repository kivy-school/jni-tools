from typing import Any, ClassVar, overload
from android.os.Parcel import Parcel
from android.view.accessibility.AccessibilityRecord import AccessibilityRecord

class AccessibilityEvent:
    CONTENT_CHANGE_TYPE_CHECKED: ClassVar[int]
    CONTENT_CHANGE_TYPE_CONTENT_DESCRIPTION: ClassVar[int]
    CONTENT_CHANGE_TYPE_CONTENT_INVALID: ClassVar[int]
    CONTENT_CHANGE_TYPE_DRAG_CANCELLED: ClassVar[int]
    CONTENT_CHANGE_TYPE_DRAG_DROPPED: ClassVar[int]
    CONTENT_CHANGE_TYPE_DRAG_STARTED: ClassVar[int]
    CONTENT_CHANGE_TYPE_ENABLED: ClassVar[int]
    CONTENT_CHANGE_TYPE_ERROR: ClassVar[int]
    CONTENT_CHANGE_TYPE_EXPANDED: ClassVar[int]
    CONTENT_CHANGE_TYPE_PANE_APPEARED: ClassVar[int]
    CONTENT_CHANGE_TYPE_PANE_DISAPPEARED: ClassVar[int]
    CONTENT_CHANGE_TYPE_PANE_TITLE: ClassVar[int]
    CONTENT_CHANGE_TYPE_STATE_DESCRIPTION: ClassVar[int]
    CONTENT_CHANGE_TYPE_SUBTREE: ClassVar[int]
    CONTENT_CHANGE_TYPE_SUPPLEMENTAL_DESCRIPTION: ClassVar[int]
    CONTENT_CHANGE_TYPE_TEXT: ClassVar[int]
    CONTENT_CHANGE_TYPE_UNDEFINED: ClassVar[int]
    CREATOR: ClassVar[Any]
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
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    @overload
    def __init__(self, p0: int) -> None: ...
    @overload
    def __init__(self, p0: "AccessibilityEvent") -> None: ...
    @overload
    def __init__(self) -> None: ...
    def toString(self) -> str: ...
    def getPackageName(self) -> str: ...
    def isAccessibilityDataSensitive(self) -> bool: ...
    def setAccessibilityDataSensitive(self, p0: bool) -> None: ...
    def setPackageName(self, p0: str) -> None: ...
    def setAction(self, p0: int) -> None: ...
    def getAction(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...
    def recycle(self) -> None: ...
    @overload
    @staticmethod
    def obtain(p0: int) -> "AccessibilityEvent": ...
    @overload
    @staticmethod
    def obtain() -> "AccessibilityEvent": ...
    @overload
    @staticmethod
    def obtain(p0: "AccessibilityEvent") -> "AccessibilityEvent": ...
    def getEventTime(self) -> int: ...
    def setEventTime(self, p0: int) -> None: ...
    def getEventType(self) -> int: ...
    def setEventType(self, p0: int) -> None: ...
    def initFromParcel(self, p0: Parcel) -> None: ...
    def getWindowChanges(self) -> int: ...
    def getRecord(self, p0: int) -> AccessibilityRecord: ...
    def getRecordCount(self) -> int: ...
    @staticmethod
    def eventTypeToString(p0: int) -> str: ...
    def appendRecord(self, p0: AccessibilityRecord) -> None: ...
    def getContentChangeTypes(self) -> int: ...
    def getMovementGranularity(self) -> int: ...
    def getSpeechStateChangeTypes(self) -> int: ...
    def setContentChangeTypes(self, p0: int) -> None: ...
    def setMovementGranularity(self, p0: int) -> None: ...
    def setSpeechStateChangeTypes(self, p0: int) -> None: ...
