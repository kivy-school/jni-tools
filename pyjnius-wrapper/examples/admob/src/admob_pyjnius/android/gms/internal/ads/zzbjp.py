from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbjp"]

class zzbjp(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbjp"
    zzb = JavaMethod("()Ljava/lang/String;")
    zzc = JavaMethod("()Ljava/lang/String;")
    zzd = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;)V")
    zze = JavaMethod("()V")
    zzf = JavaMethod("()V")