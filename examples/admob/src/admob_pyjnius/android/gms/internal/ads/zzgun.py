from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzgun"]

class zzgun(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzgun"
    zza = JavaStaticMethod("(Ljava/lang/Throwable;Ljava/lang/Class;)V")
    zzb = JavaStaticMethod("(Ljava/lang/Throwable;)V")