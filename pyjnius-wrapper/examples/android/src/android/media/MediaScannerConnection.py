from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaScannerConnection"]

class MediaScannerConnection(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaScannerConnection"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/media/MediaScannerConnection$MediaScannerConnectionClient;)V", False)]
    connect = JavaMethod("()V")
    disconnect = JavaMethod("()V")
    isConnected = JavaMethod("()Z")
    scanFile = JavaMultipleMethod([("(Ljava/lang/String;Ljava/lang/String;)V", False, False), ("(Landroid/content/Context;[Ljava/lang/String;[Ljava/lang/String;Landroid/media/MediaScannerConnection$OnScanCompletedListener;)V", True, False)])
    onServiceConnected = JavaMethod("(Landroid/content/ComponentName;Landroid/os/IBinder;)V")
    onServiceDisconnected = JavaMethod("(Landroid/content/ComponentName;)V")

    class MediaScannerConnectionClient(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaScannerConnection/MediaScannerConnectionClient"
        onMediaScannerConnected = JavaMethod("()V")

    class OnScanCompletedListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaScannerConnection/OnScanCompletedListener"
        onScanCompleted = JavaMethod("(Ljava/lang/String;Landroid/net/Uri;)V")