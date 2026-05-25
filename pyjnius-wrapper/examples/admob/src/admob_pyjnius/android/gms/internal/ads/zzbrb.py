from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbrb"]

class zzbrb(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbrb"
    zze = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;Lcom/google/android/gms/internal/ads/zzbvj;ILcom/google/android/gms/internal/ads/zzbqx;)Lcom/google/android/gms/internal/ads/zzbra;")