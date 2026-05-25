from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzbol"]

class zzbol(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzbol"
    __javaconstructor__ = [("(Lcom/google/android/gms/ads/formats/zzg;)V", False)]
    zze = JavaMethod("(Lcom/google/android/gms/internal/ads/zzboc;)V")