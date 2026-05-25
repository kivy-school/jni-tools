from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbnc"]

class zzbnc(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbnc"
    zze = JavaMethod("(Ljava/lang/String;)Ljava/lang/String;")
    zzf = JavaMethod("(Ljava/lang/String;)Lcom/google/android/gms/internal/ads/zzbml;")
    zzg = JavaMethod("()Ljava/util/List;")
    zzh = JavaMethod("()Ljava/lang/String;")
    zzi = JavaMethod("(Ljava/lang/String;)V")
    zzj = JavaMethod("()V")
    zzk = JavaMethod("()Lcom/google/android/gms/ads/internal/client/zzea;")
    zzl = JavaMethod("()V")
    zzm = JavaMethod("()Lcom/google/android/gms/dynamic/IObjectWrapper;")
    zzn = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;)Z")
    zzo = JavaMethod("()Z")
    zzp = JavaMethod("()Z")
    zzq = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;)V")
    zzr = JavaMethod("()V")
    zzs = JavaMethod("()Lcom/google/android/gms/internal/ads/zzbmi;")
    zzt = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;)Z")