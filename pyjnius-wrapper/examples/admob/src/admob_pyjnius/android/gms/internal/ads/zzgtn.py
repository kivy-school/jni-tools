from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzgtn"]

class zzgtn(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzgtn"
    zza = JavaMethod("(Ljava/lang/Object;)Lcom/google/android/gms/internal/ads/zzgtn;")
    toString = JavaMethod("()Ljava/lang/String;")