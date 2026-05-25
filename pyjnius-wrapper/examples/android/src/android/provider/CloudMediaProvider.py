from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CloudMediaProvider"]

class CloudMediaProvider(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/provider/CloudMediaProvider"
    __javaconstructor__ = [("()V", False)]
    attachInfo = JavaMethod("(Landroid/content/Context;Landroid/content/pm/ProviderInfo;)V")
    onGetMediaCollectionInfo = JavaMethod("(Landroid/os/Bundle;)Landroid/os/Bundle;")
    onQueryMedia = JavaMethod("(Landroid/os/Bundle;)Landroid/database/Cursor;")
    onQueryDeletedMedia = JavaMethod("(Landroid/os/Bundle;)Landroid/database/Cursor;")
    onQueryAlbums = JavaMethod("(Landroid/os/Bundle;)Landroid/database/Cursor;")
    onOpenPreview = JavaMethod("(Ljava/lang/String;Landroid/graphics/Point;Landroid/os/Bundle;Landroid/os/CancellationSignal;)Landroid/content/res/AssetFileDescriptor;")
    onOpenMedia = JavaMethod("(Ljava/lang/String;Landroid/os/Bundle;Landroid/os/CancellationSignal;)Landroid/os/ParcelFileDescriptor;")
    onCreateCloudMediaSurfaceController = JavaMethod("(Landroid/os/Bundle;Landroid/provider/CloudMediaProvider$CloudMediaSurfaceStateChangedCallback;)Landroid/provider/CloudMediaProvider$CloudMediaSurfaceController;")
    call = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Landroid/os/Bundle;)Landroid/os/Bundle;")
    openFile = JavaMultipleMethod([("(Landroid/net/Uri;Ljava/lang/String;)Landroid/os/ParcelFileDescriptor;", False, False), ("(Landroid/net/Uri;Ljava/lang/String;Landroid/os/CancellationSignal;)Landroid/os/ParcelFileDescriptor;", False, False)])
    openTypedAssetFile = JavaMultipleMethod([("(Landroid/net/Uri;Ljava/lang/String;Landroid/os/Bundle;)Landroid/content/res/AssetFileDescriptor;", False, False), ("(Landroid/net/Uri;Ljava/lang/String;Landroid/os/Bundle;Landroid/os/CancellationSignal;)Landroid/content/res/AssetFileDescriptor;", False, False)])
    query = JavaMultipleMethod([("(Landroid/net/Uri;[Ljava/lang/String;Landroid/os/Bundle;Landroid/os/CancellationSignal;)Landroid/database/Cursor;", False, False), ("(Landroid/net/Uri;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;)Landroid/database/Cursor;", False, False), ("(Landroid/net/Uri;[Ljava/lang/String;Ljava/lang/String;[Ljava/lang/String;Ljava/lang/String;Landroid/os/CancellationSignal;)Landroid/database/Cursor;", False, False)])
    getType = JavaMethod("(Landroid/net/Uri;)Ljava/lang/String;")
    canonicalize = JavaMethod("(Landroid/net/Uri;)Landroid/net/Uri;")
    insert = JavaMethod("(Landroid/net/Uri;Landroid/content/ContentValues;)Landroid/net/Uri;")
    delete = JavaMethod("(Landroid/net/Uri;Ljava/lang/String;[Ljava/lang/String;)I")
    update = JavaMethod("(Landroid/net/Uri;Landroid/content/ContentValues;Ljava/lang/String;[Ljava/lang/String;)I")

    class CloudMediaSurfaceController(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/provider/CloudMediaProvider/CloudMediaSurfaceController"
        __javaconstructor__ = [("()V", False)]
        onPlayerCreate = JavaMethod("()V")
        onPlayerRelease = JavaMethod("()V")
        onSurfaceCreated = JavaMethod("(ILandroid/view/Surface;Ljava/lang/String;)V")
        onSurfaceChanged = JavaMethod("(IIII)V")
        onSurfaceDestroyed = JavaMethod("(I)V")
        onMediaPlay = JavaMethod("(I)V")
        onMediaPause = JavaMethod("(I)V")
        onMediaSeekTo = JavaMethod("(IJ)V")
        onConfigChange = JavaMethod("(Landroid/os/Bundle;)V")
        onDestroy = JavaMethod("()V")

    class CloudMediaSurfaceStateChangedCallback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/provider/CloudMediaProvider/CloudMediaSurfaceStateChangedCallback"
        PLAYBACK_STATE_BUFFERING = JavaStaticField("I")
        PLAYBACK_STATE_COMPLETED = JavaStaticField("I")
        PLAYBACK_STATE_ERROR_PERMANENT_FAILURE = JavaStaticField("I")
        PLAYBACK_STATE_ERROR_RETRIABLE_FAILURE = JavaStaticField("I")
        PLAYBACK_STATE_MEDIA_SIZE_CHANGED = JavaStaticField("I")
        PLAYBACK_STATE_PAUSED = JavaStaticField("I")
        PLAYBACK_STATE_READY = JavaStaticField("I")
        PLAYBACK_STATE_STARTED = JavaStaticField("I")
        setPlaybackState = JavaMethod("(IILandroid/os/Bundle;)V")