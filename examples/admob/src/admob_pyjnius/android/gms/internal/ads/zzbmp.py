from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbmp"]

class zzbmp(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbmp"
    zzb = JavaMethod("(Ljava/lang/String;Lcom/google/android/gms/dynamic/IObjectWrapper;)V")
    zzc = JavaMethod("(Ljava/lang/String;)Lcom/google/android/gms/dynamic/IObjectWrapper;")
    zzd = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;)V")
    zze = JavaMethod("()V")
    zzf = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;I)V")
    zzdB = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;)V")
    zzdD = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;)V")
    zzdE = JavaMethod("(Lcom/google/android/gms/internal/ads/zzbmi;)V")
    zzdC = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;)V")