from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PlaybackSession"]

class PlaybackSession(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/metrics/PlaybackSession"
    reportPlaybackMetrics = JavaMethod("(Landroid/media/metrics/PlaybackMetrics;)V")
    reportPlaybackErrorEvent = JavaMethod("(Landroid/media/metrics/PlaybackErrorEvent;)V")
    reportNetworkEvent = JavaMethod("(Landroid/media/metrics/NetworkEvent;)V")
    reportPlaybackStateEvent = JavaMethod("(Landroid/media/metrics/PlaybackStateEvent;)V")
    reportTrackChangeEvent = JavaMethod("(Landroid/media/metrics/TrackChangeEvent;)V")
    getSessionId = JavaMethod("()Landroid/media/metrics/LogSessionId;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    close = JavaMethod("()V")