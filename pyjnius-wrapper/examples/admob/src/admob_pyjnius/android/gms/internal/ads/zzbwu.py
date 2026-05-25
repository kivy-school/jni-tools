from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbwu"]

class zzbwu(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbwu"
    zze = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;)V")
    zzf = JavaMethod("(Ljava/lang/String;)V")
    zzg = JavaMethod("(Lcom/google/android/gms/ads/internal/client/zze;)V")
    zzh = JavaMethod("(Lcom/google/android/gms/internal/ads/zzbvs;)V")