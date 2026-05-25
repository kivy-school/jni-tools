from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzay"]

class zzay(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzay"
    __javaconstructor__ = [("()V", False)]
    zza = JavaStaticMethod("()Lcom/google/android/gms/ads/internal/util/client/zzf;")
    zzb = JavaStaticMethod("()Lcom/google/android/gms/ads/internal/client/zzaw;")
    zzc = JavaStaticMethod("()V")
    zzd = JavaStaticMethod("()V")
    zze = JavaStaticMethod("()Z")
    zzf = JavaStaticMethod("()Ljava/lang/String;")
    zzg = JavaStaticMethod("()Lcom/google/android/gms/ads/internal/util/client/VersionInfoParcel;")
    zzh = JavaStaticMethod("()Ljava/util/Random;")