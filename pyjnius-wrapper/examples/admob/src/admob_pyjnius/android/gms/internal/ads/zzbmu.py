from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbmu"]

class zzbmu(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbmu"
    zzb = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;)V")
    zzc = JavaMethod("()V")
    zzd = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;)V")