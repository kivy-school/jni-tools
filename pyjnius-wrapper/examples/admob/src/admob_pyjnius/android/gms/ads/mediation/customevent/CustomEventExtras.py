from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["CustomEventExtras"]

class CustomEventExtras(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/mediation/customevent/CustomEventExtras"
    __javaconstructor__ = [("()V", False)]
    getExtra = JavaMethod("(Ljava/lang/String;)Ljava/lang/Object;")
    setExtra = JavaMethod("(Ljava/lang/String;Ljava/lang/Object;)V")