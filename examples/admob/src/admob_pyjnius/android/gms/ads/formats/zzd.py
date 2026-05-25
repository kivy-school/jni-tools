from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzd"]

class zzd(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/formats/zzd"
    zzc = JavaMethod("(Lcom/google/android/gms/internal/ads/zzbnd;Ljava/lang/String;)V")