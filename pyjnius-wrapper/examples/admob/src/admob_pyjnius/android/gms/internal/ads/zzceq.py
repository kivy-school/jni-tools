from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzceq"]

class zzceq(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzceq"
    zzb = JavaMethod("(Ljava/lang/String;)V")
    zzc = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Landroid/os/Bundle;)V")