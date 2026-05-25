from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbkh"]

class zzbkh(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbkh"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/lang/Object;I)V", False)]
    zza = JavaStaticMethod("(Ljava/lang/String;Z)Lcom/google/android/gms/internal/ads/zzbkh;")
    zzb = JavaStaticMethod("(Ljava/lang/String;J)Lcom/google/android/gms/internal/ads/zzbkh;")
    zzc = JavaStaticMethod("(Ljava/lang/String;D)Lcom/google/android/gms/internal/ads/zzbkh;")
    zzd = JavaStaticMethod("(Ljava/lang/String;Ljava/lang/String;)Lcom/google/android/gms/internal/ads/zzbkh;")
    zze = JavaMethod("()Ljava/lang/Object;")