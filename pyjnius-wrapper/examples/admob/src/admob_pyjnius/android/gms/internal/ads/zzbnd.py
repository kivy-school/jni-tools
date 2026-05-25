from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbnd"]

class zzbnd(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbnd"
    __javaconstructor__ = [("(Lcom/google/android/gms/internal/ads/zzbnc;)V", False)]
    zza = JavaMethod("()Lcom/google/android/gms/internal/ads/zzbnc;")
    zzb = JavaMethod("()Ljava/lang/String;")