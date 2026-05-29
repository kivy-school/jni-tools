from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["RemoteController"]

class RemoteController(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/RemoteController"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/media/RemoteController$OnClientUpdateListener;)V", False), ("(Landroid/content/Context;Landroid/media/RemoteController$OnClientUpdateListener;Landroid/os/Looper;)V", False)]
    POSITION_SYNCHRONIZATION_CHECK = JavaStaticField("I")
    POSITION_SYNCHRONIZATION_NONE = JavaStaticField("I")
    getEstimatedMediaPosition = JavaMethod("()J")
    sendMediaKeyEvent = JavaMethod("(Landroid/view/KeyEvent;)Z")
    seekTo = JavaMethod("(J)Z")
    setArtworkConfiguration = JavaMethod("(II)Z")
    clearArtworkConfiguration = JavaMethod("()Z")
    setSynchronizationMode = JavaMethod("(I)Z")
    editMetadata = JavaMethod("()Landroid/media/RemoteController$MetadataEditor;")

    class MetadataEditor(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/RemoteController/MetadataEditor"
        apply = JavaMethod("()V")

    class OnClientUpdateListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/RemoteController/OnClientUpdateListener"
        onClientChange = JavaMethod("(Z)V")
        onClientPlaybackStateUpdate = JavaMultipleMethod([("(I)V", False, False), ("(IJJF)V", False, False)])
        onClientTransportControlUpdate = JavaMethod("(I)V")
        onClientMetadataUpdate = JavaMethod("(Landroid/media/RemoteController$MetadataEditor;)V")