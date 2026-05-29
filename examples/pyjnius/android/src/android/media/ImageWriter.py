from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ImageWriter"]

class ImageWriter(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/ImageWriter"
    newInstance = JavaMultipleMethod([("(Landroid/view/Surface;I)Landroid/media/ImageWriter;", True, False), ("(Landroid/view/Surface;II)Landroid/media/ImageWriter;", True, False)])
    close = JavaMethod("()V")
    getHeight = JavaMethod("()I")
    getWidth = JavaMethod("()I")
    queueInputImage = JavaMethod("(Landroid/media/Image;)V")
    dequeueInputImage = JavaMethod("()Landroid/media/Image;")
    getUsage = JavaMethod("()J")
    setOnImageReleasedListener = JavaMethod("(Landroid/media/ImageWriter$OnImageReleasedListener;Landroid/os/Handler;)V")
    getDataSpace = JavaMethod("()I")
    getFormat = JavaMethod("()I")
    getHardwareBufferFormat = JavaMethod("()I")
    getMaxImages = JavaMethod("()I")

    class OnImageReleasedListener(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/ImageWriter$OnImageReleasedListener"
        onImageReleased = JavaMethod("(Landroid/media/ImageWriter;)V")

    class Builder(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/ImageWriter$Builder"
        __javaconstructor__ = [("(Landroid/view/Surface;)V", False)]
        setUsage = JavaMethod("(J)Landroid/media/ImageWriter$Builder;")
        setImageFormat = JavaMethod("(I)Landroid/media/ImageWriter$Builder;")
        setMaxImages = JavaMethod("(I)Landroid/media/ImageWriter$Builder;")
        setWidthAndHeight = JavaMethod("(II)Landroid/media/ImageWriter$Builder;")
        setHardwareBufferFormat = JavaMethod("(I)Landroid/media/ImageWriter$Builder;")
        setDataSpace = JavaMethod("(I)Landroid/media/ImageWriter$Builder;")
        build = JavaMethod("()Landroid/media/ImageWriter;")