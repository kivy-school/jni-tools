from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbmi"]

class zzbmi(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbmi"
    zze = JavaMethod("()F")
    zzf = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;)V")
    zzg = JavaMethod("()Lcom/google/android/gms/dynamic/IObjectWrapper;")
    zzh = JavaMethod("()F")
    zzi = JavaMethod("()F")
    zzj = JavaMethod("()Lcom/google/android/gms/ads/internal/client/zzea;")
    zzk = JavaMethod("()Z")
    zzl = JavaMethod("()Z")
    zzm = JavaMethod("(Lcom/google/android/gms/internal/ads/zzbnq;)V")