from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzc"]

class zzc(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/zzc"
    zza = JavaStaticMethod("(IILjava/lang/String;)Lcom/google/android/gms/ads/AdSize;")
    zzb = JavaStaticMethod("(II)Lcom/google/android/gms/ads/AdSize;")
    zzc = JavaStaticMethod("(II)Lcom/google/android/gms/ads/AdSize;")
    zzd = JavaStaticMethod("(Lcom/google/android/gms/ads/AdSize;)Z")
    zze = JavaStaticMethod("(Lcom/google/android/gms/ads/AdSize;)I")
    zzf = JavaStaticMethod("(Lcom/google/android/gms/ads/AdSize;)Z")
    zzg = JavaStaticMethod("(Lcom/google/android/gms/ads/AdSize;)Z")
    zzh = JavaStaticMethod("(Lcom/google/android/gms/ads/AdSize;)I")
    zzi = JavaStaticMethod("(Lcom/google/android/gms/ads/AdSize;)Z")