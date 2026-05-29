from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScrollCaptureCallback"]

class ScrollCaptureCallback(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/ScrollCaptureCallback"
    onScrollCaptureEnd = JavaMethod("(Ljava/lang/Runnable;)V")
    onScrollCaptureImageRequest = JavaMethod("(Landroid/view/ScrollCaptureSession;Landroid/os/CancellationSignal;Landroid/graphics/Rect;Ljava/util/function/Consumer;)V")
    onScrollCaptureStart = JavaMethod("(Landroid/view/ScrollCaptureSession;Landroid/os/CancellationSignal;Ljava/lang/Runnable;)V")
    onScrollCaptureSearch = JavaMethod("(Landroid/os/CancellationSignal;Ljava/util/function/Consumer;)V")