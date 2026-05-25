from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbvj"]

class zzbvj(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbvj"
    zzb = JavaMethod("(Ljava/lang/String;)Lcom/google/android/gms/internal/ads/zzbvm;")
    zzc = JavaMethod("(Ljava/lang/String;)Z")
    zze = JavaMethod("(Ljava/lang/String;)Lcom/google/android/gms/internal/ads/zzbxi;")
    zzd = JavaMethod("(Ljava/lang/String;)Z")