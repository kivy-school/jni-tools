from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ImageWriter"]

class ImageWriter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/ImageWriter"
    newInstance = JavaMultipleMethod([("(Landroid/view/Surface;I)Landroid/media/ImageWriter;", True, False), ("(Landroid/view/Surface;II)Landroid/media/ImageWriter;", True, False)])
    getMaxImages = JavaMethod("()I")
    getWidth = JavaMethod("()I")
    getHeight = JavaMethod("()I")
    dequeueInputImage = JavaMethod("()Landroid/media/Image;")
    queueInputImage = JavaMethod("(Landroid/media/Image;)V")
    getFormat = JavaMethod("()I")
    getUsage = JavaMethod("()J")
    getHardwareBufferFormat = JavaMethod("()I")
    getDataSpace = JavaMethod("()I")
    setOnImageReleasedListener = JavaMethod("(Landroid/media/ImageWriter$OnImageReleasedListener;Landroid/os/Handler;)V")
    close = JavaMethod("()V")
    finalize = JavaMethod("()V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/ImageWriter/Builder"
        __javaconstructor__ = [("(Landroid/view/Surface;)V", False)]
        setWidthAndHeight = JavaMethod("(II)Landroid/media/ImageWriter$Builder;")
        setMaxImages = JavaMethod("(I)Landroid/media/ImageWriter$Builder;")
        setImageFormat = JavaMethod("(I)Landroid/media/ImageWriter$Builder;")
        setHardwareBufferFormat = JavaMethod("(I)Landroid/media/ImageWriter$Builder;")
        setDataSpace = JavaMethod("(I)Landroid/media/ImageWriter$Builder;")
        setUsage = JavaMethod("(J)Landroid/media/ImageWriter$Builder;")
        build = JavaMethod("()Landroid/media/ImageWriter;")

    class OnImageReleasedListener(JavaInterface, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/ImageWriter/OnImageReleasedListener"
        onImageReleased = JavaMethod("(Landroid/media/ImageWriter;)V")