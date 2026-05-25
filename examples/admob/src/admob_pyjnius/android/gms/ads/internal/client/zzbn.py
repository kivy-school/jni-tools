from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbn"]

class zzbn(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzbn"
    zze = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zzm;)V")
    zzf = JavaMethod("()Ljava/lang/String;")
    zzg = JavaMethod("()Z")
    zzh = JavaMethod("()Ljava/lang/String;")
    zzi = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zzm;I)V")