from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ImageReader"]

class ImageReader(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/ImageReader"
    newInstance = JavaMultipleMethod([("(IIII)Landroid/media/ImageReader;", True, False), ("(IIIIJ)Landroid/media/ImageReader;", True, False)])
    close = JavaMethod("()V")
    setOnImageAvailableListener = JavaMethod("(Landroid/media/ImageReader$OnImageAvailableListener;Landroid/os/Handler;)V")
    getHeight = JavaMethod("()I")
    getWidth = JavaMethod("()I")
    getSurface = JavaMethod("()Landroid/view/Surface;")
    getUsage = JavaMethod("()J")
    getDataSpace = JavaMethod("()I")
    acquireLatestImage = JavaMethod("()Landroid/media/Image;")
    getHardwareBufferFormat = JavaMethod("()I")
    getMaxImages = JavaMethod("()I")
    getImageFormat = JavaMethod("()I")
    discardFreeBuffers = JavaMethod("()V")
    acquireNextImage = JavaMethod("()Landroid/media/Image;")

    class OnImageAvailableListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/ImageReader$OnImageAvailableListener"
        onImageAvailable = JavaMethod("(Landroid/media/ImageReader;)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/ImageReader$Builder"
        __javaconstructor__ = [("(II)V", False)]
        setUsage = JavaMethod("(J)Landroid/media/ImageReader$Builder;")
        setImageFormat = JavaMethod("(I)Landroid/media/ImageReader$Builder;")
        setMaxImages = JavaMethod("(I)Landroid/media/ImageReader$Builder;")
        setDefaultDataSpace = JavaMethod("(I)Landroid/media/ImageReader$Builder;")
        setDefaultHardwareBufferFormat = JavaMethod("(I)Landroid/media/ImageReader$Builder;")
        build = JavaMethod("()Landroid/media/ImageReader;")