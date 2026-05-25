from typing import Any, ClassVar, overload
from android.os.Bundle import Bundle
from android.os.Parcel import Parcel
from java.lang.Exception import Exception

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

class PlaybackErrorEvent:
    CREATOR: ClassVar[Creator]
    ERROR_AUDIO_TRACK_INIT_FAILED: ClassVar[int]
    ERROR_AUDIO_TRACK_OTHER: ClassVar[int]
    ERROR_AUDIO_TRACK_WRITE_FAILED: ClassVar[int]
    ERROR_DECODER_INIT_FAILED: ClassVar[int]
    ERROR_DECODING_FAILED: ClassVar[int]
    ERROR_DECODING_FORMAT_EXCEEDS_CAPABILITIES: ClassVar[int]
    ERROR_DECODING_FORMAT_UNSUPPORTED: ClassVar[int]
    ERROR_DECODING_OTHER: ClassVar[int]
    ERROR_DRM_CONTENT_ERROR: ClassVar[int]
    ERROR_DRM_DEVICE_REVOKED: ClassVar[int]
    ERROR_DRM_DISALLOWED_OPERATION: ClassVar[int]
    ERROR_DRM_LICENSE_ACQUISITION_FAILED: ClassVar[int]
    ERROR_DRM_OTHER: ClassVar[int]
    ERROR_DRM_PROVISIONING_FAILED: ClassVar[int]
    ERROR_DRM_SCHEME_UNSUPPORTED: ClassVar[int]
    ERROR_DRM_SYSTEM_ERROR: ClassVar[int]
    ERROR_IO_BAD_HTTP_STATUS: ClassVar[int]
    ERROR_IO_CONNECTION_CLOSED: ClassVar[int]
    ERROR_IO_CONNECTION_TIMEOUT: ClassVar[int]
    ERROR_IO_DNS_FAILED: ClassVar[int]
    ERROR_IO_FILE_NOT_FOUND: ClassVar[int]
    ERROR_IO_NETWORK_CONNECTION_FAILED: ClassVar[int]
    ERROR_IO_NETWORK_UNAVAILABLE: ClassVar[int]
    ERROR_IO_NO_PERMISSION: ClassVar[int]
    ERROR_IO_OTHER: ClassVar[int]
    ERROR_OTHER: ClassVar[int]
    ERROR_PARSING_CONTAINER_MALFORMED: ClassVar[int]
    ERROR_PARSING_CONTAINER_UNSUPPORTED: ClassVar[int]
    ERROR_PARSING_MANIFEST_MALFORMED: ClassVar[int]
    ERROR_PARSING_MANIFEST_UNSUPPORTED: ClassVar[int]
    ERROR_PARSING_OTHER: ClassVar[int]
    ERROR_PLAYER_BEHIND_LIVE_WINDOW: ClassVar[int]
    ERROR_PLAYER_OTHER: ClassVar[int]
    ERROR_PLAYER_REMOTE: ClassVar[int]
    ERROR_RUNTIME: ClassVar[int]
    ERROR_UNKNOWN: ClassVar[int]
    def getErrorCode(self) -> int: ...
    def getSubErrorCode(self) -> int: ...
    def getTimeSinceCreatedMillis(self) -> int: ...
    def getMetricsBundle(self) -> Bundle: ...
    def toString(self) -> str: ...
    def equals(self, arg0: Any) -> bool: ...
    def hashCode(self) -> int: ...
    def writeToParcel(self, arg0: Parcel, arg1: int) -> None: ...
    def describeContents(self) -> int: ...

    class Builder:
        def __init__(self) -> None: ...
        def setException(self, arg0: Exception) -> "Builder": ...
        def setErrorCode(self, arg0: int) -> "Builder": ...
        def setSubErrorCode(self, arg0: int) -> "Builder": ...
        def setTimeSinceCreatedMillis(self, arg0: int) -> "Builder": ...
        def setMetricsBundle(self, arg0: Bundle) -> "Builder": ...
        def build(self) -> "PlaybackErrorEvent": ...
