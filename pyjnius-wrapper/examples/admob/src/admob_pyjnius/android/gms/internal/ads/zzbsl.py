from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbsl"]

class zzbsl(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbsl"
    zzb = JavaMethod("()Lcom/google/android/gms/ads/internal/client/zzea;")
    zzc = JavaMethod("()V")
    zzd = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;Lcom/google/android/gms/internal/ads/zzbso;)V")
    zze = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;)V")
    zzf = JavaMethod("()Lcom/google/android/gms/internal/ads/zzbmi;")