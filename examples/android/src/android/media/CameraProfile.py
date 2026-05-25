from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CameraProfile"]

class CameraProfile(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/CameraProfile"
    __javaconstructor__ = [("()V", False)]
    QUALITY_HIGH = JavaStaticField("I")
    QUALITY_LOW = JavaStaticField("I")
    QUALITY_MEDIUM = JavaStaticField("I")
    getJpegEncodingQualityParameter = JavaMultipleMethod([("(I)I", True, False), ("(II)I", True, False)])