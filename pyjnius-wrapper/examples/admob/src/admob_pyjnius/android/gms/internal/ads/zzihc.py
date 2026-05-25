from jnius import JavaClass, JavaInterface, MetaJavaClass, JavaMethod, JavaStaticMethod, JavaMultipleMethod, JavaField, JavaStaticField

__all__ = ["zzihc"]

class zzihc(JavaClass, metaclass=MetaJavaClass):
    __javaclass__ = "com/google/android/gms/internal/ads/zzihc"
    __javaconstructor__ = [("(Lcom/google/android/gms/internal/ads/zzifz;)V", False)]
    zza = JavaMethod("()Lcom/google/android/gms/internal/ads/zzifh;")