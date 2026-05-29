from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzceo"]

class zzceo(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzceo"
    zzb = JavaMethod("(Ljava/lang/String;)V")
    zzc = JavaMethod("(Ljava/lang/String;Ljava/lang/String;Landroid/os/Bundle;)V")