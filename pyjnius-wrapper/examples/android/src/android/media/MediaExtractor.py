from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaExtractor"]

class MediaExtractor(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaExtractor"
    __javaconstructor__ = [("()V", False)]
    SAMPLE_FLAG_ENCRYPTED = JavaStaticField("I")
    SAMPLE_FLAG_PARTIAL_FRAME = JavaStaticField("I")
    SAMPLE_FLAG_SYNC = JavaStaticField("I")
    SEEK_TO_CLOSEST_SYNC = JavaStaticField("I")
    SEEK_TO_NEXT_SYNC = JavaStaticField("I")
    SEEK_TO_PREVIOUS_SYNC = JavaStaticField("I")
    setDataSource = JavaMultipleMethod([("(Landroid/media/MediaDataSource;)V", False, False), ("(Landroid/content/Context;Landroid/net/Uri;Ljava/util/Map;)V", False, False), ("(Ljava/lang/String;Ljava/util/Map;)V", False, False), ("(Ljava/lang/String;)V", False, False), ("(Landroid/content/res/AssetFileDescriptor;)V", False, False), ("(Ljava/io/FileDescriptor;)V", False, False), ("(Ljava/io/FileDescriptor;JJ)V", False, False)])
    setMediaCas = JavaMethod("(Landroid/media/MediaCas;)V")
    getCasInfo = JavaMethod("(I)Landroid/media/MediaExtractor$CasInfo;")
    finalize = JavaMethod("()V")
    release = JavaMethod("()V")
    getTrackCount = JavaMethod("()I")
    getDrmInitData = JavaMethod("()Landroid/media/DrmInitData;")
    getAudioPresentations = JavaMethod("(I)Ljava/util/List;")
    getPsshInfo = JavaMethod("()Ljava/util/Map;")
    getTrackFormat = JavaMethod("(I)Landroid/media/MediaFormat;")
    selectTrack = JavaMethod("(I)V")
    unselectTrack = JavaMethod("(I)V")
    seekTo = JavaMethod("(JI)V")
    advance = JavaMethod("()Z")
    readSampleData = JavaMethod("(Ljava/nio/ByteBuffer;I)I")
    getSampleTrackIndex = JavaMethod("()I")
    getSampleTime = JavaMethod("()J")
    getSampleSize = JavaMethod("()J")
    getSampleFlags = JavaMethod("()I")
    getSampleCryptoInfo = JavaMethod("(Landroid/media/MediaCodec$CryptoInfo;)Z")
    getCachedDuration = JavaMethod("()J")
    hasCacheReachedEndOfStream = JavaMethod("()Z")
    setLogSessionId = JavaMethod("(Landroid/media/metrics/LogSessionId;)V")
    getLogSessionId = JavaMethod("()Landroid/media/metrics/LogSessionId;")
    getMetrics = JavaMethod("()Landroid/os/PersistableBundle;")

    class CasInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaExtractor/CasInfo"
        getSystemId = JavaMethod("()I")
        getPrivateData = JavaMethod("()[B")
        getSession = JavaMethod("()Landroid/media/MediaCas$Session;")

    class MetricsConstants(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaExtractor/MetricsConstants"
        FORMAT = JavaStaticField("Ljava/lang/String;")
        MIME_TYPE = JavaStaticField("Ljava/lang/String;")
        TRACKS = JavaStaticField("Ljava/lang/String;")