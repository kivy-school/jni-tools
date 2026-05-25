from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaSync"]

class MediaSync(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaSync"
    __javaconstructor__ = [("()V", False)]
    MEDIASYNC_ERROR_AUDIOTRACK_FAIL = JavaStaticField("I")
    MEDIASYNC_ERROR_SURFACE_FAIL = JavaStaticField("I")
    finalize = JavaMethod("()V")
    release = JavaMethod("()V")
    setCallback = JavaMethod("(Landroid/media/MediaSync$Callback;Landroid/os/Handler;)V")
    setOnErrorListener = JavaMethod("(Landroid/media/MediaSync$OnErrorListener;Landroid/os/Handler;)V")
    setSurface = JavaMethod("(Landroid/view/Surface;)V")
    setAudioTrack = JavaMethod("(Landroid/media/AudioTrack;)V")
    createInputSurface = JavaMethod("()Landroid/view/Surface;")
    setPlaybackParams = JavaMethod("(Landroid/media/PlaybackParams;)V")
    getPlaybackParams = JavaMethod("()Landroid/media/PlaybackParams;")
    setSyncParams = JavaMethod("(Landroid/media/SyncParams;)V")
    getSyncParams = JavaMethod("()Landroid/media/SyncParams;")
    flush = JavaMethod("()V")
    getTimestamp = JavaMethod("()Landroid/media/MediaTimestamp;")
    queueAudio = JavaMethod("(Ljava/nio/ByteBuffer;IJ)V")

    class Callback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaSync/Callback"
        __javaconstructor__ = [("()V", False)]
        onAudioBufferConsumed = JavaMethod("(Landroid/media/MediaSync;Ljava/nio/ByteBuffer;I)V")

    class OnErrorListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaSync/OnErrorListener"
        onError = JavaMethod("(Landroid/media/MediaSync;II)V")