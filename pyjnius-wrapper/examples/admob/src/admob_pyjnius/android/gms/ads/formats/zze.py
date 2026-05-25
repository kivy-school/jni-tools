from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zze"]

class zze(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/formats/zze"
    zzb = JavaMethod("(Lcom/google/android/gms/internal/ads/zzbnd;)V")