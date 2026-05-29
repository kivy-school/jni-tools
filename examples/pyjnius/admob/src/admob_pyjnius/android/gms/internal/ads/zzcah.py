from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzcah"]

class zzcah(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzcah"
    zzh = JavaMethod("(Ljava/lang/Throwable;Ljava/lang/String;)V")
    zzi = JavaMethod("(Ljava/lang/Throwable;Ljava/lang/String;F)V")