from typing import Any, ClassVar, overload
from android.media.DrmInitData import DrmInitData
from android.media.MediaFormat import MediaFormat
from android.media.metrics.LogSessionId import LogSessionId
from android.util.Pair import Pair

class MediaParser:
    PARAMETER_ADTS_ENABLE_CBR_SEEKING: ClassVar[str]
    PARAMETER_AMR_ENABLE_CBR_SEEKING: ClassVar[str]
    PARAMETER_FLAC_DISABLE_ID3: ClassVar[str]
    PARAMETER_MATROSKA_DISABLE_CUES_SEEKING: ClassVar[str]
    PARAMETER_MP3_DISABLE_ID3: ClassVar[str]
    PARAMETER_MP3_ENABLE_CBR_SEEKING: ClassVar[str]
    PARAMETER_MP3_ENABLE_INDEX_SEEKING: ClassVar[str]
    PARAMETER_MP4_IGNORE_EDIT_LISTS: ClassVar[str]
    PARAMETER_MP4_IGNORE_TFDT_BOX: ClassVar[str]
    PARAMETER_MP4_TREAT_VIDEO_FRAMES_AS_KEYFRAMES: ClassVar[str]
    PARAMETER_TS_ALLOW_NON_IDR_AVC_KEYFRAMES: ClassVar[str]
    PARAMETER_TS_DETECT_ACCESS_UNITS: ClassVar[str]
    PARAMETER_TS_ENABLE_HDMV_DTS_AUDIO_STREAMS: ClassVar[str]
    PARAMETER_TS_IGNORE_AAC_STREAM: ClassVar[str]
    PARAMETER_TS_IGNORE_AVC_STREAM: ClassVar[str]
    PARAMETER_TS_IGNORE_SPLICE_INFO_STREAM: ClassVar[str]
    PARAMETER_TS_MODE: ClassVar[str]
    PARSER_NAME_AC3: ClassVar[str]
    PARSER_NAME_AC4: ClassVar[str]
    PARSER_NAME_ADTS: ClassVar[str]
    PARSER_NAME_AMR: ClassVar[str]
    PARSER_NAME_FLAC: ClassVar[str]
    PARSER_NAME_FLV: ClassVar[str]
    PARSER_NAME_FMP4: ClassVar[str]
    PARSER_NAME_MATROSKA: ClassVar[str]
    PARSER_NAME_MP3: ClassVar[str]
    PARSER_NAME_MP4: ClassVar[str]
    PARSER_NAME_OGG: ClassVar[str]
    PARSER_NAME_PS: ClassVar[str]
    PARSER_NAME_TS: ClassVar[str]
    PARSER_NAME_UNKNOWN: ClassVar[str]
    PARSER_NAME_WAV: ClassVar[str]
    SAMPLE_FLAG_DECODE_ONLY: ClassVar[int]
    SAMPLE_FLAG_ENCRYPTED: ClassVar[int]
    SAMPLE_FLAG_HAS_SUPPLEMENTAL_DATA: ClassVar[int]
    SAMPLE_FLAG_KEY_FRAME: ClassVar[int]
    SAMPLE_FLAG_LAST_SAMPLE: ClassVar[int]
    def getLogSessionId(self) -> LogSessionId: ...
    def setLogSessionId(self, p0: LogSessionId) -> None: ...
    @staticmethod
    def createByName(p0: str, p1: Any) -> "MediaParser": ...
    def getParserName(self) -> str: ...
    @staticmethod
    def getParserNames(p0: MediaFormat) -> list: ...
    def supportsParameter(self, p0: str) -> bool: ...
    @staticmethod
    def create(p0: Any, p1: Any) -> "MediaParser": ...
    def release(self) -> None: ...
    def advance(self, p0: Any) -> bool: ...
    def setParameter(self, p0: str, p1: Any) -> "MediaParser": ...
    def seek(self, p0: Any) -> None: ...

    class UnrecognizedInputFormatException:
        ...

    class TrackData:
        drmInitData: DrmInitData
        mediaFormat: MediaFormat

    class SeekableInputReader:
        def seekToPosition(self, p0: int) -> None: ...

    class SeekPoint:
        START: ClassVar[Any]
        position: int
        timeMicros: int
        def equals(self, p0: Any) -> bool: ...
        def toString(self) -> str: ...
        def hashCode(self) -> int: ...

    class SeekMap:
        UNKNOWN_DURATION: ClassVar[int]
        def getDurationMicros(self) -> int: ...
        def getSeekPoints(self, p0: int) -> Pair: ...
        def isSeekable(self) -> bool: ...

    class ParsingException:
        ...

    class OutputConsumer:
        def onSampleCompleted(self, p0: int, p1: int, p2: int, p3: int, p4: int, p5: Any) -> None: ...
        def onSampleDataFound(self, p0: int, p1: Any) -> None: ...
        def onSeekMapFound(self, p0: Any) -> None: ...
        def onTrackCountFound(self, p0: int) -> None: ...
        def onTrackDataFound(self, p0: int, p1: Any) -> None: ...

    class InputReader:
        def getLength(self) -> int: ...
        def read(self, p0: Any, p1: int, p2: int) -> int: ...
        def getPosition(self) -> int: ...
