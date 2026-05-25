from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzifa"]

class zzifa(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzifa"
    zzc = JavaMethod("(I)J")
    zzd = JavaMethod("(J)V")
    zze = JavaMethod("(IJ)J")
    zzf = JavaMethod("(I)Lcom/google/android/gms/internal/ads/zzifa;")