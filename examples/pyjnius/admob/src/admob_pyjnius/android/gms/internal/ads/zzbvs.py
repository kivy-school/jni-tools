from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbvs"]

class zzbvs(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbvs"
    zze = JavaMethod("()Lcom/google/android/gms/dynamic/IObjectWrapper;")
    zzf = JavaMethod("()Z")