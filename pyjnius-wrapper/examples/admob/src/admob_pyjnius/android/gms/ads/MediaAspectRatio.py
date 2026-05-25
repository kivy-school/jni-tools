from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MediaAspectRatio"]

class MediaAspectRatio(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/MediaAspectRatio"
    UNKNOWN = JavaStaticField("I")
    ANY = JavaStaticField("I")
    LANDSCAPE = JavaStaticField("I")
    PORTRAIT = JavaStaticField("I")
    SQUARE = JavaStaticField("I")