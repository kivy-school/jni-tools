from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzgug"]

class zzgug(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzgug"
    zza = JavaStaticMethod("(Lcom/google/android/gms/internal/ads/zzgtf;)Lcom/google/android/gms/internal/ads/zzgug;")
    zzb = JavaStaticMethod("(Ljava/util/regex/Pattern;)Lcom/google/android/gms/internal/ads/zzgug;")
    zzc = JavaStaticMethod("(I)Lcom/google/android/gms/internal/ads/zzgug;")
    zzd = JavaMethod("()Lcom/google/android/gms/internal/ads/zzgug;")
    zze = JavaMethod("(Lcom/google/android/gms/internal/ads/zzgtf;)Lcom/google/android/gms/internal/ads/zzgug;")
    zzf = JavaMethod("(Ljava/lang/CharSequence;)Ljava/lang/Iterable;")
    zzg = JavaMethod("(Ljava/lang/CharSequence;)Ljava/util/List;")