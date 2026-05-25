from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbes"]

class zzbes(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbes"
    zzb = JavaStaticMethod("(Landroid/os/IBinder;)Lcom/google/android/gms/internal/ads/zzbet;")