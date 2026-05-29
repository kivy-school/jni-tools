from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaProjection"]

class MediaProjection(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/projection/MediaProjection"
    createVirtualDisplay = JavaMethod("(Ljava/lang/String;IIIILandroid/view/Surface;Landroid/hardware/display/VirtualDisplay$Callback;Landroid/os/Handler;)Landroid/hardware/display/VirtualDisplay;")
    stop = JavaMethod("()V")
    registerCallback = JavaMethod("(Landroid/media/projection/MediaProjection$Callback;Landroid/os/Handler;)V")
    unregisterCallback = JavaMethod("(Landroid/media/projection/MediaProjection$Callback;)V")

    class Callback(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/projection/MediaProjection$Callback"
        __javaconstructor__ = [("()V", False)]
        onCapturedContentResize = JavaMethod("(II)V")
        onCapturedContentVisibilityChanged = JavaMethod("(Z)V")
        onStop = JavaMethod("()V")