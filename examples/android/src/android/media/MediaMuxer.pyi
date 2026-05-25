from typing import Any, ClassVar, overload
from android.media.MediaFormat import MediaFormat
from java.io.FileDescriptor import FileDescriptor
from java.nio.ByteBuffer import ByteBuffer

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class BufferInfo:
    """Forward declaration for ``android.media.MediaCodec.BufferInfo``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.media.MediaCodec.BufferInfo')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/media/MediaCodec/BufferInfo
    """
    ...

class MediaMuxer:
    @overload
    def __init__(self, arg0: str, arg1: int) -> None: ...
    @overload
    def __init__(self, arg0: FileDescriptor, arg1: int) -> None: ...
    def setOrientationHint(self, arg0: int) -> None: ...
    def setLocation(self, arg0: float, arg1: float) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def finalize(self) -> None: ...
    def addTrack(self, arg0: MediaFormat) -> int: ...
    def writeSampleData(self, arg0: int, arg1: ByteBuffer, arg2: BufferInfo) -> None: ...
    def release(self) -> None: ...

    class OutputFormat:
        MUXER_OUTPUT_3GPP: ClassVar[int]
        MUXER_OUTPUT_HEIF: ClassVar[int]
        MUXER_OUTPUT_MPEG_4: ClassVar[int]
        MUXER_OUTPUT_OGG: ClassVar[int]
        MUXER_OUTPUT_WEBM: ClassVar[int]
