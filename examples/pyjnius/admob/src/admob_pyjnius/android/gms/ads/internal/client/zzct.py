from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzct"]

class zzct(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzct"
    getLiteSdkVersion = JavaMethod("()Lcom/google/android/gms/ads/internal/client/zzez;")
    getAdapterCreator = JavaMethod("()Lcom/google/android/gms/internal/ads/zzbvj;")