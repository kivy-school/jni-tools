from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbzt"]

class zzbzt(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbzt"
    zzb = JavaStaticMethod("(Landroid/os/IBinder;)Lcom/google/android/gms/internal/ads/zzbzu;")