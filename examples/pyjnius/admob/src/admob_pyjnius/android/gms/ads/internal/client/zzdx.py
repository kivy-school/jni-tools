from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzdx"]

class zzdx(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzdx"
    zze = JavaMethod("()Ljava/lang/String;")
    zzf = JavaMethod("()Ljava/lang/String;")
    zzg = JavaMethod("()Ljava/util/List;")
    zzh = JavaMethod("()Lcom/google/android/gms/ads/internal/client/zzv;")
    zzi = JavaMethod("()Landroid/os/Bundle;")
    zzj = JavaMethod("()Ljava/lang/String;")