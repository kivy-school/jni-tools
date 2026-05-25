from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzblt"]

class zzblt(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzblt"
    __javaconstructor__ = [("(Ljava/lang/String;Ljava/util/List;Ljava/lang/Integer;Ljava/lang/Integer;Ljava/lang/Integer;IIZ)V", False)]
    zzb = JavaMethod("()Ljava/lang/String;")
    zzc = JavaMethod("()Ljava/util/List;")
    zzd = JavaMethod("()Ljava/util/List;")
    zze = JavaMethod("()I")
    zzf = JavaMethod("()I")
    zzg = JavaMethod("()I")
    zzh = JavaMethod("()I")
    zzi = JavaMethod("()I")