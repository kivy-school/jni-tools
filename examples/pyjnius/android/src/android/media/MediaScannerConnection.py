from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaScannerConnection"]

class MediaScannerConnection(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaScannerConnection"
    __javaconstructor__ = [("(Landroid/content/Context;Landroid/media/MediaScannerConnection$MediaScannerConnectionClient;)V", False)]
    connect = JavaMethod("()V")
    isConnected = JavaMethod("()Z")
    disconnect = JavaMethod("()V")
    scanFile = JavaMultipleMethod([("(Landroid/content/Context;[Ljava/lang/String;[Ljava/lang/String;Landroid/media/MediaScannerConnection$OnScanCompletedListener;)V", True, False), ("(Ljava/lang/String;Ljava/lang/String;)V", False, False)])
    onServiceConnected = JavaMethod("(Landroid/content/ComponentName;Landroid/os/IBinder;)V")
    onServiceDisconnected = JavaMethod("(Landroid/content/ComponentName;)V")

    class OnScanCompletedListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaScannerConnection$OnScanCompletedListener"
        onScanCompleted = JavaMethod("(Ljava/lang/String;Landroid/net/Uri;)V")

    class MediaScannerConnectionClient(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaScannerConnection$MediaScannerConnectionClient"
        onMediaScannerConnected = JavaMethod("()V")