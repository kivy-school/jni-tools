from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzifs"]

class zzifs(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzifs"
    zza = JavaStaticMethod("(Lcom/google/android/gms/internal/ads/zzihq;Ljava/lang/Object;Lcom/google/android/gms/internal/ads/zzihq;Ljava/lang/Object;)Lcom/google/android/gms/internal/ads/zzifs;")
    zzd = JavaMethod("(ILjava/lang/Object;Ljava/lang/Object;)I")