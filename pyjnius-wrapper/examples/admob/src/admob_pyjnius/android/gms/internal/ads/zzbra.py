from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbra"]

class zzbra(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbra"
    zze = JavaMethod("(Ljava/lang/String;)V")
    zzf = JavaMethod("()V")