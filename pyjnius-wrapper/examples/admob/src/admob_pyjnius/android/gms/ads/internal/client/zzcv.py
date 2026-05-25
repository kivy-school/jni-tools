from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzcv"]

class zzcv(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzcv"
    getLiteSdkVersion = JavaMethod("()Lcom/google/android/gms/ads/internal/client/zzez;")
    getAdapterCreator = JavaMethod("()Lcom/google/android/gms/internal/ads/zzbvj;")