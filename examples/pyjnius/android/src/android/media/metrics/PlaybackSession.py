from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PlaybackSession"]

class PlaybackSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/metrics/PlaybackSession"
    reportNetworkEvent = JavaMethod("(Landroid/media/metrics/NetworkEvent;)V")
    reportPlaybackErrorEvent = JavaMethod("(Landroid/media/metrics/PlaybackErrorEvent;)V")
    reportPlaybackMetrics = JavaMethod("(Landroid/media/metrics/PlaybackMetrics;)V")
    reportPlaybackStateEvent = JavaMethod("(Landroid/media/metrics/PlaybackStateEvent;)V")
    reportTrackChangeEvent = JavaMethod("(Landroid/media/metrics/TrackChangeEvent;)V")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    close = JavaMethod("()V")
    getSessionId = JavaMethod("()Landroid/media/metrics/LogSessionId;")