from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbwr"]

class zzbwr(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbwr"
    zze = JavaMethod("()V")
    zzf = JavaMethod("(Ljava/lang/String;)V")
    zzg = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zze;)V")