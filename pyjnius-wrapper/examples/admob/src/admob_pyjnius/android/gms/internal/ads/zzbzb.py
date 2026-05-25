from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbzb"]

class zzbzb(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbzb"
    zze = JavaMethod("(Landroid/content/Intent;)V")
    zzf = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;Ljava/lang/String;Ljava/lang/String;)V")
    zzg = JavaMethod("()V")
    zzh = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;)V")
    zzi = JavaMethod("([Ljava/lang/String;[ILcom/google/android/gms/dynamic/IObjectWrapper;)V")
    zzj = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;Lcom/google/android/gms/ads/internal/offline/buffering/zza;)V")