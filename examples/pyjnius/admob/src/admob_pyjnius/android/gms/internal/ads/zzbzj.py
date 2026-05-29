from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbzj"]

class zzbzj(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbzj"
    zze = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;)Landroid/os/IBinder;")