from typing import Any, ClassVar, overload
from android.os.Bundle import Bundle
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

class PlaybackStateEvent:
    CREATOR: ClassVar[Creator]
    STATE_ABANDONED: ClassVar[int]
    STATE_BUFFERING: ClassVar[int]
    STATE_ENDED: ClassVar[int]
    STATE_FAILED: ClassVar[int]
    STATE_INTERRUPTED_BY_AD: ClassVar[int]
    STATE_JOINING_BACKGROUND: ClassVar[int]
    STATE_JOINING_FOREGROUND: ClassVar[int]
    STATE_NOT_STARTED: ClassVar[int]
    STATE_PAUSED: ClassVar[int]
    STATE_PAUSED_BUFFERING: ClassVar[int]
    STATE_PLAYING: ClassVar[int]
    STATE_SEEKING: ClassVar[int]
    STATE_STOPPED: ClassVar[int]
    STATE_SUPPRESSED: ClassVar[int]
    STATE_SUPPRESSED_BUFFERING: ClassVar[int]
    def getState(self) -> int: ...
    def getTimeSinceCreatedMillis(self) -> int: ...
    def getMetricsBundle(self) -> Bundle: ...
    def equals(self, arg0: Any) -> bool: ...
    def hashCode(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def describeContents(self) -> int: ...

    class Builder:
        def __init__(self) -> None: ...
        def setState(self, arg0: int) -> "Builder": ...
        def setTimeSinceCreatedMillis(self, arg0: int) -> "Builder": ...
        def setMetricsBundle(self, arg0: Bundle) -> "Builder": ...
        def build(self) -> "PlaybackStateEvent": ...
