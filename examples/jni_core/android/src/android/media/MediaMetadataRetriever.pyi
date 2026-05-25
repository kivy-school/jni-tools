from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.graphics.Bitmap import Bitmap
from android.media.MediaDataSource import MediaDataSource
from android.net.Uri import Uri
from java.io.FileDescriptor import FileDescriptor

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
    def setDataSource(self, p0: Context, p1: Uri) -> None: ...
    @overload
    def setDataSource(self, p0: FileDescriptor) -> None: ...
    @overload
    def setDataSource(self, p0: FileDescriptor, p1: int, p2: int) -> None: ...
    @overload
    def setDataSource(self, p0: MediaDataSource) -> None: ...
    @overload
    def setDataSource(self, p0: str) -> None: ...
    @overload
    def setDataSource(self, p0: str, p1: dict) -> None: ...
    def extractMetadata(self, p0: int) -> str: ...
    @overload
    def getFrameAtTime(self, p0: int, p1: int, p2: Any) -> Bitmap: ...
    @overload
    def getFrameAtTime(self, p0: int) -> Bitmap: ...
    @overload
    def getFrameAtTime(self, p0: int, p1: int) -> Bitmap: ...
    @overload
    def getFrameAtTime(self) -> Bitmap: ...
    @overload
    def getScaledFrameAtTime(self, p0: int, p1: int, p2: int, p3: int, p4: Any) -> Bitmap: ...
    @overload
    def getScaledFrameAtTime(self, p0: int, p1: int, p2: int, p3: int) -> Bitmap: ...
    @overload
    def getFrameAtIndex(self, p0: int) -> Bitmap: ...
    @overload
    def getFrameAtIndex(self, p0: int, p1: Any) -> Bitmap: ...
    @overload
    def getFramesAtIndex(self, p0: int, p1: int) -> list: ...
    @overload
    def getFramesAtIndex(self, p0: int, p1: int, p2: Any) -> list: ...
    @overload
    def getImageAtIndex(self, p0: int) -> Bitmap: ...
    @overload
    def getImageAtIndex(self, p0: int, p1: Any) -> Bitmap: ...
    @overload
    def getPrimaryImage(self) -> Bitmap: ...
    @overload
    def getPrimaryImage(self, p0: Any) -> Bitmap: ...
    def getEmbeddedPicture(self) -> Any: ...
    def release(self) -> None: ...
    def close(self) -> None: ...

    class BitmapParams:
        def __init__(self) -> None: ...
        def getPreferredConfig(self) -> Any: ...
        def setPreferredConfig(self, p0: Any) -> None: ...
        def getActualConfig(self) -> Any: ...
