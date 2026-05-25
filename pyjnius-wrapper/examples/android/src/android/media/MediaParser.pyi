from typing import Any, ClassVar, overload
from android.media.DrmInitData import DrmInitData
from android.media.MediaFormat import MediaFormat
from android.media.metrics.LogSessionId import LogSessionId
from android.util.Pair import Pair

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class CryptoInfo:
    """Forward declaration for ``android.media.MediaCodec.CryptoInfo``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.media.MediaCodec.CryptoInfo')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/media/MediaCodec/CryptoInfo
    """
    ...

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
    @staticmethod
    def createByName(arg0: str, arg1: "OutputConsumer") -> "MediaParser": ...
    @staticmethod
    def create(arg0: "OutputConsumer", *arg1: str) -> "MediaParser": ...
    @staticmethod
    def getParserNames(arg0: MediaFormat) -> list: ...
    def setParameter(self, arg0: str, arg1: Any) -> "MediaParser": ...
    def supportsParameter(self, arg0: str) -> bool: ...
    def getParserName(self) -> str: ...
    def advance(self, arg0: "SeekableInputReader") -> bool: ...
    def seek(self, arg0: "SeekPoint") -> None: ...
    def release(self) -> None: ...
    def setLogSessionId(self, arg0: LogSessionId) -> None: ...
    def getLogSessionId(self) -> LogSessionId: ...

    class InputReader:
        def read(self, arg0: list[int], arg1: int, arg2: int) -> int: ...
        def getPosition(self) -> int: ...
        def getLength(self) -> int: ...

    class OutputConsumer:
        def onSeekMapFound(self, arg0: "SeekMap") -> None: ...
        def onTrackCountFound(self, arg0: int) -> None: ...
        def onTrackDataFound(self, arg0: int, arg1: "TrackData") -> None: ...
        def onSampleDataFound(self, arg0: int, arg1: "InputReader") -> None: ...
        def onSampleCompleted(self, arg0: int, arg1: int, arg2: int, arg3: int, arg4: int, arg5: CryptoInfo) -> None: ...

    class ParsingException:
        ...

    class SeekMap:
        UNKNOWN_DURATION: ClassVar[int]
        def isSeekable(self) -> bool: ...
        def getDurationMicros(self) -> int: ...
        def getSeekPoints(self, arg0: int) -> Pair: ...

    class SeekPoint:
        START: ClassVar["SeekPoint"]
        position: int
        timeMicros: int
        def toString(self) -> str: ...
        def equals(self, arg0: Any) -> bool: ...
        def hashCode(self) -> int: ...

    class SeekableInputReader:
        def seekToPosition(self, arg0: int) -> None: ...

    class TrackData:
        drmInitData: DrmInitData
        mediaFormat: MediaFormat

    class UnrecognizedInputFormatException:
        ...
