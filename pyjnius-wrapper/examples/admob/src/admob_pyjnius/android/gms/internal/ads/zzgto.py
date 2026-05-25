from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzgto"]

class zzgto(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzgto"
    zza = JavaStaticMethod("(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;")
    zzb = JavaStaticMethod("(Ljava/lang/Object;)Lcom/google/android/gms/internal/ads/zzgtn;")