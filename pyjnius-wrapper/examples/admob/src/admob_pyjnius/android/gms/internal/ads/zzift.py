from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzift"]

class zzift(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzift"
    zza = JavaStaticMethod("()Lcom/google/android/gms/internal/ads/zzift;")
    zzb = JavaMethod("(Lcom/google/android/gms/internal/ads/zzift;)V")
    entrySet = JavaMethod("()Ljava/util/Set;")
    clear = JavaMethod("()V")
    put = JavaMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    putAll = JavaMethod("(Ljava/util/Map;)V")
    remove = JavaMethod("(Ljava/lang/Object;)Ljava/lang/Object;")
    equals = JavaMethod("(Ljava/lang/Object;)Z")
    hashCode = JavaMethod("()I")
    zzc = JavaMethod("()Lcom/google/android/gms/internal/ads/zzift;")
    zzd = JavaMethod("()V")
    zze = JavaMethod("()Z")