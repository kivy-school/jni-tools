from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ThumbnailUtils"]

class ThumbnailUtils(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/ThumbnailUtils"
    __javaconstructor__ = [("()V", False)]
    OPTIONS_RECYCLE_INPUT = JavaStaticField("I")
    createAudioThumbnail = JavaMultipleMethod([("(Ljava/lang/String;I)Landroid/graphics/Bitmap;", True, False), ("(Ljava/io/File;Landroid/util/Size;Landroid/os/CancellationSignal;)Landroid/graphics/Bitmap;", True, False)])
    extractThumbnail = JavaMultipleMethod([("(Landroid/graphics/Bitmap;II)Landroid/graphics/Bitmap;", True, False), ("(Landroid/graphics/Bitmap;III)Landroid/graphics/Bitmap;", True, False)])
    createImageThumbnail = JavaMultipleMethod([("(Ljava/lang/String;I)Landroid/graphics/Bitmap;", True, False), ("(Ljava/io/File;Landroid/util/Size;Landroid/os/CancellationSignal;)Landroid/graphics/Bitmap;", True, False)])
    createVideoThumbnail = JavaMultipleMethod([("(Ljava/io/File;Landroid/util/Size;Landroid/os/CancellationSignal;)Landroid/graphics/Bitmap;", True, False), ("(Ljava/lang/String;I)Landroid/graphics/Bitmap;", True, False)])