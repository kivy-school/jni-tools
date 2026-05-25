from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbgo"]

class zzbgo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbgo"
    zze = JavaMethod("()Lcom/google/android/gms/ads/internal/client/zzbu;")
    zzf = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;Lcom/google/android/gms/internal/ads/zzbgx;)V")
    zzg = JavaMethod("()Lcom/google/android/gms/ads/internal/client/zzdx;")
    zzh = JavaMethod("(Z)V")
    zzi = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zzdq;)V")
    zzj = JavaMethod("()Ljava/lang/String;")
    zzk = JavaMethod("()J")
    zzl = JavaMethod("(J)V")