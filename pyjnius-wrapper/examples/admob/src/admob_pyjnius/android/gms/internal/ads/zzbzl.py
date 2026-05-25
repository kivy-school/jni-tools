from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbzl"]

class zzbzl(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbzl"
    zze = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;)Landroid/os/IBinder;")