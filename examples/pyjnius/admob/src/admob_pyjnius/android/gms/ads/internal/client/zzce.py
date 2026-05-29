from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzce"]

class zzce(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzce"
    zze = JavaMethod("(Ljava/lang/String;Lcom/google/android/gms/ads/internal/client/zzdx;)V")
    zzf = JavaMethod("(Ljava/lang/String;)V")
    zzg = JavaMethod("(Ljava/lang/String;Lcom/google/android/gms/ads/internal/client/zze;)V")