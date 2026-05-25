from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MultiResolutionImageReader"]

class MultiResolutionImageReader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/MultiResolutionImageReader"
    __javaconstructor__ = [("(Ljava/util/Collection;II)V", False)]
    setOnImageAvailableListener = JavaMethod("(Landroid/media/ImageReader$OnImageAvailableListener;Ljava/util/concurrent/Executor;)V")
    close = JavaMethod("()V")
    finalize = JavaMethod("()V")
    flush = JavaMethod("()V")
    getSurface = JavaMethod("()Landroid/view/Surface;")
    getStreamInfoForImageReader = JavaMethod("(Landroid/media/ImageReader;)Landroid/hardware/camera2/params/MultiResolutionStreamInfo;")