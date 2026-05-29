from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zziga"]

class zziga(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zziga"
    zzbw = JavaMethod("()Lcom/google/android/gms/internal/ads/zzifz;")
    zzbi = JavaMethod("()Z")