from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["YuvImage"]

class YuvImage(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/YuvImage"
    __javaconstructor__ = [("([BIII[I)V", False), ("([BIII[ILandroid/graphics/ColorSpace;)V", False)]
    compressToJpeg = JavaMethod("(Landroid/graphics/Rect;ILjava/io/OutputStream;)Z")
    compressToJpegR = JavaMethod("(Landroid/graphics/YuvImage;ILjava/io/OutputStream;)Z")
    getYuvData = JavaMethod("()[B")
    getYuvFormat = JavaMethod("()I")
    getStrides = JavaMethod("()[I")
    getWidth = JavaMethod("()I")
    getHeight = JavaMethod("()I")
    getColorSpace = JavaMethod("()Landroid/graphics/ColorSpace;")