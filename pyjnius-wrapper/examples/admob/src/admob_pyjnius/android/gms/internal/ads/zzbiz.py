from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbiz"]

class zzbiz(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbiz"
    zza = JavaStaticMethod("(Lcom/google/android/gms/internal/ads/zzguj;)Ljava/lang/Object;")