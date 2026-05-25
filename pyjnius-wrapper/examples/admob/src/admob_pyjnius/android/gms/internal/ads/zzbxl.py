from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbxl"]

class zzbxl(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbxl"
    zze = JavaMethod("(Ljava/lang/String;)V")
    zzf = JavaMethod("(Ljava/lang/String;)V")
    zzg = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zze;)V")