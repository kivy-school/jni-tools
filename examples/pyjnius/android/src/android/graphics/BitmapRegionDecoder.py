from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["BitmapRegionDecoder"]

class BitmapRegionDecoder(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/BitmapRegionDecoder"
    newInstance = JavaMultipleMethod([("([BIIZ)Landroid/graphics/BitmapRegionDecoder;", True, False), ("(Ljava/io/FileDescriptor;Z)Landroid/graphics/BitmapRegionDecoder;", True, False), ("(Ljava/io/InputStream;)Landroid/graphics/BitmapRegionDecoder;", True, False), ("(Ljava/io/InputStream;Z)Landroid/graphics/BitmapRegionDecoder;", True, False), ("(Ljava/lang/String;)Landroid/graphics/BitmapRegionDecoder;", True, False), ("(Ljava/lang/String;Z)Landroid/graphics/BitmapRegionDecoder;", True, False), ("([BII)Landroid/graphics/BitmapRegionDecoder;", True, False), ("(Landroid/os/ParcelFileDescriptor;)Landroid/graphics/BitmapRegionDecoder;", True, False)])
    getHeight = JavaMethod("()I")
    getWidth = JavaMethod("()I")
    isRecycled = JavaMethod("()Z")
    decodeRegion = JavaMethod("(Landroid/graphics/Rect;Landroid/graphics/BitmapFactory$Options;)Landroid/graphics/Bitmap;")
    recycle = JavaMethod("()V")