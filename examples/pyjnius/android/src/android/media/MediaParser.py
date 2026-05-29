from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaParser"]

class MediaParser(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaParser"
    PARAMETER_ADTS_ENABLE_CBR_SEEKING = JavaStaticField("Ljava/lang/String;")
    PARAMETER_AMR_ENABLE_CBR_SEEKING = JavaStaticField("Ljava/lang/String;")
    PARAMETER_FLAC_DISABLE_ID3 = JavaStaticField("Ljava/lang/String;")
    PARAMETER_MATROSKA_DISABLE_CUES_SEEKING = JavaStaticField("Ljava/lang/String;")
    PARAMETER_MP3_DISABLE_ID3 = JavaStaticField("Ljava/lang/String;")
    PARAMETER_MP3_ENABLE_CBR_SEEKING = JavaStaticField("Ljava/lang/String;")
    PARAMETER_MP3_ENABLE_INDEX_SEEKING = JavaStaticField("Ljava/lang/String;")
    PARAMETER_MP4_IGNORE_EDIT_LISTS = JavaStaticField("Ljava/lang/String;")
    PARAMETER_MP4_IGNORE_TFDT_BOX = JavaStaticField("Ljava/lang/String;")
    PARAMETER_MP4_TREAT_VIDEO_FRAMES_AS_KEYFRAMES = JavaStaticField("Ljava/lang/String;")
    PARAMETER_TS_ALLOW_NON_IDR_AVC_KEYFRAMES = JavaStaticField("Ljava/lang/String;")
    PARAMETER_TS_DETECT_ACCESS_UNITS = JavaStaticField("Ljava/lang/String;")
    PARAMETER_TS_ENABLE_HDMV_DTS_AUDIO_STREAMS = JavaStaticField("Ljava/lang/String;")
    PARAMETER_TS_IGNORE_AAC_STREAM = JavaStaticField("Ljava/lang/String;")
    PARAMETER_TS_IGNORE_AVC_STREAM = JavaStaticField("Ljava/lang/String;")
    PARAMETER_TS_IGNORE_SPLICE_INFO_STREAM = JavaStaticField("Ljava/lang/String;")
    PARAMETER_TS_MODE = JavaStaticField("Ljava/lang/String;")
    PARSER_NAME_AC3 = JavaStaticField("Ljava/lang/String;")
    PARSER_NAME_AC4 = JavaStaticField("Ljava/lang/String;")
    PARSER_NAME_ADTS = JavaStaticField("Ljava/lang/String;")
    PARSER_NAME_AMR = JavaStaticField("Ljava/lang/String;")
    PARSER_NAME_FLAC = JavaStaticField("Ljava/lang/String;")
    PARSER_NAME_FLV = JavaStaticField("Ljava/lang/String;")
    PARSER_NAME_FMP4 = JavaStaticField("Ljava/lang/String;")
    PARSER_NAME_MATROSKA = JavaStaticField("Ljava/lang/String;")
    PARSER_NAME_MP3 = JavaStaticField("Ljava/lang/String;")
    PARSER_NAME_MP4 = JavaStaticField("Ljava/lang/String;")
    PARSER_NAME_OGG = JavaStaticField("Ljava/lang/String;")
    PARSER_NAME_PS = JavaStaticField("Ljava/lang/String;")
    PARSER_NAME_TS = JavaStaticField("Ljava/lang/String;")
    PARSER_NAME_UNKNOWN = JavaStaticField("Ljava/lang/String;")
    PARSER_NAME_WAV = JavaStaticField("Ljava/lang/String;")
    SAMPLE_FLAG_DECODE_ONLY = JavaStaticField("I")
    SAMPLE_FLAG_ENCRYPTED = JavaStaticField("I")
    SAMPLE_FLAG_HAS_SUPPLEMENTAL_DATA = JavaStaticField("I")
    SAMPLE_FLAG_KEY_FRAME = JavaStaticField("I")
    SAMPLE_FLAG_LAST_SAMPLE = JavaStaticField("I")
    getLogSessionId = JavaMethod("()Landroid/media/metrics/LogSessionId;")
    setLogSessionId = JavaMethod("(Landroid/media/metrics/LogSessionId;)V")
    createByName = JavaStaticMethod("(Ljava/lang/String;Landroid/media/MediaParser$OutputConsumer;)Landroid/media/MediaParser;")
    getParserName = JavaMethod("()Ljava/lang/String;")
    getParserNames = JavaStaticMethod("(Landroid/media/MediaFormat;)Ljava/util/List;")
    setParameter = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)Landroid/media/MediaParser;")
    supportsParameter = JavaMethod("(Ljava/lang/String;)Z")
    create = JavaStaticMethod("(Landroid/media/MediaParser$OutputConsumer;[Ljava/lang/String;)Landroid/media/MediaParser;", varargs=True)
    release = JavaMethod("()V")
    advance = JavaMethod("(Landroid/media/MediaParser$SeekableInputReader;)Z")
    seek = JavaMethod("(Landroid/media/MediaParser$SeekPoint;)V")

    class UnrecognizedInputFormatException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaParser$UnrecognizedInputFormatException"

    class TrackData(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaParser$TrackData"
        drmInitData = JavaField("Landroid/media/DrmInitData;")
        mediaFormat = JavaField("Landroid/media/MediaFormat;")

    class SeekableInputReader(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaParser$SeekableInputReader"
        seekToPosition = JavaMethod("(J)V")

    class SeekPoint(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaParser$SeekPoint"
        START = JavaStaticField("Landroid/media/MediaParser$SeekPoint;")
        position = JavaField("J")
        timeMicros = JavaField("J")
        equals = JavaMethod("(Ljava/lang/Object;)Z")
        toString = JavaMethod("()Ljava/lang/String;")
        hashCode = JavaMethod("()I")

    class SeekMap(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaParser$SeekMap"
        UNKNOWN_DURATION = JavaStaticField("I")
        getSeekPoints = JavaMethod("(J)Landroid/util/Pair;")
        isSeekable = JavaMethod("()Z")
        getDurationMicros = JavaMethod("()J")

    class ParsingException(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaParser$ParsingException"

    class OutputConsumer(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaParser$OutputConsumer"
        onTrackCountFound = JavaMethod("(I)V")
        onTrackDataFound = JavaMethod("(ILandroid/media/MediaParser$TrackData;)V")
        onSeekMapFound = JavaMethod("(Landroid/media/MediaParser$SeekMap;)V")
        onSampleCompleted = JavaMethod("(IJIIILandroid/media/MediaCodec$CryptoInfo;)V")
        onSampleDataFound = JavaMethod("(ILandroid/media/MediaParser$InputReader;)V")

    class InputReader(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaParser$InputReader"
        getLength = JavaMethod("()J")
        read = JavaMethod("([BII)I")
        getPosition = JavaMethod("()J")