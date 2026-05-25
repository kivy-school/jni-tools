from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zziex"]

class zziex(JavaInterface, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zziex"
    zzf = JavaMethod("(I)I")
    zzi = JavaMethod("(I)V")
    zzg = JavaMethod("(II)I")
    zze = JavaMethod("(I)Lcom/google/android/gms/internal/ads/zziex;")