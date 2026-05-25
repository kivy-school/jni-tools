from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ScrollCaptureCallback"]

class ScrollCaptureCallback(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "android/view/ScrollCaptureCallback"
    onScrollCaptureSearch = JavaMethod("(Landroid/os/CancellationSignal;Ljava/util/function/Consumer;)V")
    onScrollCaptureStart = JavaMethod("(Landroid/view/ScrollCaptureSession;Landroid/os/CancellationSignal;Ljava/lang/Runnable;)V")
    onScrollCaptureImageRequest = JavaMethod("(Landroid/view/ScrollCaptureSession;Landroid/os/CancellationSignal;Landroid/graphics/Rect;Ljava/util/function/Consumer;)V")
    onScrollCaptureEnd = JavaMethod("(Ljava/lang/Runnable;)V")