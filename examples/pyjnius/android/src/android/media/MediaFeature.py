from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaFeature"]

class MediaFeature(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "android/media/MediaFeature"
    __javaconstructor__ = [("()V", False)]

    class HdrType(JavaClass, metaclass=MetaJavaClass):
        __javaclass__ = "android/media/MediaFeature/HdrType"
        DOLBY_VISION = JavaStaticField("Ljava/lang/String;")
        HDR10 = JavaStaticField("Ljava/lang/String;")
        HDR10_PLUS = JavaStaticField("Ljava/lang/String;")
        HLG = JavaStaticField("Ljava/lang/String;")