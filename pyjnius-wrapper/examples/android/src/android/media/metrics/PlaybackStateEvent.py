from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PlaybackStateEvent"]

class PlaybackStateEvent(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/metrics/PlaybackStateEvent"
    CREATOR = JavaStaticField("Landroid/os/Parcelable$Creator;")
    STATE_ABANDONED = JavaStaticField("I")
    STATE_BUFFERING = JavaStaticField("I")
    STATE_ENDED = JavaStaticField("I")
    STATE_FAILED = JavaStaticField("I")
    STATE_INTERRUPTED_BY_AD = JavaStaticField("I")
    STATE_JOINING_BACKGROUND = JavaStaticField("I")
    STATE_JOINING_FOREGROUND = JavaStaticField("I")
    STATE_NOT_STARTED = JavaStaticField("I")
    STATE_PAUSED = JavaStaticField("I")
    STATE_PAUSED_BUFFERING = JavaStaticField("I")
    STATE_PLAYING = JavaStaticField("I")
    STATE_SEEKING = JavaStaticField("I")
    STATE_STOPPED = JavaStaticField("I")
    STATE_SUPPRESSED = JavaStaticField("I")
    STATE_SUPPRESSED_BUFFERING = JavaStaticField("I")
    getState = JavaMethod("()I")
    getTimeSinceCreatedMillis = JavaMethod("()J")
    getMetricsBundle = JavaMethod("()Landroid/os/Bundle;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    writeToParcel = JavaMethod("(Landroid/os/Parcel;I)V")
    describeContents = JavaMethod("()I")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/metrics/PlaybackStateEvent/Builder"
        __javaconstructor__ = [("()V", False)]
        setState = JavaMethod("(I)Landroid/media/metrics/PlaybackStateEvent$Builder;")
        setTimeSinceCreatedMillis = JavaMethod("(J)Landroid/media/metrics/PlaybackStateEvent$Builder;")
        setMetricsBundle = JavaMethod("(Landroid/os/Bundle;)Landroid/media/metrics/PlaybackStateEvent$Builder;")
        build = JavaMethod("()Landroid/media/metrics/PlaybackStateEvent;")