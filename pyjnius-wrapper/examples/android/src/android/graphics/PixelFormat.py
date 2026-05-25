from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["PixelFormat"]

class PixelFormat(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/PixelFormat"
    __javaconstructor__ = [("()V", False)]
    A_8 = JavaStaticField("I")
    JPEG = JavaStaticField("I")
    LA_88 = JavaStaticField("I")
    L_8 = JavaStaticField("I")
    OPAQUE = JavaStaticField("I")
    RGBA_1010102 = JavaStaticField("I")
    RGBA_4444 = JavaStaticField("I")
    RGBA_5551 = JavaStaticField("I")
    RGBA_8888 = JavaStaticField("I")
    RGBA_F16 = JavaStaticField("I")
    RGBX_8888 = JavaStaticField("I")
    RGB_332 = JavaStaticField("I")
    RGB_565 = JavaStaticField("I")
    RGB_888 = JavaStaticField("I")
    TRANSLUCENT = JavaStaticField("I")
    TRANSPARENT = JavaStaticField("I")
    UNKNOWN = JavaStaticField("I")
    YCbCr_420_SP = JavaStaticField("I")
    YCbCr_422_I = JavaStaticField("I")
    YCbCr_422_SP = JavaStaticField("I")
    bitsPerPixel = JavaField("I")
    bytesPerPixel = JavaField("I")
    getPixelFormatInfo = JavaStaticMethod("(ILandroid/graphics/PixelFormat;)V")
    formatHasAlpha = JavaStaticMethod("(I)Z")