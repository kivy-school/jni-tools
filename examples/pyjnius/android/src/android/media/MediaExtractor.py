from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

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
    getMetrics = JavaMethod("()Landroid/os/PersistableBundle;")
    getLogSessionId = JavaMethod("()Landroid/media/metrics/LogSessionId;")
    setLogSessionId = JavaMethod("(Landroid/media/metrics/LogSessionId;)V")
    selectTrack = JavaMethod("(I)V")
    setDataSource = JavaMultipleMethod([("(Ljava/io/FileDescriptor;)V", False, False), ("(Ljava/io/FileDescriptor;JJ)V", False, False), ("(Ljava/lang/String;)V", False, False), ("(Ljava/lang/String;Ljava/util/Map;)V", False, False), ("(Landroid/content/res/AssetFileDescriptor;)V", False, False), ("(Landroid/media/MediaDataSource;)V", False, False), ("(Landroid/content/Context;Landroid/net/Uri;Ljava/util/Map;)V", False, False)])
    getCachedDuration = JavaMethod("()J")
    getCasInfo = JavaMethod("(I)Landroid/media/MediaExtractor$CasInfo;")
    getSampleCryptoInfo = JavaMethod("(Landroid/media/MediaCodec$CryptoInfo;)Z")
    getSampleTime = JavaMethod("()J")
    getSampleTrackIndex = JavaMethod("()I")
    getTrackCount = JavaMethod("()I")
    getTrackFormat = JavaMethod("(I)Landroid/media/MediaFormat;")
    hasCacheReachedEndOfStream = JavaMethod("()Z")
    getSampleFlags = JavaMethod("()I")
    getDrmInitData = JavaMethod("()Landroid/media/DrmInitData;")
    getPsshInfo = JavaMethod("()Ljava/util/Map;")
    getAudioPresentations = JavaMethod("(I)Ljava/util/List;")
    getSampleSize = JavaMethod("()J")
    readSampleData = JavaMethod("(Ljava/nio/ByteBuffer;I)I")
    setMediaCas = JavaMethod("(Landroid/media/MediaCas;)V")
    unselectTrack = JavaMethod("(I)V")
    release = JavaMethod("()V")
    advance = JavaMethod("()Z")
    seekTo = JavaMethod("(JI)V")

    class MetricsConstants(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaExtractor$MetricsConstants"
        FORMAT = JavaStaticField("Ljava/lang/String;")
        MIME_TYPE = JavaStaticField("Ljava/lang/String;")
        TRACKS = JavaStaticField("Ljava/lang/String;")

    class CasInfo(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaExtractor$CasInfo"
        getSession = JavaMethod("()Landroid/media/MediaCas$Session;")
        getSystemId = JavaMethod("()I")
        getPrivateData = JavaMethod("()[B")