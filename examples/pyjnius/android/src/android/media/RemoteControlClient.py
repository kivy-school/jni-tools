from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RemoteControlClient"]

class RemoteControlClient(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/RemoteControlClient"
    __javaconstructor__ = [("(Landroid/app/PendingIntent;Landroid/os/Looper;)V", False), ("(Landroid/app/PendingIntent;)V", False)]
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
    setPlaybackState = JavaMultipleMethod([("(IJF)V", False, False), ("(I)V", False, False)])
    editMetadata = JavaMethod("(Z)Landroid/media/RemoteControlClient$MetadataEditor;")
    getMediaSession = JavaMethod("()Landroid/media/session/MediaSession;")
    setMetadataUpdateListener = JavaMethod("(Landroid/media/RemoteControlClient$OnMetadataUpdateListener;)V")
    setOnGetPlaybackPositionListener = JavaMethod("(Landroid/media/RemoteControlClient$OnGetPlaybackPositionListener;)V")
    setPlaybackPositionUpdateListener = JavaMethod("(Landroid/media/RemoteControlClient$OnPlaybackPositionUpdateListener;)V")
    setTransportControlFlags = JavaMethod("(I)V")

    class OnPlaybackPositionUpdateListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/RemoteControlClient$OnPlaybackPositionUpdateListener"
        onPlaybackPositionUpdate = JavaMethod("(J)V")

    class OnMetadataUpdateListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/RemoteControlClient$OnMetadataUpdateListener"
        onMetadataUpdate = JavaMethod("(ILjava/lang/Object;)V")

    class OnGetPlaybackPositionListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/RemoteControlClient$OnGetPlaybackPositionListener"
        onGetPlaybackPosition = JavaMethod("()J")

    class MetadataEditor(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/RemoteControlClient$MetadataEditor"
        BITMAP_KEY_ARTWORK = JavaStaticField("I")
        BITMAP_KEY_ARTWORK = JavaStaticField("I")
        RATING_KEY_BY_OTHERS = JavaStaticField("I")
        RATING_KEY_BY_USER = JavaStaticField("I")
        putBitmap = JavaMultipleMethod([("(ILandroid/graphics/Bitmap;)Landroid/media/RemoteControlClient$MetadataEditor;", False, False), ("(ILandroid/graphics/Bitmap;)Landroid/media/MediaMetadataEditor;", False, False)])
        putObject = JavaMultipleMethod([("(ILjava/lang/Object;)Landroid/media/MediaMetadataEditor;", False, False), ("(ILjava/lang/Object;)Landroid/media/RemoteControlClient$MetadataEditor;", False, False)])
        clone = JavaMethod("()Ljava/lang/Object;")
        putLong = JavaMultipleMethod([("(IJ)Landroid/media/RemoteControlClient$MetadataEditor;", False, False), ("(IJ)Landroid/media/MediaMetadataEditor;", False, False)])
        clear = JavaMethod("()V")
        apply = JavaMethod("()V")
        putString = JavaMultipleMethod([("(ILjava/lang/String;)Landroid/media/RemoteControlClient$MetadataEditor;", False, False), ("(ILjava/lang/String;)Landroid/media/MediaMetadataEditor;", False, False)])