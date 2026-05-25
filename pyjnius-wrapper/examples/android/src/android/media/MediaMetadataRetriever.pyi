from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.graphics.Bitmap import Bitmap
from android.media.MediaDataSource import MediaDataSource
from android.net.Uri import Uri
from java.io.FileDescriptor import FileDescriptor

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Config:
    """Forward declaration for ``android.graphics.Bitmap.Config``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.graphics.Bitmap.Config')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/graphics/Bitmap/Config
    """
    ...

class MediaMetadataRetriever:
    METADATA_KEY_ALBUM: ClassVar[int]
    METADATA_KEY_ALBUMARTIST: ClassVar[int]
    METADATA_KEY_ARTIST: ClassVar[int]
    METADATA_KEY_AUTHOR: ClassVar[int]
    METADATA_KEY_BITRATE: ClassVar[int]
    METADATA_KEY_BITS_PER_SAMPLE: ClassVar[int]
    METADATA_KEY_CAPTURE_FRAMERATE: ClassVar[int]
    METADATA_KEY_CD_TRACK_NUMBER: ClassVar[int]
    METADATA_KEY_COLOR_RANGE: ClassVar[int]
    METADATA_KEY_COLOR_STANDARD: ClassVar[int]
    METADATA_KEY_COLOR_TRANSFER: ClassVar[int]
    METADATA_KEY_COMPILATION: ClassVar[int]
    METADATA_KEY_COMPOSER: ClassVar[int]
    METADATA_KEY_DATE: ClassVar[int]
    METADATA_KEY_DISC_NUMBER: ClassVar[int]
    METADATA_KEY_DURATION: ClassVar[int]
    METADATA_KEY_EXIF_LENGTH: ClassVar[int]
    METADATA_KEY_EXIF_OFFSET: ClassVar[int]
    METADATA_KEY_GENRE: ClassVar[int]
    METADATA_KEY_HAS_AUDIO: ClassVar[int]
    METADATA_KEY_HAS_IMAGE: ClassVar[int]
    METADATA_KEY_HAS_VIDEO: ClassVar[int]
    METADATA_KEY_IMAGE_COUNT: ClassVar[int]
    METADATA_KEY_IMAGE_HEIGHT: ClassVar[int]
    METADATA_KEY_IMAGE_PRIMARY: ClassVar[int]
    METADATA_KEY_IMAGE_ROTATION: ClassVar[int]
    METADATA_KEY_IMAGE_WIDTH: ClassVar[int]
    METADATA_KEY_LOCATION: ClassVar[int]
    METADATA_KEY_MIMETYPE: ClassVar[int]
    METADATA_KEY_NUM_TRACKS: ClassVar[int]
    METADATA_KEY_SAMPLERATE: ClassVar[int]
    METADATA_KEY_TITLE: ClassVar[int]
    METADATA_KEY_VIDEO_FRAME_COUNT: ClassVar[int]
    METADATA_KEY_VIDEO_HEIGHT: ClassVar[int]
    METADATA_KEY_VIDEO_ROTATION: ClassVar[int]
    METADATA_KEY_VIDEO_WIDTH: ClassVar[int]
    METADATA_KEY_WRITER: ClassVar[int]
    METADATA_KEY_XMP_LENGTH: ClassVar[int]
    METADATA_KEY_XMP_OFFSET: ClassVar[int]
    METADATA_KEY_YEAR: ClassVar[int]
    OPTION_CLOSEST: ClassVar[int]
    OPTION_CLOSEST_SYNC: ClassVar[int]
    OPTION_NEXT_SYNC: ClassVar[int]
    OPTION_PREVIOUS_SYNC: ClassVar[int]
    def __init__(self) -> None: ...
    @overload
    def setDataSource(self, arg0: str) -> None: ...
    @overload
    def setDataSource(self, arg0: str, arg1: dict) -> None: ...
    @overload
    def setDataSource(self, arg0: FileDescriptor, arg1: int, arg2: int) -> None: ...
    @overload
    def setDataSource(self, arg0: FileDescriptor) -> None: ...
    @overload
    def setDataSource(self, arg0: Context, arg1: Uri) -> None: ...
    @overload
    def setDataSource(self, arg0: MediaDataSource) -> None: ...
    def extractMetadata(self, arg0: int) -> str: ...
    @overload
    def getFrameAtTime(self, arg0: int, arg1: int) -> Bitmap: ...
    @overload
    def getFrameAtTime(self, arg0: int, arg1: int, arg2: "BitmapParams") -> Bitmap: ...
    @overload
    def getFrameAtTime(self, arg0: int) -> Bitmap: ...
    @overload
    def getFrameAtTime(self) -> Bitmap: ...
    @overload
    def getScaledFrameAtTime(self, arg0: int, arg1: int, arg2: int, arg3: int) -> Bitmap: ...
    @overload
    def getScaledFrameAtTime(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: "BitmapParams") -> Bitmap: ...
    @overload
    def getFrameAtIndex(self, arg0: int, arg1: "BitmapParams") -> Bitmap: ...
    @overload
    def getFrameAtIndex(self, arg0: int) -> Bitmap: ...
    @overload
    def getFramesAtIndex(self, arg0: int, arg1: int, arg2: "BitmapParams") -> list: ...
    @overload
    def getFramesAtIndex(self, arg0: int, arg1: int) -> list: ...
    @overload
    def getImageAtIndex(self, arg0: int, arg1: "BitmapParams") -> Bitmap: ...
    @overload
    def getImageAtIndex(self, arg0: int) -> Bitmap: ...
    @overload
    def getPrimaryImage(self, arg0: "BitmapParams") -> Bitmap: ...
    @overload
    def getPrimaryImage(self) -> Bitmap: ...
    def getEmbeddedPicture(self) -> list[int]: ...
    def close(self) -> None: ...
    def release(self) -> None: ...
    def finalize(self) -> None: ...

    class BitmapParams:
        def __init__(self) -> None: ...
        def setPreferredConfig(self, arg0: Config) -> None: ...
        def getPreferredConfig(self) -> Config: ...
        def getActualConfig(self) -> Config: ...
