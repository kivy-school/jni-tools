from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ImageReader"]

class ImageReader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/ImageReader"
    newInstance = JavaMultipleMethod([("(IIII)Landroid/media/ImageReader;", True, False), ("(IIIIJ)Landroid/media/ImageReader;", True, False)])
    getWidth = JavaMethod("()I")
    getHeight = JavaMethod("()I")
    getImageFormat = JavaMethod("()I")
    getHardwareBufferFormat = JavaMethod("()I")
    getDataSpace = JavaMethod("()I")
    getMaxImages = JavaMethod("()I")
    getUsage = JavaMethod("()J")
    getSurface = JavaMethod("()Landroid/view/Surface;")
    acquireLatestImage = JavaMethod("()Landroid/media/Image;")
    acquireNextImage = JavaMethod("()Landroid/media/Image;")
    setOnImageAvailableListener = JavaMethod("(Landroid/media/ImageReader$OnImageAvailableListener;Landroid/os/Handler;)V")
    close = JavaMethod("()V")
    discardFreeBuffers = JavaMethod("()V")
    finalize = JavaMethod("()V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/ImageReader/Builder"
        __javaconstructor__ = [("(II)V", False)]
        setMaxImages = JavaMethod("(I)Landroid/media/ImageReader$Builder;")
        setUsage = JavaMethod("(J)Landroid/media/ImageReader$Builder;")
        setImageFormat = JavaMethod("(I)Landroid/media/ImageReader$Builder;")
        setDefaultHardwareBufferFormat = JavaMethod("(I)Landroid/media/ImageReader$Builder;")
        setDefaultDataSpace = JavaMethod("(I)Landroid/media/ImageReader$Builder;")
        build = JavaMethod("()Landroid/media/ImageReader;")

    class OnImageAvailableListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/ImageReader/OnImageAvailableListener"
        onImageAvailable = JavaMethod("(Landroid/media/ImageReader;)V")