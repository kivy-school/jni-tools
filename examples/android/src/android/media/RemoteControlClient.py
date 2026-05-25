from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RemoteControlClient"]

class RemoteControlClient(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/RemoteControlClient"
    __javaconstructor__ = [("(Landroid/app/PendingIntent;)V", False), ("(Landroid/app/PendingIntent;Landroid/os/Looper;)V", False)]
    FLAG_KEY_MEDIA_FAST_FORWARD = JavaStaticField("I")
    FLAG_KEY_MEDIA_NEXT = JavaStaticField("I")
    FLAG_KEY_MEDIA_PAUSE = JavaStaticField("I")
    FLAG_KEY_MEDIA_PLAY = JavaStaticField("I")
    FLAG_KEY_MEDIA_PLAY_PAUSE = JavaStaticField("I")
    FLAG_KEY_MEDIA_POSITION_UPDATE = JavaStaticField("I")
    FLAG_KEY_MEDIA_PREVIOUS = JavaStaticField("I")
    FLAG_KEY_MEDIA_RATING = JavaStaticField("I")
    FLAG_KEY_MEDIA_REWIND = JavaStaticField("I")
    FLAG_KEY_MEDIA_STOP = JavaStaticField("I")
    PLAYSTATE_BUFFERING = JavaStaticField("I")
    PLAYSTATE_ERROR = JavaStaticField("I")
    PLAYSTATE_FAST_FORWARDING = JavaStaticField("I")
    PLAYSTATE_PAUSED = JavaStaticField("I")
    PLAYSTATE_PLAYING = JavaStaticField("I")
    PLAYSTATE_REWINDING = JavaStaticField("I")
    PLAYSTATE_SKIPPING_BACKWARDS = JavaStaticField("I")
    PLAYSTATE_SKIPPING_FORWARDS = JavaStaticField("I")
    PLAYSTATE_STOPPED = JavaStaticField("I")
    getMediaSession = JavaMethod("()Landroid/media/session/MediaSession;")
    editMetadata = JavaMethod("(Z)Landroid/media/RemoteControlClient$MetadataEditor;")
    setPlaybackState = JavaMultipleMethod([("(I)V", False, False), ("(IJF)V", False, False)])
    setTransportControlFlags = JavaMethod("(I)V")
    setMetadataUpdateListener = JavaMethod("(Landroid/media/RemoteControlClient$OnMetadataUpdateListener;)V")
    setPlaybackPositionUpdateListener = JavaMethod("(Landroid/media/RemoteControlClient$OnPlaybackPositionUpdateListener;)V")
    setOnGetPlaybackPositionListener = JavaMethod("(Landroid/media/RemoteControlClient$OnGetPlaybackPositionListener;)V")

    class MetadataEditor(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/RemoteControlClient/MetadataEditor"
        BITMAP_KEY_ARTWORK = JavaStaticField("I")
        clone = JavaMethod("()Ljava/lang/Object;")
        putString = JavaMethod("(ILjava/lang/String;)Landroid/media/RemoteControlClient$MetadataEditor;")
        putLong = JavaMethod("(IJ)Landroid/media/RemoteControlClient$MetadataEditor;")
        putBitmap = JavaMethod("(ILandroid/graphics/Bitmap;)Landroid/media/RemoteControlClient$MetadataEditor;")
        putObject = JavaMethod("(ILjava/lang/Object;)Landroid/media/RemoteControlClient$MetadataEditor;")
        clear = JavaMethod("()V")
        apply = JavaMethod("()V")

    class OnGetPlaybackPositionListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/RemoteControlClient/OnGetPlaybackPositionListener"
        onGetPlaybackPosition = JavaMethod("()J")

    class OnMetadataUpdateListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/RemoteControlClient/OnMetadataUpdateListener"
        onMetadataUpdate = JavaMethod("(ILjava/lang/Object;)V")

    class OnPlaybackPositionUpdateListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/RemoteControlClient/OnPlaybackPositionUpdateListener"
        onPlaybackPositionUpdate = JavaMethod("(J)V")