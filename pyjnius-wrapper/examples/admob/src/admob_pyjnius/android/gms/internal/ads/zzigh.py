from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzigh"]

class zzigh(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzigh"
    zzc = JavaMethod("(Lcom/google/android/gms/internal/ads/zzidp;Lcom/google/android/gms/internal/ads/zzidz;)Ljava/lang/Object;")
    zzb = JavaMethod("(Lcom/google/android/gms/internal/ads/zzidl;Lcom/google/android/gms/internal/ads/zzidz;)Ljava/lang/Object;")
    zza = JavaMethod("(Ljava/io/InputStream;Lcom/google/android/gms/internal/ads/zzidz;)Ljava/lang/Object;")