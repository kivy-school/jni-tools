from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzihe"]

class zzihe(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzihe"
    zza = JavaStaticMethod("()Lcom/google/android/gms/internal/ads/zzihe;")
    zzd = JavaMethod("()V")
    zzg = JavaMethod("(Lcom/google/android/gms/internal/ads/zzihs;)V")
    zzh = JavaMethod("()I")
    zzi = JavaMethod("()I")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")