from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaMetricsManager"]

class MediaMetricsManager(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/metrics/MediaMetricsManager"
    INVALID_TIMESTAMP = JavaStaticField("J")
    createEditingSession = JavaMethod("()Landroid/media/metrics/EditingSession;")
    createBundleSession = JavaMethod("()Landroid/media/metrics/BundleSession;")
    createPlaybackSession = JavaMethod("()Landroid/media/metrics/PlaybackSession;")
    createRecordingSession = JavaMethod("()Landroid/media/metrics/RecordingSession;")
    createTranscodingSession = JavaMethod("()Landroid/media/metrics/TranscodingSession;")
    releaseSessionId = JavaMethod("(Ljava/lang/String;)V")