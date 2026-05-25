from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzcag"]

class zzcag(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzcag"
    __javaconstructor__ = [("()V", False)]
    zzh = JavaMethod("(Ljava/lang/Throwable;Ljava/lang/String;)V")
    zzi = JavaMethod("(Ljava/lang/Throwable;Ljava/lang/String;F)V")