from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzcz"]

class zzcz(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzcz"
    zze = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;I)Landroid/os/IBinder;")