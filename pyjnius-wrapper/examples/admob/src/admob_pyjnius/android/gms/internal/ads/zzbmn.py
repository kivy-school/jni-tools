from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbmn"]

class zzbmn(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbmn"
    zzb = JavaMethod("(Ljava/lang/String;Lcom/google/android/gms/dynamic/IObjectWrapper;)V")
    zzc = JavaMethod("(Ljava/lang/String;)Lcom/google/android/gms/dynamic/IObjectWrapper;")
    zzd = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;)V")
    zze = JavaMethod("()V")
    zzf = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;I)V")
    zzdB = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;)V")
    zzdD = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;)V")
    zzdE = JavaMethod("(Lcom/google/android/gms/internal/ads/zzbmi;)V")
    zzdC = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;)V")