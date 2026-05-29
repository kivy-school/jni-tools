from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["DngCreator"]

class DngCreator(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/camera2/DngCreator"
    __javaconstructor__ = [("(Landroid/hardware/camera2/CameraCharacteristics;Landroid/hardware/camera2/CaptureResult;)V", False)]
    MAX_THUMBNAIL_DIMENSION = JavaStaticField("I")
    close = JavaMethod("()V")
    setLocation = JavaMethod("(Landroid/location/Location;)Landroid/hardware/camera2/DngCreator;")
    setDescription = JavaMethod("(Ljava/lang/String;)Landroid/hardware/camera2/DngCreator;")
    setOrientation = JavaMethod("(I)Landroid/hardware/camera2/DngCreator;")
    setThumbnail = JavaMultipleMethod([("(Landroid/graphics/Bitmap;)Landroid/hardware/camera2/DngCreator;", False, False), ("(Landroid/media/Image;)Landroid/hardware/camera2/DngCreator;", False, False)])
    writeByteBuffer = JavaMethod("(Ljava/io/OutputStream;Landroid/util/Size;Ljava/nio/ByteBuffer;J)V")
    writeImage = JavaMethod("(Ljava/io/OutputStream;Landroid/media/Image;)V")
    writeInputStream = JavaMethod("(Ljava/io/OutputStream;Landroid/util/Size;Ljava/io/InputStream;J)V")