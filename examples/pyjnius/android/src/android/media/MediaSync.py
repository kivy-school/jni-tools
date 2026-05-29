from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaSync"]

class MediaSync(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaSync"
    __javaconstructor__ = [("()V", False)]
    MEDIASYNC_ERROR_AUDIOTRACK_FAIL = JavaStaticField("I")
    MEDIASYNC_ERROR_SURFACE_FAIL = JavaStaticField("I")
    queueAudio = JavaMethod("(Ljava/nio/ByteBuffer;IJ)V")
    setAudioTrack = JavaMethod("(Landroid/media/AudioTrack;)V")
    getPlaybackParams = JavaMethod("()Landroid/media/PlaybackParams;")
    getSyncParams = JavaMethod("()Landroid/media/SyncParams;")
    setPlaybackParams = JavaMethod("(Landroid/media/PlaybackParams;)V")
    setSyncParams = JavaMethod("(Landroid/media/SyncParams;)V")
    createInputSurface = JavaMethod("()Landroid/view/Surface;")
    flush = JavaMethod("()V")
    release = JavaMethod("()V")
    setSurface = JavaMethod("(Landroid/view/Surface;)V")
    setOnErrorListener = JavaMethod("(Landroid/media/MediaSync$OnErrorListener;Landroid/os/Handler;)V")
    getTimestamp = JavaMethod("()Landroid/media/MediaTimestamp;")
    setCallback = JavaMethod("(Landroid/media/MediaSync$Callback;Landroid/os/Handler;)V")

    class OnErrorListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaSync$OnErrorListener"
        onError = JavaMethod("(Landroid/media/MediaSync;II)V")

    class Callback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaSync$Callback"
        __javaconstructor__ = [("()V", False)]
        onAudioBufferConsumed = JavaMethod("(Landroid/media/MediaSync;Ljava/nio/ByteBuffer;I)V")