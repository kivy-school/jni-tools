from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbzd"]

class zzbzd(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbzd"
    zzb = JavaStaticMethod("(Landroid/os/IBinder;)Lcom/google/android/gms/internal/ads/zzbze;")