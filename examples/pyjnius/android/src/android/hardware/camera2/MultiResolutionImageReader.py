from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MultiResolutionImageReader"]

class MultiResolutionImageReader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/MultiResolutionImageReader"
    __javaconstructor__ = [("(Ljava/util/Collection;II)V", False), ("(Ljava/util/Collection;IIJ)V", False)]
    flush = JavaMethod("()V")
    close = JavaMethod("()V")
    getStreamInfoForImageReader = JavaMethod("(Landroid/media/ImageReader;)Landroid/hardware/camera2/params/MultiResolutionStreamInfo;")
    setOnImageAvailableListener = JavaMethod("(Landroid/media/ImageReader$OnImageAvailableListener;Ljava/util/concurrent/Executor;)V")
    getSurface = JavaMethod("()Landroid/view/Surface;")