from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzx"]

class zzx(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/util/client/zzx"
    __javaconstructor__ = [("()V", False)]
    zza = JavaMethod("()I")
    zzb = JavaMethod("()I")
    zzc = JavaMethod("()D")
    zzd = JavaMethod("()Z")