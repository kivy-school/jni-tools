from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["MuteThisAdReason"]

class MuteThisAdReason(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/MuteThisAdReason"
    getDescription = JavaMethod("()Ljava/lang/String;")