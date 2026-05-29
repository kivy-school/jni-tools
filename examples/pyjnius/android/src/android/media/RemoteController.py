from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RemoteController"]

class RemoteController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/RemoteController"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/media/RemoteController$OnClientUpdateListener;)V", False), ("(Landroid/content/Context;Landroid/media/RemoteController$OnClientUpdateListener;Landroid/os/Looper;)V", False)]
    POSITION_SYNCHRONIZATION_CHECK = JavaStaticField("I")
    POSITION_SYNCHRONIZATION_NONE = JavaStaticField("I")
    sendMediaKeyEvent = JavaMethod("(Landroid/view/KeyEvent;)Z")
    editMetadata = JavaMethod("()Landroid/media/RemoteController$MetadataEditor;")
    clearArtworkConfiguration = JavaMethod("()Z")
    getEstimatedMediaPosition = JavaMethod("()J")
    setArtworkConfiguration = JavaMethod("(II)Z")
    setSynchronizationMode = JavaMethod("(I)Z")
    seekTo = JavaMethod("(J)Z")

    class OnClientUpdateListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/RemoteController$OnClientUpdateListener"
        onClientChange = JavaMethod("(Z)V")
        onClientMetadataUpdate = JavaMethod("(Landroid/media/RemoteController$MetadataEditor;)V")
        onClientPlaybackStateUpdate = JavaMultipleMethod([("(IJJF)V", False, False), ("(I)V", False, False)])
        onClientTransportControlUpdate = JavaMethod("(I)V")

    class MetadataEditor(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/RemoteController$MetadataEditor"
        BITMAP_KEY_ARTWORK = JavaStaticField("I")
        RATING_KEY_BY_OTHERS = JavaStaticField("I")
        RATING_KEY_BY_USER = JavaStaticField("I")
        apply = JavaMethod("()V")