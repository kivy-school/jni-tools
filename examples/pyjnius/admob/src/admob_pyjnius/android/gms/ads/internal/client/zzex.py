from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzex"]

class zzex(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzex"
    __javaconstructor__ = [("(Ljava/lang/String;Landroid/os/Bundle;Ljava/lang/String;)V", False)]
    zza = JavaMethod("()Ljava/lang/String;")
    zzb = JavaMethod("()Ljava/lang/String;")
    zzc = JavaMethod("()Landroid/os/Bundle;")