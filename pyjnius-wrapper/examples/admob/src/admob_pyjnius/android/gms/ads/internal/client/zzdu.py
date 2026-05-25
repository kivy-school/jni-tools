from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzdu"]

class zzdu(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/internal/client/zzdu"
    zze = JavaMethod("(Lcom/google/android/gms/dynamic/IObjectWrapper;Lcom/google/android/gms/internal/ads/zzbvj;I)Lcom/google/android/gms/ads/internal/client/zzdt;")