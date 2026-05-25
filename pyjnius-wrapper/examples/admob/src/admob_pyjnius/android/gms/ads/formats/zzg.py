from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzg"]

class zzg(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/ads/formats/zzg"
    zza = JavaMethod("(Lcom/google/android/gms/ads/formats/UnifiedNativeAd;)V")