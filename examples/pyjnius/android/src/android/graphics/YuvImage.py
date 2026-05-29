from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["YuvImage"]

class YuvImage(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/YuvImage"
    __javaconstructor__ = [("([BIII[I)V", False), ("([BIII[ILandroid/graphics/ColorSpace;)V", False)]
    compressToJpegR = JavaMethod("(Landroid/graphics/YuvImage;ILjava/io/OutputStream;)Z")
    getYuvData = JavaMethod("()[B")
    compressToJpeg = JavaMethod("(Landroid/graphics/Rect;ILjava/io/OutputStream;)Z")
    getStrides = JavaMethod("()[I")
    getYuvFormat = JavaMethod("()I")
    getHeight = JavaMethod("()I")
    getWidth = JavaMethod("()I")
    getColorSpace = JavaMethod("()Landroid/graphics/ColorSpace;")