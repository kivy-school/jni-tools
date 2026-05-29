from jnius import JavaClass, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["LutProperties"]

class LutProperties(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/hardware/LutProperties"
    ONE_DIMENSION = JavaStaticField("I")
    SAMPLING_KEY_CIE_Y = JavaStaticField("I")
    SAMPLING_KEY_MAX_RGB = JavaStaticField("I")
    SAMPLING_KEY_RGB = JavaStaticField("I")
    THREE_DIMENSION = JavaStaticField("I")
    getSize = JavaMethod("()I")
    getSamplingKeys = JavaMethod("()[I")
    getDimension = JavaMethod("()I")