from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["ImageFormat"]

class ImageFormat(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/graphics/ImageFormat"
    __javaconstructor__ = [("()V", False)]
    DEPTH16 = JavaStaticField("I")
    DEPTH_JPEG = JavaStaticField("I")
    DEPTH_POINT_CLOUD = JavaStaticField("I")
    FLEX_RGBA_8888 = JavaStaticField("I")
    FLEX_RGB_888 = JavaStaticField("I")
    HEIC = JavaStaticField("I")
    JPEG = JavaStaticField("I")
    JPEG_R = JavaStaticField("I")
    NV16 = JavaStaticField("I")
    NV21 = JavaStaticField("I")
    PRIVATE = JavaStaticField("I")
    RAW10 = JavaStaticField("I")
    RAW12 = JavaStaticField("I")
    RAW_PRIVATE = JavaStaticField("I")
    RAW_SENSOR = JavaStaticField("I")
    RGB_565 = JavaStaticField("I")
    UNKNOWN = JavaStaticField("I")
    Y8 = JavaStaticField("I")
    YCBCR_P010 = JavaStaticField("I")
    YUV_420_888 = JavaStaticField("I")
    YUV_422_888 = JavaStaticField("I")
    YUV_444_888 = JavaStaticField("I")
    YUY2 = JavaStaticField("I")
    YV12 = JavaStaticField("I")
    getBitsPerPixel = JavaStaticMethod("(I)I")