from typing import Any, ClassVar, overload
from android.os.Bundle import Bundle
from android.os.Parcel import Parcel
from java.lang.Exception import Exception

class PlaybackErrorEvent:
    CREATOR: ClassVar[Any]
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
    CONTENTS_FILE_DESCRIPTOR: ClassVar[int]
    PARCELABLE_WRITE_RETURN_VALUE: ClassVar[int]
    def getMetricsBundle(self) -> Bundle: ...
    def getSubErrorCode(self) -> int: ...
    def getTimeSinceCreatedMillis(self) -> int: ...
    def equals(self, p0: Any) -> bool: ...
    def toString(self) -> str: ...
    def hashCode(self) -> int: ...
    def writeToParcel(self, p0: Parcel, p1: int) -> None: ...
    def describeContents(self) -> int: ...
    def getErrorCode(self) -> int: ...

    class Builder:
        def __init__(self) -> None: ...
        def setMetricsBundle(self, p0: Bundle) -> Any: ...
        def setException(self, p0: Exception) -> Any: ...
        def setSubErrorCode(self, p0: int) -> Any: ...
        def setErrorCode(self, p0: int) -> Any: ...
        def setTimeSinceCreatedMillis(self, p0: int) -> Any: ...
        def build(self) -> "PlaybackErrorEvent": ...
